# TOOL-dPlacedRequest-37 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-37

The unit was built from its spec at rev-6 on base `281fabfb7`. The tree already met S1: (PINNED)
TOOL-dPlacedRequest-24 minted `NODE_LOCK_BOUND=10` at the top of the `gov_feed_sh` block and the (PINNED)
feed's take passes it as the hold of `tools/lib/gov-feed.sh#write_dir_lock_wait`, so S1 and AC2 were
observed, not rebuilt. S3 is the one code change: `tools/lib/gov-feed.sh#add_feed_event` tests
`EPOCHSECONDS` as its first statement and, unset, prints `feed: NOTE - no EPOCHSECONDS, bash 5 or (PINNED)
later is required` on stderr and returns 0 before the lock, the log or git; the block's comment states
the floor. The block was edited identically in `tools/unattended/unattended.sh` and
`tools/run-gates/post-merge.sh`. Each criterion below was observed by a probe: the spec's own `awk`
cut of `gov_feed_sh` from post-merge, sourced under `env -i PATH="$PATH" bash -c 'set -u; …'` with no
`REMOTE_BOUND` set, over a scratch repository's common dir under the node's short temp path. No gate,
suite or bar ran in this pass.

**Evidences:** TOOL-dPlacedRequest-37
- AC1 — `write_dir_lock "$c/gov-feed.lock" t1 "$NODE_LOCK_BOUND" node; echo rc=$?` printed `rc=0`, and
  `until` read the clock after the call plus 10 exactly. The staged copy, its constant line replaced (DERIVED)
  by `NODE_LOCK_BOUND=$(( REMOTE_BOUND + 10 ))`, printed `REMOTE_BOUND: unbound variable`, no `rc=` (PINNED)
  line, and left no lock.
- AC2 — over the canonical cut of `tools/lib/gov-feed.sh`, `grep -c 'REMOTE_BOUND'` printed 0 and (DERIVED)
  `grep -c '^NODE_LOCK_BOUND=10$'` printed 1. (DERIVED)
- AC3 — `set -u; unset EPOCHSECONDS`, then `GOVFEED_DIR=$c add_feed_event refs/gov/runs/tFix <commit>`
  inside the scratch repository printed 1 line, `feed: NOTE - no EPOCHSECONDS, bash 5 or later is (DERIVED)
  required`, then `rc=0`; neither `gov-feed.log` nor `gov-feed.lock` existed after. The staged copy
  with the test cut aborted on `EPOCHSECONDS: unbound variable`, no `rc=` line. A control call with
  the clock set appended 1 line to the feed, so the test leaves a bash 5 append as it was. (DERIVED)
- Parity — `cksum` of the `gov_feed_sh` cut read one sum in all 3 files; `bash -n` read all 4 (DERIVED)
  changed shell files clean. No function was minted, renamed or deleted, so `memory/map/generated/`
  was not regenerated.
- The arm — the new region-8 block, cut from `tools/unattended/unattended.test.sh` and sourced alone (PINNED)
  with stubbed `same`, `hit` and `mutate`, read 7 assertions green over this tree, 7 counted on its (DERIVED)
  skip branch; over a scratch carrier with S3's test cut it red AC3 and its `mutate`, and over one
  whose bound reads `REMOTE_BOUND` it red AC1, AC3 and its `mutate`.

## Owed at the close

- The spec's `New arm:` line: `tools/unattended/unattended.test.sh`, the region-8 (PINNED)
  TOOL-dPlacedRequest-37 block, 7 executed assertions (4 `same`, 1 `hit`, 2 `mutate`), counted on (DERIVED)
  its skip branch too; `FLOOR_ASSERTIONS` 3702 to 3709 and `FLOOR_SHARD_8` 933 to 940. Its (DERIVED)
  RED-first observation inside the suite is the close's; waived for this build's landing by README
  rule 8. (PINNED)
- The legs the spec's Gates section names, run once by the main loop.
