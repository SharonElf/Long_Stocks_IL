# Team conventions

How the three of us work together. Bias toward writing things down so we don't relitigate them every quarter.

## Communication

- **Default mode:** async, in writing
- **Primary channel:** _#project-name in Slack / Discord / etc._
- **Side channels:**
  - _#project-alerts_ — automated alerts only, mute it unless on-call
  - _#project-deploys_ — deploy notifications
- **Response-time expectations:**
  - Working hours: within 4 hours
  - Outside working hours / weekends: next business day
  - Urgent (p0): tag explicitly, expect immediate response

## Meetings

| Meeting | When | Duration | Purpose |
|---------|------|----------|---------|
| Weekly sync | _Mon 10am_ | 30 min | Status, blockers, decisions |
| Design review | _ad hoc_ | 60 min | Architecture changes |
| Retro | _monthly, last Fri_ | 45 min | What's working, what isn't |

Rules:
- Agenda in writing before the meeting, or it doesn't happen
- Decisions captured in writing within 24h (design doc, doc update, or issue comment)
- If two people can resolve it async, skip the meeting

## Decisions

- **Reversible & small:** decide in the commit, document inline
- **Reversible & medium:** decide async in a thread, summarize in the issue
- **Irreversible or architectural:** record it in `docs/01-design/design-doc.md`

## Disagreement protocol

1. Both sides write down their position in 3-5 bullets.
2. Identify what evidence would change either side's mind.
3. If still stuck after a 30-min sync, escalate to the area owner; if they're a party to the disagreement, pick a tie-breaker beforehand.
4. The decision goes in the design doc with both positions captured.

## Code review

No PR gate — everyone pushes to `main`. If you want a review, ask a
teammate to read the pushed commits.

- Author: small, focused commits. < 400 lines of diff when possible.
- Reviewer: respond within 1 business day, even if just "looking now"
- Be explicit about whether a comment is **blocking**, a **suggestion**, or a **nit**

## Working hours

- _Document each person's typical hours / timezone_
- _Note any "do not disturb" windows_
- _Vacation calendar location_

## Tools

- **Repo:** _GitHub link_
- **Issue tracker:** _link_
- **Password manager:** _link_
- **Docs hub (if any):** _Notion / Confluence / etc._
- **Chat:** _Slack / Discord_
