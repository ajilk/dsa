---
title: Breadth First Traversal
---

```python
def bft(root: TreeNode) -> List[int]:
    q = deque([root])
    result = []

    while q:
        count = len(q)
        level = []

        for _ in range(count):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.append(level)

    return result

```
