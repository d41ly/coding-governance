# PLAY-dOrderedCharter-1 deviation 15 — the catalogue's 39 rows take pending rows the spec does not name

**Serves:** deviation PLAY-dOrderedCharter-1

- **Departs from:** `PLAY-dOrderedCharter-1@rev-8` [Files touched]
- **Hand-off:** spec-to-code
- **Before:** the spec's Files touched estimate does not name `tools/playbook/core-pending.txt`, and unit 7's migration says that list is written once at its build pass and only shrinks after. The spec's edge to unit 7 says the catalogue's rows arm the meta-check's practice population, and no clause says what excuses them.
- **After:** the pass adds one `practice` row per catalogue row, 39 in all, each armed by dWitnessedBar, and the list's header says its `practice` rows landed with the catalogue.
- **Cause:** builder discovery
- **Reason:** `tools/playbook/core.py#run_meta_check` reds a practice no leg's `enforces` and no kind's `binds` names unless a pending row excuses it, and no leg enforces a practice yet, so the catalogue landing alone would red the `core meta-check` leg 39 times. The population was unarmed when unit 7 seeded the list, so its seed could not hold these rows, and unit 30's spec adds its three portable rows the same way. dWitnessedBar is the arming build because it owns the gate-leg kind: the `enforces` key on each of the legs pending there is what a practice's enforcement will be.
- **Evidence:** a probe read `core.read_pending` beside the catalogue and found the pending `practice` names equal to the 39 tags. The meta-check's own verdict is a leg, owed at the close.
- **Risk:** additive
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-1
