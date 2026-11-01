# TOOL-dIndexedDesign-40 deviation 401 — a spec audit promoted a unit for its findings

**Serves:** deviation TOOL-dIndexedDesign-40

- **Departs from:** dIndexedDesign [roster]
- **Hand-off:** design-to-spec
- **Before:** dIndexedDesign's roster carries sixteen units, `TOOL-dIndexedDesign-1` to `TOOL-dIndexedDesign-16`, one per clause of its row, beside `TOOL-dIndexedDesign-17`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dIndexedDesign-40`.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes report id 2 at HIGH (item H2) of memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-35-spec-audit-round1.md: the three cutoff keys ship blank in the passes of units 6, 8 and 4 that add them, so cutoff_keys_armed stays at its pin of 36 at every pass tip, repairing TOOL-dIndexedDesign-38. This is a spec run, so the unit is specced, audited as M4 and the owner's ruling of 2026-10-28 provide, and carried forward once, and the build run after it builds it.
- **Evidence:** the spec audit, `memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-35-spec-audit-round1.md`; the rescope add row for `TOOL-dIndexedDesign-40` in `memory/builds/dIndexedDesign/RUN.md`; the unit's spec, `memory/builds/dIndexedDesign/spec/2026-10-28-spec-TOOL-dIndexedDesign-40.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dIndexedDesign-40
- **Caused-by:** PLAY-dClosedLoop-2
