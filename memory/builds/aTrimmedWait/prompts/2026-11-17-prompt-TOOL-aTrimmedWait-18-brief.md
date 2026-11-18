# Brief — aTrimmedWait: the reconcile with local main at 8eda4a5a0, before the landing merge

**Serves:** research TOOL-aTrimmedWait-18

## The prompt

> merge to main

The owner's words in this session. `TOOL-aTrimmedWait-12` reconciled the branch with local main at
`5d48501da`; since then local main took aHastenedSweep's and aPiecewiseGrade's landings and stands
at `8eda4a5a0`. A dry `git merge-tree --write-tree HEAD main` conflicts in five files, two of them
product code, so this reconcile is a unit of its own, as `TOOL-aTrimmedWait-12` was.

## The brief

### Goal
Merge local main at `8eda4a5a0` into `branch/speedups-9c2e63` and resolve its five conflicts, so the
landing merge of the branch onto local main is conflict-free. Both sides' changes stay as each
shipped them.

### Items
1. The merge: `git merge --no-ff 8eda4a5a0` on the branch, committed with both parents and no
   conflict marker. Every file outside these five keeps the merge's own resolution:
   - `memory/project/readme-contract.txt`: keep every row, main's two then this branch's.
   - `memory/guides/SESSION-KICKOFF.md`: `last-audit` re-stamped at the merge, after §B is re-read
     against both sides' watched changes, as the manifest's own stamp rule says, and
     `last-body-change` the value that rule derives.
   - `tools/memory-tree/gen_build_index.py`, `main()`: main's `_COVERAGE_MEMO = None` stays inside
     the `--with-verdicts` `finally`, and this branch's `--write-staged` dispatch follows that
     block at its own indent, unchanged.
   - `tools/memory-tree/check-memory-hygiene.test.sh`: `FLOOR_ASSERTIONS` is this branch's figure
     plus main's raise since `5d48501da`, both sides' comment lines kept and one `MERGED` line
     naming the sum.
   - `tools/unattended/unattended.test.sh`: both sides' comment blocks stay. THE TWO SIDES' TOTAL
     FLOORS READ THE SAME NUMBER BY COINCIDENCE, so git keeps that line without a conflict and the
     sum is lost: `FLOOR_ASSERTIONS` is this branch's figure plus main's raise since `5d48501da`,
     with one `MERGED` line naming the sum, and each `FLOOR_SHARD_<n>` is this branch's figure
     plus main's raise to that shard since `5d48501da`.
   - `tools/workflows/unattended-build.test.sh` merges without a conflict; its `FLOOR_ASSERTIONS`
     is checked by the same rule.
2. The auto-merged files: name any place where one side's change reads the other's old behaviour,
   in `gen_build_index.py`, `unattended.sh`, `check-memory-hygiene.sh` and `.githooks/pre-commit`
   especially, and resolve a contradiction in this unit; none found is a finding the spec records as
   checked.
3. Regenerate the generated outputs after the merge (`python tools/run-gates/regen.py --write`,
   `python tools/memory-tree/gen_build_index.py --write` after `git add`,
   `python tools/codebase-map/gen_map.py --write`) and commit them in the merge.

### Acceptance
- The merge commit has both parents, `8eda4a5a0` among them, and `git grep -n '^<<<<<<< '` prints
  nothing.
- `bash -n` passes on every conflicted shell file and `python -m py_compile` on `gen_build_index.py`.
- A dry `git merge-tree --write-tree` of the branch onto `8eda4a5a0` reports no conflict.
- The resolutions read as item 1 states, by grep, each floor checked against its two inputs.

### Gates
The merge bar once at the close, without the self-test suites, run by the main loop; the self-test
suites of the conflicted suites once at the close on a frozen clone, also the main loop's. The pass
runs only direct checks.

### Non-goals
- Landing or pushing: the main loop makes the landing merge onto local main after the bar, and the
  owner asked for no push.
- Kit version bumps: `push-main.sh` mints them at the push boundary.
- Any behaviour change on either side beyond what a conflict forces.
- ANY SELF-TEST SUITE OR BAR INSIDE THE PASS, A SLICED SUITE INCLUDED.
- A pass commit without its acceptance ledger at
  `memory/builds/aTrimmedWait/build/2026-11-17-build-TOOL-aTrimmedWait-18-1-acceptance-ledger.md`.
- An edit after the commit that sets the spec CLOSED: the status flip is the last change of the pass.

## Owner confirmation

> merge to main
