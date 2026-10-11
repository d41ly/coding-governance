# TOOL-aSparedSpawn-4 — the runner's own spawns: a handful per leg, two git calls per bar, and a fork count with a ceiling

**Status:** INPROGRESS · rev-2 · 2026-10-10 · node a · Tier-2 · base 22efab65 · streams tooling · order 2 · ratified 2026-10-10

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-prompt-TOOL-aSparedSpawn-4-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aSparedSpawn-4-build-brief.md) | journal | — |

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
- **S10** — The process-monitor kit dir is resolved inside the legs-parse python. `run-gates.sh` reads
  the marked `resolve_kit_dir` block once, at top level, into one variable with a builtin
  `IFS= read -r -d ''`, and the legs-parse program becomes that text followed by today's program. The
  process-monitor block moves below the parse and reads the dir, or the resolver's refusal, from one
  leading output line the reader strips. The runner's own `resolve_kit_dir` shell wrapper loses its
  only caller and is deleted. Observed by AC10.
  **Readers:** by name: `tools/run-gates/run-gates.sh` spells the runner's wrapper only at its call
  in the process-monitor block (`:1069`), which this item folds; every other copy defines its own.
  by value: `tools/run-gates/run-gates.sh` derives `PROCMON_REAP` and `PROCMON_SCOPE` from it
  (`:1070`), and this item rewires both to the leading line.
- **S11** — Every remaining copy of the canonical function reads its heredoc with the builtin `read`
  in place of `"$(cat <<'RKD'`: the suite copies listed under §4, which the spawn-idiom scan of
  `TOOL-aSparedSpawn-8` does not reach. The region between the `resolve_kit_dir` markers moves no byte
  in any copy. Observed by AC11.
- **S12** — The parity suite behind the `python resolver (behaviour + inline parity + idiom ban)` leg
  gains a ban arm: a `$(cat <<'RKD'` wrapper in any file of its `resolve_kit_dir` population reds,
  comments stripped first, with a planted specimen proving the predicate fires. Observed by AC12.

## 3. Non-goals (OUT)

- No change to the bytes of any line the bar prints, any record field, or any verdict. The one
  ORDER change is S10's: the `run-gates: process-monitor:` line prints after the turnstile lines.
- No change to the atomic renames: `.leg`, `.rc` and the heartbeat keep their `mv`, which is most of
  the six events left per leg.
- No edit to `resolve_python`, and no byte moved between the `resolve_kit_dir` markers in any copy.
  S10 to S12 change only the wrapper around that region and the gate over it.
- The product copies' wrappers, which `TOOL-aSparedSpawn-8` converts first because its ban on the
  idiom lands at order 1 with no registry escape.
- No turnstile poll-loop cut, no startup-chain trim beyond S7, no `timeout` probe change. The research
  lists them; they belong to the fork-free-readers work across the tree.
- No repo-wide spawn-budget registry. The ceiling lives in the kit's own suite, since a kit file names
  nothing outside itself by literal.

### Edges

- **consumes-from** `TOOL-aSparedSpawn-1` — the sound key definition S5 precomputes; without it the
  precompute would freeze the porcelain-line key the reuse-key unit exists to fix.
- **consumes-from** `TOOL-aSparedSpawn-8` — the product copies' `resolve_kit_dir` wrappers already
  reading their heredoc with the builtin `read`; without it S12's ban reds on every product copy.
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

### The process-monitor fold (S10 to S12, owner ruling F1 (a))

Today the runner spends one python on the kit dir alone: `resolve_kit_dir "$PYBIN" process-monitor
reap.py "$KITDIR"` at `:1069`, inside the block at `:1065-1087`, through the wrapper at `:144-189`
whose program is a `$(cat <<'RKD')` capture. It runs whenever `.process-monitor.conf` exists, which it
does in this repo. The legs-parse python (`legs=` at `:1968`, closing at `:2058`) runs on every bar.

The fold reads the marked block once into a variable with `IFS= read -r -d '' … <<'RKD' || :`, which
forks nothing. The `|| :` is owed because `read -d ''` returns 1 at end of input. The legs parse
receives that text ahead of its own program, and three more arguments, home, anchor and here, only
when the conf exists. Given them, it prints one leading line, the dir or the `LookupError` text, and
never exits on a refusal. The reader strips that line before today's line-1 handling, so the dispatch
order and every row keep their bytes. Without the conf the parse prints no extra line, which keeps
today's zero cost for a repo that has not adopted the monitor.

