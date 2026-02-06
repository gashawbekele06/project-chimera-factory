{
"version": "1.0.0",
"description": "Model Context Protocol (MCP) configuration for Project Chimera. Defines all required servers, tools, schemas, capabilities, and authentication. Agents MUST load this file before any external interaction.",
"proxy_url": "https://mcppulse.10academy.org/proxy",
"telemetry_enabled": true,
"required_servers": [
{
"id": "git-mcp",
"label": "Git MCP – Version Control Bridge",
"endpoint": "mcp://git",
"auth": {
"type": "none",
"note": "Uses GitHub token from env var GIT_TOKEN if needed for private repos"
},
"version": "1.0",
"capabilities": [
"list_branches",
"create_branch",
"commit",
"push",
"create_pr",
"search_repo_history"
],
"tool_schemas": {
"commit": {
"input": {
"type": "object",
"properties": {
"message": { "type": "string", "description": "Commit message" },
"files": { "type": "array", "items": { "type": "string" }, "description": "Paths to stage" }
},
"required": ["message"]
},
"output": {
"type": "object",
"properties": {
"commit_hash": { "type": "string" },
"status": { "type": "string", "enum": ["success", "failed"] }
},
"required": ["status"]
}
}
}
},
{
"id": "filesystem-mcp",
"label": "Filesystem MCP – Secure File Access",
"endpoint": "mcp://filesystem",
"auth": { "type": "none" },
"version": "1.0",
"capabilities": [
"read_file",
"write_file",
"create_directory",
"search_files",
"delete_file"
],
"tool_schemas": {
"read_file": {
"input": { "path": { "type": "string" } },
"output": { "content": { "type": "string" } }
}
},
"notes": "Restricted to repo root only; no access outside project folder"
},
{
"id": "terminal-mcp",
"label": "Terminal MCP – Safe Shell Execution",
"endpoint": "mcp://terminal",
"auth": { "type": "none" },
"version": "1.0",
"capabilities": [
"run_command",
"run_script"
],
"tool_schemas": {
"run_command": {
"input": { "cmd": { "type": "string" } },
"output": {
"stdout": { "type": "string" },
"stderr": { "type": "string" },
"exit_code": { "type": "integer" }
}
}
},
"notes": "Allowed commands limited to uv, pytest, git status, etc. No rm -rf or dangerous ops."
},
{
"id": "browser-mcp",
"label": "Browser MCP – Controlled Web Access",
"endpoint": "mcp://browser",
"auth": { "type": "none" },
"version": "1.0",
"capabilities": [
"browse_page",
"scrape_element",
"take_screenshot"
],
"tool_schemas": {
"browse_page": {
"input": { "url": { "type": "string" } },
"output": { "content": { "type": "string" } }
}
},
"notes": "Used only for research/trend validation; no login or form submission."
}
],
"global_constraints": {
"max_requests_per_minute": 100,
"allowed_domains": ["api.twitter.com", "api.tiktok.com", "graph.instagram.com", "github.com"],
"forbidden_actions": ["shell rm -rf", "pip install", "direct http requests outside MCP"]
}
}
