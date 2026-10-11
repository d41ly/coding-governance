# TOOL-aSparedSpawn-6 — the unattended driver as a library, called in process by its suite

**Status:** INPROGRESS · rev-3 · 2026-10-11 · node a · Tier-2 · base 22efab65 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-prompt-TOOL-aSparedSpawn-6-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aSparedSpawn-6-build-brief.md) | journal | — |

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
  the price above which the research says the harness loses. The pass that builds this unit may run
  no suite, so the load is eight background `( : )` fork loops standing in for the eight shards, and
  the instrument says so. Observed by AC1.
- **S2** — `load_driver_conf()` wraps the conf-dependent preamble: the `GATE_BACKSTOP_MARGIN` seam
  (`unattended.sh:412-417`), `ROOT`, the `cd`, the conf refusal and `. "$CONF"` (`:479-543`), the
  closed sets and `read_bound_key` reads (`:559-629`), `SHARED_RECORDS` and `GENERATED_INDEXES`
  (`:645-671`), `REVIEW_ROUNDS` and its runaway check (`:843-847`) and `PROCFS_ROOT` (`:1463`). It
  EXITS on a refusal, as today. `observe_remote` (`:455`) moves above it. Nothing is re-indented, so
  column-0 greps still match. An EXECUTED driver calls it right below its definition, so every
  top-level line after it still runs after the conf, as it always did. Observed by AC2, AC5.
- **S3** — `main()` wraps the argv state, the runlog install, the parse loop and the dispatch
  (`:13156-13363`). `refuse_waive_unless_preflight` (`:13194`) moves above it as a top-level
  definition. Every `exit` keeps its `RUNLOG_CLEAN=1` marker. Observed by AC2, AC3.
- **S4** — The entry: the file's last lines return when sourced and run `main "$@"` when executed,
  whose conf `load_driver_conf` already loaded below its own definition (S2). `main` refuses with rc 2, naming the leak, when sourced and
  `BASH_SUBSHELL` is 0. Observed by AC2, AC4.
- **S5** — The `$0` and `$$` sites. `KIT_DIR` and `SELF` (`:84`, `:120`) read `BASH_SOURCE[0]`. The
  three `--hold` remedy lines (`:10249`, `:10263`, `:10304`) print `DRIVER_ARGV0`, which is `$0` when
  executed and `BASH_SOURCE[0]` when sourced. The process-ledger, group-id and runlog sites
  (`:1509-1510`, `:10167-10168`, `:12973`, `:12989`) read `DRIVER_PID`, which `load_driver_conf`
  sets from `$BASHPID` as its first act. A bare `$BASHPID` at the site is not the same value: the
  process-ledger record is written from `run_bounded`, which a caller may reach inside a subshell,
  and there an executed run records the driver's pid where `$BASHPID` names the subshell. The same
  first lines re-derive `GATE_BOUND_LIVE` from `REMOTE_BOUND_LIVE`, because the suite assigns it at
  top level for its sliced `run_bounded` arms and an in-process call would inherit the last value.
  Observed by AC3.
- **S6** — The harness in the same suite file: source the driver once, in the prologue every shard
  runs, define `run_proc` as the old process `run`, and route `run` and every wrapper that ended in
  `bash "$SCRIPT" "$@"` through one mode-aware body, `run_driver`: `( load_driver_conf && main "$@" )`
  under `UNATTENDED_HARNESS=inproc` and `bash "$SCRIPT" "$@"` otherwise. A wrapper's `env -u X` and
  `VAR=v` become `unset X` and `export VAR=v` inside the wrapper's own `( … )`. The real-process
  classes stay on direct `bash` calls or `run_proc`: the missing library, the stripped self-read,
  mutated copies, the commit-msg hook path, `timeout` and `git` shadowed through `PATH`, the direct
  `bash "$SCRIPT"` sites whose environment is their subject, claim-lock concurrency and the process
  ledger. **It lands DARK**: the
  default is `process`, so the default suite is the base suite plus this unit's arms, and the default
  flips to `inproc` in one line once the owner's equivalence run has observed AC6 and AC9 per shard.
  A shard cannot be run inside a build pass, and the shards are held suites the owner runs, so a
  default flipped unobserved would first be seen red after landing. Observed by AC6, AC9.
- **S7** — The parity table, about 30 rows covering every verb at least once with rc 0, 1 and 2, an
  argv refusal, `--plan --framed` over two slugs, an `--abort`, and a conf holding `declare`. Each row
  compares the process against the in-process body, called directly whatever `UNATTENDED_HARNESS`
  says, so the dark default still grades in-process parity, on output through `render_stable`, rc,
  and `derive_tree_digest`. Commit dates are pinned for both calls and UTC stamps are normalised, so
  a difference is the driver's and never the clock's. Observed by AC7.