The block's assignments and its scope probe move below `:2058`, after the turnstile. Its defaults
(`PROCMON_OK=0` and the not-installed `PROCMON_WHY`) stay where they are, so a trap that fires during
the turnstile wait reaches `run_leg_reap` (`:1626`) with today's fallback walk. Every other reader of
those variables (`:1629-1637`) sits on the tree-kill path, which runs only after dispatch.

The wrapper conversion is the same edit in every copy. `TOOL-aSparedSpawn-8` converts the product
copies at order 1, because its `cat-heredoc` ban has no registry escape and would red on them; this
unit converts the suite copies its scan skips, then adds S12's ban over the parity population, which
reads suites, product files and the extensionless hooks alike
(`tools/lib/resolve-python.test.sh:181-183`). The marked region is not re-rendered from the canonical,
since no byte of it moves; the existing parity arm proves that.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh` — every site above, and S10's fold.
- `tools/run-gates/run-gates.runlog.test.sh` — the fork-count arm and its ceiling.
- `tools/run-gates/run-gates.evidence.test.sh` — the key-parity, output-capture and log-name arms.
- `tools/run-gates/README.md` — the arm and its ceiling.
- `tools/run-gates/kit.toml` — the kit version, moved once for the build.
- `tools/lib/resolve-python.test.sh` — S12's ban arm, besides its own wrapper.
- `memory/map/generated/symbols.json` — regenerated, since S10 deletes a shell function.
- `tools/hooks/kit.toml`, `tools/memory-tree/kit.toml`, `tools/unattended/kit.toml`,
  `tools/workflows/kit.toml` — each touched kit's version, moved once after its last edit.
- S11's suite copies, each file `git grep -l "<<'RKD'" -- '*.test.sh'` lists:
- `.githooks/pre-push.runlog.test.sh`, `.githooks/pre-push.test.sh`,
  `skills/session-kickoff/manifest-check.test.sh`, `tools/check-agent-cap-restatement.test.sh`,
  `tools/check-hook-destinations.test.sh`, `tools/check-line-length.test.sh`,
  `tools/check-playbook-parity.test.sh`, `tools/check-spec-tokens.test.sh`,
  `tools/check-testsuite-counts.test.sh`, `tools/check-wiring.test.sh`,
  `tools/hooks/agent-cap.test.sh`, `tools/hooks/scratch-guard.test.sh`,
  `tools/memory-tree/check-memory-hygiene.test.sh`,
  `tools/memory-tree/kit-dogfood-parity.test.sh`, `tools/memory-tree/marker-contract.test.sh`,
  `tools/memory-tree/merge-rows.test.sh`, `tools/run-gates/run-gates.test.sh`,
  `tools/run-gates/run-gates.turnstile.test.sh`, `tools/run-gates/run-selftests.test.sh`,
  `tools/unattended/adopt-unattended.test.sh`, `tools/unattended/check-brief-recorded.test.sh`,
  `tools/unattended/check-pass-order.test.sh`, `tools/unattended/gate-guard.test.sh`,
  `tools/unattended/runlog-writer.test.sh`, `tools/unattended/stall-recorder.test.sh`,
  `tools/unattended/stop-guard.test.sh`, `tools/workflows/check-protocol-parity.test.sh`,
  `tools/workflows/check-review-join.test.sh`, `tools/workflows/check-verifier-fanout.test.sh`,
  `tools/workflows/tier2-review.test.sh`, `tools/workflows/unattended-build.test.sh`

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
- **Moving the legs parse up to the process-monitor block** instead of the block down. It would report
  a manifest parse error before the turnstile rather than after it, and would read the timing cache
  while another bar may still be rewriting it.
- **Re-rendering the marked region from the canonical file.** No byte inside the markers changes, so a
  re-render is a no-op the parity arm already proves; only the wrapper moves.

## 5. Production-readiness checklist

- security: `redact` must still mask every `user:pass@` the old pipeline masked; the guard is a superset test on `://` and `@`, so it can only run more often than needed, never less.
- perf / scale: the research's estimate is about 1270 s plus 910 s quiet across the canary family; the real bar gains little directly, plus one python per bar where process monitoring is adopted (S10).
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
- **AC10** — When the fork-count arm traces one bar over a fixture carrying `.process-monitor.conf`, the
  count of `$PYBIN` execs before the first leg dispatch is one fewer than a fixture copy of the runner
  at base traces, and `PROCMON_WHY` matches base's bytes for a found kit, a missing kit and a refusing
  scope. Red when: the python count is unchanged, or a refusal's text differs or aborts the parse.
  figure: both python counts DERIVED from the two traces at observation.
