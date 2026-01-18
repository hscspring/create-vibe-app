---
name: experience-record
description: Record lessons learned and experiences
---

# Skill: Record Experience

## Purpose
Capture valuable lessons learned, solutions to problems, and patterns for future reference.

## When to Use
- After solving a tricky bug
- Discovering a useful pattern
- Making an important decision
- Completing a complex feature

## Experience Categories

| Category | Tag | Description |
|----------|-----|-------------|
| Bug | `[BUG]` | Bug and its solution |
| Pattern | `[PATTERN]` | Successful code pattern |
| Pitfall | `[PITFALL]` | Things to avoid |
| Decision | `[DECISION]` | Why a choice was made |
| Tool | `[TOOL]` | Useful tool/config |
| Performance | `[PERF]` | Optimization learnings |

## Workflow

1. **Trigger** - Identify something worth recording
2. **Categorize** - Select the right category
3. **Document** - Write the experience entry
4. **Store** - Save to `wiki/experience/`
5. **Cross-reference** - Link to related docs

## Output Template

```markdown
# [CATEGORY] Short Title

## TL;DR
[One sentence summary]

## Context
[When and where this applies]

## Problem
[What was the issue or challenge]

## Solution
[How it was solved]

## Code Example
```language
// Before (bad)
...

// After (good)
...
```

## Why It Works
[Explanation of why this solution is correct]

## Prevention
[How to avoid this issue in the future]

## Related
- [Link to related experience]
- [Link to external resource]

## Tags
#tag1 #tag2 #tag3
```

## Example Entries

### Bug Example
```markdown
# [BUG] Null Pointer in User Query

## TL;DR
Always check for null before accessing user properties.

## Problem
API crashed when querying non-existent user.

## Solution
Added null check and proper error response.

## Prevention
- Add unit tests for null cases
- Use Optional types where available
```

### Decision Example
```markdown
# [DECISION] JWT over Session for Auth

## TL;DR
Chose JWT for stateless authentication.

## Context
Needed auth for microservices architecture.

## Options Considered
1. Session-based - Requires shared session store
2. JWT - Stateless, scalable

## Decision
JWT because:
- No shared state needed
- Works across services
- Easy to scale

## Trade-offs
- Larger request size
- Can't invalidate immediately
```

## Storage Structure

```
wiki/experience/
├── bugs/
│   └── null-pointer-user-query.md
├── patterns/
│   └── repository-pattern.md
├── decisions/
│   └── jwt-auth-choice.md
└── INDEX.md  # Quick reference
```

## Tips
- Write while context is fresh
- Be specific and actionable
- Include code examples
- Add searchable tags
- Link to related experiences
