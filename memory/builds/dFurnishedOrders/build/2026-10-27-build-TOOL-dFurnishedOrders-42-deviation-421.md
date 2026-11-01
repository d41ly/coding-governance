# TOOL-dFurnishedOrders-42 deviation 421 — the round-3 spec audit promoted a unit for its findings

**Serves:** deviation TOOL-dFurnishedOrders-42

- **Departs from:** dFurnishedOrders [roster]
- **Hand-off:** design-to-spec
- **Before:** dFurnishedOrders' roster carries twenty units, `TOOL-dFurnishedOrders-1` to `TOOL-dFurnishedOrders-20`, one per clause of its row, beside `TOOL-dFurnishedOrders-21`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dFurnishedOrders-42`, from the round-3 spec audit: minors batched, the roles runlog unattended and kickoff half, a write set disjoint from TOOL-dFurnishedOrders-41 by M6: MEDIUM ids 1 2 23 3 22 4 5 6 25 7 11 12 13 21 26 30 35 (items M1-M7 M9-M11 M16-M18 M22) and LOW ids 16 20 (items L2 L3).
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the minors batched; this unit closes the findings named in After. This is a spec run, so the unit is specced, audited as M4 provides unless the owner's stop rule ended the chain first, and carried forward once, and the build run after it builds it.
- **Evidence:** the round-3 spec audit, `memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-31-spec-audit-round1.md`; the rescope add row for `TOOL-dFurnishedOrders-42` in `memory/builds/dFurnishedOrders/RUN.md`; the unit's spec, `memory/builds/dFurnishedOrders/spec/2026-10-27-spec-TOOL-dFurnishedOrders-42.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dFurnishedOrders-42
- **Caused-by:** PLAY-dClosedLoop-2
