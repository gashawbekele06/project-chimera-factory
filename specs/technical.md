# specs/technical.md

## Technical Specifications

### API Contracts

#### Task Schema (Planner → Worker → Judge)

```json
{
  "type": "object",
  "properties": {
    "task_id": { "type": "string", "format": "uuid" },
    "task_type": {
      "type": "string",
      "enum": [
        "generate_content",
        "reply_comment",
        "publish_post",
        "execute_transaction",
        "perceive_trends"
      ]
    },
    "priority": { "type": "string", "enum": ["high", "medium", "low"] },
    "context": {
      "type": "object",
      "properties": {
        "goal_description": { "type": "string" },
        "persona_constraints": {
          "type": "array",
          "items": { "type": "string" }
        },
        "required_resources": {
          "type": "array",
          "items": { "type": "string" }
        },
        "budget_usdc": { "type": "number", "minimum": 0 }
      },
      "required": ["goal_description"]
    },
    "status": {
      "type": "string",
      "enum": ["pending", "in_progress", "review", "complete", "rejected"]
    },
    "confidence_score": { "type": "number", "minimum": 0, "maximum": 1 }
  },
  "required": ["task_id", "task_type", "context"]
}
```
