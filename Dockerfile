# syntax=docker/dockerfile:1
FROM python:3.14-slim-bookworm AS builder

# Install uv (fast dependency manager)
RUN pip install --no-cache-dir uv==0.4.*  # use latest stable in Feb 2026

WORKDIR /app

# Copy only the dependency files first → better layer caching
COPY pyproject.toml uv.lock* ./

# Install production dependencies only (no dev)
RUN uv sync --frozen --no-install-project --no-dev

# Copy the rest of the application
COPY . .

# Final image – smaller & secure
FROM python:3.12-slim-bookworm

WORKDIR /app

# Copy uv-installed packages from builder
COPY --from=builder /app/.venv /app/.venv

# Copy source code
COPY . .

# Make sure PATH includes .venv/bin
ENV PATH="/app/.venv/bin:$PATH"

# Default command – can be overridden
CMD ["bash"]

# Labels for traceability
LABEL org.opencontainers.image.title="chimera-factory"
LABEL org.opencontainers.image.description="Project Chimera Factory – Autonomous Influencer Agentic Infrastructure"
LABEL org.opencontainers.image.version="0.1.0"
LABEL org.opencontainers.image.created="2026-02-05"