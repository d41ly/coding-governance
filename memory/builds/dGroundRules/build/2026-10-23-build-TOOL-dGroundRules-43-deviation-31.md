# TOOL-dGroundRules-43 deviation 31 — the round-5 spec audit promoted a unit

**Serves:** deviation TOOL-dGroundRules-43

- **Departs from:** dGroundRules [roster]
- **Hand-off:** design-to-spec
- **Before:** dGroundRules's roster carries the eleven units its README opened with, one per clause of its v2 row.
- **After:** the roster also carries `TOOL-dGroundRules-43`, the round-1 audit of units 33 and 34, its minors: fifteen findings closed in the code those units leave, one scope item each.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a spec audit's exit to a unit whose mechanism closes it; this unit closes fifteen confirmed mediums and lows, batched as one unit of that round, and this spec run carries it forward once to the build run, which builds it (README rule 1).
- **Evidence:** the round-5 spec audit, `memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-33-34-spec-audit-round1.md`; the rescope add row for `TOOL-dGroundRules-43` in `memory/builds/dGroundRules/RUN.md`; the unit's spec, `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-43.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dGroundRules-43
- **Caused-by:** PLAY-dClosedLoop-2
