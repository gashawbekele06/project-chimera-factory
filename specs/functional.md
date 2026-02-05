# specs/functional.md

## Functional Specifications

Functional requirements are expressed as agent-centric user stories.

### Core Agent Capabilities

- As a Chimera Agent, I need to maintain a persistent persona (via SOUL.md + hierarchical memory) so that my voice and behavior remain consistent across interactions.
- As a Chimera Agent, I need to perceive the world via MCP Resources (trends, mentions, news) so that I can react to relevant events.
- As a Chimera Agent, I need to decompose high-level campaign goals into executable tasks via the Planner so that I pursue objectives strategically.
- As a Chimera Agent, I need to generate multimodal content (text, images, videos) using specialized MCP Tools so that I can create engaging posts.
- As a Chimera Agent, I need to publish content and engage (replies, likes) via MCP Tools so that I build audience relationships.
- As a Chimera Agent, I need to execute on-chain transactions (via Coinbase AgentKit) with CFO Judge approval so that I can earn, spend, and manage resources autonomously.
- As a Chimera Agent, I need to evolve my persona by incorporating high-engagement memories so that I improve over time.

### Swarm Roles

- As a Planner, I need to monitor global state and generate/re-plan task DAGs so that the agent pursues goals efficiently.
- As a Worker, I need to execute atomic tasks using MCP Tools and return results so that complex workflows complete.
- As a Judge, I need to review Worker outputs for quality, safety, and confidence, approving/rejecting/escalating so that only aligned actions proceed.

### Orchestrator & Human

- As a Human Orchestrator, I need to set high-level campaign goals and monitor fleet health so that I direct strategy without micromanagement.
- As a Human Reviewer, I need a simple dashboard to approve/reject escalated content so that safety is maintained with minimal effort.
