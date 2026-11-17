# TOOL-dDeclaredLoop-87 deviation 873 — the sweep's stale figures

**Serves:** deviation TOOL-dDeclaredLoop-87

- **Departs from:** `TOOL-dDeclaredLoop-87@rev-6` [§5]
- **Hand-off:** spec-to-code
- **Before:** §5's sweep, read at the tip `759298f0f`, prices the `loop budget fixtures` row of `tools/run-gates/selftest-budgets.txt` at 482 PINNED seconds and counts 6 PINNED rows of this spec in `memory/project/positional-refs.txt`, for a shrink at the commit landing rev-6.
- **After:** at this pass's base the budget row read 498 PINNED seconds, and the registry held 0 PINNED rows of this spec, so no shrink runs; the row is not raised, since the widened plant ran in under 1 PINNED second by direct CLI.
- **Cause:** builder discovery
- **Reason:** the spec was re-grounded before units 82 and 86 landed their re-price and the shrink its own commit ran; no design claim moved.
- **Evidence:** the budget row and `grep -c 'spec-TOOL-dDeclaredLoop-87.md' memory/project/positional-refs.txt` at the base `2a71d7a70`; the direct-CLI timing recorded in the acceptance ledger beside AC1.
- **Risk:** editorial
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** PLAY-dClosedLoop-2
