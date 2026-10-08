# Findings Register/ — the standard hand-maintained domain

**Kind:** hand-maintained living deliverable (NOT regeneration-only —
units edit it directly; no generator exists or should exist).

**What lives here:** `findings_register.md` — THE consolidated list of
every issue found in the studied stack: bugs, flaws, traps, gaps.
One entry per finding, each with severity, owner, recommended fix,
workaround, and status. Created by the project's "findings register"
unit; appended to by every unit that discovers something afterward.

This folder ships with the template (README only) so the structure is
visible from day one; the register file itself is created when the
first finding is recorded.

_Decision origin: AditaGoldPowerBi Unit 10 (2026-07-13) — see that
project's `Deliverables/Findings Register/findings_register.md` for a
worked example (13 findings)._

## The rules

- **IDs `F-NN` are stable and append-only** — downstream units, specs,
  and the design doc cites them; never renumber, never delete (close instead).
- **Severity:** `High` / `Medium` / `Low`.
- **Owner:** `us` / `data team` (or the external owner's name) / `both`.
  The split question: "can we work around it locally?" (us) vs
  "requires a source change" (external).
- **Status:** `open` · `workaround-in-place` · `escalated` · `fixed` ·
  `accepted`.
- **Every entry cites its source doc** (path + section) — the register
  summarizes; the study doc is the evidence. No finding from memory.
- **Route every open finding to a fixing unit** in the build plan
  before closing the register pass.
- Start the register with a summary table (ID · finding · severity ·
  owner · status · fixing unit); end it with the sweep procedure and
  the entry template below.

## The repeatable sweep (per studied stack/DB)

1. Study phase first: profile the LIVE source (dictionary + freshness +
   value sampling); never trust inherited docs.
2. Sweep the study outputs for: naming risks · identifier lies (sample
   VALUES, not column names) · freshness clusters (stale cluster =
   broken feed) · junk/test objects · missing dimensions · type traps
   (text numbers, text dates) · doc drift.
3. One entry per finding, template below.
4. Route each finding to a fixing unit; then the register is the
   starting point for every fix unit.

## Entry template

```markdown
## F-NN — <short name>

- **What:** <the defect, with concrete values/counts>
- **Evidence/source:** <doc path + section>
- **Severity:** High | Medium | Low — <why>
- **Recommended fix:** <the real fix + owning unit>
- **Workaround in place:** <what we do meanwhile, or "none">
- **Status:** open | workaround-in-place | escalated | fixed | accepted
```
