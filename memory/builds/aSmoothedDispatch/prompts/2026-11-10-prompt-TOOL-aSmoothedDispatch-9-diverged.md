# Revision brief — aSmoothedDispatch: unit 9's AC1 cannot pass as written

**Serves:** research TOOL-aSmoothedDispatch-9

## The brief

### Goal
DIVERGENCE: spec section 5, AC1. AC1 says `sed -n "/^_rf_exempt='/,/'\$/p" tools/unattended/unattended.test.sh` prints one line, the `brief|check 49` row. No code that does what S1 says can make that true. After S1 the `_rf_exempt` string opens and closes on the same line. GNU sed never tests a range's end address against the line that opened the range, so it keeps printing until the next line that ends in a quote. I built S1 exactly as section 4 describes, and that command printed 24 lines, from the `_rf_exempt=` line through `_rf_lf=$'why\nhalt-code: ...'`. A three-line scratch fixture (`_rf_exempt='one row'` / `next line` / `last'`) printed all three lines, which confirms this is how sed works and not something about this file. AC1 would need another observation, for example `grep -c "^_rf_exempt='brief|check 49:.*hash'\$"` printing 1 together with the existing `grep -c '^dispatch|check 49'` printing 0. A sed form that stops on its start line, such as `sed -n "/^_rf_exempt='/{p;/'\$/q}"`, would also print one line. The code itself needs no change: the S1 and S2 edits as written passed every other check. I put tools/unattended/unattended.test.sh back as it was and committed nothing. The spec's INPROGRESS status edit was already in the tree before I started, and I did not touch it.

### Items
1. Shard 2, the hostile-value matrix (TOOL-aEvidencedLens-21 S3 block). `FAIL the exemption for --dispatch is stale: it ACCEPTED the one-line hostile form`. The `_rf_exempt` list names `dispatch` as refusing the one-line form because it "carries a space". Since unit 1, `--writes` splits that value into paths and accepts it. The matrix's phase-line and carriage-return checks for `--dispatch` stay green, so the acceptance is safe. Remove the `dispatch` row from `_rf_exempt`; the matrix then grades `--dispatch` like every other verb.
2. Shard 4, region four. The two carriage-return arms, unit 1's at `$'two\rwords/x.sh'` and unit 8's AC5 at `$'spells\r·\rseparator.sh'`, do not hit `--dispatch was given a --writes path containing whitespace` on node a. The log shows the dispatch declared instead. On this node's Cygwin bash, `case … in *[[:space:]]*)` matches a carriage return inconsistently between invocations, while a vertical tab and a form feed match every time (measured at the close). The refusal's own comment names all three as what the split leaves. Move both arms to a vertical tab, `$'\v'`, keeping their asserted texts, and say in a comment why the carriage return is not the probe on this node.

### Acceptance
At the close, the main loop re-runs shards 2 and 4. Neither prints any of the three FAIL lines, and each shard's FAIL lines equal the base run's. Item 1 reds if `dispatch` is put back on `_rf_exempt`. Item 2's arms red when the split's IFS is widened to include `\v`, which is the staged break for both.

### Gates
unattended kit self-test (shards 2 and 4), memory hygiene, spec tokens; then the full bar once.

### Non-goals
Any change to `tools/unattended/unattended.sh`. The inherited reds the base run shares: `--record-round` absent from the hostile matrix, the `GATE_REGEN_CHECK` scrub pair, the `write_bar_green` prologue check, and the five check-118 fixture refusals in shard 4.
