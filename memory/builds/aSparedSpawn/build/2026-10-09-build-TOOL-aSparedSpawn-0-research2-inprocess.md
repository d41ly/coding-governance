# Appendix — An in-process harness for the unattended kit's suites: research and design

**Serves:** none — research that precedes this build's specs; its units await the owner's scope ruling

A read-only research pass by one of five agents on 2026-10-09, kept verbatim below its first heading. Figures are estimates from static counts and one-line timings unless marked measured; the ranked synthesis is `2026-10-09-build-TOOL-aSparedSpawn-0-research.md`.


Read-only research, node a, 2026-10-09. The worktree is `gate-runner-profiling-optimization-5d1f1e` at `6bc6c949c`. I ran no suite, leg or driver. Every count below is a static count from source. Every seconds figure is an estimate, and its basis is written beside it.

The census instruments sit beside this file in the scratchpad:

- `census.py` reads driver call sites in `unattended.test.sh`.
- `census2.py` reads leg-run sites in `check-unattended.test.sh`.
- The two `*.json` files are their samples.

If any of these figures goes into a build record, the instruments go into that build's `build/` folder with it (charter §8).

Line numbers are against `tools/unattended/` unless a path says otherwise.

---

## 0. The answer in brief

1. **The driver is already almost a library.** It defines 255 functions. No verb body calls `exit`. Each verb returns, and `fail()` only sets `status` (`unattended.sh:676`). Every `exit` sits in three places: the source-time preamble (`:87`, `:415`, `:479-482`, `:602`, `:667`, `:847`), the argument loop (`:13152-13268`), and the tail of the dispatch (`:13274-13310`). The library is already sourced by the suite (`unattended.test.sh:43`), and there is a precedent for in-process work: `slice_fn` (`unattended.test.sh:635`) evals single functions out of the shipped bytes for 11 arms.
2. **Do not split the file.** `check-arms.py` finds a gate as "a tracked `.sh` that defines `fail()` and has `fail <n> "` sites", and pairs it with `<stem>.test.sh` (`tools/memory-tree/check-arms.py:216-233`). Floors are keyed by gate path (`.memory-tree.conf`: `tools/unattended/unattended.sh:362:348`). If the fail sites moved into a library that does not define `fail()`, they would leave the population in silence. That is green-by-absence. Several other gates and suites also read the driver file by name: `core_of`, the check 26 argv sentinel, the runlog-writer suite's exit enumeration, and the source-level greps.
3. **The design.** Wrap the conf-dependent preamble in `load_driver_conf()` and the argument loop plus dispatch in `main()`, then end the file with a sourced-mode guard. The suite sources the driver once per shard and redefines `run()` as `( load_driver_conf && main "$@" ) 2>&1`. **A subshell is the process boundary.** It keeps the exit code, both file descriptors, file writes, git side effects, `exit` and the EXIT trap. So every message-only arm moves in process, and so do almost all side-effect arms.
4. **Few arms need a real process.** In a hand-checked sample of 73 arms, 0 need a process after the refactor and 2 need one before it. A targeted grep puts the process-only arms at about 40-60 call sites, plus a parity table of about 30 rows.
5. **Estimated saving, driver suite.** About 1350 in-process calls × 1.4 s quiet to 6 s loaded is about 1900-8100 s of pool work, against the 17142 s pooled reading. The unknown that matters most is the fork price of a shell that has sourced 15.4k lines. Unit 1 measures it before anything migrates.
6. **`check-unattended.sh` gets a widened `--only` selector, not a restructure.** `--only 28` and `--skip 28` exist already (`check-unattended.sh:140-149`). The post-28 checks already have one header each and a header-derived skip announcer (`:5370-5383`). Stage A adds `--only core` and `--only <N≥29>` on that machinery, with a mandatory stdout line naming the checks that ran. Splitting checks 1-27 is stage B, and it is gated on a traced census, because aGradedDoorway-7 rejected it on a CPU-only figure (`memory/builds/aGradedDoorway/build/2026-08-29-build-TOOL-aGradedDoorway-7-1-s3-cost-split.md:59`).

---

## 1. Driver structure

### 1a. The preamble, step by step

The "needed by" column says which verbs need each step. "All" includes `--version`, which today pays the whole preamble and refuses outside a repo or without a conf, although its header promises "then exit" (`:31`, and `:13259` runs after `:479-482`).

| # | step | lines | spawn and fork units (quiet path) | needed by |
|---|---|---|---|---|
| 1 | `set -u`, `KIT_UNATTENDED_VERSION` | 54-55 | 0 | all |
| 2 | `export GIT_GRAFT_FILE=/dev/null` (the dereference pin) | 75 | 0 | every history reader. A source-level arm greps it at column 0 (`unattended.test.sh:2966`) |
| 3 | `KIT_DIR` from `$0`, then source the lib, which exits 2 when the lib is missing | 84-90 | 3 | all |
| 4 | the `VERBS_SLUG` and `VERBS_INLINE` sets, `verb_list`, `usage` | 100-130 | 0 | the dispatch, refusal 14 and usage |
| 5 | `SELF` from `basename "$0"` | 120 | 2 | `usage` only |
| 6 | the remote bounds, then the `timeout -k 1s 10 true` capability probe | 144-168 | 2 | verbs that observe the remote or run a bounded command: preflight, close, resume, landed, hold, handoff, settle, claims, beat, dispatch (the callers of `observe_remote` and `run_bounded`) |
| 7 | `GATE_BACKSTOP_MARGIN`, an environment seam that exits 2 when it is not a number | 412-417 | 0 | close |
| 8 | the two NOTEs saying the bound is inert | 423, 428 | 0 | all (printed) |
| 9 | `ROOT` from `GIT rev-parse`, `cd "$ROOT"`, and refusal when there is no conf | 479-482 | 2 | all |
| 10 | the conf-default init block, then `. "$CONF"` | 493-543 | 0 | all |
| 11 | the `LANDER_MODE`, `RESUME_SCHEDULE` and `RUN_CLAIMS` closed sets, each exiting 2 | 559-603 | 0 | landing, hold and resume, claim verbs |
| 12 | `read_bound_key` ×6, each exiting 2 on a bad value (`lib-unattended.sh:231-244`), and the stale-bound NOTE | 609-629 | 0 | each key has its own readers (GATE_BOUND: preflight and close; UNIT_STALL: audit, status, liveness; …) |
| 13 | argv-state init | 633-644 | 0 | the parse loop |
| 14 | `SHARED_RECORDS`, `GENERATED_INDEXES` and the overlap refusal (exit 2) | 645-671 | about 25: `$()` wrappers, `derive_self_rel`'s dirname and basename loop, `read_conf_value`, 2 `mktemp`, `git ls-files`, awk, rm (`lib-unattended.sh:736-806`) | preflight (`check_cross_run_overlap`), dispatch, close and abort (`dod_met`), authorization, check-commit, overlaps. Lever #10 measured this as about 55% of the call mix not needing it |
| 15 | `status=0`, `RUNLOG_CHECKS=()`, `fail()` | 672-676 | 0 | all |
| 16 | constant blocks, plus `read_bound_key REVIEW_ROUNDS` and the runaway check (exit 2) | 689-1000, **843-847** | 0 | review, close, plan |
| 17 | `PROCFS_ROOT=${UNATTENDED_PROCFS:-/proc}`, an environment seam | 1463 | 0 | liveness, settle, reaper |
| 18 | runlog variables | 12790-12792 | 0 | all journaled verbs |
| 19 | argv-state init, the runlog START line and `builtin trap … EXIT` | 13103-13130 | 0, plus 1 `mkdir` the first time in a clone | all except `--version` and `--plan` |
| 20 | the parse loop. `--plan`, `--phase`, `--check-commit`, `--claims`, `--version` and `--overlaps` exit **inside** it | 13152-13268 | — | — |
| 21 | the refusal-37 guard, `usage`, the dispatch `case`, and the post-dispatch `write_run_record` for `--close` and `--abort` | 13274-13310 | — | — |

**About 35 spawn and fork units run before any verb body**, and step 14 accounts for about 25 of them. Steps 3, 5 and 6, plus the `derive_self_rel` walk inside step 14, depend only on where the kit lives. Those are about 21 of the 35, and they can run once at source time.

### 1b. Where global state is set

Global state is set in four places:

- **Source-time constants**: steps 1-6, 15, 16 and 18, along with roughly 120 more top-level `X=""` initialisers next to their functions, such as `HC_DEAD` at `:1025`, `RB_OUT` at `:210` and `AUTH_*` at `:1681-1724`. They are the same on every call.
- **Conf-dependent state**: steps 9-14, 16's `REVIEW_ROUNDS`, and 17.
- **argv state**: steps 13 and 19, deliberately initialised after the conf is sourced (`:630-632`, `:13104-13106`).
- **Verb working globals**: `DP_*`, `AUTH_*`, `GG_*`, `LV_*` and the rest, written by verb bodies.

One property makes in-process calls safe. **The parent shell never runs `main`, so every call starts from pristine source-time values.**

### 1c. How verbs dispatch

There are two routes:

- A slug verb is recognised by membership in `VERBS_SLUG` (`:13258`, `is_slug_verb` at `:105`). The `case` at `:13277-13302` then calls one `verb_*`, `print_*`, `run_*` or `write_*` function with globals as arguments.
- Inline verbs (`--plan`, `--phase`, `--check-commit`, `--claims`, `--version`, `--overlaps`) run and `exit` inside the loop.

`--plan` with several slugs, or with `--framed`, already isolates each slug in a subshell, `( verb_plan "$_pl_s" )` (`:13230-13234`). That is the same isolation pattern this design generalises.

### 1d. What blocks sourcing the driver as a library today

| blocker | where | effect when sourced | fix |
|---|---|---|---|
| top-level conf code: `cd`, `. "$CONF"`, refusals | 479-671, 843-847, 1463, 412-428 | it runs at source time against the cwd, and exits the suite on a refusal | move it into `load_driver_conf()` |
| top-level argv and dispatch, with an `exit` at the end | 13103-13310 | it runs `main` against the suite's `$@` and exits the suite | move it into `main()`, then add a guard and the entry calls |
| `exit` inside the parse loop and the dispatch | 13153-13310, about 15 sites | only harmful in the parent shell | keep them. Under the harness they exit the per-call subshell |
| `$0` | 84, 120, and `bash $0 --hold …` text at 10196, 10210, 10251 | when sourced, `$0` is the suite's path | use `BASH_SOURCE[0]` for `KIT_DIR`. Use `DRIVER_ARGV0`, which is `$0` when executed and `BASH_SOURCE[0]` when sourced, for the message text, so the process path keeps its bytes |
| `$$` | 1509-1510 (process ledger), 10114-10115 (gid), 12920 and 12936 (runlog `n` and `pid`) | every call in one suite shares a pid | use `$BASHPID`. That is identical at a process's top level, and distinct per subshell. bash ≥4 is already required by `declare -A` at `:3866` |
| the EXIT trap | 13128, and 13030 clears it | in a subshell it fires when the subshell exits, which is the right behaviour, and the parent's `trap 'rm -rf "$TMP"'` (`unattended.test.sh:130`) is reset in the child | none needed |
| `set -u` | 54 | the suite already runs `set -u` (`unattended.test.sh:11`) | none needed |
| a namespace collision with the suite | 9 function names: `derive_ask_seq read_ask_back read_held_reds read_leg_argv readme_of resolve_python run_bounded write_ask_views write_proc_record`. Several are deliberate stubs (`unattended.test.sh:7811`, `:7848`, `:13022`) | a top-level suite stub would shadow the driver for every later call | rename the helpers, and fence the stubs inside `( … )`. A source-level arm compares the two name lists (§3d) |
| `. "$CONF"` inside a function | — | `declare`, `typeset` or `local` in a conf would become local, and `return` would end the load early | Gov's own conf has none of these (checked: 0 hits). Record it as a semantic change and add one row to the parity table (§4c) |

The lib is already source-safe. It defines functions and constants, and its only `exit` sits inside `read_bound_key` (`lib-unattended.sh:234`, `:242`).

---

## 2. Arm taxonomy

### 2a. The driver suite, `unattended.test.sh`

**Population.** I counted 1936 static driver-call sites: `run` (`:495`), the 12 wrappers that run `bash "$SCRIPT"` (`run_su` `:9383`, `iprun` `:10425`, `run_dl` `:12193`, `run_ih` `:12663`, `run_hooked` `:14017`, `run_gw` `:15246`, `run_rx` `:15580`, `run_ln` `:15715`, …) and the fixture builders that call them (`bcopen`, `cropen`, …). The earlier research counted about 1450 dynamic calls (1324 `run --verb` plus 119 raw), and the cost section uses that number. Static census, by heuristic:

| class | sites | basis |
|---|---:|---|
| setup only: output discarded, no assertion in the block | 525 | the call is followed by no `hit`, `miss` or `same` before the next call or reset |
| message only: `hit` or `miss` on output alone | 751 (53% of asserting sites) | no side-effect, exit-code or stream pattern in the block |
| side effect: `$(sum)` or `before`, file tests, git reads, `read_phase` or facts, `rc` | 446 (32%) | regex over the assertions |
| process candidate: an environment prefix, raw `bash "$SCRIPT"`, kill or sleep or pid, preamble text | 214 (15%) | deliberately over-inclusive |

**Hand-checked sample.** 73 asserting sites, up to 9 per shard, seed `20261009` (the IDs are in `sample.json`). I read each block.

- **About 38 are message only.** For example, check 1's slug refusal (`:790-792`), `--park` without `--reason` (`:4423`), `--plan` with no unit set (`:2594`), and recipe-playbook refusals (`:4783`, `:4794`).
- **About 33 have side effects that a subshell keeps.** For example, "wrote nothing" pairs on `$(sum)` (`:8699`, `:8676`, `:3091`), a staged-path assertion after `--phase` (`:3040`), `rc` together with lease hashes (`:8749`), a claim ref on the remote (`:14025`), and `CLAUDE_PID` or `CLAUDE_CODE_SESSION_ID` prefixes, which the driver reads at verb time in `write_lease` (`:6992-7003`, used at `:7301`, `:8891`, `:9878`, `:9900`, `:14346`). A git binary shadowed through PATH (`:14516`) also works in a subshell, because assigning PATH resets the hash table. So does a live sleeper pid probed through `/proc` (`:9684`).
- **2 need a process today, and 0 after the refactor.** `:8059` asserts a `read_bound_key` refusal, which is preamble step 12 and moves into `load_driver_conf`. `:5052` passes `--waive` to the parse loop, which moves into `main`.

Extrapolated to the 1411 asserting sites, about 52% are message only and about 45% have subshell-safe side effects. About 3% need a process. That 3% comes from the targeted grep below, not from the sample, where the class was too rare to show.

**The arms that must stay a real process, found by targeted grep.** The counts are matching lines, so arms are fewer.

| class | evidence | approximate call sites |
|---|---|---:|
| the kit library missing beside the script, which is a source-time exit | `:6998` | 1-2 |
| `$0` and header self-read from a stripped copy | `:2827` (`bash "$TMP/stripped.sh"`) | 2 |
| a mutated copy of the driver | `cp "$SCRIPT"` ×2. The runlog-writer suite runs its own copy under `$KR` (`runlog-writer.test.sh:233`, `:474`) | 2-4 |
| `check-commit` invoked by git through a commit-msg hook | `hooksPath` ×10, `run_hooked` `:14017` | ~10 |
| `timeout` shadowed through PATH (the source-time capability probe) | a subset of 44 `PATH=` lines | ~5-10 |
| two drivers in real concurrency on the claim push lock | `claim-push.lock` ×12 lines | ~4-6 |
| the process ledger and reaper keyed on the driver's own pid | `write_proc_record`, `procs`, `PROCMON_CMD`: 15 + 5 lines | ~8-10 |
| runlog trap and exit shape | owned by `runlog-writer.test.sh` (16 driver references), which is already a process suite and unchanged | 0 here |
| **total kept** | | **about 35-45**, plus the 30-row parity table (§4c), so about 70-75 process calls out of about 1450 (about 5%) |

### 2b. The gate suite, `check-unattended.test.sh`

The gate cannot be sourced. Its checks are top-level code, and it imports the conf inside a subshell on purpose (`check-unattended.sh:222-246`). The lever here is the scope selector, so the taxonomy asks **which checks each leg run asserts on**.

- **686 static leg-run sites** (`run` `:393`, `run_skip_leg` `:643`, `lmrun` `:644`, `run_ak_leg` `:678`, `ma_leg` `:688`, raw `bash "$SCRIPT"`). The earlier research counted about 449 dynamic runs.
- **Signatures mapped to check numbers**, using `check-arms`' own extractor reimplemented in `census2.py` (352 sites mapped):
  - 282 name checks from the region holding checks 1-27 and 34-38, 44-46.
  - 33 name check 28.
  - 37 name a check after 28 (30-33, 39-43, 47-51).
  - 2 name both.
  - 13 are whole-leg controls ("the output is empty").
  - Another 332 sites were not mapped, because their messages interpolate before the longest literal run.
- **Hand sample of 30** (seed 7, `sample2.json`):
  - 26 are about one check, for example `:1946` check 13, `:2794` check 16, `:4261` check 23, `:6306` check 42 and `:5293` check 19 (already `--skip 28`).
  - 2 are about a small set (`:1218`, checks 1, 2, 4 and 16, all in the prologue).
  - 1 is an argv refusal with exit 2 (`:4292`, `--emit-ceiling`).
  - 1 needs the whole run (`:2689`, which mutates three kit files and reads the report channel).

**Extrapolated:** about 85% one check, about 7% a small set, about 3-6% whole leg or argv. Of the mapped one-check arms, about 80% sit in the region holding checks 1-27.

---

## 3. Design

### 3a. The driver: one file, two entry shapes

The changes, all in `unattended.sh`. The diff is about 25 changed lines plus three blocks moved. Nothing is re-indented, so the source-level greps that key on column 0 (`^MEMORY_ROOT=memory`, `^export GIT_GRAFT_FILE`, `core_of`'s `KEY="value"`) still match.

1. **`load_driver_conf() {` … `}`**, placed around steps 7 and 9-14. Move step 7 down next to step 9, and move `observe_remote` (`:430-477`) above the block. The function also takes `read_bound_key REVIEW_ROUNDS` and the runaway check (`:843-847`) and `PROCFS_ROOT` (`:1463`), so that every environment and conf input is re-read on every call.
   - The function **exits rather than returns** on a refusal, exactly as today.
   - Column-0 lines inside a function body are legal bash.
   - The lexicon verb `load` fits ("read a store into memory").
   - `GIT_GRAFT_FILE` stays at the top level. The suite's graft control already uses `env -u GIT_GRAFT_FILE` (`unattended.test.sh:2935`).
2. **`main() {` … `}`** around `:13103-13310`. `main` is the lexicon's reserved entry verb, "one per module". `refuse_waive_unless_preflight` stays a top-level definition, above `main`. Every `exit` inside keeps its `RUNLOG_CLEAN=1` marker, so the runlog-writer suite's exit enumeration is unchanged.
3. **The entry**, as the file's last lines:
   ```bash
   # A sourced driver defines and returns; an executed one loads its conf and runs.
   [ "${BASH_SOURCE[0]}" = "$0" ] || return 0
   load_driver_conf
   main "$@"
   ```
4. **The renames:** `$0` becomes `BASH_SOURCE[0]` at `:84` and `:120`. `bash $0 --hold` becomes `bash $DRIVER_ARGV0 --hold` at `:10196`, `:10210` and `:10251`. `$$` becomes `$BASHPID` at the 5 sites in §1d.
5. **A guard in `main`:** when it is sourced and `BASH_SUBSHELL` is 0, it refuses by name ("main ran in the sourcing shell, so its globals and its exit would leak into the caller") and returns 2. Without this guard, a bare call leaks state into every later arm.

**Optional, measured later and not in the first cut.** Move the kit-only half of step 14 (`derive_self_rel` of the library, `lib-unattended.sh:741-748`) to source time. That removes about 14 units per call on both paths. Lever #10's lazy `GENERATED_INDEXES` stacks with it.

### 3b. The harness, inside `unattended.test.sh`

The harness stays in the same file, so check-arms still pairs it and the shard contract (`:89-126`) is unchanged.

```bash
# once per shard, after the helpers and before the first arm
. "$SCRIPT" || { echo "FAIL the driver did not source, so no arm below runs in process"; exit 2; }
run()      { ( load_driver_conf && main "$@" ) 2>&1; }   # in process: same argv, same 2>&1, same exit status
run_proc() { bash "$SCRIPT" "$@" 2>&1; }                 # the old run(), kept for the process-only classes
```

How each part of today's calls carries over:

- **Explicit `( … )` on every call, never inferred from context.** The suite has `$(run …; run …)` (`:11911`) and 67 sites of the form `$(run …); rc=$?`. Eliding the subshell would let the first `main`'s `exit` kill the rest of the substitution.
- **Environment prefixes carry over.** `CLAUDE_PID=4242 run …` is a temporary environment entry on a function call, and it is exported to that function's children.
- **The wrappers become subshell bodies.** `env -u X … bash "$SCRIPT"` becomes `( cd "$dir" && unset X && export GOV_DEFAULT_BRANCH=main && load_driver_conf && main "$@" ) 2>&1`. A bare `VAR=v load_driver_conf` would scope VAR to the load alone, which is the trap to avoid.
- **The liveness counters.** `run` increments `DRV_INPROC_N` and `run_proc` increments `DRV_PROC_N`, both in the parent through a pre-increment outside the subshell. Each shard ends with `harness: <a> in-process calls, <b> process calls`. If `a` is 0 after migration, the shard reds. A probe that cannot move says so.
- **`slice_fn` (`:635`) becomes redundant for functions that are already sourced.** Leave it alone: its arms evaluate the shipped bytes on purpose.

### 3c. Why this beats predicate-level calls

The task suggested calling each refusal predicate against a prepared fixture state. I recommend the verb-level call above instead, for three reasons:

1. **Verbs are guarded chains with early returns** (`verb_preflight` at `:6371-6470`: check 6, then `check_slug`, then 27, 28, 81, 82, …). The state that reaches check N is the state that passes checks 1 to N-1. A predicate harness would need 367 extracted predicates and a hand-built precondition per arm, which is a second implementation of each chain.
2. **The gain is small.** What is left after the verb-level harness is the verb body, which lever #1 (fork-free `fact`) attacks, and fixture git. A predicate call saves neither.
3. **check-arms grades text, not execution** (`check-arms.py:261-283`). Arms keep naming literal failure text under either design, so predicate-level calls buy no extra arm-rule safety.

**The rejected alternative is R3, a `--serve` coproc** (`…research-govkit-unattended.md:86-92`). It needs a request protocol carrying the cwd, environment, argv, stdin, both streams and the exit code. Sourcing gets all of those from bash for free. Its only advantage is namespace isolation, and the collision arm below covers that.

### 3d. How check-arms keeps working

check-arms keeps working with no change on its side:

- **The gate stays the same file.** `unattended.sh` keeps `fail()` (`:676`) and all 367 sites, and its sibling test stays `unattended.test.sh`, so discovery and `ARMS_FLOORS` (`362:348`) are untouched.
- **Arm lines stay literal.** `hit "$(run …)" "<literal>"` is unchanged text, because only `run`'s definition changes. Arms moved to `run_proc` change one word, and the signature is elsewhere on the line.
- **Signature 2 (`ARMS_REFUSALS="graded"`, `.memory-tree.conf:587`) reads `exit 1` and `status=1` sites by text.** Moving top-level code inside a function changes neither the sites nor their messages. The indentation walk (`check-arms.py:105-108`) sees the same indentation, because nothing is re-indented.
- **A new source-level arm: the namespace guard.** One `grep` and `comm` over `^name()` definitions in the driver and the suite. It fails when a top-level suite definition shares a driver function's name. This is the exact computation that found the 9 collisions. It runs once per suite at about 2 spawns, and needs no runtime `declare -f` diffing.

### 3e. `check-unattended.sh`: a mandatory liveness line on `--only`

**Stage A** builds on what exists and does no untangling:

- **The parser** (`:141-149`, inside the argv sentinel pair that check 26 reads) accepts:
  - `--only 28` and `--skip 28`, as today;
  - `--only core`, which runs the prologue and the region holding checks 1-27, 34-38 and 44-46, and skips the 28 region and the post-28 `else` branch (`:5370`);
  - `--only <N>`, for N among the post-28 header set, read from the running file by `_o28_nums`' awk (`:5372-5377`) and never typed.

  Anything else is refused with exit 2, as today. Check 26 then demands an arm for each new flag value, which the migration adds.
- **The guard** is `want <N>`. It is called once, at each `# ---- check N` header in the post-28 region, and never inside a loop, because a loop over an empty population would never register its check. It records N into `RAN` when selected.
- **The liveness line is mandatory under any `--only`.** It goes to stdout, so it cannot hide on the report channel:

  `check-unattended: --only <sel> ran checks <sorted RAN>; skipped <the rest of the header-derived set>`

  If a requested N never reached its `want`, the run refuses with exit 2: "check N was requested and no guard for it ran, so its verdict would be silence". The unscoped bar run prints nothing new, so the "Exit 0 + no output" contract (`:12`) still holds. The 11 existing `--only 28` arms gain the line. They assert on announcements, not on empty output, so check that before landing.
