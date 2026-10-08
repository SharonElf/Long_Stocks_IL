# Architecture Decision Records (ADRs)

This folder is an append-only log of significant design decisions.

## When to write an ADR

Anytime you make a decision that:
- Is hard or expensive to reverse later
- Affects the architecture, data model, or external interfaces
- Future-you (or a new teammate) might wonder "why did we do it this way?"

Small decisions don't need ADRs. Big ones do.

**Retrofitting an existing project?** Decisions already made get
**retroactive ADRs** (status: "Accepted (retroactive record; decided
DATE, recorded DATE)") — the reasoning is captured while it's still
remembered.

## How to write one

Use `/new-adr` in Claude Code, or copy `0000-template.md` manually. Filename format:

```
NNNN-kebab-case-title.md
```

e.g., `0007-use-postgres-over-mongo.md`

## Rules

- **Append-only.** Once an ADR is merged, don't edit it. If a decision changes, write a new ADR that supersedes the old one (and update the old one's status to "Superseded by ADR-NNNN").
- **Short.** One page is plenty. If you need more, link out.
- **Honest.** Capture what you actually considered, including options you rejected.

## Index

_List ADRs here as you add them. Newest at the bottom._

- _0001 — Example decision_
