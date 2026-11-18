# TOOL-aTrimmedWait-19 acceptance ledger

**Serves:** journal TOOL-aTrimmedWait-19

No merge bar, no self-test suite and no `*.test.sh` ran in this pass. Every observation below was
made on node a, one command at a time, over the spec at rev-1, from the worktree root, on a pass
that started at `f92261bc6`. `$F` is `tools/memory-tree/check-memory-hygiene.test.sh` and `$R` is
`origin/main..HEAD`, as the spec's section 5 defines them; `origin/main` read `8eda4a5a0`. The
probes ran as scripts under the run's scratch directory, `$SCRATCH`, which read the suite as data.
The rename and the map re-render are commit `c3f2c4a64`; this ledger and the status flip ride the
commit after it.

## The criteria

**Evidences:** TOOL-aTrimmedWait-19
- AC1 — after step 1, `git grep -n derive_partition_lines -- tools/` printed nothing,
  `grep -c '^extract_hs_lines() { ' $F` printed 1, and `bash -n $F` exited 0. The suite spells
  `extract_hs_lines` 15 times on 9 lines, the counts the spec's evidence gives for the old name. <!-- PINNED 2026-11-18 -->
- AC2 — `cmp <(git show 3cecd39a0:$F | sed 's/derive_partition_lines/extract_hs_lines/g') $F`
  exited 0 silent, and `git diff --stat` over the step printed 9 insertions and 9 deletions in `$F` alone. <!-- PINNED 2026-11-18 -->
- AC3 — after step 1 and before step 2, `python tools/codebase-map/gen_map.py --check` exited 1;
  after `python tools/codebase-map/gen_map.py --write` it exited 0. Then
  `grep -c '"id": "extract_hs_lines"' memory/map/generated/symbols.json` printed 1,
  `git grep -c derive_partition_lines -- memory/map/` printed nothing, and
  `git status --porcelain -- memory/map/` listed only `memory/map/generated/symbols.json`, whose
  diff moved the one entry from `derive_partition_lines` to `extract_hs_lines`, file unchanged.
- AC4 — after `c3f2c4a64`, `python tools/lexicon/lexicon.py --merge-losses "$R"` from the repo
  root exited 0, printed no `merge-losses: LOSS` line, and printed the summary
  `merge-losses: graded=3 skipped=0 paths=180 losses=0 masked=0 restored=1 superseded=0 seconds=14.75`, <!-- PINNED 2026-11-18 -->
  so `losses=0` and `restored=1`.
- AC5 — after step 1,
  `python tools/check-spec-tokens.py --spec memory/builds/aTrimmedWait/spec/2026-11-15-spec-TOOL-aTrimmedWait-11.md --spec memory/builds/aTrimmedWait/spec/2026-11-16-spec-TOOL-aTrimmedWait-12.md`
  exited 0, grading both specs whatever their status, and
  `git diff --quiet 3cecd39a0 -- memory/builds/aTrimmedWait/spec/2026-11-15-spec-TOOL-aTrimmedWait-11.md memory/builds/aTrimmedWait/spec/2026-11-16-spec-TOOL-aTrimmedWait-12.md`
  exited 0.

## Before and after, on this node

The same command, `python tools/lexicon/lexicon.py --merge-losses "origin/main..HEAD"`, timed by
wall clock, one at a time with nothing else running:

| when | revision | exit | summary | wall |
|---|---|---|---|---|
| before | `f92261bc6` | 1 | `losses=1 restored=0`, one `merge-losses: LOSS 01aad174` line, `seconds=15.04` | 15.81 s <!-- PINNED 2026-11-18 --> |
| after | `c3f2c4a64` | 0 | `losses=0 restored=1`, no LOSS line, `seconds=14.75` | 15.29 s <!-- PINNED 2026-11-18 --> |

The verdict that moves is the one the spec's goal names: the loss at `01aad174` clears as
`restored`. No other count moved: `graded=3 skipped=0 paths=180 masked=0 superseded=0` both times.

The fixture, `bash "$SCRATCH/u19/probe.sh" before|after`, pulls the partition helper's one-line
definition from the suite (from `git show 3cecd39a0:$F` before, from the worktree after), defines
it under a neutral name, and grades the arms the partition block grades, over the producer's own
liveness and recomputed lines, rendered by `transition_audit.render_liveness` and `print_recomputed`, as the suite
renders them. Both runs printed the same seven verdicts, and `diff` over the two outputs, past the
line naming the helper, exited 0:

| fixture case | before | after |
|---|---|---|
| partition-equal (duplicates, blank lines, order and cache hits differ) | green | green |
| partition-missing-line | red | red |
| cold-warm-equal | green | green |
| merges-walked-differ | green | green |
| outside-check-26-kept | green | green |
| recomputed-set-aside | green | green |
| extra-line-differs | red | red |

The two red rows are the fixture's liveness: the helper's comparison can go red.

## Owed to the main loop

The spec's section 6 legs, `memory hygiene`, `spec tokens (a spec's own names resolve)`,
`recall floor`, `recall floor arms` and `codebase-map coverage + freshness`, run at the push
through `push-main.sh`. The spec declares no `New arm:` line, so no RED-first observation is owed.
