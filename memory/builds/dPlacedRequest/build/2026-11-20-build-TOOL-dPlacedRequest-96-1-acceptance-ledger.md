# TOOL-dPlacedRequest-96 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-96

The unit was built from its spec at rev-2 on base `d1de266d1`. Built: S1, the `lease:foreign-stale`
row of `tools/unattended/unattended.sh#check_claim_writable` restored beside the `lease:foreign-released`
row and above `lease:*`, byte for byte the row commit `71f85d59f` added, read by `git show` and compared
by `diff`. The arms are the TOOL-dPlacedRequest-96 block of `tools/unattended/unattended.test.sh`, a
seam of its own in region eight right after the observer clock's block, over that block's fixture and
its helpers `add_lease_commit` and `add_claim_sighting`; `FLOOR_ASSERTIONS` and `FLOOR_SHARD_8` are
raised by its assertion count. No gate, suite or bar ran in this pass.

THE AC1 PROBE, the reading the lines below cite as "the probe": a scratch script under the run's
scratch directory builds a bare origin and one clone under a short temp path, the clone's conf from the
suite's own `mkconf` with `RUN_CLAIMS="on"` and a policy file of `[budgets] enforce = "warn"`, plants
on the origin a `tStale/build` lease of session `s1`, node `other`, at its first epoch, `renews: yes`,
and plants its first sighting in the clone's change feed a day and an hour back; then it runs
`--lease acquire build tStale` and `--lease take-over build tStale` under `CLAUDE_CODE_SESSION_ID=s2`
and reads the origin's lease record after.

THE JOIN PROBE: a scratch script running the static arm's pipeline, the same `sed`, `grep -o` and
`awk` text, over one driver file and printing the read set, the reset block's lines, the missing names
and the liveness pair; never the suite.

**Evidences:** TOOL-dPlacedRequest-96
- AC1 — `stale, so --lease take-over takes it` — the probe over the driver at this pass: acquire exited 1 printing `lease refused — live-holder · tStale/build · node b · session s1 · beat 90005s · status live · verdict stale · stale, so --lease take-over takes it`. (DERIVED)
- AC1 — `take-announced` — the probe's take-over then exited 0 printing `unattended: claim taken over — tStale · node b · session s1 · …` and `lease — tStale/build · take-announced · epoch 2`. (DERIVED)
- AC1 — `epoch:` — the origin's lease record read `epoch: 1` before and `epoch: 2` after the take-over, its `session:` now `s2`. (DERIVED)
- AC1 — `95c3103ad` — the RED reading: the same probe through a scratch clone's `tools/` checked out at that commit, its driver blob `0e8038fd5` the same as this pass's base, printed acquire exit 1 `lease refused — live-holder · tStale/build · … · verdict stale` with no hint, and take-over exit 1 with the same `live-holder` line, the origin's record left at `epoch: 1` and session `s1`. (DERIVED)
- AC1 — `95c3103ad` — the join probe over the driver at that commit printed `missing: [CW_HINT ]`, the static arm's staged break as the spec states it; over the driver at this pass it printed `missing: []`. (DERIVED)
- AC1 — `95c3103ad` — the join probe read the reset block as two lines both times, `CW_HINT=` only on the second, and the first kept line `[ "$mode" != lease ] || la="$wka"`. (DERIVED)

## Readings beside the criteria

- The read set the join collects from `run_lease_verb` and `write_fence_beat`: `CW_ACT CW_CAUSE CW_CLS CW_DRAW CW_EPOCH CW_HINT CW_KIND CW_NODE CW_SHA CW_TAG CW_WHO CW_WIT`, twelve names. (DERIVED)
- The block's assertions counted off its lines: three `same` and four `hit` for the probe arm, two `same` for the join, nine in all, each moving the executed count by one. (DERIVED)
- The floors as written: `FLOOR_ASSERTIONS` from 4044 to 4053. (DERIVED)
- `FLOOR_SHARD_8` from 1263 to 1272. (DERIVED)
- `bash -n` over both edited files exited 0. (DERIVED)
- The arm `DPR1 AC2` of the lease grammar's block, a take-over of a planted stale lease to epoch two, reads the row this unit restores, so its reading moves with this pass; it is not re-observed here. (DERIVED)
- The unattended kit's version carrier was not moved by hand: the kit-epoch rule has the lander mint it at the push boundary, as `KIT_UNATTENDED_VERSION`'s history of `mint:` commits shows and as this build's earlier driver moves carry no hand bump. (DERIVED)

## Items diverged

None.

## Owed at the close

- `New arm:` `tools/unattended/unattended.test.sh`, the TOOL-dPlacedRequest-96 block, nine rows, the floors raised; its RED-first observation against the lease column at `95c3103ad` and its GREEN reading inside the suite are the close's, its clean reading owed with PLAY-dClosedLoop-14 under README rule 8. (DERIVED)
- The legs the spec's Gates section names, run once by the main loop.
