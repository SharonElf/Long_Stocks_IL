---
description: Create a new feature spec file for the next unit
---

Create a new spec in `context/specs/`.

Steps:
1. Read `context/build-plan.md` to find the next unplanned unit, or ask me which unit to spec.
2. List existing files in `context/specs/` to find the next sequential number. Filename format: `NN-kebab-case-name.md`.
3. Use the template documented in `context/specs/README.md`.
4. Ask me, one at a time, for:
   - The goal (1-2 sentences, specific and concrete)
   - Visual / structural design decisions, referencing `context/ui-context.md` tokens
   - Implementation sub-sections (one per component or system boundary)
   - Any new dependencies to install
   - Verification conditions for "done"
5. Write the spec file and show me the path.

Reminders:
- The spec must stay within ONE system boundary. If it mixes (e.g.) UI + background tasks + DB migration, split into multiple specs.
- The verification checklist must include build pass and no console errors at minimum.
- Reference invariants from `context/architecture.md` if relevant — the spec must not violate them.
