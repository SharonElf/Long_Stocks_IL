# .claude/skills/ — project-scoped skills

Skills that only need to trigger inside this repo live here, one
folder per skill:

```
.claude/skills/<name>/SKILL.md
```

Git-tracked directly, same as everything else under `.claude/` —
`git pull` is the whole sync mechanism. No copy-out step, no drift to
manage.

## SKILL.md shape

```markdown
---
name: <name>
description: <one line, specific enough that Claude picks this skill
  for the right prompts and ignores it for everything else. State
  WHEN to use it, not just what it does.>
---

# /<name> — <what it does>

<Body: how to run it, step by step. Reference other files in this
repo by path — they resolve normally since this file lives inside
the repo it describes.>
```

## When this is the wrong place

If the skill needs to trigger in sessions outside this repo too — a
cross-project domain skill, not something specific to this
codebase — it belongs at `~/.claude/skills/<name>/SKILL.md` instead.
See `docs/13-skills/README.md` for that convention and why it needs
more ceremony than this folder does.
