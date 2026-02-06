# skills/README.md

## Runtime Skills for Chimera Agents

These are reusable, typed capability packages that Worker agents call during task execution.  
Each skill has a **strict Input/Output contract** to prevent hallucinations and ensure testability.

Skills are **internal** — they orchestrate MCP Tool calls when needed but do not contain direct API logic.

### Critical Skills (Initial Set)

#### 1. `fetch_trends`

**Purpose**: Retrieve and filter current trending topics relevant to the agent's niche.

**Input Contract** (dict or Pydantic model):

```json
{
  "niche": "string (e.g., 'fashion', 'crypto')",
  "platforms": ["array[string] (e.g., ['twitter', 'tiktok'])"],
  "time_window_hours": "integer (default: 24)"
}
```
