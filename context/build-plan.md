# Build Plan

The ordered list of units that make up this build. Each
unit is a single, scoped, verifiable piece of work — small
enough to build in one focused session, concrete enough
that "done" is unambiguous.

This file is written at the start of the build, after the context
files are complete — and it covers **the WHOLE project**: completed
units stay in the table with their result and date, grouped by phase.
The plan is the whole map of the work, not just the remainder.

Two rules that keep the map honest:

- **Iterations of one deliverable = ONE unit.** A map that went
  v1 → v2 → v3 is a single unit whose result is the latest version;
  earlier versions are its iterations (superseded → `archive/`).
  A future improvement is a NEW unit.
- **Units allocate into `Code/` workflows N:M** — the allocation lives
  in `Code/README.md` ("serves units" column), not one command doc
  per unit.

## Rules for a good unit

- It produces one visible, verifiable result
- It stays within one system boundary — don't mix UI changes
  with database changes with background tasks in one unit
- It has a checklist of conditions that must be true before
  it's considered complete
- It can be built in a single focused session without
  needing to make decisions that belong in another unit

## Ordering rules

- **Dependencies first.** Never build on top of something
  that doesn't exist yet.
- **Security before functionality.** Auth and access control
  come before the features they protect.
- **Backend before frontend wiring.** Build the API, then
  wire the UI.
- **UI shells before real data.** Build the component
  structure with placeholders, then connect real data.
- **Install dependencies just in time.** Only install a
  package in the unit where it first unlocks real behavior.

## Units

Group by phase (e.g. study → structure → operate, or design → build →
harden). Completed units keep their row: result + date.

| # | Name | What it produces / produced | Depends on | Status |
|---|------|------------------------------|------------|--------|
| 01 | [unit name] | [result + date if complete] | — | [Complete YYYY-MM-DD / In progress / Planned] |
| 02 | [unit name] | [what it produces] | 01 | Planned |

_(Continue numbering. Every unit gets a spec file in
`context/specs/NN-unit-name.md` — completed units get RECORD-specs;
see `context/specs/README.md`.)_
