---
title: Naming Convention
---

Maintaining a consistent naming system is key to optimizing solving time. Some benefits include:

- reduced overhead
- reduced confusion
- chunking

Below is the naming convention I use for commonly used variables

- e.g. I always call my arrays/lists, A, 99% of the time so I never have to think about what my array is called because it will always, most certainly, be A.

|           variable name | description                                       |
| ----------------------: | :------------------------------------------------ |
|                     `A` | array                                             |
|              `A1`, `A2` | multiple arrays in function definition            |
|        `I`, `intervals` | intervals                                         |
|                     `v` | value in an array                                 |
|             `n`, `size` | array size                                        |
|              `n1`, `n2` | sizes of `A1`, `A2` respectively                  |
|              `i1`, `i2` | indices into `A1`, `A2` respectively              |
|                     `M` | matrix                                            |
|                     `m` | number of row in a matrix                         |
|                     `n` | number of columns in a matrix                     |
|                `i`, `j` | indices to element `M[i][j]`                      |
|                `y`, `x` | indices to element `M[y][x]`                      |
|              `ii`, `jj` | neighbors of `(i, j)`                             |
|              `dy`, `dx` | change in `y` and change in `x`                   |
|                     `#` | character used to mark visited elements in matrix |
|               `offsets` | stores changes in (dy, dx)                        |
|                     `G` | graph                                             |
|                     `D` | distances array (shortest path)                   |
|                     `W` | weights array (weighted graphs)                   |
|                `a`, `b` | edge a and b                                      |
|                   `nei` | neighbor of a graph node                          |
|                     `q` | queue                                             |
|             `heap`, `h` | heap                                              |
|               `d`, `hm` | dictionary                                        |
|                 `stack` | stack                                             |
|                `window` | current sliding window elements                   |
|         `left`, `right` | left and right pointers                           |
|                   `mid` | middle                                            |
|      `prefix`, `suffix` | prefix/suffix sum/product or values               |
|    `max_sum`, `cur_sum` | maximum sum, current sum (e.g., Kadane's)         |
| `head`, `tail`, `dummy` | pointer to a list node                            |
|                   `tmp` | temporary variable                                |
|                     `c` | character in string                               |
|                `s`, `e` | start, end                                        |
|              `ps`, `pe` | previous start, previous end                      |
|          `slow`, `fast` | slow, fast pointers                               |
|                   `pre` | previous list node                                |
|                   `cur` | current list node                                 |
|                   `nxt` | next list node                                    |
|        `p`, `q`, `node` | pointer to tree nodes                             |
|                    `uf` | union find                                        |
|               `visited` | visited elements                                  |
|                  `seen` | seen elements                                     |
|                  `have` | elements that are available for use               |
|   `dp`, `cache`, `memo` | dynamic programming, caching computed values      |
|      `helper()`, `fn()` | helper functions                                  |
|        `dfs()`, `bfs()` | depth/breadth first search                        |
|        `dft()`, `bft()` | depth/breadth first traversal                     |
|   `bt()`, `backtrack()` | backtrack                                         |
|                `result` | result                                            |
