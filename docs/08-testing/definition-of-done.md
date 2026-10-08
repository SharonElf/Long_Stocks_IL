# Definition of Done — Unit Close

A unit is "done" only when **all** of the items in this checklist are
true. This is the procedure to run BEFORE the unit-closing commit.

## Hard rule

**Do not start the next unit until the current unit is closed against
this checklist.** A new spec, a new unit's build, or any work on a new
unit number is forbidden while a unit remains unclosed.

## How to walk the checklist

For each item below, answer with ONE of:

- `[x] yes` — already updated in commit `<hash>`; verifiable in the diff
- `[ ] no — updating now` — make the update before continuing
- `[~] N/A — <one-sentence justification>` — only valid if the unit
  genuinely doesn't touch that area; be honest

Walk against the ACTUAL diff (`git diff`, `git log --name-only`), not
memory. Re-read each file you claim to have updated.

## Checklist

### Design docs (in-flight updates)

- [ ] `context/architecture.md` — system structure shifted? Boundaries,
      storage model, invariants, runtime layout — all current?
- [ ] `context/build-plan.md` — the unit's row reflects actual scope,
      status, and date? Status marker updated?
- [ ] `docs/01-design/decisions/` — every non-trivial design decision
      made during this unit has an ADR? One ADR per decision;
      append-only; filename `NNNN-kebab-name.md`.
- [ ] `project-map.html` (if the project uses one) — file tree, data
      flow, and unit-status badges still accurate?

### Spec + visible changes

- [ ] `context/specs/NN-*.md` — spec exists and reflects what was
      actually built (not just what was planned). Skip if the unit
      was deferred or folded into another unit.
- [ ] `docs/05-execution/changelog.md` — entry added if the change is
      user-visible.
- [ ] If the unit touched `Code/`: a regeneration/verification run
      passed (knowledge equivalent of "the build passes"). Knowledge
      units: extraction cross-checked against the live source.

### Project addenda

- [ ] Any items in the "Project addenda" section at the bottom of this
      file — walked with the same answer format.

### Progress tracker (LAST)

- [ ] `context/progress-tracker.md` — single-at-completion update:
      move the unit's entry to "Completed" with the closing date;
      refresh any session-resume anchor; commit as a small follow-up
      (`Update progress-tracker for Unit NN closure`).

## Edge cases

- **Unit deferred** — skip the spec verification; still update
  `build-plan.md` with the deferred status and a one-line reason;
  still update `progress-tracker.md`.
- **Unit folded into another** — skip the spec; update `build-plan.md`
  to show the unit as folded with a pointer to the absorbing unit.
- **Mid-session follow-up commits after a unit was closed** — allowed
  ONLY if they fix the closed unit (bug, typo, missed doc line) —
  not new behavior. Follow-ups attach to the same unit; new behavior
  is a new unit and requires its own spec via `/new-spec`.

## Reminders

- Walk against the ACTUAL diff, not memory.
- Honesty over speed. A real `[~] N/A — justification` is fine. A false
  `[~] N/A` is the failure mode this checklist exists to prevent.
- This file is the canonical close-unit procedure for the methodology.
  Linked from `context/ai-workflow-rules.md` so it is read at every
  session start regardless of chaperone mode.

---

## Project addenda

Projects with runtime files, sync workflows, or external systems
that aren't part of the generic methodology should list their
additional close-unit items here, in their local copy of this file.

Examples of items that belong here:

- A runtime configuration file loaded by an external service (e.g.
  a cloud Routine, an n8n flow, a CI job) that must be updated when
  any unit changes behavior the runtime depends on.
- A version stamp or build-id at the top of a file used to verify
  the deployed copy matches the committed source.
- A manual re-paste / re-deploy / re-sync step required outside git
  whenever a particular file changes.
- An external dashboard, API key inventory, or deploy hook that
  needs to be touched when a unit makes a specific kind of change.

If your project has no addenda, leave this section empty.