- **Producers stay unguarded**: the conf import, the warm-ups (`:328-560`), `core_of` and the per-record facts. Only the blocks that emit or consume a verdict are guarded. A post-28 check that silently read state from checks 1-27 would get empty values under `--only N`. `set -u` catches an unbound read. The projection parity arm (§4c) catches an empty initialised one.

**Stage B** is per-check `--only N` inside the region holding checks 1-27. Do it only if unit 0's trace shows check bodies there carrying spawns worth the untangling. aGradedDoorway-7 rejected it on "check bodies are 9.5% of wall". That figure is user CPU from one cold invocation (`…S3-cost-split.md:59`, with `sys 43.9 s` against `user 12.1 s`). The earlier research notes that the spawns are issued from inside those bodies (`…research-govkit-unattended.md:325-331`). The question is open, and the trace settles it.

---

## 4. What keeps the guarantee

### 4a. End-to-end process arms that stay

- **The driver suite keeps about 35-45 `run_proc` call sites** for the §2a classes:
  - the kit library missing, `$0` and header reads, and mutated copies;
  - the commit-msg hook path;
  - `timeout` shadowed through PATH;
  - claim-lock concurrency;
  - the process ledger and reaper.
- **The parity table adds about 30 more** (§4c).
- **The runlog-writer suite is unchanged and stays fully process.** It is where the EXIT trap, `exit=clean` and `exit=unclean`, START without END, and the zero-spawn xtrace count are graded.
- **For `check-unattended`:** the 13 whole-leg controls, the argv refusals (exit 2) and at least one unscoped conforming run per shard stay unscoped, so every check still runs unselected somewhere.

