# TOOL-dWitnessedBar-25 deviation 972 — the tails take the run copy's modes, and the keep verb re-hashes each tail before it commits it

**Serves:** deviation TOOL-dWitnessedBar-25

- **Departs from:** `TOOL-dWitnessedBar-25@rev-5`
- **Hand-off:** spec-to-code
- **Before:** S3 has the runner write each failing leg's tail to `<common-dir>/gate-tails/<hash>` and names no mode for that directory or its files; S5 has the keep verb read each `tail.<n>` of the run and hand its tail to `write_record`.
- **After:** the runner creates `gate-tails/` mode 700 and each tail file mode 600, as the run record's own directory and output copies are; and `keep_tails.py` re-hashes each tail file with `git hash-object --stdin` before writing its record, refusing, exit 1 naming the file, a tail whose bytes no longer hash to its name, and refuses a `tail.<n>` whose hash is not 40 or 64 hex digits.
- **Cause:** builder discovery
- **Reason:** the tail is the redacted run copy with a longer life, so it takes that copy's restrictive modes; and the tails directory is node-local and writable by any process of the clone, so a file planted or edited under a hash would otherwise be committed to the remote as the named leg's output.
- **Evidence:** `tools/run-gates/run-gates.sh` (the tails block before the verdict), `tools/run-gates/keep_tails.py#run_keep`, `tools/run-gates/keep_tails.py#read_blob_hash`.
- **Risk:** stricter
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** ask TOOL-dWitnessedBar-31
- **Caused-by:** TOOL-dWitnessedBar-25
