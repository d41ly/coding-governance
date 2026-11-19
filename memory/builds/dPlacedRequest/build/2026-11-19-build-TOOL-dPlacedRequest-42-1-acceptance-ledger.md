# TOOL-dPlacedRequest-42 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-42

The unit was built from its spec at rev-3 (PINNED) on base `b0c21c920`. The behaviour the spec asks for was
already in the tree: `TOOL-dPlacedRequest-28` moved the feed read into
`tools/unattended/unattended.sh#write_claim`, where a `create` on an empty tip calls
`tools/unattended/unattended.sh#read_feed_lease_tip` whether the write pushes or queues, and
`tools/unattended/unattended.sh#run_lease_verb`'s offline branch reaches that write with `CW_ACT` `create`
once neither a queued line (`read_gov_queue_head`) nor a cache ref names the ref. So this pass changed no
product code (S1, S2): it adds the behavioural arm S3 names and makes section 7's epoch-for-life sentence
name the offline create on an empty parent, rendered byte for byte into `memory/guides/UNATTENDED-STOPS.md`.

No gate, suite or bar ran in this pass. Each criterion below was observed by a probe script in the run's
scratch directory over a fixture of the suite's own `mkconf`, `write_lease_fixture`, `add_claim_sighting`
and `seed_lease_at`, read out of `tools/unattended/unattended.test.sh` by `sed`: a fresh bare origin and
one clone with `RUN_CLAIMS=on` per case under the node's short temp path, the build lease of `tFix` planted,
sighted by a `--claims` read, deleted on the origin with `update-ref -d`, a second `--claims` fetching with
`--prune` so `refs/gov/remote/leases/tFix/build` was gone (0 cache refs, PINNED, in every case), and the
origin renamed away before `--lease acquire build tFix` ran.

**Evidences:** TOOL-dPlacedRequest-42
- AC1 — over the deleted build tombstone the acquire exited 1 (PINNED) printing `lease refused — tombstone · tFix/build · the remote no longer holds it, and this node's feed last saw its tombstone <commit>`, that commit the planted tombstone;
  `gov-queue.log` held 0 lines (PINNED).
- AC2 — over the deleted `released` lease at epoch 4 (PINNED) the acquire exited 0 (PINNED) printing `lease — tFix/build · queued · epoch 5` (PINNED);
  the queue gained 1 line (PINNED) whose expected tip is `-`, so the flush creates the ref, and whose commit
  reads `epoch: 5` (PINNED) with `git rev-parse <commit>^` the feed's commit.
- AC3 — over a ref the feed never named the acquire exited 0 (PINNED) printing `lease — tFix/build · queued · epoch 1` (PINNED);
  the queue gained 1 line (PINNED), expected tip `-`, whose commit reads `epoch: 1` (PINNED) and
  `git log -1 --format=%P` over it prints nothing.

**Owed at the close.** The `New arm:` line of section 7: the region-8 block `TOOL-dPlacedRequest-42` in
`tools/unattended/unattended.test.sh`, 9 assertions (DERIVED: 8 `same`, 1 `hit`), each case on a fixture
of its own, RED-first against the offline branch staged to read no feed (the guard of `write_claim`'s
`read_feed_lease_tip` call given a leading `[ -n "$WL_QUEUE" ] ||`), under which AC1 and AC2 queue the
parentless epoch-1 create. The suite is waived for this build's landing by README rule 8. The floors rose
by the same 9 (DERIVED): `FLOOR_ASSERTIONS` and `FLOOR_SHARD_8`.

**The checklist, acted on.** The bug-class checklist over the pass commit selected 39 classes (DERIVED).
One needed a change. fixture-passes-by-finding-nothing: the block's first assertion read only that no
cache ref stood after the pruning fetch, which a selector matching nothing passes too, so it now counts
`refs/gov/remote/leases/tFix/build` before the deletion and after the pruning fetch, `1 0` (PINNED) for a
planted lease and `0 0` (PINNED) for the unnamed ref; a probe observed both pairs. The pass adds no refusal
branch, so refusal-branch-with-no-arm names none; the floor figure counts the executed `same` and `hit`
calls, as the grader counts them; and the two section-7 copies are byte-identical.
