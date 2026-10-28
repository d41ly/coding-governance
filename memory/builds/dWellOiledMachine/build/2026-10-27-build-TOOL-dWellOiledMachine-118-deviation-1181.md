# TOOL-dWellOiledMachine-118 deviation 1181 — the round-7 spec audit promoted a unit for a HIGH

**Serves:** deviation TOOL-dWellOiledMachine-118

- **Departs from:** dWellOiledMachine [roster]
- **Hand-off:** design-to-spec
- **Before:** dWellOiledMachine's roster carries the sixty-one units of its row and the fifty-three units its first six spec audits promoted, `TOOL-dWellOiledMachine-63` to `TOOL-dWellOiledMachine-115`, beside `TOOL-dWellOiledMachine-62`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dWellOiledMachine-118`, reverting S6 turns spec 115's AC4 red: its red case names the revert and §4 records the reading that shows it.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes a HIGH: spec-audit round 7, over the round-6 promotions, finding 18 at HIGH, item H1 (shared with findings 1 9 21), repairing TOOL-dWellOiledMachine-115. This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-7 spec audit, `memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-109-spec-audit.md`; the rescope add row for `TOOL-dWellOiledMachine-118` in `memory/builds/dWellOiledMachine/RUN.md`; the unit's spec, `memory/builds/dWellOiledMachine/spec\2026-10-27-spec-TOOL-dWellOiledMachine-118.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dWellOiledMachine-118
- **Caused-by:** PLAY-dClosedLoop-2
