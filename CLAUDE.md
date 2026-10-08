# CLAUDE.md

Team-wide conventions for this project. Claude Code reads this at the start of every session — keep it short, accurate, and committed to the repo.

Personal preferences belong in `~/.claude/CLAUDE.md`, not here.

---

## Application Building Context

Before implementing or making any architectural decision,
read the following files in order:

1. `context/project-overview.md` — product definition,
   goals, features, and scope
2. `context/architecture.md` — system structure (code +
   runtime), boundaries, storage model, and invariants
3. `context/ui-context.md` — theme, colors, typography,
   and component conventions
4. `context/code-standards.md` — implementation rules
   and conventions
5. `context/ai-workflow-rules.md` — how to build:
   scoping, splitting work, verification
6. `context/ai-safety-rules.md` — what not to do:
   destructive ops, secrets, protected files
7. `context/progress-tracker.md` — current phase,
   completed work, open questions, next steps

When working on a feature, also read the relevant spec
file in `context/specs/`.

**Read on demand outside build work.** The sequence above is
for sessions that implement or make architectural decisions.
For anything else (a question, an ops task, debugging, a
lookup), do NOT preload all seven files — use the "Where to
find things" table below as a router and read only the file
the task needs.

Update `context/progress-tracker.md` after each meaningful
implementation change.

If implementation changes the architecture, scope, or
standards documented in the context files, update the
relevant file before continuing. For non-trivial design
decisions, create an ADR via `/new-adr`.

### Chaperone mode

If the user runs `/chaperone` or pastes `chaperone.md`, take
over as the workflow driver. Read `chaperone.md` for the full
operating rules. Short version: ask one question at a time,
announce every file read/write, always tell the user what's
next. Exit on "stop" or "I'll drive".

### Multi-user repo

If more than one teammate works in this repo, treat
`context/progress-tracker.md` as the shared coordination point.
Before working on a unit, `/lock-unit NN initial` claims it.
`/release-unit NN` releases it. See `docs/10-team/team-sync.md`
for the full sync conventions.

---

## Project

Long Stocks IL ("ניהול מסחר") is a long-term trading-management system for a
single investor: hold positions long term and know when to add, reduce or
replace. Six areas: position data, ticker/candle data, yes/no gate, scanner
(monthly/weekly/daily), fine-tune (4h/1h), FIFO P&L. It sits between
`bank-portfolio-pilot` (portfolio direction from index candles) and
`trading-copilot-brain` (short-term intraday). **Current phase: configured,
not yet planned** — see `context/progress-tracker.md` for the open questions
to settle first. Do not invent design; undecided items stay marked **[open]**.

## Stack

Not decided yet (planning session). The sibling projects use Python/FastAPI on
Railway, n8n, and Supabase (Postgres) — a shared instance, so a new schema
here would live beside `bpp`. Treat that as precedent, not a decision.

## Team

| Person | Primary area | Backup for |
|--------|--------------|------------|
| _[open]_ | The call names Sharon (שרון) and Einat (עינת); roles unconfirmed | — |

## Sibling repos (read-only reference)

All in `c:\Users\dell\Documents\GitHub\`, readable without prompts via
`.claude/settings.json` → `additionalDirectories`. What to read in each, by
area: **`knowledge/REFERENCES.md`**. Never write to a sibling repo from here.

| Repo | Folder | Note |
|---|---|---|
| bank-portfolio-pilot | `../bank-portfolio-pilot` | **`git pull` first** — local checkout was 3 months behind GitHub on 2026-10-08 |
| trading-copilot-brain | `../trading-copilot-brain-22092026` | Short-term; clone name carries a date |
| Template library | `../Claude-Code-Project-Configuration` | Methodology source; never edit it from here |

The Supabase MCP reaches the shared instance; use it **read-only** here
(no schema changes without explicit approval).

## Where to find things

- **Build context (read first)** → `context/`
  - Product, architecture, code/UI/AI rules, progress
  - Feature specs (one per unit) → `context/specs/`
  - Build plan (the WHOLE map, completed units included) → `context/build-plan.md`
- **Commands (layer 3)** → `Code/` — one subfolder per workflow;
  master runbook + unit allocation → `Code/README.md`
- **Deliverables (layer 4, produced)** → `Deliverables/` — one
  subfolder per domain; generated files are regeneration-only
- **Gathered material (received, read-only)** → `knowledge/`
- **Superseded items** → `archive/` (item table in its README)
- **Skills** (auto-invoked capabilities) → project-scoped: `.claude/skills/`
  (none yet; no global skills, so no two-place sync)
- **Sibling-repo pointers** → `knowledge/REFERENCES.md`
- Design rationale & ADRs → `docs/01-design/`
- Roadmap & ownership → `docs/02-plan/`
- Infra: database, deployment, runbooks → `docs/03-infrastructure/`
- Secrets inventory & access matrix → `docs/04-access/`
- **THE project status** → `docs/05-execution/status.md` (session-end
  rituals and status updates target this file)
- Release changelog → `docs/05-execution/changelog.md`
- Open issues → _link to your tracker_ (also `docs/06-issues/README.md`)
- Debug playbook → `docs/07-debug/debug-playbook.md`
- Testing strategy → `docs/08-testing/strategy.md`
- Monitoring & alerts → `docs/09-monitoring/observability.md`

## Coding conventions

See `context/code-standards.md` for full rules.

Short version: small pure functions, tests for every non-glue
code path, no dead code, no hardcoded secrets, follow the
formatters set in `code-standards.md`.

## Workflow

- Branch from `main`. Branch name: `<owner-initial>/<short-description>` (e.g., `a/add-rate-limit`)
- Open a PR early as draft; one teammate reviews before merge
- CI (lint + tests) must be green before merge
- Squash on merge — no merge commits on `main`
- Update `docs/05-execution/changelog.md` for user-visible changes

## Definition of done

See `docs/08-testing/definition-of-done.md`. Short version: before
starting any new unit, walk the close-unit checklist — in-flight
updates to architecture, build-plan, ADRs, project-map, spec,
changelog, project addenda, and progress-tracker. Do not skip it.

## Communication

- Async first. Channel: _#project-name_
- Weekly sync: _day / time / who runs it_
- Design decisions captured as ADRs in `docs/01-design/decisions/`
- Status updates: one teammate updates `docs/05-execution/status.md` weekly

## Safety rules

Destructive actions, protected files, and "things Claude
must not do without approval" live in
`context/ai-safety-rules.md`. Claude reads that file as
part of the startup sequence above — there are no extra
safety rules here.
