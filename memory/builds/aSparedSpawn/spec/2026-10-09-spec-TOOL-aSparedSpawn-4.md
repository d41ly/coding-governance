# TOOL-aSparedSpawn-4 — the runner's own spawns: a handful per leg, two git calls per bar, and a fork count with a ceiling

**Status:** OPEN · rev-1 · 2026-10-09 · node a · Tier-2 · base 22efab65 · streams tooling · order 2

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The runner pays about 45 to 65 fork and exec events per leg for its own bookkeeping, and asks git the
same question five or more times per bar. On the real bar that is minutes; inside the canary family,
which drives the runner a few hundred times over fixtures, the research estimates about 1270 s and
910 s quiet. This unit cuts the per-leg cost to about six events with bash builtins, asks git twice per
bar, and adds a fork-count arm with a declared ceiling and no clock, so the count cannot creep back.

## 2. Scope (IN)

- **S1** — `runleg` timing from `EPOCHREALTIME` with `printf -v` for the seconds, in place of two
  `date +%s%N` captures and a `printf` capture; a `date` fallback where `EPOCHREALTIME` is unset, as
  `measure_spawn_cost` already tolerates. Observed by AC1 and AC5.
- **S2** — The leg's raw output read with `mapfile -d ''` joined by `printf -v`, then stripped of
  trailing newlines, so it is byte-identical to today's `$(cat …)` capture, NUL bytes included.
  Observed by AC2.
- **S3** — `leg_log` maps the name with `${1//[!A-Za-z0-9._-]/_}` under a C locale in place of its
  `printf | tr` capture, byte-identical for a multibyte name. Observed by AC3.
- **S4** — `redact` runs only when the output matches `*://*@*`; otherwise both copies are written by
  `printf`. The two `chmod 600` calls give way to `umask 077` set once inside the leg's worker
  subshell. Observed by AC4.
- **S5** — Every input key computed ONCE, before dispatch, into an array the forked workers inherit:
  one `git ls-files -s` over the union of guard pathspecs, one `awk` pass emitting each leg's key
  input to a file, one `git hash-object --stdin-paths` over those files. The reuse block and the ledger
  row read the array. The definition is the reuse-key unit's, reproduced byte for byte. Observed by AC6.
- **S6** — `report_one` and `ts_hb` read with `read` and `$EPOCHSECONDS` in place of `$(cat …)` and
  `$(date)`; `ts_now` becomes `$EPOCHSECONDS` at every use. `live()` writes `jobs -rp` to a work-dir
  file and counts it with `mapfile`, keeping `jobs -rp`'s meaning, so the drain re-check's race
  reasoning is untouched. Observed by AC5.
- **S7** — Per bar, `git rev-parse --git-dir --git-common-dir --verify -q HEAD` once, after
  `cd "$ROOT"`, feeding the git-dir, common-dir and header-HEAD sites; the header's `worktree` reads
  `ROOT`, which the same command already answered at start. Each consumer keeps its own normalisation.
  The two receipt writers keep their end-of-run reads. Observed by AC7.
- **S8** — The fork-count arm in `run-gates.runlog.test.sh`, beside `measure_execs` and `run_traced`:
  a `PS4` carrying `${BASHPID}`, two traced bars over a one-leg and a two-leg manifest, forks as
  distinct pids and execs as non-builtin command words, the per-leg figure as the difference. It
  first counts a specimen with known forks and REFUSES when the counter disagrees. The ceiling is a
  constant in the suite with its reason, red on growth and red when stale by more than max(3, 5 %).
  It prints the top `file:line` contributors when red. Observed by AC8 and AC9.
- **S9** — `tools/run-gates/README.md` names the arm, its ceiling and how to move it. NOT OBSERVED: prose.

## 3. Non-goals (OUT)

- No change to any line the bar prints, any record field, or any verdict.
- No change to the atomic renames: `.leg`, `.rc` and the heartbeat keep their `mv`, which is most of
  the six events left per leg.
- No edit to `resolve_python` or `resolve_kit_dir`, which are parity-gated canonical copies; see F1.
- No turnstile poll-loop cut, no startup-chain trim beyond S7, no `timeout` probe change. The research
  lists them; they belong to the fork-free-readers work across the tree.
- No repo-wide spawn-budget registry. The ceiling lives in the kit's own suite, since a kit file names
  nothing outside itself by literal.

### Edges

- **consumes-from** `TOOL-aSparedSpawn-1` — the sound key definition S5 precomputes; without it the
  precompute would freeze the porcelain-line key the reuse-key unit exists to fix.
- **consumes-from** external — bash's `EPOCHREALTIME` and `mapfile -d`, both present on node `a`'s bash
  5.3.9 per the runner report; S1 keeps a `date` fallback for a shell without the first.

## 4. Design

