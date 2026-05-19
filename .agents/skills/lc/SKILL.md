---
argument-hint: '[question/code/link]'
description: solve lc problems in python.
allowed-tools: Bash, Read, WebFetch, WebSearch
---

Solve the LeetCode problem following these requirements:

1. **Language**: Python 3 only (use type hints)
2. **Code format**: LeetCode class-based solution followed by a complexity table
3. **Naming**: Read `content/docs/naming.md` and silently apply every convention to all variable and function names — do not narrate or list which conventions were used
4. **Assumptions**: All necessary imports are available

## Fetching Questions

**If the question is unclear, not provided, or only a problem number/name/URL is given:**

1. **First, try the LeetCode fetcher script:**

   ```bash
   bash ${CLAUDE_SKILL_DIR}/retrieve.sh <query>
   ```

   - Works with question number (e.g., `1`, `42`)
   - Works with title slug (e.g., `two-sum`)
   - Works with URL (e.g., `https://leetcode.com/problems/two-sum/`)

2. **Parse the JSON output** to extract:
   - `title` - Problem title
   - `content` - Problem description (HTML, can be parsed naturally)
   - `difficulty` - Easy/Medium/Hard
   - `codeSnippets` - Find the Python3 template
   - `hints` - Official hints (if needed)
   - `exampleTestcases` - Test cases

3. **If script fails**, fallback to WebSearch and WebFetch to find the complete problem.

## Output Format

```python
class Solution:
    def methodName(self, A: List[int]) -> int:
        ...
```

| Metric           | Complexity | Reason |
| ---------------- | ---------- | ------ |
| Time Complexity  | O(n)       | ...    |
| Space Complexity | O(n)       | ...    |

Use plain text for complexity (e.g. `O(n log n)`, `O(1)`) — no LaTeX/MathJax formatting.

## Script Output Schema

```json
{
  "questionFrontendId": "1",
  "title": "Two Sum",
  "titleSlug": "two-sum",
  "content": "<p>Given an array of integers...</p>",
  "difficulty": "Easy",
  "topicTags": [{ "name": "Array", "slug": "array" }],
  "codeSnippets": [{ "lang": "Python3", "langSlug": "python3", "code": "..." }],
  "hints": ["Use a hash map..."],
  "exampleTestcases": "[2,7,11,15]\n9",
  "sampleTestCase": "[2,7,11,15]\n9"
}
```
