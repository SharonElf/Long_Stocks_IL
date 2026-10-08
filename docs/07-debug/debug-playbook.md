# Debug playbook

Read this before guessing. When something's broken, follow the steps below in order — most issues are caught in the first three.

## 1. Where to look first

| Symptom | First place to check |
|---------|----------------------|
| 500 errors in API | _Sentry / error tracker URL_ |
| Slow response | _APM / latency dashboard URL_ |
| User can't log in | _Auth service logs + Sentry user filter_ |
| Background job stuck | _Queue dashboard URL_ |
| Deployment failure | _CI/CD logs + `runbooks/rollback.md`_ |
| Database issue | _DB monitoring URL + `database.md`_ |

## 2. Reproduce locally

If you can't reproduce, you can't fix.

```bash
# Crank up logging
export LOG_LEVEL=debug

# Run with the same env config as the affected environment (sanitized)
# <command>
```

Tips:
- _Specific repro recipes go here as you find them_
- _e.g., To repro the rate-limiter bug, set `RATE_LIMIT_WINDOW=1`_

## 3. Bisect

For "it worked yesterday" bugs:

```bash
git bisect start
git bisect bad HEAD
git bisect good <known-good-sha>
# Run your test, mark good/bad, repeat
```

## 4. Common patterns

_Document recurring failure modes and their causes. Examples:_

- _"Connection refused" on startup → Postgres container not ready; add wait-for-it script._
- _Random 429s → upstream API rate limit; back off and retry._
- _OOM kills in worker → unbounded batch size; check the loop in `workers/foo.py`._

## 5. When to escalate

If after ~1 hour of focused debugging you're still stuck:
- Post in `#project-name` with what you've tried
- Pair with the area owner (see `docs/02-plan/ownership.md`)
- For prod incidents: skip the wait, page immediately

## 6. After the fact

If the bug was non-trivial:
- File a regression test
- Add a `known-issues.md` entry if there's a workaround
- For incidents: write a postmortem (`/new-postmortem` slash command)
