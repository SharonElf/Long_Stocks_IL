# Ownership

Who owns what. Each area has a primary (DRI — directly responsible individual) and a backup. The backup is who you ask when the primary is out.

## Areas

| Area | Primary | Backup | Notes |
|------|---------|--------|-------|
| Backend / API | A | C | _includes auth, business logic_ |
| Frontend | B | A | _web app, mobile if applicable_ |
| Database / data model | C | A | _schema, migrations, backups_ |
| Infrastructure / deploy | C | B | _cloud, CI/CD, runbooks_ |
| Monitoring / on-call | _rotating_ | — | _see `docs/09-monitoring/observability.md`_ |
| Security & secrets | A | C | _audits, rotations, access reviews_ |
| Cost / billing | C | A | _monthly review_ |
| Customer / stakeholder comms | B | A | _release notes, demos_ |

## How to update

- Don't have ownership debates in this file — discuss in a sync, then update.
- Backup ≠ uninvolved. The backup should be able to take over within a day if needed.
- Review ownership at least quarterly. People grow, projects shift.
