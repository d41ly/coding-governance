# TOOL-dSafePassage-51 deviation 97 — the round-6 spec audit promoted a unit

**Serves:** deviation TOOL-dSafePassage-51

- **Departs from:** dSafePassage [roster]
- **Hand-off:** design-to-spec
- **Before:** dSafePassage's roster carries the thirteen units its README opened with and the thirty-six the first five spec audits promoted, `TOOL-dSafePassage-15` to `TOOL-dSafePassage-50`.
- **After:** the roster also carries `TOOL-dSafePassage-51`: the spec audit of units 47 to 50, the step module's 15 minors: the build order observed in commit order, the walk's checks in one sequence and no link followed, the guard's keys in the guard, one section probe, and the readings that cite them.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a spec audit's exit to a unit whose mechanism closes it; this unit closes the round's MEDIUM and LOW findings as one batch, the one unit M2's one-mechanism rule admits. This is the spec run, so the unit is specced, audited, deferred and carried to the build run once (README rule 1).
- **Evidence:** the round-6 spec audit, over the round-5 promotions, `memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-47-48-49-50-spec-audit-round1.md`; the rescope add row for `TOOL-dSafePassage-51` in `memory/builds/dSafePassage/RUN.md`; the unit's spec, `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-51.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dSafePassage-51
- **Caused-by:** PLAY-dClosedLoop-2
