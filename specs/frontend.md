# Frontend Specification – Human Orchestrator & HITL Dashboard

**Version:** 1.0  
**Date:** February 06, 2026  
**Author:** Gashaw Bekele (FDE Trainee)

This specification defines the complete user-facing layer for Project Chimera. It includes:

- Inventory of all screens/dashboards/views
- User interaction flows (happy path, edge cases, failure modes)
- Component hierarchy & structure
- Accessibility standards (WCAG 2.1 AA)
- Exact mapping of each view to backend API contracts (from specs/technical.md) and returned data schemas

Goal: An AI coder agent can implement the entire frontend (React/Vue/Svelte + Tailwind or similar) without ambiguity or guesswork.

## 1. Overall Design Principles

- Framework: React 18 + TypeScript + Tailwind CSS + shadcn/ui components (or equivalent)
- State management: Zustand or Jotai (lightweight, no Redux boilerplate)
- Routing: React Router v6 (or TanStack Router)
- Authentication: JWT Bearer token stored in HttpOnly cookie (backend issues via /auth/login endpoint)
- Theme: Dark mode default (modern AI-agent aesthetic), light mode toggle
- Accessibility: WCAG 2.1 AA – semantic HTML, ARIA labels, keyboard navigation, sufficient color contrast
- Responsiveness: Mobile-first, breakpoints at 640px, 768px, 1024px, 1280px
- Internationalization: react-i18next (English default, Amharic planned)

## 2. Screen Inventory & User Flows

### 2.1 Login Screen (/login)

**Purpose**: Authenticate human orchestrator (admin / reviewer role).

**User Flow**:

- Happy path: Enter email/password → backend /auth/login → JWT set in cookie → redirect to /dashboard
- Edge case: Invalid credentials → show error toast "Invalid email or password"
- Failure mode: Network error → show "Unable to connect. Please try again."

**Components**:

- Email input (type=email, required, auto-focus)
- Password input (type=password, required)
- Submit button ("Sign In")
- "Forgot password?" link (→ /forgot-password placeholder)
- "Create account" link (→ /register placeholder)

**Backend Mapping**:

- POST /auth/login → { email, password }
- Response: 200 { token: string } → set HttpOnly cookie
- 401 → { error: "Invalid credentials" }

### 2.2 Dashboard Overview (/dashboard)

**Purpose**: High-level fleet status, quick actions, KPI overview.

**User Flow**:

- Happy path: Load → show summary cards (active agents, running campaigns, recent content, pending reviews)
- Edge case: No active agents → show "No agents online" placeholder with "Create New Agent" button
- Failure mode: API down → show cached data + error banner "Data may be outdated"

**Components**:

- Top nav bar (logo, agent count, notification bell, user avatar dropdown: profile, logout)
- KPI cards (4-column grid):
  - Active Agents (count, trend arrow)
  - Running Campaigns (count)
  - Pending Reviews (count + urgency badge)
  - Total Engagement (last 24h views/likes)
- Recent Content table (5 latest posts: thumbnail, caption snippet, platform icon, metrics, status badge)
- Quick Actions: "New Campaign", "Review Queue", "Agent List"

**Backend Mapping**:

- GET /dashboard/summary → { activeAgents: number, runningCampaigns: number, pendingReviews: number, engagement24h: { views: number, likes: number } }
- GET /content/recent?limit=5 → array of { id, thumbnailUrl, caption, platform, views, likes, status }

### 2.3 Review Queue (/review-queue)

**Purpose**: Human-in-the-loop approval/rejection of escalated content.

**User Flow**:

- Happy path: Load → paginated list of pending reviews → click item → show full preview (video/image/text) + approve/reject/edit form
- Edge case: Empty queue → "No pending reviews – all agents are confident" message
- Failure mode: Load error → retry button + offline fallback message

**Components**:

- Filter bar (by agent, urgency, time)
- Paginated table (columns: Agent, Content Type, Confidence Score, Created At, Actions)
- Detail modal/view:
  - Media preview (video player or image)
  - Generated caption/text
  - Confidence score badge (green/yellow/red)
  - Approve/Reject buttons (Approve auto-publishes, Reject → return to planner)
  - Edit form (override caption/media)

**Backend Mapping**:

- GET /review-queue?status=pending&limit=20&page=1 → array of { id, agentId, contentType, confidenceScore, createdAt, mediaUrl, caption }
- POST /review/{id}/approve → { approved: true }
- POST /review/{id}/reject → { rejected: true, reason: string }
- POST /review/{id}/edit → updated content

### 2.4 Agent List & Management (/agents)

**Purpose**: View, monitor, and manage all running agents.

**User Flow**:

- Happy path: Load → table of agents → click → detail view with status, current campaign, recent activity, wallet balance
- Edge case: No agents → "Create your first agent" wizard button
- Failure mode: API error → cached list + refresh button

**Components**:

- Table: Agent ID, Status (online/offline/busy), Niche/Persona, Current Campaign, Confidence Avg, Actions (pause, restart, delete)
- Detail panel: Live status card, Recent tasks list, Wallet balance (USDC), Memory usage

**Backend Mapping**:

- GET /agents → array of { id, status, niche, campaignId, avgConfidence, walletBalanceUsdc }
- GET /agents/{id} → detailed object

### 2.5 Campaign Management (/campaigns)

**Purpose**: Create, monitor, and pause high-level campaigns.

**User Flow**:

- Happy path: Create new → form (name, goal description, budget USDC, target platforms) → backend creates campaign → agents assigned
- Edge case: Budget exceeded → warning banner + pause option
- Failure mode: Creation error → form validation messages

**Components**:

- List view: Active/Paused/Completed campaigns
- Create form: Name, Goal (textarea), Budget (number), Platforms (multi-select)
- Detail view: Progress bar, Assigned agents, Total spend, Engagement metrics

**Backend Mapping**:

- POST /campaigns → { name, goalDescription, budgetUsdc, platforms }
- GET /campaigns → array of { id, name, status, budgetUsdc, spentUsdc, progress }

### 2.6 Component Hierarchy (High-Level)

- App
  - Layout (NavBar, Sidebar, MainContent)
    - NavBar (Logo, Agent Count, Notifications, User Menu)
    - Sidebar (Dashboard, Review Queue, Agents, Campaigns, Settings)
    - MainContent (Outlet for routes)
  - Screens (Login, Dashboard, ReviewQueue, Agents, Campaigns)

**Shared Components**:

- KPI Card
- Data Table (sortable, paginated)
- Media Preview (video player + thumbnail fallback)
- Confidence Badge (green/yellow/red)
- Toast Notifications (shadcn/ui)

**API Contract Mapping Summary**:

- All screens use typed API responses from specs/technical.md (Task/Result schemas)
- Frontend validates inputs against same JSON schemas (zod or yup)
- Error handling: 401 → redirect to login, 500 → error page with retry

This specification is complete enough for an AI agent to implement the full frontend (React + TypeScript) without ambiguity.

**Next steps**: Generate wireframes (optional: Figma link or ASCII art), implement component library, connect to backend APIs.
