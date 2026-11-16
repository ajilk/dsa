---
title: Snippets
---

## itertools

### `batched(iterable, n)`

split an iterable into chunks of size `n` (python 3.12+)

```python
from itertools import batched

list(batched("ABCDEFG", 3))  # [('A', 'B', 'C'), ('D', 'E', 'F'), ('G',)]
list(batched(A, 2))          # pair up consecutive elements
```

- yields tuples, not lists
- last batch may be shorter; `strict=True` (3.13+) raises `ValueError` instead
- pre-3.12 fallback: `[A[i : i + k] for i in range(0, n, k)]`

### `islice(iterator, start, end)`

to slice iterators

```python
from itertools import islice

def values(n: int) -> Iterator[int]:
    for i in range(n):
        yield i

islice(values(100), 20, 31) # -> [20, 21, 22, ..., 30]
```

## indexing & slicing

### Negative Indexing

`A[-k:] == A[n - k:]` where `n = len(A)`

```python
A = [1, 2, 3, 4, 5]  # k = 2
A[-2:]              # [4, 5] (last 2)
A[:-2]              # [1, 2, 3] (all except last 2)
A[-2:] + A[:-2]     # [4, 5, 1, 2, 3] (rotate right by 2)
```
