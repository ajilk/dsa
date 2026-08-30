---
title: Trie
---

```python
class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        d = self.trie
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d["."] = "."

    def end(self, s: str) -> Optional[Dict[str, Dict]]:
        d = self.trie
        for c in s:
            if c not in d:
                return None
            d = d[c]
        return d

    def search(self, word: str) -> bool:
        d = self.end(word)
        return d is not None and "." in d

    def startsWith(self, prefix: str) -> bool:
        d = self.end(prefix)
        return d is not None

```

![trie diagram](/assets/208.svg)
