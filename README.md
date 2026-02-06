# Project Chimera Factory

**Autonomous Influencer Agentic Infrastructure**

A spec-driven, governance-first repository designed as the "factory" for building reliable, scalable **Autonomous AI Influencers** using the **FastRender Swarm** pattern and **Model Context Protocol (MCP)**.

## Vision

To create a codebase so well-specified, tested, and governed that a swarm of AI agents can enter and implement complex features with minimal human conflict or hallucination.  
This is **not** a quick prototype — it is engineered for agentic reliability at scale.

## Core Principles

- **Spec-Driven Development** — All implementation is gated behind ratified specifications in `specs/`.
- **Test-Driven Development** — All tests in `tests/` are intentionally failing — they define the "empty slots" agents must fill.
- **MCP Exclusive** — All external interactions (social platforms, generation tools, commerce) route through Model Context Protocol.
- **FastRender Swarm** — Internal coordination via Planner → Worker → Judge roles with confidence-based HITL and optimistic concurrency control.
- **Governance First** — CI/CD, AI code review (CodeRabbit), and strict separation of dev tools vs. runtime skills.

## High-Level Architecture

Aligned with Project Chimera SRS §3.1:

```mermaid
graph TD
    A[Human Orchestrator<br>Goals + Dashboard] --> B[Planner]
    B --> C[Task Queue<br>(Redis)]
    C --> D[Worker Pool<br>(Parallel, Stateless)]
    D --> E[Review Queue<br>(Redis)]
    E --> F[Judge<br>(Confidence + CFO Sub-agent)]
    F -->|Approve| G[Commit State<br>(PostgreSQL + Weaviate)]
    F -->|Reject/Retry| B
    F -->|Escalate| H[HITL Review Dashboard]
    D --> I[MCP Servers<br>(Social, Generation, Coinbase, Trends)]
    B --> J[MCP Resources<br>(Perception Layer)]
    G --> K[Published Content<br>Social Platforms via MCP]
    G --> L[On-Chain Transactions<br>Coinbase AgentKit]
```

project-chimera-factory/
├── .github/
│ └── workflows/
│ └── main.yml # CI/CD: tests, lint, governance
├── .cursor/
│ └── chimera-rules.md # Prime Directive + state blocks
├── .vscode/
│ └── settings.json # MCP proxy, telemetry, Python config
├── docs/
│ ├── architecture_strategy.md # Day 1 report & architecture
│ ├── contributing.md # Branching, standards, workflow
│ └── adrs/ # Architecture Decision Records
│ ├── adr-001-database.md
│ ├── adr-002-mcp-exclusive.md
│ └── adr-003-non-goals.md
├── research/
│ └── tooling_strategy.md # MCP servers & tooling
├── specs/ # Source of truth specifications
│ ├── \_meta.md
│ ├── functional.md
│ ├── technical.md
│ ├── openclaw_integration.md
│ ├── frontend.md
│ ├── security.md
│ ├── acceptance_criteria.md
│ └── db_data_management.md
├── skills/ # Runtime skill contracts
│ ├── README.md
│ ├── fetch_trends/
│ ├── generate_video/
│ └── post_content/
├── tests/ # TDD failing tests
│ ├── **init**.py
│ ├── test_trend_fetcher.py
│ ├── test_skills_interface.py
│ └── README.md
├── config/
│ └── mcp.json # MCP servers, tools, schemas
├── .gitignore
├── Dockerfile # Containerized env
├── Makefile # Standardized commands
├── pyproject.toml # uv dependencies
├── uv.lock
└── README.md # This file

```bash
# 1. Clone the repository

git clone https://github.com/yourusername/project-chimera-factory.git
cd project-chimera-factory

# 2. Install dependencies (creates .venv)

uv sync

# 3. Verify setup

make test # should show failing TDD tests (expected)

make docker-build
make docker-test # runs tests inside container (should show same failures)

```

# Tests Directory – TDD Red Phase (Task 3.1)

These tests are **intentionally failing** — this is the required successful state.

Current status:

- 6 tests collected
- 3 failed (RuntimeError on missing credentials, NameError on missing functions) ← REQUIRED & SUCCESS
- 3 passed (schema validation, raises NotImplementedError)
- Total: 3 failed, 3 passed

```bash
make test
uv run pytest tests/ -v
```

Expected output: failures due to incomplete skills (empty slots).
