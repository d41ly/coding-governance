# TOOL-dWellOiledMachine-113 deviation 1131 — the round-6 spec audit promoted a unit for a HIGH

**Serves:** deviation TOOL-dWellOiledMachine-113

- **Departs from:** dWellOiledMachine [roster]
- **Hand-off:** design-to-spec
- **Before:** dWellOiledMachine's roster carries the sixty-one units of its row and the forty-six units its first five spec audits promoted, `TOOL-dWellOiledMachine-63` to `TOOL-dWellOiledMachine-108`, beside `TOOL-dWellOiledMachine-62`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dWellOiledMachine-113`, spec 103's AC1 counts the predicate loader in spec 96's §6 preamble alone, so the fixture's copy no longer reads red.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes a HIGH: spec-audit round 6, over the round-5 promotions, finding 20 at HIGH, item H3, repairing TOOL-dWellOiledMachine-103. This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-6 spec audit, `memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-98-spec-audit.md`; the rescope add row for `TOOL-dWellOiledMachine-113` in `memory/builds/dWellOiledMachine/RUN.md`; the unit's spec, `memory/builds/dWellOiledMachine/spec\2026-10-27-spec-TOOL-dWellOiledMachine-113.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dWellOiledMachine-113
- **Caused-by:** PLAY-dClosedLoop-2
