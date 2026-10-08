# AI Workflow Rules

How the agent **builds**. Paired with `ai-safety-rules.md` (what the agent
must not do).

## Approach

[Describe the overall development approach — e.g. Build
this project incrementally using a spec-driven workflow.
Context files define what to build, how to build it, and
the current state of progress. Always implement against
these specs — do not infer or invent behavior from scratch.]

## Scoping Rules

- Work on one feature unit at a time
- Prefer small, verifiable increments over large
  speculative changes
- Do not combine unrelated system boundaries in a
  single implementation step
- **Explain before execution:** before any multi-file change (a fix
  batch, a restructure, a sweep), present the plan as a table —
  each change → every doc it impacts — and get approval. Only then
  execute, announcing per file. Single-file edits inside an approved
  plan don't need re-approval.

## Verification bar

- Build units verify by "does it run" (tests, build, end-to-end).
- **Knowledge units verify by "is the extraction TRUE"** — cross-check
  counts and samples against the live source, never against memory or
  docs. Ground-truth checks (e.g. a raw file count the extractor must
  match) are part of the unit's checklist.
- A unit that touched `Code/` closes only if a regeneration/
  verification run passes — the knowledge equivalent of "the build
  passes".

## Session Boundaries

- **One session = one build unit.** A session is the conversation
  from Claude Code open / `/clear` until the next `/clear` or close.
  If a unit is too big for one session, split it into subunits — each
  subunit gets its own session.
- **Before ending a unit's session: persist state.** Commit any
  unstaged work and walk the close-unit checklist in
  `docs/08-testing/definition-of-done.md`. The Stop hook
  (`.claude/hooks/doc-drift-gate.py`) enforces a subset of this
  automatically when its MAP is filled in; the full checklist is
  human-driven.
- `/clear` is a manual action — no hook can trigger it. Session
  boundaries are the user's responsibility; the agent should announce
  when a unit is closed and a new session is appropriate.

## When to Split Work

Split an implementation step if it combines:

- [Concern one — e.g. UI changes and background task changes]
- [Concern two — e.g. Multiple unrelated API routes]
- [Concern three — e.g. Behavior not clearly defined in
  the context files]

If a change cannot be verified end to end quickly,
the scope is too broad — split it.

## Handling Missing Requirements

- Do not invent product behavior not defined in the
  context files
- If a requirement is ambiguous, resolve it in the
  relevant context file before implementing
- If a requirement is missing, add it as an open question
  in `progress-tracker.md` before continuing

## Architectural Decisions

When making a non-trivial design decision (data model, new
dependency, system boundary change, anything hard to reverse),
create an ADR via `/new-adr` instead of leaving it as a
session note. ADRs live in `docs/01-design/decisions/` and
are the permanent record.

## Protected Files

Do not modify the following unless explicitly instructed:

- [e.g. components/ui/* — generated UI library components]
- [e.g. Any third-party library internals]
- `docs/01-design/decisions/` — ADRs are append-only history
- `docs/07-debug/postmortems/` — postmortems are immutable
  once published

## Keeping Docs in Sync

Update the relevant context file whenever implementation
changes:

- System architecture or boundaries
- Storage model decisions
- Code conventions or standards
- Feature scope

## Before Moving to the Next Unit

**Walk the close-unit checklist in `docs/08-testing/definition-of-done.md`
before starting any new unit. Do not skip it.** The checklist covers
in-flight updates to architecture, build-plan, ADRs, project-map, spec,
changelog, project-specific addenda, and progress-tracker.

In addition, before moving on:

1. The current unit works end to end within its defined scope
2. No invariant defined in `architecture.md` was violated
3. `npm run build` (or project equivalent) passes
