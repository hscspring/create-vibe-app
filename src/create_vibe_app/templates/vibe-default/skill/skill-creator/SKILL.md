---
name: skill-creator
description: Guide for creating effective skills. Use when creating a new skill or updating an existing skill that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.
---

# Skill Creator

Create modular, self-contained packages that extend AI capabilities with specialized knowledge and workflows.

## Core Principles

### Concise is Key
Challenge each piece: "Does Claude really need this?" Prefer concise examples over verbose explanations.

### Progressive Disclosure
1. **Metadata** (~100 words) - Always loaded
2. **SKILL.md body** (<500 lines) - When triggered
3. **Bundled resources** - As needed

### Skill Structure
```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description)
│   └── Markdown instructions
└── Bundled Resources (optional)
    ├── scripts/      - Executable code
    ├── references/   - Documentation
    └── assets/       - Templates, icons
```

## SKILL.md Format

```yaml
---
name: my-skill
description: What it does AND when to use it (critical for triggering)
---

# Title

[Core instructions - imperative form]

## Sections as needed
```

## Best Practices

| Do | Don't |
|----|-------|
| Clear, comprehensive description | Vague one-liner |
| Imperative form ("Create", "Run") | Passive voice |
| Concise examples | Verbose explanations |
| Reference files for details | Everything in SKILL.md |
| Test scripts by running them | Assume they work |

## What NOT to Include
- README.md, CHANGELOG.md, INSTALLATION.md
- User-facing documentation
- Setup/testing procedures

## Creation Process

1. **Understand** - Get concrete usage examples
2. **Plan** - Identify reusable scripts/references/assets
3. **Initialize** - Create skill directory with SKILL.md
4. **Edit** - Implement resources, write instructions
5. **Test** - Verify with real usage
6. **Iterate** - Refine based on feedback
