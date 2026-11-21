# TOOL-dPlacedRequest-26 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-26

The unit was built from its spec at rev-3 on base `cb82a2743`. The walk the spec designs already (PINNED)
stands in `tools/unattended/unattended.sh#read_claims`: TOOL-dPlacedRequest-17's spec rev-5 built (PINNED)
the age pass's walk from each row's tip while the `epoch` is the tip's (an absent `epoch` reads 0), (PINNED)
taking the newest commit whose `renews` reads `yes` or is absent, else the tenure's opening commit.
That is this spec's S1, S2 and S3 rule exactly, the stop and the fallback both inside the one walk (PINNED)
`awk`, so the driver was not changed: no code of the walk was rebuilt. This pass adds what remained:
the tenure arms in `tools/unattended/unattended.test.sh` and the stops guide's sentence. Each
criterion below was observed by a probe: the driver's `--claims` and `--lease take-over` verbs over a
scratch clone and bare origin under the node's short temp path, `RUN_CLAIMS` on, the conf keys the
suite's `mkconf` writes, and sightings planted in the clone's change feed. The same probe over a
scratch copy of the driver whose walk crosses the epoch change, the copy the new arm stages, read the
failures named below. No gate, suite or bar ran in this pass.

**Evidences:** TOOL-dPlacedRequest-26
- AC1 — an epoch-1 `renews: yes` commit sighted 90000 s ago under an epoch-2 take-over `renews: no` (PINNED)
  sighted 60 s ago: `--claims` printed the row `live`, aged 61 s (DERIVED); session `s3`'s (PINNED)
  `--lease take-over build tOc` exited 1 printing `lease refused — live-holder` (DERIVED). The (DERIVED)
  crossing copy printed the row `stale` (DERIVED).
- AC2 — the epoch-2 tenure's `renews: yes` commit sighted 90000 s ago under a `renews: no` beat (PINNED)
  sighted 60 s ago printed `stale`; that renewing commit sighted 60 s ago printed `live` (DERIVED).
- AC3 — an epoch-2 tenure of two `renews: no` commits over an epoch-1 renewal sighted 93600 s ago: (PINNED)
  its opener sighted 90000 s ago printed `stale`, sighted 60 s ago `live`, its feed line deleted (DERIVED)
  `unknown` aged `-` (DERIVED). The crossing copy printed `stale` for all three (DERIVED).
- AC4 — a legacy `refs/gov/runs/tFix` chain of two commits with no `epoch` key, its tip sighted 60 s (PINNED)
  ago and its parent 90000 s ago, printed `live` (DERIVED). (PINNED)
- AC5 — `grep -n 'tenure' tools/unattended/STOPS.template.md` printed, inside section 7, the one (DERIVED)
  line "A lease is aged within its holder's tenure: a take or a take-over raises the epoch and opens a
  new", whose sentence goes on to the S3 rule; the render `memory/guides/UNATTENDED-STOPS.md` compared
  equal to the template under `cmp` (DERIVED).
- The bug-class checklist over the pass commit selected criterion-asserts-what-its-own-command-cannot-show:
  the first wording wrapped "tenure" onto the line after "A lease is aged within its holder's", so the
  criterion's `grep` could not show the sentence; the closing commit rewraps it onto one line.
- The 90000 and 93600 s figures are PINNED, 25 h and 26 h past the 24 h default of (PINNED)
  `leases.expiry-hours`.

## Owed at the close

- The spec's `New arm:` line: `tools/unattended/unattended.test.sh`, the region-8 (PINNED)
  TOOL-dPlacedRequest-26 block, 12 executed assertions (11 `same`, 1 `hit`) (DERIVED),
  `FLOOR_ASSERTIONS` 3683 to 3695 and `FLOOR_SHARD_8` 914 to 926; its red is the scratch copy (DERIVED)
  `cross.sh`, whose walk crosses the epoch change, for AC1 and AC3. Waived for this build's landing (PINNED)
  by README rule 8. (PINNED)
- The legs the spec's Gates section names, run once by the main loop.
