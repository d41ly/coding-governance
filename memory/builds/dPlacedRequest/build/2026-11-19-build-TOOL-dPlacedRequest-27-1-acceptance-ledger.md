# TOOL-dPlacedRequest-27 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-27

The unit was built from its spec at rev-2 on base `013c010e7`. Each criterion below was observed by a
probe of this unit's own code: `tools/lib/gov-ref.sh` and `tools/lib/gov-feed.sh` sourced in a scratch
bare origin and two clones under the node's short temp path, `GOVREF_RUNNER` a plain runner, the feed
in a fresh `GOVFEED_DIR`; the planted copies are `sed` cuts of the `gov_feed_sh` block the driver
carries, the same cuts the suite's new arms make. No gate, suite or bar ran in this pass; the arm the
spec's §7 declares and its RED-first observation are owed at the close.

**Evidences:** TOOL-dPlacedRequest-27
- AC1 — `refs/gov/bar-red` written to the fixture's main commit, deleted, written and deleted again,
  each through `tools/lib/gov-ref.sh#write_gov_ref` (the deletions through `remove_gov_ref`), left 4
  lines for that ref whose commit column read the commit, 40 zeros, the commit, 40 zeros, `seq` 1 to 4
  (DERIVED); a fifth `add_feed_event refs/gov/bar-red ""` left 4 lines (DERIVED). The same four writes
  over a fresh feed under the planted copy whose `tools/lib/gov-feed.sh#add_feed_event` test keys
  over the whole file left 2 lines, the third and fourth dropped (DERIVED).
- AC2 — `tools/lib/gov-feed.sh#check_feed refs/gov/remote/` over the AC1 feed exited 0 (DERIVED); with
  the fourth line doubled in place (`sed 4p`) it exited 1 printing 1 `duplicate refs/gov/bar-red`
  line naming the 40 zeros (DERIVED). The planted check copy whose duplicate rule keys over the whole
  file exited 1 over the clean AC1 feed (DERIVED).
- AC3 — the first clone wrote `refs/gov/runs/tBack` to a lone commit and then to a second one; the
  second clone fetched and set it back to the first through `write_gov_ref`, exit 0 (DERIVED). After
  the first clone's fetch into `refs/gov/remote/runs/*`,
  `tools/lib/gov-feed.sh#add_feed_sightings refs/gov/remote/` took the ref's lines from 2 to 3, the
  new last line naming the first commit (DERIVED); a second call left 3 and `check_feed` exited 0
  (DERIVED). Under the planted whole-file copy the same sighting left 2 lines (DERIVED).
- AC4 — `grep -n 'retry' tools/unattended/STOPS.template.md` printed 1 line, in section 7's change
  feed paragraph, saying a retry appends nothing and a later repeat appends again (DERIVED);
  `memory/guides/UNATTENDED-STOPS.md` is its byte copy, `cmp` silent.
- The 13-AC2 staged cut, re-anchored on the new test's `exit` clause, still appends a retried event
  that the real block drops: 7 lines stayed 7 under the block and became 8 under the cut (DERIVED).
- The `gov_feed_sh` block cut from `tools/lib/gov-feed.sh`, `tools/unattended/unattended.sh` and
  `tools/run-gates/post-merge.sh` compared equal by `diff`.

## Owed at the close

- The `New arm:` line of the spec's §7: `tools/unattended/unattended.test.sh`, the
  TOOL-dPlacedRequest-27 rows of the region-8 feed block (12 `same` rows, DERIVED), each staged red by
  the planted whole-file copies `$fd_two.whole` and `$fd_two.chk`; waived for this build's landing by
  README rule 8.
- The legs §7 names, run once by the main loop.
