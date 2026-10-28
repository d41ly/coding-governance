# TOOL-dIndexedDesign-38 deviation 383 — a spec audit promoted a unit for its findings

**Serves:** deviation TOOL-dIndexedDesign-38

- **Departs from:** dIndexedDesign [roster]
- **Hand-off:** design-to-spec
- **Before:** dIndexedDesign's roster carries sixteen units, `TOOL-dIndexedDesign-1` to `TOOL-dIndexedDesign-16`, one per clause of its row, beside `TOOL-dIndexedDesign-17`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dIndexedDesign-38`.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes the 42 MEDIUM and LOW findings of memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md batched in one unit, report ids 1 2 3 4 6 7 8 9 10 11 12 13 14 15 16 17 18 22 23 24 25 26 27 29 30 31 32 34 35 36 38 40 41 42 43 44 45 46 47 48 50 51. This is a spec run, so the unit is specced, audited as M4 and the owner's ruling of 2026-10-28 provide, and carried forward once, and the build run after it builds it.
- **Evidence:** the spec audit, `memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md`; the rescope add row for `TOOL-dIndexedDesign-38` in `memory/builds/dIndexedDesign/RUN.md`; the unit's spec, `memory/builds/dIndexedDesign/spec/2026-10-28-spec-TOOL-dIndexedDesign-38.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dIndexedDesign-38
- **Caused-by:** PLAY-dClosedLoop-2
