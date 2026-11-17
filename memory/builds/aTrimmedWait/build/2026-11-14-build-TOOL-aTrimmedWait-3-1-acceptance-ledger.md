# TOOL-aTrimmedWait-3 acceptance ledger

**Serves:** journal TOOL-aTrimmedWait-3

No merge bar, no self-test suite and no `*.test.sh` ran in this pass. Every observation below was
made on node a, one command at a time with nothing else running, from the worktree root over the
pass's tree, the spec at rev-2. Three scratch probes drove it, each kept in the run's scratch
directory: `probe_ws.sh` builds the spec's §6 fixture at `$TEMP/tws3` through the generator's own
`_fixture` and runs `--write-staged` through every AC1 to AC4 case; `probe_hook.sh` commits through
the hook over stand-in hygiene and generator gates at `$TEMP/tws3h`, and over the parent's hook
(`git show HEAD:.githooks/pre-commit`) at `$TEMP/tws3b`; `probe_time.sh` times the same commands
with the parent's generator and this pass's, swapped in turn into one kit path at `$TEMP/tws3t`, so
the kit path each prints is equal. The selftest arm `test_staged_write`, the hook suite's new arms,
every new arm's RED-first observation, and AC9 and AC10 are owed to the close.

**Evidences:** TOOL-aTrimmedWait-3
- AC1 — `python <gbi> --write-staged` in the §6 fixture exited 0 and printed
  `build-index: staged memory/LIVE.md` and `build-index: staged memory/builds/tOne/README.md`.
  Afterwards `git diff --name-only` printed nothing, `git diff --cached --name-only` listed those two
  paths beside the spec and no other, and `python <gbi> --check` exited 0. At the parent the mode word
  printed the usage line and exited 2.
- AC2 — with `STAGED_RENDER=""` the run exited 1 printing
  `build-index: render NOT staged — STAGED_RENDER is blank, so the hook does not render`, and
  `git status --porcelain` was unchanged. With `STAGED_RENDER="yes"` it exited 1 printing
  `build-index: STAGED_RENDER='yes' is not one of its two legal values, blank (off) or 1 (on)`,
  status unchanged. Run a second time after AC1's success it exited 1 printing
  `render NOT staged — no artifact's bytes moved, so check 9's refusal is not drift a render cures`.
- AC3 — with `GIT_INDEX_FILE` set to a copy of the fixture's index under another name the run exited 1
  naming that index. With `GIT_INDEX_FILE` set to `<f>/.git/index`, spelled both `/c/...` and
  `C:\...`, it exited 0 staging the same two paths as AC1. The first attempt declined its own index:
  `%TEMP%` spells the short name `DAILY-~1` and git prints the long form, so `check_staged_write` compares
  `os.path.realpath` after `os.path.normcase` rather than `os.path.abspath`, which is "names the same
  file" of §4; a reviewer should read this as the one place the code spells §4's comparison
  differently.
- AC4 — an unstaged edit to the tracked `memory/notes.md` exited 1 naming `memory/notes.md`; an
  unstaged edit to the tracked `src/x.sh` with `LIVE_LANDED_UNCLOSED` blank exited 0; the same edit
  with the key set to `1` exited 1 naming `src/x.sh`. Each decline left `git status --porcelain`
  unchanged. `build_render_pathspec` returned `['memory/', '.memory-tree.conf', 'kit/', 'carries.py']`
  and `[]` with the key set, the list `check_staged_render` built before the extraction.
- AC5 — `probe_hook.sh`, its stand-ins planted as `run_prefix_commit` plants one: the stand-in
  hygiene gate printed `HYGIENE check <N> FAILED — drift`, N = 9, on its first run, and with a
  staging stand-in generator the commit printed `GEN RAN --write-staged`, then
  `pre-commit: the build index was rendered and staged; grading the memory hygiene leg again.`,
  exited 0 after two hygiene runs, and HEAD carried `memory/rendered.md`. The parent's hook refused
  the same commit after one run.
- AC6 — `probe_hook.sh`, check 12: the generator never ran, one hygiene run, refused. Check 9 with the
  stand-in generator exiting 1: one hygiene run, refused. Both refusals compared line for line with
  the parent hook's, differing only by the generator's own `GEN RAN --write-staged` line in the
  second. `grep -c 'echo "HYGIENE check $1 FAILED' tools/memory-tree/check-memory-hygiene.sh` printed 1.
- AC7 — `grep -c '^STAGED_RENDER=""' tools/memory-tree/.memory-tree.conf.example` printed 1,
  `grep -c '^STAGED_RENDER="1"' .memory-tree.conf` printed 1 and
  `grep -c 'write-staged' tools/memory-tree/README.md` printed 1; each printed 0 at the parent.
- AC8 — `grep -c 'commit-render.md' help/README.md` printed 1, and `grep -rl 'STAGED_RENDER' help`
  named `help/commit-render.md`, which names `HYGIENE check <N> FAILED`, N = 9, and `git commit <path>`, the
  partial-commit exclusion. Each printed 0 at the parent.
- AC9 — `git commit -m probe` — not run in the pass: the commit runs the real hygiene gate through
  the hook in two clones, the unit's and base `846d51d3`, and the spec's permission line makes it the
  main loop's. Both wall times and the base remedy's, `--write`, `git add` and the second commit,
  are owed to the main loop at the close.
- AC10 — `STAGED_RENDER=""` — not run in the pass, as AC9. The unit clone's refusal with the switch
  blank, its `HYGIENE check` lines compared with the base clone's, is owed to the main loop at the
  close.
- Same command before and after (`probe_time.sh`, the §6 fixture, the spec change staged):
  `python <gbi> --check --staged` exited 1 at both, 783 ms with the parent's generator and 780 ms <!-- PINNED 2026-11-14 -->
  with this pass's, its whole output identical under `diff`. The parent's remedy, `--write` and <!-- PINNED 2026-11-14 -->
  `git add -A memory`, took 1328 ms; this pass's `--write-staged` took 1072 ms and staged the same <!-- PINNED 2026-11-14 -->
  three paths. Neither figure includes the second commit the parent's remedy also needs.
- Fix pass (`2026-11-14-prompt-TOOL-aTrimmedWait-3-fix`) — the `git rev-parse --git-path index` call in
  `tools/memory-tree/gen_build_index.py#check_staged_write` names `encoding="utf-8"` beside `text=True`, and
  `` grep -nE 'HYGIENE(\.md)?`? check [0-9]' help/commit-render.md tools/memory-tree/README.md `` printed nothing,
  exit 1, as did the same pattern over this ledger. `probe_ws.sh` and `probe_hook.sh` printed byte-identical
  output before and after the edit, under `diff`, the before run over the generator and hook of 634815f08; the
  `AC3-own` cases run the edited call. Same commands timed one at a time on node a: `probe_ws.sh` 15142 ms <!-- PINNED 2026-11-14 -->
  before and 12617 ms after, `probe_hook.sh` 8415 ms before and 14589 ms after, the hook unchanged <!-- PINNED 2026-11-14 -->
  by this pass, so the spread is the node's. The encoding-posture and tags legs that reported both reds are
  owed to the main loop's pass legs.
