# Acceptance ledger — TOOL-aTwinnedPass-3

**Serves:** journal TOOL-aTwinnedPass-3

Built against spec rev-1 in one pass commit, on node a, in the pass's own worktree reset to the
dispatch commit `8397ac8ca`. The spec's forks F1 to F3 carry their resolutions, and the build follows
each: F1 (a), live with no switch; F2 (a), one library predicate called at this unit's two sites,
the three existing inline copies left for the ask §3 names; F3 (b), the ask filed by the main loop at
the close, with nothing in this unit moved by it.

The observations below are each criterion's own command, or the changed driver run over a hand-built
fixture, run in the worktree with the change in place before the commit. No suite, gate leg or bar
ran in the pass. The role gate refused `check-arms.py --check` to the builder as the `harness arms
(fail branches armed or pinned)` leg.

The fixture for AC2 to AC5 was built inside the worktree under an untracked folder, removed before
the commit, the way the driver suite's `mkconf`, `readme`, `runmd` and `build_specced_tree` build the
tRun build: a repository with a bare origin, a `unit` branch ahead of `main`, four READY specs
`ARCH-tRun-1` to `-4`, one `--preflight tRun --keepalive-id k1` with `main` stood at HEAD for that
call, and then `GENERATED_INDEXES="work/idx:gen/mk"` appended to the conf. The same script ran the
six calls of §4 "The arms" twice, over this pass's driver and over the driver and library of base
`aebbb4a72` copied beside each other, with stdout and stderr captured apart.

Owed to the main loop at the close: the new block of ten assertions in region 4 of
`tools/unattended/unattended.test.sh` observed red at base `aebbb4a72`, then green, with
`FLOOR_ASSERTIONS` at 3339 and `FLOOR_SHARD_4` at 420; `check-arms` over the driver suite; and the
legs of the spec's Gates section.

**Evidences:** TOOL-aTwinnedPass-3
- AC1 — `check_generated_output` — the criterion's probe, sourcing the library, printed `work/idx 0`,
  `./work//idx 0`, `work/idx/x 0`, `lane/dir/y 0`, `work 1`, `work/idxa 1`, `gen/mk 1` and
  `empty 1`.
- AC2 — `so condition 1 leaves them out of the sibling comparison` — over the fixture, `ARCH-tRun-1
  --writes work/idx --writes lane/one` and then `ARCH-tRun-2 --writes work/idx --writes lane/two` each
  exited 0 with `dispatch declared` on stdout; each one's stderr carried the note. A fourth call,
  `ARCH-tRun-4 --writes work/idx/sub`, had its stderr matched whole: it carried the note and
  `for ARCH-tRun-4: work/idx/sub` at its end, and `grep -c` over its stdout for the note's two phrases
  printed `0`. The second call printed no `two passes claiming one file are not disjoint`. Over the
  base driver, the first call printed no note and the second exited 1 with `two passes claiming one
  file are not disjoint: work/idx also in`. The suite arm B1 and B2 is owed to the main loop.
- AC3 — ` dispatch · item .* ARCH-tRun-2 · reason work/idx lane/two$` — `grep -c` over the fixture's
  run-state file printed `1` after the second call, and `0` over the base driver's fixture.
  The suite arm B3 is owed to the main loop.
- AC4 — `--dispatch declares a generated index together with its generator` — `ARCH-tRun-3
  --writes gen/mk` exited 1 with that text, over this driver and over the base one. The suite arm
  B4 is owed to the main loop.
- AC5 — `--dispatch declares a path a sibling pass in the same group already declared, and two passes claiming one file are not disjoint: lane/one also in`
  — `ARCH-tRun-3 --writes lane/one` exited 1 with that whole message, naming `ARCH-tRun-1`, over this
  driver and over the base one. Then `ARCH-tRun-3 --writes work` exited 0 with `dispatch declared` and an empty stderr, so
  no note; over the base driver it exited 1 with `work also in`. The suite arms B5 and B6 are owed to
  the main loop.
- AC6 — `git diff --exit-code` — the criterion's `python -c` probe listed 40 check-49 branches over
  this driver and 40 over the base driver; `diff` of the two listings printed nothing.
  `git diff --exit-code` over `tools/unattended/unarmed-branches.txt` printed nothing.
- AC7 — `for p in $_c1_own` — the criterion's awk over `tools/unattended/unattended.sh` printed
  `2 1`, and `grep -c 'TOOL-aTwinnedPass-3'` printed `2`.
- AC8 — `is left out of that comparison` and `other than a generated output` — `grep -c` printed `1`
  for each phrase over each copy, and the `diff` of the two copies past line 1 printed nothing.
- AC9 — `"check_generated_output"` — `lexicon.py --suggest check_generated_output --as sh.function`
  printed `OK — check_generated_output leads with check`. After `gen_map.py --write`,
  `memory/map/generated/symbols.json` gained one function entry for the name, in
  `tools/unattended/lib-unattended.sh`, and nothing else.

## The close

The main loop's observations at the close, on node a, 2026-11-15, at the build tip `39a71c080` unless named.

- The region-4 block of `tools/unattended/unattended.test.sh`, run as a main-loop slice (the suite's prologue and the block): GREEN at `22ce73e14`, 30 assertions and 0 FAIL lines; RED with `unattended.sh` and `lib-unattended.sh` put back to `4f819220f`, 6 FAIL lines naming B1's note, B2's not-disjoint refusal and B6 (PINNED 2026-11-15).
- The whole shard 4/8 run did not finish inside 3000 s on this node and is not a verdict (PINNED 2026-11-15).
- At the tip the slice is GREEN with 33 assertions (PINNED 2026-11-15).
