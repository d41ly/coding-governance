# TOOL-aPrunedIndex-20 — the tag plants of `tags bundle selftest` run on a bounded pool, graded in row order

**Status:** CLOSED · rev-2 · 2026-11-26 · node a · Tier-1 · base 3d6c1702 · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-26-build-TOOL-aPrunedIndex-20-1-acceptance-ledger.md](../build/2026-11-26-build-TOOL-aPrunedIndex-20-1-acceptance-ledger.md) | journal | — |
| [2026-11-26-build-TOOL-aPrunedIndex-20-deviation-1.md](../build/2026-11-26-build-TOOL-aPrunedIndex-20-deviation-1.md) | deviation | — |
| [2026-11-26-prompt-TOOL-aPrunedIndex-17-5-owner-waiver.md](../prompts/2026-11-26-prompt-TOOL-aPrunedIndex-17-5-owner-waiver.md) | research | TOOL-aPrunedIndex-17 |
| [2026-11-26-prompt-TOOL-aPrunedIndex-20-1-spec-brief.md](../prompts/2026-11-26-prompt-TOOL-aPrunedIndex-20-1-spec-brief.md) | research | TOOL-aPrunedIndex-17 |
| [2026-11-26-review-TOOL-aPrunedIndex-17-20-diff-review-round3.md](../reviews/2026-11-26-review-TOOL-aPrunedIndex-17-20-diff-review-round3.md) | diff-review | TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-3 TOOL-aPrunedIndex-4 TOOL-aPrunedIndex-5 TOOL-aPrunedIndex-6 TOOL-aPrunedIndex-7 TOOL-aPrunedIndex-8 TOOL-aPrunedIndex-9 TOOL-aPrunedIndex-10 TOOL-aPrunedIndex-11 TOOL-aPrunedIndex-12 TOOL-aPrunedIndex-13 TOOL-aPrunedIndex-14 TOOL-aPrunedIndex-15 TOOL-aPrunedIndex-16 TOOL-aPrunedIndex-17 TOOL-aPrunedIndex-18 TOOL-aPrunedIndex-19 TOOL-aPrunedIndex-21 TOOL-aPrunedIndex-22 TOOL-aPrunedIndex-23 |
| [2026-11-26-review-TOOL-aPrunedIndex-17-20-spec-audit-round1.md](../reviews/2026-11-26-review-TOOL-aPrunedIndex-17-20-spec-audit-round1.md) | spec-audit | TOOL-aPrunedIndex-17 |
| [2026-11-26-review-TOOL-aPrunedIndex-24-diff-review-round4.md](../reviews/2026-11-26-review-TOOL-aPrunedIndex-24-diff-review-round4.md) | diff-review | TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-3 TOOL-aPrunedIndex-4 TOOL-aPrunedIndex-5 TOOL-aPrunedIndex-6 TOOL-aPrunedIndex-7 TOOL-aPrunedIndex-8 TOOL-aPrunedIndex-9 TOOL-aPrunedIndex-10 TOOL-aPrunedIndex-11 TOOL-aPrunedIndex-12 TOOL-aPrunedIndex-13 TOOL-aPrunedIndex-14 TOOL-aPrunedIndex-15 TOOL-aPrunedIndex-16 TOOL-aPrunedIndex-17 TOOL-aPrunedIndex-18 TOOL-aPrunedIndex-19 TOOL-aPrunedIndex-21 TOOL-aPrunedIndex-22 TOOL-aPrunedIndex-23 TOOL-aPrunedIndex-24 TOOL-aPrunedIndex-25 TOOL-aPrunedIndex-26 PLAY-dClosedLoop-1 TOOL-aTwinnedPass-1 TOOL-dPlacedRequest-95 TOOL-dPlacedRequest-105 TOOL-dSettledStage-1 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/playbook/tag_bundle.py#run_selftest` runs each distinct plant of `SELFTEST_ROWS` one after
another, so the `tags bundle selftest` leg costs the sum of its plants. After this unit it runs them
four at a time and grades them in row order, so the leg costs near its slowest plant. Every verdict
and every printed byte stays the same for the same plant results. This is the pool that unit 17's
section 3 hands off, and the owner approved it as a second unit on 2026-11-26.

## 2. Scope (IN)

