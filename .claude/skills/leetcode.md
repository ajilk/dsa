---
name: LeetCode Question Fetcher
description: Fetch LeetCode problem details by number, slug, or URL using GraphQL API
---

# LeetCode Question Fetching Skill

## Quick Start

Use the bundled Python script to fetch LeetCode questions:

```bash
python3 scripts/fetch-leetcode.py <query>
```

### Examples

```bash
# By question number
python3 scripts/fetch-leetcode.py 1

# By title slug
python3 scripts/fetch-leetcode.py two-sum

# By URL
python3 scripts/fetch-leetcode.py https://leetcode.com/problems/two-sum/
```

### Output Format

The script outputs JSON to stdout with the following structure:

```json
{
  "questionFrontendId": "1",
  "title": "Two Sum",
  "titleSlug": "two-sum",
  "content": "<p>Given an array of integers...</p>",
  "difficulty": "Easy",
  "topicTags": [
    { "name": "Array", "slug": "array" },
    { "name": "Hash Table", "slug": "hash-table" }
  ],
  "codeSnippets": [
    {
      "lang": "Python3",
      "langSlug": "python3",
      "code": "class Solution:\n    def twoSum..."
    }
  ],
  "hints": ["Use a hash map..."],
  "exampleTestcases": "[2,7,11,15]\n9",
  "sampleTestCase": "[2,7,11,15]\n9"
}
```

### Usage in Workflows

When fetching a LeetCode question:

1. Call the script via Bash tool
2. Parse the JSON output
3. Extract relevant fields (title, content, code snippets)
4. Format for documentation or solution

### Performance

- Typical fetch time: ~2-5 seconds
- Network-dependent latency
- No caching (always fetches fresh data)

---

## Advanced: Direct GraphQL API Usage

This section provides detailed information about the LeetCode GraphQL API for advanced users who want to implement custom fetching logic.

### Overview

LeetCode uses question title slugs (URL-friendly names) rather than question numbers directly in their API.

## API Endpoint

```
POST https://leetcode.com/graphql
```

## Required Headers

```
Content-Type: application/json
User-Agent: Mozilla/5.0
```

## Method 1: Fetch Question by Title Slug (Direct)

If you know the title slug (e.g., "two-sum", "add-two-numbers"):

### GraphQL Query

```graphql
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    title
    titleSlug
    content
    difficulty
    likes
    dislikes
    exampleTestcases
    topicTags {
      name
      slug
    }
    codeSnippets {
      lang
      langSlug
      code
    }
    stats
    hints
    solution {
      id
      canSeeDetail
      paidOnly
      hasVideoSolution
    }
    status
    sampleTestCase
    metaData
    judgerAvailable
    judgeType
    mysqlSchemas
    enableRunCode
    enableTestMode
    envInfo
  }
}
```

### Request Body (Python Example)

```python
import requests
import json

def fetch_leetcode_question(title_slug):
    url = "https://leetcode.com/graphql"

    query = """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionId
        questionFrontendId
        title
        content
        difficulty
        exampleTestcases
        topicTags {
          name
          slug
        }
        codeSnippets {
          lang
          langSlug
          code
        }
        hints
        sampleTestCase
      }
    }
    """

    payload = {
        "query": query,
        "variables": {"titleSlug": title_slug}
    }

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# Example usage
result = fetch_leetcode_question("two-sum")
print(json.dumps(result, indent=2))
```

## Method 2: Convert Question Number to Title Slug

If you only have the question number (e.g., 1, 2, 3):

### Step 1: Get All Questions List

```graphql
query problemsetQuestionList(
  $categorySlug: String
  $limit: Int
  $skip: Int
  $filters: QuestionListFilterInput
) {
  problemsetQuestionList: questionList(
    categorySlug: $categorySlug
    limit: $limit
    skip: $skip
    filters: $filters
  ) {
    total: totalNum
    questions: data {
      acRate
      difficulty
      freqBar
      frontendQuestionId: questionFrontendId
      isFavor
      paidOnly: isPaidOnly
      status
      title
      titleSlug
      topicTags {
        name
        id
        slug
      }
      hasSolution
      hasVideoSolution
    }
  }
}
```

### Step 2: Filter by Question Number

```python
def get_question_by_number(question_number):
    url = "https://leetcode.com/graphql"

    query = """
    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
      problemsetQuestionList: questionList(
        categorySlug: $categorySlug
        limit: $limit
        skip: $skip
        filters: $filters
      ) {
        questions: data {
          frontendQuestionId: questionFrontendId
          title
          titleSlug
          difficulty
        }
      }
    }
    """

    # Fetch questions in batches
    payload = {
        "query": query,
        "variables": {
            "categorySlug": "",
            "limit": 50,
            "skip": 0,
            "filters": {}
        }
    }

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    # You may need to paginate through results
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

    # Find the question with matching number
    for q in data['data']['problemsetQuestionList']['questions']:
        if q['frontendQuestionId'] == str(question_number):
            return q['titleSlug']

    return None

# Get title slug, then fetch full question
title_slug = get_question_by_number(1)
if title_slug:
    question_data = fetch_leetcode_question(title_slug)
```

