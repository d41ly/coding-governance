# TOOL-dSafePassage-49 deviation 95 — the round-5 spec audit promoted a unit

**Serves:** deviation TOOL-dSafePassage-49

- **Departs from:** dSafePassage [roster]
- **Hand-off:** design-to-spec
- **Before:** dSafePassage's roster carries the thirteen units its README opened with and the thirty-two the first four spec audits promoted, `TOOL-dSafePassage-15` to `TOOL-dSafePassage-46`.
- **After:** the roster also carries `TOOL-dSafePassage-49`: the spec audit of units 43 to 46, the step module's 20 minors: one step-row predicate, TOOL-4 after TOOL-43, a second walk refusal, identity forms held by the arm, declared exits, and the readings that cite them.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a spec audit's exit to a unit whose mechanism closes it; this unit closes the MEDIUM and LOW batch of the step module, finding ids 1 11 18 19 2 26 27 29 3. This is the spec run, so the unit is specced, audited, deferred and carried to the build run once (README rule 1).
- **Evidence:** the round-5 spec audit, over the round-4 promotions, `memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-43-44-45-46-spec-audit-round1.md`; the rescope add row for `TOOL-dSafePassage-49` in `memory/builds/dSafePassage/RUN.md`; the unit's spec, `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-49.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dSafePassage-49
- **Caused-by:** PLAY-dClosedLoop-2
