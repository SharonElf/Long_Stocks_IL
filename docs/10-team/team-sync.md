# Team Sync — multi-user workflow

How two or more people work the same repo without stepping on each
other. Read this once. Then internalize the five conventions.

## The mechanism

Git is the sync mechanism. Markdown files (including `context/`) are
version-controlled like any code. Conflicts are resolved like any
merge conflict.

What's different from normal code: the **`progress-tracker.md`** is
the single source of truth for "where are we?" Both teammates read it
on every session, both update it as they work. Treat it with care.

## The five conventions

### 1. Pull before you start, push when you stop

Every session begins with `git pull`. Every session ends with `git
push` (or a PR). No exceptions.

The reason: the agent reads `context/` and `progress-tracker.md`
from disk. If your local copy is stale, the agent makes decisions
based on yesterday's reality.

### 2. Lock unit ownership

Only one person works on a unit at a time. Use the `/lock-unit`
slash command to mark a unit in `progress-tracker.md`:

```
## In Progress
- Unit 05 — Auth flow (owner: A, started 2026-05-17)
- Unit 07 — Canvas shell (owner: B, started 2026-05-17)
```

Before starting work on a unit, run `/lock-unit NN your-initial`.
Claude will check it's not already locked by someone else and
update the tracker.

When you finish (or stop), run `/release-unit NN` to remove the
lock (or mark complete).

### 3. Feature branches per unit

One branch per unit. Naming: `<initial>/<NN>-<short-name>`.

- `a/05-auth-flow`
- `b/07-canvas-shell`

Open a PR before merging. The other teammate reviews.

### 4. Context file changes go through PR

If you update `code-standards.md`, `architecture.md`, or any other
context file, it goes through a PR like any code change. The other
teammate reviews — both because the agent's behavior depends on
these files, and because the change might affect work already in
progress.

### 5. Quick message before starting

Before running `/lock-unit`, send a 5-second message to the other
teammate: "Taking Unit 06." Prevents both of you from independently
locking adjacent units that should have been one.

## Handling sync conflicts

**Conflict in `progress-tracker.md`:** signals you both worked
without syncing. Resolve manually — usually both entries should be
kept; the order matters less than the accuracy. After resolving,
send a quick note so the other person knows what happened.

**Conflict in a context file:** stop and talk. The system depends on
these files being consistent. Don't auto-resolve.

**Two ADRs with the same number:** rare, but possible if both run
`/new-adr` simultaneously. Whoever pushes second renames their file
to the next number and updates the title.

## When you should NOT lock a unit

- The unit description in `build-plan.md` is vague — fix that first
- You don't have time to finish in one session — wait until you do
- The unit depends on another in-progress unit — wait for that one
  to finish

## When you should release a unit

- You're done and it's merged → release as complete
- You're stuck and need help → release back to "unlocked" so the
  other person can pick it up
- You're switching to something else → release back to "unlocked",
  add a session note about where you stopped

## On reviewing each other's PRs

- Read the spec file for the unit before reviewing the code
- Check the verification checklist was actually run
- If the diff goes beyond the spec scope, ask why
- Approve quickly when it matches — bottlenecks compound on small teams
