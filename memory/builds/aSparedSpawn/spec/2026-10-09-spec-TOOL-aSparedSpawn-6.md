# TOOL-aSparedSpawn-6 — the unattended driver as a library, called in process by its suite

**Status:** OPEN · rev-1 · 2026-10-09 · node a · Tier-2 · base 22efab65 · streams tooling · order 1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Make `tools/unattended/unattended.sh` sourceable, so its suite sources it once per shard and runs
each arm as `( load_driver_conf && main "$@" )` in a subshell instead of a fresh `bash` process. The
research estimates about 1900 s quiet to 8100 s loaded of pool work saved against a 17142 s pooled
reading (`research2-inprocess` §5, static counts at `6bc6c949c`), conditional on the fork price that
unit 0 below measures first.

## 2. Scope (IN)

- **S1** — Unit 0, the measurement, before any code. In a shell that has sourced the driver, time 20
  `( : )` forks against 20 in a bare shell, quiet and under an 8-shard load; record both figures and
  the instrument. The build stops at this step if the loaded fork in the sourced shell exceeds 3 s,
  the price above which the research says the harness loses. Observed by AC1.
- **S2** — `load_driver_conf()` wraps the conf-dependent preamble: the `GATE_BACKSTOP_MARGIN` seam
  (`unattended.sh:412-417`), `ROOT`, the `cd`, the conf refusal and `. "$CONF"` (`:479-543`), the
  closed sets and `read_bound_key` reads (`:559-629`), `SHARED_RECORDS` and `GENERATED_INDEXES`
  (`:645-671`), `REVIEW_ROUNDS` and its runaway check (`:843-847`) and `PROCFS_ROOT` (`:1463`). It
  EXITS on a refusal, as today. `observe_remote` (`:455`) moves above it. Nothing is re-indented, so
  column-0 greps still match. Observed by AC2, AC5.
- **S3** — `main()` wraps the argv state, the runlog install, the parse loop and the dispatch
  (`:13156-13363`). `refuse_waive_unless_preflight` (`:13194`) moves above it as a top-level
  definition. Every `exit` keeps its `RUNLOG_CLEAN=1` marker. Observed by AC2, AC3.
- **S4** — The entry: the file's last lines return when sourced and run `load_driver_conf` then
  `main "$@"` when executed. `main` refuses with rc 2, naming the leak, when sourced and
  `BASH_SUBSHELL` is 0. Observed by AC2, AC4.
- **S5** — The `$0` and `$$` sites. `KIT_DIR` and `SELF` (`:84`, `:120`) read `BASH_SOURCE[0]`. The
  three `--hold` remedy lines (`:10249`, `:10263`, `:10304`) print `DRIVER_ARGV0`, which is `$0` when
  executed and `BASH_SOURCE[0]` when sourced. The process-ledger, group-id and runlog sites
  (`:1509-1510`, `:10167-10168`, `:12973`, `:12989`) read `$BASHPID`. Observed by AC3.
- **S6** — The harness in the same suite file: source the driver once per shard, define `run_proc`
  as the old process `run`, and point `run` at the subshell body. The wrappers that call
  `bash "$SCRIPT"` become subshell bodies. The real-process classes stay on `run_proc`: the missing
  library (`unattended.test.sh:6995`), the stripped self-read (`:2827`), mutated copies, the
  commit-msg hook path, `timeout` shadowed through `PATH`, claim-lock concurrency and the process
  ledger. The research puts these at about 35-45 call sites. Observed by AC6, AC9.
- **S7** — The parity table, about 30 rows covering every verb at least once with rc 0, 1 and 2, an
  argv refusal, `--plan --framed` over two slugs, an `--abort`, and a conf holding `declare`. Each row
  compares `run_proc` and `run` on output through `render_stable`, rc, and `derive_tree_digest`.
  Observed by AC7.
- **S8** — Two source-level arms: the namespace arm, which reds when a top-level suite function
  shares a driver function's name, and the top-level-exit arm, which derives every column-0 `exit`
  outside the two function spans and reds unless a `run_proc` arm names it. The nine colliding suite
  helpers the research found are renamed or fenced inside `( … )`. Observed by AC8.
- **S9** — The liveness counters: each shard ends with a line
  `harness: <a> in-process calls, <b> process calls`, and a flipped shard with `a` at 0 reds. `UNATTENDED_HARNESS=process` redefines `run` as
  `run_proc` for the equivalence run. Observed by AC9.
- **S10** — Arm inventory unchanged across the unit, compared before and after. Observed by AC5, AC6.

## 3. Non-goals (OUT)

- Splitting the driver into a library file and a thin entry. `check-arms.py` discovers a gate as a
  tracked `.sh` defining `fail()` with `fail <n> "` sites (`tools/memory-tree/check-arms.py:216-233`);
  moving the sites out would drop them from the population in silence.
