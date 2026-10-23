# TOOL-dSafePassage-55 deviation 101 — the round-7 spec audit promoted a unit

**Serves:** deviation TOOL-dSafePassage-55

- **Departs from:** dSafePassage [roster]
- **Hand-off:** design-to-spec
- **Before:** dSafePassage's roster carries the thirteen units its README opened with and the thirty-eight the first six spec audits promoted, `TOOL-dSafePassage-15` to `TOOL-dSafePassage-52`.
- **After:** the roster also carries `TOOL-dSafePassage-55`: the roster hand-out refuses on TOOL-49 AC2's whole order predicate, written once as one probe.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a spec audit's exit to a unit whose mechanism closes it; this unit closes the round's confirmed findings its rescope add row names. This is the spec run, so the unit is specced, deferred and carried to the build run once (README rule 1). It is carried with no spec audit of its own: the owner stopped the spec reviews after this round (`memory/builds/dSafePassage/prompts/2026-10-23-prompt-TOOL-dSafePassage-1-owner-audit-cap.md`).
- **Evidence:** the round-7 spec audit, over the round-6 promotions, `memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-51-52-spec-audit-round1.md`; the rescope add row for `TOOL-dSafePassage-55` in `memory/builds/dSafePassage/RUN.md`; the unit's spec, `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-55.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dSafePassage-55
- **Caused-by:** PLAY-dClosedLoop-2