- **S1** — `tools/playbook/tag_bundle.py` gains `run_plant_process(plant)`. It returns the
  `subprocess.run` result of `gov_tag.py --fixture --plant <plant>`, with the arguments
  `run_selftest` passes today. When that call raises, it returns
  `subprocess.CompletedProcess(argv, None, stdout="", stderr=f"{type(exc).__name__}: {exc}")`, so the
  error is the plant's output. Both text fields are set, because the grading line reads
  `p.stdout + p.stderr` and the stdlib defaults `stdout` to `None`. Observed by AC3.
- **S2** — `run_selftest` collects the distinct plants of its rows in first-appearance order. It
  maps `run_plant_process` over them with `concurrent.futures.ThreadPoolExecutor(max_workers=4)`, and
  builds `runs` from `pool.map`'s results, which come back in input order. Each distinct plant runs
  once, in its own process. Observed by AC1.
- **S3** — The grading loop then runs as today over the rows in `SELFTEST_ROWS` order, reading
  `runs`. It prints each `arm ok` and `arm FAIL` line, a failing plant's indented output and the
  summary line with the bytes they have today. Observed by AC2 and AC3.
- **S4** — The bound is the one `max_workers=4` literal at the one pool call, the width of the docs
  leg's pool in `tools/govkit/selftest.py@daac944b:21214`. No constant, knob or conf key is added.
  `SELFTEST_ROWS`, which plants the leg runs and the leg's 300 s `ceiling` in `tools/gate-legs.json`
  do not change. Observed by AC4.
- **S5** — The main loop re-times the leg at the close, on the tree with units 17 and 20 together
  and on that tree with this unit's build commit reverted. On green it rewrites the
  `tags bundle selftest` rows of `tools/run-gates/selftest-budgets.txt` and
  `tools/run-gates/ceiling-evidence.txt` by unit 17's S6, and moves neither row up. A MONOTONE refusal
  there leaves the evidence row at its value from before the call. Observed by AC5.

## 3. Non-goals (OUT)

- Any edit to `tools/playbook/tag_index.py` or to a module in its import closure. On 2026-11-26
  `import_walk.derive_module_closure` printed nine modules for it, and `tag_bundle.py` is not one.
- Any edit to `tools/playbook/gov_tag.py`, which unit 17 owns. The two units' product-code files are
  disjoint, but both write `memory/map/generated/symbols.json` and the same two run-gates rows, and
  both re-version the same two `instruction_units` extractors. So this unit builds after unit 17's build
  commit, as the build README's build order says.
- The twin runner `tools/playbook/positional.py#run_selftest`, which runs `gov_tag.py --fixture --plant`
  plants with the same lazy `subprocess.run` and the same `out = p.stdout + p.stderr`. It keeps its
  serial runner. The brief scopes this unit to `tools/playbook/tag_bundle.py`, and the
  `tags positional selftest` row of `tools/run-gates/selftest-budgets.txt@d09d433d:147` reads 108 s
  under a 170 s budget, so no reading asks for a pool there.
- `tools/loop/position.py` and `tools/memory-tree/routed_commits.py`, which other sessions are landing.
- A per-plant timeout. The leg's `ceiling` bounds it today and still does.
- Printing each row as its plant finishes. Rows print after the pool returns, so an interactive run
  shows nothing until its slowest plant ends. Under the bar the leg's output is captured whole anyway.
- Charging the bar's pool more than one slot for this leg. Four processes in one bar slot is this
  unit's accepted risk, stated under section 4's "What it cannot see".

### Edges

- **consumes-from** `TOOL-aPrunedIndex-17` — AC5 runs after unit 17's AC8, on a tree holding unit 17's
  build, and writes the two rows by the procedure unit 17's AC8 spells. Without unit 17 built, AC5's
  readings and its row writes have nothing to stand on. The mechanism of S1 to S4 needs nothing from it,
  but this unit builds after unit 17's build commit, because the two write the same generated map and
  the same two run-gates rows.

## 4. Design

Today `run_selftest` starts each plant lazily inside its grading loop, the first time a row names it
(`tools/playbook/tag_bundle.py#run_selftest`). The edit moves the runs ahead of the loop:

```python
plants = list(dict.fromkeys(plant for plant, _rc, _want in rows))
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    runs = dict(zip(plants, pool.map(run_plant_process, plants)))
```

