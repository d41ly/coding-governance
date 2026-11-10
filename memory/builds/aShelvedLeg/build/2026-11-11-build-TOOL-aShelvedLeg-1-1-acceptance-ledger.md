# TOOL-aShelvedLeg-1 — acceptance ledger

**Serves:** journal TOOL-aShelvedLeg-1

Observed at the build tip 48f3377a7 on node a, 2026-11-11, by the spec's own §6 commands run verbatim from the worktree root. BEFORE is base `b904a0f9`, as each criterion's red clause reads it. The unit adds no suite arm. The round-1 blocker's gate, the leg `every held leg is budgeted, every budget row resolves`, was observed RED with the `no-trailer:` declaration removed (exit 1, naming the row) and GREEN restored (exit 0, 3 declared no-trailer).

**Evidences:** TOOL-aShelvedLeg-1
- AC1 — `held_halves.py` — the partition announces `75 leg(s)` and the grep for the leg prints 1; base reads 74 and 0.
- AC2 — `kit kit kit declarations` — the three-file probe prints exactly that; base prints `repo repo repo declarations`.
- AC3 — `tools/run-gates/selftest-budgets.txt` — the leg's row reads budget 4721 with an empty argv field.
- AC4 — `git diff b904a0f9 -- tools/run-gates/run-gates.sh .githooks/pre-push` — prints 0 lines; `run_one "kit gate"` occurs once, at line 552, argv `bash "$HERE/check-unattended.sh"`.
- AC5 — `tools/unattended/kit.toml` — the hit is the comment opening at line 256, directly above the leg's row ending `name = "unattended kit gate"` at 267; it names TOOL-aBoundedCeiling-10, the `--checks` route and the self-test variable.
- AC6 — `grep -cE 'stay merge-bar legs|ALSO merge-bar legs|stay on the merge bar'` — prints 0; the README's `check-unattended.sh` line reads "the kit gate, HELD off the bar: --checks or GATE_SELFTESTS=1".
