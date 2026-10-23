# TOOL-dGroundRules-64 deviation 52 — the closing diff review surfaced a discovery the run adopted

**Serves:** deviation TOOL-dGroundRules-64

- **Departs from:** dGroundRules [roster]
- **Hand-off:** design-to-spec
- **Before:** dGroundRules's roster carries the eleven units its README opened with, one per clause of its v2 row.
- **After:** the roster also carries `TOOL-dGroundRules-64`, the respelled literals no other repair covers, restored whole and observed: units 5, 21, 33 and 34.
- **Cause:** review finding
- **Reason:** the closing review's items H1, H2 and M1 traced to the main loop's basename respelling of spec-tokens path hits, which stripped fixture literals from acceptance criteria; the run adopts the repair of every stripped literal those items do not cover as one unit (discoveries-adopted), and this spec run carries it forward once to the build run, which builds it (README rule 1).
- **Evidence:** the closing diff review, `memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md`; the rescope add row for `TOOL-dGroundRules-64` in `memory/builds/dGroundRules/RUN.md`; the unit's spec, `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-64.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dGroundRules-64
- **Caused-by:** PLAY-dClosedLoop-2
