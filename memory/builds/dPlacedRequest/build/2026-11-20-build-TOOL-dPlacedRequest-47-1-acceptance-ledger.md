# TOOL-dPlacedRequest-47 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-47

The unit was built from its spec at rev-7 on base `0bca98088`. It changes no driver code: the guard
it pins, the walk's `step` in `tools/unattended/unattended.sh#read_claims` testing the threshold only
for a ref and commit present in `seen`, was already in the tree. The region-eight block of
`tools/unattended/unattended.test.sh` after the TOOL-dPlacedRequest-46 block writes `unguarded.sh`
under `$oc_copy`, a scratch copy of the driver whose threshold line is the TOOL-dPlacedRequest-35
block's `so_age` string with the `in seen` clause dropped, plants the mixed tenure and the two
unsighted observations, and reads each with `read_clock_row`. Each criterion below was observed by a
probe that sourced the suite's lease-fixture helpers, lifted the new block verbatim from the suite
by its first line and the region's closing cleanup, and ran it over the HEAD driver, never the
suite: a scratch clone and bare origin under the node's short temp path, `RUN_CLAIMS` on,
`leases.expiry-hours` at its default. No gate, suite or bar ran in this pass.

**Evidences:** TOOL-dPlacedRequest-47
- The staged copy: `grep -cF` printed `1 1`, the guarded line once in the driver and the (DERIVED)
  unguarded line once in the copy.
- AC1 — one epoch-1 tenure of three `renews: no` commits, the opener sighted (PINNED)
  90000 s ago, the middle with no feed line, the tip sighted 60 s ago on the ref's newest line: (PINNED)
  `read_clock_row` printed `stale` on the driver, and `unknown -` on the unguarded copy, its red.
- AC2 — a `renews: no` tip whose only feed line, the ref's newest, carries `-`, over a
  `renews: no` opener sighted 90000 s ago: `unknown -` on the driver. (PINNED)
- AC3 — a `renews: yes` beat whose only feed line carries `-`, under a `renews: no` tip sighted
  60 s ago on the ref's newest line: `unknown -` on the driver. (PINNED)
- The probe's own count: every assertion of the block passed and none failed. (DERIVED)

## Owed at the close

- The spec's `New arm:` line: `tools/unattended/unattended.test.sh`, the region-8 (PINNED)
  TOOL-dPlacedRequest-47 block, its 5 assertions (5 `same`, no loop) (DERIVED),
  `FLOOR_ASSERTIONS` 3965 to 3970 and `FLOOR_SHARD_8` 1184 to 1189. Its red is the (DERIVED)
  unguarded copy reading AC1's mixed tenure; its RED-first observation, the driver's own guard
  cut, is the close's. Waived for this build's landing by README rule 8.
- The legs the spec's Gates section names, run once by the main loop.
