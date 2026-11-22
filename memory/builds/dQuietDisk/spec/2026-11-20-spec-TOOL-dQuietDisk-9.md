# TOOL-dQuietDisk-9 — every scratch path under one owned, swept root, and every tree removed by one chmod-and-retry helper

**Status:** SPECCED · rev-4 · 2026-11-22 · node d · Tier-2 · base e4699ee7 · streams tooling · order 6 · closes TOOL-dQuietDisk-27

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md) | research | TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-reground-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-reground-task.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-14 TOOL-dQuietDisk-19 |

<!-- /gen:spec-records -->

## 1. Goal

A killed suite or runner leaves its scratch behind, and a Python removal that swallows its error
leaves git's read-only objects in the temp folder on Windows
(`memory/builds/dQuietDisk/build/2026-11-20-build-TOOL-dQuietDisk-19-analysis.md`, §8 and rework
K12). This unit gives Python one removal helper and one owned-root helper, gives bash the bar's own
owner record and dead-owner sweep as one shared block, moves every swallowing removal onto the
helper, and adds a lint that reds a new one. It also closes the two gaps ask TOOL-dQuietDisk-27
records in the bar's owned root: a native Windows child reads `TEMP` and `TMP`, which the runner
does not redirect, and a bar nested under an adopter runner's own owned `TMPDIR` counts and sweeps
that scratch instead of the real temp root.

## 2. Scope (IN)

- **S1** — `tools/lib/owned_scratch.py`, the canonical module, holding two marked blocks.
  `remove_tree_py` defines `remove_tree(path)` and `build_scratch_dir()`. `remove_tree` calls
  `shutil.rmtree` with an `onexc` hook that clears the read-only bit on the failing path and retries
  it once, never raises, and returns whether the path is gone. `build_scratch_dir()` is a
  `contextlib.contextmanager` generator over `tempfile.mkdtemp()` whose exit calls `remove_tree`, so
  no `__enter__` or `__exit__` is defined, which the lexicon would grade as functions. `onexc` alone is used, because the
  declared python floor is 3.15, the value `tools/lib/python-floor.txt` holds at `609cd40b1`.
  Observed by AC1.
- **S2** — The block `owned_tempdir_py` defines `init_owned_tempdir()`. When the process's temp dir
  sits inside a `gate-work.*` directory holding an `owner` file, it sets `tempfile.tempdir` to that
  temp dir and returns it. Otherwise it first sweeps each `gate-work.*` under the temp dir whose
  owner line names a `py:` pid that is not alive and this repository's git common dir. It then
  makes its own `gate-work.*` with an owner line `py:<pid>TAB<common dir>TAB<epoch>`, written
  tmp-then-rename, sets `tempfile.tempdir` to its `tmp`, exports `TMPDIR`, `TEMP` and `TMP` as that
  `tmp` so the suite's child processes land there too, and registers `remove_tree` of it at exit.
  A pid that cannot be judged reads as alive. Observed by AC2 and AC3.
- **S3** — Every `shutil.rmtree(..., ignore_errors=True)` and every
  `TemporaryDirectory(..., ignore_cleanup_errors=True)` under `tools/`, `skills/` and `.githooks/`
  moves to `remove_tree` and `build_scratch_dir`. Every hand-written chmod-and-retry hook in those trees
  moves to `remove_tree` too. A gov-internal file imports the canonical module; a file a kit ships
  carries the blocks inline. Each Python suite entry point in that population calls
  `init_owned_tempdir()` before its first scratch. Observed by AC4 and AC5.
  **Readers:** by name: `remove_tree`, which `tools/loop/loop_witness.py` calls through the
  memory-tree kit's `deviation_join` and which the inline block keeps; each local hook's other
  callers sit in its own file and call `remove_tree` after the move ·
  by value: NO VALUE READERS — no caller reads a removal's result today, and S1's return is new.
- **S4** — The bash face, the canonical block `owned_work_sh` in `tools/lib/owned-scratch.sh`. It
  defines `write_work_owner <dir> <common>` and `scan_dead_work <ambient> <own dir> <common>`, lifted
  from `run-gates.sh`'s two functions with their globals made arguments. The block calls
  `derive_temp_path`, `ts_alive` and `add_health_event` and defines none of them, as the runner's
  body does today, so the owner write keeps its unpredictable staging name. `run-selftests.sh`
  already carries `health_log_sh` and gains the two one-line helpers the runner holds
  (`tools/run-gates/run-gates.sh@e4699ee75:962`, `:1828`). `run-gates.sh` carries the block in
  their place and calls it with `$WORK`, the swept root S8 names and `$WORK_COMMON`, so its lines
  and health events are unchanged. `run-selftests.sh` carries it too: its sweep root becomes
  `mktemp -d "${TMPDIR:-/tmp}/gate-work.XXXXXXXX"` with an owner line, and it calls
  `scan_dead_work` before its first row. Observed by AC6 and AC7.
