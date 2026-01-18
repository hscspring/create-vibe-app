---
name: experience-record
description: Record lessons learned and experiences for future reference. Use after solving bugs, discovering patterns, making decisions, or completing complex features.
---

# Record Experience

Capture valuable lessons for future reference.

## Categories

| Tag | Use For |
|-----|---------|
| `[BUG]` | Bug solutions |
| `[PATTERN]` | Successful patterns |
| `[PITFALL]` | Things to avoid |
| `[DECISION]` | Important choices |
| `[PERF]` | Optimizations |

## Template

```markdown
# [CATEGORY] Title

## TL;DR
[One sentence]

## Problem
[What was the issue]

## Solution
[How it was solved]

## Code Example
```language
// Before (bad)
...

// After (good)
...
```

## Prevention
[How to avoid in future]

## Tags
#tag1 #tag2
```

## Example

```markdown
# [BUG] Null Pointer in User Query

## TL;DR
Check for null before accessing user properties.

## Problem
API crashed on non-existent user.

## Solution
Added null check and 404 response.

## Prevention
- Unit tests for null cases
- Use Optional types
```

## Storage

```
wiki/experience/
├── bugs/
├── patterns/
└── decisions/
```

## Tips
- Write while context is fresh
- Include code examples
- Add searchable tags
