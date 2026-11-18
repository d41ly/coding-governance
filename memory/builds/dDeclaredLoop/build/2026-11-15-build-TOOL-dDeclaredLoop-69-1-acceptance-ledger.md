# TOOL-dDeclaredLoop-69 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-69

No merge bar, no self-test suite and no gate leg ran in this pass, and `guard.py --selftest` was not
run. The criteria were observed on node `d` (win32) by probes of the unit's own code, each plant by
direct CLI over its own scratch repository under the host temp directory: the new plant, unit 59's
`push-merge-both-sides-clean`, `push-merge-conflict-pick` and `push-merge-octopus` plants, and unit
44's `push-merge-resolution-edit`, `push-merge-carries-trailered`, `push-no-trailer` and
`push-new-branch` plants, every one printing `all held` at its owed exit. The staged-verdict plants and
`write-guarded-rollback` read no code this pass changed and were not run.

Owed to the close: every leg the spec's section 7 names; the RED-first observation of the spec's one
`New arm:` line, the new plant staged red against unit 59's grade in `tools/loop/guard.py#check_push_range`;
and the `loop guard fixtures` row in `tools/run-gates/selftest-budgets.txt` re-priced from the main
loop's reading of the leg alone, as that row's own rule says, since the new plant adds one scratch
repository to that leg.

The close's RED-first observation, made by the main loop on 2026-11-17 at `a48272d09` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
`python tools/loop/guard.py --selftest` with every function the unit's pass changed in `tools/loop/guard.py`
swapped back to its pre-pass source exited 1, and 0 once restored: RED observed.

**Evidences:** TOOL-dDeclaredLoop-69
- AC1 — `merge <sha8> · .governance/policy.toml · review.max-rounds` — `python tools/loop/guard.py --fixture --plant push-merge-revert-to-unchanged-side`: in both variants, the run branch changing the cap and the run branch leaving the policy file alone, the merge of main setting `review.max-rounds` back to the base's value with neither trailer nor record was refused naming that merge and key, exit 1; the plant printed `all held` and exited 1.
- AC2 — `review.max-rounds` — `python tools/loop/guard.py --fixture --plant push-merge-both-sides-clean` exited 0 printing `all held`, its needle now counting the side's and main's commits alone since the merge equals its re-merge; `--plant push-merge-resolution-edit` exited 1, its bare merge refused naming `review.max-rounds`, its trailered one clean, printing `all held`.
- AC3 — `graded against its parents only` — `python tools/loop/guard.py --fixture --plant push-merge-octopus` and `--plant push-merge-conflict-pick` each exited 0 printing the merge's sha `graded against its parents only`, with the octopus reason and the merge-tree conflict reason, no finding, and `all held`.
- AC4 — `0 finding(s)` — the same plant's trailered scenarios, each merge carrying `Gov-Policy: policy.review.max-rounds 5 -> 3` (main's value to the base's) and a record naming `policy.review.max-rounds`, each exited 0 naming `0 finding(s)`.
