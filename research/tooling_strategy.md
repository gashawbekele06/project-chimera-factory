# research/tooling_strategy.md

## Tooling Strategy for Project Chimera

### Sub-Task A: Developer Tools (MCP Servers)

These MCP servers are for **you** (the human developer and any AI co-pilot) during development. They provide safe, traceable access to the development environment and are **not** part of the runtime Chimera agent system.

#### Selected Developer MCP Servers

1. **git-mcp**
   - Purpose: Full version control operations (status, commit, branch, diff, merge).
   - Configuration: Stdio transport, local repository access.
   - Usage: Ensures commits tell a clear story of spec → test → implementation progression.

2. **filesystem-mcp**
   - Purpose: File creation, reading, editing, and navigation within the project directory.
   - Configuration: Restricted to project root, stdio/SSE transport.
   - Usage: Primary tool for creating specs, tests, skill stubs, and documentation.

3. **browser-mcp** (or web-search-mcp)
   - Purpose: Research external references (MCP spec, Coinbase AgentKit docs, social API changes).
   - Configuration: Proxied via MCP Pulse (`https://mcppulse.10academy.org/proxy`).
   - Usage: Clarify ambiguous SRS sections or tool schemas without leaving the IDE.

4. **python-repl-mcp** (optional)
   - Purpose: Quick validation of Pydantic models, JSON schemas, or contract testing.
   - Configuration: Local interpreter bridge.

These tools enable rigorous spec-driven development while keeping the runtime agent environment clean and MCP-exclusive.

### Sub-Task B: Agent Skills (Runtime)

Runtime **skills** are internal Python modules that Chimera Worker agents call.  
Each skill is a typed capability with strict Input/Output contracts.  
Skills orchestrate MCP Tool calls when needed but contain **no direct external logic**.

The `skills/` directory contains:

- `README.md`: Contract definitions for all skills.
- Individual modules: Stub implementations raising `NotImplementedError`.

At least three critical skills are defined below (see `skills/README.md`).