- **S5** — Two `PARITY_ROWS` rows join `tools/lib/resolve-python.test.sh`, one per Python block, and
  a third for `owned_work_sh`. Observed by AC8.
- **S6** — The lint. `tools/gate-lint/encoding_posture.py` gains a mode `--cleanup` whose arm,
  `cleanup`, keys a site `<path>` `cleanup` for each AST call S3 names, read across lines. It uses
  the file's own population walk, `--measure`, ledger adapters and `--selftest`, whose
  `FLOOR_ASSERTIONS` rises by the rows added. Its registry is `memory/project/cleanup-sites.txt`,
  a shrink-only ledger with the header the encoding-posture ledger carries, holding a row only for a
  site a reviewer waives with a reason. A leg runs it over `tools`, `skills` and `.githooks`.
  Observed by AC9.
- **S7** — Native children (ask TOOL-dQuietDisk-27, gap 1). Where `run-gates.sh` exports `TMPDIR`
  as `$WORK/tmp` before the first leg, it exports `TEMP` and `TMP` to the same value, spelled as
  `mktemp -d` returned it. MSYS converts all three for a native child, so a native node or python
  leg's temp lands inside the owned root. `run-selftests.sh` sets the same three where it sets a
  row's `TMPDIR`. Observed by AC10.
- **S8** — The outer ambient root (ask TOOL-dQuietDisk-27, gap 2). An adopter runner that already
  redirects `TMPDIR` to its own owned scratch exports `GATE_OUTER_AMBIENT_TMP`, the temp root it
  was itself started under. When that variable is non-empty and names a directory, `run-gates.sh`
  takes it as its swept root, `RG_SWEPT_TMP`: the `TMPDIR entries` count and `tmpdir_entries`
  record read it, and `scan_dead_work` sweeps it. The bar's own `gate-work.*` is still made under
  `${TMPDIR:-/tmp}`, inside the outer runner's scratch, as today. When the variable is unset or
  empty, the swept root is `$GATE_AMBIENT_TMP` and nothing changes. When it names no directory,
  the runner prints one NOTE line naming it and keeps today's root. The runner reads it once and
  unsets it before any leg dispatches, so a bar nested inside a leg never inherits it. The name
  joins `BAR_INERT_KNOBS` in `.githooks/pre-push.test.sh` with its reason line, and the run-gates
  README's scratch section names it. Observed by AC11 and AC12.

## 3. Non-goals (OUT)

- No bash `rm -rf` rewrite. MSYS `rm -rf` removes git's read-only objects, and the bash leaks
  dSweptScratch measured were bookkeeping it fixed (TOOL-dSweptScratch-1, §4).
- No new sweeper. A bash-owned root is swept by `scan_dead_work`, a Python-owned one by the next
  `init_owned_tempdir()`. Each judges only its own pid kind: bash's `kill -0` cannot judge a
  Windows pid, so `py:` lines are skipped by the bash scan, whose `case` already refuses a
  non-numeric pid (`tools/run-gates/run-gates.sh#scan_dead_work`).
- No cleanup ledger seeded with today's sites. S3 moves every one, so the ledger starts with its
  header and no row.
- The other G-C lint clauses: `git init` outside the template helper, a spawn inside a loop body,
  `copytree` of a kit, `clone --no-hardlinks` and an unrooted `mktemp`. They are TOOL-dQuietDisk-23.
- No kit version bump by hand: `govkit.py mint` writes every owed bump at the lander.
- No policy key. Removing a tree and owning a root save no answer, so the cache rule does not reach
  them, and their off value would be a leak. `GATE_OUTER_AMBIENT_TMP` is not a switch either: it
  names a directory an outer runner holds, and unset is today's behaviour.
- No outer-root read in the Python face. `init_owned_tempdir()` nests inside whatever owned
  `TMPDIR` it is given and removes its own root at exit, so the root it sweeps is the one it sits in.
- No move of where a bar makes its own `gate-work.*`. Under an adopter runner it stays inside that
  runner's scratch, which the runner removes.
- No edit in incms. Its `scripts/gate.sh` exporting the variable is that repository's change.

### Edges

