# TOOL-dWellOiledMachine-108 deviation 1081 — the round-5 spec audit promoted a unit for the batched MEDIUM and LOW findings

**Serves:** deviation TOOL-dWellOiledMachine-108

- **Departs from:** dWellOiledMachine [roster]
- **Hand-off:** design-to-spec
- **Before:** dWellOiledMachine's roster carries the sixty-one units of its row and the thirty-five units its first four spec audits promoted, `TOOL-dWellOiledMachine-63` to `TOOL-dWellOiledMachine-97`, beside `TOOL-dWellOiledMachine-62`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dWellOiledMachine-108`, the round-4 promotions audit's 22 medium and low findings, batched: the arm parse, liveness halves, scoped greps, stale figures and the ask's second row.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes the batched MEDIUM and LOW findings: spec-audit round 5, over the round-4 promotions, its 22 minor findings batched into one unit. This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-5 spec audit, `memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-95-spec-audit.md`; the rescope add row for `TOOL-dWellOiledMachine-108` in `memory/builds/dWellOiledMachine/RUN.md`; the unit's spec, `memory/builds/dWellOiledMachine/spec\2026-10-27-spec-TOOL-dWellOiledMachine-108.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dWellOiledMachine-108
- **Caused-by:** PLAY-dClosedLoop-2
