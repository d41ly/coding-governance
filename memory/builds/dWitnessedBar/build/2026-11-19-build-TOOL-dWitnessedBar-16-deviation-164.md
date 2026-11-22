# TOOL-dWitnessedBar-16 deviation 164 — the map self-test's unhomed-name arm names an unregistered `.txt`

**Serves:** deviation TOOL-dWitnessedBar-16

- **Departs from:** `TOOL-dWitnessedBar-16@rev-13 [S15]`
- **Hand-off:** spec-to-code
- **Before:** S15's `dead-path carriers` item says this unit's own carrier, the `memory/map/baseline.toml` argument of `cj.derive_baseline_additions` in `tools/codebase-map/selftest.py`, is repointed to `memory/map/baseline.txt`.
- **After:** the argument names `memory/map/unregistered.txt`, a name the arm's fixture registers no home for, so the arm still asserts what it was written to: the never-gains compare answers a name no `[[ledger]]` registration homes with `None` and the reason `no [[ledger]] registration homes`.
- **Cause:** builder discovery
- **Reason:** the arm's fixture registers `memory/map/baseline.txt` two lines above it, so that name read literally makes the compare grade the seeded baseline and return `{}`, and the arm's `nowhere is None` assertion fails, reddening `codebase-map kit selftest`, a leg section 7 names. The same arm's later lines already grade `baseline.txt` itself. The spelling chosen removes the dead `.toml` carrier S15 is about and keeps the case the arm covers.
- **Evidence:** `test_baseline_additions_from_git` in `tools/codebase-map/selftest.py`; the pass's probe of `tools/memory-tree/coverage_join.py#derive_baseline_additions` over gov's tree with `memory/map/unregistered.txt` returned `None` and `no [[ledger]] registration homes memory/map/unregistered.txt`.
- **Risk:** editorial
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** none
- **Caused-by:** PLAY-dClosedLoop-2
