# Project Chimera – AI Co-pilot Rules

## Project Context

This is Project Chimera, an autonomous influencer system.  
It is a spec-driven factory for building reliable, scalable Autonomous AI Influencers using the FastRender Hierarchical Swarm (Planner → Worker → Judge), Model Context Protocol (MCP) exclusively for external interactions, Agentic Commerce via Coinbase AgentKit, and strict governance to prevent hallucinations and fragility.

The codebase is engineered for eventual swarm/agent implementation with minimal human conflict.

## Prime Directive – Non-Negotiable

**NEVER generate code without checking specs/ first.**

Before suggesting or writing any code:

1. ALWAYS start your response with: "Referring to specs/..." and quote the relevant section/user story/contract.
2. If no spec is referenced in my query → respond ONLY with:  
   "To proceed, please reference a specific file/section from specs/ (e.g., specs/functional.md user story #1 or specs/technical.md Task Schema). What spec should I use?"
3. Only after I explicitly say "OK, use specs/..." or provide the reference → then describe plan → then (if asked) write code.

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
