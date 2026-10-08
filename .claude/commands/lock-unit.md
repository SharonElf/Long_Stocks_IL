---
description: Claim ownership of a build unit so two teammates don't collide
---

Lock a unit in `context/progress-tracker.md`.

Steps:

1. Parse the unit number and owner initial from the user's invocation.
   If either is missing, ask for it. Format expected:
   `/lock-unit NN initial` (e.g. `/lock-unit 05 A`).

2. Read `context/progress-tracker.md`.

3. Read `context/build-plan.md` and confirm the unit number exists.
   If not, tell the user and stop.

4. Check the "In Progress" section of `progress-tracker.md`:
   - If unit NN is already locked by someone else → tell the user
     who has it and stop. Do NOT overwrite.
   - If unit NN is already locked by the same owner → tell them
     it's already locked and stop.
   - If unit NN is not locked → proceed.

5. Add a line to the "In Progress" section of `progress-tracker.md`:

   ```
   - Unit NN — [name from build-plan] (owner: X, started YYYY-MM-DD)
   ```

   Use today's date. Use the name exactly as it appears in
   `build-plan.md`.

6. Update "Current Phase" if it was "Ready to build" — change to
   "Building Unit NN".

7. Confirm to the user:
   - "Locked Unit NN — [name] for owner X. Ready to spec it (use
     `/new-spec`) or implement it."

Reminder: this is a coordination signal, not an enforcement mechanism.
Git is the actual sync. The other teammate has to pull to see the lock.
