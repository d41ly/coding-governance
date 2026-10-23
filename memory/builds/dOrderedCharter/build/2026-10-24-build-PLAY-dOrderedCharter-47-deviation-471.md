# PLAY-dOrderedCharter-47 deviation 471 — the round-1 spec audit promoted a unit for a high

**Serves:** deviation PLAY-dOrderedCharter-47

- **Departs from:** dOrderedCharter [roster]
- **Hand-off:** design-to-spec
- **Before:** dOrderedCharter's roster carries thirty-seven units, `PLAY-dOrderedCharter-1` to `PLAY-dOrderedCharter-37`, one per clause of its row, beside `PLAY-dOrderedCharter-38`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `PLAY-dOrderedCharter-47`, a record written on a branch that never held the positional check is graded print-only, by its adding commit's ancestry.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes the spec-audit round 1 finding 81 (HIGH, item H8). This is a spec run, so the unit is specced, audited once more under the owner's two-round cap (`memory/builds/dOrderedCharter/prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-owner-review-cap.md`) and carried forward once, and the build run after it builds it.
- **Evidence:** the round-1 spec audit, `memory/builds/dOrderedCharter/reviews/2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md`; the rescope add row for `PLAY-dOrderedCharter-47` in `memory/builds/dOrderedCharter/RUN.md`; the unit's spec, `memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-47.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit PLAY-dOrderedCharter-47
- **Caused-by:** PLAY-dClosedLoop-2
