---
title: Singly Linked List
---

```python
class Node:
    def __init__(self, key: int = None, value: int = None):
        self.key = key
        self.value = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = Node()

    def insert(self, node: Node) -> None:
        pre, nxt = self.head, self.head.next
        node.next = nxt
        pre.next = node

    def remove(self, pre: Node) -> Optional[int]:
        if pre.next is None:
            return None
        node = pre.next
        pre.next = node.next
        return node.key

    def last(self) -> Optional[Node]:
        node = self.head
        while node.next is not None:
            node = node.next
        return node if node != self.head else None

```
