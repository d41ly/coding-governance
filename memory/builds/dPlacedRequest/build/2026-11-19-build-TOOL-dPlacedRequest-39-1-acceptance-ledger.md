# TOOL-dPlacedRequest-39 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-39

The unit was built from its spec at rev-4 on base `7af144383`. `tools/lib/gov-feed.sh#add_feed_event` (PINNED)
keeps its clock test, its common-dir cache and its git reads in the caller's shell and runs the lock
take, the key check, the counter and the append in a subshell `( … ) || rc=$?`, whose `EXIT` trap,
armed on the line after the take, calls `tools/lib/gov-feed.sh#remove_dir_lock` with the call's
token. The subshell's exit is read once: 0 returns quietly, 3 prints today's lock-busy NOTE, any (PINNED)
other prints `feed: NOTE - <ref>: the append exited <rc>`; every path returns 0. The take is (PINNED)
TOOL-dPlacedRequest-24's `write_dir_lock_wait` with its wait of 5 s, as the tree holds it, where the (PINNED)
spec's sketch spells the factory's single take: the wait is the factory's retrying form and the
NOTE for rc 3 is today's line, which names that wait. The block's comment states the containment (PINNED)
and what it does not check. The block was spliced byte-identically into
`tools/unattended/unattended.sh` and `tools/run-gates/post-merge.sh`. No gate, suite or bar ran in
this pass: each criterion below was observed by a probe of the spec's own shape, the `gov_feed_sh`
cut of `tools/lib/gov-feed.sh` sourced by an argument path under `bash -c 'set -u; …'` inside a
scratch repository with one commit under the node's short temp path. (PINNED)

**Evidences:** TOOL-dPlacedRequest-39
- AC1 — with `: "$GOVFEED_PLANT_UNSET"` planted on the line after the trap's arming, the call printed
  bash's `GOVFEED_PLANT_UNSET: unbound variable` line, then 1 line `feed: NOTE - refs/gov/bar-red: (DERIVED)
  the append exited 1`, then `after`; the shell exited 0 and no `gov-feed.lock` remained in the (DERIVED)
  common dir. The same planted copy under `set -eu` printed the same lines and exited 0. The staged (DERIVED)
  case, the base's own uncontained body with the plant after its take, printed the unbound-name line,
  never `after`, exited non-zero, printed 0 NOTE lines and left `gov-feed.lock` held. (DERIVED)
- AC2 — the unplanted cut appended 1 line whose `seq` reads 1; the same ref and commit again left 1 (DERIVED)
  line and no lock. A caller probe after the call read `GOVFEED_DIR` set and `s`, `n` and `l`
  unset, so the subshell sets no global a caller reads beyond the cache S3 keeps in the caller (S3).
- Busy — a live lock held by another token, 60 s ahead, gave the lock-busy NOTE after the wait, (DERIVED)
  `after`, and the other writer's `owner` untouched: the trap is armed only after a take.
- Parity — `cksum` of the `gov_feed_sh` cut read one sum in all 3 files; `bash -n` read all 5 (DERIVED)
  changed shell files clean. No function was minted, renamed or deleted.
- Siblings' arms the containment moves. `tools/lib/resolve-python.test.sh#check_feed_copies`'s two
  release plants named the explicit release line the trap replaces, so both now plant on the trap
  line; a probe applying each plant to the canonical cut read 1 matching line, the command plant (DERIVED)
  printed `release_feed_lock: command not found` and the held plant left `gov-feed.lock`, the two
  reds the arm expects. TOOL-dPlacedRequest-37's region-8 AC3 red, a copy with the clock test cut, (PINNED)
  now aborts inside the subshell: a probe of that copy read `rc=0 1 0 no-log no-lock`, so its (DERIVED)
  expectation and its header say so; it still differs from the green reading on the NOTE that names
  the clock.
- The arm's fixtures — a probe applying the new block's 5 `sed` scripts to the driver's cut read (DERIVED)
  each one changing its copy, and running the block's calls over them read `after 1 no-lock` for
  the planted copy, `no-after 0 lock` for the brace-group copy, `after 1 lock` for the trap-cut (DERIVED)
  copy, `after 1 1 / after 1` for the clean append and its retry, and `after 1 1 / after 2` for the (DERIVED)
  copy whose key check falls through.
- The bug-class checklist over the pass commit selected 54 classes. One needed a change: (DERIVED)
  `refusal-branch-with-no-arm`, since the busy exit's NOTE, a decline line the restructured body
  dispatches on rc 3, had no arm. The block now drives it: a live lock another writer holds, 60 s (DERIVED)
  ahead, through a copy taking with no wait, read `after 1 0 other`, the busy NOTE alone and the (DERIVED)
  holder's `owner` untouched; its red, the same copy with the busy take exiting 4, read (DERIVED)
  `after 0 1 other`, an abort's NOTE in its place, both observed by a probe of the two copies. The (DERIVED)
  `heredoc-escape-reaches-the-regex` class bit once in this pass, a backslash lost from a plant line
  written through a heredoc before the commit, and the line was rewritten with the edit tool. The
  rest needed none: the plant's arm asserts bash's unbound-name line, so its fixture reaches the
  abort; each staged red is a `mutate` of the shipped cut that reds a no-op; counts are `grep -c`
  over files; every git call unsets `GIT_DIR` or runs under `env -i`, and the scratch commit passes
  `--no-verify` and `commit.gpgsign=false`.

## Owed at the close

- The spec's `New arm:` line: `tools/unattended/unattended.test.sh`, the region-8 (PINNED)
  TOOL-dPlacedRequest-39 block in a compound block of its own, 15 executed assertions (7 `same`, 1 (DERIVED)
  `hit`, 7 `mutate`), no skip branch; `FLOOR_ASSERTIONS` 3709 to 3724 and `FLOOR_SHARD_8` 940 to (DERIVED)
  955. Its RED-first observation inside the suite is the close's; waived for this build's landing (DERIVED)
  by README rule 8. (PINNED)
- The positional citations of `tools/unattended/unattended.sh` and `tools/run-gates/post-merge.sh`
  past the `gov_feed_sh` block, which the block's net 13 added lines move, read by the pass legs. (DERIVED)
- `tools/lib/resolve-python.test.sh` section 2a over the retargeted release plants, and the (PINNED)
  TOOL-dPlacedRequest-37 region-8 block's changed AC3 red reading, both read by their suites at the (PINNED)
  close.
- The legs the spec's Gates section names, run once by the main loop.
