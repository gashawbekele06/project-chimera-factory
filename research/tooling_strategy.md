# Tooling & MCP Strategy

**Version:** 1.0  
**Date:** February 05, 2026

## Sub-Task A: Developer Tools (MCP Servers for Human Developer)

These MCP servers assist **me** (the FDE Trainee) during development in VS Code. They provide safe, standardized access to tools/resources without breaking the MCP-exclusive rule.

All servers route through the configured proxy: `https://mcppulse.10academy.org/proxy`  
Tenx MCP Sense is connected for full traceability (telemetry enabled in `.vscode/settings.json`).

Selected & configured developer MCP servers:

- **git-mcp** (or GitHub MCP / Git server):  
  Version control bridge — list branches, commit, push, create PRs, search repo history.  
  Purpose: Enables AI co-pilot to suggest git operations safely without shell escapes.

- **filesystem-mcp**:  
  Secure file read/write, search, create/edit files in allowed directories (repo root).  
  Purpose: Lets AI agent read specs/, write drafts, or edit .md files during planning.

- **terminal-mcp** (or shell-like):  
  Run safe shell commands (uv sync, pytest, git status, make test).  
  Purpose: Execute build/test/lint commands from within IDE agent workflows.

- **browser-mcp** (or Puppeteer / Playwright-based):  
  Controlled web browsing, scraping, or fetching docs.  
  Purpose: Research trends, API docs, or OpenClaw examples during architecture planning.

These are configured via VS Code MCP extension + proxy URL. No direct shell/API calls allowed outside MCP.

## Sub-Task B: Runtime Agent Skills (for Chimera Agents)

Skills are atomic, reusable capabilities that **Worker** agents call via MCP Tools during runtime execution.  
They are **not** developer tools — they power the autonomous influencers.

Skills are defined in `skills/` with:

- README.md containing description + strict Input/Output JSON schemas
- No implementation logic yet — contracts only (structure ready for agents to fill later)

Critical first skills (chosen for core influencer workflow):

1. fetch_trends — perceive real-time trends
2. generate_video — create multimodal content
3. post_content — publish approved content

See `skills/` directory for detailed contracts.
