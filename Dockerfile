# Dockerfile

FROM python:3.14-slim

WORKDIR /app

# Install uv
RUN pip install --no-cache-dir uv

# Copy lockfile and pyproject.toml
COPY uv.lock pyproject.toml .

# Install dependencies into .venv
RUN uv sync --frozen

# Activate virtual environment by adding .venv/bin to PATH
ENV PATH="/app/.venv/bin:$PATH"

# Copy the rest of the project
COPY . .

# Default command: run failing tests
CMD ["pytest", "tests/", "-v"]