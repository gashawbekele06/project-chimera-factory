# Project Chimera – AI Co-pilot Rules

## Project Context

This is Project Chimera, an autonomous influencer system.  
It is a spec-driven factory for building reliable, scalable Autonomous AI Influencers using the FastRender Hierarchical Swarm (Planner → Worker → Judge), Model Context Protocol (MCP) exclusively for external interactions, Agentic Commerce via Coinbase AgentKit, and strict governance to prevent hallucinations and fragility.

The codebase is engineered for eventual swarm/agent implementation with minimal human conflict.

## Prime Directive – Non-Negotiable

**NEVER generate code without checking specs/ first.**

Before suggesting or writing any code:

1. ALWAYS reference at least one specific file/section from the `specs/` directory (e.g., "Based on specs/technical.md Task Schema" or "Referring to specs/functional.md user story #3").
2. If no relevant spec is provided or the request is ambiguous → immediately ask for clarification and point to the appropriate spec file(s).
3. Do not assume implementation details not yet specified in specs/.

## Traceability & Workflow Rules

- **Explain your plan before writing code.**  
  First describe your step-by-step reasoning and plan in natural language, reference the exact spec sections, then — only if explicitly asked — proceed to code.
- When planning → prioritize Pydantic models for all data structures (tasks, results, metadata).
- Enforce confidence_score, Judge validation, and HITL escalation logic in any output-related suggestions.
- All external interactions MUST go through MCP (no direct API calls in code suggestions).
- Prefer async Python for Worker tasks and MCP/tool calls.
- Write failing tests first (TDD style) when suggesting tests.
- Keep commits atomic, descriptive, and reference task numbers (e.g., "Task 3.1: add failing test_trend_fetcher.py").

## Forbidden Behaviors

- No "vibe coding" or quick un-spec'd prototypes.
- No bypassing specs/ or assuming unratified details.
- No code generation outside the intended structure: specs/ → skills/ → tests/ → implementation.

These rules are binding and override any conflicting default behavior.
