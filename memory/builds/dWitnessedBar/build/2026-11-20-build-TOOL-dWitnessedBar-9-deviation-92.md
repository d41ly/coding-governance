# TOOL-dWitnessedBar-9 deviation 92 — run-gates moves to 1.54 for `level`, and the adapter rows carry the keys every leg carries

**Serves:** deviation TOOL-dWitnessedBar-9

- **Departs from:** `TOOL-dWitnessedBar-9@rev-4 [§4]`
- **Hand-off:** spec-to-code
- **Before:** S1 gives `level` its `LEG_KEY_FLOORS` row, and §4 Files touched lists no `tools/run-gates/run-gates.sh`. S4 names an adapter row's `level`, `pack` and tag, and S2 names `derive_product_rows(repo, value)`.
- **After:** `KIT_RUN_GATES_VERSION` moves 1.53 to 1.54 in `run-gates.sh`, its README marker with it, and the floor row reads `"level": (1, 54)`; the emitter gains no branch for the key, since no descriptor row carries it. Each adapter row also carries `name` (`<runner> <level> tests`), `purpose`, `subject` `repo` and `enforces` `practice.verify`. `derive_product_rows` takes optional `runners`, `rows` and `detected`, which the leg factory passes so its render adds adapter rows only and runs `detect` before any policy read. The run-gates map dossier claims the new leg and lists `product_tests.py`.
- **Cause:** builder discovery
- **Reason:** a floor row names the run-gates version whose canary first admits the key, and 1.53 already shipped `LEG_KEYS` without `level` on this branch, so the key needs a version of its own, as units 12, 19 and 10 each took one. A manifest row needs a name, the leg factory's `purpose` arm grades one on every row, and the canary compares a leg's `tests` with the dossiers' claims. Reading the manifest's own rows inside the render would carry a dropped declaration's row into the next render.
- **Evidence:** `tools/run-gates/run-gates.sh:37`, `tools/govkit/govkit.py#LEG_KEY_FLOORS`, `tools/run-gates/product_tests.py#derive_adapter_row`, `tools/run-gates/leg_factory.py#derive_runner_rows`, `memory/map/features/run-gates.md`.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** none
- **Caused-by:** PLAY-dClosedLoop-2
