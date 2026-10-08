# Project lifecycle & archive plan

Every project ends or pauses eventually. Decide how it ends now, when you can think clearly — not later, in a panic.

## Project status

- **Phase:** _Active / Maintenance / Sunset / Archived_
- **Last reviewed:** YYYY-MM-DD
- **Reviewed by:** _initials_

Revisit at least quarterly.

## Phase definitions

### Active
Full team is working on it. New features, regular releases.

### Maintenance
No new features. Bug fixes and security patches only. One person nominally owns it.

### Sunset (planned shutdown)
Wind-down underway. Users notified, migration paths offered, end date set.

### Archived
Read-only. Repo archived on GitHub. No deployments running.

## Pause checklist

If pausing the project temporarily (not shutting down):

- [ ] Document the pause in `docs/05-execution/status.md`
- [ ] Note the resume trigger (date or event)
- [ ] Confirm monitoring still alerts on outages
- [ ] Ensure secrets won't expire silently — set calendar reminders for any < 12 months
- [ ] Designate a contact person for the duration of the pause

## Shutdown checklist

If shutting the project down:

- [ ] Set a public shutdown date, communicated to users
- [ ] Provide data export for users (GDPR / good-practice)
- [ ] Document migration paths if alternatives exist
- [ ] Schedule infrastructure teardown 30 days after shutdown
- [ ] Cancel third-party subscriptions
- [ ] Revoke API keys at providers
- [ ] Archive the repo (read-only) — don't delete; future-you may want the history
- [ ] Move secrets out of the active vault into cold storage / delete
- [ ] Update `docs/05-execution/status.md` with the final state
- [ ] Final postmortem-style writeup: what worked, what didn't, what we learned

## Handoff checklist

If transferring ownership to another team:

- [ ] All docs in this folder current and accurate (especially `00-quickstart.md`)
- [ ] Run the quickstart end-to-end yourself to verify
- [ ] Walk new owner through `CLAUDE.md`, ownership matrix, runbooks
- [ ] Update GitHub repo ownership, cloud account access, password manager
- [ ] Schedule a 2-week and 6-week check-in
- [ ] Keep yourself accessible for questions for at least 90 days
