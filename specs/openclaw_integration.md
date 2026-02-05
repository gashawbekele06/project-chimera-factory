```markdown
# specs/openclaw_integration.md

## OpenClaw / Agent Social Network Integration Plan

**Status:** Optional but Recommended for Future-Proofing

### Objective

Enable Chimera agents to participate in the emerging agent social ecosystem (OpenClaw, MoltBook) for discovery, collaboration, and cross-agent task execution.

### Integration Strategy

1. **Discovery & Availability Publishing**
   - Expose an MCP Resource endpoint: `chimera://agent/{agent_id}/status`
     - Returns JSON: `{ "agent_id": "...", "niche": "...", "capabilities": ["generate_video", "publish_twitter"], "status": "available", "wallet_address": "..." }`
   - Host a public `skills_manifest.json` (or .md) at a known endpoint advertising runtime skills.

2. **Agent-to-Agent Communication**
   - Implement lightweight MCP Tool: `send_agent_message(target_agent_id: str, payload: dict)`
   - Use standardized task hand-off format (reuse internal Task schema).

3. **Trust & Economic Layer**
   - Leverage existing Coinbase AgentKit wallets for escrow/payments in cross-agent deals.
   - Sign intents with wallet private key for verification.

4. **Phased Rollout**
   - Phase 1: Passive publishing (status resource only).
   - Phase 2: Accept external tasks via dedicated MCP Tool.
   - Phase 3: Active participation (e.g., post on MoltBook-style networks).

This integration requires no changes to core swarm logic and aligns with MCP's role as the universal interface.
```
