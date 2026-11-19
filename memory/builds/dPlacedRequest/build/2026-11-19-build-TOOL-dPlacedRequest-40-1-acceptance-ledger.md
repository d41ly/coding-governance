# TOOL-dPlacedRequest-40 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-40

The unit was built from its spec at rev-3 (PINNED) on base `e7abc136d`. In
`tools/unattended/unattended.sh#run_lease_verb` the `TOOL-dPlacedRequest-32` S4 refusal now sits inside one
`case` on the act, right after the `RUN_CLAIMS` switch: `prune`, `flush`, `fence` and `status` are the exempt
list and pass with no session; `acquire`, `take-over`, `renew`, `release` and `offer` are written as the
holder list, and the same arm's `*` gates an act on neither list, so a new act is refused id-less until it
is named exempt (S1, S2). The refusal's line and exit code are `TOOL-dPlacedRequest-32`'s, unchanged. The
stops guide's lease section names both lists, rendered byte for byte into
`memory/guides/UNATTENDED-STOPS.md`; the verbs guide's `--lease` row and `help/loop.md`'s lease paragraph
narrow their no-session clause to the holder acts, the verbs render copied byte for byte, and the
`--lease` usage anchor is unmoved because no usage line moved.

**What the tree said that the spec's goal did not.** At the base only `flush` reached the blanket refusal:
the `--lease` dispatch hands `prune` to `tools/unattended/unattended.sh#write_lease_prune` and `fence` to
`tools/unattended/unattended.sh#write_fence_beat` before `run_lease_verb`, and neither asks for a session,
and no `status` act is dispatched yet. So AC1 and AC3 already held at the base, and the behaviour this
unit moves is `flush`'s; the `prune`, `fence` and `status` names in the exempt arm state the rule for any
future route through the verb.

No gate, suite or bar ran in this pass. The criteria were observed by one probe script in the run's scratch
directory over a bare origin and a clone under the node's short temp path: it extracts the suite's own
`mkconf`, `write_lease_fixture`, `seed_lease_at`, `add_claim_sighting`, `run_offer_arm`, `run_lease_arm`,
`read_lease_field` and claim-clock helpers, then the new suite block itself by `awk`, and runs the block
under stub `same` and `hit` printers. Every id-less call ran through `run_offer_arm` with `-`, that is
`env -u CLAUDE_CODE_SESSION_ID`, with `RUN_CLAIMS` on and no run-state file.

**Evidences:** TOOL-dPlacedRequest-40
- AC1 — a cadence `run` tombstone `run/weekly/2026-10`, sighted eight days (PINNED) ago, past the
  default `leases.queued-claim-days`; `--lease prune` with no session exited 0 (PINNED) printing
  `lease — leases/run/weekly/2026-10 · pruned`, and the origin held 0 (DERIVED) refs under
  `refs/gov/leases/run`.
- AC2 — session `s1` acquired `build tQueue` with the origin renamed away, leaving 1 (DERIVED) line in
  `gov-queue.log`; with the origin back, `--lease flush` with no session exited 0 (PINNED), the queue held
  0 (DERIVED) lines and the origin held the `tQueue` build lease.
- AC3 — with no lease ref on the origin, `--lease fence build tFix` with no session exited 0 (PINNED)
  printing exactly `fence — none · no lease on the remote`.
- AC4 — over `s1`'s held `tFix` build lease, `acquire build tFix`, `take-over build tFix`,
  `renew build tFix`, `release build tFix --as withdrawn` and `offer build tFix --to b` with no session each
  exited 2 (PINNED) printing the `no session` line once, and the origin's `refs/gov` names and tips read
  identical before and after. The control: `s1`'s own `renew build tFix` exited 0 (PINNED) and the record
  still names `session: s1`, so the refusal is the absent session's and not the arguments'.

**Owed at the close.** The `New arm:` line: the `TOOL-dPlacedRequest-40` block of region 8 of
`tools/unattended/unattended.test.sh`, right after the `TOOL-dPlacedRequest-32` block behind a seam of its
own, 7 assertions (DERIVED: 6 `same` and 1 `hit`). The probe above ran it green on this driver; that probe is
no suite reading. Its RED-first observation is the close's: a scratch copy whose exempt list names
`release` reds AC4, its release refused `live-holder` rather than `no session`; a copy refusing every
`--lease` act with no session at the verb's dispatch reds AC1, AC2 and AC3; the base driver reds AC2
alone. The suite is waived for this build's landing by README rule 8. The floors rose by the same 7
(DERIVED): `FLOOR_ASSERTIONS` and `FLOOR_SHARD_8`.
