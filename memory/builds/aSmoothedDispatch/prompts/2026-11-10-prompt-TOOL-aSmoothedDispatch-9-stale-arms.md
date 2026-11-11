# Promotion brief — aSmoothedDispatch: three driver-suite arms unit 1's split left red

**Serves:** research TOOL-aSmoothedDispatch-9

## The brief

### Goal
At the close, the driver suite `tools/unattended/unattended.test.sh` ran at the tip `55d65f5c8` and at the base `ae6735c1f`, shards 2, 3 and 4. Three FAIL lines appear at the tip and not at the base. All three follow from unit 1, which splits `--writes` values on space, tab and newline. Units 1 and 8 are CLOSED, so this unit corrects the suite. No product code changes: each refusal still behaves as its spec says.

### Items
1. Shard 2, the hostile-value matrix (TOOL-aEvidencedLens-21 S3 block). `FAIL the exemption for --dispatch is stale: it ACCEPTED the one-line hostile form`. The `_rf_exempt` list names `dispatch` as refusing the one-line form because it "carries a space". Since unit 1, `--writes` splits that value into paths and accepts it. The matrix's phase-line and carriage-return checks for `--dispatch` stay green, so the acceptance is safe. Remove the `dispatch` row from `_rf_exempt`; the matrix then grades `--dispatch` like every other verb.
2. Shard 4, region four. The two carriage-return arms, unit 1's at `$'two\rwords/x.sh'` and unit 8's AC5 at `$'spells\r·\rseparator.sh'`, do not hit `--dispatch was given a --writes path containing whitespace` on node a. The log shows the dispatch declared instead. On this node's Cygwin bash, `case … in *[[:space:]]*)` matches a carriage return inconsistently between invocations, while a vertical tab and a form feed match every time (measured at the close). The refusal's own comment names all three as what the split leaves. Move both arms to a vertical tab, `$'\v'`, keeping their asserted texts, and say in a comment why the carriage return is not the probe on this node.

### Acceptance
At the close, the main loop re-runs shards 2 and 4. Neither prints any of the three FAIL lines, and each shard's FAIL lines equal the base run's. Item 1 reds if `dispatch` is put back on `_rf_exempt`. Item 2's arms red when the split's IFS is widened to include `\v`, which is the staged break for both.

### Gates
unattended kit self-test (shards 2 and 4), memory hygiene, spec tokens; then the full bar once.

### Non-goals
Any change to `tools/unattended/unattended.sh`. The inherited reds the base run shares: `--record-round` absent from the hostile matrix, the `GATE_REGEN_CHECK` scrub pair, the `write_bar_green` prologue check, and the five check-118 fixture refusals in shard 4.

### Limitations
The builder runs no suite; the main loop observes the arms at the close. Raise no floor unless the assertion count moves.
