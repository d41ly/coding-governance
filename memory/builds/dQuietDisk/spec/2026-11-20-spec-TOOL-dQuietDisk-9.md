# TOOL-dQuietDisk-9 — every scratch path under one owned, swept root, and every tree removed by one chmod-and-retry helper

**Status:** CLOSED · rev-6 · 2026-11-22 · node d · Tier-2 · base ebab8b90 · streams tooling · order 6 · closes TOOL-dQuietDisk-27 · ratified 2026-11-22

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-28 |
| [2026-11-22-build-TOOL-dQuietDisk-9-1-acceptance-ledger.md](../build/2026-11-22-build-TOOL-dQuietDisk-9-1-acceptance-ledger.md) | journal | — |
| [2026-11-22-build-TOOL-dQuietDisk-9-deviation-1.md](../build/2026-11-22-build-TOOL-dQuietDisk-9-deviation-1.md) | deviation | — |
| [2026-11-22-build-TOOL-dQuietDisk-9-widen-14.md](../build/2026-11-22-build-TOOL-dQuietDisk-9-widen-14.md) | widen | — |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-reground-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-reground-task.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-14 TOOL-dQuietDisk-19 |
| [2026-11-22-prompt-TOOL-dQuietDisk-17-reground-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-17-reground-task.md) | research | TOOL-dQuietDisk-17 |
| [2026-11-22-prompt-TOOL-dQuietDisk-9-1-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-9-1-spec-writer.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-9-build-brief.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-9-build-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-9-divergence-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-9-divergence-task.md) | research | — |

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

- **S1** — `tools/lib/owned_scratch.py`, the canonical module, holding three marked Python blocks.
  `remove_tree_py` defines `remove_tree(path)` and `build_scratch_dir()`. `remove_tree` calls
  `shutil.rmtree` with an `onexc` hook that clears the read-only bit on the failing path and retries
  it once, never raises, and returns whether the path is gone. `build_scratch_dir()` is a
  `contextlib.contextmanager` generator over `tempfile.mkdtemp()` whose exit calls `remove_tree`, so
  no dunder the lexicon would grade is defined. `onexc` alone is used: the declared python floor is
  3.15 (`tools/lib/python-floor.txt` at `ebab8b90b`).
  Observed by AC1.
- **S2** — The block `owned_work_py` defines `resolve_owned_work(path)`: the nearest of `path` and
  its parents that is named `gate-work.*` and holds an `owner` file, or None. That is the walk
  `tools/lib/template_cache.py#TemplateCache` makes in its constructor today, which becomes a call
  to it, so the two never disagree on which root a process sits in. The block
  `owned_tempdir_py` defines `init_owned_tempdir()`, `scan_dead_scratch(ambient, common)` and
  `read_pid_alive(pid)`. When `resolve_owned_work(tempfile.gettempdir())` answers,
  `init_owned_tempdir()` sets `tempfile.tempdir` to that temp dir and returns it, making nothing and
  spawning nothing. Otherwise it resolves this repository's git common dir with one
  `git rev-parse --path-format=absolute --git-common-dir`, which reads empty outside a repository.
  It then calls `scan_dead_scratch`, which removes each `gate-work.*` directly under the temp dir
  whose owner line names a `py:` pid that `read_pid_alive` judges dead and the same common dir, and
  removes nothing when the common dir is empty. It makes its own root with
  `tempfile.mkdtemp(prefix="gate-work.")`, writes the owner line `py:<pid>TAB<common dir>TAB<epoch>`
  tmp-then-rename, makes `tmp` inside it, sets `tempfile.tempdir` to that `tmp`, exports `TMPDIR`,
  `TEMP` and `TMP` as that `tmp` so the suite's child processes land there too, and registers
  `remove_tree` of the whole root at exit, so a template cache made under it goes with it.
  `read_pid_alive` is `os.kill(pid, 0)` on POSIX and `OpenProcess` with `GetExitCodeProcess` on
  Windows, where `os.kill` is never called, because signal 0 there is `CTRL_C_EVENT`. Any error
  reads as alive. Observed by AC2 and AC3.
  **Readers:** by name: none, since the constructor's loop is unnamed and withdraws no name, and the
  attribute it sets keeps its name ·
  by value: `resolve_template` in `tools/lib/template_cache.py`, which reads the root the
  constructor sets and gets the same directory, because `resolve_owned_work` walks the same paths
  in the same order.
- **S3** — Every `shutil.rmtree(..., ignore_errors=True)` and every
  `TemporaryDirectory(..., ignore_cleanup_errors=True)` under `tools/`, `skills/` and `.githooks/`
  moves to `remove_tree` and `build_scratch_dir`. Every hand-written chmod-and-retry hook in those
  trees moves to `remove_tree` too. A program a landed `[[upgrade]]` row names in its argv is
  excluded, because `tools/govkit/upgrade_steps.py#check_frozen` reds the `step-rows-frozen` leg on
  any byte of it changing. At `ebab8b90b` that excludes three files under `tools/govkit/steps/`:
  `conf_pins_to_ledger.py` and `registry_to_ledger.py` keep their one cleanup site each, which
  enter `memory/project/cleanup-sites.txt` as waived rows with that reason, and
  `kickoff_facts_to_overlay.py` keeps its hook. Every file but `tools/lib/owned_scratch.py` carries the blocks
  it calls inline, a gov-internal file included, as the copy rule in the design section states. Each
  Python suite entry point in that population, a file a gate leg's argv runs to execute arms, calls
  `init_owned_tempdir()` before its first scratch and before it builds a `TemplateCache`. Observed
  by AC4 and AC5.
  **Readers:** by name: `remove_tree`, which `tools/loop/loop_witness.py` and
  `tools/memory-tree/routed_commits.py` call through `deviation_join`, and
  `tools/run-gates/keep_tails.py` calls through `product_tests`; the inline block keeps the name in
  each of those two modules. Each local hook's other callers sit in its own file and call
  `remove_tree` after the move ·
  by value: NO VALUE READERS — each of those calls is a bare statement today, and S1's return is new.
