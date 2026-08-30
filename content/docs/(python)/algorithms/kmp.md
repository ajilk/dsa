---
title: KMP Algorithm
---

## Overview

KMP (Knuth-Morris-Pratt) is an efficient string matching algorithm that finds
occurrences of a pattern in a text in linear time. Unlike naive matching which
restarts from scratch after each mismatch, KMP uses information about previously
matched characters to skip redundant comparisons.

<Callout title="Core Insight" type="idea">
When a mismatch occurs after matching some characters, the pattern itself contains enough information to determine where the next match could begin, avoiding re-examination of previously matched characters.
</Callout>

## Algorithm Steps

### Phase 1: Build LPS Array

The LPS (Longest Proper Prefix which is also Suffix) array stores, for each
position in the pattern, the length of the longest proper prefix that matches
a suffix.

1. Initialize `lps[0] = 0` (no proper prefix for single character)
2. Use two pointers: `length` (length of previous longest prefix-suffix), `i` (current position)
3. For each position `i` from 1 to m-1:
   - If `pattern[i] == pattern[length]`: extend the match, `lps[i] = length + 1`, increment both
   - Else if `length > 0`: fall back to `lps[length - 1]` and retry
   - Else: `lps[i] = 0`, move to next position

### Phase 2: Pattern Matching

1. Use two pointers: `i` for text, `j` for pattern
2. While `i < len(text)`:
   - If characters match: increment both `i` and `j`
   - If `j == len(pattern)`: found match at index `i - j`, use LPS to continue
   - Else if mismatch:
     - If `j > 0`: use LPS to skip (`j = lps[j - 1]`)
     - Else: increment `i`

## Complexity

| Metric           | Complexity | Reason                              |
| ---------------- | ---------- | ----------------------------------- |
| Time Complexity  | $O(n + m)$ | LPS built in O(m), matching in O(n) |
| Space Complexity | $O(m)$     | LPS array stores m values           |

Where n = length of text, m = length of pattern

## Implementation

```python
def build_lps(pattern: str) -> list[int]:
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    return lps


def kmp_search(text: str, pattern: str) -> list[int]:
    n, m = len(text), len(pattern)
    if m == 0:
        return []

    lps = build_lps(pattern)
    result = []
    i = j = 0

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == m:
                result.append(i - j)
                j = lps[j - 1]
        elif j > 0:
            j = lps[j - 1]
        else:
            i += 1

    return result
```

## Example

### LPS Construction for pattern "ABABC"

```python
pattern = "ABABC"
lps = [0, 0, 1, 2, 0]
```

| i   | char | compare with | result              | lps[i] |
| --- | ---- | ------------ | ------------------- | ------ |
| 0   | A    | -            | -                   | 0      |
| 1   | B    | A            | ≠                   | 0      |
| 2   | A    | A            | =                   | 1      |
| 3   | B    | B            | =                   | 2      |
| 4   | C    | A            | ≠, fallback to 0, ≠ | 0      |

- `lps[2]=1`: "A" is both prefix and suffix of "ABA"
- `lps[3]=2`: "AB" is both prefix and suffix of "ABAB"

### Pattern Matching

```python
text = "ABABDABABC"
pattern = "ABABC"
lps = [0, 0, 1, 2, 0]

result = kmp_search(text, pattern)
```

| i   | j   | text[i] | pattern[j] | action                             |
| --- | --- | ------- | ---------- | ---------------------------------- |
| 0   | 0   | A       | A          | match, i=1, j=1                    |
| 1   | 1   | B       | B          | match, i=2, j=2                    |
| 2   | 2   | A       | A          | match, i=3, j=3                    |
| 3   | 3   | B       | B          | match, i=4, j=4                    |
| 4   | 4   | D       | C          | mismatch, j=lps[3]=2               |
| 4   | 2   | D       | A          | mismatch, j=lps[1]=0               |
| 4   | 0   | D       | A          | mismatch, i=5                      |
| 5   | 0   | A       | A          | match, continue...                 |
| ... |     |         |            | match found at i=10, j=5 → index 5 |

## Key Points

- **When to use KMP**: Large texts, long patterns, or repeated searches with same pattern
- **Python's `find()`**: Often sufficient for small patterns (≤10 chars); uses optimized C implementation
- **LPS intuition**: Tells us "if we've matched j characters and fail, we've actually matched lps[j-1] characters of a potential new match"
- **Variants**: Can be adapted to count occurrences, find all matches, or check if pattern exists
- **Alternative algorithms**: Rabin-Karp (rolling hash), Boyer-Moore (skip from end), Z-algorithm

## Related Problems

- [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)
- [214. Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/)
- [3006. Find Beautiful Indices in the Given Array I](https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/)
