# Secrets inventory

**This file lists what secrets exist and where they live. It does NOT contain the secrets themselves.**

If you ever feel tempted to paste a real key here, stop. Use the password manager.

## Secret store

Primary: _e.g., 1Password vault "Project XYZ" / Doppler project / AWS Secrets Manager_

All real values live there. Local `.env` files are populated from the store, never committed.

## Inventory

| Secret name | Used by | Lives in store as | Rotation cadence | Last rotated | Who can rotate |
|-------------|---------|-------------------|------------------|--------------|----------------|
| `DATABASE_URL` (prod) | API server | `prod/database-url` | yearly | YYYY-MM-DD | C |
| `STRIPE_SECRET_KEY` | API server | `prod/stripe-secret` | on suspected leak | YYYY-MM-DD | A |
| `OPENAI_API_KEY` | API server | `prod/openai-key` | quarterly | YYYY-MM-DD | A |
| `JWT_SIGNING_KEY` | API server | `prod/jwt-signing-key` | yearly | YYYY-MM-DD | A |
| _add more..._ | | | | | |

## Rotation procedure

1. Generate new secret value at the provider (e.g., Stripe dashboard, OpenAI console).
2. Update the value in the secret store.
3. Trigger a deploy / restart to pick up the new value.
4. Verify the new secret works in staging first if possible.
5. Revoke the old secret at the provider.
6. Update "Last rotated" in this file.

## If a secret leaks

1. Treat it as already compromised. Don't wait to confirm.
2. Rotate immediately (steps above).
3. Check logs / audit trails for unauthorized use during the leak window.
4. Write a postmortem (`docs/07-debug/postmortems/`).
5. Add `gitleaks` or equivalent to pre-commit hooks if not already there.
