# Runbooks

Step-by-step procedures for operational tasks. Written so that whoever is on-call at 2 AM — including someone who didn't write the code — can follow them.

## When to write a runbook

If you've had to figure out how to do something operational more than once, write it down.

## Runbook index

- `deploy.md` — how to deploy (and what to do if it fails)
- `rollback.md` — how to roll back a deployment
- `restore-from-backup.md` — restore the database from a snapshot
- _Add others as needed: `rotate-secrets.md`, `scale-up.md`, `incident-response.md`_

## Format

Each runbook should have:

1. **When to use it** — what triggers this procedure
2. **Prerequisites** — access needed, tools to install
3. **Steps** — numbered, copy-pasteable commands
4. **Verification** — how to confirm it worked
5. **If it fails** — escalation path
