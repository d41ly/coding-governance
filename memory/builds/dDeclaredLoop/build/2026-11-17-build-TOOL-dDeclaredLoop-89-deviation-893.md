# TOOL-dDeclaredLoop-89 deviation 893 — the sweep's stale figures

**Serves:** deviation TOOL-dDeclaredLoop-89

- **Departs from:** `TOOL-dDeclaredLoop-89@rev-5` [§5]
- **Hand-off:** spec-to-code
- **Before:** §5's sweep, read at the tip `64e2a7e97`, prices the `loop budget fixtures` row of `tools/run-gates/selftest-budgets.txt` at 482 PINNED seconds, counts 5 PINNED usage rows of `budget.py` in `tools/govkit/usage.toml` and 3 PINNED rows of this spec in `memory/project/positional-refs.txt`, for a shrink at the commit landing rev-5, and §4 quotes the loop README's reach paragraph as ending on five reaches.
- **After:** at this pass's base the budget row read 498 PINNED seconds, the usage file held 6 PINNED rows of `budget.py`, the registry held 0 PINNED rows of this spec, so no shrink runs, and the reach paragraph counted six, a count this pass keeps by naming `load_tree_lib` in place of `derive_conf_reads`; the budget row is not raised, since the widened plant ran in under 1 PINNED second by direct CLI.
- **Cause:** builder discovery
- **Reason:** the spec was re-grounded before units 76 to 87 landed their re-prices, their usage rows, the shrink and the reach that unit 86 added; no design claim moved.
- **Evidence:** the budget row, the usage rows and `grep -c 'spec-TOOL-dDeclaredLoop-89.md' memory/project/positional-refs.txt` at the base `7d4a42868`; the reach paragraph of `tools/loop/README.md` there; the direct-CLI timing recorded in the acceptance ledger beside AC1.
- **Risk:** editorial
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** PLAY-dClosedLoop-2
