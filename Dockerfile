# syntax=docker/dockerfile:1

# === Stage 1: Builder (install deps, cache layers) ===
FROM python:3.14-slim-bookworm AS builder

# Install uv (pinned version for reproducibility)
RUN pip install --no-cache-dir uv==0.4.29

WORKDIR /app

# Copy only dependency files first → excellent caching
COPY pyproject.toml uv.lock* ./

# Install ALL dependencies (dev + prod) for testing
RUN uv sync --frozen --all-extras --no-install-project

# Copy the rest of the source code (after deps → cache hit on deps)
COPY . .

# === Stage 2: Runtime (minimal, secure image) ===
FROM python:3.14-slim-bookworm

WORKDIR /app

# Copy only the virtualenv from builder (small & fast)
COPY --from=builder /app/.venv /app/.venv

# Copy source code
COPY . .

# Ensure venv binaries are on PATH
ENV PATH="/app/.venv/bin:$PATH"

# Metadata labels (good practice)
LABEL org.opencontainers.image.title="chimera-factory"
LABEL org.opencontainers.image.description="Project Chimera Factory – Autonomous AI Influencer Infrastructure"
LABEL org.opencontainers.image.version="0.1.0"
LABEL org.opencontainers.image.created="2026-02-06"

# Default command (bash for interactive debugging)
CMD ["bash"]