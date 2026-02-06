# research/tooling_strategy.md

## Tooling Strategy

### Sub-Task A: Developer Tools (MCP Servers)

These are **MCP servers** used during development to assist **you** (the human/AI co-pilot) in building and maintaining the codebase. They are **not** part of the runtime Chimera agent environment.

#### Selected & Configured Developer MCP Servers

1. **git-mcp**
   - Purpose: Version control operations (commit, branch, diff, status).
   - Configuration: Standard stdio transport; auto-discovered in local dev environment.
   - Usage: Enables safe, traceable commits that tell the story of spec → test → implementation.

2. **filesystem-mcp**
   - Purpose: File editing, creation, reading, and navigation.
   - Configuration: Local filesystem access via stdio/SSE; restricted to project directory.
   - Usage: Primary tool for creating/modifying specs, tests, and stubs.

3. **browser-mcp** (or web-search-mcp)
   - Purpose: Research external documentation, MCP specs, or API references.
   - Configuration: Proxied through MCP Pulse[](https://mcppulse.10academy.org/proxy).
   - Usage: For clarifying SRS details or MCP tool schemas without leaving the IDE.

4. **python-repl-mcp** (optional but recommended)
   - Purpose: Quick validation of Pydantic schemas or contract testing.
   - Configuration: Local Python interpreter bridge.

#### Rationale

- These tools empower spec-driven, traceable development while keeping the runtime agent clean.
- All are local or proxied — no direct internet in agent runtime.
- Documented here for clarity and future reference.

### Sub-Task B: Agent Skills (Runtime)

Runtime skills are **internal, typed function packages** that the Chimera agent swarm (Workers) will call.  
They are **not** MCP servers themselves but will eventually be wrapped/exposed via MCP Tools when needed (e.g., for cross-agent collaboration).

Skills live in the `skills/` directory. Each skill is a Python module with:

- Clear Input/Output contracts (Pydantic models recommended).
- Stub implementation raising `NotImplementedError` (TDD compliance).
- No direct external calls — all external work routes through future MCP Tools.

See `skills/README.md` for detailed contracts of the initial critical skills.
