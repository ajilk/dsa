---
title: Binet's Formula
---

The golden ratio is an irrational mathematical constant:

$$\Large \varphi = \frac{1 + \sqrt{5}}{2} \approx 1.618033988...$$

## Definition

$\varphi$ is the positive solution to the equation $x^2 - x - 1 = 0$:

$$x^2 = x + 1$$

Its conjugate is $\psi = \frac{1 - \sqrt{5}}{2} \approx -0.618$

## Key Properties

**Self-similarity**: $\varphi = 1 + \frac{1}{\varphi}$

**Powers**: $\varphi^n = \varphi^{n-1} + \varphi^{n-2}$ (follows the Fibonacci recurrence)

**Reciprocal**: $\frac{1}{\varphi} = \varphi - 1$

## Binet's Formula

Closed-form solution for linear recurrences with characteristic roots $\varphi$ and $\psi$:

$$\Large a_n = \frac{\varphi^n - \psi^n}{\sqrt{5}}$$

Since $|\psi| < 1$, the $\psi^n$ term vanishes for large $n$:

$$\Large a_n \approx \frac{\varphi^n}{\sqrt{5}}$$

**Derivation**: For recurrence $a_n = a_{n-1} + a_{n-2}$:

- Characteristic equation: $x^2 - x - 1 = 0$
- Roots: $\varphi$ and $\psi$
- General solution: $a_n = A\varphi^n + B\psi^n$
- Constants $A, B$ determined by initial conditions

#### Related Problems

- [509. Fibonacci Number](../leetcode/math/509.mdx)
