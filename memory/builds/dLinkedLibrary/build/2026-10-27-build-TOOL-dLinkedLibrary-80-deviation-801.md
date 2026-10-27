# TOOL-dLinkedLibrary-80 deviation 801 — the round-4 spec audit promoted a unit for the minors batch

**Serves:** deviation TOOL-dLinkedLibrary-80

- **Departs from:** dLinkedLibrary [roster]
- **Hand-off:** design-to-spec
- **Before:** dLinkedLibrary's roster carries twenty-five units, `TOOL-dLinkedLibrary-1` to `TOOL-dLinkedLibrary-25`, one per clause of its row, and the spec audit's promotions `TOOL-dLinkedLibrary-37` to `TOOL-dLinkedLibrary-74`, beside `TOOL-dLinkedLibrary-26`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dLinkedLibrary-80`, the spec audit of units 65 to 74: its medium and low findings, batched.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit batches the MEDIUM and LOW findings: spec-audit of units 65 to 74 round1 (reviews/2026-10-27-review-TOOL-dLinkedLibrary-65-spec-audit.md) minors batched in one unit (BUILD-METHOD M4): MEDIUM ids 1 11 27 2 12 41 10 26 28 40 22 21 43 42 4 15 37 20 14 38 13 23 24 39 (items M1-M18) and LOW ids 6 7 17 8 3 16 (items L1-L5); repairs none. This is a spec run, so the unit is specced, audited as M4 and the owner's ruling of 2026-10-27 provide, and carried forward once, and the build run after it builds it.
- **Evidence:** the round-4 spec audit, `memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-65-spec-audit.md`; the rescope add row for `TOOL-dLinkedLibrary-80` in `memory/builds/dLinkedLibrary/RUN.md`; the unit's spec, `memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-80.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dLinkedLibrary-80
- **Caused-by:** PLAY-dClosedLoop-2
