---
argument-hint: "[question/code/link]"
description: Solve LeetCode problems in Python. Use when asked to solve, write, or fix a LeetCode problem, or when given a problem number/name/URL.
allowed-tools: Bash
---

Solve the LeetCode problem following these requirements:

1. **Language**: Python 3 only (use type hints)
2. **Code format**: LeetCode class-based solution (no explanations unless asked)
3. **Naming**: Follow conventions in `content/docs/naming.md`
4. **Assumptions**: All necessary imports are available

## Fetching Questions

**If the question is unclear, not provided, or only a problem number/name/URL is given:**

1. **First, try the LeetCode fetcher script:**

   ```bash
   python3 ${CLAUDE_SKILL_DIR}/fetch-leetcode.py <query>
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

3. **If script fails**, fallback to web search and web fetch to find the complete problem.

## Output Format

```python
class Solution:
    def functionName(self, param1: int, param2: List[int]) -> int:
        # code here
        pass
```

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
