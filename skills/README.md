# skills/README.md

## Chimera Agent Runtime Skills

Skills are reusable, strongly-typed functions that Worker agents invoke during task execution.  
They are **internal** — no direct API calls. External interactions route through MCP Tools.

Each skill has:

- Explicit Input/Output contracts.
- Stub implementation (TDD-ready).

### Critical Skills

#### 1. `fetch_trends`

**Purpose**: Discover and rank trending topics relevant to the agent's niche.

**Input Contract**:

```json
{
  "niche": "string",
  "platforms": ["array[string]"],
  "time_window_hours": "integer (default: 24)",
  "max_results": "integer (default: 10)"
}
```