## Method 3: Direct URL Pattern (Alternative)

LeetCode questions follow a URL pattern. You can sometimes construct the title slug from common patterns:

- Question 1: "two-sum"
- Question 2: "add-two-numbers"
- Pattern: lowercase, words separated by hyphens

However, this is unreliable for programmatic use. Always use the API when possible.

## Complete Implementation Example

```python
import requests
import json

class LeetCodeAPI:
    BASE_URL = "https://leetcode.com/graphql"

    def __init__(self):
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }

    def fetch_question_by_slug(self, title_slug):
        """Fetch question details by title slug"""
        query = """
        query questionData($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            questionId
            questionFrontendId
            title
            titleSlug
            content
            difficulty
            likes
            dislikes
            exampleTestcases
            topicTags {
              name
              slug
            }
            codeSnippets {
              lang
              langSlug
              code
            }
            hints
            sampleTestCase
            stats
          }
        }
        """

        payload = {
            "query": query,
            "variables": {"titleSlug": title_slug}
        }

        response = requests.post(self.BASE_URL, json=payload, headers=self.headers)
        return response.json()

    def find_title_slug_by_number(self, question_number):
        """Find title slug by question number"""
        query = """
        query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int) {
          problemsetQuestionList: questionList(
            categorySlug: $categorySlug
            limit: $limit
            skip: $skip
          ) {
            questions: data {
              frontendQuestionId: questionFrontendId
              titleSlug
            }
          }
        }
        """

        skip = 0
        limit = 100

        while True:
            payload = {
                "query": query,
                "variables": {
                    "categorySlug": "",
                    "limit": limit,
                    "skip": skip
                }
            }

            response = requests.post(self.BASE_URL, json=payload, headers=self.headers)
            data = response.json()

            questions = data.get('data', {}).get('problemsetQuestionList', {}).get('questions', [])

            if not questions:
                break

            for q in questions:
                if q['frontendQuestionId'] == str(question_number):
                    return q['titleSlug']

            skip += limit

        return None

    def fetch_question_by_number(self, question_number):
        """Fetch question details by question number"""
        title_slug = self.find_title_slug_by_number(question_number)

        if not title_slug:
            return {"error": f"Question {question_number} not found"}

        return self.fetch_question_by_slug(title_slug)

# Usage
api = LeetCodeAPI()

# Method 1: By number
question = api.fetch_question_by_number(1)
print(json.dumps(question, indent=2))

# Method 2: By slug (faster if you know it)
question = api.fetch_question_by_slug("two-sum")
print(json.dumps(question, indent=2))
```

## Response Structure

The API returns a JSON object with this structure:

```json
{
  "data": {
    "question": {
      "questionId": "1",
      "questionFrontendId": "1",
      "title": "Two Sum",
      "titleSlug": "two-sum",
      "content": "<p>Given an array of integers...</p>",
      "difficulty": "Easy",
      "likes": 45000,
      "dislikes": 1500,
      "exampleTestcases": "[2,7,11,15]\n9\n[3,2,4]\n6",
      "topicTags": [
        { "name": "Array", "slug": "array" },
        { "name": "Hash Table", "slug": "hash-table" }
      ],
      "codeSnippets": [
        {
          "lang": "Python3",
          "langSlug": "python3",
          "code": "class Solution:\n    def twoSum(self, nums: List[int], target: int) -> List[int]:\n        "
        }
      ],
      "hints": ["Use a hash map..."],
      "sampleTestCase": "[2,7,11,15]\n9"
    }
  }
}
```

## Key Fields Explanation

- **questionFrontendId**: The question number shown on LeetCode (e.g., "1", "2")
- **titleSlug**: URL-friendly question identifier (e.g., "two-sum")
- **content**: HTML-formatted question description
- **difficulty**: "Easy", "Medium", or "Hard"
- **codeSnippets**: Starting code templates for various languages
- **exampleTestcases**: Test cases in LeetCode format
- **topicTags**: Categories/topics the question belongs to
- **hints**: Official hints for solving the problem

## Best Practices

1. **Use title slug when possible**: It's faster and more direct
2. **Cache question list**: If fetching multiple questions, cache the list to avoid repeated API calls
3. **Handle errors**: LeetCode API can be rate-limited; implement retry logic
4. **Parse HTML content**: The `content` field contains HTML; parse it to extract plain text if needed
5. **Respect rate limits**: Don't spam the API; add delays between requests

## Common Issues & Solutions

### Issue 1: Rate Limiting

**Solution**: Add delays between requests (1-2 seconds), use exponential backoff

### Issue 2: Question Not Found

**Solution**: Verify the question number/slug exists, check for typos

### Issue 3: HTML Content

**Solution**: Use libraries like BeautifulSoup to parse HTML from the `content` field

### Issue 4: Code Snippets Format

**Solution**: The `code` field in `codeSnippets` is a string; extract for specific language

## Additional Notes

- LeetCode's GraphQL API is unofficial and may change without notice
- Some questions require authentication (premium questions)
- The API doesn't require authentication for public questions
- Question numbers (frontendQuestionId) are not always sequential
