---
name: design-create
description: Create a design document for a feature or system
---

# Skill: Create Design Document

## Purpose
Create a comprehensive design document that guides implementation.

## Inputs
- Requirement document
- Existing architecture context (from `wiki/design/`)

## Workflow

1. **Analyze** - Understand the requirement
2. **Research** - Check existing patterns in `wiki/tech/`
3. **Design** - Create the architecture
4. **Document** - Write the design doc
5. **Review** - Get user approval

## Output Template

```markdown
# Design: [Feature Name]

## Overview
[What this design covers]

## Requirements Reference
- [Link to requirement]

## Goals
- Goal 1
- Goal 2

## Non-Goals
- What this does NOT cover

## Architecture

### System Context
[How this fits into the overall system]

### Components
| Component | Responsibility |
|-----------|----------------|
| ComponentA | Does X |
| ComponentB | Does Y |

### Data Flow
```
[Diagram or description of data flow]
```

### API Design
[If applicable]

#### Endpoint: POST /api/example
- Request: `{ "field": "value" }`
- Response: `{ "result": "value" }`

## Implementation Plan
1. Step 1
2. Step 2
3. Step 3

## Alternatives Considered
| Option | Pros | Cons | Decision |
|--------|------|------|----------|
| Option A | ... | ... | Selected |
| Option B | ... | ... | Rejected |

## Risks & Mitigations
| Risk | Mitigation |
|------|------------|
| Risk 1 | How to handle |

## Open Questions
- [ ] Question 1
```

## Storage
Save to `wiki/design/[feature-name].md`

## Tips
- Keep designs focused on the "what" and "why"
- Leave implementation details flexible
- Get user approval before implementation