**The per-leg sites, re-verified at base 22efab65** (`run-gates.sh`): `s=$(date +%s%N)` at `:2428`;
`out=$(cat …raw)` at `:2466`; `e=` and `secs=` captures at `:2467-2468`; `leg_log` at `:2483` with its
`printf | tr` at `:252-255`; two `| redact` pipelines and two `chmod` at `:2485-2486` and
`:2499-2500`; `$(input_key)` at `:2511`, and again in the reuse block at `:2301`; `mv` at `:2513` and
`:2521`; `ts_hb` at `:2520` with `$(ts_now)` and an `mv` (`:1118-1119`); `rc=$(cat …)` in
`report_one` at `:2581`; `live()` at `:3568`, called at `:3578` and `:3590`.

**The per-bar git sites.** `--show-toplevel` at `:98`; `--git-dir` at `:243`; `--git-common-dir` at
`:1103`, `:1543`, `:3479` and `:3904`; `HEAD` at `:2225`; `--show-toplevel` again at `:2248`. Every one
runs after the `cd "$ROOT"` at `:99`, and no later `cd` runs in the main shell, so one call made right
after that `cd` answers each with the value it reads today. Probed in a scratch repo on node `a`: with
an unborn branch, `--verify -q HEAD` beside the two dir flags prints both dirs and exits 1 with no HEAD
line, while a bare `HEAD` echoes the literal word; S7 takes the first form and reads a nonzero status
as an empty HEAD. `KITREL`'s `--show-prefix` (`:214`) asks from `KITDIR`, which the runlog suite places
outside the scratch repo, so it stays a separate question.

**A research figure refuted on re-verification.** The ceiling-max python (`:1021`) runs only under
`--print-profile`, which exits before the legs-parse python starts, so merging the two saves nothing on
any path. It stays.

**The key precompute.** The forked worker inherits the array, so the ledger row needs no git call. The
union pathspec is the guards' union, so one `ls-files -s` serves every guarded leg; the per-leg slice
is the same pathspec match the reuse-key unit specifies for the dirt rows. Its parity is observed
against ledger keys written by a copy of the runner at that unit's landing, over the same fixture.

**Measured stays measured.** Per-leg figures above are the research's static counts. The arm's first
run on the cut runner fixes the ceiling, and that number is PINNED in the suite with its date and node.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh` — every site above.
- `tools/run-gates/run-gates.runlog.test.sh` — the fork-count arm and its ceiling.
- `tools/run-gates/run-gates.evidence.test.sh` — the key-parity, output-capture and log-name arms.
- `tools/run-gates/README.md` — the arm and its ceiling.
- `tools/run-gates/kit.toml` — the kit version, moved once for the build.

### Alternatives rejected

- **A `PATH` shim that counts execs.** `TOOL-aThawedCorpus-3` was retired partly because a shim cannot
  see a fork; an xtrace pid count can, and `run_traced` already traces this runner.
- **A wall-clock budget per leg.** It reds on a loaded host; a fork count does not move with load.
- **`$(< file)` for the output read.** Whether it forks on bash 5.2 and later was not measured by the
  spawns report, and `$(<f 2>/dev/null)` silently reads empty; `mapfile` is a builtin on every version
  the runner meets.
- **A `umask 077` subshell per write**, as the runner report wrote it. A subshell is a fork; the worker
  is already its own subshell, so the mask is set once there.
- **Rewriting the runner in Python.** The runner report puts the direct saving at about 1 % of the bar
  against weeks of parity work.

## 5. Production-readiness checklist

- security: `redact` must still mask every `user:pass@` the old pipeline masked; the guard is a superset test on `://` and `@`, so it can only run more often than needed, never less.
- perf / scale: the research's estimate is about 1270 s plus 910 s quiet across the canary family; the real bar gains little directly.
- error / empty / loading states: an empty raw file, a NUL-bearing one and an unborn HEAD each keep today's values, by arm.
- observability: the arm prints per-leg forks and execs and the top contributors, so a later regression names its line.
- risks: byte drift in a captured output or a log filename; `umask` reaching a file a reader expects at a wider mode.
- testing: byte-equality arms against today's behaviour, a key-parity arm, a fork-count arm whose break is staged before landing.
- migration: none; records and output keep their bytes.
- user docs: `tools/run-gates/README.md` (S9).

## 6. Acceptance criteria

- **AC1** — When a fixture leg sleeps one second, its `.leg` row's seconds field reads between 1.000
  and the ceiling with three decimals, from `EPOCHREALTIME`. Red when: `secs` loses its format or
  reads zero because the separator in `EPOCHREALTIME` was not stripped.
