---
title: Complexity Analysis
description: How to analyze time and space complexity
---

## Big O Notation

Big O describes the **upper bound** of growth rate as input size $n$ approaches infinity. We drop constants and lower-order terms.

| Complexity    | Name         | Example                   |
| ------------- | ------------ | ------------------------- |
| $O(1)$        | Constant     | Array access, hash lookup |
| $O(\log n)$   | Logarithmic  | Binary search             |
| $O(n)$        | Linear       | Single loop               |
| $O(n \log n)$ | Linearithmic | Merge sort, heap sort     |
| $O(n^2)$      | Quadratic    | Nested loops              |
| $O(2^n)$      | Exponential  | Subsets, backtracking     |
| $O(n!)$       | Factorial    | Permutations              |

## Time Complexity

### Single Loop

```python
for i in range(n):  # O(n)
    # O(1) work
```

### Nested Loops

```python
for i in range(n):      # O(n)
    for j in range(n):  # O(n)
        # O(1) work
# Total: O(n^2)
```

**Dependent loops:**

```python
for i in range(n):          # O(n)
    for j in range(i):      # O(i) on average = O(n/2)
        # O(1) work
# Total: O(n^2) — sum of 1+2+...+n = n(n+1)/2
```

### Loop with Multiplicative Step

```python
i = 1
while i < n:
    i *= 2  # doubles each iteration
# Iterations: log₂(n) → O(log n)
```

### Loop with Division

```python
while n > 0:
    n //= 2  # halves each iteration
# Iterations: log₂(n) → O(log n)
```

### Multiple Sequential Loops

```python
for i in range(n):    # O(n)
    pass
for i in range(m):    # O(m)
    pass
# Total: O(n + m)
```

### Recursion

**Linear recursion:**

```python
def f(n):
    if n <= 0:
        return
    f(n - 1)  # single recursive call
# O(n) calls
```

**Binary recursion (divide and conquer):**

```python
def f(n):
    if n <= 1:
        return
    f(n // 2)
    f(n // 2)
# Recurrence: T(n) = 2T(n/2) + O(1)
# By Master Theorem: O(n)
```

**Exponential recursion:**

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
# O(2^n) — two branches at each level
```

### Master Theorem

For recurrences of the form $T(n) = aT(n/b) + O(n^d)$:

| Condition      | Complexity        |
| -------------- | ----------------- |
| $d > \log_b a$ | $O(n^d)$          |
| $d = \log_b a$ | $O(n^d \log n)$   |
| $d < \log_b a$ | $O(n^{\log_b a})$ |

**Common examples:**

| Algorithm     | Recurrence              | Result        |
| ------------- | ----------------------- | ------------- |
| Binary search | $T(n) = T(n/2) + O(1)$  | $O(\log n)$   |
| Merge sort    | $T(n) = 2T(n/2) + O(n)$ | $O(n \log n)$ |
| Karatsuba     | $T(n) = 3T(n/2) + O(n)$ | $O(n^{1.58})$ |

## Space Complexity

**Space complexity = auxiliary space only** (extra space used by the algorithm).

**Exclude:**

- Input space (given to you)
- Output space (required regardless of approach)

### Examples

```python
def sum_array(A):
    total = 0           # O(1) auxiliary
    for v in A:
        total += v
    return total
# Space: O(1)
```

```python
def get_squares(A):
    return [v * v for v in A]  # output array
# Space: O(1) — output doesn't count
```

```python
def merge_sort(A):
    if len(A) <= 1:
        return A
    mid = len(A) // 2
    left = merge_sort(A[:mid])   # creates copy
    right = merge_sort(A[mid:])  # creates copy
    return merge(left, right)
# Space: O(n) — temporary arrays at each level
```

### Recursion Stack Space

Recursive calls use stack space:

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
# Space: O(n) — n stack frames
```

**Tail recursion** (if optimized): $O(1)$ space.

## Data Structure Operations

| Structure      | Access | Search      | Insert      | Delete      |
| -------------- | ------ | ----------- | ----------- | ----------- |
| Array          | $O(1)$ | $O(n)$      | $O(n)$      | $O(n)$      |
| Dynamic Array  | $O(1)$ | $O(n)$      | $O(1)$\*    | $O(n)$      |
| Linked List    | $O(n)$ | $O(n)$      | $O(1)$      | $O(1)$      |
| Hash Table     | —      | $O(1)$\*    | $O(1)$\*    | $O(1)$\*    |
| BST (balanced) | —      | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ |
| Heap           | —      | $O(n)$      | $O(\log n)$ | $O(\log n)$ |

\*Amortized or average case

## Amortized Analysis

**Amortized cost** = average cost per operation over a sequence of operations.

### Dynamic Array (ArrayList)

- Doubling strategy: when full, allocate 2x space and copy
- Single insert can be $O(n)$ (when resizing)
- But $n$ inserts cost $O(n)$ total → $O(1)$ amortized per insert

**Proof:** After $n$ inserts, total copy operations = $1 + 2 + 4 + ... + n < 2n = O(n)$.

### Two-Pointer Patterns

```python
left, right = 0, 0
while right < n:
    # expand window
    right += 1
    while invalid:
        left += 1
# Each pointer moves at most n times
# Total: O(n), not O(n^2)
```

## Common Pitfalls

| Code                        | Appears      | Actually                                      |
| --------------------------- | ------------ | --------------------------------------------- |
| `str += char` in loop       | $O(n)$       | $O(n^2)$ — strings are immutable              |
| `list.insert(0, x)` in loop | $O(n)$       | $O(n^2)$ — shifts all elements                |
| `x in list` in loop         | $O(n)$       | $O(n^2)$ — use set for $O(1)$ lookup          |
| Slicing `A[i:j]`            | $O(1)$       | $O(j-i)$ — creates copy                       |
| `list.sort()` / `sorted()`  | $O(1)$ space | $O(n)$ space — Timsort uses auxiliary storage |

## Quick Reference

**Identify the pattern:**

| Pattern                | Time          |
| ---------------------- | ------------- |
| Fixed iterations       | $O(1)$        |
| Halving/doubling       | $O(\log n)$   |
| Single pass            | $O(n)$        |
| Sort then process      | $O(n \log n)$ |
| Nested dependent loops | $O(n^2)$      |
| All pairs              | $O(n^2)$      |
| All subsets            | $O(2^n)$      |
| All permutations       | $O(n!)$       |
