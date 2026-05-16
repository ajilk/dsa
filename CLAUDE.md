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
bun types:check      # Type check (runs fumadocs-mdx, next typegen, tsc)

# Create new LeetCode solution
bun run new <category>/<number>.md   # e.g., bun run new array/138.md

# Fetch LeetCode problem details
python3 scripts/fetch-leetcode.py <query>   # query: number, slug, or URL
```

## Architecture

- **Content**: MDX files in `content/docs/` organized by topic (algorithms, data_structures, leetcode, patterns, misc)
- **Source config**: `source.config.ts` - Fumadocs MDX configuration with KaTeX math support
- **App**: Next.js app router in `src/app/` with catch-all route for docs

### LeetCode Solutions Structure

Solutions live in `content/docs/leetcode/<category>/<number>.md`. Each category has a `meta.json` that lists pages in order. The `bun run new` script creates the file and updates `meta.json` automatically.

### MDX Features

- Math equations via remark-math/rehype-katex
- Mermaid diagrams via custom component (`src/components/mermaid.tsx`)
- Tabs component for multiple solutions

## Naming Conventions for Solutions

When writing LeetCode solutions, follow `content/docs/naming.md`:
- `A` for arrays, `M` for matrices, `G` for graphs
- `i`, `j` for indices; `y`, `x` for matrix coordinates
- `left`, `right` for two pointers; `slow`, `fast` for fast/slow pointers
- `dp`, `cache`, `memo` for dynamic programming
- `dfs()`, `bfs()` for traversals; `bt()` for backtracking