- **S4** — The bash face, the canonical block `owned_work_sh` in `tools/lib/owned-scratch.sh`. It
  defines `write_work_owner <dir> <common>` and
  `scan_dead_work <ambient> <own dir> <common> <health log>`, lifted from
  `tools/run-gates/run-gates.sh#write_work_owner` and `#scan_dead_work` with their globals made
  arguments. It calls `derive_temp_path`, `ts_alive` and `add_health_event` and defines none, as
  the runner's body does, so the owner write keeps its unpredictable staging name. `run-gates.sh`
  carries it in place of its two functions, called with `$WORK`, S8's swept root, `$WORK_COMMON` and
  `$RG_HEALTH_LOG`, so its lines and health events are unchanged. `run-selftests.sh` carries it
  too, with the `health_log_sh` block and the runner's two one-line helpers
  (`tools/run-gates/run-gates.sh@7848b83f22c0:962`, `:1828`), none of which it holds today. Its startup scratch, `RS_SCRATCH`
  (`tools/run-gates/run-selftests.sh@c9d39e4a1284:1035`), becomes
  `mktemp -d "${TMPDIR:-/tmp}/gate-work.XXXXXXXX"`, its one owned root in every mode. One
  `git rev-parse --git-dir --git-common-dir` there gives both dirs, parsed by parameter expansion
  as the runner parses its facts
  (`tools/run-gates/run-gates.sh@7848b83f22c0:127-131`), and never by a loop. The common dir is
  normalised to `RG_COMMON`'s form (`:1113-1114`) by `cd` and `$PWD` in the running shell, with no
  subshell, and the health log comes from `derive_health_log`. It writes the owner line and calls `scan_dead_work` there, before any mode
  runs a row. The sweep root (`tools/run-gates/run-selftests.sh@c9d39e4a1284:1478`) becomes
  `$RS_SCRATCH/s` and the attribution scratch (`:2030`) becomes `$RS_SCRATCH/a`, each made by
  `mkdir`. The sweep mode's own `git rev-parse --git-dir` (`:1489`) takes the startup answer. S4
  adds two command substitutions to `run-selftests.sh`, `$(git rev-parse --git-dir --git-common-dir)`
  and `$(derive_health_log ...)`, and no loop fed by either. The second grows the
  `spawn-idiom-sites` row `tools/run-gates/run-selftests.sh` `pure-fn-subst` (3 [PINNED at
  `ebab8b90b`]) by one, which the main loop widens through `ratchet.py widen` after the pass.
  Observed by AC6 and AC7.
- **S5** — Four `PARITY_ROWS` rows join `tools/lib/resolve-python.test.sh`: one for each Python
  block and one for `owned_work_sh`. Observed by AC8.
- **S6** — The lint. `tools/gate-lint/encoding_posture.py` gains a mode `--cleanup`, with its scan
  `scan_python_cleanup` and its arms tuple `CLEANUP_ARMS`, holding the one arm `cleanup`. The arm
  keys a site `<path>` `cleanup` for each AST call S3 names, read across lines. It uses the file's
  own population walk, `--measure`, ledger adapters and `--selftest`, whose `FLOOR_ASSERTIONS`
  rises by the rows added. Its registry is `memory/project/cleanup-sites.txt`, a shrink-only ledger
  with the encoding-posture ledger's header, holding a row only for a site a reviewer waives with a
  reason. The leg is gov-only, an `[[exempt_leg]]` row in `tools/govkit/registry.toml` shaped as the
  `spawn budget (forks per hot entrypoint)` row, run over `.`, `{prefix}`, `skills` and
  `.githooks`. Its ledger is a `[[ledger]]` row in `tools/gate-lint/kit.toml` beside the
  `fork-ceilings` row, seeded through `tools/memory-tree/convert_registry.py read-back`, which gains
  the population's table row. `.memory-tree.conf` names the file in `PROJECT_REGISTRY_EXTRA`, and
  `python tools/run-gates/leg_factory.py --write` re-renders `tools/gate-legs.json`. Observed by AC4
  and AC9.
- **S7** — Native children (ask TOOL-dQuietDisk-27, gap 1). Where `run-gates.sh` exports `TMPDIR`
  as `$WORK/tmp` before the first leg, it exports `TEMP` and `TMP` to the same value, spelled as
  `mktemp -d` returned it. MSYS converts all three for a native child, so a native node or python
  leg's temp lands inside the owned root. `run-selftests.sh` sets the same three where it sets a
  row's `TMPDIR` (`tools/run-gates/run-selftests.sh@c9d39e4a1284:1578`). Observed by AC10.
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
- **S9** — The orphaned owner (F1, resolved (b)). Each sweep also removes a root whose owner names a
  dead pid of its own kind and an absolute common dir that names no directory, whatever repository
  that was. A common dir that names a directory keeps today's rule, so another live repository's
  root is never touched. `scan_dead_work` tests it with `[ -d ]` and `scan_dead_scratch` with
  `os.path.isdir`, once per foreign root. Observed by AC13.
  **Readers:** by name: none, since the item widens a predicate and withdraws no name ·
  by value: NO VALUE READERS — `scan_dead_work` returns 0 on every path and its callers read only
  its stderr line, and `scan_dead_scratch` is new.

## 3. Non-goals (OUT)

- No bash `rm -rf` rewrite. MSYS `rm -rf` removes git's read-only objects, and the bash leaks
  dSweptScratch measured were bookkeeping it fixed (TOOL-dSweptScratch-1, §4).
- No new sweeper. A bash-owned root is swept by `scan_dead_work`, a Python-owned one by the next
  `init_owned_tempdir()`. Each judges only its own pid kind: bash's `kill -0` cannot judge a
  Windows pid, so `py:` lines are skipped by the bash scan, whose `case` already refuses a
  non-numeric pid (`tools/run-gates/run-gates.sh#scan_dead_work`).
- No owned root for a bash suite run directly. `lib-selftest.sh`'s `SELFTEST_ROOT` and the
  `mktemp -d` of each suite that carries the cache inline are removed by a trap and left by a kill.
  Under a bar or the self-test runner they already sit in an owned root. A direct run is G-C's
  unrooted-`mktemp` clause, ask TOOL-dQuietDisk-23, as are the leftovers the design section counts.
- No movable site seeded into the cleanup ledger. S3 moves every one, so the ledger holds only the
  two frozen step programs' waived rows.
