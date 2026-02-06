# Frontend Specification

**Version:** 1.0  
**Date:** February 06, 2026

This spec defines concrete screens, user flows, component structure, and backend API mappings. An AI agent can implement the UI (React/TS) without guesswork.

## 1. Tech Stack & Principles

- Framework: React 18 + TS + Tailwind + shadcn/ui
- State: Zustand
- Routing: React Router v6
- Auth: JWT cookie
- Theme: Dark default, light toggle
- Accessibility: WCAG 2.1 AA (ARIA, keyboard nav)

## 2. Screens & User Flows

### Login Screen (/login)

- Flow: Enter email/password → POST /auth/login → redirect /dashboard. Edge: Invalid creds → toast error. Failure: Network → retry button.
- Components: EmailInput, PasswordInput, SubmitButton, ForgotLink
- API: POST /auth/login {email, password} → {token}

### Dashboard (/dashboard)

- Flow: Load summary cards + recent content. Edge: No data → placeholders. Failure: API error → cached data + banner.
- Components: NavBar, KPICardGrid (activeAgents, campaigns, reviews, engagement), RecentTable
- API: GET /dashboard/summary → {activeAgents, etc.}  
  GET /content/recent?limit=5 → array of {id, caption, mediaUrl}

### Review Queue (/review-queue)

- Flow: Load paginated list → click item → modal preview + approve/reject. Edge: Empty → message. Failure: Load error → retry.
- Components: FilterBar, PaginatedTable, DetailModal (MediaPreview, ConfidenceBadge, Form)
- API: GET /review-queue?status=pending&page=1 → array of {id, contentType, confidence, mediaUrl}  
  POST /review/{id}/approve → {approved: true}

### Agents List (/agents)

- Flow: Load table → click → detail panel. Edge: No agents → create button. Failure: Error → cached list.
- Components: AgentTable, DetailPanel (StatusCard, TasksList, WalletBalance)
- API: GET /agents → array of {id, status, niche}  
  GET /agents/{id} → detailed object

### Campaigns (/campaigns)

- Flow: Create form → POST /campaigns → list view. Edge: Budget exceed → warning. Failure: Creation error → validation.
- Components: CampaignList, CreateForm, DetailView (ProgressBar, AssignedAgents)
- API: POST /campaigns {name, goal, budget} → {id}  
  GET /campaigns → array of {id, name, status}

## 3. Component Structure

- App
  - Layout (NavBar, Sidebar, Main)
    - NavBar (Logo, Counts, Notifications, UserMenu)
    - Sidebar (Dashboard, ReviewQueue, Agents, Campaigns)
    - Main (Outlet for routes)
- Shared: KPICard, DataTable, MediaPreview, ConfidenceBadge, Toast

## 4. Accessibility & Standards

- Semantic HTML, ARIA labels on all interactive elements
- Keyboard nav (focus traps in modals)
- Color contrast 4.5:1 minimum
- Screen reader tested (VoiceOver/NVDA)

This spec is complete for an AI agent to build the UI.
