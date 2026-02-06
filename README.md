# Project Chimera Factory

**Autonomous Influencer Agentic Infrastructure**

A spec-driven, governance-first repository designed as the "factory" for building reliable, scalable Autonomous AI Influencers using the FastRender Swarm pattern and Model Context Protocol (MCP).

## Vision

To create a codebase so well-specified, tested, and governed that a swarm of AI agents can enter and implement complex features with minimal human conflict or hallucination.  
This is **not** a quick prototype — it is engineered for agentic reliability at scale.

## Core Principles

- **Spec-Driven Development**: All implementation is gated behind ratified specifications in `specs/`.
- **Test-Driven Development**: All tests in `tests/` are intentionally failing — they define the "empty slots" agents must fill.
- **MCP Exclusive**: All external interactions (social platforms, generation tools, commerce) route through Model Context Protocol.
- **FastRender Swarm**: Internal coordination via Planner → Worker → Judge roles with confidence-based HITL and optimistic concurrency control.
- **Governance First**: CI/CD, AI code review (CodeRabbit), and strict separation of dev tools vs. runtime skills.

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
├── .github/workflows/ # CI/CD pipeline
├── .cursor/ # IDE agent rules (context for AI assistants)
├── research/ # Architecture strategy & tooling docs
├── specs/ # Source of truth specifications
├── skills/ # Runtime skill interfaces (contracts only)
├── tests/ # Failing tests (TDD goal posts)
├── Dockerfile # Containerized environment
├── Makefile # Standardized commands (or use uv directly)
├── pyproject.toml # Professional dependency management (uv)
└── README.md # This file

# Setup

# Prerequisites

Python 3.12+ (managed via uv)
uv
Docker (optional, for containerized testing)

Installation

# Install dependencies (creates virtual env)

uv sync

# Run Tests

pytest tests/ -v

# Or in Docker

make test

# Test change for CodeRabbit review

This is a dummy change to trigger AI review.
