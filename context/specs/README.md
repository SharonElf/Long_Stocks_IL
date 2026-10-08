# Feature Specs

One file per unit from `build-plan.md` — **every unit, completed ones
included**. A planned unit's spec is its forward contract; a completed
unit's spec is its RECORD (see below). Numbers match the build plan.

## Filename format

```
NN-unit-name.md
```

e.g. `01-design-system.md`, `02-editor-shell.md`,
`03-auth.md`.

Numbers match the unit numbers in `build-plan.md`.

## Spec template

Use `/new-spec` in Claude Code, or copy the template
below.

```markdown
# Unit NN: [Feature Name]

## Goal

One or two sentences describing the concrete output
of this unit. Be specific.

## Design

Visual and structural decisions specific to this unit.
Reference `ui-context.md` tokens where relevant.

## Implementation

### [Component or sub-section]

Detailed description of what to build.

### [Next sub-section]

Description.

## Dependencies

- package-name (reason)

## Verify when done

- [ ] Condition one
- [ ] Condition two
- [ ] No TypeScript errors
- [ ] No console errors
- [ ] Responsive at mobile and desktop
- [ ] Build passes (`npm run build` or equivalent)
```

## RECORD-spec template (for completed / retrofitted units)

When a unit was finished before its spec existed (retrofit), or when
closing a unit, the spec becomes the unit's record:

```markdown
# Unit NN: [Name] — RECORD (complete YYYY-MM-DD)

## Goal
[What the unit set out to produce.]

## Method (what was done)
[The actual steps/tools/workflows used.]

## Verification performed
[How truth was established — ground-truth checks, counts, runs.]

## Result
[The deliverables and exactly where they live.]

## Open residue
[Anything left open — each item pointing at the unit that owns it.]
```

## The three-prompt workflow

**To implement a unit:**

```
Read context/specs/NN-feature-name.md.
Update context/progress-tracker.md to mark this as
in progress.
Implement it exactly as specified.
Do not go beyond the scope of this unit.
```

**To correct something off-spec:**

```
The [specific element] does not match the spec.
Expected: [what the spec says].
Current: [what was built].
Fix only this. Do not change anything else.
```

**To close a unit:**

```
Implementation is complete and verified.
Mark unit NN complete in context/progress-tracker.md.
Push branch feat/NN-feature-name to GitHub.
```
