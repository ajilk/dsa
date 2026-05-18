#!/usr/bin/env python3
"""
LeetCode Question Fetcher
Fetches LeetCode problem details using the GraphQL API.

Usage:
    python3 fetch-leetcode.py <query>

    <query> can be:
        - Question number (e.g., 1, 42)
        - Title slug (e.g., two-sum)
        - URL (e.g., https://leetcode.com/problems/two-sum/)
"""

import argparse
import json
import re
import sys
import time
from typing import Optional, Dict, Any
import requests


class LeetCodeFetcher:
    """Fetches LeetCode questions via GraphQL API"""

    BASE_URL = "https://leetcode.com/graphql"

    def __init__(self):
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (CP-Documentation-Tool)"
        }

    def _make_request(self, payload: Dict[str, Any], max_retries: int = 3) -> Dict[str, Any]:
        """Make GraphQL request with retry logic"""
        for attempt in range(max_retries):
            try:
                response = requests.post(
                    self.BASE_URL,
                    json=payload,
                    headers=self.headers,
                    timeout=10
                )
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                if attempt == max_retries - 1:
                    raise Exception(f"Network error after {max_retries} attempts: {str(e)}")
                # Exponential backoff: 1s, 2s, 4s
                wait_time = 2 ** attempt
                time.sleep(wait_time)

        return {}

    def fetch_question_by_slug(self, title_slug: str) -> Dict[str, Any]:
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
            isPaidOnly
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

        result = self._make_request(payload)

        # Check if question was found
        if not result.get("data") or not result["data"].get("question"):
            raise Exception(f"Question not found: {title_slug}")

        question = result["data"]["question"]

        # Check if question is premium only
        if question.get("isPaidOnly"):
            raise Exception(
                f"Question '{question.get('title', title_slug)}' (#{question.get('questionFrontendId', '?')}) "
                f"is premium-only. Please subscribe or choose a free question."
            )

        return question

    def find_title_slug_by_number(self, question_number: int) -> Optional[str]:
        """Find title slug by question number using pagination"""
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
              titleSlug
            }
          }
        }
        """

        skip = 0
        limit = 100
        target = str(question_number)

        # Search through pages until we find the question
        while skip < 5000:  # Reasonable upper limit
            payload = {
                "query": query,
                "variables": {
                    "categorySlug": "",
                    "limit": limit,
                    "skip": skip,
                    "filters": {}
                }
            }

            try:
                result = self._make_request(payload)

                # More robust error checking
                if not result or "data" not in result:
                    raise Exception(f"Invalid API response when searching for question {question_number}")

                data = result.get("data")
                if not data:
                    raise Exception(f"No data returned from API")

                question_list = data.get("problemsetQuestionList")
                if not question_list:
                    raise Exception(f"No question list in API response")

                questions = question_list.get("questions", [])

                if not questions:
                    break

                for q in questions:
                    if q.get("frontendQuestionId") == target:
                        return q.get("titleSlug")

                skip += limit

            except KeyError as e:
                raise Exception(f"Unexpected API response structure: {str(e)}")

        return None

    def parse_url(self, url: str) -> Optional[str]:
        """Extract title slug from LeetCode URL"""
        pattern = r"leetcode\.com/problems/([^/?]+)"
        match = re.search(pattern, url)
        return match.group(1) if match else None

    def fetch(self, query: str) -> Dict[str, Any]:
        """Main entry point: fetch by number, slug, or URL"""
        # Check if it's a URL
        if "leetcode.com" in query.lower():
            slug = self.parse_url(query)
            if not slug:
                raise Exception(f"Could not extract problem slug from URL: {query}")
            return self.fetch_question_by_slug(slug)

        # Check if it's a number
        if query.isdigit():
            slug = self.find_title_slug_by_number(int(query))
            if not slug:
                raise Exception(f"Question #{query} not found")
            return self.fetch_question_by_slug(slug)

        # Assume it's a title slug
        return self.fetch_question_by_slug(query)


def main():
    parser = argparse.ArgumentParser(
        description="Fetch LeetCode question details via GraphQL API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s 1                                    # Fetch by number
  %(prog)s two-sum                              # Fetch by slug
  %(prog)s https://leetcode.com/problems/two-sum/  # Fetch by URL
        """
    )
    parser.add_argument(
        "query",
        help="Question number, title slug, or URL"
    )

    args = parser.parse_args()

    fetcher = LeetCodeFetcher()
    try:
        result = fetcher.fetch(args.query)
        print(json.dumps(result, indent=2))
        sys.exit(0)
    except Exception as e:
        error_msg = {"error": str(e)}
        print(json.dumps(error_msg, indent=2), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