- No successor step programs. Retiring the landed rows to new programs is a separate mechanism this
  unit does not need, and two waived rows cost nothing.
- The other G-C lint clauses: `git init` outside the template helper, a spawn inside a loop body,
  `copytree` of a kit, `clone --no-hardlinks` and an unrooted `mktemp`. They are TOOL-dQuietDisk-23.
- No kit version bump by hand: `govkit.py mint` writes every owed bump at the lander.
- No policy key. Removing a tree and owning a root save no answer, so the cache rule does not reach
  them, and their off value would be a leak. `GATE_OUTER_AMBIENT_TMP` is not a switch either: it
  names a directory an outer runner holds, and unset is today's behaviour.
- No outer-root read in the Python face: it nests in whatever owned `TMPDIR` it is given and removes
  its own root at exit.
- No move of where a bar makes its own `gate-work.*`: under an adopter runner it stays in that
  runner's scratch.
- No edit to `tools/lib/template-cache.sh`: its walk already finds S4's root.
- No edit in incms. Its `scripts/gate.sh` exporting the variable is that repository's change.

### Edges

- **hands-off** external — incms `scripts/gate.sh` exports `GATE_OUTER_AMBIENT_TMP` as the temp
  root it started under, in that repository under its own governance, once a minted run-gates kit
  carrying S8 reaches it through `govkit update`

## 4. Design

### Where the code was read

Code at `ebab8b90b`, this run's `HEAD` with orders 1 to 4 built. A citation is by symbol or
`<path>@<blob>:<line>`, each blob read at that commit.

### What it saves, measured

`%TEMP%`'s top level was read on 2026-11-22 at `ebab8b90b`; each count below is PINNED there.

| Residue | Count | Who made it | After this unit |
|---|---|---|---|
| Python `mkdtemp` roots holding `m13-gov-*` fixtures | 4 roots, 13,029 entries | `tools/govkit/selftest.py#main`'s `TemporaryDirectory`, run outside a bar on 2026-11-20 and left whole, a kill's shape | S2: a root of this shape carries an owner and the next Python suite sweeps it; these four predate it and stay |
| Dead fixture bars' `gate-work.*` | 2 roots, 20 entries | a runner suite's fixture bar, whose owner names a removed fixture repository | S9: the next bar sweeps both |
| Bash `tmp.*` dirs | 11 dirs, 32 entries | function-local `mktemp -d` in `tools/run-gates/run-gates.gov.test.sh` (6) and `tools/unattended/unattended.sh` (5) | not reached: ask TOOL-dQuietDisk-23 |

Two probes ran on 2026-11-22 under python 3.15.2 [PINNED]. `shutil.rmtree(..., ignore_errors=True)`
over a one-commit repository left 8 entries, 3 of them read-only objects; an `onexc` chmod-and-retry
hook left 0. From Git Bash with only `TMPDIR` at a planted `gate-work.*/tmp`, node's `os.tmpdir()`
answered `%TEMP%`; with `TEMP` and `TMP` exported too it answered the planted dir, and a Git Bash
child of python read all three in their MSYS form.

The unit adds git processes in two places only [DERIVED from the reads S2 and S4 name]:
- one per Python suite run outside any owned root, none when nested;
- one per `run-selftests.sh` run outside its sweep mode, none in it, where the startup read
  replaces the sweep mode's own.

### The population, read over the real tree first

The predicate: an AST `Call` whose callee is named `rmtree` with the keyword `ignore_errors=True`,
or `TemporaryDirectory` with `ignore_cleanup_errors=True`, over every tracked `*.py` under `tools/`,
`skills/` and `.githooks/`, read through one `git cat-file --batch`.

| Tree | `rmtree` sites | `TemporaryDirectory` sites | Files | Of them, shipped by a kit |
|---|---|---|---|---|
| `59e882afd` | 59 | 11 | 33 | 22 files, 40 sites [PINNED] |
| `a2619a3f6` | 35 | 11 | 15 | 12 files, 26 sites [PINNED] |
| base `b3f5a2bc3` | 45 | 11 | 21 | 16 files, 34 sites [PINNED] |
| `HEAD` `ebab8b90b` | 51 | 11 | 25 | 18 files, 36 sites [PINNED] |

The `ebab8b90b` row was read on 2026-11-22, the same scan reproducing the `b3f5a2bc3` row. Orders 1
to 4 added `tools/lib/template_cache.py` and `tools/lib/history_store.py` with its two copies. The `TemporaryDirectory` sites sit in
`tools/govkit/upgrade_steps.py` and `tools/govkit/selftest.py`. A plain
`TemporaryDirectory()` is outside the predicate: its own cleanup resets permissions and retries, as
`tempfile.TemporaryDirectory._rmtree` reads under 3.15. "Shipped" is
`python tools/govkit/govkit.py shipped`, run at each sha for its row. The hand-written hooks,
`git grep -lE "onexc|onerror"` over the same trees, sit in 23 files [PINNED] at `ebab8b90b`, the same 23 as
at `b3f5a2bc3` [PINNED], among them `tools/memory-tree/deviation_join.py#remove_tree`,
`tools/govkit/upgrade_walk.py#remove_tree`, `tools/govkit/step_gate.py` and
`tools/lib/commit_trailers.py`. The builder re-runs the predicate at the pass's own base with
`--cleanup --measure` and moves what it prints outside the frozen step programs. figure: DERIVED at the pass's base; the table is
PINNED at the four shas named.

### The copy rule

`tools/lib/` ships nothing (`tools/govkit/registry.toml@4649a8980b3d:253`). Every file but
`tools/lib/owned_scratch.py` carries each block it calls inline, between
`# >>> remove_tree_py — canonical copy: owned_scratch.py in gov's lib dir` and
`# <<< remove_tree_py`, and the parity table holds each copy to the canonical block
(`tools/lib/resolve-python.test.sh@76c8f4628980:405`). A gov-internal file is no exception:
- `tools/lib/history_store.py` travels whole as two kits' copies, its site inside its own block;
- `tools/govkit/selftest.py` loads `tools/lib/template_cache.py` by path, so a sibling import has
  no path, and that file already carries `git_env_leaks_py` inline;
