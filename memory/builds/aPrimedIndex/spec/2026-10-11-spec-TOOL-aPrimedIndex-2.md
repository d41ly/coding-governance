# TOOL-aPrimedIndex-2 — one runner verb rewrites every declared output in stage order, and a second names each stale one

**Status:** CLOSED · rev-2 · 2026-10-11 · node a · Tier-2 · base b726385f · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aPrimedIndex-2-1-acceptance-ledger.md](../build/2026-10-11-build-TOOL-aPrimedIndex-2-1-acceptance-ledger.md) | journal | — |
| [2026-10-11-prompt-TOOL-aPrimedIndex-1-2-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aPrimedIndex-1-2-build-brief.md) | journal | TOOL-aPrimedIndex-1 TOOL-aPrimedIndex-3 TOOL-aPrimedIndex-4 |
| [2026-10-11-prompt-TOOL-aPrimedIndex-1.md](../prompts/2026-10-11-prompt-TOOL-aPrimedIndex-1.md) | research | TOOL-aPrimedIndex-1 TOOL-aPrimedIndex-3 TOOL-aPrimedIndex-4 |
| [2026-10-11-review-TOOL-aPrimedIndex-1-4-implementation-diff-round1.md](../reviews/2026-10-11-review-TOOL-aPrimedIndex-1-4-implementation-diff-round1.md) | diff-review | TOOL-aPrimedIndex-1 TOOL-aPrimedIndex-3 TOOL-aPrimedIndex-4 |

<!-- /gen:spec-records -->

## 1. Goal

Give a session one command that regenerates every output the kits declare, in the order their inputs
require, and one that names each stale output without writing anything, so a session never has to
know which generator a red leg wanted.

## 2. Scope (IN)

- **S1** — A new kit file, `regen.py` in the run-gates kit, reads every tracked kit descriptor beside
  its own kit, resolves the rows TOOL-aPrimedIndex-1 declares into regeneration items, and refuses a
  malformed row. Observed by AC1 and AC2.
- **S2** — `--list` prints every item in run order: stage, kit, outputs, write argv, check argv, and
  a count line. Observed by AC1.
- **S3** — `--check` runs every item's check concurrently, each bounded, and prints one verdict line
  per item, then a count line. It writes nothing. It exits 0 when every item is fresh, 1 when any is
  stale or its check failed or timed out, and 2 when the declaration was refused. Observed by AC3.
- **S4** — `--write` runs every item's write, stage by stage, the items of one stage concurrently,
  and prints the files each stage moved. A failing write stops before the next stage. It exits 0, 1
  on a failed write, or 2 on a refused declaration. Observed by AC4.
- **S5** — Untracked files are named before a `--write`, because the build-index generator
  enumerates with `git ls-files` and does not see a record that has not been added. Observed by AC4.
- **S6** — `run-gates.sh` takes `--regen`, `--regen-check` and `--regen-list` as its first argument
  and hands over to `regen.py` with the interpreter it already resolves, before any bar machinery
  starts. Observed by AC5.
- **S7** — The kit README documents the three verbs, the exit codes and the two knobs. Observed by
  AC5.

## 3. Non-goals (OUT)

- The bar does not call it yet; TOOL-aPrimedIndex-3 wires the check into the runner.
- No commit. A session commits what `--write` moved.
- No guard or input set per item: every declared item is checked on every call. A guard would cost
  an early signal when it is too narrow and is left to a later build that measures the need.

### Edges

- **consumes-from** `TOOL-aPrimedIndex-1` — the declared rows; with none the verb reports an empty set.
- **hands-off** `TOOL-aPrimedIndex-3` — calling `--check` before a bar and refusing on its exit.
- **hands-off** `TOOL-aPrimedIndex-4` — calling `--write` over the lander's merged tree.

## 4. Design

### Resolution

1. The tree is the current directory's git toplevel, the one the runner has already moved into, so a
   suite driving the runner from a scratch repository grades that repository, as the runner's legs
   do. The tool root is where this kit sits below its OWN repository, found by walking up to the
   directory holding `.git`, the walk `derive_self_rel` in `tools/unattended/lib-unattended.sh`
   makes and for its reason; that relative path is applied to the tree. Neither is spelled.
2. Descriptors are `git ls-files` over `<tool root>/*/kit.toml` in the tree, tracked only, as the
   unattended reader enumerates them. Each is parsed with `tomllib`; one that does not parse is a refusal
   naming it.
3. `{kit}` is the descriptor's directory, `{prefix}` the tool root, `{memory_root}` the
   `MEMORY_ROOT` of `.memory-tree.conf` (default `memory`) and `{map_root}` the `MAP_ROOT` of
   `.codebase-map.conf` (default `{memory_root}/map`). A `when` is evaluated as the unattended reader
   evaluates it. A token left unresolved refuses the row.
4. An argv beginning `python` or `python3` runs under `sys.executable`; any other program is
   resolved on `PATH` before it runs. Windows' process creation searches its system directory before
   `PATH`, and on a node with WSL installed the `bash` there is WSL's, which cannot read a linked
   worktree's `.git` file: every Git-Bash check read "not a git repo" in TOOL-aPrimedIndex-1's pass.
   Every command runs from the repo root.
