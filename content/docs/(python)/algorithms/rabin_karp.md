---
title: Rabin-Karp Algorithm
---

## Overview

Rabin-Karp is a string matching algorithm that uses hashing to find pattern
occurrences in text. Instead of comparing characters directly, it compares
hash values of the pattern with hash values of text substrings.

<Callout title="Core Insight" type="idea">
Use a rolling hash to efficiently compute hash values of consecutive substrings in O(1) time, avoiding O(m) recomputation at each position.
</Callout>

## Algorithm Steps

1. Compute hash of pattern
2. Compute hash of first window (first m characters of text)
3. Slide the window across text:
   - If hashes match: verify with character-by-character comparison (avoid false positives)
   - Use rolling hash to update window hash in O(1)

### Rolling Hash Formula

Using polynomial rolling hash with base `d` and modulus `q`:

- Initial: `hash = (c[0]*d^(m-1) + c[1]*d^(m-2) + ... + c[m-1]) % q`
- Roll: `new_hash = ((old_hash - c[old]*d^(m-1)) * d + c[new]) % q`

## Complexity

| Metric           | Complexity | Reason                                         |
| ---------------- | ---------- | ---------------------------------------------- |
| Time Complexity  | $O(n + m)$ | Average case; O(nm) worst case with collisions |
| Space Complexity | $O(1)$     | Only stores hash values and pointers           |

Where n = length of text, m = length of pattern

## Implementation

```python
def rabin_karp(text: str, pattern: str) -> list[int]:
    n, m = len(text), len(pattern)
    if m > n:
        return []

    d = 256
    q = 101
    h = pow(d, m - 1, q)

    p_hash = 0
    t_hash = 0
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    result = []
    for i in range(n - m + 1):
        if p_hash == t_hash:
            if text[i:i + m] == pattern:
                result.append(i)

        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            if t_hash < 0:
                t_hash += q

    return result
```

## Example

```python
text = "ABABDABABC"
pattern = "ABAB"
result = rabin_karp(text, pattern)
```

With d=256, q=101, m=4:

- Pattern hash: computed once
- Window slides: hash updated in O(1) using rolling formula
- Hash match at i=0: verify "ABAB" == "ABAB" ✓
- Hash match at i=5: verify "ABAB" == "ABAB" ✓
- Result: [0, 5]

## Key Points

- **When to use**: Multiple pattern search, plagiarism detection, finding repeated substrings
- **Hash collisions**: Always verify matches with direct comparison
- **Choice of q**: Use prime number to reduce collisions
- **Choice of d**: Typically 256 (ASCII) or alphabet size
- **vs KMP**: Rabin-Karp better for multiple patterns; KMP guarantees O(n+m)
- **Variants**: Can search multiple patterns simultaneously by storing pattern hashes in a set

## Related Problems

- [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)
- [187. Repeated DNA Sequences](https://leetcode.com/problems/repeated-dna-sequences/)
- [1044. Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/)