The loop body keeps its grading and printing lines and drops only its `if plant not in runs` branch.
A worker that raises would make `pool.map` raise on iteration and lose every other plant's result,
so `run_plant_process` catches `Exception` and returns a run whose `returncode` is `None`, whose
`stdout` is the empty string and whose `stderr` is the exception's line. That run
fails each row naming its plant, as `got rc=None` with the exception's line as its output, and the
other plants are graded as usual. Today the same exception ends the leg with a traceback. A
`KeyboardInterrupt` is not an `Exception` and still ends the leg.

Each plant makes its own scratch top with `tempfile.mkdtemp(prefix="gt")` in
`tools/playbook/gov_tag.py#run_fixture`. Its index lives in that fixture's git directory, so two
plants running at once share no file. None of the 13 plants the rows name reads a clock: the only
`time.monotonic` reads in `gov_tag.py` belong to `queued-writers`, which the leg does not run. Unit
17's held answers patch module attributes inside each plant's own process, so the pool cannot mix
them.

On 2026-11-26 unit 17's section 4 measured a scratch pool of four workers over its five plants at
109.3 s, against 223.6 s run one after another, a ratio near 0.49. (PINNED, 2026-11-26)

### What it cannot see

- A plant that someday writes a path shared with another plant. AC5's exit-0 readings observe today's
  13 plants together, and nothing catches a later plant that does.
- Oversubscription under the bar. The leg holds one slot of the bar's pool and starts up to four
  processes, as the govkit selftest leg already does.

### Migration

`tools/playbook/tag_bundle.py` is in the import closure of `instruction_units.py`, as
`import_walk.derive_module_closure` printed on 2026-11-26, through `gov_tag.py`. The edit therefore
re-versions the `instruction_units:extract_unit` and `instruction_units:extract_repo` extractors, and
each node re-parses their rows once, the cost unit 17's section 4 accepts for its own edit.

### Files touched (estimate)

- `tools/playbook/tag_bundle.py`
- `memory/map/generated/symbols.json`, regenerated by the codebase-map generator's `--write` for the
  new function
- the unit's acceptance ledger under `memory/builds/aPrunedIndex/build/`, one line per criterion
- by the main loop at the close, on AC5's green only: `tools/run-gates/selftest-budgets.txt` and
  `tools/run-gates/ceiling-evidence.txt`

### Alternatives rejected

- A named module constant or an environment knob for the width. The brief asks that the bound be
  declared once and that no second constant stand beside the one it reuses. The repository holds no
  shared width for a selftest pool: `tools/govkit/selftest.py` and `tools/policy/check_policy.py`
  each spell `max_workers=4` at their call. A knob would also be a new public surface.
- `GATE_REGEN_JOBS`. It is regen's knob, read by `tools/run-gates/regen.py#read_knob` against
  `DEFAULT_JOBS` at `tools/run-gates/regen.py@28f415f8:53`, and the playbook kit does not import the
  run-gates kit.
- `GATE_JOBS`. It is the bar's width. A leg reading it would give one bar knob a second meaning, and at
  width 8 this leg would start eight processes inside one bar slot.
- A shared pool helper under `tools/lib/`. The pool is three standard-library lines here. Extracting
  one helper for every such call site is a separate mechanism with its own adopters.
- `concurrent.futures.as_completed`. It yields in finish order, so the grading loop would need the
  rows re-sorted, where `pool.map` already returns them in input order.

## 5. Acceptance criteria

- **AC1** — When a probe script under the run's scratch puts `tools/playbook` on `sys.path`, imports
  `tag_bundle`, and replaces `subprocess.run` with a fake that records how many fakes are running at
  once, then calls `tag_bundle.run_selftest()`, it prints `calls=13 distinct=13 peak=4`. The fake
  sleeps `0.05 * (13 - i)` s for the plant at index `i`, so the first plant finishes last, and returns
  each row's wanted exit and line. `distinct` is computed from `tag_bundle.SELFTEST_ROWS` by the probe.
  Red when: the plants still run one at a time, so `peak=1`; the pool is unbounded, so `peak=13`; or
  a plant named by two rows runs twice, so `calls=14`.
  figure: DERIVED from `SELFTEST_ROWS` at observation time; 13 distinct plants over 14 rows on
  2026-11-26.
