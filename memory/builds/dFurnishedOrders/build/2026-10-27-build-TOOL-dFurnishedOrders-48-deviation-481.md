# TOOL-dFurnishedOrders-48 deviation 481 — the round-5 spec audit promoted a unit for its findings

**Serves:** deviation TOOL-dFurnishedOrders-48

- **Departs from:** dFurnishedOrders [roster]
- **Hand-off:** design-to-spec
- **Before:** dFurnishedOrders' roster carries twenty units, `TOOL-dFurnishedOrders-1` to `TOOL-dFurnishedOrders-20`, one per clause of its row, beside `TOOL-dFurnishedOrders-21`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dFurnishedOrders-48`, from the round-5 spec audit: minors batched, the govkit step, parity-arm, guard and ratchet half: MEDIUM ids 1 2 3 4 9 11 12 13 14 15 17 19 22 23 24 25 30 31 32 33 35 (items M1-M13) and LOW ids 5 18 21 28 34 (items L1 L2 L5 L6 L8).
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the minors batched; this unit closes the findings named in After. This is a spec run, so the unit is specced, audited as M4 provides unless the owner's stop rule ended the chain first, and carried forward once, and the build run after it builds it.
- **Evidence:** the round-5 spec audit, `memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-43-spec-audit-round1.md`; the rescope add row for `TOOL-dFurnishedOrders-48` in `memory/builds/dFurnishedOrders/RUN.md`; the unit's spec, `memory/builds/dFurnishedOrders/spec/2026-10-27-spec-TOOL-dFurnishedOrders-48.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dFurnishedOrders-48
- **Caused-by:** PLAY-dClosedLoop-2