- `tools/govkit/govkit.py`, `upgrade_steps.py` and `selftest.py` already carry lib blocks inline.

A block that calls another carries it: `owned_tempdir_py` calls `remove_tree` and
`resolve_owned_work`, so its carriers carry all three, and `template_cache.py` carries
`owned_work_py` and `remove_tree_py`. `deviation_join.remove_tree` and `product_tests.remove_tree`
keep their names for their outside callers. The `commit_trailers_py` block holds its hook, so the
moved call sits inside that block in all three copies.

### The owner line both faces read

```text
<pid>\t<git common dir>\t<start epoch>      bash: an MSYS pid, judged by kill -0
py:<pid>\t<git common dir>\t<start epoch>   python: a native pid, judged by read_pid_alive
```

Each face compares the common dir in its own spelling: bash's is `cd` and `pwd` over git's answer,
the `RG_COMMON` form both runners now share, and Python's is git's absolute form. Each sweeps only
its own pid kind, so the two spellings never meet.

A dead owner is swept when its common dir is this repository's, as today, or when it is absolute
and names no directory (S9). The two dead fixture roots in `%TEMP%`, 20 entries [PINNED at
`ebab8b90b`], are that case: their owners name `/tmp/tmp.*/.git` repositories their suites removed.

### Where the template cache lands

The cache's root and its `.stage-<key>-<pid>` directories are scratch paths. Both faces
(`tools/lib/template_cache.py#TemplateCache`, `tools/lib/template-cache.sh` `resolve_template_root`)
take the nearest owned `gate-work.*` above the temp dir, else the caller's own scratch.

| Where a suite runs | Cache root today | After this unit |
|---|---|---|
| under a bar | `$WORK/templates`, owned and swept | unchanged |
| a row of `run-selftests.sh` | the suite's own scratch, unowned | `$RS_SCRATCH/templates`, owned and swept (S4) |
| a Python suite run directly | its `TemporaryDirectory`, unowned | `<its gate-work.*>/templates`, owned and swept (S2) |
| a bash suite run directly | its `mktemp -d`, unowned | unchanged, a non-goal |

Under the self-test runner every row shares one cache root; a key names its builder, so suites
share an entry only for the same base, and stage-then-rename covers two rows building one key.

### The two gaps of ask TOOL-dQuietDisk-27

The owned-root block sits at `tools/run-gates/run-gates.sh@7848b83f22c0:2399-2465`, unchanged since
`b3f5a2bc3` in body and lines. It sets `GATE_AMBIENT_TMP=${TMPDIR:-/tmp}`, makes `$WORK` there,
sweeps `"$GATE_AMBIENT_TMP"/gate-work.*`, counts `"$GATE_AMBIENT_TMP"/*` into `TMPDIR_ENTRIES` and
exports only `TMPDIR` (`:2465`). The incms session measured both gaps
(`memory/builds/dQuietDisk/BACKLOG.md`, ask TOOL-dQuietDisk-27), and this re-ground's probe saw
the first one again.

```bash
GATE_AMBIENT_TMP=${TMPDIR:-/tmp}                 # unchanged: where $WORK is made
RG_SWEPT_TMP=$GATE_AMBIENT_TMP                   # what the count and the sweep read
if [ -n "${GATE_OUTER_AMBIENT_TMP:-}" ]; then
  if [ -d "$GATE_OUTER_AMBIENT_TMP" ]; then RG_SWEPT_TMP=$GATE_OUTER_AMBIENT_TMP
  else echo "run-gates: NOTE - GATE_OUTER_AMBIENT_TMP names no directory, so the bar counts and sweeps $GATE_AMBIENT_TMP" >&2; fi
fi
unset GATE_OUTER_AMBIENT_TMP
# ... scan_dead_work "$RG_SWEPT_TMP" "$WORK" "$WORK_COMMON" "$RG_HEALTH_LOG"; the count globs "$RG_SWEPT_TMP"/*
export TMPDIR="$WORK/tmp" TEMP="$WORK/tmp" TMP="$WORK/tmp"
```

Under an outer root the count no longer includes this bar's own dir, which sits in the outer
runner's scratch; two nested bars over one unchanged outer root still print one figure. The
variable's name was checked with `python tools/lexicon/lexicon.py --suggest GATE_OUTER_AMBIENT_TMP
--as constant`, which answers that the declaration carries no `constant` cell. So no lexicon cell
grades an environment name, and the runner's knob census is its one grader: every `GATE_` name the
runner reads through `$` must sit in exactly one class (`.githooks/pre-push.test.sh#check_knob_classes`,
its classes comment and `BAR_INERT_KNOBS` at `.githooks/pre-push.test.sh@9abef5a9a376:2115`). It is
inert there because it moves only a count and a sweep that needs a dead owner of this repository,
never a leg or a verdict. `GATE_AMBIENT_TMP` stays as that census classes it, assigned in the runner.

### Inventory

| Minted identifier | Kind | Naming cell | Graded by |
|---|---|---|---|
| `remove_tree_py`, `owned_work_py`, `owned_tempdir_py`, `owned_work_sh` | parity block markers | `PARITY_ROWS` | `tools/lib/resolve-python.test.sh` |
| `remove_tree`, `build_scratch_dir`, `resolve_owned_work`, `init_owned_tempdir`, `scan_dead_scratch`, `read_pid_alive` | Python functions | `py.function`, lexicon `--suggest` OK | the probes of section 6 |
| `scan_python_cleanup` | Python function | `py.function`, lexicon `--suggest` OK | the scanner's `--selftest` |
| `write_work_owner`, `scan_dead_work` | shell functions, lifted under their names | `sh.function`, lexicon `--suggest` OK | the probes of section 6 |
| `--cleanup`, arm `cleanup`, `CLEANUP_ARMS` | scanner mode, arm and arms tuple | the scanner's mode table | its `--selftest` |
| `cleanup-sites` | ledger population | `.memory-tree.conf` `PROJECT_REGISTRY_EXTRA` | `memory hygiene` |
| `cleanup posture (a tree removal that swallows its error)` | gov-only gate leg | `tools/govkit/registry.toml` `[[exempt_leg]]` | `run-gates canary` |
| `GATE_OUTER_AMBIENT_TMP` | environment variable an outer runner exports | `BAR_INERT_KNOBS` | `pre-push self-test`'s knob census |
| `RG_SWEPT_TMP` | runner variable | none | the fixture bars of section 6 |

