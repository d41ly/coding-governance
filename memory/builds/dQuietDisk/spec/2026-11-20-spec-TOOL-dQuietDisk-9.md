# TOOL-dQuietDisk-9 — every scratch path under one owned, swept root, and every tree removed by one chmod-and-retry helper

**Status:** SPECCED · rev-1 · 2026-11-20 · node d · Tier-2 · base 609cd40b · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |

<!-- /gen:spec-records -->

## 1. Goal

A killed suite or runner leaves its scratch behind, and a Python removal that swallows its error
leaves git's read-only objects in the temp folder on Windows
(`memory/builds/dQuietDisk/build/2026-11-20-build-TOOL-dQuietDisk-19-analysis.md`, §8 and rework
K12). This unit gives Python one removal helper and one owned-root helper, gives bash the bar's own
owner record and dead-owner sweep as one shared block, moves every swallowing removal onto the
helper, and adds a lint that reds a new one.

## 2. Scope (IN)

- **S1** — `tools/lib/owned_scratch.py`, the canonical module, holding two marked blocks.
  `remove_tree_py` defines `remove_tree(path)` and `scratch_dir()`. `remove_tree` calls
  `shutil.rmtree` with an `onexc` hook that clears the read-only bit on the failing path and retries
  it once, never raises, and returns whether the path is gone. `scratch_dir()` is a context manager
  over `tempfile.mkdtemp()` whose exit calls `remove_tree`. `onexc` alone is used, because the
  declared python floor is 3.15, the value `tools/lib/python-floor.txt` holds at `609cd40b1`.
  Observed by AC1.
- **S2** — The block `owned_tempdir_py` defines `enter_owned_tempdir()`. When the process's temp dir
  sits inside a `gate-work.*` directory holding an `owner` file, it sets `tempfile.tempdir` to that
  temp dir and returns it. Otherwise it first sweeps each `gate-work.*` under the temp dir whose
  owner line names a `py:` pid that is not alive and this repository's git common dir. It then
  makes its own `gate-work.*` with an owner line `py:<pid>TAB<common dir>TAB<epoch>`, written
  tmp-then-rename, sets `tempfile.tempdir` to its `tmp`, and registers `remove_tree` of it at exit.
  A pid that cannot be judged reads as alive. Observed by AC2 and AC3.
- **S3** — Every `shutil.rmtree(..., ignore_errors=True)` and every
  `TemporaryDirectory(..., ignore_cleanup_errors=True)` under `tools/`, `skills/` and `.githooks/`
  moves to `remove_tree` and `scratch_dir`. Every hand-written chmod-and-retry hook in those trees
  moves to `remove_tree` too. A gov-internal file imports the canonical module; a file a kit ships
  carries the blocks inline. Each Python suite entry point in that population calls
  `enter_owned_tempdir()` before its first scratch. Observed by AC4 and AC5.
  **Readers:** by name: `remove_tree`, which `tools/loop/loop_witness.py` calls through the
  memory-tree kit's `deviation_join` and which the inline block keeps; each local hook's other
  callers sit in its own file and call `remove_tree` after the move ·
  by value: NO VALUE READERS — no caller reads a removal's result today, and S1's return is new.
- **S4** — The bash face, the canonical block `owned_work_sh` in `tools/lib/owned-scratch.sh`. It
  defines `write_work_owner <dir> <common>` and `scan_dead_work <ambient> <own dir> <common>`, lifted
  from `run-gates.sh`'s two functions with their globals made arguments. `run-gates.sh` carries the
  block in their place and calls it with `$WORK`, `$GATE_AMBIENT_TMP` and `$WORK_COMMON`, so its
  lines and health events are unchanged. `run-selftests.sh` carries it too: its sweep root becomes
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

## 3. Non-goals (OUT)

- No bash `rm -rf` rewrite. MSYS `rm -rf` removes git's read-only objects, and the bash leaks
  dSweptScratch measured were bookkeeping it fixed (TOOL-dSweptScratch-1, §4).
- No new sweeper. A bash-owned root is swept by `scan_dead_work`, a Python-owned one by the next
  `enter_owned_tempdir()`. Each judges only its own pid kind: bash's `kill -0` cannot judge a
  Windows pid, so `py:` lines are skipped by the bash scan, whose `case` already refuses a
  non-numeric pid (`tools/run-gates/run-gates.sh#scan_dead_work`).
- No cleanup ledger seeded with today's sites. S3 moves every one, so the ledger starts with its
  header and no row.
- The other G-C lint clauses: `git init` outside the template helper, a spawn inside a loop body,
  `copytree` of a kit, `clone --no-hardlinks` and an unrooted `mktemp`. They are TOOL-dQuietDisk-23.
- No kit version bump by hand: `govkit.py mint` writes every owed bump at the lander.
- No policy key. Removing a tree and owning a root save no answer, so the cache rule does not reach
  them, and their off value would be a leak.

### Edges

none

## 4. Design

### Where the code was read

