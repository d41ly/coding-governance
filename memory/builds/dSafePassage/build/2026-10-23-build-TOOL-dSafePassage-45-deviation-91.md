# TOOL-dSafePassage-45 deviation 91 — the round-4 spec audit promoted a unit

**Serves:** deviation TOOL-dSafePassage-45

- **Departs from:** dSafePassage [roster]
- **Hand-off:** design-to-spec
- **Before:** dSafePassage's roster carries the thirteen units its README opened with and the twenty-eight the first three spec audits promoted, `TOOL-dSafePassage-15` to `TOOL-dSafePassage-42`.
- **After:** the roster also carries `TOOL-dSafePassage-45`: the spec audit of units 36 to 42, the step contract's 21 minors: a derived pair count, a credential class over keys and values, a walk by git's own test, declared exits, and the readings that cite them.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a spec audit's exit to a unit whose mechanism closes it; this unit closes the MEDIUM and LOW batch of the step contract, finding ids 1 7 14 24 9 22 10 19 20 21 3 18 23. This is the spec run, so the unit is specced, audited, deferred and carried to the build run once (README rule 1).
- **Evidence:** the round-4 spec audit, over the round-3 promotions, `memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-36-37-38-39-40-41-42-spec-audit-round1.md`; the rescope add row for `TOOL-dSafePassage-45` in `memory/builds/dSafePassage/RUN.md`; the unit's spec, `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-45.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dSafePassage-45
- **Caused-by:** PLAY-dClosedLoop-2
