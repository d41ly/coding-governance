# TOOL-dFurnishedOrders-49 deviation 491 — the round-5 spec audit promoted a unit for its findings

**Serves:** deviation TOOL-dFurnishedOrders-49

- **Departs from:** dFurnishedOrders [roster]
- **Hand-off:** design-to-spec
- **Before:** dFurnishedOrders' roster carries twenty units, `TOOL-dFurnishedOrders-1` to `TOOL-dFurnishedOrders-20`, one per clause of its row, beside `TOOL-dFurnishedOrders-21`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dFurnishedOrders-49`, from the round-5 spec audit: minors batched, the roles-suite budget, interrupt probe and write-set record half, a write set disjoint from TOOL-dFurnishedOrders-48 by M6: LOW ids 6 7 16 20 26 27 (items L3 L4 L7 L9).
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the minors batched; this unit closes the findings named in After. This is a spec run, so the unit is specced, audited as M4 provides unless the owner's stop rule ended the chain first, and carried forward once, and the build run after it builds it.
- **Evidence:** the round-5 spec audit, `memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-43-spec-audit-round1.md`; the rescope add row for `TOOL-dFurnishedOrders-49` in `memory/builds/dFurnishedOrders/RUN.md`; the unit's spec, `memory/builds/dFurnishedOrders/spec/2026-10-27-spec-TOOL-dFurnishedOrders-49.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dFurnishedOrders-49
- **Caused-by:** PLAY-dClosedLoop-2
