# TOOL-dPlacedRequest-16 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-16

The unit was built from its spec at rev-8 on base `5f71c0608`. A lease is never deleted by the kit
but a run's tombstone. `tools/unattended/unattended.sh#read_claims` reads the status `released` with
the verdict `released`, stamps `gov-last-fetch` on every read that answered, and carries the walk's
renewing beat out as the row's `beat-sha` field.
`tools/unattended/unattended.sh#check_claim_writable` classes a `released` record and a build or unit
tombstone before the identity rows and a draw's hold after them, read by one first-parent `git log`.
`tools/unattended/unattended.sh#run_lease_verb` gains the release outcomes, `--for draw`, the hold's
own-holder rule and the feed's epoch for a create of a ref the remote no longer holds.
`tools/unattended/unattended.sh#write_gov_queue` refuses an aged, absent or unparsable `last-fetch`
as `epoch-fence`, `tools/unattended/unattended.sh#write_lease_prune` is the new `--lease prune`, and
`tools/unattended/unattended.sh#run_budget_draw` wraps the patch draw in the root's hold. The run's
end writes `released` in `verb_landed`, `verb_abort`, `verb_preflight` and
`tools/unattended/unattended.sh#write_settle_claim`. The card's
`skills/session-kickoff/manifest-check.sh#derive_claims_line` ranks and hides `released` as
`terminal`.

Each criterion below was observed by a probe: the driver's `--lease` verb over two scratch clones of
one bare origin under the node's short temp path, `RUN_CLAIMS` on and `USERNAME=daily-agent`, and the
driver sourced in a clone for the write table's run columns and for `run_budget_draw`. Epochs differ
from the spec's where the probe planted its tombstone at another epoch; each is the read epoch plus
one, as the criterion states. No gate, suite or bar ran in this pass; every new arm's RED-first
observation is owed at the close.

**Evidences:** TOOL-dPlacedRequest-16
- AC1 — session `s1` released its live `tFix` at epoch 1 and session `s2` on the second clone
  acquired it live at epoch 2, parented on the `released` commit; `s1` released that at epoch 2 and
  acquired it itself live at epoch 3 on the `released` commit, `renews: yes` (DERIVED).
- AC2 — `--preflight` — the second half only: sourced over a `released` build lease, the write
  table's `preflight` column read `foreign-released` and the act `take`, rc 0 (DERIVED). The first half,
  `--landed` writing `released` over a fixture run, was not run here: the run-claim arms AC9 and AC20
  now type `released` after `--abort` and `--landed`, owed to the suite at the close.
- AC3 — over a `landed` build lease at epoch 4, its writer's acquire, another session's acquire and a
  take-over each exited 1 printing `lease refused — tombstone`, the ref unchanged; sourced over the
  same row, `preflight` and `take-over` printed `UNATTENDED check 107 FAILED` carrying `tombstone`,
  `holder` check 108, `status` one announced line ending `tombstone` with rc 3, `beat` rc 3 (DERIVED).
- AC4 — a draw over the tombstone at epoch 4 wrote `held` at epoch 5 parented on it, and
  `--as landed` wrote `landed` back at epoch 5; a second draw held at epoch 6, its holder's renew
  wrote `held` with `renews: no`, and another session's draw exited 1 `live-holder`. With the
  opener's sighting planted two days old the draw took the hold at epoch 7, parented on it, and a
  third session read `foreign-tombstone`; with the next opener's line removed a draw read
  `live-holder`, and planted stale a take-over and an acquire each read `tombstone`, the ref
  unchanged (DERIVED).
- AC5 — `tombstone` — a run lease at epoch 2 deleted after this node sighted it was re-created at epoch 3 parented
  on the deleted tip; a sighted build tombstone deleted from the origin refused `tombstone`, the ref
  absent (DERIVED).
- AC6 — a queued acquire planted eight days old was refused `epoch-fence` and removed, and one
  planted six days old flushed; the queue read empty after (DERIVED).
- AC7 — clone A read no lease for `tQ`, clone B acquired and released it, A queued an acquire offline
  and its flush printed `yield`, the origin keeping B's chain (DERIVED).
