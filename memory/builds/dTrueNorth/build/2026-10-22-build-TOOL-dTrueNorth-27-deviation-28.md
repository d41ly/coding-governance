# TOOL-dTrueNorth-27 deviation 28 — the plain merge bar's nine red legs promoted to a unit

**Serves:** deviation TOOL-dTrueNorth-27

- **Departs from:** dTrueNorth [roster]
- **Hand-off:** design-to-spec
- **Before:** dTrueNorth's roster carries the twenty-four units its spec run, both spec audits and the closing diff review gave it, `TOOL-dTrueNorth-1` to `TOOL-dTrueNorth-20` and `TOOL-dTrueNorth-23` to `TOOL-dTrueNorth-26`, every one CLOSED when the plain merge bar ran at `f4b9849c9`.
- **After:** the roster also carries `TOOL-dTrueNorth-27`, which clears the nine bar legs the build's own units turned red, each at its cause, before the close.
- **Cause:** builder discovery
- **Reason:** The plain merge bar at f4b9849c9, run after every unit closed, reds 9 of 68 legs, each caused by this build's diff. dTrueNorth is a whole run that closes without carry-forward (README rule 1), so the reds are built here; they are one unit because every remedy answers the bar and none needs another landed first.
- **Evidence:** the bar log, `memory/builds/dTrueNorth/build/2026-10-22-build-TOOL-dTrueNorth-27-bar1.log`; the rescope add row for `TOOL-dTrueNorth-27` in `memory/builds/dTrueNorth/RUN.md`; the unit's spec, `memory/builds/dTrueNorth/spec/2026-10-22-spec-TOOL-dTrueNorth-27.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of dTrueNorth's whole run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dTrueNorth-27
- **Caused-by:** PLAY-dClosedLoop-2
