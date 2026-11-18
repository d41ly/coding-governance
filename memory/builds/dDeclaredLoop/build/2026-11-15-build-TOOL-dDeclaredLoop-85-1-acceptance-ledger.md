# TOOL-dDeclaredLoop-85 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-85

No merge bar, no self-test suite and no gate leg ran in this pass, and `guard.py --selftest` was not
run. The criteria were observed on node `d` (win32, git 2.54.0.windows.1) by probes of the unit's own
code: the three new plants and the touched plants `push-merge-tree-fatal`, `push-merge-no-write-tree`,
`push-merge-both-sides-clean` and `push-merge-unrelated-histories` by direct CLI, each over its own
scratch repository under the host temp directory and each printing `all held`, and `python -c` probes
in `tools/loop/`.

AC5's probe as the spec spells it, `import guard` then `guard.main(...)`, does not run on this tree:
`tools/loop/floor.py#read_policy_modules` drops a `guard` module that is not the policy kit's from
`sys.modules`, so the in-process grade's `patch.object(sys.modules[__name__], ...)`, written by
TOOL-dDeclaredLoop-81, patches the policy kit's `guard` and raises AttributeError on
`push-merge-tree-fatal` alone, before this unit's code is reached. Under `--selftest` the module is
`__main__` and the grade runs. AC5 was observed by loading `tools/loop/guard.py` under the module name
`loopguard` in one process and calling its `main` twice; the literal probe's spelling is owed to the
spec writer.

Owed to the close: every leg the spec's section 7 names; the RED-first observation of the spec's one
`New arm:` line in `tools/loop/guard.py#check_write_tree_usage`, `tools/loop/guard.py#resolve_write_tree_support`
and `tools/loop/guard.py#run_guard_plant`; and the `loop guard fixtures` row in
`tools/run-gates/selftest-budgets.txt` re-priced from the main loop's reading of the leg alone, as that
row's own rule says, since the three new plants each add one scratch repository to that leg.

The close's RED-first observation, made by the main loop on 2026-11-17 at `a48272d09` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
`python tools/loop/guard.py --selftest` with every function the unit's pass changed in `tools/loop/guard.py`
swapped back to its pre-pass source exited 1, and 0 once restored: RED observed.

**Evidences:** TOOL-dDeclaredLoop-85
- AC1 — `push-merge-probe-failed` — exited 1 printing `the clean re-merge failed: probe failed: start failed: fx stand-in`, `merge <sha8> · .governance/policy.toml · review.max-rounds`, `merge-tree runs: 0` and `all held`.
- AC2 — `push-merge-probe-silent` — exited 1 printing `the clean re-merge failed: probe failed: 129`, `merge-tree runs: 0` and `all held`.
- AC3 — `push-merge-old-git-usage` — exited 0 printing `graded against its parents only — this git has no merge-tree --write-tree`, `merge-tree runs: 0` and `all held`.
- AC4 — `check_write_tree_usage` — answered `supported`, `unsupported`, `probe failed`, `probe failed` and `probe failed` on the five cases; `build_failure_detail` answered `129`, `128 fatal: x` and `start failed: e`; `resolve_write_tree_support()` answered `supported` first on this node.
- AC5 — `push-merge-probe-silent` — run after `push-merge-tree-fatal` in one process, through the module loaded as `loopguard`: both exited 1, the second printing `merge-tree runs: 0` and `all held`, the memo empty after both.
- AC6 — `push-merge-tree-fatal` — exited 1 printing `the clean re-merge failed: 128 fatal: fx stand-in` and `all held`.
- AC7 — `usage probe` — `grep -c` printed 1 over `help/policy.md` and 5 over `tools/loop/guard.py`.
