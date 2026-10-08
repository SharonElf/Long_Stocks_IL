# Database

## Engine

_e.g., PostgreSQL 16, hosted on AWS RDS, db.t4g.medium_

## Where to find the schema

_e.g., `migrations/` folder, or `prisma/schema.prisma`, or `models/` package_

Don't duplicate the schema here — link to it. Source of truth is the code.

## Connection

- Local dev: `DATABASE_URL` in `.env` (see `.env.example`)
- Staging: secret in _password manager / vault location_
- Production: managed via _IaC tool / secret manager_

## Migrations

- Tool: _e.g., Alembic, Prisma migrate, Flyway_
- Naming: _e.g., `YYYYMMDD_HHMM_short_description`_
- **Rule:** every migration must be committed to the repo and must be reversible (or explicitly justified as not).
- Never run a migration manually in production. Always through CI/CD.

## Backups

- Frequency: _e.g., automated nightly snapshots, retained 30 days_
- Restore tested: _date of last successful restore drill_
- RPO (max data loss tolerable): _e.g., 24 hours_
- RTO (max downtime tolerable): _e.g., 4 hours_

## Performance notes

- Indexes: _list any non-obvious indexes and why they exist_
- Heavy queries: _document slow queries and their workarounds_
- Connection pooling: _e.g., PgBouncer, max 100 conns_
