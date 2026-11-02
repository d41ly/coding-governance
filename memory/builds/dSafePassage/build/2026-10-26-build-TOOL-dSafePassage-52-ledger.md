**Serves:** journal TOOL-dSafePassage-52

# TOOL-dSafePassage-52 — acceptance ledger

The unit as built, at spec rev-3. Every scope item holds at HEAD with no product write. S1 to S3 are
readings TOOL-dSafePassage-50's arm already satisfies: the suite carries one `_mt_rc=` scan (now line
1028), the arm's first `check-arms.py` line (1402) sits below it and below the 28-32 block's
`skip — 28-32` line (1239), and above the final `[ "$fail" = 0 ]` line (1592). S4's render route is
not taken: TOOL-dSafePassage-50 AC2 found neither a duplicate nor a gap in the `SPEC_AC_ORDER_CUTOFF`
paragraph or the example row (each counts `1` today), so neither the template, its rendered copy nor
the example conf is written. S5 to S7 are readings of descriptions, which no code carries. This pass
writes only this ledger and the spec's status header.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on node d
(Windows) over this worktree at a2a7334b, by the probe the spec names.

Owed at the close: none of this unit's own — §7 adds no arm. The §7 legs `push-main self-test`,
`foreign-prefix parity (every self-test at three prefixes)`, `kit/dogfood doc parity`, `recall floor`,
`recall floor arms`, `memory-hygiene self-test` and `spec tokens (a spec's own names resolve)` run at
the close's bar.

**Evidences:** TOOL-dSafePassage-52
- AC1 — `ok-branch` — the guard probe with `HERE=tools` and the suite's own `^_mt_rc=` line eval'd printed `ok-branch`; `bash -c 'set -u; [ -n "$_mt_rc" ]; echo after'` printed `_mt_rc: unbound variable`, exited 127 and printed no `after`.
- AC2 — `check-arms.py` — `grep -c '^_mt_rc=' tools/push-main.test.sh` printed `1`; the four-pattern grep printed `_mt_rc=` at 1028, `skip — 28-32` at 1239, the first `check-arms.py` at 1402 and the final `[ "$fail" = 0 ]` at 1592, so 1028 < 1402, 1239 < 1402 and 1402 < 1592.
- AC3 — `no edit` — the pairing probe over `60d90cb7..HEAD` listed no commit touching `memory/TEMPLATE-SPEC.md` with a `Pass` trailer of `TOOL-dSafePassage-52`, and printed `no edit`: zero paired, the honest outcome where TOOL-dSafePassage-50 AC2 found no gap, not coverage.
