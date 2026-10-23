# TOOL-dSafePassage-46 deviation 92 — the round-4 spec audit promoted a unit

**Serves:** deviation TOOL-dSafePassage-46

- **Departs from:** dSafePassage [roster]
- **Hand-off:** design-to-spec
- **Before:** dSafePassage's roster carries the thirteen units its README opened with and the twenty-eight the first three spec audits promoted, `TOOL-dSafePassage-15` to `TOOL-dSafePassage-42`.
- **After:** the roster also carries `TOOL-dSafePassage-46`: the spec audit of units 36 to 42, its three minors off the step module: the drift pin raised in the pass that arms its key, a lander arm that finds its sibling kit, and the `ac-order` key documented.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a spec audit's exit to a unit whose mechanism closes it; this unit closes the round's MEDIUM and LOW findings as one batch, the one unit M2's one-mechanism rule admits. This is the spec run, so the unit is specced, audited, deferred and carried to the build run once (README rule 1).
- **Evidence:** the round-4 spec audit, over the round-3 promotions, `memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-36-37-38-39-40-41-42-spec-audit-round1.md`; the rescope add row for `TOOL-dSafePassage-46` in `memory/builds/dSafePassage/RUN.md`; the unit's spec, `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-46.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dSafePassage-46
- **Caused-by:** PLAY-dClosedLoop-2
