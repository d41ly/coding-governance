# TOOL-dWellOiledMachine-92 deviation 921 — the round-3 spec audit promoted a unit for a HIGH

**Serves:** deviation TOOL-dWellOiledMachine-92

- **Departs from:** dWellOiledMachine [roster]
- **Hand-off:** design-to-spec
- **Before:** dWellOiledMachine's roster carries the sixty-one units of its row and the twenty-eight units its round-1 and round-2 spec audits promoted, `TOOL-dWellOiledMachine-63` to `TOOL-dWellOiledMachine-90`, beside `TOOL-dWellOiledMachine-62`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dWellOiledMachine-92`, the lifted node lock handed to TOOL-dPlacedRequest-24 and -11 by an ask row, and unit 83's claim on their contract withdrawn.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes a HIGH: spec-audit round 3, over the round-2 promotions, finding 22 at HIGH, item H2, repairing TOOL-dWellOiledMachine-83. This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-3 spec audit, `memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-80-spec-audit.md`; the rescope add row for `TOOL-dWellOiledMachine-92` in `memory/builds/dWellOiledMachine/RUN.md`; the unit's spec, `memory/builds/dWellOiledMachine/spec\2026-10-27-spec-TOOL-dWellOiledMachine-92.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dWellOiledMachine-92
- **Caused-by:** PLAY-dClosedLoop-2
