# TOOL-dGroundRules-55 deviation 43 — the closing diff review promoted a unit

**Serves:** deviation TOOL-dGroundRules-55

- **Departs from:** dGroundRules [roster]
- **Hand-off:** design-to-spec
- **Before:** dGroundRules's roster carries the eleven units its README opened with, one per clause of its v2 row.
- **After:** the roster also carries `TOOL-dGroundRules-55`, the criterion bug class gains the side read: a criterion observes its scope item by running the check, never by reading what the check reads.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M8 and M4 promote every confirmed finding at the closing review's exit to a unit whose mechanism closes it; this unit closes one confirmed high of that round, and this spec run carries it forward once to the build run, which builds it (README rule 1).
- **Evidence:** the closing diff review, `memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md`; the rescope add row for `TOOL-dGroundRules-55` in `memory/builds/dGroundRules/RUN.md`; the unit's spec, `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-55.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dGroundRules-55
- **Caused-by:** PLAY-dClosedLoop-2