- **AC2** — When the AC1 probe also loads the parent commit's `tag_bundle.py`, written to the scratch
  by `git show <parent>:tools/playbook/tag_bundle.py` and loaded with `importlib.util`, and runs both
  modules' `run_selftest` under one fake with `contextlib.redirect_stdout`, the two captures are equal
  byte for byte and both return 0. Under a second fake that returns exit 1 and two output lines for
  `named-probe`, the captures are equal again, both return 1, and both hold the `arm FAIL  tag plant
  named-probe` line with the two lines indented under it.
  Red when: rows print in finish order, a failing plant's output is dropped, or the summary line moves.
- **AC3** — When the AC1 probe runs `tag_bundle.run_selftest()` under a fake that raises
  `OSError("probe")` for `released-rows` only, it returns 1. It prints `arm FAIL  tag plant released-rows`
  with `got rc=None`, then the indented line `OSError: probe`, then `FAIL — 1 of 14 tag plant rows failed`,
  and every other row prints `arm ok`.
  Red when: the exception escapes `run_selftest` as a traceback, or the plant's rows print `arm ok`.
- **AC4** — When `git grep -c "max_workers" -- tools/playbook/tag_bundle.py` runs on the built tree it
  prints `tools/playbook/tag_bundle.py:1`. `git diff --name-only <parent> <build commit>` names
  `tools/playbook/tag_bundle.py` and none of `tools/playbook/tag_index.py`, `tools/playbook/gov_tag.py`,
  `tools/gate-legs.json`, `tools/playbook/positional.py`, `tools/loop/position.py` or
  `tools/memory-tree/routed_commits.py`. The AC2
  probe prints `rows same: True` for the two modules' `SELFTEST_ROWS`.
  Red when: a second width is declared, `SELFTEST_ROWS` changes, or the diff touches a cut-line file.
- **AC5** — When the main loop, at the close and after unit 17's AC8, times
  `python tools/playbook/tag_bundle.py --selftest` three times on a detached worktree under
  `"$TEMP/pi20-base"` at the tip with this unit's build commit reverted, and three times on the tip,
  back to back in one session with unit 17's AC7 gauge beside each, the ledger records the six
  readings and the six gauges. The reverted tree holds unit 17 and not this unit. AC5 is green when
  all four hold: every reading exits 0 and prints `PASS — the tag plants, 14 rows`, under the leg's
  300 s `ceiling` in `tools/gate-legs.json`; the largest gauge is at most 1.5 times the smallest; the
  worst reading after over the worst reading before is at most 0.75; and the worst reading after is at
  most 106 s. A set whose gauges fall outside that band is retaken, at most twice. On green the main (PINNED, 2026-11-26)
  loop runs the call unit 17's AC8 spells, with this AC's worst reading after, and only where that
  reading is lower than the node-a row as it then stands. Where it is not, neither row is written, and
  that is not red. Before anything else,
  the call's `--reset` deletes the leg's non-ok rows from the retained run files under
  `<git-dir>/gate-run/`. A retained ok reading at or above the worst after makes the call exit 1 with
  its MONOTONE line before it writes the evidence file, and the evidence row then keeps its value
  from before the call. The main loop then derives the budget value by unit 17's AC8 rule, 1.5 times
  the node-a row as the call leaves it, floored at 60. It writes the budget row only after testing that
  the value is lower than the row as it then stands.
  On red it writes neither row and records the readings, the gauges and the failed condition. On either
  verdict the ledger records the diff of the other legs' rows, which every `--write` re-derives.
  Red when: a reading exits non-zero, fails a row, or reaches the ceiling; the gauges stay out of
  band; the ratio exceeds 0.75; the worst reading after exceeds 106 s; or the `tags bundle selftest`
  row of either file reads higher after the write than before it. Another leg's row moving is not red.
  permission: a pass runs no self-test leg, so the readings and both writes are the main loop's.
  cost: six readings of the leg. At a 0.21 s gauge the reverted tree runs the five plants one after
  another in no less than unit 17's section 4 sum of 157.7 s, and the tip near 0.49 of that, about
  77 s, from section 4's pool ratio. The six readings take at least about 12 minutes, plus the eight
  `bundle-*` plants, which nothing has timed. The cost scales with the gauge. At that gauge the 106 s
  bound is reachable only if the eight `bundle-*` plants add under about 29 s to a pooled reading.
  figure: the readings are DERIVED at observation time. The 0.75 bound is PINNED: it leaves the
  section 4 pool ratio of 0.49 room for the eight `bundle-*` plants, which nothing has timed under a
  pool.

