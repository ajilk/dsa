---
title: Kruskal's Algorithm
---

## Overview

Kruskal's Algorithm is a greedy algorithm that finds a Minimum Spanning Tree (MST) for a weighted undirected graph. It builds the MST by selecting edges in increasing order of weight, ensuring no cycles are formed.

**Minimum Spanning Tree (MST)**: A subset of edges that connects all vertices with the minimum total edge weight and contains no cycles. An MST has exactly `V-1` edges for a graph with `V` vertices.

## Algorithm Steps

1. Sort all edges by weight in ascending order
2. Initialize a Union-Find data structure for cycle detection
3. For each edge in sorted order:
   - If connecting the edge doesn't create a cycle, add it to MST
   - Otherwise, skip the edge
4. Continue until MST has `V-1` edges (where V is number of vertices)

## Complexity

| Metric           | Complexity    | Reason                     |
| ---------------- | ------------- | -------------------------- |
| Time Complexity  | $O(E \log E)$ | Dominated by sorting edges |
| Space Complexity | $O(V)$        | Union-Find structure       |

Where E = number of edges, V = number of vertices

## Implementation

Uses [Union Find](../data_structures/uf.mdx) for cycle detection.

```python
def kruskal(n: int, edges: list[list[int]]) -> tuple[int, list[tuple[int, int, int]]]:
    """
    n: number of vertices (0 to n-1)
    edges: list of [weight, u, v]
    Returns: (mst_weight, mst_edges)
    """
    edges.sort()  # Sort by weight
    uf = UnionFind(n)
    mst_weight = 0
    mst_edges = []

    for weight, u, v in edges:
        if uf.union(u, v):
            mst_weight += weight
            mst_edges.append((u, v, weight))
            if len(mst_edges) == n - 1:
                break

    return mst_weight, mst_edges
```

## Example

```python
# Graph with 4 vertices
n = 4
edges = [
    [1, 0, 1],  # weight=1, edge 0-1
    [2, 1, 2],  # weight=2, edge 1-2
    [3, 2, 3],  # weight=3, edge 2-3
    [4, 0, 2],  # weight=4, edge 0-2
    [5, 1, 3],  # weight=5, edge 1-3
]

weight, mst = kruskal(n, edges)
# weight = 6
# mst = [(0, 1, 1), (1, 2, 2), (2, 3, 3)]
```

## Key Points

- Greedy approach: always choose minimum weight edge that doesn't create cycle
- Requires sorting edges first
- Uses Union-Find for efficient cycle detection
- Works on disconnected graphs (produces Minimum Spanning Forest)
- Efficient for sparse graphs (fewer edges)
