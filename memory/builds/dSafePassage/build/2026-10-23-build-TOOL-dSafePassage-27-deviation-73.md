# TOOL-dSafePassage-27 deviation 73 — the round-2 spec audit promoted a unit

**Serves:** deviation TOOL-dSafePassage-27

- **Departs from:** dSafePassage [roster]
- **Hand-off:** design-to-spec
- **Before:** dSafePassage's roster carries the thirteen units its README opened with and the twelve the round-1 spec audit promoted, `TOOL-dSafePassage-15` to `TOOL-dSafePassage-26`.
- **After:** the roster also carries `TOOL-dSafePassage-27`: the prepared landing's one untracked snapshot, taken before the walk, serves the regeneration's refusal too.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a spec audit's exit to a unit whose mechanism closes it; this unit closes finding id 1 at HIGH. This is the spec run, so the unit is specced, audited, deferred and carried to the build run once (README rule 1).
- **Evidence:** the round-2 spec audit, over the round-1 promotions, `memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-15-16-17-18-19-20-21-22-23-24-25-26-spec-audit-round1.md`; the rescope add row for `TOOL-dSafePassage-27` in `memory/builds/dSafePassage/RUN.md`; the unit's spec, `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-27.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dSafePassage-27
- **Caused-by:** PLAY-dClosedLoop-2
