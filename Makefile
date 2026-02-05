# Makefile for Project Chimera Factory
# Standard commands for setup, test, and optional checks

SHELL := /bin/bash
PYTHON := python
UV := uv
DOCKER := docker
IMAGE_NAME := chimera-factory
TAG := latest

# ────────────────────────────────────────────────
# Help / Default
# ────────────────────────────────────────────────

.PHONY: help
help: ## Show this help message
	@echo "Project Chimera Factory – Makefile commands"
	@echo "───────────────────────────────────────────────"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help

# ────────────────────────────────────────────────
# Setup & Dependencies
# ────────────────────────────────────────────────

.PHONY: setup
setup: ## Install all dependencies using uv
	$(UV) sync --frozen

.PHONY: setup-dev
setup-dev: setup ## Install dev dependencies too
	$(UV) sync --frozen --extra dev

# ────────────────────────────────────────────────
# Docker
# ────────────────────────────────────────────────

.PHONY: docker-build
docker-build: ## Build Docker image
	$(DOCKER) build -t $(IMAGE_NAME):$(TAG) .

.PHONY: docker-test
docker-test: docker-build ## Run tests inside Docker container
	$(DOCKER) run --rm $(IMAGE_NAME):$(TAG) pytest tests/

# ────────────────────────────────────────────────
# Testing
# ────────────────────────────────────────────────

.PHONY: test
test: ## Run all tests (local)
	$(UV) run pytest tests/ -v

.PHONY: test-cov
test-cov: ## Run tests with coverage
	$(UV) run pytest tests/ --cov --cov-report=term-missing

# ────────────────────────────────────────────────
# Spec / Code Alignment Check (optional but recommended)
# ────────────────────────────────────────────────

.PHONY: spec-check
spec-check: ## Basic check: grep for common spec violations (customize as needed)
	@echo "Checking for direct API calls outside MCP..."
	@grep -r -E "(requests\.get|httpx\.get|urllib|tweepy)" . --exclude-dir={.git,.venv,tests,specs,skills} || echo "No direct API calls found outside MCP (good)"
	@echo ""
	@echo "Checking for missing spec references in code comments..."
	@grep -r -E "specs/" . --include="*.py" || echo "No spec references in code yet (expected at this stage)"
	@echo ""
	@echo "Spec-check complete. Customize this target further if needed."