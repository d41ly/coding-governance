# TOOL-dGroundRules-45 deviation 33 — the round-6 spec audit promoted a unit

**Serves:** deviation TOOL-dGroundRules-45

- **Departs from:** dGroundRules [roster]
- **Hand-off:** design-to-spec
- **Before:** dGroundRules's roster carries the eleven units its README opened with, one per clause of its v2 row.
- **After:** the roster also carries `TOOL-dGroundRules-45`, the overlap probes read their pairs from the arm's table, so no criterion spells a pair a second time.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a spec audit's exit to a unit whose mechanism closes it; this unit closes one confirmed high of that round, and this spec run carries it forward once to the build run, which builds it (README rule 1).
- **Evidence:** the round-6 spec audit, `memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md`; the rescope add row for `TOOL-dGroundRules-45` in `memory/builds/dGroundRules/RUN.md`; the unit's spec, `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-45.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dGroundRules-45
- **Caused-by:** PLAY-dClosedLoop-2
