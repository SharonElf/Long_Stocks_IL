# Quickstart

Goal: someone new (or you, returning after 6 months) can go from `git clone` to a passing test in under an hour.

## Prerequisites

- _Language runtime version (e.g., Python 3.12, Node 20)_
- _Package manager (e.g., uv, pnpm, poetry)_
- _Docker (if applicable)_
- Access to:
  - GitHub repo
  - Team password manager (1Password / Doppler) — for secrets
  - _Other: cloud console, monitoring dashboards_

Ask the person who onboarded you (or check `docs/04-access/permissions.md`) if any access is missing.

## First-time setup

```bash
# 1. Clone
git clone <repo-url>
cd <project>

# 2. Install dependencies
# <e.g., uv sync, pnpm install, poetry install>

# 3. Copy environment template
cp .env.example .env
# Then fill in real values from the team password manager.

# 4. Start local services (if any)
# <e.g., docker compose up -d>

# 5. Run migrations / seed data (if any)
# <e.g., make migrate, npm run db:seed>

# 6. Run the test suite to confirm everything works
# <e.g., pytest, npm test>
```

If a step fails, check `docs/07-debug/known-issues.md` before asking — it may already be documented.

## Your first push

A small, safe first change to confirm your workflow is working end-to-end:

1. `git pull` to make sure you're current
2. Add your name to the team table in `CLAUDE.md` (if not already there)
3. Commit and push directly to `main`

This walks you through the pull-commit-push loop — without touching production code.

## Common gotchas

_Add things here as you discover them. Examples:_

- _Port 5432 conflicts with local Postgres → stop the system service or change `DATABASE_URL`_
- _On Apple Silicon, `<library>` needs `arch -arm64` prefix_
- _The first run downloads ~500MB of model files; subsequent runs are fast_

## Who to ask

- Backend / API → A
- Frontend → B
- Infra / data → C
- Anything else → `#project-name` Slack channel