- Predicate-level calls or a `--serve` coproc. The research rejects both (§3c).
- The runlog-writer suite. It stays a process suite and keeps grading the EXIT trap and exit shapes.
- Moving the kit-only half of the conf preamble to source time. Measured later, if at all.
- Any change to `tools/unattended/check-unattended.sh` or its suite; that is the hand-off below.

### Edges

- **consumes-from** `TOOL-aSparedSpawn-8` — the fork-free readers. Every in-process call still forks
  once, in a shell that now holds the whole driver, so the verb bodies' `$(fact …)` forks are paid at
  the heavier price until that unit removes them.
- **hands-off** `TOOL-aSparedSpawn-7` — the `--only core` and `--only <N>` selectors of
  `check-unattended.sh`, and the migration of its suite's arms onto them.

## 4. Design

### The driver: one file, two entry shapes

```bash
# A sourced driver defines and returns; an executed one loads its conf and runs.
[ "${BASH_SOURCE[0]}" = "$0" ] || return 0
load_driver_conf
main "$@"
```

`GIT_GRAFT_FILE` stays exported at the top level; the suite's graft control already uses
`env -u GIT_GRAFT_FILE`. `. "$CONF"` inside a function makes a conf `declare`, `typeset` or `local`
function-local and a conf `return` end the load early. Gov's conf has none of these (research,
0 hits); the parity table carries one row for it.

### The harness

```bash
. "$SCRIPT" || { echo "FAIL the driver did not source, so no arm below runs in process"; exit 2; }
run()      { DRV_INPROC_N=$((DRV_INPROC_N+1)); ( load_driver_conf && main "$@" ) 2>&1; }
run_proc() { DRV_PROC_N=$((DRV_PROC_N+1)); bash "$SCRIPT" "$@" 2>&1; }
```

The `( … )` is explicit on every call. The suite has `$(run …; run …)` forms, and an elided subshell
would let the first `main`'s `exit` end the rest of the substitution. An environment prefix on a
function call is exported to that function's children, so `CLAUDE_PID=4242 run …` carries over. A
wrapper that ran `env -u X … bash "$SCRIPT"` becomes a subshell body:
`( cd "$d" && unset X && load_driver_conf && main "$@" ) 2>&1`.
A bare `VAR=v load_driver_conf` would scope `VAR` to the load alone. The driver
already isolates `--plan` slugs the same way, `( verb_plan "$_pl_s" )` (`unattended.sh:13292`).

### Migration

In order, each step landing on its own with the inventory compared:

1. Unit 0 (S1). No code.
2. The driver refactor (S2-S5). `run` is still a process, so the whole suite must be green unchanged.
   Run `gen_map.py --write`, because new functions stale `symbols.json`.
3. `run_proc`, an unused in-process body, the parity table and the two source-level arms (S6-S8).
4. Flip shard 1, then shards 2 to 8, one step each, moving each shard's process-class sites to
   `run_proc` (S6, S9).

The inventory comparison, before and after every step:

1. `check-arms.py --report` rows for the driver, normalised to gate, check, ordinal, signature, state
   and armed-by file with the line column dropped. The diff must be empty, and `--emit-floors` must
   reproduce the driver's `ARMS_FLOORS` token in `.memory-tree.conf`.
2. Every non-comment `hit`, `miss` or `same` line, with `run` and `run_proc` rewritten to one word,
   sorted. The diff must be empty apart from the arms the step adds, which its commit message lists.
3. Each shard's `PASS (N assertions)` count, equal or higher by exactly the added arms, read from the
   shard log and never through `tail`.

The unattended kit version is bumped once, after the last move, in every carrier
`check-kit-versions.sh` derives.

### Inventory

New identifiers: `load_driver_conf` (verb `load`), `main` (the reserved entry verb), `run_proc`,
`derive_tree_digest`, `render_stable`, and the variables `DRIVER_ARGV0`, `DRV_INPROC_N`,
`DRV_PROC_N` and `UNATTENDED_HARNESS`.

### Files touched (estimate)

- `tools/unattended/unattended.sh` — the two wraps, the entry, the `$0` and `$$` sites, the moves.
- `tools/unattended/unattended.test.sh` — the harness, parity table, source-level arms, shard flips.
- `memory/map/generated/symbols.json` — regenerated for the new functions.

### Alternatives rejected

- **A separate library file.** It hides the fail sites from `check-arms.py` (§3).
- **Verb-level predicate calls.** A predicate harness would need each refusal chain re-implemented
  per arm, since the state reaching check N is the state that passed checks 1 to N-1 (research §3c).
- **A `--serve` coproc.** It needs a protocol for cwd, environment, argv, stdin, both streams and the
  exit code; a subshell gets all of them from bash.
- **Inferring the subshell from context.** The `$(run …; run …)` forms make that unsafe.

## 5. Production-readiness checklist

