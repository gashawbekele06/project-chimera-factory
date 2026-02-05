### File 4: skills/generate_video/README.md

````markdown
# Skill: generate_video

**Description**  
Generate short-form video content (e.g., 15–60s TikTok-style clip) matching agent persona, using text prompt, images, or audio via MCP generation tool.

**Input Schema**

```json
{
  "type": "object",
  "properties": {
    "prompt": {
      "type": "string",
      "description": "Detailed video description / script"
    },
    "persona_id": {
      "type": "string",
      "description": "Reference to SOUL.md persona"
    },
    "duration_seconds": {
      "type": "integer",
      "minimum": 5,
      "maximum": 120,
      "default": 30
    },
    "style": {
      "type": "string",
      "enum": ["realistic", "animated", "cinematic"]
    },
    "resolution": {
      "type": "string",
      "enum": ["720p", "1080p"],
      "default": "1080p"
    },
    "audio_enabled": { "type": "boolean", "default": true }
  },
  "required": ["prompt", "persona_id"]
}
```
````