- **hands-off** external — incms `scripts/gate.sh` exports `GATE_OUTER_AMBIENT_TMP` as the temp
  root it started under, in that repository under its own governance, once a minted run-gates kit
  carrying S8 reaches it through `govkit update`

## 4. Design

### Where the code was read

Code at `e4699ee75`, the build base: the merge that brought dWitnessedBar's land tip `ed833f684`
into this run, as the owner ruled on 2026-11-22. It holds both lines rev-1 read separately,
dWitnessedBar's and main's with TOOL-dSweptScratch-1. A citation is by symbol or
`<path>@e4699ee75:<line>`.

### The population, read over the real tree first

The predicate: an AST `Call` whose callee is named `rmtree` with the keyword `ignore_errors=True`,
or `TemporaryDirectory` with `ignore_cleanup_errors=True`, over every tracked `*.py` under `tools/`
and `skills/`. The first two rows were run on 2026-11-20:

| Tree | `rmtree` sites | `TemporaryDirectory` sites | Files | Of them, shipped by a kit |
|---|---|---|---|---|
| `609cd40b1` | 59 | 11 | 33 | 22 files, 40 sites [PINNED] |
| HEAD `a5537b925` | 35 | 11 | 15 | 12 files, 26 sites [PINNED] |
| base `e4699ee75` | 45 | 11 | 21 | 16 files, 34 sites [PINNED] |

The 11 `TemporaryDirectory` sites are all in `tools/govkit/upgrade_steps.py` (10) and
`tools/govkit/selftest.py` (1). A line grep finds 57 and 12 at `609cd40b1`; the AST reads a call
split across lines, which the grep misses. "Shipped" is `python tools/govkit/govkit.py shipped`, run at
`a5537b925` for the first two rows and at `e4699ee75` for the third. The `e4699ee75` row was read on
2026-11-22 over `tools/`, `skills/` and `.githooks/`, which holds none. The merge of dWitnessedBar's
land tip added ten `rmtree` sites over `a5537b925`, among them
`tools/run-gates/verdict_flow.py`, `tools/run-gates/leg_factory.py` and
`tools/run-gates/verdict_backends.py`. The hand-written hooks, `git grep -nE "onexc|onerror"` at
`e4699ee75`, sit in 23 files [PINNED], among them `tools/memory-tree/deviation_join.py#remove_tree`,
`tools/govkit/upgrade_walk.py#remove_tree`, `tools/govkit/step_gate.py` and
`tools/lib/commit_trailers.py`. The builder re-runs the predicate at the pass's own base with
`--cleanup --measure` and moves what it prints. figure: DERIVED at the pass's base; the table is
PINNED at the three shas named.

### The copy rule

`tools/lib/` ships nothing (`tools/govkit/registry.toml@e4699ee75:253`), so a shipped file carries
the block inline between `# >>> remove_tree_py — canonical copy: owned_scratch.py in gov's lib dir`
and `# <<< remove_tree_py`, as `common_dir.py`'s copies do (`tools/lib/common_dir.py`), and the
parity table holds each copy to the canonical block (`tools/lib/resolve-python.test.sh@e4699ee75:405`).
`deviation_join.remove_tree` keeps its name because `loop_witness.remove_tree` calls it.

### The owner line both faces read

```text
<pid>\t<git common dir>\t<start epoch>      bash: an MSYS pid, judged by kill -0
py:<pid>\t<git common dir>\t<start epoch>   python: a native pid, judged by the OS
```

The Python liveness check is `os.kill(pid, 0)` on POSIX and `OpenProcess` with
`GetExitCodeProcess` on Windows. Any error is "alive", the direction that keeps a directory.

### The two gaps of ask TOOL-dQuietDisk-27

The owned-root block sits at `tools/run-gates/run-gates.sh@e4699ee75:2399-2465`, byte-identical to
its body at `609cd40b1` and only moved. It sets `GATE_AMBIENT_TMP=${TMPDIR:-/tmp}`, makes `$WORK`
there, sweeps `"$GATE_AMBIENT_TMP"/gate-work.*`, counts `"$GATE_AMBIENT_TMP"/*` into
`TMPDIR_ENTRIES` and exports only `TMPDIR` (`:2465`). The incms session measured both gaps
(`memory/builds/dQuietDisk/BACKLOG.md`, ask TOOL-dQuietDisk-27): `os.tmpdir()` in a native node
child returned `%TEMP%` until `TEMP` and `TMP` were exported too, and under incms `scripts/gate.sh`
the count and the sweep read incms's fresh scratch.

