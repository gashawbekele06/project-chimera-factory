### File 5: skills/post_content/README.md

````markdown
# Skill: post_content

**Description**  
Publish approved text, image, or video content to social platforms with AI disclosure flag via MCP tool.

**Input Schema**

```json
{
  "type": "object",
  "properties": {
    "platform": {
      "type": "string",
      "enum": ["twitter", "instagram", "tiktok"]
    },
    "text_content": { "type": "string", "maxLength": 280 },
    "media_urls": {
      "type": "array",
      "items": { "type": "string", "format": "uri" }
    },
    "disclosure_level": {
      "type": "string",
      "enum": ["automated", "assisted", "none"],
      "default": "automated"
    },
    "thread_id": { "type": "string", "description": "For replies or threads" }
  },
  "required": ["platform", "text_content"]
}
```
````
