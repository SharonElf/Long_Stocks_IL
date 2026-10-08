#!/usr/bin/env python3
"""
doc-drift-gate.py — Stop hook for the chaperone workflow.

Purpose:
  Layer 2 of the doc-drift gate. When the agent finishes a turn (Stop event),
  the harness invokes this script. The script inspects the git diff of the
  current "unit baseline" (committed but unpushed + uncommitted + untracked)
  and applies a path -> required-doc map. If any mapped trigger path changed
  WITHOUT its required doc also being touched, the script exits 2 with a
  message that lists each violation. The harness blocks the stop and re-prompts
  the agent.

Contract with the harness:
  - Reads JSON context from stdin.
  - If stop_hook_active is true, exits 0 immediately (avoids 8-block cap loop).
  - Otherwise, exits 0 (clean) or exits 2 (block + reason on stderr).
  - On ANY unexpected exception: exits 2 (fail closed).

Editing the map:
  Each project must fill in the MAP list below for its own drift-prone docs.
  Each rule is a dict with a 'trigger' glob and a 'required_doc' glob. If any
  path in the changeset matches 'trigger', then at least one path in the
  changeset must also match 'required_doc' -- otherwise it's a violation.

  See `docs/08-testing/definition-of-done.md` for the full close-unit
  procedure that this gate enforces a subset of.

Known limits:
  1. Verifies a doc was TOUCHED, not that it's correct.
  2. Blind to changes in paths not in the map.
  3. Stop hooks self-override after 8 consecutive blocks.
"""

import sys
import json
import fnmatch
import subprocess

# === MAP (each project edits this for its own drift-prone docs) ============
# Example rules (delete and replace with your project's):
#   {"trigger": "src/**/*.py", "required_doc": "context/architecture.md"},
#   {"trigger": "migrations/*.sql", "required_doc": "docs/data-model.md"},
#
# Leave MAP empty to disable the gate. With MAP = [], the script always
# exits 0 (no rules to check).
MAP = []
# ===========================================================================


def _run(*args):
    """Run a subprocess; return non-empty stdout lines. Never raises."""
    try:
        result = subprocess.run(
            list(args), capture_output=True, text=True, check=False, timeout=15
        )
        return [line for line in result.stdout.splitlines() if line.strip()]
    except Exception:
        return []


def _normalize(p):
    """Normalize to forward slashes for cross-platform glob matching."""
    return p.replace("\\", "/").strip()


def _changed_paths():
    """Union of: committed-since-last-push, uncommitted, untracked."""
    paths = set()

    # Committed since last push (origin/main..HEAD).
    # If origin/main doesn't exist (fresh clone, no remote), this just returns [].
    committed = _run("git", "diff", "--name-only", "origin/main..HEAD")
    paths.update(_normalize(p) for p in committed)

    # Uncommitted (staged + unstaged) -- working tree vs HEAD.
    uncommitted = _run("git", "diff", "--name-only", "HEAD")
    paths.update(_normalize(p) for p in uncommitted)

    # Untracked but not gitignored.
    untracked = _run("git", "ls-files", "--others", "--exclude-standard")
    paths.update(_normalize(p) for p in untracked)

    return paths


def _any_match(glob_pattern, paths):
    """True iff any path matches the given glob pattern."""
    pat = _normalize(glob_pattern)
    return any(fnmatch.fnmatch(p, pat) for p in paths)


def main():
    # 1. Read harness context from stdin.
    try:
        ctx = json.load(sys.stdin)
    except Exception:
        ctx = {}

    # 2. Short-circuit when already in a block loop (avoids 8-block cap).
    if ctx.get("stop_hook_active"):
        sys.exit(0)

    # 3. If no rules, gate is disabled.
    if not MAP:
        sys.exit(0)

    # 4. Get the changeset for the current unit baseline.
    changed = _changed_paths()
    if not changed:
        sys.exit(0)

    # 5. Apply each map rule.
    violations = []
    for rule in MAP:
        if _any_match(rule["trigger"], changed) and not _any_match(
            rule["required_doc"], changed
        ):
            violations.append(
                f"changed `{rule['trigger']}` -> required `{rule['required_doc']}` was NOT touched"
            )

    # 6. Block or pass.
    if violations:
        print("doc-drift-gate: in-flight doc updates required", file=sys.stderr)
        print("", file=sys.stderr)
        for v in violations:
            print(f"  - {v}", file=sys.stderr)
        print("", file=sys.stderr)
        print(
            "Update the required docs in this unit's work, OR add a single",
            file=sys.stderr,
        )
        print(
            "explanatory line to the required doc if no real update is needed",
            file=sys.stderr,
        )
        print(
            "(the gate verifies the file was touched, not its content).",
            file=sys.stderr,
        )
        sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:
        # Fail closed: any unexpected error blocks the stop with the error.
        print(f"doc-drift-gate: internal error -- failing closed: {e}", file=sys.stderr)
        sys.exit(2)