```bash
GATE_AMBIENT_TMP=${TMPDIR:-/tmp}                 # unchanged: where $WORK is made
RG_SWEPT_TMP=$GATE_AMBIENT_TMP                   # what the count and the sweep read
if [ -n "${GATE_OUTER_AMBIENT_TMP:-}" ]; then
  if [ -d "$GATE_OUTER_AMBIENT_TMP" ]; then RG_SWEPT_TMP=$GATE_OUTER_AMBIENT_TMP
  else echo "run-gates: NOTE - GATE_OUTER_AMBIENT_TMP names no directory, so the bar counts and sweeps $GATE_AMBIENT_TMP" >&2; fi
fi
unset GATE_OUTER_AMBIENT_TMP
# ... scan_dead_work "$RG_SWEPT_TMP" "$WORK" "$WORK_COMMON"; the count globs "$RG_SWEPT_TMP"/*
export TMPDIR="$WORK/tmp" TEMP="$WORK/tmp" TMP="$WORK/tmp"
```

Under an outer root the count no longer includes this bar's own dir, which sits in the outer
runner's scratch; two nested bars over one unchanged outer root still print one figure. The
variable's name was checked with `python tools/lexicon/lexicon.py --suggest GATE_OUTER_AMBIENT_TMP
--as constant`, which answers that the declaration carries no `constant` cell (its declared cells
are `js.function`, `js.type`, `py.function`, `py.type` and `sh.function`). So no lexicon cell grades
an environment name, and the runner's knob census is its one grader: every `GATE_` name the runner
reads must sit in exactly one class (`.githooks/pre-push.test.sh@e4699ee75:1940`). It is inert there
because it moves only a count and a sweep that needs a dead owner of this repository, never a leg
or a verdict. `GATE_AMBIENT_TMP` itself stays as that census classes it, assigned in the runner.

### Inventory

| Minted identifier | Kind | Naming cell | Graded by |
|---|---|---|---|
| `remove_tree_py`, `owned_tempdir_py`, `owned_work_sh` | parity block markers | `PARITY_ROWS` | `tools/lib/resolve-python.test.sh` |
| `remove_tree`, `build_scratch_dir`, `init_owned_tempdir` | Python functions | `py.function`, lexicon `--suggest` OK | the probes of section 6 |
| `write_work_owner`, `scan_dead_work` | shell functions, lifted under their names | `sh.function`, lexicon `--suggest` OK | the probes of section 6 |
| `--cleanup`, arm `cleanup` | scanner mode and arm | the scanner's `ARMS` tuples | its `--selftest` |
| `cleanup-sites` | ledger population | `.memory-tree.conf` `PROJECT_REGISTRY_EXTRA` | `memory hygiene` |
| `cleanup posture (a tree removal that swallows its error)` | gate leg | `tools/gate-legs.json` | `run-gates canary` |
| `GATE_OUTER_AMBIENT_TMP` | environment variable an outer runner exports | `BAR_INERT_KNOBS` | `pre-push self-test`'s knob census |
| `RG_SWEPT_TMP` | runner variable | none | the fixture bars of section 6 |

### Files touched (estimate)

`tools/lib/owned_scratch.py` · `tools/lib/owned-scratch.sh` · `tools/lib/resolve-python.test.sh` ·
`tools/run-gates/run-gates.sh` · `tools/run-gates/run-selftests.sh` ·
`tools/gate-lint/encoding_posture.py` · `memory/project/cleanup-sites.txt` · `.memory-tree.conf` ·
`tools/gate-legs.json` · `memory/guides/SESSION-KICKOFF.md` · `.githooks/pre-push.test.sh` ·
`tools/run-gates/README.md`

Plus every file the predicate and the hook grep name at the pass's base. At `e4699ee75` those are
42 files [PINNED]:

`.githooks/pre_push_bar_selftest.py` · `tools/branch-reconcile/selftest.py` ·
`tools/govkit/fixture_target.py` · `tools/govkit/selftest.py` · `tools/govkit/step_gate.py` ·
`tools/govkit/steps/conf_pins_to_ledger.py` · `tools/govkit/steps/kickoff_facts_to_overlay.py` ·
`tools/govkit/steps/registry_to_ledger.py` · `tools/govkit/upgrade_steps.py` ·
`tools/govkit/upgrade_walk.py` · `tools/lexicon/selftest.py` · `tools/lib/commit_trailers.py` ·
`tools/loop/claims.py` · `tools/loop/factories.py` · `tools/memory-recall/check-recall.py` ·
`tools/memory-recall/query.py` · `tools/memory-recall/selftest.py` ·
`tools/memory-recall/test_recall_floor.py` · `tools/memory-tree/commit_trailers.py` ·
`tools/memory-tree/convert_registry.py` · `tools/memory-tree/deviation_join.py` ·
`tools/memory-tree/gen_build_index.py` · `tools/memory-tree/ratchet.py` ·
`tools/playbook/check_layers.py` · `tools/playbook/edge_grammar.py` ·
`tools/playbook/fixtures/composition.py` · `tools/playbook/gov_tag.py` ·
`tools/playbook/load_sets.py` · `tools/playbook/writing_practice.py` ·
`tools/policy/check_policy.py` · `tools/process-monitor/selftest.py` ·
`tools/run-gates/check-receipt.py` · `tools/run-gates/held_halves.py` ·
`tools/run-gates/leg_factory.py` · `tools/run-gates/measure_legs.py` ·
`tools/run-gates/owed_rows.py` · `tools/run-gates/product_tests.py` ·
`tools/run-gates/verdict_backends.py` · `tools/run-gates/verdict_flow.py` ·
`tools/runlog/selftest.py` · `tools/unattended/commit_trailers.py` · `tools/unattended/fix_keeps.py`

The kickoff manifest's `watch:` line names `tools/run-gates/run-gates.sh`,
`tools/run-gates/run-selftests.sh`, `tools/gate-legs.json` and `.memory-tree.conf`, so the commit
that stages them re-stamps the manifest's `last-audit`.

### Alternatives rejected

| Alternative | Why it loses |
|---|---|
| A shared module the kits import from `tools/lib/` | No adopter has `tools/lib/`; a shipped file importing it fails on arrival, the class the check-line-length descriptor records. |
| A new scanner file beside `encoding_posture.py` | It would copy the population walk, `--measure` and the ledger adapters, which the existing modes already share. |
| A registry seeded with today's sites | S3 moves them all, and a seeded registry is a ratchet that never drains. |
| One sweeper for both pid kinds in bash | MSYS `kill -0` reads a native pid as dead and would remove a live Python suite's root. |
| `onerror` below 3.12 | The floor is 3.15, so the branch would be dead code. |

## 5. Production-readiness checklist

- security: removal stays inside directories the run made or a dead owner of this repository made,
  matched by common dir as `scan_dead_work` matches today. An unreadable or foreign owner line is
  never swept. `GATE_OUTER_AMBIENT_TMP` moves which directory the sweep lists, never its predicate,
  so an exported value can only remove a dead bar's `gate-work.*` of this repository.
- perf / scale: `init_owned_tempdir` lists the temp dir's `gate-work.*` entries once per suite;
  the glob reads names, not every entry's metadata.
- error / empty / loading states: a removal that still fails returns False and raises nothing, as
  `ignore_errors` did; the root it sits in is swept later.
- observability: the bash sweep keeps its `sweeping the scratch of a dead bar` line and health event.
  The Python sweep prints one stderr line per root it removes, before the suite's first output.
- risks: a removal is the only write a cleanup site makes, so moving it moves no suite verdict;
  AC5 observes it. The gotcha `append-without-an-idempotence-key` applies to the owner write, which
  is tmp-then-rename.
- testing: the probes of section 6 and the scanner's `--selftest`.
- migration: N/A — no stored data; a root left by a run before this unit has no owner and is never
  swept, as today.
- user docs: no page under `help/` names a cleanup call or a scratch root. The kit README's
  scratch section, `tools/run-gates/README.md` "The scratch directory — owned, redirected and
  swept", gains `TEMP` and `TMP` beside `TMPDIR` and a paragraph on `GATE_OUTER_AMBIENT_TMP`: who
  exports it, what it moves, and that unset is today's behaviour.

## 6. Acceptance criteria

- **AC1** — When a probe under `%TEMP%/<short-name>` makes a repository with a commit, so its
  `.git/objects` hold read-only files, and calls `remove_tree` on it, the call returns True and the
  path is gone. With the hook's `os.chmod` deleted, the path survives and the call returns False
  without raising.
  Red when: the read-only objects survive, or a failure raises.
- **AC2** — When a probe runs with `TMPDIR` inside a planted `gate-work.x/tmp` holding `gate-work.x/owner`,
  `init_owned_tempdir()` returns that `tmp` and makes no directory. Run with an ambient `TMPDIR`, it
  makes one `gate-work.*` holding an owner line that starts `py:`, a child `python -c` it starts
  prints that root's `tmp` for each of `TMPDIR`, `TEMP` and `TMP`, and the directory is gone after
  the process exits.
  Red when: a nested run makes a second root, a direct run's root outlives it, or a child reads
  the ambient temp dir.
- **AC3** — When a probe plants, under one ambient dir, a root owned by a dead `py:` pid of this
  repository, one by a live `py:` pid, one by a dead `py:` pid of another common dir, and one by a
  bash pid, and calls `init_owned_tempdir()`, only the first is removed.
  Red when: a live, foreign or bash-owned root is removed.
- **AC4** — When `python tools/gate-lint/encoding_posture.py --cleanup --measure . tools skills .githooks`
  runs at the unit's tip, it prints no `cleanup` line. Run over a fixture tree holding one planted
  `shutil.rmtree(p, ignore_errors=True)` split over two lines, it prints one `cleanup` line naming
  that file. When the main loop runs the new leg, the graded run with the registry argument, at the
  close, it exits 0 at the tip and 1 with the planted call.
  Red when: a split call is missed, or a site survives the move.
  permission: the graded run is the new leg's own argv, owed to the main loop (scratch-guard row
  G1); the pass makes the `--measure` runs.
- **AC5** — When every Python file S3 touched compiles under `python -m py_compile`, and AC2's probe
  shows a child's temp landing in the owned root, the pass's half holds. When the main loop runs
  each suite S3 touched at the close, in a scratch `git clone --shared` of gov with `TEMP`, `TMP`
  and `TMPDIR` pointed at an empty directory, it prints the same arm lines and exit code as at the
  build's base, and the directory holds 0 entries after it exits. The unattended kit's suites are
  excluded, as the owner's rule of 2026-08-23 requires.
  Red when: an arm's result moves, or an entry remains.
  cost: the touched suites run in full once each, some for minutes.
  figure: DERIVED at observation; the residual at the build's base is recorded beside it.
  permission: a role agent runs no suite (scratch-guard row G3), so the suite runs are owed to the
  main loop; the pass makes the compile check and the probe.
- **AC6** — When a bash probe sources `owned-scratch.sh` from `tools/lib/`, plants a `gate-work.*`
  whose owner names a dead MSYS pid and this common dir, one naming a live pid, and one whose owner
  starts `py:`, and calls `scan_dead_work`, only the first is removed and the sweep line names its
  pid.
  Red when: the `py:` root or the live one is removed.
- **AC7** — When a bash probe that sources the block makes a `gate-work.*` root, calls
  `write_work_owner` on it and is killed with `kill -9`, the root remains with its owner line, and a
  second probe's `scan_dead_work` over the same ambient dir sweeps it. When
  `grep -n "scan_dead_work\|gate-work" tools/run-gates/run-selftests.sh` runs, it prints the sweep
  root's `mktemp` line and a `scan_dead_work` call above the row loop.
  Red when: the killed root survives the second scan, or the sweep root is not an owned
  `gate-work.*`.
- **AC8** — When the parity table's `blk` awk extracts each new block from the canonical file and
  from every copy, every pair compares equal, and the runner carries `write_work_owner` as the
  inline block.
  Red when: a copy drifts by one byte, which the new `PARITY_ROWS` rows then report.
- **AC9** — When the main loop runs `python tools/gate-lint/encoding_posture.py --selftest` at the
  close, it prints its count line at or above the raised `FLOOR_ASSERTIONS` and exits 0. With the
  `--cleanup` arm's keyword test inverted, it exits 1.
  Red when: the new mode's rows do not execute.
  permission: a role agent runs no `--selftest` (scratch-guard row G3); this is the first `New
  arm:` line's RED and GREEN observation, owed to the main loop. The pass's proxy is AC4's
  `--measure` runs.

- **AC10** — When a bash probe under `%TEMP%/<short-name>` takes the edited runner's
  `export TMPDIR=` line, the one that also exports `TEMP` and `TMP`, sets `WORK` to a planted
  `gate-work.x` holding `tmp`, evaluates the line and starts
  `node -e "process.exit(require('os').tmpdir().includes('gate-work.') ? 0 : 1)"` from Git Bash,
  the child exits 0. With `TEMP` and `TMP` taken out of the line, the same child exits 1. When
  `grep -n "TEMP=" tools/run-gates/run-selftests.sh` runs, it prints the row launch line, setting
  `TEMP` and `TMP` beside `TMPDIR`. When the main loop runs a fixture bar at the close, in the
  shape the runner's own suites build one, whose one leg is that `node -e` line, the leg passes, and
  it is red with the export deleted from the fixture's copy of the runner.
  Red when: a native child's `os.tmpdir()` still answers the ambient `%TEMP%`.
  fixture: a host with `node` on `PATH`, as gov's hooks already require.
  permission: a role agent runs no runner, a fixture copy included (scratch-guard row G2), so the
  fixture bar is owed to the main loop; the pass makes the probe.
- **AC11** — When a bash probe takes the edited runner's outer-root read, extracted as AC10 takes
  its line, and evaluates it with `GATE_OUTER_AMBIENT_TMP` naming an outer root A, `RG_SWEPT_TMP`
  reads A and the variable is unset after it; unset, `RG_SWEPT_TMP` reads `$GATE_AMBIENT_TMP`; and
  naming a missing directory, it prints the NOTE line and reads `$GATE_AMBIENT_TMP`. A second probe
  sourcing `owned-scratch.sh` and calling `scan_dead_work` over A, holding a planted
  `gate-work.dead` whose owner names a dead MSYS pid and the probe's git common dir, sweeps it. When
  the main loop runs the fixture bar of AC10 at the close with A holding `gate-work.dead` and two
  other entries, `TMPDIR` at an empty directory B and the variable exported as A, the sweep line
  names the planted pid, `gate-work.dead` is gone, the bar prints `TMPDIR entries 2`, its one leg,
  `bash -c '[ -z "${GATE_OUTER_AMBIENT_TMP+x}" ]'`, passes, and its own `gate-work.*` was made
  under B. Run again with the variable unset, the planted dir survives and the bar prints
  `TMPDIR entries 1`.
  Red when: a nested bar still counts and sweeps the outer runner's scratch, or a leg inherits the
  variable.
  permission: the fixture bar is owed to the main loop (scratch-guard row G2); the pass makes the
  two probes.
- **AC12** — When `grep -n "GATE_OUTER_AMBIENT_TMP" .githooks/pre-push.test.sh` runs, it prints the
  variable's reason line in the knob classes comment and the `BAR_INERT_KNOBS` line naming it. When
  `grep -n "GATE_OUTER_AMBIENT_TMP" tools/run-gates/README.md` runs, it prints a line of the
  scratch section.
  Red when: the runner reads a `GATE_` name the knob census does not class, or the README does
  not name it.

No verdict moves: each touched suite keeps its arm lines and exit code (AC5), and the runners keep
their lines and their sweep predicate for bash-owned roots (AC6, AC7). Exporting `TEMP` and `TMP`
and reading an outer root move where a temp file lands and which root is counted and swept, never
a leg's result (AC10, AC11).

## 7. Gates

`encoding posture (text IO names its encoding)` · `pre-push self-test` · `shell-hygiene selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `run-gates turnstile` · `run-gates evidence` · `run-gates canary` · `run-gates gov canary` · `run-gates run-log line` · `pre-push run-log line` · `measure-legs selftest` · `run-selftests self-test` · `scratch-guard self-test` · `routed-commits selftest` · `kit/dogfood doc parity` · `transition-audit arms` · `straggler-guard arms` · `tier2-review self-test` · `codebase-map kit selftest` · `recall floor` · `recall floor arms` · `process-monitor census selftest` · `runlog selftest` · `branch-reconcile selftest` · `lexicon selftest` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `playbook render selftest` · `policy fixtures` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `line length`

