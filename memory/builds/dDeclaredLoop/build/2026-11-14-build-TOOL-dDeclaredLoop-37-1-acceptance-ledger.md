# TOOL-dDeclaredLoop-37 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-37

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed by
the `git grep` commands the spec's §4 "The probes" spells, run from the repository root over the
working tree and over base `ed497191`, by the two `python -c` commands of the same section, and by
a scratch `python` probe that imports `tools/memory-tree/routed_commits.py`, builds the planted
repository through `build_fixture` and calls `check_trailer_parses` over it. The pass base is
`edef0b36`.

Owed to the close: every leg the spec's section 7 names, and the RED-first observation of its two
`New arm:` lines, both in `tools/memory-tree/routed_commits.py#run_selftest`. The second line's
staged break is the one deviation 373 describes: observe it on the arm's unreadable-revision call.

**Evidences:** TOOL-dDeclaredLoop-37
- AC1 — `git grep -n -F` — the S1 probe over the built tree, this pass's edit to
  `tools/memory-tree/routed_commits.py` included, printed no line and exited with git's no-match
  status. With `ed497191` before the `--` it printed the base lines, by file as the figure below.
  The arm's own needles and its planted format are written as split adjacent literals, so the file
  that holds them is not printed.
  figure: PINNED, measured 2026-11-14: 6 lines at base, 2 in `tools/memory-tree/routed_commits.py`, 1 in `tools/unattended/check-unattended.sh`, 2 in `tools/unattended/lib-unattended.sh` and 1 in `tools/unattended/unattended.sh`; none on the built tree.
- AC2 — `read_attribution_tokens` — each S2 probe printed at least one line on the built tree:
  `read_commits(` and `derive_attribution(` in `tools/memory-tree/routed_commits.py`, the `replace`
  call in `tools/memory-tree/deviation_join.py`, the `tokens` call and the `--reverse` call in
  `tools/unattended/lib-unattended.sh`, the `-1` call in `tools/unattended/check-unattended.sh` and
  the `message` call in `tools/unattended/unattended.sh`. With `ed497191` before the `--` every one
  of them printed none.
- AC3 — `check_trailer_parses` — the first S5 command printed no hit; the second, given
  `ed497191`, printed the base lines of AC1 as `<path>:<line>` relative to the tool root, the same
  files and the same count as AC1's base run. Over the planted repository the predicate, given the
  fixture commit, returned the consumer's line alone, and neither the `*.test.sh` nor the
  `commit_trailers.py` holding the same format; given no revision it returned an empty list, since
  the fixture checks nothing out; given a revision git cannot parse, and given a directory outside
  any repository, it raised `Refusal` carrying git's line.
  figure: PINNED, measured 2026-11-14: 6 lines at base through the predicate, 1 line over the planted repository.

The staged break, observed in the same probe with `run_git`'s failure read as no hit: the planted
consumer was still named and the base run still printed its lines, so the break as the spec's
second `New arm:` line and AC3's `Red when:` clause word it moves neither. The unreadable-revision
call returned an empty list under that break, which is what the planted arm now refuses. Recorded
as `2026-11-14-build-TOOL-dDeclaredLoop-37-deviation-373.md`.

Not run here: the two arms themselves, which only the `routed-commits selftest` leg executes. The
probe calls the predicate with the arms' own arguments and stands in for that leg until the close.
