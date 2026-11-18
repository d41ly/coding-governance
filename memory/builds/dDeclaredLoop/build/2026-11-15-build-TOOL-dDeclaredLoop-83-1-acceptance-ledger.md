# TOOL-dDeclaredLoop-83 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-83

No merge bar, no self-test suite and no gate leg ran in this pass. The pass wrote spec text only: 75
S27's fallback clause, 75 AC27 and 75's guard arm line, as a rev-9 bump of the 75 spec with its
revision-log line. Each criterion was observed by its own grep over the 75 spec in the working tree,
and AC1 and AC3 were also read at the pass's base `4975700c6` through `git show`, where AC1's grep
printed 1 and AC3's AC27-range grep for the plant key printed 0, so both greps can read red. The
claims S1 restates were read against `tools/loop/guard.py#read_remerge_policy` and
`tools/loop/guard.py#check_push_range` as built: `uncomputable` for an octopus merge or a git without
`merge-tree --write-tree`, `conflicted` for an exit 1, and `failed` for an exit 0 with no tree id, any
other exit or a start that fails, printing `the clean re-merge failed: <detail>`; and
`push-merge-tree-fatal` is owed exit 1 in `tools/loop/guard.py#run_selftest`'s owed map. No guard
plant was run: no code moved, and 75's own pass runs the plant.

Owed to the close: every leg the spec's section 7 names. The spec declares no `New arm:` line.

**Evidences:** TOOL-dDeclaredLoop-83
- AC1 — `any other exit code grades against the parents alone` — `grep -c` over the 75 spec printed 0; at the base it printed 1.
- AC2 — `never a fall to the parents` — over the S27-to-S28 range of the 75 spec, `grep -c` printed 1 for it, 1 for `conflicted paths hold the policy path`, 1 for `no tree id` and 1 for `its blob parses`.
- AC3 — `push-merge-tree-fatal` — over the AC27-to-AC28 range, `grep -c` printed 1 for it and 1 for `the clean re-merge failed: 128`, and `grep -c "^New arm: tools/loop/guard.py.*tree-fatal"` over the file printed 1; at the base the range grep for the plant key printed 0.