### Files touched (estimate)

`tools/lib/owned_scratch.py` · `tools/lib/owned-scratch.sh` · `tools/lib/resolve-python.test.sh` ·
`tools/run-gates/run-gates.sh` · `tools/run-gates/run-selftests.sh` ·
`tools/gate-lint/encoding_posture.py` · `tools/gate-lint/kit.toml` · `tools/govkit/registry.toml` ·
`memory/project/cleanup-sites.txt` · `.memory-tree.conf` · `tools/gate-legs.json`, rendered by
`leg_factory.py --write` · `memory/guides/SESSION-KICKOFF.md` · `.githooks/pre-push.test.sh` ·
`tools/run-gates/README.md` · `memory/project/shell-role.txt`, whose rows for the two runners and a
new row for `tools/lib/owned-scratch.sh` grow only through
`python tools/memory-tree/ratchet.py widen shell-role`, which the main loop runs after the pass

Plus every file the predicate and the hook grep name at the pass's base, less the frozen step
programs. At `ebab8b90b` those are 43 files [DERIVED: the 46 both greps name, less three]:

`.githooks/pre_push_bar_selftest.py` · `tools/branch-reconcile/selftest.py` ·
`tools/govkit/fixture_target.py` · `tools/govkit/selftest.py` · `tools/govkit/step_gate.py` ·
`tools/govkit/upgrade_steps.py` ·
`tools/govkit/upgrade_walk.py` · `tools/lexicon/selftest.py` · `tools/lib/commit_trailers.py` ·
`tools/lib/history_store.py` · `tools/lib/template_cache.py` ·
`tools/loop/claims.py` · `tools/loop/factories.py` · `tools/memory-recall/check-recall.py` ·
`tools/memory-recall/query.py` · `tools/memory-recall/selftest.py` ·
`tools/memory-recall/test_recall_floor.py` · `tools/memory-tree/commit_trailers.py` ·
`tools/memory-tree/convert_registry.py` · `tools/memory-tree/deviation_join.py` ·
`tools/memory-tree/gen_build_index.py` · `tools/memory-tree/history_store.py` ·
`tools/memory-tree/ratchet.py` ·
`tools/playbook/check_layers.py` · `tools/playbook/edge_grammar.py` ·
`tools/playbook/fixtures/composition.py` · `tools/playbook/gov_tag.py` ·
`tools/playbook/load_sets.py` · `tools/playbook/writing_practice.py` ·
`tools/policy/check_policy.py` · `tools/process-monitor/selftest.py` ·
`tools/run-gates/check-receipt.py` · `tools/run-gates/held_halves.py` ·
`tools/run-gates/leg_factory.py` · `tools/run-gates/measure_legs.py` ·
`tools/run-gates/owed_rows.py` · `tools/run-gates/product_tests.py` ·
`tools/run-gates/verdict_backends.py` · `tools/run-gates/verdict_flow.py` ·
`tools/runlog/selftest.py` · `tools/unattended/commit_trailers.py` · `tools/unattended/fix_keeps.py` ·
`tools/unattended/history_store.py`

TOOL-dQuietDisk-17 is WONTDO, retired by its F2, so this pass builds on `tools/govkit/selftest.py`
as units 18 and 11 left it.

The kickoff manifest's `watch:` line names `tools/run-gates/run-gates.sh`,
`tools/run-gates/run-selftests.sh`, `tools/gate-legs.json` and `.memory-tree.conf`, so the commit
that stages them re-stamps the manifest's `last-audit`.

### Alternatives rejected

| Alternative | Why it loses |
|---|---|
| Files importing `owned_scratch.py` | Adopters have no `tools/lib/`, two files have no import path, and each importer's leg would need it in its guard. |
| A cleanup leg every adopter runs | Its registry names gov's own sites, as the `spawn budget` leg's does. |
| A new scanner file | It would copy the walk, `--measure` and the ledger adapters the modes share. |
| A registry seeded with today's sites | S3 moves them all; a seeded ratchet never drains. |
| One sweeper for both pid kinds in bash | MSYS `kill -0` reads a native pid as dead. |
| An owned root per self-test runner mode | One startup root covers every mode. |
| `onerror` below 3.12 | The floor is 3.15: dead code. |
| Successor programs for the frozen steps | A second mechanism, `[[retired]]` rows and new programs, for two sites (YAGNI). |

## 5. Production-readiness checklist

- security: removal stays inside directories the run made, or a dead owner made for this
  repository or for one whose common dir names no directory (S9). An unreadable owner line, a live
  pid, a relative common dir and another existing repository's root are never swept, and an empty
  common dir sweeps nothing. `GATE_OUTER_AMBIENT_TMP` moves which directory the sweep lists, never
  its predicate. A bar's durable records live under its git dir, never in this scratch.
- perf / scale: `init_owned_tempdir` lists the temp dir's `gate-work.*` names once per suite; the
  git processes added are the design section's two.
- error / empty / loading states: a removal that still fails returns False and raises nothing, as
  `ignore_errors` did; its root is swept later.
- observability: the bash sweep keeps its `sweeping the scratch of a dead bar` line and health event,
  and `run-selftests.sh` gains both. The Python sweep prints one stderr line per root it removes,
  before the suite's first output.
- risks: a removal is the only write a cleanup site makes, so moving it moves no suite verdict;
  AC5 observes it. The gotcha `append-without-an-idempotence-key` applies to the owner write, which
  is tmp-then-rename. The three history legs' code digests name their kit's `commit_trailers.py`
  (`tools/unattended/check-pass-order.sh@bc36c481c969:548`,
  `tools/memory-tree/routed_commits.py@e3088f9bcba9:360`), which S3 edits, so each grades cold once
  after this unit lands. A self-test runner row's path grows by 6 characters [DERIVED from
  `tmp.XXXXXXXXXX` against `gate-work.XXXXXXXX/s`] near `MAX_PATH`; AC5's suite runs observe it.
- testing: the probes of section 6 and the scanner's `--selftest`.
- migration: N/A — no stored data; a root left by a run before this unit has no owner and is never
  swept, as today.
