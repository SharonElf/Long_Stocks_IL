# Testing strategy

How we know the code works before shipping.

## Test layers

### Unit tests
- **Scope:** single function or class, no I/O
- **Where:** _e.g., next to source files in `*_test.py` or `__tests__/`_
- **Tool:** _e.g., pytest, vitest, jest_
- **Run locally:** _e.g., `pytest`, `npm test`_

### Integration tests
- **Scope:** multiple components together, real database, mocked external APIs
- **Where:** _e.g., `tests/integration/`_
- **Tool:** _same as unit, with fixtures spinning up test DB_
- **Run locally:** _e.g., `pytest tests/integration`_

### End-to-end (E2E) tests
- **Scope:** full user flows against a running stack
- **Where:** _e.g., `tests/e2e/`_
- **Tool:** _e.g., Playwright, Cypress_
- **Run locally:** _e.g., `npm run test:e2e`_
- **Run in CI:** _on push + nightly_

## What needs tests

- Every new code path that isn't pure glue
- Every bug fix (regression test)
- Every non-trivial business rule
- Edge cases for input validation

## What doesn't need tests

- Trivial getters/setters
- Generated code
- Throwaway scripts (mark them as such)

## CI

- **Runs on:** every push to `main`, nightly
- **Required to pass before merge:** lint, type-check, unit + integration tests
- **Runs nightly:** E2E suite + dependency audit
- **Pipeline file:** _e.g., `.github/workflows/ci.yml`_

## Coverage

Coverage is a guardrail, not a goal. We target _e.g., 80% for new code_, but don't game the metric. A well-tested 60% is better than a gamed 95%.

## Flaky tests

Zero tolerance. If a test is flaky:
1. Mark it with `@flaky` / `.skip` immediately
2. File a `p1` issue
3. Fix or delete within a week

A flaky test in CI is worse than no test — it teaches the team to ignore failures.
