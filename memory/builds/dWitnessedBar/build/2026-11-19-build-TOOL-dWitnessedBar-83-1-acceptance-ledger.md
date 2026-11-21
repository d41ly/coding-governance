# TOOL-dWitnessedBar-83 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-83

No merge bar, no self-test suite and no gate leg ran in this pass, and no code file changed. The pass
wrote records only: the clause `TOOL-dWitnessedBar-83` S3 appends to the AC15 line of
`2026-11-19-build-TOOL-dWitnessedBar-73-1-acceptance-ledger`, and this ledger. On node d, 2026-11-21,
the builder ran the owner pipeline and the two greps the criteria spell, over the tree at the pass's
base `8d1aa5123`, as probes of the spec's claims; each observation the criteria place at the close
is OWED to the main loop there, after every unit this run builds is terminal.

**Evidences:** TOOL-dWitnessedBar-83
- AC1 — `grep -B1 '^FLOOR_ASSERTIONS=' tools/run-gates/run-gates.gov.test.sh | head -1` — at base the owner pipeline printed 28 specs ending at `TOOL-dWitnessedBar-90` (DERIVED from the builder's probe), and the line above the constant is the `TOOL-aShardedFloor-2` comment (`tools/run-gates/run-gates.gov.test.sh#FLOOR_ASSERTIONS`), which names no owner, since unit 90 is not yet built. The pipeline's list and the comment naming its last line's id are OWED to the main loop at the close.
- AC2 — `PASS (<n> assertions)` — OWED to the main loop at the close: the arm's executed count over the built tree, the value `grep '^FLOOR_ASSERTIONS='` prints then, and the owner the owner pipeline derives then, all three written on this line.
- AC3 — `grep -n 'AC15' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-73*acceptance-ledger*` — the grep prints one line, which now names this unit's equality criterion, by its label, as the close's equality beside the `FLOOR_ASSERTIONS=72` it records (DERIVED from the builder's probe). The `PASS` count from a scratch clone at `71f212ad1`, written on that same line, is OWED to the main loop at the close.