New arm: tools/gate-lint/encoding_posture.py · covers AC4 AC9 · the --cleanup mode's selftest rows; a planted swallowing removal split over two lines, and a TemporaryDirectory with ignore_cleanup_errors, each staged in a fixture tree · FLOOR_ASSERTIONS rises by the rows added
New arm: tools/lib/resolve-python.test.sh · covers AC8 · the three new PARITY_ROWS rows; each failing case is staged by one changed byte in a copy · none

The new cleanup leg itself is declared in `tools/gate-legs.json`, and its RED and GREEN observation
at the close is the main loop's, as are the suite runs of AC5 and the fixture bars of AC10 and AC11.
The bar runs once at the close.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft. Order 6, not the briefed 1. The population spans files
  TOOL-dQuietDisk-1 (`tools/lib/resolve-python.test.sh`), TOOL-dQuietDisk-7 and -11
  (`tools/govkit/fixture_target.py`), TOOL-dQuietDisk-8 (`tools/policy/check_policy.py`),
  TOOL-dQuietDisk-5 and -15 (`tools/run-gates/run-gates.sh`), TOOL-dQuietDisk-16
  (`tools/govkit/upgrade_steps.py`) and TOOL-dQuietDisk-17 and -18 (`tools/govkit/selftest.py`)
  write, at orders 1 to 5. No unit depends on this one, so it runs after all of them and moves the
  sites they leave.
