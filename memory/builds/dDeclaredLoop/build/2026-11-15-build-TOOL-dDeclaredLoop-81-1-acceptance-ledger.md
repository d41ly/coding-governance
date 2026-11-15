# TOOL-dDeclaredLoop-81 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-81

No merge bar, no self-test suite and no gate leg ran in this pass, and `guard.py --selftest` was not
run. The criteria were observed on node `d` (win32, git 2.54.0.windows.1) by probes of the unit's own
code: the three new plants by direct CLI, each over its own scratch repository under the host temp
directory, and a `python -c` probe in `tools/loop/`. The existing push plants of units 44, 59, 69 and
78, which reach the changed re-merge reader and push arm, were run the same way and each printed
`all held`; the staged-verdict plants and `write-guarded-rollback` read no code this pass changed and
were not run. A `python -c` probe with `run_merge_tree` swapped read the state table: exit 0 with no
output as `failed` `0 no tree id`, exit -9 with no standard error as `failed` `-9`, exit 1 as
`conflicted`, an `OSError` at start as `failed` `start failed: ...`, and the probe answering false as
`uncomputable` `this git has no merge-tree --write-tree`.

Owed to the close: every leg the spec's section 7 names; the RED-first observation of the spec's one
`New arm:` line in `tools/loop/guard.py#read_remerge_policy` and `tools/loop/guard.py#check_push_range`;
and the `loop guard fixtures` row in `tools/run-gates/selftest-budgets.txt` re-priced from the main
loop's reading of the leg alone, as that row's own rule says, since the three new plants each add one
scratch repository to that leg.

**Evidences:** TOOL-dDeclaredLoop-81
- AC1 — `the clean re-merge failed: 128` — `push-merge-unrelated-histories`, its bare scenario: the orphan merge, untrailered, exited 1 naming `the clean re-merge failed: 128 fatal: refusing to merge unrelated histories` and `merge <sha8> · .governance/policy.toml · review.max-rounds`; the plant printed `all held` and exited 1.
- AC2 — `0 finding(s)` — the same plant's first scenario, the merge carrying `Gov-Policy: policy.review.max-rounds 4 -> none` and a record naming `policy.review.max-rounds`, exited 0 naming `0 finding(s)` and printing `the clean re-merge failed: 128`.
- AC3 — `push-merge-tree-fatal` — exited 1 printing `the clean re-merge failed: 128 fatal: fx stand-in`, `merge <sha8> · .governance/policy.toml · review.max-rounds`, `merge-tree runs: 1` and `all held`.
- AC4 — `push-merge-no-write-tree` — exited 0 printing `graded against its parents only — this git has no merge-tree --write-tree`, `merge-tree runs: 0` and `all held`.
- AC5 — `check_write_tree_usage` — answered True on git 2.54's usage line and False on the trivial-form line `usage: git merge-tree <base-tree> <branch1> <branch2>`; `resolve_write_tree_support()` answered True on this node.
