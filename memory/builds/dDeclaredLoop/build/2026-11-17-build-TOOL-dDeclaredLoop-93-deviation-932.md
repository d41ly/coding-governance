# TOOL-dDeclaredLoop-93 deviation 932 — the exit-claim probe counts one more claim and the leg's budget row reads one more second

**Serves:** deviation TOOL-dDeclaredLoop-93

- **Departs from:** `TOOL-dDeclaredLoop-93@rev-3` [§4, §5, §6]
- **Hand-off:** spec-to-code
- **Before:** the evidence and AC3's figure state that the exit-claim probe finds 13 PINNED claims with rev-3 in the folder, and the sweep's row for the `loop guard fixtures` leg cites the 140 PINNED second row of `tools/run-gates/selftest-budgets.txt`.
- **After:** run at the base `44be2307e`, the probe counts 14 PINNED claims and the same set `{1}`, the extra one in the spec of `TOOL-dDeclaredLoop-94`, whose fourth revision restates the plant's exit 1; the budget row reads 141 PINNED seconds, re-priced by unit 92's pass.
- **Cause:** builder discovery
- **Reason:** both figures moved under passes that landed after this spec's re-ground, and neither is a design claim: AC3 states the count is derived at observation time and owes at least five with the set `{1}`, and this pass writes neither the budget row nor the leg. No design claim moved.
- **Evidence:** the exit-claim probe run at the base over `memory/builds/dDeclaredLoop/spec/`, the `loop guard fixtures` row of `tools/run-gates/selftest-budgets.txt`, and this unit's acceptance ledger.
- **Risk:** editorial
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** PLAY-dClosedLoop-2
