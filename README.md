# 🎸 create-vibe-app

Scaffold AI-friendly project structures for **Vibe Coding** – a methodology that helps AI agents work more effectively on your codebase.

## ✨ What is Vibe Coding?

Vibe Coding is a development approach where:
- **AI agents** handle implementation based on clear structures
- **Knowledge compounds** through wiki and experience recording
- **Complexity-based routing** ensures the right workflow for each task

## 📦 Installation

```bash
pip install create-vibe-app
```

## 🚀 Usage

```bash
create-vibe-app my-project
cd my-project
code .
```

Then in your AI assistant:
> "Read MAIN.md, then help me build [your idea]"

## 📁 Generated Structure

```
my-project/
├── MAIN.md           # Project entry point
├── agent/            # AI agent definitions
│   ├── phase-router.md
│   ├── requirement-manager.md
│   ├── design-manager.md
│   ├── implementation-executor.md
│   └── experience-depositor.md
├── skill/            # Reusable workflow skills (10)
├── wiki/             # Project knowledge base
├── requirement/      # Task tracking
├── mcp/              # External tool configs
├── code/             # Your source code
└── reference/        # Reference implementations
```

## 🔄 Workflow

```
User Task → Analyze Intent → Detect Complexity → Route → Update Knowledge
                                ↓
                    Simple: Direct execution
                    Medium: Requirement → Design → Implement
                    Complex: Full flow + User confirmation
```

## Examples

[hscspring/create-vibe-app-examples](https://github.com/hscspring/create-vibe-app-examples)
