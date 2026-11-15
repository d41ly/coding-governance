# Acceptance ledger — TOOL-aTwinnedPass-2

**Serves:** journal TOOL-aTwinnedPass-2

Built against spec rev-2 in one pass commit, on node a, in the pass's own worktree reset to the
dispatch commit `4d7da6191`. The spec's forks F1 to F4 carry their resolutions, and the build follows
each: F1 (a), `git merge --no-ff`; F2 (a), the verbs in their own file `pass-tree.sh`, sourcing the
driver; F3 (a), a second verb `--remove` sharing `remove_pass_tree`; F4 (a), a `--from` flag compared
with the fork point exactly.

The observations below are each criterion's own command, or the new tool run over a hand-built
fixture, run in the worktree with the change in place before the commit. No suite, gate leg or bar
ran in the pass. The fixture was the suite's own, built by hand inside the worktree under an
untracked folder and removed before the commit: `main` with the base commit and then `m1.txt`;
`run`, checked out, cut from the base and carrying the records commit C (`918ae24c`) with the
run-state file `memory/builds/tRun/RUN.md`; the conf in `mkconf`'s shape; the fixture kit
`tools/fx/` with one `[[generated]]` row for `fx-out.txt` and its `render.sh`; and copies of
`regen.py` and `profile_bar.py` at `tools/run-gates/`. Passes 2, 3, 4, 5, 7 and 8 were worktrees on
`agent-p<n>` reset to C, passes 9 and 10 cut from `main` with no reset. The isolation hook refused a
fixture-wide `core.hooksPath`, so the fixture's commits ran this node's global hooks, which skip in
a tree that holds no kit; the suite sets the fixture's own empty hooks path. Pass 2's merge ran
before every plain `git` call in the tool went through the library's pinned `GIT`; that edit
silenced the graft-file hint those calls printed and changed no verdict, and every later probe,
pass 3's whole merge path included, ran the committed tool.

Owed to the main loop at the close: the suite `tools/unattended/pass-tree.test.sh`, arms T1 to T5,
observed red at base `aebbb4a72`, where the tool is absent and every arm's run exits 127, then
under each mutation its `New arm:` lines name (`--no-ff` dropped, the `Pass: none` line dropped,
`check_resolvable_path` returning 0, the fork-point and run-state refusals removed, the restore's
`git clean -qfd` removed, `--remove`'s lost-commit refusal removed and widened to an ahead-of-`HEAD`
test), then green; its first run confirms or re-declares the 300 s budget row; AC9's measurement;
and the legs of the spec's Gates section.

**Evidences:** TOOL-aTwinnedPass-2
- AC1 — `merge(tRun): TOOL-tRun-3's pass tree` — over the fixture, `--merge tRun --pass TOOL-tRun-2
  --branch agent-p2 --from <C>` and then the same for pass 3 each exited 0 and printed one sha alone
  on stdout. `%p` of each merge read `<previous HEAD> <pass commit>`: pass 2's `f8fd26a1`, pass 3's
  `21bd1ae`. Pass 3's merge conflicted on `fx-out.txt` and the README's `gen:fx` region; regen
  reported `moved: README.md, fx-out.txt`, `fx-out.txt` read `p2.txt` then `p3.txt`, the README's
  region the same, and `render.sh --check` exited 0. The subject read as the token, the `Pass`
  trailer read `none`, the body `Merges agent-p3 at 21bd1ae…, dispatched from 918ae24c.`, `git
  worktree list` named the run's tree alone, `git branch --list 'agent-p*'` printed nothing, and
  `git status --porcelain` printed nothing.
- AC2 — `agent-p4` — pass 4 reset to C committed its own `p2.txt`; `--merge` of it after pass 2
  exited 1 with one stderr line naming `p2.txt` and not `fx-out.txt`. HEAD stayed `3b57c68`, `git
  status --porcelain` printed nothing, `git rev-parse -q --verify MERGE_HEAD` exited 1, and branch
  `agent-p4` and its worktree remained. The first probe, before the merge's own lines went to a
  scratch file, showed `git merge -q` still printing `CONFLICT (content): Merge conflict in <path>`
  for an admitted path; that is why they do.
- AC3 — `pass-tree: REFUSING` — nine `--merge` calls each exited 1 with one line opening with the
  token: from pass 5's worktree on `agent-p5` (naming `refs/heads/run`); with an untracked
  `stray.txt` (naming the clean test); for `agent-none`; for `run`; for `-x`; for pass 5, naming
  `--remove`; for pass 8, naming the run-state file; with `--from HEAD`; and for pass 9 with
  `--from <C>`, reading `forks from 95756833, not from 918ae24c ... its builder did not reset its
  worktree to that commit`. HEAD stayed `3b57c68` and `git status --porcelain` stayed empty, and
  `git ls-files m1.txt` printed nothing.
- AC4 — `fx-partial.txt` — `--merge` of pass 7 with `FX_RENDER_FAIL=1` exited 1 after regen
  reported `moved: fx-partial.txt` and `FAILED`; HEAD stayed `3b57c68`, `git status --porcelain`
  printed nothing, `fx-partial.txt` was absent, and `MERGE_HEAD` did not resolve.
- AC5 — `bash pass-tree.sh --remove tRun --branch agent-p5` — exited 0 for pass 5 and, as
  `agent-p10`, for pass 10 cut with no reset; neither branch nor worktree remained. For `agent-p7`
  it exited 1 naming `--merge` and both remained. For `agent-none` it exited 0 with one stderr NOTE
  naming it.
- AC6 — `pass_commit <anchor> TOOL-tRun-2 <run-state file>` — a `bash -c` sourcing
  `tools/unattended/lib-unattended.sh` in the fixture printed pass 2's `f8fd26a1…`, not the merge,
  with exit 0; `bash tools/unattended/unattended.sh --check-commit` over a file holding pass 3's
  merge message exited 0.
- AC7 — `grep -c 'tools/unattended'` — printed 0 over `pass-tree.sh`; above its first function, at
  line 70, `grep -cF` found `--dispatch`, `--brief`, `unattended-unit.js`, `passBase`, `writes`,
  `Pass: none`, `--merge`, `--from` and `--remove` each at least once. `grep -c "pass-tree.sh"`
  printed 1 over each guide copy, and the criterion's `diff` printed nothing.
- AC8 — `python tools/lexicon/lexicon.py --suggest <name> --as sh.function` — printed `OK` for each
  of the eleven inventory names and for the suite's `check_has`, `check_lacks`, `check_same`,
  `run_tool`, `measure_refusals`, `write_fixture_pass` and `check_merge_refused`. After
  `gen_map.py --write`, `memory/map/generated/symbols.json` carried one entry for each of the tool's
  ten functions and the suite's eight, and nothing else moved. `grep -c "pass-tree.test.sh"` printed
  1 over `tools/unattended/kit.toml`, inside the `project-owned` include list, and 1 over
  `tools/run-gates/selftest-budgets.txt`; `grep -c "pass-tree.sh"` printed 1 over the kit README.
- AC9 — `tools/workflows/unattended-unit.js` — not observed in the pass: the serial and parallel
  measurement is the main loop's at the close, as the criterion's permission line says.
