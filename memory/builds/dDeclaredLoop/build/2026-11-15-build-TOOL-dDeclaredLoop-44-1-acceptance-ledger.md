# TOOL-dDeclaredLoop-44 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-44

No merge bar, no self-test suite and no gate leg ran in this pass, and `guard.py --selftest` was not
run. The criteria were observed on node `d` (win32) by probes of the unit's own code, each plant by
direct CLI over its own scratch repository under the host temp directory: the three new plants, and
the `push-no-trailer` and `write-guarded-rollback` plants kept green beside them. The codebase map's
`gen_map.py --check` exited clean, since the pass adds no top-level definition.

Owed to the close: every leg the spec's section 7 names; the RED-first observation of the spec's one
`New arm:` line, each new plant staged red against the built arm's `--no-merges` read, against
`read_added_units` reading a merge through `--diff-filter=A`, and against the all-zero base passed
to git as written; and the `loop guard fixtures` row in `tools/run-gates/selftest-budgets.txt` read
against the leg's own timing, since the three plants each add one scratch repository to that leg.

The close's RED-first observation, made by the main loop on 2026-11-17 at `c7cbca292` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
`python tools/loop/guard.py --selftest` with every function the unit's pass changed in `tools/loop/guard.py`
swapped back to its pre-pass source exited 1, and 0 once restored: RED observed.

**Evidences:** TOOL-dDeclaredLoop-44
- AC1 — `push-merge-carries-trailered` — `python tools/loop/guard.py --fixture --plant push-merge-carries-trailered` read every commit of the range, the merge included, graded the side's trailered commit alone, printed no finding and `all held`, and exited 0: the merge's combined diff omits the policy file, so the merge owed nothing.
- AC2 — `review.max-rounds` — `python tools/loop/guard.py --fixture --plant push-merge-resolution-edit`: the merge carrying its trailer and the change record its resolution adds was graded and printed no finding, exit 0; the same merge with neither was refused twice naming `merge <sha8>`, `review.max-rounds` and the merge's own change, exit 1; the plant printed `all held`.
- AC3 — `refs/remotes/origin/main` — `python tools/loop/guard.py --fixture --plant push-new-branch` with `GOV_REMOTE` and `GOV_DEFAULT_BRANCH` set empty: the all-zero base read as `origin/main, the landed revision`, the count line naming the commit count the plant derives from its own history, exit 0; with that tracking ref deleted the arm printed `cannot judge` naming `refs/remotes/origin/main`, exit 2; the plant printed `all held`.