- rev-2 · 2026-11-22 · closes TOOL-dQuietDisk-27 and re-grounded at e4699ee75 (dWitnessedBar's
  land tip merged), under `2026-11-22-prompt-TOOL-dQuietDisk-1-reground-task`. Ask 27's two gaps
  join as S7 and S8, with AC10 to AC12: `TEMP` and `TMP` exported beside `TMPDIR` by both runners,
  and `GATE_OUTER_AMBIENT_TMP`, the outer runner's ambient root, read for the count and the sweep
  and classed inert in the pre-push knob census. S2 exports the three names from the Python face
  too, the same class. S4 states the three helpers the lifted block calls. What moved: the
  owned-root block to `run-gates.sh` lines 2399 to 2465, unchanged in body; the population to 45
  `rmtree` and 11 `TemporaryDirectory` sites in 21 files, and the hooks to 23 files [PINNED], so the file
  list is re-derived; the registry exemption to line 253; the base to `e4699ee7`.
- rev-3 · 2026-11-22 · under `2026-11-22-prompt-TOOL-dQuietDisk-1-divergence-task`. The two names
  the lexicon refused lead with a declared verb, each checked by `--suggest`: `scratch_dir` is
  `build_scratch_dir`, a `contextlib.contextmanager` generator so that no dunder is graded, and
  `enter_owned_tempdir` is `init_owned_tempdir`. Section 6 no longer has the pass run a gate: AC4's
  graded run, AC5's suite runs, AC9's `--selftest` and the fixture bars of AC10 and AC11 are owed to
  the main loop, and the pass makes `--measure` runs, a compile check and probes of the extracted
  runner lines.
