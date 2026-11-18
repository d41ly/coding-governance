# TOOL-dDeclaredLoop-62 deviation 624 — the budget row is re-priced over the plants unit 60 left, not the spec's seventeen

**Serves:** deviation TOOL-dDeclaredLoop-62

- **Departs from:** `TOOL-dDeclaredLoop-62@rev-4` [§4 §5]
- **Hand-off:** spec-to-code
- **Before:** the spec's §4 Evidence and §5 read `PLANTS` at seventeen keys PINNED and the `loop budget fixtures` row of `tools/run-gates/selftest-budgets.txt` at 339 seconds PINNED over a 226-second proxy PINNED, and price the new plant at about the `parallel-append` plant's 5 seconds PINNED.
- **After:** the row is re-priced from what `TOOL-dDeclaredLoop-60` left at the base of this pass, nineteen plants PINNED and 347 seconds PINNED over a 231-second proxy PINNED, plus `parallel-append-uneven` read by direct CLI at 15 seconds PINNED (node `d`, 2026-11-16, the higher of two readings, `parallel-append` reading 20 seconds PINNED in the same window): a 246-second proxy PINNED over twenty plants PINNED, x1.5, written as 369 PINNED. The proxy stays under the leg's hang-bound `ceiling` of 300 PINNED in `tools/gate-legs.json`, so §5's stop clause does not trigger.
- **Cause:** builder discovery
- **Reason:** rev-4 was grounded before `TOOL-dDeclaredLoop-60` added the `draws-survive-rotation` and `patch-archived` plants and re-priced the row; the spec names that whichever of 60 and this unit lands second re-reads the row's figures, so only the figures moved, not the design.
- **Evidence:** `tools/loop/budget.py#PLANTS` and the `loop budget fixtures` row at the base of this pass, and the same at its commit.
- **Risk:** editorial
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** TOOL-dDeclaredLoop-60
