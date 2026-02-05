# Project Chimera: Domain Architecture Strategy

**Date:** February 05, 2026  
**Author:** Forward Deployed Engineer (FDE) Trainee

This document fulfills **Task 1.2** of the Project Chimera 3-Day Challenge. It is created **before any implementation code** and serves as a strategic plan based on the Software Requirements Specification (SRS), challenge guidelines, and research insights. All decisions prioritize reliability, governance, scalability, and strict adherence to Spec-Driven Development.

## 1. Agent Pattern Selection

### Chosen Pattern: FastRender Hierarchical Swarm (Planner → Worker → Judge)

The **FastRender Swarm** pattern defined in SRS §3.1 is the clear best fit.

#### Rationale

- Provides **parallel execution** via stateless Workers while maintaining strong governance through the Judge role.
- Enables **dynamic re-planning** (Planner reacts to new perceptions such as trends or mentions).
- Includes **built-in quality and safety gates** (Judge enforces persona, confidence thresholds, and can escalate or reject).
- Supports **optimistic concurrency control** to prevent state conflicts.
- Explicitly designed for complex, multi-step tasks like multimodal content creation and engagement.

#### Rejected Alternatives

- **Sequential Chain**: Linear, fragile, no parallelism, and no dedicated quality layer — unsuitable for high-velocity autonomous workflows.
- **Pure Hierarchical Swarm (no defined roles)**: Lacks explicit governance and error recovery mechanisms.
- **Monolithic Agent**: Cannot scale and violates SRS requirements for swarm coordination.

This pattern directly supports the project's goal of self-healing, exception-based orchestration for a fleet of thousands of agents.

## 2. Human-in-the-Loop (HITL) – Safety Layer

### Placement: Integrated into the Judge Role (Confidence-Based Escalation)

HITL is positioned **exclusively within the Judge component**, as specified in SRS NFR 1.0–1.2.

#### Mechanism

- Every Worker output includes a `confidence_score` (0.0–1.0).
- Judge routing logic:
  - **> 0.90**: Auto-approve.
  - **0.70–0.90**: Pause task and add to async HITL queue (agent continues other work).
  - **< 0.70**: Auto-reject and return to Planner for retry.
- **Mandatory escalation** for sensitive topics (politics, health, finance, etc.) regardless of score.
- Humans interact via a dedicated Review Dashboard (Approve/Reject/Edit).

#### Why Here?

- Centralizes safety without bottlenecking high-confidence actions.
- Maximizes agent autonomy while ensuring brand and ethical compliance.
- Aligns with "management by exception" philosophy.

## 3. Database Strategy: SQL vs NoSQL for High-Velocity Video Metadata

### Recommendation: Hybrid – PostgreSQL (SQL) Primary + Complementary Systems

#### Metadata Characteristics

- Structured fields: `video_id`, `agent_id`, `timestamp`, `platform_post_id`, `media_url`, `generation_params` (JSON), engagement metrics (views/likes over time).
- High write velocity (potentially thousands/day across fleet).
- Query needs: joins with agents/campaigns, time-series analytics, filtering.

#### Decision: PostgreSQL with TimescaleDB Extension

- **Why SQL (PostgreSQL)**:
  - Strong consistency and relational integrity (foreign keys, ACID).
  - Efficient joins for campaign reporting and analytics.
  - TimescaleDB hypertables handle high-velocity time-series ingestion with NoSQL-like performance.
  - Explicitly required in SRS §2.3 for transactional data.
- **Why Not Pure NoSQL**:
  - Schema flexibility is unnecessary (metadata schema is stable).
  - Weaker joins and consistency would complicate reliable reporting and wallet linkages.

#### Complementary Storage

- **Weaviate**: Vector storage for semantic search on video descriptions/transcripts.
- **Object Storage (e.g., S3)**: Raw video binaries (database stores URLs only).
- **Redis**: Cache frequently accessed metadata.

## 4. Architecture Diagrams

### Overall System Flow

```mermaid
graph TD
    A[Human Orchestrator<br/>Goals + Dashboard] --> B[Planner]
    B --> C[Task Queue<br/>(Redis)]
    C --> D[Worker Pool<br/>(Parallel, Stateless)]
    D --> E[Review Queue<br/>(Redis)]
    E --> F[Judge<br/>(Confidence + CFO Sub-agent)]
    F -->|Approve| G[Commit State<br/>(PostgreSQL + Weaviate)]
    F -->|Reject/Retry| B
    F -->|Escalate| H[HITL Review Dashboard]
    D --> I[MCP Servers<br/>(Social, Generation, Coinbase, Trends)]
    B --> J[MCP Resources<br/>(Perception Layer)]
    G --> K[Video Metadata<br/>(PostgreSQL/TimescaleDB)]
    K --> L[S3 Object Storage<br/>(Video Files)]
```
