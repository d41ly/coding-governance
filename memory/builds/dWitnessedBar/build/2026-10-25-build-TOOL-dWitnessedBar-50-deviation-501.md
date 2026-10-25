# TOOL-dWitnessedBar-50 deviation 501 — the round-1 spec audit promoted a unit for a HIGH finding

**Serves:** deviation TOOL-dWitnessedBar-50

- **Departs from:** dWitnessedBar [roster]
- **Hand-off:** design-to-spec
- **Before:** dWitnessedBar's roster carries thirty units, `TOOL-dWitnessedBar-1` to `TOOL-dWitnessedBar-30`, one per clause of its row, beside `TOOL-dWitnessedBar-31`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dWitnessedBar-50`, the round-1 spec audit's finding id 50 at HIGH, report item H11.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a HIGH to a unit whose mechanism closes it; this unit closes spec-audit round 1 finding id 50. This is a spec run, so the unit is specced, audited as M4 provides unless the owner's stop at round 14 left it unaudited, and carried forward once, and the build run after it builds it.
- **Evidence:** the round-1 spec audit, `memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md`; the rescope add row for `TOOL-dWitnessedBar-50` in `memory/builds/dWitnessedBar/RUN.md`; the unit's spec, `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-50.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dWitnessedBar-50
- **Caused-by:** PLAY-dClosedLoop-2
