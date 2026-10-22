# TOOL-dTrueNorth-29 deviation 31 — the flagged bar's self-test reds promoted to a unit

**Serves:** deviation TOOL-dTrueNorth-29

- **Departs from:** dTrueNorth [roster]
- **Hand-off:** design-to-spec
- **Before:** dTrueNorth's roster carries the twenty-five units its spec run, both spec audits, the closing diff review and the plain merge bar gave it, `TOOL-dTrueNorth-1` to `TOOL-dTrueNorth-20` and `TOOL-dTrueNorth-23` to `TOOL-dTrueNorth-27`, every one CLOSED when the flagged bar ran at `e583a7f42`.
- **After:** the roster also carries `TOOL-dTrueNorth-29`, which turns green the self-test arms the build's own units turned red in five legs, each at its cause, before the close.
- **Cause:** builder discovery
- **Reason:** The flagged bar GATE_FULL=1 GATE_SELFTESTS=1 at e583a7f42, run at VERIFYING after the plain bar went green, reds the spec-tokens, row-grammar, tier2-review, unattended-build and memory-hygiene self-tests on arms this build's diff broke. dTrueNorth is a whole run that closes without carry-forward (README rule 1), so the reds are built here; they are one unit because every remedy answers the same bar and none needs another landed first.
- **Evidence:** the bar's red legs, `memory/builds/dTrueNorth/build/2026-10-22-build-TOOL-dTrueNorth-29-flagged-bar.md`; the rescope add row for `TOOL-dTrueNorth-29` in `memory/builds/dTrueNorth/RUN.md`; the unit's spec, `memory/builds/dTrueNorth/spec/2026-10-22-spec-TOOL-dTrueNorth-29.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of dTrueNorth's whole run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dTrueNorth-29
- **Caused-by:** PLAY-dClosedLoop-2
