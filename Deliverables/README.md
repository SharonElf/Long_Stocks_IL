# Deliverables/ — the outputs layer (layer 4)

Everything the project **produces** — including organized/curated
forms of gathered data. (Organizing existing data is work product:
a dictionary built from a studied DB is a deliverable, not
"knowledge".)

## Rules

1. **One subfolder per DOMAIN** — not per unit, not per source item.
   Domains are opened when their first unit starts (e.g. a knowledge
   base, a findings register, analyses, alerts).
2. **Inside a domain, organize in folders that aid understanding**
   (e.g. by subject area), each with a short reading guide in the
   domain README.
3. **Layer 4 is a rule, not a single folder**: each `Code/` workflow's
   README states where its outputs land. The anti-pattern this
   prevents: one mixed `outputs/` pile where curated docs, regenerable
   data, and one-off artifacts are indistinguishable.
4. **Two kinds of deliverables — declare which in the domain README:**
   - **Regenerated** — built by a `Code/` workflow; regeneration-only,
     nobody hand-edits a built file; edit the source and regenerate.
   - **Hand-maintained living** — curated directly by units (registers,
     decision logs). Edited in place; append-friendly; no generator.
   A domain is one or the other, never mixed.
5. **`Findings Register/` is a standard hand-maintained domain** every
   study-a-stack project gets: the consolidated issue list (severity ·
   owner · fix · workaround · status per finding, stable `F-NN` IDs).
   The full pattern + entry template: `Findings Register/README.md`
   (kept in this template so the structure is visible from day one).
6. **Data graduation:** shared machine data (json/csv consumed by
   several workflows) starts inside the domain that produced it,
   flagged "temporary home" in its README. When operational consumers
   arrive, it graduates to a first-class home (a root data shelf or a
   datastore you own) — decided **at that unit** (noted in the design doc), not upfront.
7. **Ops Package — standard optional feature:** when the project has
   real non-developer consumers, ship them a **separate consumer repo**
   (analyst `CLAUDE.md`, exported deliverables, QUICKSTART, feedback
   register that returns as commits; least-privilege read-only access;
   export workflow in `Code/`). Opened as a unit. Full pattern:
   `3-explanations/08-the-ops-package.md` in the template bundle.
8. Superseded deliverables move to `archive/` in the same commit as
   their replacement.

_Worked example: `ClaudeProjects/AditaGoldPowerBi/Deliverables/Rentgen/`
(Database · Reports · Identifiers · Data · Explorer, with a reading
guide)._
