# AI Safety Rules

What the agent **must not do**. Paired with `ai-workflow-rules.md`
(how the agent builds).

These are operational guardrails — destructive or
irreversible actions that always require explicit human
approval, regardless of what the spec or progress tracker
says.

## Things the agent must NOT do without explicit approval

- Delete files in `docs/07-debug/postmortems/` (postmortems
  are immutable once published)
- Run database migrations or any destructive data operation
- Modify deployment scripts or infrastructure-as-code in
  `infra/` or `.github/workflows/`
- Commit secrets — check `.env`, `*.pem`, `*.key`, and
  obvious key patterns before adding any files
- Force-push any branch (pushing straight to `main` is the normal flow)
- Install new dependencies without confirming they belong
  in the chosen stack
- Make changes outside the scope of the current spec file

## Behavior when in doubt

- When asked to add a feature, check `docs/02-plan/` first
  for context and ownership
- When debugging, follow `docs/07-debug/debug-playbook.md`
  before guessing
- When making a non-trivial design choice, record it in
  `docs/01-design/design-doc.md` (see `ai-workflow-rules.md`)
- Prefer asking over assuming if requirements are ambiguous
- If a requirement is missing, add it as an open question
  in `progress-tracker.md` rather than inventing behavior

## Secrets and credentials

- Never paste a real secret value into any file in the repo
- All secret values live in the team password manager —
  see `docs/04-access/secrets-inventory.md`
- `.env` is gitignored; only `.env.example` is committed
- If a secret is accidentally committed, treat it as already
  compromised — follow the rotation procedure in
  `secrets-inventory.md` immediately
