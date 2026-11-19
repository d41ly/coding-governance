# TOOL-dWitnessedBar-15 deviation 154 — a widen whose seed fails leaves the armed home unchanged

**Serves:** deviation TOOL-dWitnessedBar-15

- **Departs from:** `TOOL-dWitnessedBar-15@rev-8 [S2]`
- **Hand-off:** spec-to-code
- **Before:** S2 says a seed that exits non-zero, times out or reports a dead probe leaves the home holding only the header and one `# unarmed` line, with no case named for `--widen` over a present, armed home.
- **After:** under `--widen`, over a present and armed home, a seed that fails writes nothing: the home keeps every row byte for byte, and `seed` prints `unarmed <population> <reason>; the armed home is unchanged` and exits 1. Over an absent or unarmed home a failed seed records the unarmed line as S2 says.
- **Cause:** builder discovery
- **Reason:** S2 read literally over an armed home would erase its rows, and §4's widen row says the verb never rewrites, removes or re-dates a row; the next run would then seed the home whole at a later sha, the laundering §1 forbids. The specific row was followed over the general clause, and the printed line says why nothing was written.
- **Evidence:** `seed_population` in `tools/lib/legacy_ledger.py`; the pass's scratch probe, a widen whose seed exited 1, printed that line and left the home's bytes equal (the acceptance ledger's AC4 line).
- **Risk:** stricter
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** ask TOOL-dWitnessedBar-31
- **Caused-by:** PLAY-dClosedLoop-2
