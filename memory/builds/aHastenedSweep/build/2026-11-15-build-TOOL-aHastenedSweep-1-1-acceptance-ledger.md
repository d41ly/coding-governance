# Acceptance ledger — TOOL-aHastenedSweep-1

**Serves:** journal TOOL-aHastenedSweep-1

Built against spec rev-1 in one pass commit, on node a, in the pass's own worktree reset to the
dispatch commit `deef46d66`. The §4 line holds at that tip: the call site is line 3103 of
`tools/memory-tree/check-memory-hygiene.sh`, and its text is the one §4 quotes.

The observations below are each criterion's own command, run in the worktree with the change in
place before the commit, or the changed engine and the shipped one over a hand-built fixture. No
suite, gate leg or bar ran in the pass.

Owed to the main loop at the close:
- AC3, the live-tree A/B: `check-memory-hygiene.sh --only 25`, changed against shipped at one commit,
  `cmp`-identical with the same exit code, with both wall times and the output's line count recorded here.
- The legs §7 lists, and in the `memory-hygiene self-test` leg the check 25 arms `tFixture-208`,
  `tFixture-209`, `tFixture-216` and the word-boundary fixtures 218 to 221 keeping their red verdicts.
  This unit adds no arm, so no `New arm:` red-then-green is owed.

**Evidences:** TOOL-aHastenedSweep-1
- AC1 — `cmp` — in a fresh repository at `%TEMP%/hs1fx`, built with the suite's conf and
  `write_readers_spec` shape, its guide `memory/guides/treaders.md` opening line 3 with
  `count_shard_rows` at column 1 and spelling `tSpelledInGuide`, `tRerunAll` and `--dry-run` on line 4,
  and eight committed specs, `bash <worktree>/tools/memory-tree/check-memory-hygiene.sh --only 25` and
  the shipped engine from `git archive f25308f0 tools` both exited 1 and `cmp` printed nothing. The
  output carries one U line each for `count_shard`, `tRerun`, `shard_rows`, `--dry` and
  `tAbsentReader`, each saying `which no reader spells`, and one `READER NOT IN TREE covers it` line for
  `tAbsentReader`, and names neither `count_shard_rows` nor `tSpelledInGuide`. Its red case, a scratch
  copy with the guard written `index(ln, pl[i]) > 1`, exited 1 and differed from the shipped output at
  line 7, a U line for `count_shard_rows`.
- AC2 — `git diff --numstat f25308f0` — printed one row for the shell, 2 added and 1 deleted;
  `grep -c 'index(ln, pl\[i\]) && test_whole_token(ln, pl\[i\])'` printed `1` and
  `grep -c "TOOL-aHastenedSweep-1)"` printed `1`. `bash -n` over the shell exited 0.
- AC3 — `--only 25` — NOT OBSERVED in this pass: the live-tree A/B is the main loop's at the close, as
  the criterion's permission line assigns, and its wall times and line count are recorded here then.
- AC4 — `git show --stat HEAD -- memory/guides/SESSION-KICKOFF.md` — the pass commit stages the
  manifest with `last-audit` re-stamped at `deef46d66706f10b0d46f7d4b6d50fa6a98e8839`, the dispatch
  HEAD; `git log -1 --format=%H -G'^last-audit:'` over the manifest is read after the commit.