### 4b. How a refusal that fires only in a real process is still caught

After the refactor, the refusals that **only** fire in a process can be derived. They are the top-level `exit` sites left outside `load_driver_conf` and `main`. By the §1a table that is exactly one, the missing library at `:87`. Every conf, environment and argv refusal moves inside one of the two functions, so the in-process path reaches it too.

**Derive that set, never list it.** A source-level arm finds column-0 `exit` lines outside the two function spans, using the same span reader `slice_fn` uses. It asserts that each one is named by a `run_proc` arm. A new top-level refusal then reds until a process arm claims it.

Two more mechanisms back that up:

- **The kit's Definition of Done runs the whole suite once in process mode.** A switch, `UNATTENDED_HARNESS=process`, redefines `run` as `run_proc`. This is the same owner-run, on-demand cadence as `GATE_SELFTESTS`, so every arm runs both ways at least once per kit version.
- **The default bar runs in process.**

### 4c. Proving the two paths agree: the parity arm

The parity table has about 30 rows, one fixture state each. It covers every verb at least once, with these outcomes:

- refusal (rc 1);
- success (rc 0);
- misconfiguration (rc 2, from `read_bound_key`, `LANDER_MODE`, and the `SHARED_RECORDS`/`GENERATED_INDEXES` overlap);
- an argv refusal (14 and 37);
- `--plan --framed` with two slugs;
- an `--abort` that runs the post-dispatch `write_run_record`;
- one conf containing `declare` (§1d).

