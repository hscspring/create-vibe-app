---
name: code-commit
description: Commit code changes with proper messages
---

# Skill: Code Commit

## Purpose
Create well-structured git commits with meaningful messages.

## Inputs
- Changed files
- Context of what was done

## Workflow

1. **Stage** - Review changes to be committed
2. **Categorize** - Determine commit type
3. **Compose** - Write commit message
4. **Commit** - Execute git commit

## Commit Message Format

### Conventional Commits
```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
| Type | Description |
|------|-------------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `style` | Formatting, no code change |
| `refactor` | Code restructuring |
| `test` | Adding tests |
| `chore` | Maintenance tasks |

### Examples

```bash
# Feature
feat(auth): add user login functionality

Implement JWT-based authentication with:
- Login endpoint
- Token validation
- Session management

Closes #123

# Bug fix
fix(api): handle null response in user query

Previously threw NullPointerException when user not found.
Now returns 404 with proper error message.

# Documentation
docs(readme): update installation instructions
```

## Best Practices

1. **Atomic commits** - One logical change per commit
2. **Present tense** - "add feature" not "added feature"
3. **No period** - Subject line doesn't end with period
4. **50/72 rule** - Subject ≤50 chars, body wrapped at 72
5. **Reference issues** - Use "Closes #123" or "Fixes #456"

## Quick Commit Commands

```bash
# Stage all and commit
git add -A && git commit -m "type(scope): message"

# Amend last commit
git commit --amend

# Interactive staging
git add -p
```