5. Rows with one `write` and one `check` join into one item listing all their outputs; a
   `[[regenerate]]` row's output is named by its kit. Two rows of one item declaring different
   stages refuse.

### Output

Every line starts `regen:`. A stale item prints its check command and the last eight lines of its
output, indented, so the reason is on screen without opening a log. The count line reads
`regen: <n> declared · <f> fresh · <s> stale · <t>s`, every figure derived.

### Knobs

`GATE_REGEN_JOBS` bounds concurrency, default 4. `GATE_REGEN_BOUND` bounds each command in seconds,
default 900; a command that outlives it is killed and its item reads `TIMEOUT`.

### Inventory

Functions in `regen.py`, each led by a verb of the closed table in `.lexicon.conf`: `main`,
`derive_repo_root`, `read_toplevel`, `read_conf_value`, `read_descriptors`, `read_knob`, `resolve_argv`,
`check_when`, `check_stage`, `build_items`, `add_item`, `render_argv`, `run_command`, `run_checks`,
`run_writes`, `read_dirty_paths`, `print_items`, `print_tail`; one exception class, `Refusal`. In
`run-gates.sh`, the hand-over is inline in the argument case and defines no function.

### Files touched (estimate)

- `tools/run-gates/regen.py`
- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-gates.test.sh`
- `tools/run-gates/README.md`
- `memory/map/features/run-gates.md`

### Alternatives rejected

- **A bash reader.** Argv arrays in TOML are what the existing awk readers cannot parse; they read
  scalar strings only, by design.
- **govkit as the reader.** govkit does not ship to adopters, so an adopter would hold declarations
  and no reader.
- **Writes run serially.** Concurrency inside a stage is safe because the stage's outputs are
  disjoint, which §4's inventory shows, and a serial `--write` costs the sum of eleven commands.

## 5. Production-readiness checklist

- security: runs only argvs from tracked descriptors, with no shell, from the repo root.
- perf / scale: bounded concurrency and a bound per command; the cost on node `a` is recorded at
  build.
- error / empty / loading states: an empty set prints a zero count and exits 0; a refused row exits
  2 naming the descriptor and the key.
- observability: one line per item and a derived count line, so a probe that cannot move says so.
- risks: a generator that reads untracked files and one that does not disagree about a fresh record,
  which S5 names before the write.
- testing: arms in the run-gates canary on a fixture descriptor; direct observation in a scratch
  clone.
- migration: none; a new file and a new argument.
- user docs: the kit README (S7).

## 6. Acceptance criteria

- **AC1** — When `regen.py --list` runs from the repo root of this tree, it prints the items of
  TOOL-aPrimedIndex-1's inventory in stage order and a count line equal to their number. Red when:
  an item is missing, out of stage order, or printed twice.
  figure: DERIVED by the verb from the descriptors at run time.
- **AC2** — When a fixture descriptor in a scratch clone declares a `[[generated]]` row carrying
  `write` and no `check`, `regen.py --list` exits 2 naming that descriptor.
  Red when: the row is read, skipped silently, or the verb exits 0.
  fixture: a scratch clone under the session scratchpad, built and removed at build time.
- **AC3** — When `memory/gotchas/INDEX.md` is edited by one row in a scratch clone,
  `regen.py --check` from its repo root exits 1 with a `STALE` line naming the gotchas item and
  writes nothing; on the untouched clone it exits 0 with every item fresh. Red when: the edited clone
  exits 0, or `git status --porcelain` changes during the check.
  cost: about two minutes on node `a`.
- **AC4** — When the same edited clone runs `regen.py --write` from its repo root, it restores
  `memory/gotchas/INDEX.md`, names it among the moved files, and a following `--check` exits 0.
  Red when: the file stays stale, or a stage runs after a failed write.
- **AC5** — When the runner is handed `--regen-list` as its first argument, its output equals
  `regen.py --list`, and `grep -n "regen" tools/run-gates/README.md` shows all three verbs.
  Red when: the argument reaches the bar's setup, or a verb is undocumented.

## 7. Gates

`codebase-map coverage + freshness` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `install-prefix (shipped surface)` · `line length` · `memory hygiene` · `recall floor` · `recall floor arms`

New arm: tools/run-gates/run-gates.test.sh · covers AC2 AC3 · a fixture descriptor with a partial row, and a fixture check that exits 1 · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.
- rev-2 · 2026-10-11 · §4 · S1 · a program other than python is resolved on `PATH` before it runs;
  TOOL-aPrimedIndex-1's pass found WSL's `bash` taken ahead of Git-Bash's.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py` named `resolve_generated_indexes` in
`tools/unattended/lib-unattended.sh` as the seam that already enumerates these descriptors; this
verb repeats its enumeration and `when` rule in python, because the new keys are TOML arrays its awk
cannot read and a copy-installed kit cannot source another kit. The repo-root walk is
`derive_self_rel`'s. govkit's `derive_regenerate_argvs` resolves the same tokens but does not ship.

Recall terms used: `python tools/memory-recall/query.py "is regenerating generated indexes enforced before the merge bar runs, so a stale index does not red the bar" --terms "generated index stale regen render --write freshness leg bar pre-push lander prepare gotchas symbols LIVE.md"`.
