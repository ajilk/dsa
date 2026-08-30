# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Data Structures & Algorithms documentation site built with Fumadocs (Next.js-based documentation framework). Contains LeetCode solutions, data structures, algorithms, and patterns documentation.

## Commands

```bash
# Development
bun dev              # Start dev server
bun build            # Production build
bun lint             # Run ESLint
bun format           # Format with Prettier
bun format:check     # Check formatting
bun types:check      # Type check (runs fumadocs-mdx, next typegen, tsc)
bun clean            # Remove .next, .source, out
```

## Architecture

- **Content**: MDX files in `content/docs/`, split into root-toggle sections by language — `content/docs/(python)/` (algorithms, data_structures, leetcode, patterns, misc) and `content/docs/cpp/` (competitive programming, WIP)
- **Source config**: `source.config.ts` - Fumadocs MDX configuration with KaTeX math support
- **App**: Next.js app router in `src/app/` with a single catch-all route `[[...slug]]/page.tsx` serving all docs pages
- **Source loader**: `src/lib/source.ts` - wraps Fumadocs source API; `source.pageTree` drives the sidebar, `source.getPage()` resolves pages

### Build pipeline

`bun types:check` runs three steps in sequence: `fumadocs-mdx` (scans `content/docs/` and emits type stubs into `.source/`), `next typegen` (generates route-level types), then `tsc --noEmit`. The `.source/` directory must exist before TypeScript runs — `postinstall` handles this on fresh installs.

### LeetCode Solutions Structure

Solutions live in `content/docs/(python)/leetcode/<category>/<number>.md`. Each category has a `meta.json` that controls sidebar order. When adding a new solution:

1. Create `content/docs/(python)/leetcode/<category>/<number>.md`
2. Add the number (without extension) to the `pages` array in that category's `meta.json`

Standard solution format:

```md
---
title: <number>. <Problem Name>
---

\`\`\`python
class Solution:
def method(self, A: List[int], ...) -> ...:
...
\`\`\`

| Metric           | Complexity | Reason |
| ---------------- | ---------- | ------ |
| Time Complexity  | $O(n)$     | ...    |
| Space Complexity | $O(n)$     | ...    |
```

### MDX Features

- Math equations via remark-math/rehype-katex (inline: `$O(n)$`, block: `$$...$$`)
- Mermaid diagrams via `<Mermaid chart="..." />` (`src/components/mermaid.tsx`)
- `<Tabs>` / `<Tab>` components for multiple solutions (from fumadocs-ui)

## Naming Conventions for Solutions

See @content/docs/(python)/naming.md for the full variable naming table.
