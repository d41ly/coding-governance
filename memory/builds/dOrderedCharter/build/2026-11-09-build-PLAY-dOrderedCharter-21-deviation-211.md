# PLAY-dOrderedCharter-21 deviation 211 — the step arm lives in the roles adopter suite, not a checker selftest

**Serves:** deviation PLAY-dOrderedCharter-21

- **Departs from:** `PLAY-dOrderedCharter-21@rev-4` [Gates]
- **Hand-off:** spec-to-code
- **Before:** the Gates section's first `New arm:` line puts the AC1 arm in `tools/roles/check_roles.py`, as its selftest's fixture kit omitting `step` on one workflow row.
- **After:** the arm is two `check_arm` lines in arm 10 of `tools/roles/adopt-roles.test.sh`, the suite the `roles adopter self-test` leg runs: over the fixture's copy of the shipped kit, the `build` row with its `step` line dropped must exit 1 with an R6 line naming `(build)` and `missing key 'step'`, then with `step = "buld"` an R6 line naming `(build)` and `step 'buld'`; the shipped table is restored after.
- **Cause:** builder discovery
- **Reason:** `check_roles.py` has no selftest and no leg runs one; the `roles catalogue` leg runs it over the tree alone. A selftest added there would be an arm no gate runs. Arm 10 already runs the shipped checker over a fixture copy of the shipped kit, which is AC1's own shape.
- **Evidence:** the awk and sed edits the arm makes were run over `tools/roles/workflows.toml`, each differing from it in the `build` row's `step` line alone; the checker over a scratch copy of gov's tree printed the two R6 lines the arm asserts, exit 1 each, and exit 0 once restored.
- **Risk:** none
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-21
