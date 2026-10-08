# Code/ — the commands layer (layer 3)

Everything executable-on-demand or by automation lives here — scripts,
queries, configs, runnable runbooks (`.py`, `.sql`, `.json`, `.md`).

The 4-layer model: `context/build-plan.md` (the list) →
`context/specs/` (the contracts) → **`Code/` (the commands)** →
`Deliverables/` (the outputs). See
`3-explanations/06-the-knowledge-layer.md` in the template bundle.

## Rules

1. **One subfolder per functional workflow** — never loose files at
   this root. Each subfolder carries its own README stating: what it
   runs, how to run it, and **where its outputs land**.
2. **Units allocate into workflows (N:M)** — a unit may create a
   workflow, extend one, or just use existing ones. The allocation
   lives in the table below ("serves units"), not one command doc
   per unit.
3. **Provenance:** every committed artifact's generator is committed
   with it, here, in the same commit. Inline generation in a chat
   session is saved here before the session ends.
4. This root README is the **master runbook**: keep the workflow table
   and the cross-workflow run order current.

## Workflows

| Subfolder | Runs | Produces (layer 4) | Serves units |
|---|---|---|---|
| _[workflow]/_ | _[what it executes]_ | _[which Deliverables path]_ | _[unit numbers]_ |

## Cross-workflow run order

1. _[step — e.g. sync the studied source]_
2. _[step]_

_Worked example: `ClaudeProjects/AditaGoldPowerBi/Code/` (6 workflows,
regeneration order, run-readiness warnings)._
