# TOOL-dPlacedRequest-50 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-50

The unit was built from its spec at rev-6 on base `d8feb5fdd`. Its F2 ruling makes S1 and S2
observations of spec 47's built arm and text, so this pass builds nothing: no driver line, no arm
row and no function moved, and spec 47, CLOSED, is untouched. No gate, suite or bar ran in this pass.

THE TENURE PROBE, the reading the lines below cite as "the probe": a scratch script that lifts
`mkconf`, `add_claim_sighting`, `derive_claim_ago`, `write_lease_fixture`, `add_lease_commit`,
`remove_clock_refs` and `read_clock_row` out of `tools/unattended/unattended.test.sh` by their opening
lines, and its `so_age` and `ug_age` strings, never the suite. It writes the arm's unguarded copy by
the same substitution, plants the `DPR47 AC1` tenure as that block plants it, over a scratch clone and
bare origin under the node's short temp path with `RUN_CLAIMS` on and `leases.expiry-hours` at its
default, and reads the `tOc` row over the HEAD driver, then over the copy, in the block's order.

**Evidences:** TOOL-dPlacedRequest-50
- The staged copy: `grep -cF` of the guarded line in the driver and the unguarded line in the copy (DERIVED)
- printed `1 1`. (DERIVED)
- The feed lines the probe planted for the middle commit, so it is absent from `seen`: (DERIVED)
- 0 (DERIVED)
- AC1 — the tenure `read_clock_row` reads, its tip and opener planted by `derive_claim_ago` at the PINNED ages of spec 47 rev-7, its middle unsighted: (PINNED)
- 60 s (PINNED)
- 90000 s (PINNED)
- AC1 — `read_clock_row` over `$SCRIPT` printed `stale`, aged from its tip: (PINNED)
- `stale 61` (PINNED)
- AC1, RED — `read_clock_row` over the unguarded copy printed `unknown -`, so the two read apart and the tenure reaches the guard. (PINNED)
- AC1 — `grep -c 'DPR47 AC1' tools/unattended/unattended.test.sh` printed: (PINNED)
- 2 (PINNED)
- AC2 — `sed '/^## 9\./,$d' 2026-10-25-spec-TOOL-dPlacedRequest-47.md | tr -s '[:space:]' ' '` carries `never its red case`, counted by `grep -o | wc -l`: (PINNED)
- 2 (PINNED)
- AC2 — the same text's AC1 names `renews: no` commits and the unguarded copy that `stops at the middle commit and prints unknown -`; its S1 closes `Observed by AC1.` (PINNED)
- S1 — the walk's `step` in `tools/unattended/unattended.sh#read_claims` carries the threshold test behind `((rf[i], c) in seen)`, the line the arm's `so_age` names. (DERIVED)

## Owed at the close

- Nothing of a new arm: the spec's Gates section names none, and the arm observed is spec 47's.
- The legs the spec's Gates section names, run once by the main loop.
- Noted, not acted on: spec 47's hands-off edge to this unit still says this unit observes it with a
  new AC4; spec 47 is CLOSED and this spec's rev-6 adds no AC4, so the edge is stale text in a frozen spec.
