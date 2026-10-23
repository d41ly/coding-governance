# TOOL-dSafePassage-41 deviation 87 — the round-3 spec audit promoted a unit

**Serves:** deviation TOOL-dSafePassage-41

- **Departs from:** dSafePassage [roster]
- **Hand-off:** design-to-spec
- **Before:** dSafePassage's roster carries the thirteen units its README opened with and the twenty-one the round-1 and round-2 spec audits promoted, `TOOL-dSafePassage-15` to `TOOL-dSafePassage-35`.
- **After:** the roster also carries `TOOL-dSafePassage-41`: the `ac-order` join lands in the pass that arms it, so no commit carries the join without its cutoff key.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a spec audit's exit to a unit whose mechanism closes it; this unit closes finding id 22 at HIGH. This is the spec run, so the unit is specced, audited, deferred and carried to the build run once (README rule 1).
- **Evidence:** the round-3 spec audit, over the round-2 promotions, `memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-27-28-29-30-31-32-33-34-35-spec-audit-round1.md`; the rescope add row for `TOOL-dSafePassage-41` in `memory/builds/dSafePassage/RUN.md`; the unit's spec, `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-41.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dSafePassage-41
- **Caused-by:** PLAY-dClosedLoop-2
