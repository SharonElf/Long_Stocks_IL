# Access matrix

Who can access what. **No secrets in this file** — only the access map.

Review quarterly. Revoke access promptly when someone changes role or leaves.

## Per-resource access

| Resource | A | B | C | Notes |
|----------|---|---|---|-------|
| GitHub repo | admin | write | write | |
| GitHub repo settings | ✓ | | | only A can change branch protection |
| Cloud account (prod) | admin | read | admin | |
| Cloud account (staging) | admin | admin | admin | |
| Production database | read-only | — | read/write | C handles migrations |
| Production secrets manager | ✓ | — | ✓ | |
| Staging secrets manager | ✓ | ✓ | ✓ | |
| Domain registrar | ✓ | — | — | |
| Monitoring dashboards | ✓ | ✓ | ✓ | |
| Sentry / error tracker | admin | member | member | |
| CI/CD admin | ✓ | — | ✓ | |
| Stripe / billing | ✓ | — | — | |

## Onboarding checklist

When adding a new teammate:

- [ ] GitHub repo invite
- [ ] Cloud account (with scoped role, not admin by default)
- [ ] Password manager vault invite
- [ ] Monitoring access
- [ ] Slack channel
- [ ] Added to `CLAUDE.md` team table and `docs/02-plan/ownership.md`

## Offboarding checklist

When someone leaves:

- [ ] Revoke GitHub access
- [ ] Revoke cloud IAM credentials
- [ ] Remove from password manager
- [ ] Rotate any shared secrets they had access to
- [ ] Remove from monitoring / dashboards
- [ ] Remove from Slack
- [ ] Update ownership matrix
