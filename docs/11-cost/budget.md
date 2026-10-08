# Cost & budget

Tracking what this project costs to run. If you don't watch it, it grows.

## Monthly budget

| Category | Budget | Actual (last month) | Trend |
|----------|--------|---------------------|-------|
| Cloud compute | _$XXX_ | _$YYY_ | →/↑/↓ |
| Database | _$XXX_ | _$YYY_ | → |
| Storage / CDN | _$XXX_ | _$YYY_ | → |
| Third-party APIs | _$XXX_ | _$YYY_ | → |
| Monitoring / logging | _$XXX_ | _$YYY_ | → |
| **Total** | **_$XXX_** | **_$YYY_** | |

## Review cadence

- **Monthly:** one teammate (rotating) reviews the bill, flags anomalies, updates this table
- **Quarterly:** look for optimization wins (reserved instances, right-sizing, unused resources)

## Anomaly thresholds

- Any line item up >25% MoM → investigate within 1 week
- Total cost up >15% MoM with no known cause → root-cause within 1 week

## Where to find the numbers

| Source | URL | Who has access |
|--------|-----|----------------|
| Cloud billing | _link_ | _initials_ |
| Stripe (if applicable) | _link_ | _initials_ |
| Other SaaS | _list_ | _initials_ |

## Known cost drivers

_Document things that are expected to be expensive so they don't surprise anyone._

- _e.g., E2E tests in CI cost ~$X/month — kept because catches Y_
- _e.g., Postgres has 2 read replicas — needed at current load_

## Cost optimization log

_When you cut a meaningful cost, note it here so we know what we tried._

- _YYYY-MM-DD — switched from X to Y, saved ~$Z/month_
