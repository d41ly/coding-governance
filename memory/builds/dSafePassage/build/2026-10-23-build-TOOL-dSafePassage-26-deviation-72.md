# TOOL-dSafePassage-26 deviation 72 — the round-1 spec audit promoted a unit

**Serves:** deviation TOOL-dSafePassage-26

- **Departs from:** dSafePassage [roster]
- **Hand-off:** design-to-spec
- **Before:** dSafePassage's roster carries the thirteen units its README opened with, one per clause of its v2 row.
- **After:** the roster also carries `TOOL-dSafePassage-26`: the round-1 spec audit's 54 minors: one base rule, one writer each, honest populations, declared exits, and the texts that name them.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a spec audit's exit to a unit whose mechanism closes it; this unit closes the round's MEDIUM and LOW findings as one batch, the one unit M2's one-mechanism rule admits. This is the spec run, so the unit is specced, audited, deferred and carried to the build run once (README rule 1).
- **Evidence:** the round-1 spec audit, `memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md`; the rescope add row for `TOOL-dSafePassage-26` in `memory/builds/dSafePassage/RUN.md`; the unit's spec, `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-26.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dSafePassage-26
- **Caused-by:** PLAY-dClosedLoop-2
