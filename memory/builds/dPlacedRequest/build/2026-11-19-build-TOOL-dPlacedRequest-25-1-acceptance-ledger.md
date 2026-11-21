# TOOL-dPlacedRequest-25 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-25

The unit was built from its spec at rev-3 on base `0575ae861`. `renews` now has one derivation,
`tools/unattended/unattended.sh#derive_lease_renews`, called once per lease write by
`tools/unattended/unattended.sh#write_claim` over the epoch read (empty on a create), the epoch it
writes, `leases.renewal` and a witness verdict. The verdict is the verb's
(`tools/unattended/unattended.sh#run_lease_verb`: `question`, `new` or `none` from
`check_lease_witness`) or the driver's (`tools/unattended/unattended.sh#read_lease_renewal`, now
setting `LR_VERDICT`), so the per-act `case` on `CW_ACT` under `fixed` and the per-policy `case` in the
verb are gone. The `witness` key is written as before. Each criterion below was observed by a probe:
the driver's `--lease` verb over a scratch clone and bare origin under the node's short temp path,
`RUN_CLAIMS` on, `USERNAME=daily-agent`, the conf keys the suite's `mkconf` writes, and
`derive_lease_renews` called in a shell that sourced the driver. The same fixture probe run over a
detached checkout of the base read `renews: no` for the take-over, the create and the legacy claim's
first lease write. No gate, suite or bar ran in this pass; the arm the spec's Gates section declares and its
RED-first observation are owed at the close.

**Evidences:** TOOL-dPlacedRequest-25
- AC1 — session `s2`'s `--lease take-over build tFix` with no witness, over a planted stale lease at
  epoch 1 under the default `progress`, exited 0 and the record read `epoch: 2` and `renews: yes`; the
  `--lease renew build tFix` after it read `epoch: 2` and `renews: no` (DERIVED). Over the base the
  take-over read `renews: no` (DERIVED).
- AC2 — `--lease acquire build tNew` with no witness read `epoch: 1` and `renews: yes`; with
  `leases.renewal` planted `none` a create read `renews: -`; planted `fixed` a create read `yes` and
  the renew after it `no` (DERIVED). Over the base the create read `renews: no` (DERIVED).
- AC3 — `derive_lease_renews` over the table printed, per policy, the create, the raised epoch, and
  the same epoch with a `new`, a `question` and a `none` verdict: `progress` yes yes yes yes no,
  `activity` yes yes yes yes yes, `fixed` yes yes no no no, `none` - - - - - (DERIVED), each cell as
  the spec's table states. A policy outside the four, a refused read, printed `no` (DERIVED).
- AC4 — `grep -n 'tenure' tools/unattended/STOPS.template.md` printed the `leases.renewal` row of
  section 7, which now says a write that opens a tenure renews under every value but `none`; the
  render `memory/guides/UNATTENDED-STOPS.md` compared equal to the template under `cmp` (DERIVED).
- AC5 — over the stubbed open question, two renews of `tNew` each given the planted commit as
  `--witness` both read `renews: yes`, the witness stored as that commit (DERIVED);
  `derive_lease_renews 3 3 progress question` printed `yes` (DERIVED).
- The legacy claim's first lease write (S2) — `--lease acquire build tMig` over a slug holding only a
  legacy claim wrote `epoch: 1` and `renews: yes` (DERIVED); over the base it read `renews: no`
  (DERIVED).
- The suite block `TOOL-dPlacedRequest-25: A WRITE THAT OPENS A TENURE RENEWS` adds region-eight
  assertions, all `same`: 7 of them (DERIVED).
  `FLOOR_ASSERTIONS` moves 3571 to 3578 (DERIVED), and `FLOOR_SHARD_8` 805 to 812 (DERIVED).
  Its steps were run as the probe above under other lease names; the block itself was not run, and
  its RED-first observation against a scratch copy keyed on the act name is the close's.
- `gen_map.py --write` regenerated `memory/map/generated/symbols.json` for the minted function.