- AC8 — `--lease prune` deleted a cadence lease and a legacy claim each sighted eight days ago and
  left a legacy claim sighted six days ago and a build tombstone sighted a year ago;
  `--lease prune build tTomb` and `--lease prune unit tTomb u1` each exited 1 printing
  `prune refused — tombstone` (DERIVED). The first probe pruned the six-day claim too, because the
  claim read re-set `LB_VALUE` to the expiry bound; the prune now keeps its own bound.
- AC9 — section 7 of `tools/unattended/STOPS.template.md` holds `released` 10 times, `tombstone`
  17 times, `--for draw` 2 times and `leases.queued-claim-days` 3 times, and its terminal-take
  sentence names cadence and legacy run claims only; the render compared equal under `cmp` (DERIVED).
- AC10 — with `gov-last-fetch` deleted, and planted `garbage`, an offline acquire queued
  `last-fetch: -`, and the flush refused it `epoch-fence`, removed the line, wrote no ref and exited
  0 (DERIVED).
- AC11 — `--as aborted` on a build lease and `--as withdrawn` on a run lease each exited 2 with
  `lease not written`, the refs unchanged; `--as aborted` on the run lease wrote `aborted`,
  `--as withdrawn` and `--as landed` on a build lease wrote their status; over a draw's hold a plain
  release and `--as withdrawn` printed `a draw's hold is released --as landed`, `--as aborted`
  exited 2, and another session's acquire read `tombstone` (DERIVED).
- AC12 — `CLAIM_READS` by `CLAIM_MODES` against the cells `GC_CELLS` types, compared with
  `comm -3`, printed nothing over 60 cells each side (DERIVED).
- AC13 — `gov-last-fetch` — the driver's own stamp lines, extracted and run 200 times in the background beside 200 reads
  by its own queued-record reader lines, read `-` 0 times; the grep the criterion names printed 0, and
  the reader over an absent file read `-` (DERIVED).
- AC14 — with the budget module stood in by a stub, `run_budget_draw tPatch re-dispatch u1` over a
  root tombstoned at epoch 5 set `_bd_rc` 0, logged 1 draw, and left the root reading `landed` at
  epoch 6, `held` at epoch 6 and the epoch-5 tombstone; with another session's fresh hold it set
  `_bd_rc` 2 naming `live-holder` and drew nothing; offline it named `queued` and drew nothing; with
  `RUN_CLAIMS` off it drew and no lease moved (DERIVED). The first probe drew nothing offline for
  another reason, the peers' claim read, so the acquire now runs before the peers' refusal is applied.
- AC15 — the card's awk, extracted from `derive_claims_line`, over nine rows printed
  `claims — 9 on the remote · 6 shown · 3 hidden`, `sRel` sorted beside `vLanded`, `rRelOld` hidden
  (DERIVED); with `released` dropped from its set it printed `claims — skipped:` (DERIVED).
- AC16 — `tombstone` — sourced over the run's own tombstone, the status column printed one line carrying
  `tombstone` and returned 3, which `write_settle_claim` reads as nothing written; the `--settle` arm
  is owed to the suite at the close.
- The suite gains the block `TOOL-dPlacedRequest-16 — A LEASE NEVER DELETED` and 12 new `GC_CELLS`
  rows in region eight and a settle arm in region six, 105 assertions (DERIVED): `FLOOR_ASSERTIONS`
  3578 to 3683, `FLOOR_SHARD_8` 812 to 914 and `FLOOR_SHARD_6` 127 to 130 (DERIVED). Existing arms
  that typed `landed` or `aborted` after a run's end now type `released`, and the queue-lock arm's
  first line carries a recent `last-fetch`. The card suite gains 2 assertions, its floor 350 to 352
  (DERIVED).
- The bug-class checklist over the pass commit named `refusal-branch-with-no-arm`: the block now also
  arms a renew and a release of a `released` lease, the prune's unit, missing-period, offline and
  `RUN_CLAIMS`-off refusals, and a refused `leases.queued-claim-days` keeping a queued line and
  refusing the prune, each probed first over the scratch fixture (DERIVED). It named
  `ledger-token-wrapped-across-a-line-joins-nothing`, and no code span in this ledger wraps.
- `gen_map.py --write` regenerated `memory/map/generated/symbols.json` for `write_lease_prune`; the
  `--lease` usage anchor in `help/loop.md` is refreshed to the fingerprint that
  `docs_leg.py --fingerprints` printed.
