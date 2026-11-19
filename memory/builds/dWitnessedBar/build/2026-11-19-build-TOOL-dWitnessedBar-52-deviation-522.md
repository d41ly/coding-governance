# TOOL-dWitnessedBar-52 deviation 522 — the two conf plants share a fixture helper the inventory does not name

**Serves:** deviation TOOL-dWitnessedBar-52

- **Departs from:** `TOOL-dWitnessedBar-52@rev-6 [§4]`
- **Hand-off:** spec-to-code
- **Before:** §4 Inventory mints `read_root_confs` and the plant functions `run_plant_untracked_conf` and `run_plant_ignored_conf`, and no other function.
- **After:** `ratchet.py` also mints `write_scalar_fixture`, the one fixture both plants build: a `conf-scalar-pins` registration over a tracked root `.fix.conf` assigning `BAR_PIN`, its home holding that pin's row. The `ignored-conf` plant also runs the leg, which holds `BAR_PIN` and passes without naming `.x.conf`, and the `untracked-conf` plant's leg check refuses an `undeclared site` on `.fix.conf`, so its exit 1 is FOO_PIN's alone.
- **Cause:** builder discovery
- **Reason:** the charter's `[reuse]` rule extracts a kind's factory at its second instance, and the two plants build the same fixture, as the cutoff plants share `write_cutoff_fixture`. The tracked `.fix.conf` and its held row keep each plant's checks from passing over nothing: `ignored-conf`'s absence of `.x.conf` is read beside a conf the measure does read, and the leg's verdict turns on the planted conf only. The lexicon answered OK for `write_scalar_fixture` as a `py.function`.
- **Evidence:** `write_scalar_fixture`, `run_plant_untracked_conf` and `run_plant_ignored_conf` in `tools/memory-tree/ratchet.py`; their rows in `memory/map/generated/symbols.json`; the acceptance ledger's AC2 and AC3 lines.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** ask TOOL-dWitnessedBar-31
- **Caused-by:** PLAY-dClosedLoop-2
