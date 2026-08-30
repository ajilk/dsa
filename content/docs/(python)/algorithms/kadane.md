---
title: Kadane's Algorithm
---

## Overview

Kadane's Algorithm is an efficient dynamic programming algorithm used to find the maximum sum of a contiguous subarray within a one-dimensional array of numbers.

<Callout title="Core Insight" type="idea">
At each position, decide whether to extend the current subarray or start a new one from the current element.
</Callout>

## Algorithm Steps

1. Initialize `max_sum` and `cur_sum` to `-inf`
2. For each value `v` in the array:
   - `cur_sum = max(cur_sum + v, v)` (extend or start new)
   - `max_sum = max(max_sum, cur_sum)` (track global maximum)
3. Return `max_sum`

## Complexity

| Metric           | Complexity | Reason                          |
| ---------------- | ---------- | ------------------------------- |
| Time Complexity  | $O(n)$     | Single pass through array       |
| Space Complexity | $O(1)$     | Only tracks current and max sum |

## Implementation

```python
def kadane(A: list[int]) -> int:
    max_sum = cur_sum = -inf

    for v in A:
        cur_sum = max(cur_sum + v, v)
        max_sum = max(max_sum, cur_sum)

    return max_sum
```

## Example

```python
A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# Walk through:
# v = -2: cur_sum = max(-inf + -2, -2) = -2, max_sum = -2
# v =  1: cur_sum = max(-2 + 1, 1)     =  1, max_sum =  1
# v = -3: cur_sum = max(1 + -3, -3)    = -2, max_sum =  1
# v =  4: cur_sum = max(-2 + 4, 4)     =  4, max_sum =  4
# v = -1: cur_sum = max(4 + -1, -1)    =  3, max_sum =  4
# v =  2: cur_sum = max(3 + 2, 2)      =  5, max_sum =  5
# v =  1: cur_sum = max(5 + 1, 1)      =  6, max_sum =  6
# v = -5: cur_sum = max(6 + -5, -5)    =  1, max_sum =  6
# v =  4: cur_sum = max(1 + 4, 4)      =  5, max_sum =  6

result = kadane(A)  # Returns 6, subarray [4, -1, 2, 1]
```

## Key Points

- Greedy/DP approach: at each element, choose to extend or restart
- Initializing with `-inf` handles empty subarrays and all-negative arrays
- Works in a single pass with no auxiliary data structures
- Can be modified to track subarray indices by recording start/end when `max_sum` updates

## Related Problems

- [Maximum Subarray](../leetcode/dp/53.md)
- [Maximum Product Subarray](../leetcode/dp/152.md)
