# MCP (Model Context Protocol) Configurations

This directory contains configurations for external tools and services that extend AI capabilities.

## What is MCP?
MCP connects AI agents to external services and data sources, providing access to tools like:
- Issue trackers (TAPD, Jira)
- Knowledge bases (Wiki, Notion)
- Code repositories
- Databases
- APIs

## How to Use
1. Add your MCP configuration files here
2. Reference them in your agent definitions
3. AI will automatically use available MCPs

## Example Configuration

```json
{
  "name": "github-mcp",
  "type": "github",
  "config": {
    "repo": "owner/repo",
    "token_env": "GITHUB_TOKEN"
  }
}
```

## Common MCPs
- GitHub/GitLab integration
- Jira/Linear/TAPD issue tracking
- Confluence/Notion documentation
- Database access
- API integrations

## Resources
- [MCP Documentation](https://modelcontextprotocol.io/)
- [Official MCP Servers](https://github.com/modelcontextprotocol/servers)
