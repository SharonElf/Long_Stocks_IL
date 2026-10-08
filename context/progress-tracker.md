# Progress Tracker

**Cadence:** updated by the agent after every meaningful
implementation change (per-feature unit). For weekly human
status, see `docs/05-execution/status.md`. For per-release
user-visible changes, see `docs/05-execution/changelog.md`.

## Current Phase

- **Configured — awaiting the first planning session** (started 2026-10-08).
  Launch fork answered: **BUILDS** software. `knowledge/` is seeded.
  No planning has been done on purpose.

## Current Goal

- Plan the project (build plan + specs) in the next session.

## Completed

- 2026-10-08 — Project configuration: template cloned from
  `Claude-Code-Project-Configuration/1-the-template`, `knowledge/` seeded
  (call summary, TASE data research, `REFERENCES.md` to sibling repos),
  `context/project-overview.md` filled with stated facts only, `CLAUDE.md`
  filled, sibling repos added to `.claude/settings.json`.

## In Progress

- None yet.

> **Multi-user note:** when more than one teammate uses this repo,
> each in-progress unit is listed with owner and start date. Use
> `/lock-unit NN initial` to claim a unit, `/release-unit NN` to
> release it. See `docs/10-team/team-sync.md`.
>
> Format: `- Unit NN — [name] (owner: X, started YYYY-MM-DD)`

## Next Up

1. In the new session: first `git pull` in `../bank-portfolio-pilot` (local copy is
   3 months behind GitHub), then run `/chaperone`.
2. Basic build plan outline is written in `context/build-plan.md` (21 units, 6 decision gates).
   Start with units 01 and 02 (settle blocking questions, chart source test).
3. Resolve the Open Questions below, then fill the remaining context files
   (`architecture`, `ui-context`, `code-standards`, `ai-workflow-rules`,
   `ai-safety-rules`) and write `context/build-plan.md`.

## Open Questions

Ask these first in the planning session.

1. **Relationship to bpp.** Does this project *own* position data (area 1) or read it from
   `bpp.holdings`/`lots`? Does it replace or sit beside bpp's daily ADD/HOLD/REDUCE/SELL engine?
2. **Universe.** Israeli only, or the whole mixed portfolio (US stocks/ETFs too)? Which
   brokers/accounts?
3. **Intraday data reality.** Classic Israeli mutual funds (12 held) and bonds publish a daily
   NAV only, so 4h/1h fine-tuning can only apply to exchange-traded instruments. Is that acceptable?
4. **Candle source.** The pasted research (free TASE daily history + 15-min sampled hourly
   candles) was **checked 2026-10-08 and does not hold up** (TASE's official daily history is
   paid, $100–500 a month; the free-website and sampling claims are unconfirmed). Full record in
   `docs/03-infrastructure/data-sources.md`. Still open: the hands-on test (build plan unit 02).
5. **Algorithm style.** Deterministic rules (like the brain's gates), Claude-driven (like bpp),
   or a mix? What does "yes/no gate" gate — a trade, a position, a scanner flag?
6. **Time horizon & decision cadence.** Holding period, how often it runs, how results are
   delivered (Telegram / HTML report like the neighbors?).
7. **P&L scope.** Reuse brain Spec 136 (Schwab) and/or bpp lots; note bpp
   `lot_allocations` is empty today.
8. **Stack and hosting.** Neighbors use n8n + Supabase + Python/FastAPI on Railway. Same here? New schema in the shared Supabase instance?
9. **People and roles.** The call names Sharon and Einat; who owns what here, and who is `esupport`?
10. **Success criteria** for the project.

> Non-trivial architectural decisions go in
> `docs/01-design/design-doc.md`, not here. This section is for
> open product questions only.

## Session Notes

- 2026-10-08 (planning session 1): worked backwards from the end result, ignoring the
  neighbor systems on purpose. First draft saved in `docs/02-plan/first-draft-plan.md`
  (end result, decisions, logic chain, data list, tensions, open questions). Reuse of
  bpp/brain is deferred until the requirements are complete. Nothing implemented.
- 2026-10-08 (revision 2): investor changed the draft. Risk is judged **per ticker** (portfolio
  view, risk groups, targets and "how much" parked as a next stage); market sentiment is
  **weekly**; each ticker gets statistical figures and possibly news. Draft plan and
  `docs/02-plan/process-overview.html` updated. Still nothing implemented.
- 2026-10-08 (data foundation): verified the pasted TASE research against TASE's own 2026 price
  list and other sources. Result: not usable as written; no confirmed 1h/4h source for Israeli
  securities yet. Recorded in `docs/03-infrastructure/data-sources.md` (claims, prices, what was
  not checked, where to look, what to do next). The price list PDF is saved in `knowledge/`.
  Do not redo this research; only the hands-on steps listed there remain.
- 2026-10-08: the call's Schwab file problems (no fill times, no reference number)
  are what brain Spec 136 already solves — see `knowledge/REFERENCES.md` area 6.
- bpp's own docs from June say "Israeli only, index-level candles, no per-security
  candles needed"; this project's per-security daily/weekly/monthly candle need
  changes that assumption.
- Sibling folder names can drift (the brain clone is `trading-copilot-brain-22092026`);
  update `CLAUDE.md` → "Sibling repos" and `.claude/settings.json` if one is renamed.
