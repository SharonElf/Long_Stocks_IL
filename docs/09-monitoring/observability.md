# Monitoring & observability

How we know it's working in production — without waiting for users to tell us.

## Three pillars

### Logs
- **Where:** _e.g., CloudWatch / Loki / Datadog Logs URL_
- **Format:** structured JSON, one event per line
- **Retention:** _e.g., 30 days hot, 1 year cold_
- **Levels:** `error` and `warn` should be actionable; `info` for business events; `debug` only in dev

### Metrics
- **Where:** _e.g., Grafana / Datadog / CloudWatch Metrics URL_
- **Tool:** _e.g., Prometheus, OpenTelemetry_
- **Golden signals:** latency, traffic, errors, saturation (per service)

### Traces
- **Where:** _e.g., Datadog APM / Jaeger / Tempo URL_
- **Tool:** _e.g., OpenTelemetry instrumentation_
- **Sampling:** _e.g., 100% on error paths, 5% otherwise_

## Dashboards

| Dashboard | Purpose | URL |
|-----------|---------|-----|
| Service health | Real-time golden signals | _link_ |
| Business metrics | DAU, key conversions | _link_ |
| Costs | Cloud spend by service | _link_ |
| Errors | Sentry / error tracker | _link_ |

## Alerts

| Alert | Severity | Trigger | Routes to | Runbook |
|-------|----------|---------|-----------|---------|
| API error rate > 5% (5m) | SEV1 | _PagerDuty / phone_ | On-call | `runbooks/api-errors.md` |
| API p95 > 2s (10m) | SEV2 | _Slack #alerts_ | On-call | _link_ |
| DB CPU > 80% (15m) | SEV2 | _Slack #alerts_ | On-call | _link_ |
| Cert expiring < 14d | SEV3 | _Slack #alerts_ | A | _link_ |

## Alert hygiene

- Every alert must have a runbook link. No runbook → no alert.
- If an alert fires and nothing should be done, delete or tune it.
- Review alert noise monthly. Goal: every page is actionable.

## On-call (if applicable)

- Rotation: _e.g., weekly, A → B → C_
- Handoff: _e.g., Monday 10am sync covers anything outstanding_
- Compensation: _document if relevant_
- Escalation: _who to call if primary doesn't respond in 15 min_
