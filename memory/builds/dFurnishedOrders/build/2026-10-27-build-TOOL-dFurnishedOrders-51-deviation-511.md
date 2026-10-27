# TOOL-dFurnishedOrders-51 deviation 511 — the round-6 spec audit promoted a unit for its findings

**Serves:** deviation TOOL-dFurnishedOrders-51

- **Departs from:** dFurnishedOrders [roster]
- **Hand-off:** design-to-spec
- **Before:** dFurnishedOrders' roster carries twenty units, `TOOL-dFurnishedOrders-1` to `TOOL-dFurnishedOrders-20`, one per clause of its row, beside `TOOL-dFurnishedOrders-21`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dFurnishedOrders-51`, from the round-6 spec audit: finding id 24 at HIGH, report item H2: unit 49's interrupt probe never pins whose pid it checks, so a pid from another namespace reads as gone and the arm passes unchecked.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the minors batched; this unit closes the findings named in After. This is a spec run, so the unit is specced, audited as M4 provides unless the owner's stop rule ended the chain first, and carried forward once, and the build run after it builds it.
- **Evidence:** the round-6 spec audit, `memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-47-spec-audit-round1.md`; the rescope add row for `TOOL-dFurnishedOrders-51` in `memory/builds/dFurnishedOrders/RUN.md`; the unit's spec, `memory/builds/dFurnishedOrders/spec/2026-10-27-spec-TOOL-dFurnishedOrders-51.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dFurnishedOrders-51
- **Caused-by:** PLAY-dClosedLoop-2
