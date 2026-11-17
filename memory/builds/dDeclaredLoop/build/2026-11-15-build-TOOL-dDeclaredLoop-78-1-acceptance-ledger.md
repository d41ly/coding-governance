# TOOL-dDeclaredLoop-78 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-78

No merge bar, no self-test suite and no gate leg ran in this pass, and `guard.py --selftest` was not
run. The criteria were observed on node `d` (win32) by probes of the unit's own code, each plant by
direct CLI over its own scratch repository under the host temp directory: the four new plants, unit
69's `push-merge-revert-to-unchanged-side`, unit 59's `push-merge-both-sides-clean`,
`push-merge-conflict-pick` and `push-merge-octopus`, and unit 44's `push-merge-resolution-edit`,
`push-merge-carries-trailered`, `push-no-trailer` and `push-new-branch`, every one printing `all held`
at its owed exit. The staged-verdict plants and `write-guarded-rollback` read no code this pass changed
and were not run.

Owed to the close: every leg the spec's section 7 names; the RED-first observation of the spec's one
`New arm:` line, AC4 staged red against an unparseable re-merge sent to the parents as unit 59 built it
and AC1 to AC3 against a re-merge tree lacking the file read as `uncomputable`, both in
`tools/loop/guard.py#read_remerge_policy`; and the `loop guard fixtures` row in
`tools/run-gates/selftest-budgets.txt` re-priced from the main loop's reading of the leg alone, as that
row's own rule says, since the four new plants each add one scratch repository to that leg.

The close's RED-first observation, made by the main loop on 2026-11-17 at `c7cbca292` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
`python tools/loop/guard.py --selftest` with every function the unit's pass changed in `tools/loop/guard.py`
swapped back to its pre-pass source exited 1, and 0 once restored: RED observed.

**Evidences:** TOOL-dDeclaredLoop-78
- AC1 — `push-merge-resurrect-deleted-policy` — main deleted the policy file, the run branch merged main keeping its own file with no trailer or record; the clean re-merge read `absent`, the merge was refused naming `merge <sha8> · .governance/policy.toml · review.max-rounds` among every key it kept, exit 1, printing `all held`.
- AC2 — `push-merge-resurrect-emptied-policy` — the same history with main's file emptied to no keys; the re-merge read `present` with an empty table, the merge refused naming the same, exit 1, printing `all held`.
- AC3 — `push-merge-both-absent` — the run branch merged main taking the deletion; the push arm exited 0 naming `0 finding(s)` and printed `all held`; `push-merge-revert-to-unchanged-side` exited 1 naming `review.max-rounds` in both variants, printing `all held`.
- AC4 — `does not parse at C` — main and the run branch each declared `[leases]` apart, git's clean re-merge declared it twice; the merge, its blob equal to its first parent's, was refused as `merge <sha8> · .governance/policy.toml does not parse at C, so its changed keys are unknown`, exit 1, printing `all held` and no `Traceback`.
