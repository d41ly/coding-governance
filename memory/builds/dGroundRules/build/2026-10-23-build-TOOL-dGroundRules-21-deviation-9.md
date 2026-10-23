# TOOL-dGroundRules-21 deviation 9 — the round-1 spec audit promoted a unit

**Serves:** deviation TOOL-dGroundRules-21

- **Departs from:** dGroundRules [roster]
- **Hand-off:** design-to-spec
- **Before:** dGroundRules's roster carries the eleven units its README opened with, one per clause of its v2 row.
- **After:** the roster also carries `TOOL-dGroundRules-21`, the round-1 spec audit's minors: forty-one findings closed in the code units 1 to 10 leave, one scope item each.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a spec audit's exit to a unit whose mechanism closes it; this unit closes forty-one confirmed mediums and lows, batched as one unit of that round, and this spec run carries it forward once to the build run, which builds it (README rule 1).
- **Evidence:** the round-1 spec audit, `memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1.md`; the rescope add row for `TOOL-dGroundRules-21` in `memory/builds/dGroundRules/RUN.md`; the unit's spec, `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-21.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dGroundRules-21
- **Caused-by:** PLAY-dClosedLoop-2
