# TOOL-dFurnishedOrders-37 deviation 371 — the round-2 spec audit promoted a unit for its findings

**Serves:** deviation TOOL-dFurnishedOrders-37

- **Departs from:** dFurnishedOrders [roster]
- **Hand-off:** design-to-spec
- **Before:** dFurnishedOrders' roster carries twenty units, `TOOL-dFurnishedOrders-1` to `TOOL-dFurnishedOrders-20`, one per clause of its row, beside `TOOL-dFurnishedOrders-21`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dFurnishedOrders-37`, from the round-2 spec audit: minors batched in one unit: MEDIUM ids 4 5 14 6 11 34 12 36 18 13 23 20 21 41 22 40 26 27 31 32 28 33 35 38 39 37 43 (items M1-M22) and LOW ids 7 8 9 17 15 16 19 24 29 42 (items L1-L9).
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the minors batched; this unit closes the findings named in After. This is a spec run, so the unit is specced, audited as M4 provides unless the owner's stop rule ended the chain first, and carried forward once, and the build run after it builds it.
- **Evidence:** the round-2 spec audit, `memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-22-spec-audit-round1.md`; the rescope add row for `TOOL-dFurnishedOrders-37` in `memory/builds/dFurnishedOrders/RUN.md`; the unit's spec, `memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-37.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dFurnishedOrders-37
- **Caused-by:** PLAY-dClosedLoop-2
