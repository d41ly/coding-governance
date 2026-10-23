# TOOL-dSafePassage-16 deviation 62 — the round-1 spec audit promoted a unit

**Serves:** deviation TOOL-dSafePassage-16

- **Departs from:** dSafePassage [roster]
- **Hand-off:** design-to-spec
- **Before:** dSafePassage's roster carries the thirteen units its README opened with, one per clause of its v2 row.
- **After:** the roster also carries `TOOL-dSafePassage-16`: the step record's precondition, one predicate beside its one writer, and the schema-4 bootstrap it answers.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a spec audit's exit to a unit whose mechanism closes it; this unit closes finding id 50 at BLOCKER. This is the spec run, so the unit is specced, audited, deferred and carried to the build run once (README rule 1).
- **Evidence:** the round-1 spec audit, `memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md`; the rescope add row for `TOOL-dSafePassage-16` in `memory/builds/dSafePassage/RUN.md`; the unit's spec, `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-16.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dSafePassage-16
- **Caused-by:** PLAY-dClosedLoop-2