Code at `609cd40b1`, the tip of `branch/unattended-dwitnessedbar-2ed3b3`, by symbol or as
`<path>@609cd40b1:<line>`. The population was also read at this branch's HEAD `a5537b925`, because
TOOL-dSweptScratch-1 landed on main after dWitnessedBar forked and moved many sites.

### The population, read over the real tree first

The predicate: an AST `Call` whose callee is named `rmtree` with the keyword `ignore_errors=True`,
or `TemporaryDirectory` with `ignore_cleanup_errors=True`, over every tracked `*.py` under `tools/`
and `skills/`. Run on 2026-11-20:

| Tree | `rmtree` sites | `TemporaryDirectory` sites | Files | Of them, shipped by a kit |
|---|---|---|---|---|
| `609cd40b1` | 59 | 11 | 33 | 22 files, 40 sites |
| HEAD `a5537b925` | 35 | 11 | 15 | 12 files, 26 sites |

The 11 `TemporaryDirectory` sites are all in `tools/govkit/upgrade_steps.py` (10) and
`tools/govkit/selftest.py` (1). A line grep finds 57 and 12 at `609cd40b1`; the AST reads a call
split across lines, which the grep misses. "Shipped" is `python tools/govkit/govkit.py shipped` at
HEAD. The hand-written hooks, `git grep -nE "onexc|onerror"` at HEAD, sit in 19 files, among them
`tools/memory-tree/deviation_join.py#remove_tree`, `tools/govkit/upgrade_walk.py#remove_tree` and
`tools/govkit/step_gate.py`. The build's base is the merge of both lines, so the builder re-runs the
predicate there with `--cleanup --measure` and moves what it prints. figure: DERIVED at the build's
base; the table is PINNED at the two shas named.

### The copy rule

`tools/lib/` ships nothing (`tools/govkit/registry.toml@609cd40b1:237`), so a shipped file carries
the block inline between `# >>> remove_tree_py — canonical copy: owned_scratch.py in gov's lib dir`
and `# <<< remove_tree_py`, as `common_dir.py`'s copies do (`tools/lib/common_dir.py`), and the
parity table holds each copy to the canonical block (`tools/lib/resolve-python.test.sh@609cd40b1:405`).
`deviation_join.remove_tree` keeps its name because `loop_witness.remove_tree` calls it.

### The owner line both faces read

```text
<pid>\t<git common dir>\t<start epoch>      bash: an MSYS pid, judged by kill -0
py:<pid>\t<git common dir>\t<start epoch>   python: a native pid, judged by the OS
```

The Python liveness check is `os.kill(pid, 0)` on POSIX and `OpenProcess` with
`GetExitCodeProcess` on Windows. Any error is "alive", the direction that keeps a directory.

### Inventory

| Minted identifier | Kind | Naming cell | Graded by |
|---|---|---|---|
| `remove_tree_py`, `owned_tempdir_py`, `owned_work_sh` | parity block markers | `PARITY_ROWS` | `tools/lib/resolve-python.test.sh` |
| `remove_tree`, `scratch_dir`, `enter_owned_tempdir` | Python functions | none | the probes of section 6 |
| `--cleanup`, arm `cleanup` | scanner mode and arm | the scanner's `ARMS` tuples | its `--selftest` |
| `cleanup-sites` | ledger population | `.memory-tree.conf` `PROJECT_REGISTRY_EXTRA` | `memory hygiene` |
| `cleanup posture (a tree removal that swallows its error)` | gate leg | `tools/gate-legs.json` | `run-gates canary` |

### Files touched (estimate)

`tools/lib/owned_scratch.py` · `tools/lib/owned-scratch.sh` · `tools/lib/resolve-python.test.sh` ·
`tools/run-gates/run-gates.sh` · `tools/run-gates/run-selftests.sh` ·
`tools/gate-lint/encoding_posture.py` · `memory/project/cleanup-sites.txt` · `.memory-tree.conf` ·
`tools/gate-legs.json` · `memory/guides/SESSION-KICKOFF.md`

Plus every file the predicate and the hook grep name at the build's base. At HEAD those are:

`tools/branch-reconcile/selftest.py` · `tools/govkit/fixture_target.py` · `tools/govkit/selftest.py` ·
`tools/govkit/upgrade_steps.py` · `tools/govkit/upgrade_walk.py` · `tools/govkit/step_gate.py` ·
`tools/loop/factories.py` · `tools/loop/claims.py` · `tools/memory-recall/check-recall.py` ·
`tools/memory-recall/query.py` · `tools/memory-recall/test_recall_floor.py` ·
`tools/memory-recall/selftest.py` · `tools/memory-tree/gen_build_index.py` ·
`tools/memory-tree/deviation_join.py` · `tools/memory-tree/commit_trailers.py` ·
`tools/playbook/check_layers.py` · `tools/playbook/fixtures/composition.py` ·
`tools/playbook/edge_grammar.py` · `tools/playbook/gov_tag.py` · `tools/playbook/load_sets.py` ·
`tools/playbook/writing_practice.py` · `tools/policy/check_policy.py` ·
`tools/process-monitor/selftest.py` · `tools/run-gates/held_halves.py` ·
`tools/run-gates/measure_legs.py` · `tools/run-gates/check-receipt.py` ·
`tools/run-gates/owed_rows.py` · `tools/runlog/selftest.py` · `tools/lexicon/selftest.py` ·
`tools/lib/commit_trailers.py` · `tools/unattended/commit_trailers.py` ·
`.githooks/pre_push_bar_selftest.py`

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
  never swept.
