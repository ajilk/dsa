---
title: Fenwick Trees
---

```python
class FenwickTree:
    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 1)

    def add(self, i: int, v: int) -> None:
        while i <= self.size:
            self.tree[i] += v
            i = i + (i & -i)

    def sum(self, i: int) -> int:
        total = 0
        while i > 0:
            total += self.tree[i]
            i = i - (i & -i)
        return total

    def range_sum(self, left: int, right: int) -> int:
        return self.sum(right) - self.sum(left - 1)

```
