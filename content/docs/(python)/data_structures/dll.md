---
title: Doubly Linked List
---

```python
class Node:
    def __init__(self, key: int = None, value: int = None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node: Node) -> None:
        pre, nxt = self.head, self.head.next
        node.prev = pre
        node.next = nxt
        pre.next = node
        nxt.prev = node

    def remove(self, node: Node) -> int:
        pre, nxt = node.prev, node.next
        pre.next = nxt
        nxt.prev = pre
        return node.key

    def last(self) -> Optional[Node]:
        pre = self.tail.prev
        return pre if pre != self.head else None

```
