# TOOL-dWellOiledMachine-77 deviation 771 — the round-1 spec audit promoted a unit for a HIGH

**Serves:** deviation TOOL-dWellOiledMachine-77

- **Departs from:** dWellOiledMachine [roster]
- **Hand-off:** design-to-spec
- **Before:** dWellOiledMachine's roster carries sixty-one units, `TOOL-dWellOiledMachine-1` to `TOOL-dWellOiledMachine-61`, one per clause of its row, beside `TOOL-dWellOiledMachine-62`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dWellOiledMachine-77`, a session is bound as the owner only when no machine launcher started it.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes a HIGH: spec-audit round 1 of the dWellOiledMachine spec set, finding 63 at HIGH, item H14, repairing TOOL-dWellOiledMachine-12. This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-1 spec audit, `memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md`; the rescope add row for `TOOL-dWellOiledMachine-77` in `memory/builds/dWellOiledMachine/RUN.md`; the unit's spec, `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-77.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dWellOiledMachine-77
- **Caused-by:** PLAY-dClosedLoop-2
