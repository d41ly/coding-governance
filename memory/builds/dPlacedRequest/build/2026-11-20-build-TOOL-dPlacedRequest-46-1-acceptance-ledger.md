# TOOL-dPlacedRequest-46 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-46

The unit was built from its spec at rev-6 on base `4c3162038`. The walk's `step` in
`tools/unattended/unattended.sh#read_claims` gains one stop after the tenure's end and before the
renewing beat: a commit whose `renews` reads `-` stops the row there and stands for the beat, so the
verdict pass's existing never-stale read of that flag decides the row and no older commit of the
tenure is ever aged. The walk's comment and the function's header name the stop, and section 7 of
`tools/unattended/STOPS.template.md`, copied to `memory/guides/UNATTENDED-STOPS.md`, names it beside
the renewing beat. Each criterion below was observed by a probe that lifted the new block of
`tools/unattended/unattended.test.sh` and its helpers by name and ran them, never the suite: the
driver's `--claims` over a scratch clone and bare origin under the node's short temp path,
`RUN_CLAIMS` on, the lease chains planted by `commit-tree` and each sighting a line planted in the
clone's change feed, `leases.expiry-hours` at its default of 24. The unit-35-order copy is the (PINNED)
block's own scratch copy of the driver with the `-` stop's line cut. No gate, suite or bar ran in
this pass.

**Evidences:** TOOL-dPlacedRequest-46
- The staged copy: `grep -cF` of the stop's line printed 1 over the driver and 0 over the (DERIVED)
  unit-35-order copy (DERIVED).
- AC1 — a `renews: -` tip sighted 60 s ago over a `renews: no` commit of its epoch sighted (PINNED)
  3600000 s ago: `--claims` printed the row `live`; the unit-35-order copy printed `stale`. (PINNED)
- AC2 — a `renews: no` tip sighted 60 s ago over a `renews: -` commit sighted 120 s ago over a (PINNED)
  `renews: no` commit sighted 3600000 s ago: `live`; the copy printed `stale`. (PINNED)
- AC3 — four two-commit tenures, tips `renews: yes`, no `renews` key, `renews: -` and `renews: no`,
  each sighted 60 s ago over a `renews: no` commit sighted 3600000 s ago: `live live live stale`; (PINNED)
  the copy printed `live live stale stale`.
- AC4 — AC2's chain with the `-` commit unsighted: `unknown` with age `-`; the copy printed `stale`.
- AC5 — `grep -n 'renews' memory/guides/UNATTENDED-STOPS.md` names, in section 7's renewing-beat
  sentence, a `renews: -` commit as a stop of the walk tested before any age, and
  `cmp tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md` exited 0.
- The same probe over the base driver read AC1 `stale`, AC2 `stale`, AC4 `stale` aged 61 s and AC3's (DERIVED)
  `-` row `stale`, so the stop is what moves each verdict.

## Owed at the close

- The spec's `New arm:` line: `tools/unattended/unattended.test.sh`, the region-8 (PINNED)
  TOOL-dPlacedRequest-46 block, 8 executed assertions (8 `same`) (DERIVED), `FLOOR_ASSERTIONS` 3957 (DERIVED)
  to 3965 and `FLOOR_SHARD_8` 1176 to 1184; its red is the unit-35-order copy. Waived for this (DERIVED)
  build's landing by README rule 8.
- The DPR26 and DPR35 blocks' staged copies cut lines this pass kept byte-identical, so their reds
  stand; the close observes them with the rest of the suite.
- The legs the spec's Gates section names, run once by the main loop, the kit epoch leg among them.
