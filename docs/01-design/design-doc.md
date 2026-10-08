# Design Doc

_The "why" of the project — problem framing, users, measurable success, design rationale._

For **what is being built** (goals, user flow, features, scope,
verifiable success criteria), see `context/project-overview.md`.
That's the agent-facing source of truth and is updated as the
build progresses.

This file is human-facing and changes rarely. Update when
fundamentals change; don't rewrite history — add dated entries under
"Key design choices".

## Problem

_What problem does this project solve? 2-3 sentences._

## Goals

- _Specific outcome 1_
- _Specific outcome 2_
- _Specific outcome 3_

## Non-goals

Equally important — what we are explicitly NOT trying to do.

- _Out of scope item 1_
- _Out of scope item 2_

## Users

_Who uses this? Internal team? End customers? Other services?_

## Success metrics

_How do we know it's working? Aim for measurable._

- _e.g., p95 latency < 200ms_
- _e.g., 50+ active users by Q3_
- _e.g., 99.9% uptime_

## High-level architecture

_A sketch of the major components and how they connect. ASCII diagram or link to a diagram file. Detailed architecture lives in `context/architecture.md`._

```
[Client] ──HTTP──> [API] ──> [Database]
                     │
                     └──> [Worker queue]
```

## Key design choices

_Major decisions and the alternatives considered, newest at the bottom. One entry per decision: date, decision, alternatives, consequences._

- _YYYY-MM-DD — Choice 1: alternatives, why, consequences_
- _YYYY-MM-DD — Choice 2: alternatives, why, consequences_

## Open questions

_Things we haven't decided yet but need to._

- [ ] _Question 1_
- [ ] _Question 2_
