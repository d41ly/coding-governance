# TOOL-dGroundRules-55 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-55

No merge bar, gate leg or self-test suite ran in this pass. The built-tree criteria ran verbatim from
this worktree's root over `82f44fa67` with this pass's record in the working tree. The staged break
of AC2 ran in a clone under `%TEMP%/gr55`, checked out at `82f44fa67` with this pass's record copied
over the clone's and one paragraph backticking a path appended. Owed at the close: the
`gotchas selftest`, `memory hygiene`, `recall floor` and `recall floor arms` legs over the built tree.

**Evidences:** TOOL-dGroundRules-55
- AC1 — `grep -c "never runs the check" memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md` printed `2`, the symptom head and the fix; `grep -c "TOOL-dGroundRules-44" memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md` printed `2` and `grep -c "closing quote" memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md` printed `2`; each printed `0` over the record at `82f44fa67`.
- AC2 — `python tools/memory-tree/gotchas.py --check` exited 0 and `grep -c "| class | 3 |  | an acceptance criterion names" memory/gotchas/INDEX.md` printed `1`; in the clone, with the break appended, `--check` exited 1 naming `HYGIENE check 17: memory/gotchas/INDEX.md is stale`, and after `gotchas.py --write` the grep printed `0`, the row's Anchors cell reading `4`.
