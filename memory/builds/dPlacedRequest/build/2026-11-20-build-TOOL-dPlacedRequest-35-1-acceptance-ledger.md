# TOOL-dPlacedRequest-35 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-35

The unit was built from its spec at rev-4 on base `14f7d2e87`. The bounded walk TOOL-dPlacedRequest-34 (PINNED)
built in `tools/unattended/unattended.sh#read_claims` tested the renewing beat under an `ep[c] == te[i]`
guard ahead of the tenure stop, so it already read no age across an epoch change, as that unit's
`Decided:` line records. This pass puts the three tests of the walk's `step` in S1's stated order, the
tenure's end first, then the renewing beat with the guard dropped, then the threshold, and rewrites
the walk's comment to that order; S2's fallback is the existing `od[i]` stop, unchanged. Each
criterion below was observed by a probe: the driver's `--claims` over a scratch clone and bare origin
under the node's short temp path, `RUN_CLAIMS` on, the lease chains planted by `commit-tree` and each
sighting a line planted in the clone's change feed, `leases.expiry-hours` at its default of 24. The (PINNED)
same probe ran the two scratch copies the new arm stages, built by the arm's own substitutions: (PINNED)
`age-first.sh`, whose `awk` tests the threshold before the tenure stop, and `skip-tip.sh`, whose walk
skips each row's tip. The probe over the base driver read the same verdicts as over the pass's, so (DERIVED)
the order change moves no verdict the base read; the arms pin the order against a regression. No
gate, suite or bar ran in this pass.

**Evidences:** TOOL-dPlacedRequest-35
- The staged copies: `grep -cF` of the threshold test in `age-first.sh` printed 2 and of the skip in (DERIVED)
  `skip-tip.sh` 1 (DERIVED). (DERIVED)
- AC1 — an epoch-1 `renews: yes` commit sighted 90000 s ago under an epoch-2 take-over `renews: no` (PINNED)
  sighted 60 s ago: `--claims` printed the row `live`, aged 61 s (DERIVED); `age-first.sh` printed (DERIVED)
  `stale` (DERIVED).
- AC2 — an epoch-2 tip `renews: yes` sighted 60 s ago over two epoch-1 `renews: yes` commits sighted (PINNED)
  90000 s and 93600 s ago: `--claims` printed `live`, aged 61 s (DERIVED); `skip-tip.sh` printed (DERIVED)
  `stale` (DERIVED). `age-first.sh` printed `live` here, so AC2's red is the tip-skipping copy's alone.
- AC3 — an epoch-2 tenure of two `renews: no` commits over an epoch-1 renewal sighted 93600 s ago: (PINNED)
  its older commit sighted 90000 s ago printed `stale`, sighted 60 s ago `live` (DERIVED); (DERIVED)
  `age-first.sh` printed `stale` for both (DERIVED).
- The 90000 and 93600 s figures are PINNED, 25 h and 26 h past the 24 h default of (PINNED)
  `leases.expiry-hours`.

## Owed at the close

- The spec's `New arm:` line: `tools/unattended/unattended.test.sh`, the region-8 (PINNED)
  TOOL-dPlacedRequest-35 block, 8 executed assertions (8 `same`) (DERIVED), `FLOOR_ASSERTIONS` 3949 (DERIVED)
  to 3957 and `FLOOR_SHARD_8` 1168 to 1176; its red is `age-first.sh` for AC1 and AC3 and (DERIVED)
  `skip-tip.sh` for AC2. Waived for this build's landing by README rule 8. (PINNED)
- The DPR26 block's staged `cross.sh` still cuts the tenure stop's line, which this pass kept
  byte-identical, so its red stands; the close observes it with the rest of the suite.
- The legs the spec's Gates section names, run once by the main loop.
