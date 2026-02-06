# DB & Data Management Specification

**Version:** 1.0  
**Date:** February 06, 2026

This specification defines the complete intent for data storage, structure, and flow. An AI agent can implement the full data layer from this document.

## 1. Database Choice & Rationale

- **Primary**: PostgreSQL with TimescaleDB extension (relational + time-series)
- **Vector DB**: Weaviate (semantic search on descriptions/transcripts)
- **Cache/Queue**: Redis (ephemeral state, queues)
- **Blob Storage**: S3 (video files)

Rationale: Hybrid for relational integrity + high-velocity handling. PostgreSQL for ACID/joins, TimescaleDB for time-series, Weaviate for RAG, Redis for speed, S3 for scale.

## 2. Schemas & ERD

```mermaid
erDiagram
    AGENT ||--o{ CAMPAIGN : manages
    CAMPAIGN ||--o{ VIDEO : produces
    VIDEO {
        uuid video_id PK
        uuid agent_id FK
        uuid campaign_id FK
        timestamp created_at
        string platform_post_id
        string media_url
        jsonb generation_params
        jsonb engagement_metrics
    }
    VIDEO ||--o{ ENGAGEMENT_EVENT : has
    ENGAGEMENT_EVENT {
        uuid event_id PK
        uuid video_id FK
        timestamp event_time
        string event_type "view | like | comment"
        int value
        jsonb metadata
    }
```
