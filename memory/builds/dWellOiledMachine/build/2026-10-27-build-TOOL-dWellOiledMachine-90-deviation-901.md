# TOOL-dWellOiledMachine-90 deviation 901 — the round-2 spec audit promoted a unit for the batched MEDIUM and LOW findings

**Serves:** deviation TOOL-dWellOiledMachine-90

- **Departs from:** dWellOiledMachine [roster]
- **Hand-off:** design-to-spec
- **Before:** dWellOiledMachine's roster carries the sixty-one units of its row and the seventeen units the round-1 spec audit promoted, `TOOL-dWellOiledMachine-63` to `TOOL-dWellOiledMachine-79`, beside `TOOL-dWellOiledMachine-62`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dWellOiledMachine-90`, the promotions audit's 55 medium and low findings, batched: claims, fixtures, readers, registries and the sibling records that drifted.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes the batched MEDIUM and LOW findings: spec-audit round 2, over the round-1 promotions, its 55 minor findings batched into one unit. This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-2 spec audit, `memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-63-spec-audit.md`; the rescope add row for `TOOL-dWellOiledMachine-90` in `memory/builds/dWellOiledMachine/RUN.md`; the unit's spec, `memory/builds/dWellOiledMachine/spec\2026-10-27-spec-TOOL-dWellOiledMachine-90.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dWellOiledMachine-90
- **Caused-by:** PLAY-dClosedLoop-2
