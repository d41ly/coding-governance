# TOOL-dGroundRules-39 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-39

No merge bar, no gate leg and no self-test suite ran in this pass. AC1 ran in this worktree from the
policy kit's directory. AC2 and AC3 ran on a `git clone` of the branch under `%TEMP%/g39` carrying
the changed `check_policy.py`, each staging applied by a script to the clone's copy of the
receipt-less search in `derive_census_tree`; a third staging, the `*/*/` pattern dropped, printed
`WRONG: ('source', 'tools')` on the planted line, so the depth-2 candidate is seen to count. The
case's plants are copies of the source's registry, so its one traced read is that file, under the
`policy fixtures` guard. Owed at the close: the `policy fixtures` leg over the built tree, AC4
again, and the new arm's red-first observation (AC1, AC2, AC3).

**Evidences:** TOOL-dGroundRules-39
- AC1 — `python check_policy.py --fixture census-window-edge` — printed the unplanted line answering `('source', 'tools')`, then `vendor/gov/govkit/registry.toml planted · refused tools/govkit/registry.toml, vendor/gov/govkit/registry.toml · RED as planted`, `guard-trace · 1 source read(s)` and `56 assertion(s) executed · 0 wrong`, no `WRONG`; exit 0.
- AC2 — `DEPTH3_LIVE`, then the AC1 command in the clone — the unplanted line printed `WRONG: refused a/b/c/govkit/registry.toml, tools/govkit/registry.toml` and the planted line `WRONG` naming all three; `2 wrong`, exit 1.
- AC3 — `TOPLEVEL`, then the AC1 command in the clone — the unplanted line printed `WRONG: refused registry.toml, tools/govkit/registry.toml` and the planted line `WRONG` naming all three; `2 wrong`, exit 1.
- AC4 — `python check_policy.py --repo <t>` over `TREE_AMBIG` under `%TEMP%/g39a` — `arm_cap_census` printed the one finding `tools/govkit/registry.toml, vendor/gov/govkit/registry.toml: 2 govkit/registry.toml candidates, so the tool root is not guessed and no row is graded`, beside the framework's `population: zero` line `run_arm` adds to an arm that graded nothing.
- AC5 — `CASE_PATHS`, `python -c "import check_policy as c; w, p = c.derive_window_edge_paths(); print(*w, p, sep='\n')"` — printed `tools/govkit/registry.toml`, `a/b/c/govkit/registry.toml`, `registry.toml` and `vendor/gov/govkit/registry.toml`: four distinct paths, three under a `govkit/` whose parent has one, three and two segments, one at the top level.
