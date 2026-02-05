# Skill: fetch_trends

**Description**  
Retrieve current trending topics, hashtags, or search volumes from specified social platforms via MCP resource/tool.  
Enables the agent to perceive real-time trends for content alignment.

**Input Schema** (JSON passed to MCP Tool)

```json
{
  "type": "object",
  "properties": {
    "platforms": {
      "type": "array",
      "items": { "type": "string", "enum": ["twitter", "tiktok", "instagram"] },
      "minItems": 1
    },
    "region": {
      "type": "string",
      "description": "ISO 3166-1 alpha-2 code, e.g. 'ET' (Ethiopia), 'US', or 'global'"
    },
    "limit": {
      "type": "integer",
      "minimum": 5,
      "maximum": 50,
      "default": 10
    }
  },
  "required": ["platforms"]
}
```
