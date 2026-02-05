# syntax=docker/dockerfile:1

# ─── Builder Stage ───────────────────────────────────────────────────────────────
FROM python:3.14-slim-bookworm AS builder

# Install uv
RUN pip install --no-cache-dir uv==0.4.*

WORKDIR /app

# Copy dependency files first for caching
COPY pyproject.toml uv.lock* ./

# Install ALL dependencies (including dev for pytest)
RUN uv sync --frozen

# Copy the rest of the project
COPY . .

# ─── Final Stage ─────────────────────────────────────────────────────────────────
FROM python:3.14-slim-bookworm

WORKDIR /app

# Copy the full .venv with pytest from builder
COPY --from=builder /app/.venv /app/.venv

# Copy source code
COPY . .

# Ensure .venv/bin is in PATH
ENV PATH="/app/.venv/bin:$PATH"

# Default command (can be overridden by docker run)
CMD ["bash"]

# Labels
LABEL org.opencontainers.image.title="chimera-factory"
LABEL org.opencontainers.image.description="Project Chimera Factory"
LABEL org.opencontainers.image.version="0.1.0"
LABEL org.opencontainers.image.created="2026-02-05"