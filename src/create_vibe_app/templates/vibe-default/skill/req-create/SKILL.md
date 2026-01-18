---
name: req-create
description: Create a new requirement document
---

# Skill: Create Requirement

## Purpose
Create a well-structured requirement document from a user idea or request.

## Inputs
- User description of the feature/task
- Priority level (optional)

## Workflow

1. **Capture** - Get the user's description
2. **Clarify** - Ask clarifying questions if needed
3. **Structure** - Format into standard template
4. **Index** - Add to `requirement/INDEX.md`
5. **Store** - Save detailed doc to `requirement/in-progress/`

## Output Template

```markdown
# [REQ-XXX] Title

## Summary
[One sentence description]

## Background
[Why this is needed, context]

## User Story
As a [user type], I want [goal], so that [benefit].

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Priority
[P0: Critical | P1: High | P2: Medium | P3: Low]

## Estimated Effort
[S/M/L/XL]

## Dependencies
- None

## Notes
[Additional context]
```

## Example Usage

**Input:**
> "我想添加用户登录功能"

**Output:**
Creates `requirement/in-progress/REQ-001-user-login.md` and updates INDEX.

## Tips
- Keep requirements atomic (one feature per requirement)
- Make acceptance criteria testable
- Link to related design docs when available
