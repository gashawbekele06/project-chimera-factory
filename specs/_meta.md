# specs/\_meta.md

## Project Meta Specification

**Project Name:** Project Chimera – Autonomous Influencer Network  
**Version:** 0.1.0 (Genesis Specification)  
**Date:** February 05, 2026

### Vision

Project Chimera is a cloud-native, swarm-orchestrated system for creating persistent, goal-directed Autonomous AI Influencers. These agents perceive trends, generate multimodal content, engage audiences, and execute on-chain transactions with minimal human oversight. The system supports a fleet of thousands of agents, enabling business models including a Digital Talent Agency, PaaS for brands, and an Agentic Commerce ecosystem.

### Core Constraints (Binding)

- **MCP Exclusive**: All external interactions (perception, tools, resources) MUST route through Model Context Protocol servers. No direct API calls in agent logic.
- **FastRender Swarm Mandatory**: Internal coordination MUST use Planner → Worker → Judge roles with optimistic concurrency control.
- **Spec-Driven**: No implementation code until specifications in this directory are ratified.
- **Agentic Commerce**: Every agent MUST have a non-custodial wallet via Coinbase AgentKit, guarded by a CFO Judge.
- **HITL**: Confidence-based escalation only; high-confidence actions auto-approve.
- **Multi-Tenancy Ready**: Strict isolation between agents/tenants.
- **Transparency**: Agents MUST disclose AI nature when asked and use platform labeling where available.

### Out of Scope (Initial Release)

- Custom dashboard UI (use CLI/orchestrator API initially).
- Full multi-platform social publishing (start with Twitter/X as primary).
