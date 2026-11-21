# Brief — dSkippedRecord: the close's run-record commit is made only when staging left a diff

**Serves:** research TOOL-dSkippedRecord-1

## The prompt

> In coding-governance, fix the commit in `write_run_record` (`tools/unattended/unattended.sh`) so a close whose re-rendered run record is byte-identical after staging skips the commit instead of failing with a printed line. Route through `/session-kickoff` first; a shipped-kit edit is Tier-2. Reuse the shape `tools/push-main.sh#write_staged_change` landed with (stage, answer 2 on a failed `git status`/`git add`, answer 1 when `git diff --cached --quiet` exits 0, every caller refuses on 2). Add an `unattended.test.sh` arm that reproduces the empty stage (RED on the current driver, GREEN after) and one for a failed stage. Drain the `tools/unattended/unattended.sh` row from `memory/project/stage-commit-sites.txt` in the fixing commit, so the leg `shell hygiene (a stage committed with no staged-diff test)` reads it admitted. Done = the arms observed RED then GREEN and recorded, the registry row gone, the leg green. Do not run `--selftests` of the unattended kit without asking the owner; land only on the owner's explicit ask through `bash tools/push-main.sh` from the primary tree.

## The brief

### Goal
`write_run_record` stages the run record and the paths its index render moved, then answers that
stage the way `write_staged_change` answers its own: 0 the stage holds a diff, 1 nothing is staged,
2 a stage or the staged-diff test failed. The `in-place` `--close` commit runs only on 0, prints one
skip line on 1 and one refusal line on 2; the verb's exit is unchanged on all three.

### Items
1. `tools/unattended/unattended.sh`: `write_run_record`'s stage-and-commit tail takes the 0/1/2
   answer, its two existing stage-failure lines become the 2 answer's, and a failing
   `git diff --cached --quiet` (exit above 1) is a 2, never read as "staged".
2. `tools/unattended/unattended.test.sh`: an arm whose close re-renders a run record identical to
   the committed one, and an arm whose stage fails.
3. `memory/project/stage-commit-sites.txt`: the `tools/unattended/unattended.sh` row deleted in the
   same commit.

### Acceptance
The empty-stage arm fails on the driver at 81657e77c with "its commit failed" and passes after the
fix, with the skip line printed and HEAD unmoved. The failed-stage arm passes on the fix and fails on
a staged break that commits past a failed stage. Both observations are recorded in the unit's
acceptance ledger. `sh_hygiene.py --stage-commits` over the leg's argv reads the file admitted, its
row gone, and exits 0.

### Gates
The `unattended.test.sh` shard holding the new arms · `shell hygiene (a stage committed with no
staged-diff test)` · `memory hygiene` · `testsuite-counts` · the full bar at landing.

### Non-goals
No other commit site in `unattended.sh`, `lib-unattended.sh` or `pass-tree.sh` · no change to
`tools/push-main.sh` or `tools/gate-lint/sh_hygiene.py` · no change to any verb's exit code (the run
record's S6: every miss is one line and a return 0).

### Limitations
Units run no gates. No unattended `--selftests` without the owner's ask. Landing only on the owner's
ask, through `bash tools/push-main.sh` from the primary tree.

### Reuse
`tools/push-main.sh#write_staged_change` and its four callers are the shape: answer 0, 1 or 2, and
every caller refuses on 2. `push-main.sh` is another kit and `unattended.sh` sources only
`lib-unattended.sh`, so the shape is reused, not the function; the spec decides whether the answer
lives in `lib-unattended.sh` or inside `write_run_record`. `reuse_lookup.py` named no stage-answer
seam in the unattended kit. Recall returned TOOL-dSettledStage-2 (registered this site),
TOOL-aMendedFleet-63 (the run record's commit, S1 to S6), TOOL-dAlignedCarrier-9 and
TOOL-dMendedRecall-2. Recall terms: write_run_record run record close commit in-place stage empty
write_staged_change unchecked-stage stage-commit-sites drained.

## Drawn from the session

> Should the new build dSkippedRecord (one Tier-2 unit: write_run_record in tools/unattended/unattended.sh skips its close commit when staging left nothing, and refuses when staging failed) declare `spec-audit:`? — "No audit (Recommended)"
— owner, kickoff, 2026-11-19

## Owner confirmation

Asked: Say go and I'll start, or adjust any field.
Answer: land it
