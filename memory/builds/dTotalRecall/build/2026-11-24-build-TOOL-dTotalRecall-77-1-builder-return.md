**Serves:** journal TOOL-dTotalRecall-77
**Caused-by:** TOOL-dTotalRecall-77

# TOOL-dTotalRecall-77 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `0573fa2c5` from [2026-11-24-prompt-TOOL-dTotalRecall-77-build-brief](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-77-build-brief.md), recorded whole, each number's line tagged by the recorder; the pass tip is `049c4503d`.

## Why

Spec rev-4 holds as written. Section 4's probe printed every line AC1 states, unit 76's ledger holds the two `live` lines, and the sweep line before them is rc=0 with no failure line. The acceptance ledger is written and the spec is CLOSED. (DERIVED 2026-11-24, the pass)

## Summary

Built TOOL-dTotalRecall-77 with no product code change. The commit holds the acceptance ledger (C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/memory/builds/dTotalRecall/build/2026-11-24-build-TOOL-dTotalRecall-77-1-acceptance-ledger.md), the spec header set to CLOSED (its date was already 2026-11-24), RUN.md, and the rows gen_build_index.py rewrote (LIVE.md, backlog/TOOL.md, the build README, the spec's record table). Every path was inside the declared write set, so no extra --dispatch was made. The brief was already recorded at eb2dafe7df71, unchanged.

Claims checked against the tree before writing:
- `skills/session-kickoff/manifest-check.sh` at `aec378661` reads as the spec cites at its `fail()` and `exit "$status"` lines.
- The checker's file is unchanged from `aec378661` to the base.
- Unit 76 section 4's `print_read`, its staging and its last-unit read are as the spec describes. (DERIVED 2026-11-24, the pass)
- The consumes-from and hands-off ends in specs 78, 79 and 80 agree on `read_checker`. (DERIVED 2026-11-24, the pass)
No divergence was found.

Checks run (DERIVED 2026-11-24):
- AC1: section 4's two fences, saved as one script whose text a diff found identical to the spec's fences, printed the stated lines and exited 0. Over the same failing stub the old pipe printed 0. The git grep over unit 76's ledger printed `live rc=1` and its check-9 line.
- AC2: the Evidences git grep printed this ledger's block line, before and after the commit. The last unit line before `live` is unit 87's `073d03dd7`, rc=0, with no failure line beneath it. (DERIVED 2026-11-24, the pass)
- The probe's body calls `mktemp -d`; it ran with TMPDIR set to the run's scratch directory so nothing landed outside it, and a Decided: trailer records that. It removed its tree.

Which gate this stands in for: the probe stands in for no section 7 leg. It is the only exercise of `read_checker`, which is spec text. The checker itself was not run, as the spec requires. No gate, suite or bar was run by hand; the commit's pre-commit hook ran its staged checks and passed. (DERIVED 2026-11-24, the pass)

Owed to the close: the section 7 legs `memory hygiene`, `recall floor` and `recall floor arms`. There is no new arm, so no RED-first observation is owed. (DERIVED 2026-11-24, the pass)

The gotchas checklist ran over HEAD~1..HEAD. The classes that bear on a ledger were checked: no wrapped token, no pipe in a table cell, and the red stub is not vacuous because the lifted `fail()` count is 1. Nothing needed a change. The working tree is clean and no command was skipped.

With no unit INPROGRESS, the index now derives the build as DEFERRED in LIVE.md and the build README, and lists TOOL-dTotalRecall-27 in backlog/TOOL.md under unit 100. That lasts until the next unit is flipped INPROGRESS.
