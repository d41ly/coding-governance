# Brief — aTwinnedPass: the reconcile with local main at a76c6afe7, before the landing merge

**Serves:** research TOOL-aTwinnedPass-13

## The prompt

> merge to local main

The owner's word in this session, after the bar went green on `d8bda2e01`. A trial `git merge --no-ff` of `branch/dazzling-jackson-b895c0` onto local main at `a76c6afe7` (aLightenedLoop's landing, equal to `origin/main`) conflicted in four files. The scratch-guard refused the conflict resolution as a product write no buildable unit owns, so the trial was aborted, and the reconcile is this unit, as `TOOL-aLightenedLoop-8` was for that build.

## The brief

### Goal
Merge local main at `a76c6afe7` into `branch/dazzling-jackson-b895c0` and resolve its four conflicts, so that the landing merge of the branch onto local main is conflict-free. Both sides' changes stay as each shipped them.

### Items
1. The merge: `git merge --no-ff a76c6afe7` on the branch, committed with both parents and no conflict marker. The trial conflicted in exactly these four files; every other file keeps the merge's own resolution:
   - `memory/project/readme-contract.txt`: keep both rows, `memory/builds/aLightenedLoop/README.md` then `memory/builds/aTwinnedPass/README.md`.
   - `tools/unattended/unattended.test.sh`: `FLOOR_ASSERTIONS` becomes 3348, the common base's 3329 plus main's 6 (`TOOL-aLightenedLoop-3` and `-8`) plus this branch's 13 (`TOOL-aTwinnedPass-3` and `-5`). Both sides' comment blocks stay, and one `MERGED` line names the sum. `FLOOR_SHARD_3` (main's) and `FLOOR_SHARD_4` (this branch's) auto-merge to 451 and 423; verify both against the merged suite rather than trusting the merge.
   - `tools/workflows/unattended-build.test.sh`: `FLOOR_ASSERTIONS` becomes 1043, the base's 950 plus main's 4 (`TOOL-aLightenedLoop-3`) plus this branch's 89 (`TOOL-aTwinnedPass-1`, `-4`, `-11`), comments kept and one `MERGED` line.
   - `tools/workflows/unattended-unit.js`, the `DRIVER_STEPS` ternary: keep this branch's `cfg.passBase !== undefined` branch unchanged, and in the remaining unattended branch take main's `TOOL-aLightenedLoop-3` text ("The main loop declared this unit's write set with ... before it spawned you ... Before you write a path outside that set, declare it with the same command ..."), not the base's "Declare the write set ... before you write anything".
2. The design question the merge raises: main's `TOOL-aLightenedLoop-3` moved the first `--dispatch` from the builder to the main loop (the build harness's `declare` return in `unattended-build.js`), which is what this build's `passBase` branch already assumed. State whether the merged `passBase` sentence and main's `declare` instruction agree, and whether any doc this build wrote (`tools/unattended/VERBS.template.md`, `memory/guides/UNATTENDED-VERBS.md`, `tools/unattended/README.md`, `help/pass-legs.md`) contradicts main's text after the auto-merge. A contradiction is resolved in this unit; none is a finding the spec records as checked.
3. `tools/unattended/unattended.sh` auto-merged: main's `verb_dispatch` hunk is comment-only (the spec-token window), and this branch's condition-1 change (`_c1_own`, `_c1_gen`, `check_generated_output`) sits inside that window. Verify the merged comment's claim that nothing in the window writes the tree still holds with `check_generated_output` in it.
4. Regenerate the generated outputs after the merge (`python tools/run-gates/regen.py --write`, `python tools/memory-tree/gen_build_index.py --write` after `git add`, `python tools/codebase-map/gen_map.py --write`) and commit them in the merge.

### Acceptance
- The merge commit has both parents, `a76c6afe7` among them, and `git grep -n '^<<<<<<< '` prints nothing.
- `bash -n` passes on both suites, and `node --check` on `tools/workflows/unattended-unit.js`.
- A trial `git merge --no-ff --no-commit` of the branch onto `a76c6afe7` reports no conflict.
- The four resolutions read as item 1 states, by grep.

### Gates
The merge bar once at the close, without the self-test suites, run by the main loop. The pass runs only direct checks.

### Non-goals
- Landing or pushing: the main loop makes the landing merge onto local main after the bar, and the owner asked for no push.
- Kit version bumps: `push-main.sh` mints them at the push boundary.
- Any behaviour change on either side beyond what a conflict forces.
- Asks `TOOL-aTwinnedPass-6` to `-10` and `-12`.
- ANY SELF-TEST SUITE OR BAR INSIDE THE PASS, A SLICED SUITE INCLUDED.
- A pass commit without its acceptance ledger: the pass commit carries `memory/builds/aTwinnedPass/build/2026-11-15-build-TOOL-aTwinnedPass-13-1-acceptance-ledger.md`.
- An edit after the commit that sets the spec CLOSED: the status flip is the last change of the pass.
