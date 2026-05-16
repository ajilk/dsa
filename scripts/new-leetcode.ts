#!/usr/bin/env bun

import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'fs';
import { basename, dirname, extname, join } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const CONTENT_DIR = join(__dirname, '..', 'content', 'docs', 'leetcode');

const args = process.argv.slice(2);
if (args.length === 0 || !args[0].includes('/')) {
  console.error('Usage: bun run new <category>/<number>.md');
  console.error('Example: bun run new array/138.md');
  process.exit(1);
}

const [category, filename] = args[0].split('/');
if (extname(filename) !== '.md') {
  console.error('Error: Filename must have .md extension');
  process.exit(1);
}

const problemNumber = basename(filename, '.md');
const categoryDir = join(CONTENT_DIR, category);
const filePath = join(categoryDir, filename);
const metaPath = join(categoryDir, 'meta.json');

// Create directory if needed
if (!existsSync(categoryDir)) {
  mkdirSync(categoryDir, { recursive: true });
}

// Check if file exists
if (existsSync(filePath)) {
  console.error(`Error: File already exists: ${args[0]}`);
  process.exit(1);
}

// Create file with tabs template
const template = `---
title: ${problemNumber}. Problem Title
---

<Tabs items={['Solution 1', 'Solution 2']}>
<Tab value="Solution 1">
\`\`\`python

\`\`\`
</Tab>
<Tab value="Solution 2">
\`\`\`python

\`\`\`
</Tab>
</Tabs>
`;

writeFileSync(filePath, template, 'utf-8');
console.log(`✓ Created: ${args[0]}`);

// Update meta.json
let meta: { title: string; pages: string[] };
if (existsSync(metaPath)) {
  meta = JSON.parse(readFileSync(metaPath, 'utf-8'));
} else {
  meta = {
    title: category.charAt(0).toUpperCase() + category.slice(1).replace('_', ' '),
    pages: [],
  };
}

if (!meta.pages.includes(problemNumber)) {
  meta.pages.push(problemNumber);
  meta.pages.sort((a, b) => {
    const aNum = parseInt(a);
    const bNum = parseInt(b);
    if (!isNaN(aNum) && !isNaN(bNum)) return aNum - bNum;
    if (!isNaN(aNum)) return -1;
    if (!isNaN(bNum)) return 1;
    return a.localeCompare(b);
  });
}

writeFileSync(metaPath, JSON.stringify(meta, null, 2) + '\n', 'utf-8');
console.log(`✓ Updated: ${category}/meta.json`);
