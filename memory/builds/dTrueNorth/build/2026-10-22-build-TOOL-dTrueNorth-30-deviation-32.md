# TOOL-dTrueNorth-30 deviation 32 — the check 21 writer arm that has never been green, promoted to a unit

**Serves:** deviation TOOL-dTrueNorth-30

- **Departs from:** dTrueNorth [roster]
- **Hand-off:** design-to-spec
- **Before:** dTrueNorth's roster carries `TOOL-dTrueNorth-1` to `TOOL-dTrueNorth-20` and `TOOL-dTrueNorth-23` to `TOOL-dTrueNorth-29`, every one CLOSED at `92a0dcb96`.
- **After:** the roster also carries `TOOL-dTrueNorth-30`, whose writer-test conf in the hygiene suite declares `RECORD_UNDATED_ARTIFACTS="exempt"`, so check 21's second writer-test arm grades the record it is about.
- **Cause:** builder discovery
- **Reason:** At 92a0dcb96 the memory-hygiene self-test still reds the arm TOOL-dTrueNorth-14 added, check 21 failing on the undated result.json an earlier block plants in the shared fixture and leaves there. The arm's writer test never ran in a suite before the close, so the arm has never been green. dTrueNorth closes without carry-forward (README rule 1), so the red is built here, as one micro-unit.
- **Evidence:** the spec brief, `memory/builds/dTrueNorth/prompts/2026-10-22-prompt-TOOL-dTrueNorth-30-spec-brief.md`; the rescope add row for `TOOL-dTrueNorth-30` in `memory/builds/dTrueNorth/RUN.md`; the unit's spec, `memory/builds/dTrueNorth/spec/2026-10-22-spec-TOOL-dTrueNorth-30.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of dTrueNorth's whole run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dTrueNorth-30
- **Caused-by:** PLAY-dClosedLoop-2
