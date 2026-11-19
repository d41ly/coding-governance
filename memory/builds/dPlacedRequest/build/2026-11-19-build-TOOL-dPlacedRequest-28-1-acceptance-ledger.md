# TOOL-dPlacedRequest-28 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-28

The unit was built from its spec at rev-4 (PINNED) on base `a2a6af2d2`, the second dispatch after the first
returned a divergence. `tools/unattended/unattended.sh#read_feed_lease_tip` holds the read
`tools/unattended/unattended.sh#run_lease_verb` made inline under "THE EPOCH FOR LIFE", its `awk` and its
`cat-file` unchanged, and prints nothing, `tombstone <commit>` or `<commit> <epoch>` (S1).
`tools/unattended/unattended.sh#write_claim` is its one caller: after it derives its ref and before it
computes the epoch, a `create` on an empty tip reads it; a feed commit parents the create at its epoch plus
one, the ref still expected absent, and a feed tombstone builds, pushes and queues nothing and returns 3
(PINNED), `WC_WHY` naming the feed commit (S2). That return is mapped once, in the refusal arm, keyed on
`CW_MODE`, which `tools/unattended/unattended.sh#check_claim_writable` now sets to the column it graded:
check 107 (PINNED) for `preflight` and `take-over`, check 108 (PINNED) for `holder`, the policy's own line
otherwise. `tools/unattended/unattended.sh#run_lease_verb` keeps no feed read and maps 3 to
`lease refused — tombstone` before its queued branch; `tools/unattended/unattended.sh#write_lease_offer`
resets no tip and no epoch (S3); `tools/unattended/unattended.sh#verb_resume`'s two holder writes return 1
on 3 as on 1, and `tools/unattended/unattended.sh#write_settle_claim` names no retry on 3. Section 7 of
`tools/unattended/STOPS.template.md` names every create, and `memory/guides/UNATTENDED-STOPS.md` is its
byte-identical render.

No gate, suite or bar ran in this pass. Each criterion below was observed by a probe script in the run's
scratch directory over a fixture of the suite's own `mkconf`, `write_lease_fixture`, `add_claim_sighting`
and `seed_lease_at`, read out of `tools/unattended/unattended.test.sh` by `awk`: a bare origin and one clone
with `RUN_CLAIMS=on` under the node's short temp path, each lease planted, sighted by a `--claims` read and
deleted on the origin with `update-ref -d`.

**Evidences:** TOOL-dPlacedRequest-28
- AC1 — `--lease offer unit tFix TOOL-tFix-2 --to b` over the sighted unit tombstone, deleted on the origin, exited 1 (PINNED) printing `tombstone`, the origin holding no such ref;
  the line read `lease refused — tombstone · tFix/unit/TOOL-tFix-2 · the remote no longer holds it, and
  this node's feed last saw its tombstone <commit>`, that commit the planted tombstone.
- AC2 — the same offer over a sighted `released` lease at epoch 4 (PINNED), deleted, wrote `epoch: 5` (PINNED), `status: released`, `offer: b`, parented on the feed's commit;
  it printed `lease — tFix/unit/TOOL-tFix-3 · offer b · epoch 5` (PINNED), and the origin's `ref^` equalled
  the planted commit.
- AC3 — the offer of `TOOL-tFix-4`, a ref the feed never named, wrote `epoch: 1` (PINNED) with no parent;
  `git log -1 --format=%P` over it printed nothing.
- AC4 — the sourced `read_feed_lease_tip` printed nothing, `tombstone <commit>` and `<commit> 4` (PINNED) for the three cases, and `--lease acquire unit tFix TOOL-tFix-2` exited 1 (PINNED) printing `tombstone` and the feed commit;
  the acquire's line was the offer's, byte for byte. Offline, the origin renamed away, the same acquire
  exited 1 (PINNED) with the same line and the queue log stayed empty.
- AC5 — in the lease fixture's clone, standing in for the claim fixture's tree, `write_claim tRun live k1 strict` after `read_claims strict` and `check_claim_writable tRun preflight k1 s1 k1` returned 0 (PINNED) over a sighted `released` build lease at epoch 4 (PINNED), deleted;
  `CW_ACT` read `create` and `CW_MODE` `preflight`, the origin's `refs/gov/leases/tRun/build^` was the
  feed's commit and the ref read `epoch: 5` (PINNED). The same call through a staged `write_claim` whose
  read is cut by `sed` returned 0 (PINNED) and built the parentless commit at `epoch: 1` (PINNED), the RED.
- AC6 — over a sighted, deleted build tombstone, `write_claim` under the `preflight` column returned 3 (PINNED) and printed check 107 (PINNED) carrying `tombstone`, the origin holding no ref;
  the `take-over` column printed check 107 (PINNED) and the `holder` column check 108 (PINNED) naming
  `--abort <slug> --code claim-lost`, each setting the exit status 1 (PINNED); the `status` column printed
  the one `claim not written` line carrying `WC_WHY`, the `beat` column printed nothing, and
  `write_settle_claim` printed that one line and no retry, each leaving the status 0 (PINNED). The
  `--preflight` verb itself is observed by the suite's arm, which needs the run fixture.

**Owed at the close.** The `New arm:` line of section 7: the region-8 block `TOOL-dPlacedRequest-28`
in `tools/unattended/unattended.test.sh`, 21 assertions (DERIVED), RED-first against the base
driver, whose offer and driver creates read no feed; the block carries its own staged RED for AC5 beside
it. The suite is waived for this build's landing by README rule 8. The block's `--preflight` and two
`--resume` arms observe AC6 through the verbs, which no probe here ran, and the floors rose by the same
21 (DERIVED). Also owed: the suite's run-claim arms after the feed clearing below, which no probe ran.

**The fixture's feed.** Every create now reads the clone's feed, and the suite's claim fixture kept one feed
across every arm, so `remove_claim_refs` and the SU fixture's claims branch now clear the feed with the refs;
an arm meaning a deletion outside the kit deletes the one ref with `update-ref -d` and keeps it.
`seed_lease_at` takes `LF_CLONE` for the clone whose feed sights the commit.

**The checklist, acted on.** The bug-class checklist over the pass commit selected 52 classes (DERIVED).
Two needed a change. refusal-branch-with-no-arm: the `take-over` alternative of `write_claim`'s
return-3 arm had no arm, so the block now calls the sourced take-over column to its check 107; and
`verb_resume`'s two holder writes were edited where one arm reached one, so a second `--resume` under
another session, whose lease is not current, reaches the other. amendment-leaves-its-other-half-standing:
section 7's offer paragraph still called an offer over an absent lease a create at epoch 1, so it now
reads the feed as every create does, rendered byte for byte. A probe observed the take-over column's
check 107 (PINNED) and return 3 (PINNED).