Each row runs four steps:

```bash
reset_X; a=$(run_proc ARGS); ra=$?; da=$(derive_tree_digest)
reset_X; b=$(run ARGS);      rb=$?; db=$(derive_tree_digest)
same "parity ROW output" "$(render_stable "$b")" "$(render_stable "$a")"
same "parity ROW rc"     "$rb" "$ra"
same "parity ROW tree"   "$db" "$da"
```

- **`derive_tree_digest`** is `git rev-parse HEAD`, `git status --porcelain`, the hash of `git diff --cached` and the hash of every `RUN.md`, run through one `git hash-object --stdin`. It leaves out the runlog journal, whose pid and timestamps legitimately differ.
- **`render_stable`** masks ISO-8601 stamps and `$BASHPID` values.

**The `check-unattended` twin is the projection parity arm.** For each post-28 N, and for `core`, on the conforming fixture and on one red fixture of N, it asserts that the unscoped run's lines for N equal the `--only N` run's lines. That proves the selector neither drops nor adds a verdict.

---

## 5. Estimated cost after

### Driver suite

**Saved per call** = one `bash` exec + 0.75 s parse + about 21 preamble units (steps 3, 5, 6 and the `derive_self_rel` walk) − one extra fork in a heavier shell.

- **Quiet:** 21 ms spawn, about 30 ms per unit including forks. That is 0.02 + 0.75 + 0.6 − 0.1 ≈ **1.3-1.4 s**.
- **Loaded:** 0.2-0.29 s per fork or spawn (calibration table, `…research-govkit-unattended.md:20-28`). That is 0.5 + 1.0 + 4.6 − 0.3 ≈ **5-6 s**.

