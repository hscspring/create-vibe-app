---
name: code-review
description: Review code for quality, bugs, security, and improvements. Use when self-reviewing before commit, reviewing PRs, or debugging issues.
---

# Code Review

Systematically review code for quality, bugs, and security.

## Checklist

| Priority | Check |
|----------|-------|
| 🔴 Critical | Security (no secrets, injection) |
| 🔴 Critical | Correctness (logic, edge cases) |
| 🟡 Important | Performance (N+1, loops) |
| 🟡 Important | Error handling |
| 🟢 Nice-to-have | Readability, DRY, style |

## Process

1. **Context** - Read requirement/design
2. **High-level** - Architecture check
3. **Line-by-line** - Detailed inspection
4. **Tests** - Check coverage
5. **Document** - Summarize findings

## Output Format

```markdown
## Code Review: [Name]

### Summary
[Approved / Changes Requested]

### Issues
- 🔴 [file:line] Problem → Suggestion
- 🟡 [file:line] Problem → Suggestion

### Good Patterns 👍
- [What was done well]
```

## Common Issues

```python
# 🔴 Security
password = "hardcoded"          # Bad
password = os.environ["PASS"]   # Good

# 🔴 SQL Injection
f"SELECT * WHERE id={id}"       # Bad
"SELECT * WHERE id=%s", (id,)   # Good
```

## Tips
- Be constructive
- Explain the "why"
- Acknowledge good patterns
