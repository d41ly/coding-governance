# TOOL-dTrueNorth-27 deviation 30 — the drift pin cutoff_keys_armed rises 34 -> 36, the two keys dTrueNorth arms by design

**Serves:** deviation TOOL-dTrueNorth-27

- **Departs from:** dTrueNorth [cutoff_keys_armed]
- **Hand-off:** design-to-spec
- **Before:** `tools/drift-audit/drift_signals.py` pins `cutoff_keys_armed` at 34, set at aRoutedQuill's close on 2026-10-10, and dTrueNorth arms `SPEC_CARRIES_CUTOFF` (TOOL-dTrueNorth-1) and `SPEC_AUDIT_PIN_CUTOFF` (TOOL-dTrueNorth-5) in `.memory-tree.conf`, a count of 36.
- **After:** the pin reads 36, its `34 -> 36` line naming both keys and decision TOOL-dTrueNorth-28, and no other key stops being armed.
- **Cause:** builder discovery
- **Reason:** The plain merge bar at f4b9849c9 reds `drift-audit records` on the count. Both keys put a clause of the build's design behind a cutoff, the binding lines and the audit pins, so no code change lowers the count without disarming a rule landed specs are graded by; the pin is the drift-audit kit's, a carrier no dTrueNorth clause names, so the fork was settled at rung 5 by the standing ruling.
- **Evidence:** `memory/builds/dTrueNorth/build/2026-10-22-build-TOOL-dTrueNorth-27-bar1.log`; TOOL-dTrueNorth-27 §8 F5; the decision row `TOOL-dTrueNorth-28`; the standing ruling ER:388 (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:914-922`), decision row `PLAY-dClosedLoop-6`
- **Risk:** loosening
- **Approver:** author, the run's main loop, under the chain's `author-recorded` value, citing ER:388 (`PLAY-dClosedLoop-6`)
- **Follow-through:** new unit TOOL-dTrueNorth-27
- **Caused-by:** PLAY-dClosedLoop-6
- **Surface:** cutoff_keys_armed in tools/drift-audit/drift_signals.py, its PINS row
