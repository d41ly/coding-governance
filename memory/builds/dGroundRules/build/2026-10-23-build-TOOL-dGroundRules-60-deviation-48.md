# TOOL-dGroundRules-60 deviation 48 — the closing diff review promoted a unit

**Serves:** deviation TOOL-dGroundRules-60

- **Departs from:** dGroundRules [roster]
- **Hand-off:** design-to-spec
- **Before:** dGroundRules's roster carries the eleven units its README opened with, one per clause of its v2 row.
- **After:** the roster also carries `TOOL-dGroundRules-60`, unit 52's overlap observations taken through the whole probe, with the Python column shown graded on its own.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M8 and M4 promote every confirmed finding at the closing review's exit to a unit whose mechanism closes it; this unit closes one confirmed high of that round, and this spec run carries it forward once to the build run, which builds it (README rule 1).
- **Evidence:** the closing diff review, `memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md`; the rescope add row for `TOOL-dGroundRules-60` in `memory/builds/dGroundRules/RUN.md`; the unit's spec, `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-60.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dGroundRules-60
- **Caused-by:** PLAY-dClosedLoop-2