- **S8** — Two arms: the namespace arm and the top-level-exit arm. The namespace arm compares, at
  the end of each shard, the suite shell's definition of every driver function against the
  definition sourced in the prologue, and reds naming each that differs. A static scan for a
  colliding top-level name cannot tell a double fenced in `( … )` or restored after its block from
  one that leaks into every later in-process call, and the comparison grades that property itself.
  The nine colliding suite helpers the research found are fenced in `( … )` or restored by
  re-sourcing the driver after their block; `resolve_python`'s suite copy is the
  byte-identical canonical block and compares equal. The top-level-exit arm derives every top-level
  `exit` outside the two function spans and reds unless a declared row names the refusal text beside
  it and the suite holds an arm asserting that text from a driver run as a process. Observed by AC8.
- **S9** — The liveness counters: each call through the harness appends one byte to a per-mode
  tally file, because `out=$(run …)` runs `run` in a subshell and an incremented variable is lost
  there. Each shard ends with a line `harness: <a> in-process calls, <b> process calls`, and under
  `UNATTENDED_HARNESS=inproc` an `a` of 0 reds. `UNATTENDED_HARNESS=process`, the default until the
  flip, routes `run_driver` to the process for the equivalence run. Observed by AC9.
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
# Below load_driver_conf's definition: an executed driver loads its conf there, in its old order.
[ "${BASH_SOURCE[0]}" != "$0" ] || load_driver_conf
# The file's last lines: a sourced driver defines and returns; an executed one runs.
[ "${BASH_SOURCE[0]}" = "$0" ] || return 0
main "$@"
```

`GIT_GRAFT_FILE` stays exported at the top level; the suite's graft control already uses
`env -u GIT_GRAFT_FILE`. `. "$CONF"` inside a function makes a conf `declare`, `typeset` or `local`
function-local and a conf `return` end the load early. Gov's conf has none of these (research,
0 hits); the parity table carries one row for it.

### The harness

```bash
. "$SCRIPT" || { echo "FAIL the driver did not source, so no arm below runs in process"; exit 2; }
run_driver() {   # the one body: in process under UNATTENDED_HARNESS=inproc, a process otherwise
  if [ "$UNATTENDED_HARNESS" = inproc ]; then printf . >>"$DRV_INPROC_TALLY"; ( load_driver_conf && main "$@" )
  else printf . >>"$DRV_PROC_TALLY"; bash "$SCRIPT" "$@"; fi
}
run()      { run_main_at_head run_driver "$@" 2>&1; }
run_proc() { printf . >>"$DRV_PROC_TALLY"; run_main_at_head bash "$SCRIPT" "$@" 2>&1; }
```

The `( … )` is explicit on every call. The suite has `$(run …; run …)` forms, and an elided subshell
would let the first `main`'s `exit` end the rest of the substitution. An environment prefix on a
function call is exported to that function's children, so `CLAUDE_PID=4242 run …` carries over. A
wrapper that ran `env -u X … bash "$SCRIPT"` becomes a subshell body:
`( cd "$d" && unset X && run_main_at_head run_driver "$@" 2>&1 )`.
A bare `VAR=v load_driver_conf` would scope `VAR` to the load alone. The driver
already isolates `--plan` slugs the same way, `( verb_plan "$_pl_s" )` (`unattended.sh:13292`).

### Migration

In order, each step landing on its own with the inventory compared:

1. Unit 0 (S1). No code.
2. The driver refactor (S2-S5). `run` is still a process, so the whole suite must be green unchanged.
   Run `gen_map.py --write`, because new functions stale `symbols.json`.
3. `run_proc`, `run_driver` behind the dark default, the wrappers routed through it, the parity
   table, the two arms and the tally (S6-S9). Steps 1 to 3 are this unit's build pass.
4. The flip, after the unit: the owner's equivalence run takes each shard once per mode, AC6 and AC9
   observed, and the default of `UNATTENDED_HARNESS` then changes to `inproc` in one line.

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
`run_driver`, `run_inproc` (the uncounted in-process body the parity table calls), `derive_tree_digest`, `render_stable`, and the variables `DRIVER_ARGV0`, `DRIVER_PID`,
`DRV_INPROC_TALLY`, `DRV_PROC_TALLY`, `DRV_FNS` and `UNATTENDED_HARNESS`.

### Files touched (estimate)

- `tools/unattended/unattended.sh` — the two wraps, the entry, the `$0` and `$$` sites, the moves.
- `tools/unattended/unattended.test.sh` — the harness, the routed wrappers, the parity table, the two arms.
- `memory/map/generated/symbols.json` — regenerated for the new functions.
- `2026-10-11-build-TOOL-aSparedSpawn-6-fork-probe.sh` under the build folder — unit 0's instrument.

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
- observability: each shard prints `harness: <a> in-process calls, <b> process calls`; `a` at 0 under `inproc` reds.
- risks: global state leaking between arms (the parity table), name collisions (the namespace arm), foreign-prefix probes.
- testing: the parity table, the two arms, and one run per shard in each `UNATTENDED_HARNESS` mode before the flip.
- migration: none for adopters; executed behaviour is byte-identical, and the kit version bumps once.
  The suite's own default stays `process` until the owner's flip (§4 step 4).
- user docs: N/A — no user-facing surface; the driver's header comment names the sourced mode.

## 6. Acceptance criteria

- **AC1** — When the unit-0 probe times 20 `( : )` forks in a shell that sourced
  `tools/unattended/unattended.sh` and 20 in a bare shell, quiet and under eight background fork
  loops, both figures and the instrument sit under the build folder before any driver line changes.
  Red when: the driver diff lands with no figure, or the loaded sourced fork exceeds 3 s and S2 starts.
  cost: minutes; the load is eight `( : )` loops the instrument starts and reaps itself.
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
- **AC6** — When each shard runs once with `UNATTENDED_HARNESS=process` and once with `inproc`, both
  print one `PASS (N assertions)` count, equal to the pre-unit count plus exactly the arms this unit
  adds, and the sorted assertion multiset of the two runs matches.
  Red when: an assertion disappears, a mode reds where the other passes, or the count is read
  through `tail`.
  permission: the driver shards are held suites the owner runs on demand; owed at that run.
- **AC7** — When the parity block runs in its shard, every row agrees on
  `render_stable` output, rc and `derive_tree_digest`; with `read_bound_key` staged out of
  `load_driver_conf`, the rc-2 row reds. Red when: the staged break passes.
  permission: a build pass runs no suite and no slice of one; owed at VERIFYING with the shard.
- **AC8** — When a top-level suite function named like a driver function, or a column-0 `exit` with
  no `run_proc` arm, is staged, the namespace arm and the top-level-exit arm each red naming it.
  Red when: either staged break passes.
- **AC9** — When a run under `UNATTENDED_HARNESS=inproc` is staged with `run` pointed back at
  `run_proc`, its `harness:` line reads 0 in-process calls and the run reds; with
  `UNATTENDED_HARNESS=process` the same shard is green. Red when: a zero count passes, or process
  mode reds on an arm in-process mode passes.
  permission: the staged zero is observed on a shard run at VERIFYING, never on a slice in the pass;
  the per-shard runs in both modes are the owner's on-demand cadence.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `push-main self-test` · `check-wiring self-test` · `settings-merge selftest` · `run-gates canary` · `run-gates evidence` · `foreign-prefix parity (every self-test at three prefixes)` · `install-prefix self-test` · `dead-path carriers self-test` · `lexicon naming predicates` · `spec-tokens self-test` · `kit-placeholders self-test` · `recall floor` · `recall floor arms` · `unattended kit gate` · `harness arms (fail branches armed or pinned)` · `codebase-map coverage + freshness` · `kit version markers` · `runlog selftest`

New arm: tools/unattended/unattended.test.sh · covers AC7 · parity rows staged by removing one conf read from load_driver_conf · none
New arm: tools/unattended/unattended.test.sh · covers AC8 · a colliding suite function and an unclaimed column-0 exit, each staged · none
New arm: tools/unattended/unattended.test.sh · covers AC9 · a flipped shard pointed back at run_proc · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.
- rev-2 · 2026-10-11 · §2 §4 §5 §6 S1 S5 S6 S7 S8 S9 AC1 AC6 AC9 · the build pass. The harness lands
  DARK behind `UNATTENDED_HARNESS=process`, because no shard can run inside a pass and the shards are
  held, so the per-shard flips become one owner flip after an equivalence run in both modes. Every
  driver call routes through one mode-aware `run_driver`. The counters are tally files, since
  `$(run …)` loses an incremented variable. The pid sites read `DRIVER_PID`, set from `$BASHPID` at
  the top of `load_driver_conf`, because a bare `$BASHPID` inside a subshell changes an executed
  run's record; `GATE_BOUND_LIVE` is re-derived there for the suite's top-level assignment. The
  namespace arm compares definitions at shard end instead of scanning names, which cannot tell a
  restored double from a leaking one. Unit 0's load is eight fork loops, not eight shards.
- rev-3 · 2026-10-11 · §2 §4 §6 S2 S4 S8 AC7 AC9 · the build pass. An executed driver calls
  `load_driver_conf` right below its definition instead of at the file's end, so the top-level lines
  after the preamble still run after the conf and a conf still cannot pre-set what they initialise.
  The colliding suite helpers are restored by re-sourcing the driver after their block, which
  restores every definition at once where `slice_fn` restores one. `run_inproc` joins the inventory
  as the parity table's uncounted in-process body. AC7 and AC9 are observed on shard runs at
  VERIFYING, because the corrected brief forbids a suite slice inside a pass.

## 10. Reuse audit

The probe, `tools/codebase-map/reuse_lookup.py`, asked "source a shell script as a library and call
its main in a subshell", returned only Python `main` entries and name-stem neighbours: no existing seam fits. The
precedents extended are in-tree: `slice_fn` (`unattended.test.sh:635`) already evals driver
functions from the shipped bytes, and `( verb_plan "$_pl_s" )` (`unattended.sh:13292`) is the subshell
isolation this generalises.

Recall terms used: unattended.sh driver sourced in-process subshell harness run slice_fn preamble shard check-arms floors
