---
title: Segment Trees
---

```python
class TreeNode:
    def __init__(self, value: int, start: int, end: int, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.value = value
        self.start = start
        self.end = end
        self.left = left
        self.right = right

class SegmentTree:
    def __init__(self, values: List[int]):
        self.values = values
        self.root = self.build(0, len(values) - 1)

    def build(self, start: int, end: int) -> TreeNode:
        if start == end:
            return TreeNode(self.values[start], start, end)
        left = self.build(start, (start + end) // 2)
        right = self.build((start + end) // 2 + 1, end)
        return TreeNode(left.value + right.value, start, end, left, right)

    def update(self, root: TreeNode, idx: int, value: int) -> int:
        if root.start == root.end and idx == root.start:
            root.value = value
            return value
        if root.start > idx or root.end < idx:
            return root.value

        mid = (root.start + root.end) // 2
        if idx <= mid:
            self.update(root.left, idx, value)
        else:
            self.update(root.right, idx, value)

        root.value = root.left.value + root.right.value
        return root.value

    def query(self, root: TreeNode, left: int, right: int) -> int:
        if root.start > right or root.end < left:
            return 0
        if left <= root.start <= root.end <= right:
            return root.value
        return self.query(root.left, left, right) + self.query(root.right, left, right

```
