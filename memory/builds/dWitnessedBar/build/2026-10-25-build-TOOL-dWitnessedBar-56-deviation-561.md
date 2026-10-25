# TOOL-dWitnessedBar-56 deviation 561 — the round-2 spec audit promoted a unit for its batched minors

**Serves:** deviation TOOL-dWitnessedBar-56

- **Departs from:** dWitnessedBar [roster]
- **Hand-off:** design-to-spec
- **Before:** dWitnessedBar's roster carries thirty units, `TOOL-dWitnessedBar-1` to `TOOL-dWitnessedBar-30`, one per clause of its row, beside `TOOL-dWitnessedBar-31`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dWitnessedBar-56`, the round-2 spec audit's minors, batch A.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, the MEDIUM and LOW findings to one batch unit, or two over disjoint write sets; this unit closes the spec-audit round 2 minors batch A. This is a spec run, so the unit is specced, audited as M4 provides unless the owner's stop at round 14 left it unaudited, and carried forward once, and the build run after it builds it.
- **Evidence:** the round-2 spec audit, `memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md`; the rescope add row for `TOOL-dWitnessedBar-56` in `memory/builds/dWitnessedBar/RUN.md`; the unit's spec, `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-56.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dWitnessedBar-56
- **Caused-by:** PLAY-dClosedLoop-2
