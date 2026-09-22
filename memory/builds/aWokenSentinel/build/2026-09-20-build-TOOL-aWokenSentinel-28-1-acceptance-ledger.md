# TOOL-aWokenSentinel-28 — acceptance ledger

**Serves:** journal TOOL-aWokenSentinel-28

Every leg-shaped half below reads `observed at --close`: this pass ran no gate, no leg and no
suite. The pass verified with the direct checks the spec's section 7 names for it: the copied
checker run whole over a scratch kit seeded by the kit gate suite's own PREAMBLE (lines 1 to 278
of `tools/unattended/check-unattended.test.sh`, sourced under `bash -c` with `$0` set to the suite
so `HERE` derives to the kit, `TMPDIR` pointed at `%TEMP%/lc28`, the arm block sourced after it
from the session scratchpad's `lc28-arm.sh`, with the kit gate's own suite committed into the
scratch kit beside the driver suite copy so the population holds the file the by-name exclusion is
for), `run` instrumented to keep each checker output and exit status; three further runs of the same
fixture over a MUTATED checker copy, so the arm itself was seen RED once per branch it reads; and
the greps of AC2 and AC3 over the tip and unit 23's tip. Those stand in for the
`unattended kit gate`, `harness arms (fail branches armed or pinned)`, `memory hygiene`,
`spec tokens` and `install-prefix` legs, which run once at the close. One spec fold was owed and
taken as rev-2 BEFORE the code: section 4's sketch appended the staged line to the copy's end with
`>>` and deleted it with `sed -i '$d'`, which is inside no function body and disagreed with S1 and
AC1; the design is now spec 23's own splice and a `mutate` delete, with `run` and
`$KIT_REL/unattended.test.sh` as the names spec 23's arm has.

**Evidences:** TOOL-aWokenSentinel-28
- AC1 — five checker runs over the scratch kit at the tip, each ~15 s on node `a`: with `  _x=$(echo "$_o" | wc -l)` spliced after `check_status_one_line() {` (the copy's line 88, `_lc_at`), rc 1 and one FAILED line, `UNATTENDED check 33 FAILED — a shell file in this kit counts a captured variable's lines by adding a newline first … hits: unattended.test.sh:88:  _x=$(echo "$_o" | wc -l)`; with that line deleted by `mutate`, rc 0, zero FAILED lines and the copy back at the shipped 6383 lines; with `  _x=$(wc -l <<< "$_o")` spliced instead, rc 1 and the same sentence ending `hits: unattended.test.sh:88:  _x=$(wc -l <<< "$_o")`; deleted, rc 0 and zero FAILED lines; with `  read -r _y <<< "$_o"` spliced, rc 0 and zero FAILED lines with the line still present (6384 lines). The block alone printed `n=12 st=0`. The arm's OWN red readings, over a checker copy mutated by sed and asserted changed by hash: `|echo)` dropped from `_lc_re` → the echo staged line passes the checker (rc 0) and exactly the echo reading's two `hit` lines FAIL (`FAIL missing: counts a captured variable's lines by adding a newline first`, `FAIL missing: hits: unattended.test.sh:88:`), st 1; the `<<<` alternation dropped → the here-string staged line passes (rc 0) and exactly its two `hit` lines FAIL, st 1; the `<<<` branch loosened to `|<<<` → every run reds first on the driver's own `unattended.sh:3133:  done <<<"$dirty"`, the control's `miss` FAILS (`FAIL unexpected: …adding a newline first`) beside the two GREEN readings' misses and the two line assertions, st 1. OBSERVED
- AC2 — `grep -cE "(printf '%s\\\\n'|echo) \"\\\$[A-Za-z_][A-Za-z0-9_]*\"[[:space:]]*\|[[:space:]]*wc -l|wc -l[[:space:]]*<<<" tools/unattended/check-unattended.test.sh` printed `0` at the tip (and `0` at 07d595d2, the base); `grep -c 'adding a newline first' tools/unattended/check-unattended.test.sh` printed `6` at the tip (unit 23's full-signature `hit`, this unit's two `hit` and three `miss` lines) and `1` at the base. The two assembled values were also evaluated alone under `bash -c` and printed `  _x=$(echo "$_o" | wc -l)` and `  _x=$(wc -l <<< "$_o")`. OBSERVED
- AC3 — `sed -n 's/^FLOOR_ASSERTIONS=//p' tools/unattended/check-unattended.test.sh` printed `434` at the tip and `422` at fb988384, unit 23's pass tip (and `422` at 07d595d2, so no sibling moved it between); `FLOOR_SHARD_2` printed `343` and `331`; both moved by the 12 the block executed alone (five `mutate`, four `hit`, three `miss`), and `FLOOR_SHARD_1` is untouched. The whole-suite reading of the raised floors is `observed at --close`. OBSERVED
- checkers — `bash -n` exited 0 on the suite and it carries no CR byte. The `unattended kit gate`, `harness arms`, `memory hygiene`, `spec tokens` and `install-prefix` legs are `observed at --close`.

## What this ledger does not evidence

No kit gate, hygiene leg, spec-token leg, install-prefix leg or `*.test.sh` suite ran inside this
pass; every one is `--close`'s and each row above says so. The `harness arms` verdict on the
whole population is the close's: this unit adds readings under check 33's branch, which unit 23's
full-signature arm armed, and moves no branch's verdict. The three arm-RED readings were taken
over a checker COPY in the scratch kit mutated by sed, never the shipped checker. The
`unattended gate selftest` budget row absorbs the five added checker runs (~75 s on node `a` in
this fixture) without a re-measure. No identifier under `tools/` was minted; `_lc_cmd`, `_lc_line`
and `_lc_at` are shell locals of the suite arm. The spec's section 1 pricing of 199 s per checker
run is the ledger's contended bar-leg figure; inside this fixture a run took ~15 s.
