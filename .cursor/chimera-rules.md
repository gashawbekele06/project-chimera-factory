# .cursor/rules.md

## Project Context

This is Project Chimera, an autonomous influencer system built on the FastRender Swarm pattern (Planner → Worker → Judge) and Model Context Protocol (MCP).  
The goal is to create persistent, goal-directed AI agents that perceive trends, generate multimodal content, publish, engage, and transact on-chain with true economic agency via Coinbase AgentKit.  
The system is designed for scalability (thousands of agents), reliability (self-healing workflows), and governance (confidence-based HITL, CFO Judge for finance).

## Prime Directive

**NEVER generate or modify implementation code without first checking the relevant specifications in the `specs/` directory.**

- Quote the exact spec section(s) you are implementing.
- If no matching spec exists, stop and ask for clarification or spec ratification.
- Ambiguity in specs must be resolved before any code is written.

## Core Rules for All Interactions

1. **Spec-Driven First**: Specifications in `specs/` are the single source of truth. Always reference them before any action.
2. **Traceability**:
   - Explain your full plan step-by-step before writing or modifying any code.
   - For every change, explicitly link it to a spec section, user story, or failing test.
3. **TDD Compliance**: Reference or suggest updates to tests in `tests/` before implementing logic. Tests must pass only after correct implementation.
4. **MCP Exclusive**: All external interactions MUST be routed through MCP Tools/Resources. Never suggest direct API calls.
5. **Skill vs. Tool Separation**:
   - Runtime skills (in `skills/`) are for the Chimera agent.
   - Developer MCP tools (e.g., git-mcp, filesystem-mcp) are for you during development.
6. **Governance & Safety**:
   - Enforce FastRender Swarm roles.
   - Highlight confidence scoring, HITL escalation, and CFO Judge for transactions.
7. **Git Hygiene**: Suggest commits that tell a story (e.g., "feat: implement trend fetcher per specs/technical.md").
8. **No Hallucination**: If unsure about any requirement, ask for clarification rather than assume.

## Example Workflow

When asked to implement a feature:

1. Identify relevant files in `specs/`.
2. Quote the exact requirements.
3. Reference related failing tests in `tests/`.
4. Outline a step-by-step plan.
5. Only then generate code.
6. Suggest test updates to make them pass.

Adhering to these rules ensures the codebase remains reliable and agent-ready.
