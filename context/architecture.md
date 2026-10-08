# Architecture

The full system — both how it's structured in code and how it
runs in production. If reality and this doc disagree, fix one
of them.

## Stack

| Layer     | Technology                  | Role   |
| --------- | --------------------------- | ------ |
| Framework | [e.g. Next.js + TypeScript] | [Role] |
| UI        | [e.g. Tailwind + shadcn/ui] | [Role] |
| Auth      | [e.g. Clerk]                | [Role] |
| Database  | [e.g. Prisma + PostgreSQL]  | [Role] |
| [Layer]   | [Technology]                | [Role] |

## Topology

Diagram or ASCII sketch of services, data flow, and external
dependencies.

```
                ┌──────────────┐
   users ──────▶│  CDN / Edge  │
                └──────┬───────┘
                       ▼
                ┌──────────────┐       ┌──────────────┐
                │   API server │──────▶│   Postgres   │
                └──────┬───────┘       └──────────────┘
                       │
                       ▼
                ┌──────────────┐
                │  Worker queue│
                └──────────────┘
```

## Components

### [Component name]

- **Purpose:** [what it does]
- **Tech:** [language / framework / runtime]
- **Where it runs:** [cloud / region / service]
- **Scales how:** [horizontally / vertically / not at all]
- **Owner:** [initials]

_(Add one block per major component.)_

## System Boundaries

Folder ownership in the codebase.

- `[folder]` — [What this folder owns and is responsible for]
- `[folder]` — [What this folder owns and is responsible for]
- `[folder]` — [What this folder owns and is responsible for]
- `[folder]` — [What this folder owns and is responsible for]

## Storage Model

- **[Storage type — e.g. Database]:** [What lives here —
  e.g. metadata, ownership, relationships]
- **[Storage type — e.g. Blob/File Storage]:** [What lives
  here — e.g. generated files, media, large artifacts]

## Auth and Access Model

- [How authentication works — e.g. Every user signs in
  via Clerk]
- [How ownership works — e.g. Every project has a single
  owner]
- [How access control works — e.g. Only the owner or a
  collaborator can mutate project resources]

## External Dependencies

| Service | Purpose | Critical? | Failure mode |
|---------|---------|-----------|--------------|
| [e.g. Stripe] | [payments] | Yes | [queue retries; alert on >5min outage] |
| [e.g. Sentry] | [error tracking] | No | [degrade silently; logs still local] |

## Data Flow

Describe how data moves through the system, including any
async paths. Where does state live? What's idempotent vs.
not?

## Capacity & Scaling Assumptions

- Expected load: [e.g. 100 req/s peak]
- Bottleneck: [e.g. database writes]
- Scaling plan: [e.g. read replicas at 500 req/s]

## Invariants

Rules the codebase must never violate. Violations are bugs,
not trade-offs.

1. [Rule — e.g. Request handlers do not run long-lived
   background work]
2. [Invariant two]
3. [Invariant three]
4. [Invariant four]