- **AC2** — When fixture legs print output with trailing newlines, an embedded NUL byte and none at
  all, the `gate-logs` copy and the run-record `.out` copy equal byte for byte what the `$(cat …)`
  capture produced for the same legs. Red when: `mapfile -d ''` drops content after a NUL or keeps a
  trailing newline.
- **AC3** — When a leg is named with a space, a slash and a multibyte character, `leg_log` returns the
  path today's `tr` mapping returns. Red when: the C locale is not in force and a multibyte character
  maps to one underscore instead of one per byte.
- **AC4** — When a leg prints `https://u:p@host/x` and another prints no URL, the first copy carries
  `***:***@` and the second equals its raw output; both files carry the mode a `chmod 600` gives on
  that host. Red when: the guard skips a credential, or the mask is not set in the worker.
- **AC5** — When the dispatch pool equivalence arm runs at `GATE_JOBS=1` and `GATE_JOBS=4`, the two
  reports are identical, as today. Red when: the file-backed `live()` miscounts and a leg reports
  `(no result)` or the pool exceeds its width.
- **AC6** — When a fixture with guarded and unguarded legs and a dirty tree runs, every ledger key
  (`input_key`) equals the key a copy of the runner at the reuse-key unit's landing writes over the same fixture.
  Red when: the precompute's slice or order differs from the per-leg definition.
- **AC7** — When bars run in a primary tree, a linked worktree and a repo on an unborn branch, the
  header's `head`, `worktree` and every path built from the git dir or common dir equal today's.
  Red when: a relative git dir is resolved against the wrong directory, or an unborn HEAD reads `HEAD`.
- **AC8** — When the fork-count arm counts its specimen through its `PS4` trace, it reports the specimen's known fork count;
  with the trace descriptor closed early it REFUSES rather than reporting zero. Red when: a counter
  that cannot move reports a passing figure.
- **AC9** — When a fixture copy of the runner gains one `$(date +%s)` inside `runleg`, the arm reds,
  naming the measured figure, the ceiling and that `file:line` among the top contributors. Red when:
  the per-leg difference does not see one added fork.
  figure: the ceiling is PINNED in the suite from the arm's first run on the cut runner, dated and noded.

## 7. Gates

`run-gates run-log line` · `run-gates evidence` · `run-gates canary` · `run-gates turnstile` ·
`run-gates gov canary` · `run-gates adopter e2e` · `profile-bar selftest` · `pre-push run-log line` ·
`push-main self-test` · `check-wiring self-test` · `settings-merge selftest` ·
`foreign-prefix parity (every self-test at three prefixes)` ·
`python resolver (behaviour + inline parity + idiom ban)` · `install-prefix self-test` ·
`dead-path carriers self-test` · `lexicon naming predicates` · `spec-tokens self-test` ·
`kit-placeholders self-test` · `harness arms (fail branches armed or pinned)` ·
`shell hygiene (a loop fed by a command substitution)` · `codebase-map coverage + freshness` ·
`testsuite counts (every bar self-test prints one)` · `line length` · `memory hygiene` ·
`spec tokens (a spec's own names resolve)`

New arm: tools/run-gates/run-gates.runlog.test.sh · covers AC8 AC9 · a closed trace descriptor, then one added `$(date +%s)` in a fixture copy of `runleg` · its `FLOOR_ASSERTIONS` rises by the assertions added
New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC1 AC2 AC3 AC4 AC6 AC7 · each builtin swapped back for a variant that loses the byte the arm pins · its `FLOOR_ASSERTIONS` rises by the assertions added

## 8. Open questions

- **F1 — Is the process-monitor kit-dir python folded into the legs-parse python?** It runs on every bar
  in a repo that adopts process monitoring, this one included, through `resolve_kit_dir`, a
  parity-gated canonical copy whose program is a `$(cat <<'RKD')` heredoc.
  - (a) Fold it: lift the program text into a builtin `read`, pass it to the legs-parse python, and
    re-render every copy of the canonical function, moving its parity suite. One python and two
    spawns fewer per bar here, and the heredoc's two spawns fewer at every call site of every copy.
  - (b) Leave it: this unit touches no canonical copy, and the fold goes with the tree-wide
    fork-free-readers work, which already lists the `resolve_kit_dir` heredoc among its edits.
  - Recommendation: (b); the saving is one python per bar, and the copies are a separate review surface.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "count forks of a traced runner invocation"` ranked name-token
neighbours (`counts`, `build_invocations`, `derive_runner_verbs`) and the `run-gates` affordance seam;
the seam extended here is in that kit and the probe did not rank it: `measure_execs`, `run_traced` and
`build_traced_runner` in `run-gates.runlog.test.sh`, which already trace this runner on their own
descriptor to count execs after the last leg. The fork-count arm adds a pid field to the same `PS4`.

Recall terms used: runleg spawns exec count xtrace measure_execs baseline EPOCHREALTIME rev-parse runner startup
