# TOOL-dWellOiledMachine-79 deviation 791 — the round-1 spec audit promoted a unit for the batched MEDIUM and LOW findings

**Serves:** deviation TOOL-dWellOiledMachine-79

- **Departs from:** dWellOiledMachine [roster]
- **Hand-off:** design-to-spec
- **Before:** dWellOiledMachine's roster carries sixty-one units, `TOOL-dWellOiledMachine-1` to `TOOL-dWellOiledMachine-61`, one per clause of its row, beside `TOOL-dWellOiledMachine-62`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dWellOiledMachine-79`, the spec audit's 49 medium and low findings, batched: capability rows, pack shapes, launch environment, registries, renders and the records that miscount.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes the batched MEDIUM and LOW findings: spec-audit round 1 of the dWellOiledMachine spec set, its 49 minor findings batched into one unit,. This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-1 spec audit, `memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md`; the rescope add row for `TOOL-dWellOiledMachine-79` in `memory/builds/dWellOiledMachine/RUN.md`; the unit's spec, `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-79.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dWellOiledMachine-79
- **Caused-by:** PLAY-dClosedLoop-2
