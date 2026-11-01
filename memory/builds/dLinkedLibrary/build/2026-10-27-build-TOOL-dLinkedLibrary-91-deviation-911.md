# TOOL-dLinkedLibrary-91 deviation 911 — the round-6 spec audit promoted a unit for the minors batch

**Serves:** deviation TOOL-dLinkedLibrary-91

- **Departs from:** dLinkedLibrary [roster]
- **Hand-off:** design-to-spec
- **Before:** dLinkedLibrary's roster carries twenty-five units, `TOOL-dLinkedLibrary-1` to `TOOL-dLinkedLibrary-25`, one per clause of its row, and the spec audit's promotions `TOOL-dLinkedLibrary-37` to `TOOL-dLinkedLibrary-86`, beside `TOOL-dLinkedLibrary-26`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dLinkedLibrary-91`, the spec audit of units 81 to 86: its medium and low findings, batched.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit batches the MEDIUM and LOW findings: spec-audit of units 81 to 86 round1 (reviews/2026-10-27-review-TOOL-dLinkedLibrary-81-spec-audit.md) minors batched in one unit (BUILD-METHOD M4): MEDIUM ids 2 3 32 5 6 29 8 13 34 14 23 15 18 21 22 24 28 35 36 (items M1-M15) and LOW ids 4 7 25 9 11 12 16 26 17 19 37 (items L1-L9); repairs none. This is a spec run, so the unit is specced, audited as M4 and the owner's ruling of 2026-10-27 provide, and carried forward once, and the build run after it builds it.
- **Evidence:** the round-6 spec audit, `memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-81-spec-audit.md`; the rescope add row for `TOOL-dLinkedLibrary-91` in `memory/builds/dLinkedLibrary/RUN.md`; the unit's spec, `memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-91.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dLinkedLibrary-91
- **Caused-by:** PLAY-dClosedLoop-2
