# TOOL-aTrimmedWait-8 acceptance ledger

**Serves:** journal TOOL-aTrimmedWait-8

No merge bar, no self-test suite and no `*.test.sh` ran in this pass. Every observation below was
made on node a, one command at a time with nothing else running, over the spec at rev-2, from the
worktree root at base `c563cccaf`. The pass probe is `probe8.py`, saved in the run's scratch
directory: it builds `<f>` and `<d>` as §6 defines them in fixture repositories under the short
temp path, runs `<gbi> --write-staged` through its CLI for each case, and reads `git status
--porcelain` and `git diff --cached --name-only` before and after. It ran once against the built
`tools/memory-tree/gen_build_index.py` and once against the base copy, extracted with `git archive
HEAD` into the scratch directory. The changed code is `tools/memory-tree/gen_build_index.py#cmd_write`,
`tools/memory-tree/gen_build_index.py#_build_design_fixture`,
`tools/memory-tree/gen_build_index.py#test_asbuilt_view` and
`tools/memory-tree/gen_build_index.py#test_staged_write`.

**Evidences:** TOOL-aTrimmedWait-8
- AC1 — with `<d>`'s staged conf setting `DESIGN_BASELINE` to forty zeros, `python <gbi> --write-staged`
  exited 1 and printed `build-index: render NOT staged — as-built view — DESIGN_BASELINE` as its only
  line, and the status and cached names were unchanged. The base copy exited 1 after staging the
  build README and LIVE, the red the criterion names.
- AC2 — with an empty `<f>/.git/index.lock` planted and `GIT_INDEX_FILE` unset, the run exited 1 and
  printed `git add refused the rendered artifacts`; after the lock was removed the tree was unchanged
  and the build README held its committed bytes. The base copy left the written README in place.
- AC3 — with `<d>`'s view hand edit and tOne's `parents: nope` staged, the run exited 1 naming
  `parents: names 'nope'`, the tree unchanged and the view at its staged bytes; with the view's
  removal staged instead, the same run left no view file. The base copy left the view rewritten in
  the first case and recreated in the second.
- AC4 — `<d>` with `BACKLOG_MODE="builds"` and `ASK_CUTOFF="2099-01-01"` rendered and committed, an
  authored `- ARCH-tOne-9` row staged into the ARCH view and the as-built view hand-edited and staged:
  the run exited 1, printed `render NOT staged — the data-loss guard holds memory/backlog/ARCH.md`,
  and the tree was unchanged, with the guarded branch's inline restore deleted.
- AC5 — `<f>` with a committed `memory/ledger/2020-01.md`: the run exited 0, printed
  `build-index: staged memory/ledger/2020-01.md`, the file was gone, and
  `git diff --cached --name-only --diff-filter=D` listed it.
- AC6 — `GIT_INDEX_FILE` set to a copy of the index named `other-index`: the run exited 1 naming it,
  and the tree was unchanged.
- AC7 — `GIT_INDEX_FILE` set to a copy of the index at `<f>/.git/index.lock`: exit 0 and
  `build-index: staged memory/builds/tOne/README.md`. With `GIT_INDEX_FILE=.git/index`, a relative
  path, exit 0 the same way. `own + ".lock"` and the resolved compare in `check_staged_write` are
  untouched, so `git commit -a` and a plain commit proceed as at base.
- AC8 — `check-memory-hygiene.sh --only 12 --spec` naming tThree-1's path, over the scoped tree the
  suite's own fixture lines built in a short temp directory: exit 1, one line holding `declares no matching **consumes-from**` for tThree-1, equal to the
  unscoped `--only 12` run's line, and no line naming `2026-09-08-spec-tThree-3.md`, whose payload
  finding the unscoped run printed. `--build tOne` still printed `over 4 spec(s) of tOne`. <!-- PINNED 2026-11-14 -->
- AC9 — `grep -E '"\$SCOPED" = 1|\| SCOPED' tools/memory-tree/check-memory-hygiene.sh | grep -oE '[A-Z0-9_]+_CUTOFF' | sort -u`
  printed exactly `SPEC_EDGES_CUTOFF`, and `grep -c 'SPEC_EDGES_CUTOFF="2026-09-08"' tools/memory-tree/check-memory-hygiene.test.sh`
  printed 2. The arm's armed-date test, run by hand over the scope tree's conf, armed `SPEC_EDGES_CUTOFF`
  at the last committed spec date `2026-09-08` and reported an unset key as unarmed.
- AC10 — `python tools/check-spec-tokens.py --legs-for tools/memory-tree/check-memory-hygiene.sh`
  printed `branch-guard self-test <- tools/memory-tree/check-memory-hygiene.sh [selftests/repo]`, and
  `git diff --numstat -- tools/gate-legs.json` printed one line added and none removed: the path sits
  before `{prefix}/lib/` so no comma moves.
- AC11 — `grep -c '_build_design_fixture(' tools/memory-tree/gen_build_index.py` printed 3, and
  `grep -cF 'merge=ours\n"'` over the same file printed 1.
- AC12 — `grep -c 'as-built view cannot be rendered' help/commit-render.md` printed 1, and
  `grep -c 'puts back every file it wrote' help/commit-render.md` printed 1.
- Verdict parity — `probe8.py` over the base copy and the built generator gave the same exit code in
  every case: 1 for AC1, AC2, AC3 both halves, AC4 and AC6, and 0 for AC5, AC7 both halves and the
  clean render. What moved is only the tree a refusal leaves, which is the defect this unit closes.
  Over the scoped tree, every `--only 12 --spec` of tOne-1 to tOne-4, `--build tOne` and the tOne and
  tTwo lines of the unscoped run printed byte-identical output with and without the new edge cutoff.
- Timing — the clean `--write-staged` over `<f>`, the same command at base and after, one run at a
  time, the median of seven each, by `time8.py` in the run's scratch directory:
  base 0.554 s, after 0.516 s, each exit 0. <!-- PINNED 2026-11-14 -->
- Owed to the close: the four `New arm:` lines of §7, observed RED-first by the main loop — the
  `test_staged_write` arms for AC1 to AC3 at base, the AC4 to AC7 arms on their staged breaks, the
  tThree arms with `|| SCOPED` and then `| SCOPED` dropped, and the derived-key arm with the scoped
  conf's key dropped and on a producer copy planting an unset key; and the gate legs §7 lists.
