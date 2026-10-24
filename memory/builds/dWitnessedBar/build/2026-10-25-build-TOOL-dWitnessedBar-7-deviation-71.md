# TOOL-dWitnessedBar-7 deviation 71 — a gate "changed" is a leg whose argv moved or an arm a spec declares, not every edit to a file the leg reads

**Serves:** deviation TOOL-dWitnessedBar-7

- **Departs from:** `cl-dClosedLoop-0345@3265ae12` [one per gate a build adds or changes]
- **Hand-off:** design-to-spec
- **Before:** `test.seen-red` reads one seen-red record "per gate a build adds or changes", which a reader can take to include every gate whose script or any file it reads changed in the build's range
- **After:** the owed set is every leg whose `tools/gate-legs.json` row is added past the build's base or whose `argv` moved, and every leg a `New arm:` line of the build's specs resolves to; a gate script edited with no `argv` change and no declared arm owes no record (TOOL-dWitnessedBar-7 §2 S4, §8 F3)
- **Cause:** design defect
- **Reason:** A seen-red record is a planted red re-run on its staged break (flow-steps `build.acceptance`), and only an arm someone planted has one. An edit to a shared script such as `tools/govkit/govkit.py`, which `govkit selfcheck` and `kit epoch` both run, has no plant, so owing a record for it would red `test.seen-red` on every build that touches the script with nothing a run could record. The owed set is the one the build method already owes arms for (M8 reads the `New arm:` lines).
- **Evidence:** TOOL-dWitnessedBar-7 §8 F3; `memory/guides/BUILD-METHOD.md:280-282`; `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:290`
- **Risk:** loosening
- **Approver:** spec writer, the gov-spec-writer role of the harness's spec stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** amends cl-dClosedLoop-0345@3265ae12
- **Caused-by:** TOOL-dWitnessedBar-7
