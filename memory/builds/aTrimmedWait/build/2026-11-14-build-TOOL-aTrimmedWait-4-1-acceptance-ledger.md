# TOOL-aTrimmedWait-4 acceptance ledger

**Serves:** journal TOOL-aTrimmedWait-4

No merge bar, no self-test suite and no `*.test.sh` ran in this pass. Every observation below was
made on node a, one command at a time with nothing else running, over the spec at rev-3. The code
landed in b2c96fea3. One scratch probe, `probe_wm.py` in the run's scratch directory, builds the
spec's §6 fixture through the generator's own `_fixture`, renders it with `--write`, commits it, and
runs AC1 to AC3 through the CLI. Before each `--write` it sets every file's mtime to one fixed past
value, so any write moves that mtime whatever the filesystem's resolution. It ran once with this
unit's generator, at `%TEMP%/atw4a`, and once with the base kit at `846d51d3`, checked out through
`git worktree add` at `%TEMP%/atw4base`, at `%TEMP%/atw4b`. AC4 and AC5 ran in one clone of this
repository at b2c96fea3, at `%TEMP%/atw4c`. The selftest arm `test_write_moved` and its RED-first
observation are owed to the main loop at the close.

**Evidences:** TOOL-aTrimmedWait-4
- AC1 — `python <gbi> --write` run again in `<f>` exited 0 and printed
  `build-index: wrote 0 artifact(s), 4 unchanged`. The `st_mtime_ns` of every tracked file stayed at
  the value pinned before the run, so the moved set was empty. At base the same run printed
  `build-index: wrote 4 artifact(s)`, and four mtimes moved: `memory/LIVE.md`, the build README, the
  spec and `memory/ledger/2026-08.md`.
- AC2 — the spec's `INPROGRESS` changed to `DEFERRED`, then `python <gbi> --write` exited 0 and printed
  `build-index: wrote 2 artifact(s), 2 unchanged`. The paths whose `st_mtime_ns` moved were the spec,
  `memory/LIVE.md` and `memory/builds/tOne/README.md`, which is exactly the set `git status --porcelain`
  reported. `python <gbi> --check` then exited 0. At base the moved set also held
  `memory/ledger/2026-08.md`, which `git status --porcelain` did not report.
- AC3 — the build README rewritten with CRLF line endings, then `python <gbi> --write` printed
  `build-index: wrote 1 artifact(s), 3 unchanged`. Afterwards the file held no `\r\n` and its bytes
  equalled its LF render from before the rewrite. The base gave the same bytes, after rewriting all
  four artifacts.
- Verdict parity on the fixture — at both generators every `--write` exited 0. `--check` on the
  stale tree after the status flip exited 1 at both, naming
  `memory/builds/tOne/README.md (stale — differs from a fresh render)`. `--check` after the write
  exited 0 at both. `diff -r --exclude=.git` of the two fixture trees after the full run found no
  difference.
- AC4 — the clone at b2c96fea3 had this spec's status changed to `DEFERRED`, committed with
  `--no-verify`. From a clean checkout of that commit (`git reset --hard`, `git clean -fdx`),
  `--write` ran once with this unit's generator, printing `build-index: wrote 2 artifact(s), 3211 unchanged` <!-- PINNED 2026-11-14 -->
  and once with the generator at base `846d51d3`, printing `build-index: wrote 3213 artifact(s)`. <!-- PINNED 2026-11-14 -->
  `git diff --binary` after each, with a sha256 line for each untracked file (none were added),
  measured 3612 bytes, and `cmp` of the two outputs found them byte-identical. <!-- PINNED 2026-11-14 -->
- AC5 — `python tools/memory-tree/gen_build_index.py --write` on the clean clone at b2c96fea3: the
  base generator took 35.8 s and printed `build-index: wrote 3213 artifact(s)`. This unit's took <!-- PINNED 2026-11-14 -->
  32.9 s and printed `build-index: wrote 0 artifact(s), 3213 unchanged`. A second pair on the same <!-- PINNED 2026-11-14 -->
  clone took 32.4 s at base and 32.0 s at this unit, and a pair in this worktree took 36.6 s and <!-- PINNED 2026-11-14 -->
  35.4 s. Every run exited 0 and left `git status --short` empty. The saving here is 0.4 s to 2.9 s, <!-- PINNED 2026-11-14 -->
  well below the 16.8 s that §4 measured with the scratch copy under the session's scratch directory. <!-- PINNED 2026-11-14 -->
  The write half costs less on this clone and this worktree than it did there.