- user docs: no page under `help/` names a cleanup call or a scratch root (`git grep` at
  `ebab8b90b`). `tools/run-gates/README.md` "The scratch directory — owned, redirected and swept"
  gains `TEMP` and `TMP` beside `TMPDIR`, the orphaned-owner sweep of S9, and a paragraph on
  `GATE_OUTER_AMBIENT_TMP`: who exports it, what it moves, and that unset is today's behaviour.

## 6. Acceptance criteria

- **AC1** — When a probe under `%TEMP%/<short-name>` makes a repository with a commit, so its
  `.git/objects` hold read-only files, and calls `remove_tree` on it, the call returns True and the
  path is gone. With the hook's `os.chmod` deleted, the path survives and the call returns False
  without raising.
  Red when: the read-only objects survive, or a failure raises.
- **AC2** — When a probe runs with `TMPDIR` inside a planted `gate-work.x/tmp` holding
  `gate-work.x/owner`, `init_owned_tempdir()` returns that `tmp`, makes no directory and spawns no
  git, and a `TemplateCache()` built there with no `SELFTEST_TEMPLATE_ROOT` answers
  `gate-work.x/templates` as its root. Run with an ambient `TMPDIR`, it makes one `gate-work.*`
  holding an owner line that starts `py:`, a `TemplateCache()` built after it answers that root's
  `templates`, a child `python -c` it starts prints that root's `tmp` for each of `TMPDIR`, `TEMP`
  and `TMP`, and the directory is gone after the process exits.
  Red when: a nested run makes a second root, the cache's root sits outside the owned root, a
  direct run's root outlives it, or a child reads the ambient temp dir.
- **AC3** — When a probe plants, under one ambient dir, a root owned by a dead `py:` pid of this
  repository, one by a live `py:` pid, one by a dead `py:` pid of another existing common dir, and one by a
  bash pid, and calls `init_owned_tempdir()`, only the first is removed. Run outside any repository,
  so the common dir reads empty, it removes none of the four.
  Red when: a live, foreign or bash-owned root is removed, or an empty common dir sweeps.
- **AC4** — When `python tools/gate-lint/encoding_posture.py --cleanup --measure . tools skills .githooks`
  runs at the unit's tip, it prints two `cleanup` lines, naming `conf_pins_to_ledger.py` and
  `registry_to_ledger.py`, and the `cleanup-sites` ledger holds those two waived rows, each with its
  reason. Run over a fixture tree holding one planted
  `shutil.rmtree(p, ignore_errors=True)` split over two lines, it prints one `cleanup` line naming
  that file. `grep -n "cleanup posture" tools/gate-legs.json tools/govkit/registry.toml` prints the
  leg's rendered and `[[exempt_leg]]` rows, and
  `grep -n "cleanup-sites" tools/gate-lint/kit.toml .memory-tree.conf tools/memory-tree/convert_registry.py`
  prints a line from each file. When the main loop runs the new leg, the graded run with the
  registry argument, at the close, it exits 0 at the tip and 1 with the planted call.
  Red when: a split call is missed, a site outside the two frozen programs survives the move, a
  frozen program changes a byte, or the leg is not rendered.
  permission: the graded run is the new leg's argv, the main loop's (scratch-guard row G1); the
  pass makes the `--measure` runs and the greps.
- **AC5** — When every Python file S3 touched compiles under `python -m py_compile`, and AC2's probe
  shows a child's temp landing in the owned root, the pass's half holds. When the main loop runs
  each suite S3 touched at the close, in a scratch `git clone --shared` of gov with `TEMP`, `TMP`
  and `TMPDIR` pointed at an empty directory, it prints the same arm lines and exit code as at the
  build's base, and the directory holds 0 entries after it exits. The unattended kit's suites are
  excluded, as the owner's rule of 2026-08-23 requires.
  Red when: an arm's result moves, or an entry remains.
  cost: the touched suites run in full once each, some for minutes.
  figure: DERIVED at observation; the residual at the build's base is recorded beside it.
  permission: a role agent runs no suite (scratch-guard row G3); the pass makes the compile check
  and the probe.
- **AC6** — When a bash probe sources `owned-scratch.sh` from `tools/lib/`, plants a `gate-work.*`
  whose owner names a dead MSYS pid and this common dir, one naming a live pid, and one whose owner
  starts `py:`, and calls `scan_dead_work` with a probe health log path, only the first is removed,
  the sweep line names its pid, and the health log gains one `scratch-swept` line.
  Red when: the `py:` root or the live one is removed, or no event is written.
- **AC7** — When a bash probe that sources the block makes a `gate-work.*` root, calls
  `write_work_owner` on it and is killed with `kill -9`, the root remains with its owner line, and a
  second probe's `scan_dead_work` over the same ambient dir sweeps it. When
  `grep -n "scan_dead_work\|gate-work\|RS_SCRATCH/[sa]" tools/run-gates/run-selftests.sh` runs, it
  prints the startup root's `mktemp` line, a `scan_dead_work` call above the first mode branch, and
  the sweep and attribution scratch lines inside it. When a probe sources
  `tools/lib/template-cache.sh` with `TMPDIR` at a planted `gate-work.x/s/1/tmp` whose `gate-work.x`
  holds an owner file, `resolve_template_root` prints `gate-work.x/templates`.
  Red when: the killed root survives the second scan, a mode's scratch sits outside the owned root,
  or a row's cache root sits outside it.
- **AC8** — When the parity table's `blk` awk extracts each new block from the canonical file and
  from every copy, every pair compares equal, the runner carries `write_work_owner` as the inline
  block, and the self-test runner's new `health_log_sh` copy compares equal to the canonical in
  `tools/lib/health-log.sh`.
  Red when: a copy drifts by one byte, which the new `PARITY_ROWS` rows and the existing
  `health_log_sh` row then report.
- **AC9** — When the main loop runs `python tools/gate-lint/encoding_posture.py --selftest` at the
  close, it prints its count line at or above the raised `FLOOR_ASSERTIONS` and exits 0. With the
  `--cleanup` arm's keyword test inverted, it exits 1.
  Red when: the new mode's rows do not execute.
  permission: a role agent runs no `--selftest` (scratch-guard row G3); this is the first `New
  arm:` line's RED and GREEN observation, owed to the main loop. The pass's proxy is AC4's
  `--measure` runs.
