# TOOL-dWitnessedBar-14 deviation 143 — `seed laundering` runs a population's seed when a base row was removed

**Serves:** deviation TOOL-dWitnessedBar-14

- **Departs from:** `TOOL-dWitnessedBar-14@rev-10 [§5]`
- **Hand-off:** spec-to-code
- **Before:** §5's perf line says `both ways` runs only seeds no other leg runs and that the other legs read files and `git diff`.
- **After:** `ratchet (seed laundering)` also runs a population's seed, once, through `run_seed_argv`, and only where a base row is absent from the working rows; a population with no removed row runs no seed.
- **Cause:** builder discovery
- **Reason:** S9 and AC5 grade a row removed while its seed still measures the key, and a drained row whose seed no longer measures it as green. Only a seed run can say which, so the scope item was followed over the perf line, and the run is limited to the populations that removed a row.
- **Evidence:** `run_seed_laundering` and `read_seed_rows` in `tools/memory-tree/ratchet.py`; the `laundering` plant's second and third checks (the acceptance ledger's AC5 line).
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** ask TOOL-dWitnessedBar-31
- **Caused-by:** PLAY-dClosedLoop-2
