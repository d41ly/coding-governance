# TOOL-dDeclaredLoop-59 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-59

No merge bar, no self-test suite and no gate leg ran in this pass, and `guard.py --selftest` was not
run. The criteria were observed on node `d` (win32) by probes of the unit's own code, each plant by
direct CLI over its own scratch repository under the host temp directory: the three new plants, and
unit 44's `push-merge-resolution-edit`, `push-merge-carries-trailered`, `push-no-trailer` and
`push-new-branch` plants kept green beside them. `read_remerge_policy` was also probed in process over
a scratch repository holding two unrelated roots: two parents answered the other-exit reason naming
merge-tree's exit, three parents the octopus reason, and a commit re-merged with itself the empty
table and no reason.

Owed to the close: every leg the spec's section 7 names; the RED-first observation of the spec's one
`New arm:` line, each new plant staged red against unit 44's first-parent grade and 44's own plant held
owed 1 under the key grade; and the `loop guard fixtures` row in `tools/run-gates/selftest-budgets.txt`
re-priced from the main loop's reading of the leg alone, as that row's own rule says, since the three
plants each add one scratch repository to that leg.

The close's RED-first observation, made by the main loop on 2026-11-17 at `a48272d09` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
`python tools/loop/guard.py --selftest` with every function the unit's pass changed in `tools/loop/guard.py`
swapped back to its pre-pass source exited 1, and 0 once restored: RED observed.

**Evidences:** TOOL-dDeclaredLoop-59
- AC1 — `push-merge-both-sides-clean` — `python tools/loop/guard.py --fixture --plant push-merge-both-sides-clean`: side's trailered cap raise and main's trailered `review.max-rounds` merged cleanly with `--no-ff`; the arm graded all three commits, the merge included, printed no finding and `all held`, and exited 0.
- AC2 — `review.max-rounds` — `python tools/loop/guard.py --fixture --plant push-merge-resolution-edit`, unit 44's plant unchanged: with its trailer and record the merge printed no finding, exit 0; with neither it was refused naming `merge <sha8>`, `review.max-rounds` and the merge's own change, exit 1; the plant printed `all held`.
- AC3 — `push-merge-conflict-pick` — `python tools/loop/guard.py --fixture --plant push-merge-conflict-pick`: the conflicting `review.max-rounds` resolved to side's value with no trailer on the merge; the arm printed the merge's sha `graded against its parents only` with the reason `its re-merge conflicts, merge-tree exit 1`, no finding, `all held`, and exited 0.
- AC4 — `push-merge-octopus` — `python tools/loop/guard.py --fixture --plant push-merge-octopus`: main, `b1` and `b2` each set a different key and main merged both branches in one octopus merge; the arm printed the merge's sha `graded against its parents only` with the octopus reason naming its parent count, no finding, `all held`, and exited 0.