- security: no new input surface; conf refusals still exit, now from inside `load_driver_conf`.
- perf / scale: estimated 1900-8100 s pool work saved; the sourced-shell fork price (unit 0) decides it.
- error / empty / loading states: a failed source exits the shard with 2; `main` in the sourcing shell refuses with 2.
- observability: each shard prints `harness: <a> in-process calls, <b> process calls`; `a` at 0 after a flip reds.
- risks: global state leaking between arms (the parity table), name collisions (the namespace arm), foreign-prefix probes.
- testing: the parity table, the two source-level arms, and one `UNATTENDED_HARNESS=process` run per flipped shard.
- migration: none for adopters; executed behaviour is byte-identical, and the kit version bumps once.
- user docs: N/A — no user-facing surface; the driver's header comment names the sourced mode.

## 6. Acceptance criteria

- **AC1** — When the unit-0 probe times 20 `( : )` forks in a shell that sourced
  `tools/unattended/unattended.sh` and 20 in a bare shell, quiet and loaded, both figures and the
  instrument sit under the build folder before any driver line changes.
  Red when: the driver diff lands with no figure, or the loaded sourced fork exceeds 3 s and S2 starts.
  cost: minutes; the loaded half needs eight concurrent shards as background load.
  figure: PINNED at the measurement's date, node and sha.
- **AC2** — When a shell in a repo root sources `tools/unattended/unattended.sh` and then runs
  `declare -F load_driver_conf main`, it prints both names, exits 0, and writes no runlog line.
  Red when: sourcing runs a verb, exits the caller, or prints a refusal.
- **AC3** — When `bash tools/unattended/unattended.sh --version` and a `--hold` remedy fixture run as
  processes, their bytes equal the same runs at base, and `grep -n '\$\$' tools/unattended/unattended.sh`
  finds no pid read left. Red when: an executed message changes, or a `$$` read survives.
- **AC4** — When `main --version` is called in the shell that sourced the driver, it returns 2 and
  names the leak. Red when: it runs the verb in the parent shell.
- **AC5** — When `python tools/memory-tree/check-arms.py --report` runs before and after each step,
  the driver's normalised rows are identical, and `--emit-floors` reproduces the driver's
  `ARMS_FLOORS` token. Red when: any row disappears or the token moves.
- **AC6** — When each flipped shard runs, its `PASS (N assertions)` count equals the pre-flip count
  plus exactly the arms the step lists, and the sorted assertion multiset matches the pre-flip one.
  Red when: an assertion disappears, or the count is read through `tail`.
  permission: the driver shards are held suites the owner runs on demand.
- **AC7** — When the parity block runs as a slice (prologue plus that block), every row agrees on
  `render_stable` output, rc and `derive_tree_digest`; with `read_bound_key` staged out of
  `load_driver_conf`, the rc-2 row reds. Red when: the staged break passes.
  cost: a slice, about a minute; the whole suite is not run for this.
- **AC8** — When a top-level suite function named like a driver function, or a column-0 `exit` with
  no `run_proc` arm, is staged, the namespace arm and the top-level-exit arm each red naming it.
  Red when: either staged break passes.
- **AC9** — When a flipped shard is staged with `run` pointed back at `run_proc`, its `harness:` line
  reads 0 in-process calls and the shard reds; with `UNATTENDED_HARNESS=process` the same shard is
  green. Red when: a zero count passes, or process mode reds on an arm in-process mode passes.
  permission: the process-mode shard run is the owner's on-demand cadence.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `push-main self-test` · `check-wiring self-test` · `settings-merge selftest` · `run-gates canary` · `run-gates evidence` · `foreign-prefix parity (every self-test at three prefixes)` · `install-prefix self-test` · `dead-path carriers self-test` · `lexicon naming predicates` · `spec-tokens self-test` · `kit-placeholders self-test` · `recall floor` · `recall floor arms` · `unattended kit gate` · `harness arms (fail branches armed or pinned)` · `codebase-map coverage + freshness` · `kit version markers` · `runlog selftest`

New arm: tools/unattended/unattended.test.sh · covers AC7 · parity rows staged by removing one conf read from load_driver_conf · none
New arm: tools/unattended/unattended.test.sh · covers AC8 · a colliding suite function and an unclaimed column-0 exit, each staged · none
New arm: tools/unattended/unattended.test.sh · covers AC9 · a flipped shard pointed back at run_proc · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.

## 10. Reuse audit

The probe, `tools/codebase-map/reuse_lookup.py`, asked "source a shell script as a library and call
its main in a subshell", returned only Python `main` entries and name-stem neighbours: no existing seam fits. The
precedents extended are in-tree: `slice_fn` (`unattended.test.sh:635`) already evals driver
functions from the shipped bytes, and `( verb_plan "$_pl_s" )` (`unattended.sh:13292`) is the subshell
isolation this generalises.

Recall terms used: unattended.sh driver sourced in-process subshell harness run slice_fn preamble shard check-arms floors
