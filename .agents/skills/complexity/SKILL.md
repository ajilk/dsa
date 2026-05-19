---
argument-hint: '[code]'
description: Analyze time and space complexity of code. Use when asked about Big O, time complexity, space complexity, or to analyze algorithm performance.
---

Analyze the provided code and determine its time and space complexity.

## Reference Guide

Read `content/docs/misc/complexity.md` for detailed complexity analysis rules.

## Key Rules

### Space Complexity

- **Auxiliary space only** — exclude input and output space
- Count recursion stack frames
- Mutable input modifications = O(1) space

### Time Complexity Patterns

| Pattern                          | Complexity |
| -------------------------------- | ---------- |
| Fixed iterations                 | O(1)       |
| Halving/doubling (binary search) | O(log n)   |
| Single pass                      | O(n)       |
| Sort + process                   | O(n log n) |
| Nested loops (n × n)             | O(n²)      |
| All subsets                      | O(2ⁿ)      |
| All permutations                 | O(n!)      |

### Common Pitfalls

- `str += char` in Python loop → O(n²) not O(n)
- `list.insert(0, x)` in loop → O(n²)
- `x in list` in loop → O(n²) — use set
- Slicing `A[i:j]` → O(j-i) not O(1)
- **Python `list.sort()` / `sorted()`** → O(n) space, not O(1) (Timsort uses auxiliary space for merging)

### Recursion Analysis

Use Master Theorem for T(n) = aT(n/b) + O(n^d):

- d > log_b(a) → O(n^d)
- d = log_b(a) → O(n^d log n)
- d < log_b(a) → O(n^(log_b a))

## Output Format

Provide analysis in this table format:

| Metric | Complexity | Explanation                                      |
| ------ | ---------- | ------------------------------------------------ |
| Time   | O(?)       | Brief reason explaining the dominant factor      |
| Space  | O(?)       | Auxiliary space only — what extra memory is used |

### Additional Notes (if applicable)

- Best/average/worst case if they differ significantly
- Amortized complexity if relevant (e.g., dynamic arrays)
- Any assumptions about input or operations
