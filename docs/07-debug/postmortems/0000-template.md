# Postmortem NNNN: _Title_

- **Incident date:** YYYY-MM-DD HH:MM TZ
- **Detected:** YYYY-MM-DD HH:MM (how — alert, user report, etc.)
- **Resolved:** YYYY-MM-DD HH:MM
- **Duration:** _hh:mm_
- **Severity:** SEV1 / SEV2 / SEV3
- **Authors:** _initials_
- **Status:** Draft / Final

## Summary

_2-3 sentences. What broke, who it affected, how long, how it was fixed._

## Impact

- _Users affected: e.g., ~10% of API requests returned 500 for 23 minutes_
- _Data loss: yes/no, details_
- _Revenue / SLA impact: if applicable_

## Timeline

All times in _TZ_.

| Time | Event |
|------|-------|
| HH:MM | _Trigger event (e.g., deploy of commit abc123)_ |
| HH:MM | _First alert fired_ |
| HH:MM | _On-call acknowledged_ |
| HH:MM | _Hypothesis formed_ |
| HH:MM | _Mitigation applied_ |
| HH:MM | _Service restored_ |
| HH:MM | _All-clear confirmed_ |

## Root cause

_What actually caused this. Not the proximate trigger — the underlying reason it was possible._

## What went well

_Things that helped detect or resolve faster._

## What went poorly

_Things that delayed detection, response, or resolution._

## Action items

| Action | Owner | Due | Issue link |
|--------|-------|-----|------------|
| _e.g., Add alert for X_ | A | YYYY-MM-DD | _#123_ |
| _e.g., Add regression test for Y_ | B | YYYY-MM-DD | _#124_ |

## Lessons

_What did we learn? What should we do differently next time?_
