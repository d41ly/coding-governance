# TOOL-dWellOiledMachine-124 deviation 1241 — the round-8 spec audit promoted a unit for a HIGH

**Serves:** deviation TOOL-dWellOiledMachine-124

- **Departs from:** dWellOiledMachine [roster]
- **Hand-off:** design-to-spec
- **Before:** dWellOiledMachine's roster carries the sixty-one units of its row and the fifty-nine units its first seven spec audits promoted, `TOOL-dWellOiledMachine-63` to `TOOL-dWellOiledMachine-121`, beside `TOOL-dWellOiledMachine-62`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dWellOiledMachine-124`, spec 121's AC4 is observed both ways: its walk count reads red over spec 115 before the cross-read and green after, and §4 records both readings.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes a HIGH: spec-audit round 8, over the round-7 promotions, finding 13 at HIGH, item H1 (shared with findings 1 9), repairing TOOL-dWellOiledMachine-121. This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-8 spec audit, `memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-116-spec-audit.md`; the rescope add row for `TOOL-dWellOiledMachine-124` in `memory/builds/dWellOiledMachine/RUN.md`; the unit's spec, `memory/builds/dWellOiledMachine/spec\2026-10-27-spec-TOOL-dWellOiledMachine-124.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dWellOiledMachine-124
- **Caused-by:** PLAY-dClosedLoop-2
