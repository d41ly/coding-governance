# TOOL-dPlacedRequest-17 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-17

The unit was built from its spec at rev-5 on base `a33105588`. Each criterion below was observed by a
probe of this unit's own code: the driver's `--claims` run in a scratch clone with a bare origin under
the node's short temp path, `RUN_CLAIMS` on, each lease planted on the origin by `commit-tree` with
explicit parents and each sighting a line appended to the clone's `gov-feed.log`. The red copies are a
`git show` of the base driver (its age pass reads `beat-utc`) and two cuts of this driver that the
suite's new block makes the same way: one whose age pass reads `beat-utc` for every sighting, one that
deletes the feed after the fetch. No gate, suite or bar ran in this pass; the arms the spec's §7
declares and their RED-first observations are owed at the close.

**Evidences:** TOOL-dPlacedRequest-17
- AC1 — a lease whose only commit carries `renews: yes` and a `beat-utc` 25 h before now, sighted by
  the read itself, printed `tOc live` with field 4 at 0 and 1 s (DERIVED, two runs); the base driver
  copy and the cut whose age pass reads `beat-utc` each printed it `stale`, aged 90003 and 90004 s (DERIVED)
  (DERIVED).
- AC2 — the same lease with its feed line planted 25 h ago printed `stale` at 90001 s (DERIVED); with
  `leases.expiry-hours = 48` committed to `.governance/policy.toml` and pushed, `policy.py get`
  answered 48 and `--claims` printed `live` (DERIVED).
- AC3 — a `renews: yes` commit sighted 25 h ago under a `renews: no` beat sighted 60 s ago printed (DERIVED)
  `stale` with field 4 at 61 s (DERIVED); the same chain with the beat `renews: yes` printed `live`
  (DERIVED).
- AC4 — a lease whose commit carries `renews: -`, sighted 1000 h ago, printed `live` at 3600001 s (DERIVED)
  (DERIVED).
- AC5 — `tools/unattended/unattended.sh#check_deadline_passed`, defined over the sourced
  `tools/lib/gov-feed.sh#read_first_seen`, returned 1 for an offer sighted 60 s ago whose (DERIVED)
  `offer-deadline` read a day past and bound 300, 0 for one sighted 400 s ago, 1 for a tombstone (DERIVED)
  sighted 6 days ago whose `beat-utc` read 8 days ago and bound 604800, 0 for one sighted 8 days ago,
  and 2 for an unsighted commit (DERIVED).
- AC6 — a lease and a legacy claim both printed `live` under the driver; under the cut deleting the
  feed after `add_feed_sightings` both printed age `-` and `unknown`, neither `stale` (DERIVED).
- AC7 — `grep -n 'first saw\|leases.expiry-hours\|leases.queued-claim-days\|leases.offer-seconds'`
  over `tools/unattended/STOPS.template.md` printed 9 lines (DERIVED), every one inside section 7
  "The lease": the three bound rows of its key table, the observer clock paragraph and the verdict
  table's first row; `memory/guides/UNATTENDED-STOPS.md` is its byte copy, `cmp` silent.
- AC8 — a tenure of three commits at epoch 1, all `renews: no`, printed `live` with its opener sighted
  82800 s ago and `stale` with it sighted 90000 s ago, the two later commits sighted 60 s ago (DERIVED);
  the same tenure parented on a two-commit legacy `refs/gov/runs/tL` chain carrying no `renews`, every
  legacy commit sighted 60 s ago under both refs, printed the same two verdicts (DERIVED). The 82800
  and 90000 s figures are PINNED, 23 h and 25 h either side of the 24 h default.
- AC9 — the inventory `git grep` of the criterion, over `tools/unattended/unattended.test.sh` with
  its five patterns (`beat-utc`, `renews: no`, `seed_claim`, `seed_lease`, `seed_su_claim`), printed
  75 lines at the base (DERIVED). Every arm they reach
  stages its claim through one of four seeds, and each seed now plants the sighting at the `beat-utc`
  it is handed through `tools/unattended/unattended.test.sh#add_claim_sighting`: `seed_claim` and
  `seed_lease` in the run-claim block, `seed_su_claim` in the settle block, `seed_lease_at` in the
  lease block. The nine stale seeds that aged a claim `GH_BOUND + 600` now age it `GH_EXPIRY + 600`,
  `GH_EXPIRY` 86400 PINNED as `leases.expiry-hours`' default. No expected verdict, `hit`, `miss` or
  `same` of those arms changed. The arms: the five-verdict AC2 arm, AC16, AC5, AC11, AC7, AC8, AC10,
  AC19, AC18, AC20 and the `--beat` arm of the run-claim block; GH10 AC2; GH11 AC2; the GH12 and DPR1
  claim-table arm's `foreign-stale` and every other row of `seed_claim_row` and `seed_lease_row`; GH20
  AC3 and AC6; GH23 AC2; GH31 AC2, AC3 and AC4; GH36 AC6; GH32 AC6; DPR1 AC2; and DPR1 AC4 and AC12,
  which read a driver-written `renews: no` and age nothing.
- The DEAD PROBE rule: a sighting planted as `2026-02-30T00:00:00Z` turned both rows of the read
  `unknown`, aged `-` (DERIVED), the staging the AC16 arm now reaches through `seed_claim`.
- `tools/unattended/unattended.sh#read_lease_bound` printed 86400 for 24 h, 5400 for 1.5 h, 0 for 0,
  604800 for 7 days and 300 for 300 s, and returned 1 with LB_VALUE empty for a refused read and for (DERIVED)
  a kind it does not name (DERIVED).
- The `gov_feed_sh` block cut from `tools/lib/gov-feed.sh`, `tools/unattended/unattended.sh` and
  `tools/run-gates/post-merge.sh` hashed equal (DERIVED).

## Owed at the close

- The first `New arm:` line of the spec's §7: `tools/unattended/unattended.test.sh`, the region-8
  TOOL-dPlacedRequest-17 block, 21 executed `same` assertions (DERIVED), `FLOOR_ASSERTIONS` 3531 to
  3552 and `FLOOR_SHARD_8` 765 to 786; its red is the cut copy `beat-utc.sh` for AC1 and `no-feed.sh`
  for AC6. Waived for this build's landing by README rule 8.
- The second `New arm:` line: the re-staged arms of AC9, each staged red by its `beat-utc`-only seed
  against this driver, then green on its planted feed line.
- The legs §7 names, run once by the main loop.