- perf / scale: `enter_owned_tempdir` lists the temp dir's `gate-work.*` entries once per suite;
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
- user docs: N/A — no page under `help/` names a cleanup call or a scratch root.

## 6. Acceptance criteria

- **AC1** — When a probe under `%TEMP%/<short-name>` makes a repository with a commit, so its
  `.git/objects` hold read-only files, and calls `remove_tree` on it, the call returns True and the
  path is gone. With the hook's `os.chmod` deleted, the path survives and the call returns False
  without raising.
  Red when: the read-only objects survive, or a failure raises.
- **AC2** — When a probe runs with `TMPDIR` inside a planted `gate-work.x/tmp` holding `gate-work.x/owner`,
  `enter_owned_tempdir()` returns that `tmp` and makes no directory. Run with an ambient `TMPDIR`, it
  makes one `gate-work.*` holding an owner line that starts `py:`, and the directory is gone after
  the process exits.
  Red when: a nested run makes a second root, or a direct run's root outlives it.
- **AC3** — When a probe plants, under one ambient dir, a root owned by a dead `py:` pid of this
  repository, one by a live `py:` pid, one by a dead `py:` pid of another common dir, and one by a
  bash pid, and calls `enter_owned_tempdir()`, only the first is removed.
  Red when: a live, foreign or bash-owned root is removed.
- **AC4** — When `python tools/gate-lint/encoding_posture.py --cleanup --measure . tools skills .githooks`
  runs at the unit's tip, it prints no `cleanup` line, and the graded run with the registry
  argument exits 0. One planted `shutil.rmtree(p, ignore_errors=True)`
  split over two lines reds the graded run naming its file.
  Red when: a split call is missed, or a site survives the move.
- **AC5** — When each suite S3 touched is run directly in a scratch `git clone --shared` of gov with
  `TEMP`, `TMP` and `TMPDIR` pointed at an empty directory, it prints the same arm lines and exit
  code as at the build's base, and the directory holds 0 entries after it exits. The unattended
  kit's suites are excluded, as the owner's rule of 2026-08-23 requires.
  Red when: an arm's result moves, or an entry remains.
  cost: the touched suites run in full once each, some for minutes.
  figure: DERIVED at observation; the residual at the build's base is recorded beside it.
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
- **AC9** — When `python tools/gate-lint/encoding_posture.py --selftest` runs, it prints its count
  line at or above the raised `FLOOR_ASSERTIONS` and exits 0. With the `--cleanup` arm's keyword
  test inverted, it exits 1.
  Red when: the new mode's rows do not execute.

No verdict moves: each touched suite keeps its arm lines and exit code (AC5), and the runners keep
their lines and their sweep predicate for bash-owned roots (AC6, AC7).

## 7. Gates

`encoding posture (text IO names its encoding)` · `shell-hygiene selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `run-gates turnstile` · `run-gates evidence` · `run-gates canary` · `run-gates gov canary` · `run-gates run-log line` · `pre-push run-log line` · `measure-legs selftest` · `run-selftests self-test` · `scratch-guard self-test` · `routed-commits selftest` · `kit/dogfood doc parity` · `transition-audit arms` · `straggler-guard arms` · `tier2-review self-test` · `codebase-map kit selftest` · `recall floor` · `recall floor arms` · `process-monitor census selftest` · `runlog selftest` · `branch-reconcile selftest` · `lexicon selftest` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `playbook render selftest` · `policy fixtures` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `line length`

New arm: tools/gate-lint/encoding_posture.py · covers AC4 AC9 · the --cleanup mode's selftest rows; a planted swallowing removal split over two lines, and a TemporaryDirectory with ignore_cleanup_errors, each staged in a fixture tree · FLOOR_ASSERTIONS rises by the rows added
New arm: tools/lib/resolve-python.test.sh · covers AC8 · the three new PARITY_ROWS rows; each failing case is staged by one changed byte in a copy · none

The new cleanup leg itself is declared in `tools/gate-legs.json`, and its RED and GREEN observation
at the close is the main loop's. The bar runs once at the close.

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

## 10. Reuse audit

The seams extended: the bar's owner record and dead-owner sweep
(`tools/run-gates/run-gates.sh#write_work_owner`, `#scan_dead_work`, TOOL-dDerivedDocket-25), lifted
into one block rather than copied; the chmod-and-retry hook of
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
health); its branch changes `run-gates.sh` and `run-selftests.sh`, and no spec of it at
`609cd40b1` changes the owner record or the sweep.

Recall terms used: rmtree ignore_errors onexc remove_tree chmod read-only scratch owned sweep gate-work owner TMPDIR