- **AC10** — When a bash probe under `%TEMP%/<short-name>` takes the edited runner's `export TMPDIR=`
  line, sets `WORK` to a planted `gate-work.x` holding `tmp`, evaluates the line and starts
  `node -e "process.exit(require('os').tmpdir().includes('gate-work.') ? 0 : 1)"` from Git Bash,
  the child exits 0. With `TEMP` and `TMP` taken out of the line, the same child exits 1. When
  `grep -n "TEMP=" tools/run-gates/run-selftests.sh` runs, it prints the row launch line, setting
  `TEMP` and `TMP` beside `TMPDIR`. When the main loop runs a fixture bar at the close, built as
  the runner's own suites build one, whose one leg is that `node -e` line, the leg passes, and it is
  red with the export deleted from the fixture's runner.
  Red when: a native child's `os.tmpdir()` still answers the ambient `%TEMP%`.
  fixture: a host with `node` on `PATH`, as gov's hooks already require.
  permission: a role agent runs no runner, a fixture copy included (scratch-guard row G2); the
  pass makes the probe.
- **AC11** — When a bash probe evaluates the edited runner's outer-root read, extracted as in AC10,
  with `GATE_OUTER_AMBIENT_TMP` naming an outer root A, `RG_SWEPT_TMP`
  reads A and the variable is unset after it; unset, `RG_SWEPT_TMP` reads `$GATE_AMBIENT_TMP`; and
  naming a missing directory, it prints the NOTE line and reads `$GATE_AMBIENT_TMP`. A second probe
  sourcing `owned-scratch.sh` and calling `scan_dead_work` over A, holding a planted
  `gate-work.dead` whose owner names a dead MSYS pid and the probe's git common dir, sweeps it. When
  the main loop runs the fixture bar of AC10 at the close with A holding `gate-work.dead` and two
  other entries, `TMPDIR` at an empty directory B and the variable exported as A, the sweep line
  names the planted pid, `gate-work.dead` is gone, the bar prints `TMPDIR entries 2`, its one leg,
  `bash -c '[ -z "${GATE_OUTER_AMBIENT_TMP+x}" ]'`, passes, and its own `gate-work.*` was made
  under B. Unset, the planted dir survives and the bar prints `TMPDIR entries 1`.
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
- **AC13** — When a bash probe sourcing `owned-scratch.sh` plants under one ambient dir four roots,
  each with a dead MSYS pid unless named: one whose common dir is absolute and names no directory,
  one naming another existing repository's common dir, one with a live pid and a missing common
  dir, and one whose missing common dir is relative, `scan_dead_work` removes only the first, and
  its sweep line names that pid; the same four with `py:` pids, under `scan_dead_scratch`, lose
  only the first. Each probe runs first with S9's directory test deleted, and the first survives.
  After the main loop's bar at the close, the two dead fixture roots the design section counts are
  gone from `%TEMP%`.
  Red when: an orphaned root survives, or a live, relative or existing-repository root is removed.
  figure: the two roots are PINNED at `ebab8b90b`; a pid reused since then would keep its root.
  permission: the bar is the main loop's; the pass makes the two probes.

No verdict moves: each touched suite keeps its arm lines and exit code (AC5), and the runners keep
their lines and their sweep of this repository's roots (AC6, AC7), widened only to orphaned owners
(AC13). The temp exports and the outer root move where temp lands and what is swept (AC10, AC11).

## 7. Gates

