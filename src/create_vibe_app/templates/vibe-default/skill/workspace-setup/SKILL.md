---
name: workspace-setup
description: Initialize development environment
---

# Skill: Workspace Setup

## Purpose
Set up a consistent development environment for a new project or developer.

## Inputs
- Project type (web, backend, mobile, etc.)
- Tech stack

## Workflow

1. **Identify** - Determine project requirements
2. **Install** - Install dependencies
3. **Configure** - Set up configuration files
4. **Verify** - Run verification commands
5. **Document** - Update setup docs

## Common Setup Tasks

### Node.js / Frontend
```bash
# Install dependencies
npm install

# Verify
npm run dev
```

### Python
```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
# or
pip install -e .

# Verify
python -c "import main; print('OK')"
```

### Rust
```bash
cargo build
cargo test
```

### Docker
```bash
docker-compose up -d
```

## Configuration Files Checklist

- [ ] `.env` - Environment variables (copy from `.env.example`)
- [ ] IDE settings (`.vscode/`, `.idea/`)
- [ ] Linter config (`.eslintrc`, `pyproject.toml`)
- [ ] Git hooks (`.husky/`, `pre-commit`)

## Environment Variables Template

```bash
# .env.example
DATABASE_URL=postgresql://user:pass@localhost:5432/db
API_KEY=your-api-key-here
DEBUG=true
```

## Verification Checklist

- [ ] Dependencies installed
- [ ] Configuration files present
- [ ] Development server starts
- [ ] Tests pass
- [ ] Linter passes

## Tips
- Always document setup steps in README
- Use `.env.example` for environment template
- Consider using Docker for complex setups
- Record any issues in `wiki/experience/`
