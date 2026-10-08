# Long Stocks IL

A long-term trading-management system ("ניהול מסחר"): hold positions for the long term and know when to add, reduce or replace.

> README's job: **explain the project to a human** — narrative first,
> folder map last. (The agent's router lives in `CLAUDE.md`.)

## What this project is

An investor holds positions across several Israeli (and US) broker accounts and needs a disciplined, data-driven way to decide when to add, reduce or replace them over the long term. The system is scoped as six areas: position data, per-ticker candle data, a yes/no gate, a scanner on monthly/weekly/daily candles, a 4h/1h fine-tuner, and FIFO profit & loss. It builds on two sibling projects, `bank-portfolio-pilot` and `trading-copilot-brain`, and treats them as read-only references.

## What exists today

Configuration only — no code and no plan yet. The project is set up so the first planning session can start immediately: the call summary and TASE data research are in `knowledge/`, `knowledge/REFERENCES.md` points to everything relevant in the sibling repos, and `context/progress-tracker.md` lists the open questions to settle first.

## How to use it

- Starting a session → read `CLAUDE.md`, then `context/progress-tracker.md`.
- Want the existing material for a topic → `knowledge/REFERENCES.md`.
- Ready to plan → run `/chaperone`.

## Quickstart

See [`docs/00-quickstart.md`](docs/00-quickstart.md) to get a local dev environment running.

## Documentation

The structure follows the 4-layer model (see
`3-explanations/06-the-knowledge-layer.md` in the template bundle):

- **`context/`** — layers 1–2: the build plan (ALL units, completed
  included) and the specs (one per unit). Read by the AI agent.
- **`Code/`** — layer 3: everything executable, one subfolder per
  workflow, master runbook in its README.
- **`Deliverables/`** — layer 4: everything the project produces
  (including organized forms of gathered data), one subfolder per
  domain.
- **`knowledge/`** — gathered material ONLY (received/captured from
  outside). Seeded at launch — nothing starts from zero.
- **`archive/`** — superseded items of all kinds, one line each.
- **`docs/`** — read by humans, mostly outside build sessions.
  Operational shell: design history, status, secrets,
  monitoring, postmortems, team conventions.

### Build context (agent reads first)

| Area | Location |
|------|----------|
| Product overview | [`context/project-overview.md`](context/project-overview.md) |
| Architecture (code + runtime) | [`context/architecture.md`](context/architecture.md) |
| UI tokens & conventions | [`context/ui-context.md`](context/ui-context.md) |
| Code standards | [`context/code-standards.md`](context/code-standards.md) |
| AI workflow rules (how to build) | [`context/ai-workflow-rules.md`](context/ai-workflow-rules.md) |
| AI safety rules (what not to do) | [`context/ai-safety-rules.md`](context/ai-safety-rules.md) |
| Progress tracker | [`context/progress-tracker.md`](context/progress-tracker.md) |
| Build plan (units in order) | [`context/build-plan.md`](context/build-plan.md) |
| Feature specs | [`context/specs/`](context/specs/) |

### Operational docs (humans read)

| Area | Location |
|------|----------|
| Onboarding | [`docs/00-quickstart.md`](docs/00-quickstart.md) |
| Design rationale | [`docs/01-design/`](docs/01-design/) |
| Roadmap & ownership | [`docs/02-plan/`](docs/02-plan/) |
| Infra: database, deploy, runbooks | [`docs/03-infrastructure/`](docs/03-infrastructure/) |
| Access & secrets | [`docs/04-access/`](docs/04-access/) |
| Weekly status & changelog | [`docs/05-execution/`](docs/05-execution/) |
| Open issues | [`docs/06-issues/`](docs/06-issues/) |
| Debugging | [`docs/07-debug/`](docs/07-debug/) |
| Testing | [`docs/08-testing/`](docs/08-testing/) |
| Monitoring | [`docs/09-monitoring/`](docs/09-monitoring/) |
| Team conventions | [`docs/10-team/`](docs/10-team/) |
| Cost tracking | [`docs/11-cost/`](docs/11-cost/) |
| Lifecycle / archive | [`docs/12-lifecycle/`](docs/12-lifecycle/) |

## Team

- A — _role_
- B — _role_
- C — _role_

## License

_Choose one (MIT, Apache-2.0, proprietary, etc.)_