**Calls moved** ≈ 1450 − about 75 process calls ≈ **1375**.

**Total** ≈ 1375 × 1.4 s ≈ **1900 s** quiet, up to 1375 × 6 s ≈ **8100 s** of pool work loaded, against the 17142 s pooled reading. That is roughly 11-47%. Add a one-off source per shard, about 8 × 1-2 s.

**What remains:**

- the per-call conf half of the preamble, about 14 units;
- verb bodies (190 `$(fact …)` sites, which lever #1 attacks);
- fixture git, about 2000-3000 s (359 `reset_tree`, 885 commits, 167 pushes, from the earlier research);
- about 75 process calls × 4-8 s ≈ 300-600 s.

**Overlap with other levers:** lever #10 (the lazy `GENERATED_INDEXES`) removes the same step-14 term on the process path, so do not add the two estimates together. Lever #1 is independent.

**The biggest risk to this estimate is the fork price.** An MSYS fork copies the parent's heap. `$(:)` cost 89 ms in a shell holding 1.6 MB, against 10 ms on node d. After sourcing about 15.4k lines of function bodies, the suite shell is larger. If a fork rises above about 1 s loaded, the saving roughly halves. Above about 3 s, the harness loses. Unit 1 measures it.

### Gate suite

Today: about 449 runs × 20-30 s ≈ 9000-13500 s of pool work.

Stage A applies to about 90% of runs:

- arms in the region holding checks 1-27 run `--only core` and save the cost share `f` of the 28 region plus the post-28 checks;
- arms on 28 and post-28 checks run `--only N` and save about 1 − (that check's share).

`f` is **unmeasured**. The earlier research's static guess was 30-50% (lever #17). Check 30 alone launches the driver once per leg run (`:5385-5400`).

With `f` from 0.3 to 0.5, the saving is about 449 × 25 s × (0.8 × f + 0.2 × 0.8) ≈ **4300-6500 s** of pool work, conditional on unit 0. Stage B is unpriced until the trace exists.

---

## 6. Migration plan

Each unit lands on its own, and each keeps the arm inventory equal.

**How to compare inventories, run before and after every unit:**

1. `python tools/memory-tree/check-arms.py --report`, keeping the rows for `tools/unattended/unattended.sh` and `tools/unattended/check-unattended.sh`. Normalise them to `(gate, check, ordinal, signature, state, armed-by-file)` and drop the line column, because moved blocks shift lines. **The diff must be empty.** Run `--emit-floors`, and its tokens for the two gates must still read `362:348` and `264:256`.
2. **The literal multiset of assertions.** Take every non-comment `hit`, `miss` or `same` line in each suite. Rewrite `\b(run|run_proc)\b` as `CALL`, then sort. The diff must be empty, apart from the parity and namespace arms the unit itself adds. List those in the commit message.
3. **Each shard's `PASS (N assertions)` count** must be equal, or higher by exactly the added arms. Read it from the shard log, not through `tail`, per the memory note "never read a suite result through tail".
4. **The harness liveness line** (`harness: a in-process, b process`) once unit 3 exists. `a` must rise monotonically across units 3-5, and `a + b` must equal the previous run total.

| unit | change | Tier | gate it must pass | exit criterion |
|---|---|---|---|---|
| **0. Measure** | One traced run each (no code landed): (i) a `check-unattended.sh` conforming fixture leg under `PS4='+$EPOCHREALTIME $LINENO '`, attributed by line to check headers, giving `f` and stage B's case; (ii) in a shell that has sourced the driver, 20 × `( : )` against 20 in a bare shell, quiet and under the 8-shard load | 1 | none | record both figures with their instruments under `memory/builds/<slug>/build/` |
| **1. Make the driver sourceable** | §3a items 1-5. Re-key the line-keyed install-prefix waivers that the moved blocks shift (memory note "install-prefix waivers are line-keyed"). Run `gen_map.py --write`, because new functions make `symbols.json` stale | 2 (it changes the dispatch path) | `check-unattended` (core_of, check 26 sentinel, checks 39/48/51 function scans), runlog-writer, check-arms, lexicon (`load_driver_conf`, `main`) | the whole driver suite green **unchanged**, because `run` is still a process |
| **2. Harness, the parity table and the namespace arm** | Define `run_proc`. Define an in-process `run_inproc` beside it, **unused by any arm except the parity table**. Add the namespace-collision arm and the derived top-level-exit arm (§4b). Rename and fence the 9 colliding suite helpers | 1 | the suite; inventories 1-3 | parity rows all equal on node a; the fork figure from unit 0 holds |
| **3. Flip one shard** | In shard 1 only (`:785`), point `run` at the in-process body. Move the shard's process-class sites to `run_proc` | 1 | inventories 1-4 | shard 1 green; its wall clock recorded against its pre-flip reading |
| **4. Flip the remaining shards, one unit each** (2-8) | as unit 3. The wrappers `run_su`, `iprun`, `run_dl`, `run_ih`, `run_gw`, `run_rx` and `run_ln` become subshell bodies (§3b) | 1 each | inventories 1-4 | each shard green; `UNATTENDED_HARNESS=process` still green for that shard |
| **5. `check-unattended --only core` and `--only <N≥29>`** | §3e stage A: the parser, `want`, the liveness line, the refusal when a requested check never ran, and the check 26 arms for the new flag values. Update the 11 `--only 28` arms for the new line. Add the projection parity arms | 2 (it changes a merge-bar leg's argv surface) | the gate suite; check-arms; check 26 | projection parity green for every N |
| **6. Migrate the gate arms, one shard per unit** | `run` becomes `run_scoped <sel>` wherever an arm names one check or region and has no `miss` on a check outside the selection. Arms with such a `miss` become `--only N,M` or stay unscoped | 1 each | inventories 1-3 | shard green; the liveness line asserted once per migrated block |
| **7. (only if unit 0 says so) stage B** | per-check guards inside the region holding checks 1-27 | 2 | — | — |

Bump the kit version once, after unit 6, not per unit (memory note "bump kit versions once, after the last move"). It has five carriers.

Every unit's Definition of Done includes one `UNATTENDED_HARNESS=process` run of the shards it touched. That is the charter's "verify, not assert" for an equivalence claim.
