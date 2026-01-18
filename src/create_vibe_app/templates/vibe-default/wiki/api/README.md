# Wiki: API Documentation

This directory contains API specifications and documentation.

## Purpose
Store API contracts, endpoint documentation, and integration guides.

## Example Contents
- REST API endpoints
- GraphQL schemas
- WebSocket protocols
- Third-party API integrations

## Template

```markdown
# API: [Service Name]

## Base URL
`https://api.example.com/v1`

## Authentication
[Auth method description]

## Endpoints

### GET /resource
**Description**: Get a resource

**Parameters**:
| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | Yes | Resource ID |

**Response**:
```json
{
  "id": "123",
  "name": "Example"
}
```

**Errors**:
| Code | Description |
|------|-------------|
| 404 | Resource not found |
```

## Tips
- Keep API docs in sync with implementation
- Include request/response examples
- Document error cases
