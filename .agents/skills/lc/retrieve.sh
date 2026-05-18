#!/usr/bin/env bash
set -euo pipefail

GRAPHQL_URL="https://leetcode.com/graphql"
USER_AGENT="Mozilla/5.0 (CP-Documentation-Tool)"

gql_request() {
    local payload="$1"
    local attempt=0
    while [ $attempt -lt 3 ]; do
        local out
        if out=$(curl -s -f -X POST "$GRAPHQL_URL" \
            -H "Content-Type: application/json" \
            -H "User-Agent: $USER_AGENT" \
            --data "$payload" \
            --max-time 10 2>/dev/null); then
            echo "$out"
            return 0
        fi
        attempt=$((attempt + 1))
        [ $attempt -lt 3 ] && sleep $((2 ** (attempt - 1)))
    done
    echo '{"error":"network error after 3 attempts"}' >&2
    exit 1
}

fetch_by_slug() {
    local slug="$1"
    local query='query questionData($titleSlug: String!) { question(titleSlug: $titleSlug) { questionId questionFrontendId title titleSlug content difficulty likes dislikes isPaidOnly exampleTestcases topicTags { name slug } codeSnippets { lang langSlug code } hints sampleTestCase stats } }'
    local payload
    payload=$(jq -n --arg q "$query" --arg s "$slug" \
        '{"query":$q,"variables":{"titleSlug":$s}}')

    local result
    result=$(gql_request "$payload")

    if echo "$result" | jq -e '.data.question == null' >/dev/null 2>&1; then
        echo "{\"error\":\"Question not found: $slug\"}" >&2
        exit 1
    fi

    local is_paid
    is_paid=$(echo "$result" | jq -r '.data.question.isPaidOnly // false')
    if [ "$is_paid" = "true" ]; then
        local title
        title=$(echo "$result" | jq -r '.data.question.title // "unknown"')
        echo "{\"error\":\"'$title' is premium-only\"}" >&2
        exit 1
    fi

    echo "$result" | jq '.data.question'
}

find_slug_by_number() {
    local number="$1"
    local query='query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) { problemsetQuestionList: questionList(categorySlug: $categorySlug limit: $limit skip: $skip filters: $filters) { questions: data { frontendQuestionId: questionFrontendId titleSlug } } }'
    local skip=0
    local limit=100

    while [ "$skip" -lt 5000 ]; do
        local payload
        payload=$(jq -n --arg q "$query" --argjson skip "$skip" --argjson limit "$limit" \
            '{"query":$q,"variables":{"categorySlug":"","limit":$limit,"skip":$skip,"filters":{}}}')

        local result
        result=$(gql_request "$payload")

        local slug
        slug=$(echo "$result" | jq -r --arg num "$number" \
            '.data.problemsetQuestionList.questions[] | select(.frontendQuestionId == $num) | .titleSlug' 2>/dev/null || true)

        if [ -n "$slug" ]; then
            echo "$slug"
            return 0
        fi

        local count
        count=$(echo "$result" | jq '.data.problemsetQuestionList.questions | length' 2>/dev/null || echo 0)
        [ "$count" -eq 0 ] && break

        skip=$((skip + limit))
    done

    echo ""
}

parse_url_slug() {
    echo "$1" | sed 's|.*leetcode\.com/problems/\([^/?]*\).*|\1|'
}

main() {
    local query="${1:-}"

    if [ -z "$query" ]; then
        echo "Usage: $0 <number|slug|url>" >&2
        exit 1
    fi

    local slug=""

    case "$query" in
        *leetcode.com*)
            slug=$(parse_url_slug "$query")
            if [ -z "$slug" ] || [ "$slug" = "$query" ]; then
                echo '{"error":"Could not extract slug from URL"}' >&2
                exit 1
            fi
            ;;
        *[!0-9]*)
            slug="$query"
            ;;
        *)
            slug=$(find_slug_by_number "$query")
            if [ -z "$slug" ]; then
                echo "{\"error\":\"Question #$query not found\"}" >&2
                exit 1
            fi
            ;;
    esac

    fetch_by_slug "$slug"
}

main "$@"
