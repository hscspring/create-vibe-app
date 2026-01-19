<!--
AI Instructions:
1. Read this file to understand the project structure
2. For new projects: help user describe their task, then break it down
3. For existing projects: read code first, deposit knowledge to wiki/
4. Use agents in agent/ and skills in skill/ to complete work
5. Record learnings in wiki/experience/
-->

# Vibe Coding Project

Welcome to your Vibe Coding project! This structure is designed to help AI agents work more effectively.

## 🚀 Quick Start

### New Project
Just tell the AI what you want to build:
> "帮我创建一个用户登录功能"

AI will automatically:
1. Break down requirements (via requirement-manager)
2. Create design (via design-manager)
3. Implement code (via implementation-executor)
4. Record learnings (via experience-depositor)

### Existing Project
First, let AI understand your codebase:
> "先阅读整个项目，把架构和关键信息沉淀到 wiki/"

Then continue with new tasks normally.

## 📁 Directory Structure

| Directory | Purpose |
|-----------|---------|
| `agent/` | Agent role definitions |
| `skill/` | Reusable workflow skills |
| `wiki/` | Project knowledge base |
| `requirement/` | Task tracking |
| `mcp/` | External tool configs |
| `code/` | Source code |
| `reference/` | Reference implementations |

> **💡 Tip**: Replace `code/` with your existing structure (e.g., `src/`) if needed.

## 🔄 Workflow

```
User Task → Phase Router → Agent → Execute → Record Learnings
                             ↓
                       wiki/ (context)
```

### Agents
| Agent | Role |
|-------|------|
| phase-router | Analyze intent, route to correct agent |
| requirement-manager | Break down and manage requirements |
| design-manager | Architecture and design decisions |
| implementation-executor | Write and modify code |
| experience-depositor | Extract and record learnings |

### Skills (10)
`req-create` · `design-create` · `code-commit` · `code-review` · `test-create` · `experience-record` · `workspace-setup` · `skill-creator` · `frontend-design` · `webapp-testing`

---
Happy Vibe Coding! 🎉

