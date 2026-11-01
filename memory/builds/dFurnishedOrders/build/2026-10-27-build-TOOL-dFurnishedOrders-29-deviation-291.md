# TOOL-dFurnishedOrders-29 deviation 291 — the round-1 spec audit promoted a unit for its findings

**Serves:** deviation TOOL-dFurnishedOrders-29

- **Departs from:** dFurnishedOrders [roster]
- **Hand-off:** design-to-spec
- **Before:** dFurnishedOrders' roster carries twenty units, `TOOL-dFurnishedOrders-1` to `TOOL-dFurnishedOrders-20`, one per clause of its row, beside `TOOL-dFurnishedOrders-21`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dFurnishedOrders-29`, from the round-1 spec audit: minors batched, roles hooks and runlog half: MEDIUM ids 2 5 7 23 24 51 25 29 30 31 32 33 34 35 36 39 43 44 45 56 57 58 59 (items M1 M2 M4 M7-M18 M20-M22 M25-M28) and LOW ids 10 12 14 38 15 16 26 27 37 47 60 61 (items L1 L3 L5-L9 L11 L13-L15).
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the minors batched; this unit closes the findings named in After. This is a spec run, so the unit is specced, audited as M4 provides unless the owner's stop rule ended the chain first, and carried forward once, and the build run after it builds it.
- **Evidence:** the round-1 spec audit, `memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md`; the rescope add row for `TOOL-dFurnishedOrders-29` in `memory/builds/dFurnishedOrders/RUN.md`; the unit's spec, `memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-29.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dFurnishedOrders-29
- **Caused-by:** PLAY-dClosedLoop-2
