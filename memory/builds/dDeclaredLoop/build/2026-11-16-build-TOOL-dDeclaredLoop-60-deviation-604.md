# TOOL-dDeclaredLoop-60 deviation 604 — the budget row is re-priced over the plants unit 61 left, not the spec's sixteen

**Serves:** deviation TOOL-dDeclaredLoop-60

- **Departs from:** `TOOL-dDeclaredLoop-60@rev-4` [§5]
- **Hand-off:** spec-to-code
- **Before:** the spec's §5 risks read `PLANTS` at sixteen plants PINNED and the `loop budget fixtures` row of `tools/run-gates/selftest-budgets.txt` at 336 seconds PINNED, a 224-second proxy PINNED, and re-price that row by adding the two new plants' readings, x1.5.
- **After:** the row is re-priced from what `TOOL-dDeclaredLoop-61` left at the base of this pass, seventeen plants PINNED and 339 seconds PINNED over a 226-second proxy PINNED, plus `draws-survive-rotation` 2s PINNED and `patch-archived` 3s PINNED read by direct CLI: a 231-second proxy PINNED over nineteen plants, x1.5, written as 347 PINNED.
- **Cause:** builder discovery
- **Reason:** rev-4 was grounded before `TOOL-dDeclaredLoop-61` added the `draw-id-rows` plant and re-priced the row; the spec names that the last unit to land re-prices over every plant then present, so only the figures moved, not the design.
- **Evidence:** `tools/loop/budget.py#PLANTS` and the `loop budget fixtures` row at the base of this pass, and the same at its commit.
- **Risk:** editorial
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** TOOL-dDeclaredLoop-61
