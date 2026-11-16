# TOOL-dDeclaredLoop-31 deviation 313 — the budget fixtures row is re-priced over the two plants this unit adds

**Serves:** deviation TOOL-dDeclaredLoop-31

- **Departs from:** `TOOL-dDeclaredLoop-31@rev-4` [§5]
- **Hand-off:** spec-to-code
- **Before:** the spec's §5 sweep names `budget.py`'s `main` and `PLANTS` against the `loop budget fixtures` leg as "an added branch and added keys", and its files-touched list holds no `tools/run-gates/selftest-budgets.txt`, so the row's cost verdict stays at 369 seconds PINNED over a 246-second proxy PINNED and twenty plants PINNED.
- **After:** the `loop budget fixtures` row is re-priced from the plants at the base of this pass plus the two this unit adds, each read alone by direct CLI on node `d`: `ending` 3 seconds PINNED and `driver-exhausted` 68 seconds PINNED, a 317-second proxy PINNED over twenty-two plants PINNED, x1.5, written as 476 PINNED. The proxy sits above the leg's hang-bound `ceiling` of 300 seconds PINNED in `tools/gate-legs.json`, which this pass does not move: the leg runs every plant in one process, so its reading is below the proxy by the interpreter starts it saves, and the main loop's first reading of the leg alone decides whether that ceiling needs its evidence-backed raise.
- **Cause:** builder discovery
- **Reason:** the spec's AC2, AC3 and AC4 are observed through the `driver-exhausted` plant, which runs the unattended driver about a dozen times in a scratch repository, and its sweep priced the plant's keys but not its cost.
- **Evidence:** `tools/loop/budget.py#PLANTS` and the `loop budget fixtures` row of `tools/run-gates/selftest-budgets.txt` at the base of this pass and at its commit, and the two plants' `held` readings in this unit's acceptance ledger.
- **Risk:** editorial
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** TOOL-dDeclaredLoop-62
