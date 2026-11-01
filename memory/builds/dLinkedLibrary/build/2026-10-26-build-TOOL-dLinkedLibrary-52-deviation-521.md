# TOOL-dLinkedLibrary-52 deviation 521 — the round-1 spec audit promoted a unit for the minors batch

**Serves:** deviation TOOL-dLinkedLibrary-52

- **Departs from:** dLinkedLibrary [roster]
- **Hand-off:** design-to-spec
- **Before:** dLinkedLibrary's roster carries twenty-five units, `TOOL-dLinkedLibrary-1` to `TOOL-dLinkedLibrary-25`, one per clause of its row, beside `TOOL-dLinkedLibrary-26`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dLinkedLibrary-52`, the code half of the round-1 audit's minors: 53 findings closed where the built code holds them.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit batches the MEDIUM and LOW findings: spec-audit round1 (reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md) minors batched, code half split by write set (BUILD-METHOD M4, M6): MEDIUM ids 5 24 6 7 9 40 63 11 14 15 21 60 23 25 28 31 32 33 34 37 39 44 74 45 46 47 48 52 53 55 62 61 68 69 70 71 72 73 75 78 79 80 (items R16-R20, R23, R24, R26-R33, R35, R36, R38-R45, R47-R55, R57-R59) and LOW ids 17 18 19 29 41 36 38 42 54 66 81 (items R61-R68, R70, R71). This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-1 spec audit, `memory/builds/dLinkedLibrary/reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md`; the rescope add row for `TOOL-dLinkedLibrary-52` in `memory/builds/dLinkedLibrary/RUN.md`; the unit's spec, `memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-52.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dLinkedLibrary-52
- **Caused-by:** PLAY-dClosedLoop-2