- rev-4 · 2026-11-22 · wording only, under `2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task`. In section
  4 and section 9 the measured file and site counts of the population table, the hook grep's file
  count, the pass-base file list's count and rev-3's re-ground line are marked PINNED. Design, scope
  and acceptance unchanged.

## 10. Reuse audit

The seams extended: the bar's owner record and dead-owner sweep
(`tools/run-gates/run-gates.sh#write_work_owner`, `#scan_dead_work`, TOOL-dDerivedDocket-25), lifted
into one block rather than copied, and its owned-root block, which S7 and S8 extend in place
rather than beside it; the chmod-and-retry hook of
`tools/memory-tree/deviation_join.py#remove_tree`, which becomes the canonical `remove_tree`; the
copy rule of `PARITY_ROWS`; and `tools/gate-lint/encoding_posture.py`'s AST population walk and its
shrink-only ledger through `legacy_ledger`, which the new mode reuses.

`python tools/codebase-map/reuse_lookup.py "remove a scratch tree with a chmod and retry handler"`
ranked `remove_tree` in `tools/govkit/upgrade_walk.py`, `tools/loop/loop_witness.py` and
`tools/memory-tree/deviation_join.py`: three copies of the one helper this unit makes canonical.

Recall returned TOOL-dSweptScratch-1 (CLOSED on main, `5a311c9fa`), which moved most sites onto
local hooks and stated in its §3 that a killed run's leak was out of its reach; this unit is that
reach. It also returned TOOL-aBranchedMandate-6, which measured the read-only-object mechanism, and
TOOL-dQuietDisk-23, the other G-C clauses. The owning chain build is dWitnessedBar (Test: gate
health); its branch changes `run-gates.sh` and `run-selftests.sh`, and no spec of it changes the
owner record or the sweep, at `609cd40b1` or at `e4699ee75`: the block's body is byte-identical at
both. The re-ground read `git log 609cd40b1..ed833f684` over both runners and
`.githooks/pre-push.test.sh`, and the specs added since, units 106 to 110. Two overlaps are named
for the merge. Three files the population moves are dWitnessedBar's own,
`tools/run-gates/verdict_flow.py`, `tools/run-gates/leg_factory.py` and
`tools/run-gates/verdict_backends.py`. The knob census S8 joins classes names from its units 5,
8, 25, 40 and 56, and its units 63, 106 and 110 changed `.githooks/pre-push.test.sh` after
`609cd40b1`; S8 adds one name and one reason line there. The incms side is TOOL-dQuietDisk-27's source: the incms
fix-4 session's notes in the shared notes folder, `fix4-incms-notes-for-gov.md`, ask for exactly
these two changes, and its `scripts/gate.sh` records that it owes the export once gov names the
variable.

Recall terms used: rmtree ignore_errors onexc remove_tree chmod read-only scratch owned sweep gate-work owner TMPDIR TEMP TMP ambient nested outer runner knob census