- **AC11** — When the parity arm of `python resolver (behaviour + inline parity + idiom ban)` grades the
  `resolve_kit_dir` row after the pass, every copy's marked region equals `tools/lib/resolve_kit_dir.py`
  byte for byte, and its population covers every file `git grep -l '>>> resolve_kit_dir'` lists outside
  `memory/`. Red when: a wrapper edit moved a byte between the markers, or a copy left the population.
- **AC12** — When one suite copy's wrapper is reverted to `"$(cat <<'RKD'` in a scratch clone, the S12
  ban arm reds naming that file, and a comment spelling the same idiom stays silent. Red when: the
  reverted wrapper passes, or the comment fires.

## 7. Gates

`agent-cap self-test` · `agent-instructions self-test` · `backlog migration selftest` ·
`branch-guard self-test` · `build-index selftest` · `check-arms selftest` ·
`check-wiring self-test` · `codebase-map adopter e2e` · `codebase-map kit selftest` ·
`corpus-ids selftest` · `dead-path carriers self-test` · `drift-audit selftest` ·
`foreign-prefix parity (every self-test at three prefixes)` · `gotchas selftest` ·
`hook destinations self-test` · `install-prefix self-test` · `kit-placeholders self-test` ·
`kit/dogfood doc parity` · `lexicon naming predicates` · `line-length gate selftest` ·
`manifest-check self-test` · `memory-hygiene self-test` · `memory-recall kit selftest` ·
`playbook parity selftest` · `pre-push bar self-test` · `pre-push run-log line` ·
`pre-push self-test` · `profile-bar selftest` · `push-main self-test` ·
`pytest-guardrails self-test` · `python resolver (behaviour + inline parity + idiom ban)` ·
`recall floor` · `recall floor arms` · `review-join self-test` · `row-grammar selftest` ·
`row-keyed merge driver replay` · `run-gates adopter e2e` · `run-gates canary` ·
`run-gates evidence` · `run-gates gov canary` · `run-gates run-log line` · `run-gates turnstile` ·
`run-selftests self-test` · `scratch-guard self-test` · `settings-merge selftest` ·
`spec-tokens self-test` · `straggler-guard arms` · `tier2-review self-test` ·
`transition-audit arms` · `unattended-build self-test` · `verdict-epoch self-test` ·
`verifier fan-out self-test` · `harness arms (fail branches armed or pinned)` ·
`shell hygiene (a loop fed by a command substitution)` · `codebase-map coverage + freshness` ·
`testsuite counts (every bar self-test prints one)` · `line length` · `kit version markers` ·
`kit epoch (shipped bytes move, the version moves)` ·
`verdict epoch (kit version dates the engine)` · `memory hygiene` ·
`spec tokens (a spec's own names resolve)`

New arm: tools/run-gates/run-gates.runlog.test.sh · covers AC8 AC9 AC10 · a closed trace descriptor, then one added `$(date +%s)` in a fixture copy of `runleg` · its `FLOOR_ASSERTIONS` rises by the assertions added
New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC1 AC2 AC3 AC4 AC6 AC7 · each builtin swapped back for a variant that loses the byte the arm pins · its `FLOOR_ASSERTIONS` rises by the assertions added
New arm: tools/lib/resolve-python.test.sh, the S12 ban beside its section 3 ban · covers AC11 AC12 · one suite copy's wrapper reverted to the cat capture in a scratch clone, and a commented specimen · none, the suite pins no assertion floor

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
  - RESOLVED (owner, 2026-10-10): (a) fold it in this unit, re-rendering every copy of the canonical function.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.
- rev-2 · 2026-10-10 · §2 §3 §4 §5 §6 §7 S10 S11 S12 AC10 AC11 AC12 · folded the owner's F1 ruling (a):
  the process-monitor kit dir moves into the legs-parse python, every suite copy's `resolve_kit_dir`
  wrapper takes the builtin read, the parity suite gains a ban arm, and the edge to
  `TOOL-aSparedSpawn-8` names who converts the product copies.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "count forks of a traced runner invocation"` ranked name-token
neighbours (`counts`, `build_invocations`, `derive_runner_verbs`) and the `run-gates` affordance seam;
the seam extended here is in that kit and the probe did not rank it: `measure_execs`, `run_traced` and
`build_traced_runner` in `run-gates.runlog.test.sh`, which already trace this runner on their own
descriptor to count execs after the last leg. The fork-count arm adds a pid field to the same `PS4`.
For S12 the seam is the section 3 ban of `tools/lib/resolve-python.test.sh`, whose comment strip and
planted specimen the new ban reuses; for S10 it is the legs-parse program itself, which already
inlines a parity-gated canonical (`resolve_prefix_token`) the same way.

Recall terms used: runleg spawns exec count xtrace measure_execs baseline EPOCHREALTIME rev-parse runner startup