`ratchet (populated)` · `step-rows-frozen` · `encoding posture (text IO names its encoding)` · `pre-push self-test` · `pre-push bar self-test` · `shell-hygiene selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `run-gates turnstile` · `run-gates evidence` · `run-gates canary` · `run-gates gov canary` · `run-gates run-log line` · `pre-push run-log line` · `measure-legs selftest` · `run-selftests self-test` · `scratch-guard self-test` · `selftest harness self-test` · `history-store selftest` · `routed-commits selftest` · `kit/dogfood doc parity` · `transition-audit arms` · `straggler-guard arms` · `tier2-review self-test` · `codebase-map kit selftest` · `recall floor` · `recall floor arms` · `memory-recall kit selftest` · `process-monitor census selftest` · `runlog selftest` · `branch-reconcile selftest` · `lexicon selftest` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `playbook render selftest` · `policy fixtures` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `line length`

New arm: tools/gate-lint/encoding_posture.py · covers AC4 AC9 · the --cleanup mode's selftest rows; a planted swallowing removal split over two lines, and a TemporaryDirectory with ignore_cleanup_errors, each staged in a fixture tree · FLOOR_ASSERTIONS rises by the rows added
New arm: tools/lib/resolve-python.test.sh · covers AC8 · the four new PARITY_ROWS rows; each failing case is staged by one changed byte in a copy · none

The new cleanup leg, `cleanup posture (a tree removal that swallows its error)`, unrendered until
this unit builds, is declared in `tools/govkit/registry.toml` and rendered into
`tools/gate-legs.json`, and its RED and GREEN observation at the close is the main loop's, as are
the suite runs of AC5 and the fixture bars of AC10 and AC11. The bar runs once at the close.

## 8. Open questions

- **F1 — Does a sweep remove a dead owner's root whose common dir no longer exists?**
  - Two dead fixture roots, 20 entries [PINNED at `ebab8b90b`], name repositories their suites
    removed, and today's predicate keeps any root naming another common dir.
  - (a) Keep the predicate, and file the class as an ask beside TOOL-dQuietDisk-23.
  - (b) Widen both sweeps to a dead owner whose absolute common dir names no directory: S9, AC13.
  - Recommendation: (b), weighed against deny by default and a drive that is only absent for now.
  - RESOLVED (agent, 2026-11-22, delegated): (b), widen the sweep. The brief asks for zero residue
    after the next run; the sweep still requires a dead owner, and a bar's durable records live
    under its git dir, never in this scratch, so a missing repository leaves nothing of value to
    keep.

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft. Order 6, not the briefed 1. The population spans files
  TOOL-dQuietDisk-1 (`tools/lib/resolve-python.test.sh`), TOOL-dQuietDisk-7 and -11
  (`tools/govkit/fixture_target.py`), TOOL-dQuietDisk-8 (`tools/policy/check_policy.py`),
  TOOL-dQuietDisk-5 and -15 (`tools/run-gates/run-gates.sh`), TOOL-dQuietDisk-16
  (`tools/govkit/upgrade_steps.py`) and TOOL-dQuietDisk-17 and -18 (`tools/govkit/selftest.py`)
  write, at orders 1 to 5. No unit depends on this one, so it runs after all of them and moves the
  sites they leave.
- rev-2 · 2026-11-22 · closes TOOL-dQuietDisk-27 and re-grounded at b3f5a2bc3 (dWitnessedBar's
  land tip merged), under `2026-11-22-prompt-TOOL-dQuietDisk-1-reground-task`. Ask 27's two gaps
  join as S7 and S8, with AC10 to AC12: `TEMP` and `TMP` exported beside `TMPDIR` by both runners,
  and `GATE_OUTER_AMBIENT_TMP`, the outer runner's ambient root, read for the count and the sweep
  and classed inert in the pre-push knob census. S2 exports the three names from the Python face
  too, the same class. S4 states the three helpers the lifted block calls. What moved: the
  owned-root block to `run-gates.sh` lines 2399 to 2465, unchanged in body; the population to 45
  `rmtree` and 11 `TemporaryDirectory` sites in 21 files, and the hooks to 23 files [PINNED], so the file
  list is re-derived; the registry exemption to line 253; the base to `b3f5a2bc`.
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
- rev-5 · 2026-11-22 · re-grounded at ebab8b90b (orders 1 to 4 built), under
  `2026-11-22-prompt-TOOL-dQuietDisk-17-reground-task`. What moved: the population to 51 `rmtree`
  and 11 `TemporaryDirectory` sites in 25 files and the file list to 46 [PINNED at `ebab8b90b`],
  adding `template_cache.py` and the three `history_store.py` copies; the knob census to line 2115.
  The goal holds; scope and acceptance moved for reasons the re-read found. S4: the self-test runner
  carries no `health_log_sh` block, which rev-2 said it did, and its startup and attribution scratch
  sat outside rev-2's root, so it gains the block and one startup root holding all three (AC6, AC7).
  S3: rev-2's import rule has no path for `history_store.py`'s whole copies or `template_cache.py`'s
  by-path load, so every file carries its blocks inline. S2: the cache's walk is the owned-root
  walk's second instance, so it becomes `owned_work_py` (AC2, AC7, AC8's four rows). S6:
  `tools/gate-legs.json` is rendered, so the leg is a gov-only `[[exempt_leg]]` with a `[[ledger]]`
  row (AC4). The design section states the saving measured and the git processes added. F1 was
  resolved (b) by the main loop under the run's mandate, adding S9 and AC13, and
  TOOL-dQuietDisk-17's retirement leaves `selftest.py` as units 18 and 11 left it.
- rev-6 · 2026-11-22 · the first build pass's divergences, ruled under
  `2026-11-22-prompt-TOOL-dQuietDisk-9-divergence-task`. S3 excludes every program a landed
  `[[upgrade]]` row names, which `check_frozen` freezes: three step programs leave the file list,
  their two cleanup sites become the ledger's two waived rows, and the kickoff step's hook stays,
  so section 3, AC4 and the alternatives follow. S4 states its two command substitutions and the
  `pure-fn-subst` row the second grows. Section 7 names the cleanup leg, `ratchet (populated)`,
  which the ledger now populates, and `step-rows-frozen`. Kit versions still move only at the
  close's mint. The next pass builds on `TOOL-dQuietDisk-9-build.patch`, 56 files [PINNED, the
  divergence task's count]; the record keeps `TOOL-dQuietDisk-9-frozen-steps.patch`, not applied.

## 10. Reuse audit

The seams extended: the bar's owner record and dead-owner sweep
(`tools/run-gates/run-gates.sh#write_work_owner`, `#scan_dead_work`, TOOL-dDerivedDocket-25), lifted
into one block, and its owned-root block, which S7 and S8 extend in place; the hook of
`tools/memory-tree/deviation_join.py#remove_tree`, the canonical `remove_tree`; the cache's walk
(`tools/lib/template_cache.py#TemplateCache`), which becomes `resolve_owned_work`; `health_log_sh`,
one more parity-held copy; the copy rule of `PARITY_ROWS`;
`tools/gate-lint/encoding_posture.py`'s AST population walk and its shrink-only ledger through
`legacy_ledger`; and the gov-only leg shape of `spawn budget (forks per hot entrypoint)`.

`python tools/codebase-map/reuse_lookup.py "remove a scratch tree with a chmod and retry handler"`,
re-run at `ebab8b90b`, ranked `remove_tree` in six files, `tools/govkit/upgrade_walk.py` and
`tools/memory-tree/deviation_join.py` among them. A probe for the owned-root walk returned none; it
was found by reading `template_cache.py`.

Recall returned TOOL-dSweptScratch-1 (CLOSED, `5a311c9fa`), whose §3 put a killed run's leak out of
its reach, which this unit reaches; TOOL-aBranchedMandate-6, which measured the read-only objects;
and TOOL-dQuietDisk-23, the other G-C clauses. The owning chain build is dWitnessedBar (Test: gate
health), now landed and merged at `40def53f7`. Its own files the population moves are
`tools/run-gates/verdict_flow.py`, `tools/run-gates/leg_factory.py` and
`tools/run-gates/verdict_backends.py`, and the knob census S8 joins classes names from its units 5,
8, 25, 40 and 56. Since `b3f5a2bc3`, units 1, 5, 7, 11 and 12 changed files this unit edits,
outside the blocks it moves. Ask TOOL-dQuietDisk-27's source is the incms session's
`fix4-incms-notes-for-gov.md` in the shared notes folder; `fix4-incms-landed.md` records that incms
owes the one export line once gov builds the variable.

Recall terms used: rmtree ignore_errors onexc remove_tree chmod read-only scratch owned sweep gate-work owner TMPDIR TEMP TMP ambient nested outer runner knob census template cache root walk health log exempt leg
