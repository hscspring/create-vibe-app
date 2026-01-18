# Wiki: Experience & Lessons Learned

This directory contains lessons learned, solutions to problems, and patterns discovered during development.

## Purpose
Capture valuable knowledge that compounds over time, making future work easier.

## Categories

| Tag | Description |
|-----|-------------|
| `[BUG]` | Bug solutions |
| `[PATTERN]` | Successful patterns |
| `[PITFALL]` | Things to avoid |
| `[DECISION]` | Important decisions |
| `[TOOL]` | Tool tips |
| `[PERF]` | Performance learnings |

## Example Entry

```markdown
# [BUG] Database Connection Timeout

## TL;DR
Increase connection pool timeout for long queries.

## Problem
Queries over 30s were failing with connection timeout.

## Solution
Set `pool_timeout=60` in database config.

## Prevention
Monitor slow queries and optimize before they timeout.
```

## Tips
- Write while context is fresh
- Be specific and actionable
- Include code examples
- Add searchable tags
