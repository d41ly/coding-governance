# TOOL-dSafePassage-48 deviation 94 — the round-5 spec audit promoted a unit

**Serves:** deviation TOOL-dSafePassage-48

- **Departs from:** dSafePassage [roster]
- **Hand-off:** design-to-spec
- **Before:** dSafePassage's roster carries the thirteen units its README opened with and the thirty-two the first four spec audits promoted, `TOOL-dSafePassage-15` to `TOOL-dSafePassage-46`.
- **After:** the roster also carries `TOOL-dSafePassage-48`: the step contract refuses `sendemail.sendmailCmd` and every send-email executor key in its identity form.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a spec audit's exit to a unit whose mechanism closes it; this unit closes finding id 10 at HIGH. This is the spec run, so the unit is specced, audited, deferred and carried to the build run once (README rule 1).
- **Evidence:** the round-5 spec audit, over the round-4 promotions, `memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-43-44-45-46-spec-audit-round1.md`; the rescope add row for `TOOL-dSafePassage-48` in `memory/builds/dSafePassage/RUN.md`; the unit's spec, `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-48.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dSafePassage-48
- **Caused-by:** PLAY-dClosedLoop-2
