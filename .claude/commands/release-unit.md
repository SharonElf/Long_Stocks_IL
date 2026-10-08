---
description: Release a build unit you previously locked
---

Release a unit lock in `context/progress-tracker.md`.

Steps:

1. Parse the unit number from the user's invocation. If missing,
   ask which unit. Format: `/release-unit NN` (e.g. `/release-unit 05`).

2. Read `context/progress-tracker.md`.

3. Find unit NN in the "In Progress" section.
   - If not found → tell the user the unit isn't locked and stop.

4. Ask the user: "How do you want to release Unit NN?"
   - A) Complete — work is done, merged
   - B) Unlock — pausing or handing off, keep the spec/code in place
   - C) Abandon — discard, will not finish

5. Based on the answer:

   **A) Complete:**
   - Remove the line from "In Progress"
   - Add to "Completed" with today's date:
     `- Unit NN — [name] (completed YYYY-MM-DD by X)`
   - If this was the last in-progress unit, set Current Phase to
     "Ready to build" and update Next Up from build-plan.md.

   **B) Unlock:**
   - Remove the line from "In Progress"
   - Add a session note: "Unit NN released back to unlocked by X
     on YYYY-MM-DD. Status at handoff: [ask user for one line]."
   - Leave Current Phase unchanged unless this was the only unit
     in progress.

   **C) Abandon:**
   - Remove the line from "In Progress"
   - Add a session note: "Unit NN abandoned by X on YYYY-MM-DD.
     Reason: [ask user]."
   - Recommend the user create an ADR via `/new-adr` if the
     abandonment reflects a design change.

6. Confirm to the user with the action taken and what's next.

Reminder: releasing a unit doesn't undo any code changes — that's
a Git operation, not a tracker operation.
