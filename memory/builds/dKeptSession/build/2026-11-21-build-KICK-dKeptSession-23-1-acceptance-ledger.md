# KICK-dKeptSession-23 — acceptance ledger

**Serves:** journal KICK-dKeptSession-23

No merge bar, no self-test suite and no gate leg ran in this pass, and the legs the spec's section 7
names were not run as commands. The criteria were observed on win32 at the pass's base `9900b200`.
AC1, AC2 and AC5 were observed by a fixture probe: a scratch script that lifts the suite's `same`,
`mkconf`, `run_mail_arm` and `read_mail_refs` and this unit's new block verbatim, moves the fixture
root to a short path under the user temp directory and the driver's own scratch to the session
scratchpad, and runs the tracked driver through them; no other block of the suite ran. It printed
five assertions and no FAIL (DERIVED, that probe). AC3 and AC4 were observed by the direct probes
the spec names, sourcing `tools/lib/gov-feed.sh` in a fresh bash and calling `scan_feed_writers`.

Before the first edit the spec's cited code was probed at the base, and each claim held.
`write_mail_ref` (`tools/unattended/unattended.sh#write_mail_ref`) builds its commit through
`build_gov_commit` under the `gov-claim` identity over `git mktree`'s empty tree and writes it only
through `write_gov_ref` (`tools/unattended/unattended.sh#write_gov_ref`), whose one success exit
calls `write_feed_success`, which sets the cache ref and calls `add_feed_event`; a lost or
uncompleted write returns before it. `write_mail_post` (`tools/unattended/unattended.sh#write_mail_post`)
and `read_mailbox` (`tools/unattended/unattended.sh#read_mailbox`) each call
`add_feed_sightings refs/gov/remote/` after their fetch. `scan_feed_writers`
(`tools/lib/gov-feed.sh#scan_feed_writers`) reads `FEED_WRITER_HELPER_FNS` as `add_feed_event
write_feed_success write_gov_ref`, and its "WHAT THIS DOES NOT CHECK" names the four shapes S4
states. The census arm's section "THE FEED WRITER CENSUS" in `tools/lib/resolve-python.test.sh`
plants the plain push of `refs/gov/mail/fx/a/s1` in its `plain.sh`. The `REFUSAL_CEILINGS` row of
`.memory-tree.conf` reads 347 for the driver and 266 for its checker (PINNED, read 2026-11-23 at
`9900b200`), and neither file is edited here. The suite's effective pins were `FLOOR_ASSERTIONS=4095`
and `FLOOR_SHARD_8=1312` (PINNED, read 2026-11-23 at `9900b200`), units 5's and 31's raises on top of
unit 22's.

The driver carries 19986 lines at this base (DERIVED, `wc -l` at `9900b200`), so the planted push of
AC3, appended after the last line, sits lower than section 4's census probe line at `c9e89a057`; the
design does not move.

`memory/map/generated/symbols.json` does not move: the new block defines no shell function, and its
racer `git` shim is a file the block writes, not a function of the suite. No row of
`tools/run-gates/selftest-budgets.txt` is re-priced, as section 4 states.

Owed to the close: every leg the spec's section 7 names; the unattended suite whole, whose effective
`FLOOR_ASSERTIONS` rises from 4095 to 4100 and `FLOOR_SHARD_8` from 1312 to 1317 (PINNED, the new
block's five unconditional `same` rows, all in region eight); and the `New arm:` line's RED-first
observation, the block run against a copy of the driver whose `write_mail_ref` pushes around
`write_gov_ref`, and against one that appends whatever its push did.

## Decisions taken in the build

- The block builds unit 5's two-clone fixture again rather than appending to unit 5's block: AC1
  needs a bare remote holding no mail ref, and unit 5's block leaves several, while a post of this
  block's inside it would move unit 5's own row counts. It reuses `run_mail_arm` and
  `read_mail_refs`, which unit 5's block defines in the same region, and defines no function.
- AC2's lost post runs on session `s3` and the shim records the `<commit>:<ref>` it was asked to
  push, so the criterion reads the lost commit by name, absent from the remote and from the feed,
  rather than only the lines the feed gained, which a lost post leaves empty.
- AC5 runs after the lost post, so A's read may sight the racer as well; the row reads the lines
  naming B's commit, which is what the criterion counts.

**Evidences:** KICK-dKeptSession-23
- AC1 — the fixture probe: over a bare remote holding no governance ref, A's one post on `s1` left one line in A's feed, `refs/gov/mail/fx/a/s1`, `mail`, `4b825dc642cb6eb9a060e54bf8d69288fbee4904` and the remote tip of that ref.
  (DERIVED, that probe: one line, PINNED, the fixture's single post.)
- AC2 — the fixture probe: the same post retried printed `mail — duplicate <id> · refs/gov/remote/mail/fx/a/s1`, exit 1, and the feed held the line count it held before; the post on `s3` under the racer shim printed `mail — lost <id> · refs/gov/mail/fx/a/s3 · lost the race on the lease: [rejected] (stale info)`, exit 1, the remote ref holding the racer.
  (DERIVED, that probe.) The commit the shim recorded was absent from the bare remote by `cat-file -e` and named by no feed line, and no line the feed gained named a commit the remote lacks (DERIVED, that probe).
- AC3 — `bash -c '. tools/lib/gov-feed.sh && scan_feed_writers "$1"' _ <copy>` over a scratch copy of the driver with a planted `planted_mail_writer` pushing `refs/gov/mail/fx/a/s1` under `--force-with-lease` and calling no helper, appended after its last line, printed one line naming the copy's path and the planted push's line, the copy's second-to-last, and exited 1.
  (DERIVED, that probe: the copy held 19989 lines, PINNED, that probe.)
- AC4 — the same probe over the shipped `tools/unattended/unattended.sh` printed nothing, rc 0; `awk '/^write_mail_ref\(\)/,/^}/' tools/unattended/unattended.sh | grep -v '^[[:space:]]*#' | grep -cw push` printed 0, and the same body with `grep -cw write_gov_ref` printed 1.
  (DERIVED, that probe.)
- AC5 — the fixture probe: after B's `fy` posted one `question` to `build:fx` and A ran `--mail read fx`, A's feed gained one line naming B's commit, its ref `refs/gov/mail/fy/b/t1` and kind `mail`.
  (DERIVED, that probe.)
