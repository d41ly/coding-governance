# TOOL-dDeclaredLoop-74 deviation 742 — the sweep's stale figures, read at this pass's base

**Serves:** deviation TOOL-dDeclaredLoop-74

- **Departs from:** `TOOL-dDeclaredLoop-74@rev-3` [§4]
- **Hand-off:** spec-to-code
- **Before:** the design's evidence and §5's sweep, read at the tip `adbc3ecf5`, count 21 PINNED plants in `PLANTS`, its grep printing 20 PINNED continuation rows, and price the `loop position fixtures` budget row at 411 PINNED seconds.
- **After:** at this pass's base `PLANTS` held 25 PINNED plants, the grep printing 24 PINNED continuation rows, after unit 67 added its three built plants, and the budget row read 425 PINNED seconds; `failed-fetch` makes 26 PINNED plants, still ahead of `plan-line` and `status-line`. The row is not re-priced in this pass: the plant ran alone by direct CLI in seconds, and the close's timed reading of the leg re-prices it where it passes.
- **Cause:** builder discovery
- **Reason:** the spec was re-grounded before unit 67 landed its plants and the row's re-price; no design claim moved, and every other sweep figure held at the base.
- **Evidence:** `grep -c '^          "' tools/loop/position.py` at this pass's base; the `loop position fixtures` row of `tools/run-gates/selftest-budgets.txt` at this pass's base.
- **Risk:** editorial
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** PLAY-dClosedLoop-2
