**Serves:** journal TOOL-dSafePassage-50

# TOOL-dSafePassage-50 — acceptance ledger

The unit as built, at spec rev-2. TOOL-dSafePassage-46's pass (8c69f3e4) already built what this unit
repairs, reading its own §3 hands-off bullet to this unit: its derived-count arm in
`tools/push-main.test.sh` sits below the suite's one `_mt_rc=` scan, after the 28-32 block and before
the final line, and the `SPEC_AC_ORDER_CUTOFF` paragraph and example row were written once. So S1 and
S5 hold at HEAD with no product write, and §4 "The paragraph's owner" gives this unit no write when
AC2 finds neither a duplicate nor a gap. S2, S3 and S4 are readings of TOOL-dSafePassage-46's
citations, which no code carries. This pass writes only this ledger and the spec's status header.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on node d
(Windows) over this worktree at 33cc36e0.

Owed at the close: the RED-first observation of the `New arm:` line (arm 37's derived-count arm in
`tools/push-main.test.sh`, its failing case an arm copy moved above the `_mt_rc=` scan), and
`push-main self-test`, `foreign-prefix parity (every self-test at three prefixes)`, `kit/dogfood doc
parity`, `recall floor`, `recall floor arms`, `memory-hygiene self-test` and `spec tokens (a spec's own
names resolve)`.

**Evidences:** TOOL-dSafePassage-50
- AC1 — `grep -n -e '^_mt_rc=' -e 'check-arms.py' tools/push-main.test.sh` printed `1028:_mt_rc=...` first and the first `check-arms.py` line at `1402`, so the load sits below the scan. The scan run from `tools/` printed `_mt_rc=memory-tree`, and a scratch probe running count37's Python over `tools/push-main.sh` with `tools/memory-tree/check-arms.py` printed `d37 6 PREPARE_REFUSALS 6 ok`: the arm's `ok` branch, not its `skip —` branch, in gov's own tree.
- AC2 — `grep -c 'SPEC_AC_ORDER_CUTOFF'` printed `1` over `tools/memory-tree/SPEC-TEMPLATE.template.md` and `1` over `memory/TEMPLATE-SPEC.md`, and `grep -c '^SPEC_AC_ORDER_CUTOFF=""' tools/memory-tree/.memory-tree.conf.example` printed `1`.