## 6. Gates

`tags bundle selftest` · `tags (the resolver's checks)` · `instruction units selftest` · `instruction edits (manifest checks)` · `edges (every declared edge parses, is registered and resolves)` · `lexicon naming predicates` · `playbook render selftest` · `govkit acceptance matrix` · `policy fixtures` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `every held leg is budgeted, every budget row resolves` · `leg ceilings clear their evidenced maximum` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

`tags (the resolver's checks)`, `instruction units selftest`, `instruction edits (manifest checks)` and
`edges (every declared edge parses, is registered and resolves)` are owed because the edit re-versions
two `instruction_units` extractors, as unit 17's section 7 owes them for the same re-version. They are
the four legs that open the live index, so they are owed at the close once the owner's go holds, and by
no pass before it. `playbook render selftest`, `govkit acceptance matrix` and `policy fixtures` guard
`tools/playbook/tag_bundle.py`. The four after the map legs read the two rows AC5 may write.

New arm: tools/playbook/tag_bundle.py · covers AC2 · one `SELFTEST_ROWS` row's wanted line edited to a string its plant never prints, so the leg under the pool prints that plant's output and exits 1 · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-26 · initial draft.
- rev-2 · 2026-11-26 · §2 §3 §4 §5 §6 §9 S1 S5 AC4 AC5 · folded
  `2026-11-26-review-TOOL-aPrunedIndex-17-20-spec-audit-round1`: findings 5, 13 and 22 (the fallback
  sets `stdout=""` beside its stderr), 3 and 17 (the "may build concurrently" sentence struck; this
  unit builds after unit 17's build commit, and the edge says so), 9 and 20 (AC5 and S5 say the
  `--reset` deletes the leg's non-ok run rows before any refusal, and a MONOTONE refusal leaves the
  evidence row as it stood), 2 (the budget value derives from the evidence row as the call leaves it,
  and each write follows the test it can trip), 10 (the worktree spelled `"$TEMP/pi20-base"`), 11
  (AC5's cost derived from unit 17's timed sums and the pool ratio, with what makes 106 s reachable),
  14 (the twin runner in `tools/playbook/positional.py` named in §3 and §9 and kept serial, with
  AC4's cut line holding it), 15 (the WONTDO ask no longer cited; the bar-slot risk is this unit's,
  accepted), 18 (the `tags` and `edges` legs owed, under unit 17's timing sentence), 23 (AC5's red
  scoped to the `tags bundle selftest` row of either file).

## 9. Reuse audit

The seam extended is `tools/playbook/tag_bundle.py#run_selftest`, and the pool shape is the one
`tools/govkit/selftest.py@daac944b:21214` already uses for the docs leg's plants:
`ThreadPoolExecutor(max_workers=4)` with `pool.map`, read back in case order. The probe
`python tools/codebase-map/reuse_lookup.py "run fixture plant subprocesses on a bounded thread pool and grade them in row order"`
ranked name-stem neighbours only, `run`, `fixture`, `run_git` and `run_selftest_cases` among them, and
none is a pool. `git grep -n "max_workers"` over `tools/` found the same literal at its call in
`tools/govkit/selftest.py` and `tools/policy/check_policy.py`, and `regen.py`'s pool reading its own
knob, so no shared width exists to reuse. A grep for the call shape the edit changes,
`git grep -n -- '"--fixture", "--plant"' -- 'tools/*.py'`, found one twin that runs `gov_tag.py`
plants: `tools/playbook/positional.py#run_selftest`, at `tools/playbook/positional.py@3bbaecc5:750`.
Section 3 records why it keeps its serial runner. The recall answered unit 17's section 4 pool
measurement first, then `TOOL-aTimedTurnstile-5`, whose audit found no shell concurrency seam.
Recall terms used: selftest plant fixture ThreadPoolExecutor max_workers pool row order leg ceiling budget concurrency
