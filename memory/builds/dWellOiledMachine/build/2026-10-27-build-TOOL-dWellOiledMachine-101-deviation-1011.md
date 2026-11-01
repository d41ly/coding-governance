# TOOL-dWellOiledMachine-101 deviation 1011 — the round-5 spec audit promoted a unit for a HIGH

**Serves:** deviation TOOL-dWellOiledMachine-101

- **Departs from:** dWellOiledMachine [roster]
- **Hand-off:** design-to-spec
- **Before:** dWellOiledMachine's roster carries the sixty-one units of its row and the thirty-five units its first four spec audits promoted, `TOOL-dWellOiledMachine-63` to `TOOL-dWellOiledMachine-97`, beside `TOOL-dWellOiledMachine-62`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dWellOiledMachine-101`, spec 95's ordering check is observed red: a fixture where an older spec-set commit names unit 90 and the amendment lands late.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes a HIGH: spec-audit round 5, over the round-4 promotions, finding 29 at HIGH, item H1 (shared with findings 1 11 19 12 20 30 13 21 31), repairing TOOL-dWellOiledMachine-95. This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-5 spec audit, `memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-95-spec-audit.md`; the rescope add row for `TOOL-dWellOiledMachine-101` in `memory/builds/dWellOiledMachine/RUN.md`; the unit's spec, `memory/builds/dWellOiledMachine/spec\2026-10-27-spec-TOOL-dWellOiledMachine-101.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dWellOiledMachine-101
- **Caused-by:** PLAY-dClosedLoop-2
