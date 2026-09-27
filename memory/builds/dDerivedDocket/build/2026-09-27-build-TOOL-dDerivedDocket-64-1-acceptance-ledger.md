# TOOL-dDerivedDocket-64 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-64

A bar waiting in the gate turnstile's queue is now a move. The runner's wait loop writes
`waited<TAB><seconds>` into `gate-queue-heartbeat` under its own worktree's git dir on every tick
that neither acquires nor makes reap or sweep progress. The write is one builtin line between the
`TS_WAITED` refresh and the `TS_MAXWAIT` test, guarded and error-swallowed like the status file's,
and nothing removes the file. `derive_last_move` gains one term after its gate-log term: the file's
mtime, source `gate-queue`, absent contributing nothing and an undatable reading naming the dead
probe that check 52 already refuses on. No key, function, `fail` branch, pinned ordinal, version or
conf key moved. The driver's `--liveness` header and in-body comment name the heartbeat, the protocol
row and both confs point at `--liveness` instead of listing its signals, and the turnstile section of
the run-gates README says what the file is for and that it is never removed. The `unattended` and
`run-gates` dossiers each gained one sentence and stay under the cap.

The suites gained their arms and nothing ran them. The driver suite has 11 assertions in the
`--liveness` signals block and 8 after unit 61's AC20 arm, all in region two, so `FLOOR_ASSERTIONS`
rose 1717 to 1736 and `FLOOR_SHARD_2` 1521 to 1540, with `FLOOR_SHARD_1` unmoved. The resume-tick
suite has 3 after the U62 block, so its floor rose 173 to 176. The turnstile suite has arm 6c's 3
inside the position fixture, so its floor rose 71 to 74. Each count is taken off the block's own
assertion lines.

No merge bar, no gate leg and no `*.test.sh` suite ran in this pass. The direct checks were these.
§4's minimal fixture was run through the driver and `resume-tick.sh --dry-run`, against this unit's
kit and against a copy whose `derive_last_move` lacks the queue term. Each new suite block was run
alone behind a replica of its own suite's prologue, with `HERE` pointed at a kit copy. The signals
block went n 20 to 40, its 9 existing assertions and the 11 new ones, and the AC2 block executed
its 8, all green. Under the term-less copy 15 of the 19 new assertions went red. The tick arm was
3 of 3 green and 2 red under that copy. The turnstile position fixture was 6
of 6 green over this unit's runner. It was red under three runner copies: with the write line
deleted, all three new assertions; with the file removed beside `gate-queue-status`, the outlives
assertion; with the write moved into the position-change branch, the advance assertion.

AC2, AC3, AC4, AC6, AC8 and AC9 carry `permission:` lines, so none gets a line here. Their direct
checks ran all the same. For AC3, the fixture's dry-run printed `skip · verdict LIVE` with the
heartbeat fresh and `resumed · attempt 1` with it dated 2001-01-01. The term-less copy printed
`resumed · attempt 1` for both. For AC6, every `four signals` and enumeration grep read 0, and the
run-gates README carries the basename once. For AC9, both version markers read 1, and the function
counts (199 and 56) and the driver's `fail` count (289) equal the parent's. The added lines of every
edited kit file carry no `tools/<kit>/` literal. The unit names no function, so no lexicon answer is
owed.

**Evidences:** TOOL-dDerivedDocket-64
- AC1 — `last-move-source: gate-queue` — over §4's fixture, 5400 s bound and `run-branch:
  refs/heads/main`, `--liveness` printed `last-move-source: commit`, `stale: yes`, `verdict: STALE`
  with no heartbeat. With one written just now it printed `gate-queue`, `stale: no`, `verdict: LIVE`,
  on the same fifteen keys in the same order. Dated 2001-01-01, past the bound and newer than the
  commit, it read `gate-queue`, `stale: yes`, `verdict: STALE`. With a `stat` stub failing on that
  path alone, the call exited 1 at check 52 naming `stat -c %Y on .git/gate-queue-heartbeat`, with no
  `verdict:` line. The term-less copy read `commit`, `stale: yes` with the fresh file, and `verdict:
  STALE` rather than a refusal under the stub.
- AC5 — `tools/unattended/unattended.sh` — `grep -cE '^[^#]*gate-queue-heartbeat'` printed 1 over it
  and 1 over the gate runner; the loop-scoped `awk` count printed 1; and the `-nE` grep printed the
  heartbeat at line 1038, above the `TS_MAXWAIT` test at 1039.
- AC7 — `git cat-file -s` — the protocol template and its render each read 64424 bytes in 703 lines
  at the parent and 64357 in 703 at the build commit, −67 bytes and 0 lines each.
