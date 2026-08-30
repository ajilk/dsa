---
title: Kahn's Algorithm
---

## Overview

Kahn's Algorithm performs topological sorting on a Directed Acyclic Graph (DAG) using a BFS-based approach. It processes nodes with no incoming edges first, gradually removing edges to reveal more processable nodes.

**Topological Sort**: A linear ordering of vertices where for every directed edge $(u, v)$, vertex $u$ comes before $v$ in the ordering. Only possible for DAGs.

## Algorithm Steps

1. Calculate in-degree (number of incoming edges) for each vertex
2. Add all vertices with in-degree 0 to a queue
3. While queue is not empty:
   - Remove a vertex from queue and add to result
   - For each neighbor of this vertex:
     - Decrease its in-degree by 1
     - If in-degree becomes 0, add to queue
4. If result contains all vertices, return it; otherwise, graph has a cycle

## Complexity

| Metric           | Complexity | Reason                           |
| ---------------- | ---------- | -------------------------------- |
| Time Complexity  | $O(V + E)$ | Visits each vertex and edge once |
| Space Complexity | $O(V)$     | In-degree array and queue        |

Where V = number of vertices, E = number of edges

## Implementation

```python
from collections import deque

def kahn_topological_sort(n: int, edges: list[list[int]]) -> list[int]:
    """
    n: number of vertices (0 to n-1)
    edges: list of directed edges [u, v] where u -> v
    Returns: topological ordering, or [] if cycle exists
    """
    # Build adjacency list and in-degree array
    G = [[] for _ in range(n)]
    in_degree = [0] * n

    for a, b in edges:
        G[a].append(b)
        in_degree[b] += 1

    # Initialize queue with nodes having in-degree 0
    q = deque([i for i in range(n) if in_degree[i] == 0])
    result = []

    while q:
        node = q.popleft()
        result.append(node)

        # Reduce in-degree for neighbors
        for nei in G[node]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                q.append(nei)

    # Check if all nodes were processed (no cycle)
    return result if len(result) == n else []
```

## Example

```python
# Graph: 0 -> 1 -> 3
#        0 -> 2 -> 3
n = 4
edges = [
    [0, 1],
    [0, 2],
    [1, 3],
    [2, 3]
]

result = kahn_topological_sort(n, edges)
# result = [0, 1, 2, 3] or [0, 2, 1, 3]
# Both are valid topological orderings

# Graph with cycle
edges_cycle = [[0, 1], [1, 2], [2, 0]]
result = kahn_topological_sort(3, edges_cycle)
# result = [] (cycle detected)
```

## Cycle Detection

If the algorithm processes fewer than $n$ vertices, the graph contains a cycle. This happens when remaining vertices all have non-zero in-degree (circular dependency).

```python
def has_cycle(n: int, edges: list[list[int]]) -> bool:
    result = kahn_topological_sort(n, edges)
    return len(result) != n
```

## Key Points

- BFS-based approach for topological sorting
- Detects cycles: returns empty list if cycle exists
- Multiple valid orderings may exist for a DAG
- Useful for task scheduling, course prerequisites, build systems
- Alternative: DFS-based topological sort (post-order traversal)
- In-degree tracks number of dependencies for each node

## Related Problems

- [269. Alien Dictionary](../leetcode/graph/269.mdx)
