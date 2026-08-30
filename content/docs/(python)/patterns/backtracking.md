---
title: Backtracking
---

```python
result = []

def bt(i: int, path: List) -> None:
    # base case: check terminal state
    if i == n:
        result.append(path[:])  # or path.copy()
        return

    # explore choices
    for choice in choices:
        # make choice
        path.append(choice)

        # recurse
        backtrack(i + 1, path)

        # undo choice (backtrack)
        path.pop()

bt(0, [])
```
