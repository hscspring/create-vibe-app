---
name: code-review
description: Review code for issues, bugs, and improvements
---

# Skill: Code Review

## Purpose
Systematically review code for quality, bugs, security issues, and improvements.

## Inputs
- Code files or diff to review
- Context (requirement, design doc)

## Review Checklist

### 🔴 Critical (Must Fix)
- [ ] **Security** - No hardcoded secrets, SQL injection, XSS
- [ ] **Correctness** - Logic errors, edge cases
- [ ] **Data integrity** - Proper validation, error handling

### 🟡 Important (Should Fix)
- [ ] **Performance** - N+1 queries, unnecessary loops
- [ ] **Error handling** - Graceful failures, proper logging
- [ ] **Testing** - Adequate test coverage

### 🟢 Suggestions (Nice to Have)
- [ ] **Readability** - Clear naming, comments
- [ ] **DRY** - No code duplication
- [ ] **Style** - Consistent formatting

## Review Process

1. **Understand context** - Read requirement and design
2. **High-level review** - Architecture and structure
3. **Line-by-line review** - Detailed code inspection
4. **Test review** - Check test coverage
5. **Document findings** - Create review summary

## Output Format

```markdown
## Code Review: [Feature/PR Name]

### Summary
[Overall assessment: Approved / Changes Requested / Needs Discussion]

### Critical Issues 🔴
- [ ] Issue 1 (file:line)
  - Problem: ...
  - Suggestion: ...

### Important Issues 🟡
- [ ] Issue 1 (file:line)
  - Problem: ...
  - Suggestion: ...

### Suggestions 🟢
- [ ] Suggestion 1 (file:line)
  - Current: ...
  - Better: ...

### Positive Notes 👍
- Good pattern in file.py
- Clear error handling

### Questions
- Why was X approach chosen over Y?
```

## Common Patterns to Check

### Security
```python
# Bad
password = "hardcoded123"
query = f"SELECT * FROM users WHERE id = {user_id}"

# Good
password = os.environ.get("PASSWORD")
query = "SELECT * FROM users WHERE id = %s", (user_id,)
```

### Error Handling
```python
# Bad
result = risky_operation()

# Good
try:
    result = risky_operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
    raise
```

## Tips
- Be constructive, not critical
- Explain the "why" behind suggestions
- Acknowledge good patterns
- Prioritize issues clearly
