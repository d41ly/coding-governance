# TOOL-dFurnishedOrders-46 deviation 461 — the round-4 spec audit promoted a unit for its findings

**Serves:** deviation TOOL-dFurnishedOrders-46

- **Departs from:** dFurnishedOrders [roster]
- **Hand-off:** design-to-spec
- **Before:** dFurnishedOrders' roster carries twenty units, `TOOL-dFurnishedOrders-1` to `TOOL-dFurnishedOrders-20`, one per clause of its row, beside `TOOL-dFurnishedOrders-21`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dFurnishedOrders-46`, from the round-4 spec audit: minors batched, the roles run-gates unattended kickoff and gate-manifest half, a write set disjoint from TOOL-dFurnishedOrders-45 by M6: MEDIUM ids 2 3 8 10 15 16 20 22 29 (items M2 M3 M4 M6 M7 M8 M9 M10 M11) and LOW ids 4 11 12 17 19 24 28 30 33 (items L1 L3 L4 L6 L8 L9 L11 L12 L13).
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the minors batched; this unit closes the findings named in After. This is a spec run, so the unit is specced, audited as M4 provides unless the owner's stop rule ended the chain first, and carried forward once, and the build run after it builds it.
- **Evidence:** the round-4 spec audit, `memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-38-spec-audit-round1.md`; the rescope add row for `TOOL-dFurnishedOrders-46` in `memory/builds/dFurnishedOrders/RUN.md`; the unit's spec, `memory/builds/dFurnishedOrders/spec/2026-10-27-spec-TOOL-dFurnishedOrders-46.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dFurnishedOrders-46
- **Caused-by:** PLAY-dClosedLoop-2
