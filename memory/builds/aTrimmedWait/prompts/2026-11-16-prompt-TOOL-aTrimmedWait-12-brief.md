# Brief — aTrimmedWait: the reconcile with local main at 5d48501da, before the landing merge

**Serves:** research TOOL-aTrimmedWait-12

## The prompt

> merge to main

The owner's words in this session, after the close bar read GREEN on `272a5b3b6`. Local main moved
from this build's base `846d51d39` to `5d48501da` (aTwinnedPass's landing). A dry
`git merge-tree --write-tree main HEAD` conflicts in eight files, five of them product code, so the
reconcile is this unit, as `TOOL-aTwinnedPass-13` was for that build.

Main's `TOOL-aClearedLedger-6` fixed the same partition-arm red this build's `TOOL-aTrimmedWait-11`
fixed, through its own helper `extract_hs_lines`, which folds only the `cache hits` count. The owner
ruled on 2026-11-16 that this branch's `derive_partition_lines` and its fixture arm survive, and
main's `extract_hs_lines` goes.

## The brief

### Goal
Merge local main at `5d48501da` into `branch/speedups-9c2e63` and resolve its eight conflicts, so the
landing merge of the branch onto local main is conflict-free. Both sides' changes stay as each
shipped them, but for the one helper the owner's ruling retires.

### Items
1. The merge: `git merge --no-ff 5d48501da` on the branch, committed with both parents and no
   conflict marker. Every file outside these eight keeps the merge's own resolution:
   - `memory/project/readme-contract.txt`: keep every row, main's four then this branch's.
   - `memory/guides/SESSION-KICKOFF.md`: `last-audit` re-stamped at the merge, after §B is re-read
     against both sides' watched changes, as the manifest's own stamp rule says.
   - `tools/template-size-limits.txt`, the `.claude/skills/unattended/SKILL.md` row: both sides'
     comment blocks stay, and the row is the merged skill's CR-stripped size, measured, with one
     `MERGED` line naming the measure.
   - `tools/memory-tree/gen_build_index.py`, `cmd_write`: one function carrying both sides. Main's
     `TOOL-aLightenedLoop-1` stamp removal before any write, its `TOOL-aLightenedLoop-6` render-state
     read and its `written` record of every write, and the stamp written after the verdicts; this
     branch's `staged` parameter and decline, its moved-only writes (`TOOL-aTrimmedWait-4`), its undo
     and `finally` (`TOOL-aTrimmedWait-8`) and its staging. Every write the merged function makes is
     recorded in `written`, so main's settled-tree check reads the render's own writes. State
     whether a staged decline or an undo can leave a stamp behind, and make it leave none.
   - `tools/memory-tree/check-memory-hygiene.test.sh`: the partition arm keeps this branch's
     `derive_partition_lines` compare and `diff` and its fixture arm, and main's `extract_hs_lines`
     and its comment block go (owner, 2026-11-16). `FLOOR_ASSERTIONS` is the base's 707 plus main's
     raise plus this branch's 42, verified against the merged suite, with both sides' comment lines
     kept and one `MERGED` line naming the sum.
   - `tools/unattended/unattended.sh`, `verb_dispatch`: this branch's hunk, the order read taken from
     `check_unit_spec`. Main's no-fork order read (`order_verb_of "<spec>" >/dev/null` then
     `$_order_verb`) replaces the command substitution in `check_unit_spec`, so no order read forks.
   - `tools/unattended/unattended.test.sh`: `FLOOR_ASSERTIONS`, `FLOOR_SHARD_3` and `FLOOR_SHARD_4`
     are each the base's figure plus main's raises plus this branch's, every comment line kept and
     one `MERGED` line per floor naming its sum, each verified against the merged suite rather than
     trusted to the arithmetic.
   - `tools/workflows/unattended-build.test.sh`: `FLOOR_ASSERTIONS` the same way.
2. The auto-merged files: name any place where one side's change reads the other's old behaviour,
   in `gen_build_index.py`, `unattended.sh` and `check-memory-hygiene.sh` especially, and resolve a
   contradiction in this unit; none found is a finding the spec records as checked.
3. Regenerate the generated outputs after the merge (`python tools/run-gates/regen.py --write`,
   `python tools/memory-tree/gen_build_index.py --write` after `git add`,
   `python tools/codebase-map/gen_map.py --write`) and commit them in the merge.

### Acceptance
- The merge commit has both parents, `5d48501da` among them, and `git grep -n '^<<<<<<< '` prints
  nothing.
- `bash -n` passes on every conflicted shell file and `python -m py_compile` on `gen_build_index.py`.
- A dry `git merge-tree --write-tree` of the branch onto `5d48501da` reports no conflict.
- `gen_build_index.py --selftest` exits 0 on a frozen clone of the merge; the main loop runs it.
- The resolutions read as item 1 states, by grep.

### Gates
The merge bar once at the close, without the self-test suites, run by the main loop; the self-test
suites of the three conflicted suites once at the close on a frozen clone, also the main loop's. The
pass runs only direct checks.

### Non-goals
- Landing or pushing: the main loop makes the landing merge onto local main after the bar, and the
  owner asked for no push.
- Kit version bumps: `push-main.sh` mints them at the push boundary.
- Any behaviour change on either side beyond what a conflict or the owner's ruling forces.
- ANY SELF-TEST SUITE OR BAR INSIDE THE PASS, A SLICED SUITE INCLUDED.
- A pass commit without its acceptance ledger at
  `memory/builds/aTrimmedWait/build/2026-11-16-build-TOOL-aTrimmedWait-12-1-acceptance-ledger.md`.
- An edit after the commit that sets the spec CLOSED: the status flip is the last change of the pass.

## Owner confirmation

> merge to main
