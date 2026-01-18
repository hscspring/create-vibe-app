# Vibe Coding Project

Welcome to your Vibe Coding project! This structure is designed to help AI agents work more effectively on your codebase.

## 🚀 Quick Start

1. **Define your requirement** in `requirement/INDEX.md`
2. **Let AI design** using agents in `agent/`
3. **Implement** with skills in `skill/`
4. **Record learnings** in `wiki/`

## 📁 Directory Structure

| Directory | Purpose |
|-----------|---------|
| `agent/` | Agent role definitions and prompts |
| `skill/` | Reusable workflow skills |
| `wiki/` | Project knowledge base (context) |
| `requirement/` | Task and requirement tracking |
| `mcp/` | External tool configurations |
| `code/` | Your source code |
| `reference/` | Reference implementations |

## 🔄 Workflow

```
User Intent → Phase Router → Agent → Skill Execution → Experience Deposit
                                ↓
                          wiki/ (context loading)
```

### Agents
- **phase-router**: Routes intent to the correct agent
- **requirement-manager**: Manages requirement lifecycle
- **design-manager**: Handles architecture and design
- **implementation-executor**: Writes and modifies code
- **experience-depositor**: Extracts and records learnings

### Skills
Pre-defined reusable workflows:
- `req-create/` - Create new requirements
- `design-create/` - Create design documents
- `code-commit/` - Commit with proper messages
- `code-review/` - Review code for issues
- `test-create/` - Generate test cases
- `experience-record/` - Record lessons learned
- `workspace-setup/` - Initialize dev environment

## 📝 Getting Started

1. Start by adding your first requirement:
   ```markdown
   # requirement/INDEX.md
   - [ ] [REQ-001] Your first feature
   ```

2. Invoke the requirement manager agent to refine it.

3. Use design-manager to create architecture.

4. Let implementation-executor write the code.

5. Record learnings with experience-depositor.

Happy Vibe Coding! 🎉
