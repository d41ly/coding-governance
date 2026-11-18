# TOOL-dDeclaredLoop-80 deviation 803 — the sweep's stale figures, read at this pass's base

**Serves:** deviation TOOL-dDeclaredLoop-80

- **Departs from:** `TOOL-dDeclaredLoop-80@rev-6` [§5]
- **Hand-off:** spec-to-code
- **Before:** §5's sweep, read at the tip `adbc3ecf5`, prices the budget leg's row at 476 PINNED seconds and the breakpoint leg's at 266 PINNED, counts one PINNED row of this spec in `memory/project/positional-refs.txt`, which a shrink takes out, and has its grep print one PINNED conf-name line in `budget.py`, four PINNED in `breakpoints.py` and one PINNED call of the pre-placement staging.
- **After:** at this pass's base the budget row read 485 PINNED seconds and the breakpoint row 317 PINNED, both as unit 76 re-priced them, and neither is re-priced, the case's added work being one scratch module parsed in milliseconds; the registry held no row of this spec, 0 PINNED, so no shrink runs; `derive_conf_reads` named 9 PINNED hits on 6 PINNED lines in `budget.py`, every one inside `tools/loop/budget.py#run_budget_plant`, and 8 PINNED hits on 6 PINNED lines in `breakpoints.py`, 7 PINNED inside `tools/loop/breakpoints.py#run_breakpoint_plant` and 1 PINNED in the staging S2 renames, which the staging's three PINNED calls reach, as the sweep's base column anticipates.
- **Cause:** builder discovery
- **Reason:** the spec was re-grounded before units 72, 64, 76 and 67 landed their plants, their re-prices and an earlier positional shrink; no design claim moved, and the base probe found no hit outside the boundary but the staging.
- **Evidence:** the base probe recorded in the acceptance ledger beside AC1; `grep -c 'spec-TOOL-dDeclaredLoop-80.md' memory/project/positional-refs.txt` printed 0 PINNED; the leg rows of `tools/run-gates/selftest-budgets.txt` at this pass's base.
- **Risk:** editorial
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** PLAY-dClosedLoop-2
