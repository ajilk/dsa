---
title: Tips & Tricks
---

### `isslice(iterator, start, end)`

to slice iterators

```python
def values(n: int) -> Iterator[int]:
    for i in range(n):
        yield i

islice(values(100), 20, 31) # -> [20, 21, 22, ..., 30]
```

### Negative Indexing

`A[-k:] == A[n - k:]` where `n = len(A)`

```python
A = [1, 2, 3, 4, 5]  # k = 2
A[-2:]              # [4, 5] (last 2)
A[:-2]              # [1, 2, 3] (all except last 2)
A[-2:] + A[:-2]     # [4, 5, 1, 2, 3] (rotate right by 2)
```
