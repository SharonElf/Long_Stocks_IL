# Issues

Open issues live in the project's issue tracker, not here. This file just points there and documents our conventions.

## Tracker

_e.g., https://github.com/org/repo/issues_
_e.g., https://linear.app/team/project_

## Filing a good issue

A good issue includes:

- **What happened** vs. **what you expected**
- **Steps to reproduce** (if a bug)
- **Environment** (browser / OS / version)
- **Severity guess** (use labels below)
- **Logs / screenshots** where helpful

For feature requests:

- **Problem** the feature solves
- **Why now** (urgency, blockers)
- **Acceptance criteria** if you have them

## Labels

### Priority
- `p0` — production down or data loss; drop everything
- `p1` — important; fix this week
- `p2` — should fix this month
- `p3` — nice-to-have, no urgency

### Type
- `bug` — broken behavior
- `feature` — new capability
- `chore` — maintenance, deps, refactor
- `docs` — docs only
- `infra` — infrastructure, CI/CD

### Status (if not using a board with columns)
- `needs-triage` — fresh, not yet evaluated
- `blocked` — waiting on something external
- `in-progress` — actively being worked
- `needs-review` — PR open, awaiting review

## Triage

Weekly during the sync: walk through `needs-triage` issues, assign priority/type/owner or close as won't-fix.

## Stale issues

If an issue has been open with no activity for 90 days:
- Comment asking if still relevant
- Close after 14 more days of silence
- Move closed-but-still-valid ideas to "Someday" in `docs/02-plan/roadmap.md`
