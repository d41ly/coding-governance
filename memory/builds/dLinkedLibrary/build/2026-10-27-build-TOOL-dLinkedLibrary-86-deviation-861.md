# TOOL-dLinkedLibrary-86 deviation 861 — the round-5 spec audit promoted a unit for the minors batch

**Serves:** deviation TOOL-dLinkedLibrary-86

- **Departs from:** dLinkedLibrary [roster]
- **Hand-off:** design-to-spec
- **Before:** dLinkedLibrary's roster carries twenty-five units, `TOOL-dLinkedLibrary-1` to `TOOL-dLinkedLibrary-25`, one per clause of its row, and the spec audit's promotions `TOOL-dLinkedLibrary-37` to `TOOL-dLinkedLibrary-80`, beside `TOOL-dLinkedLibrary-26`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dLinkedLibrary-86`, the spec audit of units 75 to 80: its medium and low findings, batched.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit batches the MEDIUM and LOW findings: spec-audit of units 75 to 80 round1 (reviews/2026-10-27-review-TOOL-dLinkedLibrary-75-spec-audit.md) minors batched in one unit (BUILD-METHOD M4): MEDIUM ids 1 2 16 22 40 3 4 5 12 14 15 39 17 23 25 26 27 28 29 37 38 41 (items M1-M18) and LOW ids 6 18 7 8 19 42 10 11 21 24 (items L1-L7); repairs none. This is a spec run, so the unit is specced, audited as M4 and the owner's ruling of 2026-10-27 provide, and carried forward once, and the build run after it builds it.
- **Evidence:** the round-5 spec audit, `memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-75-spec-audit.md`; the rescope add row for `TOOL-dLinkedLibrary-86` in `memory/builds/dLinkedLibrary/RUN.md`; the unit's spec, `memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-86.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dLinkedLibrary-86
- **Caused-by:** PLAY-dClosedLoop-2
