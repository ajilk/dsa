---
title: Inverse Ackermann Function
---

## Overview

The inverse Ackermann function, denoted as $\alpha(n)$, is an extremely slowly growing function that appears in the analysis of algorithms, most notably in the amortized time complexity of [Union Find](../data_structures/uf.mdx) operations.

## Definition

$\alpha(n)$ is the inverse of the Ackermann function $A(n,n)$. It can be informally defined as:

$$\alpha(n) = \min\{k : A(k, k) \geq n\}$$

Where $A(k, k)$ is the Ackermann function, which grows extraordinarily fast.

## Growth Rate

The inverse Ackermann function grows so slowly that for all practical values of $n$:

| $n$                           | $\alpha(n)$ |
| ----------------------------- | ----------- |
| $10^{80}$ (atoms in universe) | $\leq 4$    |
| $2^{65536}$                   | $5$         |

For any input size encountered in practice, $\alpha(n) \leq 4$, making it effectively constant.

## Applications in Computer Science

### Union Find Data Structure

The most common appearance of $\alpha(n)$ is in the amortized time complexity of Union Find operations with path compression and union by rank:

- **Find**: $O(\alpha(n))$ amortized
- **Union**: $O(\alpha(n))$ amortized

This makes Union Find operations "almost constant time" for practical purposes.

### Other Algorithms

- **Tarjan's off-line least common ancestors algorithm**: $O(\alpha(n))$ per query
- **Minimum spanning tree algorithms** (Kruskal's, Prim's with specific implementations)

## Why It Matters

Although $\alpha(n)$ is not truly constant ($O(1)$), it's so close that:

1. For competitive programming, treat it as constant time
2. The theoretical distinction matters for algorithmic analysis
3. It represents the best achievable bound for certain problems (e.g., Union Find operations)

## Key Points

- Effectively constant for all practical input sizes
- Always $\leq 4$ for realistic problem constraints
- Represents nearly optimal performance in Union Find
- Can be treated as $O(1)$ in competitive programming analysis
- Arises from highly optimized data structures using path compression
