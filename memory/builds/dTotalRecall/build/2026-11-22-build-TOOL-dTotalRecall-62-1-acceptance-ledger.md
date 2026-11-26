# TOOL-dTotalRecall-62 — acceptance ledger, build pass 1

**Serves:** log TOOL-dTotalRecall-62
**Caused-by:** TOOL-dTotalRecall-62

No merge bar, no self-test suite and no gate leg ran in this pass. The spec writer applied §2 and §4 to the specs of
units 52 (rev-5 to rev-6) and 59 (rev-2 to rev-3) over base `9213ce523`; the main loop re-ran the greps below from
`memory/builds/dTotalRecall/spec/` on node d, 2026-11-23.

**Evidences:** TOOL-dTotalRecall-62
- AC1 — `absorbs = ` — `grep -n "absorbs = "` over spec 52 printed nothing, `grep -c "check_new_at_base"` over it printed 8 and `grep -c "amended by TOOL-dTotalRecall-62"` printed 1 for each of specs 52 and 59 (DERIVED 2026-11-23). §4's probe printed `True` with no `gained` key at the merge-base `8b8b1374c` (DERIVED 2026-11-23, the writer's run).
- AC2 — `legacy-records` — OWED to unit 52's pass tip: §4's probe and the retirement grep there.
- AC3 — `absorbs` — OWED to unit 59's pass tip: its AC3 fixture and the registry grep there.
