---
argument-hint: [question/code/link]
description: Solve LeetCode problems in Python
allowed-tools: [Bash, web_search, web_fetch]
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
   python3 /Users/ajilk/Documents/git/cp/scripts/fetch-leetcode.py <query>
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

Example output format:

```python
class Solution:
    def functionName(self, param1: int, param2: List[int]) -> int:
        # code here
        pass
```
