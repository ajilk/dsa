---
title: Knapsack
---

## Overview

Knapsack problems involve selecting items with given weights/costs to maximize value or reach a target, subject to capacity constraints.

**Two variants:**

- **0/1 Knapsack**: each item used at most once
- **Unbounded Knapsack**: each item can be used unlimited times

## 0/1 Knapsack

Given `n` items with weights `w[i]` and values `v[i]`, maximize total value without exceeding capacity `W`.

<Callout title="Core Insight" type="idea">
For each item, decide to include it or not. `dp[i][w]` = max value using first `i` items with capacity `w`.
</Callout>

**Recurrence**: `dp[i][w] = max(dp[i-1][w], dp[i-1][w-w[i]] + v[i])`

### 2D Implementation

| Metric | Complexity     | Reason                         |
| ------ | -------------- | ------------------------------ |
| Time   | $O(n \cdot W)$ | Nested loops: items × capacity |
| Space  | $O(n \cdot W)$ | 2D DP table                    |

```python
def knapsack_01(weights: list[int], values: list[int], W: int) -> int:
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])

    return dp[n][W]
```

### Space-Optimized (1D)

| Metric | Complexity     | Reason                         |
| ------ | -------------- | ------------------------------ |
| Time   | $O(n \cdot W)$ | Nested loops: items × capacity |
| Space  | $O(W)$         | Single DP array                |

```python
def knapsack_01_optimized(weights: list[int], values: list[int], W: int) -> int:
    dp = [0] * (W + 1)

    for i in range(len(weights)):
        for w in range(W, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[W]
```

**Key**: Iterate capacity **backwards** to prevent using same item twice.

## Unbounded Knapsack

Each item can be selected unlimited times.

**Recurrence**: `dp[w] = max(dp[w], dp[w-w[i]] + v[i])` for all items

| Metric | Complexity     | Reason                         |
| ------ | -------------- | ------------------------------ |
| Time   | $O(n \cdot W)$ | Nested loops: items × capacity |
| Space  | $O(W)$         | Single DP array                |

```python
def knapsack_unbounded(weights: list[int], values: list[int], W: int) -> int:
    dp = [0] * (W + 1)

    for i in range(len(weights)):
        for w in range(weights[i], W + 1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[W]
```

**Key**: Iterate capacity **forwards** to allow reusing same item.

## Loop Order Comparison

| Variant   | Inner Loop Direction   | Why                      |
| --------- | ---------------------- | ------------------------ |
| 0/1       | `range(W, w[i]-1, -1)` | Backwards prevents reuse |
| Unbounded | `range(w[i], W+1)`     | Forwards allows reuse    |

## Common Variations

| Problem Type         | Approach                             |
| -------------------- | ------------------------------------ |
| Maximize value       | Standard knapsack                    |
| Minimize coins/count | Initialize `dp = [inf]`, use `min()` |
| Count combinations   | Initialize `dp[0] = 1`, use `+=`     |
| Check feasibility    | Use boolean DP                       |

## Related Problems

- [322. Coin Change](../leetcode/dp/322.md) - unbounded knapsack (minimize count)
