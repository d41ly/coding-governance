# TOOL-dLandedOwners-3 — acceptance ledger

**Serves:** journal TOOL-dLandedOwners-3

No merge bar, gate or self-test suite ran in this pass. Each criterion was observed by the spec's own
command, or by a `python -c` probe calling the unit's functions, from the worktree root, with the landed
revision L at `5a311c9f` (the remote-tracking `origin/main` at this pass). Every red was observed either at
the pass's base `06a4802b`, before the first edit, or as a staged break made inside the probe's own
process: a name replaced on the imported module, or a scratch copy of `check_policy.py` under the
session's scratchpad imported ahead of the kit's, so no tracked file was edited to observe it. The
fixture repositories were made by the case's own `tempfile.mkdtemp(prefix="pol-")` under `%TEMP%` and
removed by `remove_repo`; the real repository's refs were never written.

**Evidences:** TOOL-dLandedOwners-3
- AC1 — `run_reader_declared('reader-coverage-declared')` printed `case declared-outside: green`, its
  line carrying `declared outside the scan at memory/builds/bPlanted/build/instrument.py: the instrument applies the value`,
  and `case declared-unlanded: green`, its line carrying `so this arm checked nothing at`, with no
  line carrying `WRONG:`. Red: with `read_unscanned_readers` replaced by one returning no rows,
  `case declared-outside: red` printed `WRONG: graded 1 · reader coverage: fixture.planted (owner bPlanted, landed at`
  and `has no reader`.
- AC2 — the same call printed `case <name>: red` for `declared-and-read`, `declared-untracked`,
  `declared-scanned`, `declared-malformed`, `declared-unknown` and `declared-twice`, each with the text
  its row of `RD_CASES` names, no `WRONG:`, and returned `(8, 0)` (PINNED, this pass). Red: on a
  scratch copy whose `elif path in scanned:` reads `elif False:`, `case declared-scanned: green`
  printed `WRONG: graded 1` and the disposition line for `consumer.py`, `(8, 1)` (PINNED, this pass).
  The case's run through `check_policy.py --fixture reader-coverage-declared`, with the guard-trace
  and count lines, is the `policy fixtures` leg's and is the main loop's at the close.
- AC3 — the spec's command over `check_reader_coverage('.', landed={'dDeclaredLoop'})` printed
  `reader coverage: deviation.approval (owner dDeclaredLoop) declared outside the scan at memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py: the chain applies the approval route in this instrument at the value PLAY-dClosedLoop-4 fixed, author-recorded; no tracked code passes the key to a policy reader`
  after `reader coverage: graded 32 of 273 catalogue key(s)` (DERIVED, the catalogue at this pass),
  and its last line `[]`. Red: at the base, and again with `read_unscanned_readers` replaced by one
  returning no rows, the last line was
  `['reader coverage: deviation.approval (owner dDeclaredLoop, landed at 5a311c9f) has no reader']`.
  `arm_reader_coverage` through `run_arm` over this tree, owners derived, printed the same
  disposition line and `0 finding(s) · 64 of 273 catalogue key(s) graded for a reader` (DERIVED, this pass).
- AC4 — `run_reader_coverage('reader-coverage')` printed every case line the base printed, identical
  once each `landed at` and `nothing at` sha is masked, and returned `(13, 0)` (PINNED, this pass):
  the eleven cases of the spec's base and the two `TOOL-dLandedOwners-2` added after it (PINNED, `84595fe08`). Red: with
  `READER_SKIPPED` replaced by a pattern matching nothing, `case not-a-reader: green` printed
  `WRONG: graded 1`, `(13, 1)` (PINNED, this pass).
- AC5 — the spec's command printed `[['legacy-homes.txt', 'unscanned-readers.txt']]`. Red: at the
  base it printed `[['legacy-homes.txt']]`.
- AC6 — `grep -c "unscanned-readers.txt"` counted `help/policy.md:3` and `tools/policy/README.md:5`
  (PINNED, this pass), and `grep -F "declared outside the scan at" help/policy.md` printed the
  disposition line's form. Red: at the base both counts were `0` and the second grep printed nothing.

Owed to the close (M8): the arm `tools/policy/check_policy.py --fixture reader-coverage-declared`
observed RED on its staged break and GREEN restored, recorded here under a `Pass: none` commit, and
the legs of the spec's section 7.

## New-arm observations (main loop, M8)

Observed at `f3a64d91b` in an LF clone under `%TEMP%/armlo`, through `python tools/policy/check_policy.py --fixture <case>`, one staged break at a time, the file restored byte for byte after each run. Before the breaks and after the restore every fixture below read `0 wrong` at `f3a64d91b`.

- `--fixture reader-coverage-declared` · break: `read_unscanned_readers` answers no rows (its `is_file` test replaced by `True`) · RED: `case declared-outside` printed WRONG, rc 1 at `f3a64d91b` · GREEN once restored.
- `--fixture reader-coverage-declared` · break: the scanned-path test of `check_reader_coverage` (`elif path in scanned`) replaced by `elif False` · RED: `case declared-scanned` printed `WRONG: graded 1`, rc 1 at `f3a64d91b` · GREEN once restored.
