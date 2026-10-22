# TOOL-dTrueNorth-23 deviation 22 — the closing diff review promoted a unit

**Serves:** deviation TOOL-dTrueNorth-23

- **Departs from:** dTrueNorth [roster]
- **Hand-off:** design-to-spec
- **Before:** dTrueNorth's roster carries twenty units, `TOOL-dTrueNorth-1` to `TOOL-dTrueNorth-20`, every one CLOSED when the closing diff review ran.
- **After:** the roster also carries `TOOL-dTrueNorth-23`, the kit's glob-pathspec readers strip the four pathspec-mode variables.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit to a unit whose mechanism closes it, a HIGH to a unit of its own; this unit closes one confirmed high of the closing diff review, item H1 (finding 2), and the run builds it rather than carrying it forward, since dTrueNorth is a whole run (README rule 1).
- **Evidence:** the closing diff review, `memory/builds/dTrueNorth/reviews/2026-10-22-review-TOOL-dTrueNorth-1-closing-diff-review-round1.md`; the rescope add row for `TOOL-dTrueNorth-23` in `memory/builds/dTrueNorth/RUN.md`; the unit's spec, `memory/builds/dTrueNorth/spec/2026-10-22-spec-TOOL-dTrueNorth-23.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dTrueNorth-23
- **Caused-by:** PLAY-dClosedLoop-2
