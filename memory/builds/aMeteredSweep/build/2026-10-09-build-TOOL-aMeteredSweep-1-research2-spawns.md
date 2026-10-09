# Appendix — Unneeded process creation in the repo's shell code: census, fork-free replacements, lint rules, top edits

**Serves:** research TOOL-aMeteredSweep-1

A read-only research pass by one of five agents on 2026-10-09, kept verbatim below its first heading. Figures are estimates from static counts and one-line timings unless marked measured; the ranked synthesis is `2026-10-09-build-TOOL-aMeteredSweep-1-research2-menu.md`.


Node `a`, 2026-10-09, worktree `gate-runner-profiling-optimization-5d1f1e` at `6bc6c949c`. This was a read-only
pass. I ran no gate leg, suite, `*.test.sh` or `run-gates.sh`. The only things executed were micro-benchmarks
of one-line idioms in Git-Bash 5.3.9 (cygwin build), plus Python scanners over `git ls-files '*.sh'`. The
scanners are kept in the scratchpad beside this file: `census.py`, `classify.py`, `purefn2.py`, `loops.py`,
`toplevel.py` and `forkcount.sh`.

All counts below are STATIC SITES. A site inside a loop or a hot function runs many times, and a site in a
cold branch may never run. Where a figure says "per invocation" or gives seconds, it is an estimate. It
multiplies sites by a visible loop bound and by an invocation count, and those invocation counts come from
the aMeteredSweep research appendices (`memory/builds/aMeteredSweep/build/*-research-*.md`), not from a
trace. Treat every second as good to about a factor of two. Several of the edits overlap that build's
levers 6, 8, 9, 10 and 14; where they do, the lever is named, and the two sets of savings must not be added.

## 0. Bottom line

- **The unit of cost is a process creation (P): one fork, or one exec.** Under Cygwin/MSYS, a builtin
  inside `$(…)` costs a whole fork. In the measurements below a fork is 200–315 ms and a fork+exec is
  500–660 ms under the current load. The fork-free spelling of the same operation costs 0.01–0.4 ms. That
  is a factor of 1,000 to 100,000, so ANY executed site matters once it sits in a path called a thousand
  times.
- **722 `$(f …)` sites call a function whose body spawns nothing** (368 product, 354 suite sites). Each of
  those is one fork that buys nothing. 290 of them are in `tools/unattended/unattended.sh` alone, including
  188 `$(fact …)`, 30 `$(runmd_of …)` and 28 `$(readme_of …)`.
- **The hottest fixed costs are in the per-call preludes.** The unattended driver
  (`unattended.sh:84,120,165,479,653,656,662`) pays about 17 avoidable P on EVERY call, and the suites
  make about 1,450 calls. `check-unattended.sh:482-587,1164-1166` pays 23 `$(core_of …)` forks, and each
  of them re-reads about 900 lines of the 13k-line driver in a bash `read` loop (146 ms measured), on
  every one of about 450 invocations.
- **Two zero-false-positive bans are available today:** `$(date [-u] +%s)` and `$(cat <<'TAG' …)`. One
  latent-bug ban costs nothing because the tree holds none: `$(<file 2>/dev/null)` silently reads EMPTY
  (verified below). The other classes need a count registry keyed on (path, class), which is the same
  grammar as `memory/project/location-probe-waivers.txt`.
- **Forks per invocation can be measured deterministically, with no clock.** A `PS4='+${BASHPID}|'`
  trace through `env SHELLOPTS=xtrace BASH_XTRACEFD=<fd>` follows child bash scripts and gives a stable
  lower bound. That makes a ceiling arm that cannot flake under load, unlike the clock arms the
  aMeteredSweep build had to fix. The prototype was verified on a specimen (§4.2).

## 1. Cost model, measured this session

Each figure is a 20-iteration loop in Git-Bash 5.3.9 on node `a`, with the machine LOADED (a bare `$(:)`
read 197–315 ms against the 90–290 ms quiet figure in the brief). The script is `bench.sh` /
`bench2.sh` / `bench3.sh` in the scratchpad. The ratios are what matter; the absolute values move with
load.

| idiom | ms/iter | fork-free replacement | ms/iter |
|---|---:|---|---:|
| `x=$(:)` (one fork, no exec) | 197–315 | — | — |
| `/usr/bin/true` (fork+exec) | 658 | — | — |
| `x=$(printf "%s" a)` | 337 | `printf -v x "%s" a` | 0.01 |
| `x=$(echo a)` | 369 | `x=a` / `printf -v` | 0.01 |
| `x=$(fn a)`, fn = `printf` | 173 | `fn a >/dev/null; x=$G` / `REPLY` | 0.02 |
| `x=$(cat "$f")` | 1061 | `x=$(<"$f")` (bash 5.3: no fork) | 0.35 |
| | | `IFS= read -r -d '' x <"$f"` / `mapfile` | 0.38 |
| `x=$(cat <<'RKD' … RKD)` | 436 | `IFS= read -r -d '' x <<'RKD' … RKD` `|| :` | 0.14 |
| `x=$(basename "$p")` | 711 | `x=${p##*/}` | 0.02 |
| `x=$(dirname "$p")` | 864 | `x=${p%/*}` (guarded, §2) | 0.02 |
| `x=$(date +%s)` | 604 | `x=$EPOCHSECONDS` | 0.01 |
| `x=$(date -u +%Y-%m-%dT%H:%M:%SZ)` | 914 | `TZ=UTC0 printf -v x '%(%Y-%m-%dT%H:%M:%SZ)T' -1` | 0.12 |
| `$(printf … \| grep -c foo)` | 1646 | `mapfile`/loop, or one `awk` for many counts | 0.13–0.21 |
| `grep -c foo <<<"$v"` (in `$(…)`) | 891 | as above | 0.13 |
| `printf … \| wc -l` | 976 | `mapfile -t a <<<"$v"; n=${#a[@]}` | 0.13 |
| `[ "$(printf %s "$v" \| wc -l)" -ne 0 ]` (newline test) | 668 | `[[ $v == *$'\n'* ]]` | 0.02 |
| `printf %s "$v" \| grep -qE "$re"` | 607 | `[[ $v =~ $re ]]` | 0.04 |
| `$(printf %s "$r" \| tr -d '\r')` | 966 | `${r//$'\r'/}` | 0.02 |
| `$(echo "$p" \| sed 's/file/x/')` | 1308 | `${p/file/x}` | 0.02 |
| `$(echo "$p" \| tr a-z A-Z)` | 1187 | `${p^^}` | 0.01 |
| `timeout -k 1s 10 true` (a capability probe) | 796 | memoise or probe lazily (§3) | — |
| `$(git --version)` vs `$(G --version)`, G = git wrapper | 524–573 vs 555–676 | the wrapper adds no clear extra fork (+6 to +18 %, within noise) | — |
| `python -c pass` | 1366 | memoise the resolver probe (§3) | — |
| `bash -c :` | 612 | — | — |

Two further measurements bear on the rules:

- **A bash `read` loop is fork-free but not free.** One `while IFS= read -r` pass over the 13,310-line
  driver took 2,026 ms, and over its first 906 lines 146 ms. Above about 1–2k lines, ONE `awk` beats a
  bash loop, so a "fork-free" rewrite that replaces an `awk` with a `read` loop over a large file is a
  regression. `core_of` (`check-unattended.sh:471`) is the live instance: it is fork-free inside and is
  still called 23 times through `$(…)`.
- **The pipeline cost model holds.** `$(a | b)` = 1 comsub fork + 1 fork per pipeline element + 1 exec
  per external element. So `$(printf … | grep -c …)` is about 4 P, which matches the 1.6 s against
  `$(:)` at 0.3 s.

## 2. Census

### 2.1 Pattern totals (tracked `*.sh`)

There are 124 files: 59 product, of which 6 are build-folder probes under `memory/`, and 65 suites
(`*.test.sh`). Comments and quoted-heredoc bodies are excluded. The source is `classify.py` and
`census.py`.

| pattern | product | suites | replacement class |
|---|---:|---:|---|
| any command substitution `$(`/backtick | 3,094 | 11,468 | — |
| `$(f …)`, f a **leaf-pure** shell function (no spawn in its body) | **368** | **354** | out-variable, §3 R1 |
| `$(f …)`, f any repo-defined shell function (incl. `GIT` wrapper) | 1,172 | 4,910 | case by case |
| `$(printf FMT ARGS)`, no pipe (pure) | 18 | 115 | `printf -v` |
| `$(printf …` (all forms, mostly `printf "$X" \| tool`) | 429 | 811 | builtins or one `awk` |
| `$(echo WORD)` | 2 | 0 | `read -ra` / assignment |
| `$(cat "file")` | 30 | 184 | `{ x=$(<f); } 2>/dev/null` |
| `$(cat <<'TAG' …)` | 18 | 34 | `read -r -d ''` |
| `$(basename …)` | 36 | 61 | `${p##*/}` |
| `$(dirname …)` | 86 | 222 | `${p%/*}` + guard |
| ` …$(cd "$(dirname …)" && pwd)` script-dir prologue | 47 | 75 | see R5 |
| `$(date [-u] +%s)` | 23 | 99 | `$EPOCHSECONDS` |
| `$(date +%s%N)` | 7 | 4 | `${EPOCHREALTIME/[.,]/}` (µs) |
| `$(date +FMT)` (now, no `-d`/`-r`) | 63 | 119 | `printf '%(FMT)T' -1` |
| `$(date -d/-r …)` (parsing — NOT replaceable) | 12 | 14 | keep |
| `$(printf/echo … \| grep -c …)` | 57 | 171 | `mapfile`/loop, or one `awk` |
| `$(printf/echo … \| wc -l)` | 15 | 6 | `mapfile`, or `[[ == *$'\n'* ]]` |
| `printf/echo "$v" \| grep -q…` | 74 | 377 | `[[ =~ ]]` / `case` |
| `printf/echo … \| sed 's/x/y/'` (trivial) | 9 | 10 | `${v//x/y}` |
| `printf/echo … \| tr …` | 36 | 23 | `${v//…}`, `${v^^}` |
| `… \| head -1` / `head -n 1` | 135 | 129 | `${v%%$'\n'*}`, `grep -m1` |
| `$(resolve_python …)` (each RUNS a python probe) | 41 | 56 | memoise, R7 |
| `timeout -k 1s 10 true` capability probe | 6 | 3 | memoise or lazy, R8 |
| `python -c` / `"$PY" -c` | 6 | 68 | batch |
| `node -e` | 2 | 23 | batch |
| `bash -c` | 3 | 96 | batch |
| `git …` (any) | 875 | 5,466 | memoise identical queries |
| `git config user.*/core.autocrlf` (fixture setup) | — | 232 | env, R9 |
| `git init` | — | 234 | template + `cp -r` |

### 2.2 Leaf-pure functions called through `$(…)`

These are the clearest waste: each call is exactly one fork, and removing it changes no work at all.
`purefn2.py` resolves each call per file, against a same-file definition or the sourced
`lib-unattended.sh`. A callee that calls another function is treated as impure, so this is a LOWER
bound.

| sites | function | defined in |
|---:|---|---|
| 188 | `fact` | `tools/unattended/unattended.sh:1208` (pure bash since aRepatriatedFork; the CALL still forks) |
| 30 | `fact_of` | `tools/unattended/check-unattended.sh:852` |
| 30 / 28 | `runmd_of` / `readme_of` | `unattended.sh:1196-1197` (a one-line `printf` of a path) |
| 76 | `derive_sidecar` | `stop-guard.test.sh`, `stall-recorder.test.sh` |
| 53 / 43 | `rec` / `review_out` | `tools/workflows/unattended-build.test.sh` |
| 25 / 25 | `run_in` / `S` | `.githooks/straggler-guard.test.sh`, `hygiene-parity.test.sh` |
| 22 / 18 | `audit` / `audit_rc` | `tools/memory-tree/transition-audit.test.sh` |
| 11 / 4 | `declared_scalar` / `declared_list` | `check-playbook.sh:343`, `unattended.sh:11299` |
| 9 / 5 / 4 | `first_of` / `settings_json` / `abspath` | `tools/check-wiring.sh:270…` |
| 6 | `ask_home_of` | `lib-unattended.sh` |
| 4 | `normpath` | `lib-unattended.sh:617`, still `$(…)` at `:884`, `:893`, `unattended.sh:12666`, `:12716` |

By file: `unattended.sh` 290, `unattended-build.test.sh` 124, `stop-guard.test.sh` 54,
`transition-audit.test.sh` 40, `check-unattended.sh` 34, `hygiene-parity.test.sh` 32.

The NON-pure function substitutions that matter most, because they sit in hot loops or preludes, are:

- `unattended.sh`: `GIT` 120, `ask_field` 16, `resolve_sidecar_dir` 13, `derive_index_repair` 11,
  `read_utc_now` 9 (a `date` wrapper), `resolve_python` 8.
- `check-unattended.sh`: `GIT` 39, `core_of` 26 (bash read loop over the driver).
- `run-gates.sh`: `ts_now` 9 sites, 11 uses (`date +%s`, `:1059`).
- `manifest-check.sh`: `getval` 5 (`:269`, a `printf|sed|head|sed` = 6 P per call).
- `run-selftests.sh`: `attr_count` 5, `read_now_ms` (`:1246`, `$(( $(date +%s%N) / 1000000 ))` = 3 P).

### 2.3 Loops whose body spawns, the multiplier

`loops.py`, product files. The figure is static spawn sites inside the body, and the loop header
names the iteration domain.

| file:line | loop | body sites | domain |
|---|---|---:|---|
| `tools/unattended/unattended.sh:11023` | `for _ad_id in $AD_SCOPE` | 113 | per ask |
| `tools/unattended/check-playbook.sh:393` | `while read -r pb` | 100 | per playbook |
| `tools/unattended/check-brief-recorded.sh:356` / `:393` | per README / `for id in $ids` | 86 / 60 | 66 READMEs / 656 ids |
| `tools/unattended/check-pass-order.sh:314` / `:375` | per README / per id | 59 / 30 | same |
| `tools/unattended/check-unattended.sh:3751` / `:3980` | `for f in $RUNS` | 47 / 43 | 82 run records |
| `tools/unattended/check-unattended.sh:651` | `for rvf in $(GIT ls-files …RUN*.md)` | 33 | run records |
| `tools/unattended/unattended.sh:4210-4235` | `ask_rank_order`, selection sort | ~12 P per inner step | **O(n²)** in asks |
| `tools/unattended/lib-unattended.sh:1943` | `for _bu_c in $(GIT log …)` (`baseline_units`) | 14 | per commit, called per record |
| `tools/unattended/lib-unattended.sh:1127` | `for _bc_c in $(GIT rev-list …)` (`build_commit`) | 8 | per commit, called per id |
| `tools/run-gates/run-gates.sh:1269` | turnstile wait loop | 19 | per poll (`$(ls\|sort\|head)` + `$(basename)` each tick) |
| `tools/memory-tree/check-memory-hygiene.sh:1328`, `:2228`, `:562` | `printf \| grep \| while read` | 11–13 | per file / row (bodies mostly builtins) |
| `tools/check-wiring.sh:819`, `:509`, `:1385` | per name / hook / ref | 22 / 11 / 11 | small constant lists |

### 2.4 The same `git` question asked repeatedly in one run

- **The runner, once per invocation.** `run-gates.sh` asks `rev-parse --show-toplevel` (`:98`,
  `:2189`), `--git-dir` (`:243`), `--git-common-dir` (`:1044`, `:1484`, `:3420`, `:3845`), `HEAD`
  (`:2166`, `:3827`, `:3873`) and `hash-object -- "$LEGS_FILE"` (`:2172`, `:3829`, `:3875`). One
  `git rev-parse --show-toplevel --git-dir --git-common-dir` answers three of them in a single spawn.
  The receipt writers at `:3827`/`:3873` are alternatives, so about 5 git spawns per invocation are
  removable.
- **The runner re-executes itself.** `run-gates.sh:91-96` re-execs under an absolute `$0` when `$0` is
  relative, which repeats the `:81` prologue (`$(cd "$(dirname "$0")" && pwd)`, 3 P). That is small,
  and it is deliberate.
- **`lib-unattended.sh:1942-1950`, per commit.** It runs `GIT show` and then the SAME blob through
  `extract_run_facts | grep` twice (`base:`, then `phase:`), and its prologue is
  `$(cat "$_bu_rel" | extract_run_facts | grep -m1 …)`, a useless `cat`.
- **Suites, fixture setup.** There are 232 `git config user.email|user.name|core.autocrlf` sites and
  234 `git init` sites. The memory-hygiene suite alone holds 24 init + 24 + 24 + 17 config; pre-push holds
  24 `rev-parse --git-dir` + 24 `rev-parse HEAD`; unattended.test.sh holds 270 `add -A` and 45
  `rev-parse HEAD`.

### 2.5 Ranking: estimated P per invocation × invocations per bar and held suites

The invocation counts come from the aMeteredSweep appendices; the P per invocation from static sites
on the executed path. The suites dominate: the self-test tier was 46,408 of the profiled bar's 54,049
leg-seconds.

| # | file | est. P per invocation | invocations (bar + suites) | est. P total | avoidable share |
|---:|---|---:|---:|---:|---|
| 1 | `tools/unattended/unattended.sh` (+ sourced `lib-unattended.sh`) | ~30 prelude + 10–200 per verb | ~1,450 (`unattended.test.sh`, 8 shards) + stop-guard/resume-tick suites | ~90k–150k | prelude 17 P, `fact` 1 P per read, `runmd_of`/`readme_of`, `printf` |
| 2 | `tools/unattended/check-unattended.sh` | repo leg 3,500–5,000; fixture 100–150 | 1 + ~450 | ~50k–75k | 23 `core_of` forks, `fact_of`, per-record loops |
| 3 | `tools/run-gates/run-gates.sh` | 40–60 fixed + 45–65 per leg | bar 1×126 legs; ~400 runner runs in the canary, evidence, turnstile, runlog and foreign-prefix suites | ~30k–50k | 7 P per leg in `runleg`, ~10 P of repeated git, a 2 P timeout probe |
| 4 | `tools/memory-tree/check-memory-hygiene.sh` | 150–250 shell + ~11 python | 1 + ~97 in its suite + parity suites | ~15k–25k | ~110 `printf "$FILES" \| …` pipelines; PRE_* counts |
| 5 | `tools/unattended/check-pass-order.sh` + `check-brief-recorded.sh` | ~2,950 together | 1 each + their self-tests | ~5k–10k | `build_commit` per id (prior lever 14) |
| 6 | `tools/check-wiring.sh` | ~80–150, 2 python probes (`:454`, `:465`) | ~120 in its suite | ~10k–18k | resolver ×2, `first_of`/`json_str` forks |
| 7 | `skills/session-kickoff/manifest-check.sh` | ~60–100 | 1 + 52 static sites in its suite | ~4k–8k | `getval` 6 P × 5, `printf \| grep -q` |
| 8 | `tools/unattended/check-playbook.sh` | ~100 per playbook | 1 + its suite | ~2k–5k | `declared_scalar`/`declared_list` forks |
| 9 | `tools/push-main.sh` | ~60 | push-main + pre-push suites (hundreds of runs) | ~5k–10k | `resolve_python` ×2 (`:561`, `:590`), `$(date +%s)` (`:234`, `:240`) |

## 3. Replacement catalogue: portable to bash 5.2, cost, traps

R1–R13 cover the patterns the brief named, and two the census added. `${ cmd; }` is not used anywhere
below, because it is a parse error on CI's bash 5.2. The repo already relies on `EPOCHSECONDS` at 27
sites, so bash ≥ 5.0 features are fine.

**R1. `$(f args)` where f computes a value in the shell → the GLOBAL-OUT convention.**
- **The convention:** the function sets a named global and also prints, and a hot caller writes
  `f args >/dev/null; v=$F_V`. This is the convention `lib-unattended.sh:635` already established for
  `normpath`/`_np`.
- **Saving:** one fork per call (173–315 ms here). The redirect of a builtin's stdout to `/dev/null`
  costs nothing.
- **Trap: keep the call SPELLING.** Structural arms grep the source by it.
  `check-unattended.sh:5727-5745` recognises a phase read as `fact <file> phase`, and
  `unattended.test.sh:7714-7723` counts `baseline_units ` call sites. A rename to `fact_into v f phase`
  or `fact -v v f phase` would leave the c39 arm BLIND rather than red: a guard sharing a spelling with
  the code it guards.
- **Trap: dynamic scope.** `printf -v "$1"` writes to the callee's own `local` of the same name when the
  caller passes a name that collides with it. A fixed global name per function avoids that, so prefer
  it to a `-v name` parameter.
- **Trap: subshell isolation was a feature.** Check each function for `cd`, `set`, `trap`, `exit` and
  global writes. `exit` inside `$(…)` only ended the subshell, but without one it ends the script. The
  "pure" classifier in §2.2 excluded no such functions by name, so a reviewer must still read each body.
- **Trap: newline stripping.** `$(…)` strips ALL trailing newlines, and the global keeps them. `fact`
  prints `"%s\n"`, so set the global WITHOUT the newline.
- **Trap: exit status.** `if x=$(f)` and `f >/dev/null; x=$F_V` carry the same status only when the
  read of `$F_V` is not placed between the call and the test.

**R2. `$(printf FMT ARGS)` → `printf -v var FMT ARGS`.**
- **Saving:** one fork.
- **Trap:** when FMT ends in `\n`, `$(…)` stripped the newline and `printf -v` keeps it, so drop it
  from FMT.
- **Trap:** `printf -v 'a[i]'` works, but `printf -v` into a `local` must follow the `local`
  declaration.

**R3. `$(cat "f" [2>/dev/null])` → `{ x=$(<"f"); } 2>/dev/null` or `IFS= read -r -d '' x <"f" || :`.**
- **Saving:** on bash 5.3 `$(<f)` does not fork (measured 0.35 ms). On bash 5.2 (CI) it still forks
  but skips the `cat` exec. That is not measured here, because no 5.2 is installed on node `a`, and
  WSL is 5.3.9 too.
- **TRAP, verified: `$(<f 2>/dev/null)` reads NOTHING.** Any extra redirection defeats the special
  case, so bash runs an empty command with redirections. It returned `[]` and still forked (417 ms).
  The silencing goes OUTSIDE: `{ x=$(<f); } 2>/dev/null` keeps rc=1 on a missing file, verified.
- **Trap:** `read -r -d ''` returns 1 at EOF (put `|| :` under `set -e`) and keeps trailing newlines,
  which `$(…)` stripped.
- No `$(<… 2>…)` site exists in the tree today, which is why banning it costs nothing.

**R4. `$(cat <<'TAG' … TAG)` → `IFS= read -r -d '' var <<'TAG' || :` then `var=${var%$'\n'}`.**
- **Saving:** 2 P, 436 ms against 0.14 ms.
- **Where:** 18 product sites, almost all the inline `resolve_kit_dir` probe (`lib-unattended.sh:133`,
  `run-gates.sh:145`, `check-wiring.sh:399`, `manifest-check.sh:678`, …).
- **Cost of the edit:** `resolve_kit_dir` has 47 byte-identical gated copies
  (`resolve-python.test.sh:108`), so this is one canonical edit plus a re-render of the copies.

**R5. `$(basename p)` / `$(dirname p)` → parameter expansion, with the edge cases spelled out.**
- `base=${p%/}; base=${base##*/}`, and `case $p in */*) d=${p%/*}; d=${d:-/} ;; *) d=. ;; esac`.
- **Trap:** these differ from coreutils on `p=/` (basename `/`), on repeated trailing slashes, and on
  `basename p .sh` (suffix: `${base%.sh}`).
- **The script-dir prologue.** `X="$(cd "$(dirname "$0")" && pwd)"` (47 product sites, 2–3 P) becomes
  `_d=${0%/*}; [ "$_d" = "$0" ] && _d=.` followed by `X=$(CDPATH= cd -- "$_d" && pwd)`, which is 1 P.
  Going to 0 P needs `cd`/`$PWD`/`cd -` in the current shell. That is unsafe in a sourced library, and
  safe at the top of a script before anything relative is opened.

**R6. `date`.**
- `$(date [-u] +%s)` → `$EPOCHSECONDS`, which is exact (epoch is UTC).
- `$(date +%s%N)` → `${EPOCHREALTIME/[.,]/}` gives MICROseconds, so scale `*1000` or change the divisor.
  The `[.,]` covers a locale with a decimal comma.
- `$(date [-u] +FMT)` → `[TZ=UTC0] printf -v x '%(FMT)T' -1`. This was verified byte-identical for
  `%Y-%m-%dT%H:%M:%SZ` under `TZ=UTC0` and for `%z`, and `TZ` was left unset afterwards.
- **Trap:** `%N`, `%:z` and the GNU `-`/`_` padding flags are glibc/coreutils behaviour; `printf %()T`
  uses the C library `strftime`, so keep those formats on `date`.
- **Trap:** `date -d`/`-r` parsing has no builtin equivalent. It is excluded from the ban (12 product
  sites).
- `read_utc_now` (`unattended.sh:1404`), `ts_now` (`run-gates.sh:1059`) and `read_now_ms`
  (`run-selftests.sh:1246`) become one-line builtins plus R1.

**R7. Cross-process memo for `resolve_python`.**
- Each call RUNS `"$c" -c "import sys"`: a 0.9–1.4 s python start, plus the `$(…)` fork. That is by
  design (`tools/lib/resolve-python.sh:25`), so a stub cannot answer.
- Nothing exports a verified launcher (`git grep 'export GOV_PYTHON'` is empty). So the runner, each
  suite and every resolving script re-probe from scratch: `check-wiring.sh` twice (`:454`, `:465`),
  `push-main.sh` twice (`:561`, `:590`), the hygiene checker once per run (`:432`), the runner once per
  run (`:191`), `pyrun.sh:30` once per merge-driver call, and 8 driver verbs.
- **Remedy:** the canonical resolver returns at once when `GOV_PYTHON_RAN` equals the first nonempty
  candidate, and the RUNNER, which already resolves `PYBIN`, exports both `GOV_PYTHON` and
  `GOV_PYTHON_RAN`.
- **Trap:** this is a guard that trusts an inherited variable. An operator or stale environment setting
  `GOV_PYTHON_RAN` skips the probe. The failure stays loud, because the launcher fails at first real
  use, but it moves from the resolver's named refusal to a later, vaguer error. Accept that explicitly,
  or key the memo on `$PPID`-independent evidence such as `command -v` path plus mtime.
- **Cost of the edit:** 25+ inline byte-identical copies, gated, so one canonical edit plus a re-render.

**R8. The `timeout -k 1s 10 true` capability probe.**
- It runs on EVERY driver call (`unattended.sh:165`), every `check-unattended.sh` run (`:1186`, `:5866`),
  every runner run (`run-gates.sh:703`) and `lib-unattended.sh:1267`. Each is 2 P (796 ms loaded).
- **Remedy:** probe lazily in the one function that runs a bounded command, or inherit
  `GOV_TIMEOUT_K_LIVE` from the runner or suite.
- **Trap, lazy:** the liveness NOTE at `unattended.sh:423/428` is printed at prelude time, and moving
  it changes WHEN an operator is told.
- **Trap, inherited:** same caveat as R7. Also, the probe is deliberately 10 s, not 1 s
  (TOOL-aSiftedFork-7), so a memo must never be recorded by a 1 s probe.

**R9. Fixture git identity through the environment** (suites; this is prior lever 10).
- Export `GIT_AUTHOR_NAME/EMAIL`, `GIT_COMMITTER_NAME/EMAIL`, plus
  `GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.autocrlf GIT_CONFIG_VALUE_0=false` once in the prologue,
  and delete the per-repo `git config` lines. That is 2–4 git spawns per fixture.
- **Trap:** `GIT_CONFIG_COUNT` needs git ≥ 2.31 (node `a` has 2.54).
- **Trap:** env config reaches EVERY git the arm runs, including the code under test. An arm that
  asserts behaviour under a DIFFERENT `core.autocrlf` must override it locally.
- **Trap:** product code that reads `git config user.email` sees the env identity only through
  `git var`, not through `git config`.

**R10. Per-variable pipelines to builtins.**
- `printf %s "$v" | grep -qE re` → `[[ $v =~ $re ]]`. Keep the regex in a variable or unquoted.
  - **Trap:** grep matches LINE-wise, and `^`/`$` in `=~` anchor the whole string. That is identical only
    for single-line values; for multi-line values use a `case`/loop.
  - **Trap:** `=~` uses the C library regex, so `\b`, `\<` and `\d` do not port. `grep -F` becomes a
    `case "$v" in *"$needle"*)` test.
  - **Trap:** `grep -x` becomes the anchors `^…$`.
- `| wc -l` used as a newline test → `[[ $v == *$'\n'* ]]`. The live sites are `unattended.sh:2753`,
  `:5716`, `:5920`, `:6940`, each 3–4 P.
- `| tr -d '\r'` → `${v//$'\r'/}`.
- `| head -1` → `${v%%$'\n'*}`.
- `| grep -c .` on a variable → `mapfile -t a <<<"$v"`, then count the non-empty entries.
  - **Trap:** `<<<` appends a newline, so an EMPTY `$v` yields one empty element. `grep -c .` counts
    non-empty lines; `wc -l` counts newlines.
- MANY counts over ONE population (`check-memory-hygiene.sh:461-485`, six `$(printf "$FILES" | grep -cE …)`)
  → one `awk` that prints `name count` pairs. That is 2 P instead of 18.
  - **Trap:** `grep -E` and `awk` ERE differ on intervals: `{4}` needs `--re-interval` on old mawk, while
    gawk and busybox are fine. Check CI's awk.

**R11. Memoise a `$(…)` in a loop whose arguments do not depend on the loop variable.** Hoist it, or
keep an associative array keyed by argument. The instances:
- `build_commit`'s range, the same for every id (prior lever 14);
- `read_landing_commit`, called up to 4× per record (prior lever 9);
- `ask_field` in `ask_rank_order`: 12 P per (pass, id) in a selection sort, so n² × 12. For 10 asks
  that is 600 P. One `awk` over `AW_ROWS` fills `declare -A` maps for status, sev, holds and closers,
  and the sort becomes pure bash.

**R12. Interpreter per item.**
- Instances: `python -c`/`node -e`/`bash -c` in a data-sized loop (`run_wf` 161 sites in
  `unattended-build.test.sh`; `check-hook-destinations.sh:165` python per fragment).
- **Remedy:** one interpreter fed the whole item set, a coproc worker, or `xargs`-style batching.
- **Trap:** per-item failure attribution has to survive the batching (charter §7).

**R13. One reader per big file, not N.**
- **Where:** `core_of`/`read_bare_const` (`check-unattended.sh:471`, `:561`) are 23 calls, each a fork
  plus a bash read of about 900 driver lines.
- **Remedy:** one `awk` emitting every `^[A-Z_]+="…"[ \t]*$` declaration (first wins) into a temp file,
  read once into `declare -A CORE`.
- **Trap:** keep "only whitespace after the closing quote" and first-match-wins exactly. Check 1
  refuses on an empty value, so the map must keep empty-for-absent semantics.

## 4. A lint gate and a spawn-budget arm

### 4.1 Static classes for a `--spawn-idioms` mode of `tools/gate-lint/sh_hygiene.py`

This is the same architecture as `--location-probes`:
- **Population:** every tracked `*.sh` plus every shebang-shell file, narrowed by pathspecs. Start with
  `. :!*.test.sh :!memory/`, as that leg does.
- **Code extraction:** `extract_code` for the comment cut, with the heredoc tracker skipping the bodies
  of QUOTED heredocs. Those are data, such as the embedded python and the specimens suites write.
- **Registry:** one, `<path> TAB <class> TAB <count> TAB <reason>`. It is keyed on (path, class) and
  NEVER on line; `install-prefix waivers are line-keyed` is the repo's own lesson. Equality runs in
  both directions with counts, so a drained site forces its row down in the same commit and the
  population can only shrink.
- **Output:** derived populations and near-miss counts are printed on every run, green included.
- **Self-test:** `--selftest` with specimens in both directions, and its failing case observed (§7).
- **Placement:** cost is one python pass, about 1 s, so it goes `subject = repo` with no guard.
  Memory note: a new GUARDED leg reds foreign specs.
- **Hidden cost:** a new registry under `memory/project/` must be added to hygiene check 3's closed name
  set. That is the same trap the gate-lint `kit.toml` header records.

| class | predicate (on the code half, outside single quotes, not after `\$`) | gating | why |
|---|---|---|---|
| `epoch-date` | `$(date` `[-u]` `+%s)` and `$(date +%s%N)` | **BAN** (drain all 30 product sites in the landing unit) | exact replacement, zero FP |
| `cat-heredoc` | `$(cat <<` | **BAN** (18 product; 47 resolver copies re-render from the canonical) | exact replacement |
| `redirected-read` | `$(<` followed by any further redirection inside the same `$(…)` | **BAN** (0 sites) | always a bug: reads empty (§3 R3) |
| `printf-subst` | `$(printf FMT ARGS)` with no `\|`, `>`, `<` inside, and FMT not ending `\n` | BAN in product (18), registry in suites | exact; the `\n` form is a near miss, printed |
| `pure-fn-subst` | `$(f …)` where f is defined in the same file, or in a library the file sources by a literal path, and f's body holds no `$(`, backtick, `\|`, `<(`, `>(` and no first word outside builtins and keywords | registry | the semantic traps in R1 need a human; a callee calling a function grades impure, which is a MISS, never a false red |
| `cat-file` | `$(cat "<one word>" [2>/dev/null])` | registry | 5.2 keeps a fork; the R3 redirect trap |
| `path-subst` | `$(basename`, `$(dirname` | registry | edge cases (R5) |
| `date-fmt` | `$(date [-u] +FMT)` with no `-d`/`-r` and FMT free of `%N` `%:z` `%-` `%_` | registry | strftime parity per format |
| `var-pipe` | `printf\|echo <one expansion> \|` into `grep -q/-c`, `wc -l`, `tr`, `sed s///`, `head -1`, `cut` | registry | line-wise against whole-string semantics (R10) |
| `spawn-in-loop` | spawn sites inside a `for/while/until` body whose word list or feed is NOT all literals | registry, counts summed per file | the multiplier; literal-list loops (`for f in SKILL.md …`) are exempt |
| `interp-per-item` | `python -c`, `"$PY" -c`, `node -e`, `bash -c` inside such a loop | registry | R12 |

What the header must say it does NOT check:
- execution frequency (a cold usage-message `$(basename "$0")` grades like a hot one; the registry
  reason says so);
- `eval`'d strings and code built in variables;
- substitutions split across line continuations;
- transitive purity;
- repeated identical `git` queries across functions;
- cross-process repeated probes (R7, R8);
- the cost of fork-free work (a bash `read` loop over 13k lines, §1).

The last three are why the static leg needs the runtime arm below.

**Measured populations if wired today.** Product: `epoch-date` 30, `cat-heredoc` 18, `printf-subst`
18, `pure-fn-subst` 368, `cat-file` 30, `path-subst` 122, `date-fmt` ~51, `var-pipe` ~230. That gives a
registry of roughly 60–90 (path, class) rows for product, against the 77 lines of the existing
`substitution-fed-loops.txt`. The suites would add about 200 rows, so wire suites as a second step, with
rows carried rather than drained.

### 4.2 The spawn-budget arm: forks per invocation of a hot entrypoint, with a declared ceiling

**The counter.** It was prototyped as `forkcount.sh` in the scratchpad and verified on a specimen:

```bash
exec {xfd}>"$trace"
env BASH_XTRACEFD=$xfd PS4='+${BASHPID}|${BASH_SOURCE##*/}:${LINENO}|' SHELLOPTS=xtrace \
    bash <entrypoint> <args> >/dev/null 2>&1
exec {xfd}>&-
# forks  = distinct BASHPID values - 1
# execs  = trace lines whose command word is not a builtin, keyword or a function defined in the traced files
```

- `SHELLOPTS` is readonly in bash, so it must be set through `env`. A plain assignment failed with
  "readonly variable", verified.
- Exported `SHELLOPTS=xtrace` makes every CHILD `bash` script trace too. That answers the "bash -x does
  not follow children" memory, and the specimen's child script was traced.
- It is a deterministic LOWER bound. A subshell that traces no command of its own (the comsub parent of
  a pipeline) is not seen, and a plain external command counts once though it costs fork+exec. On the
  specimen it reported 7 pids and 3 externals against 8 forks and 3 execs actually made.
- The PS4 `file:line` field gives each unit a site, so a red arm can print the top 10 lines by count
  rather than a bare total.

**The arm.** A bash leg, `tools/gate-lint/spawn-budget.sh`, `subject = repo`, unguarded:
1. **Calibrate first.** Count a committed specimen with known counts. If the counter disagrees, REFUSE
   ("the counter cannot move"), which is the liveness assertion charter §7 requires.
2. **Run each declared entrypoint once on a fixture.** Discard its output; never assert behaviour from
   a traced run. The candidates, by §2.5:
   - `unattended.sh` on a cheap verb (the prelude);
   - `check-unattended.sh` on the minimal fixture;
   - `run-gates.sh` with a 1-leg and a 2-leg `GATE_LEGS` manifest. The difference is the per-leg cost,
     and the 1-leg run is the fixed cost.
   - `check-memory-hygiene.sh` on a scratch tree;
   - `manifest-check.sh`;
   - `check-wiring.sh --check`.
3. **Compare against `memory/project/spawn-budgets.txt`.** The row is `<id> TAB <ceiling> TAB <reason>`.
   - It is RED when measured > ceiling, which is growth. The message prints the delta and the top
     `file:line` contributors.
   - It is RED when ceiling > measured + max(3, 5%). That is a stale ceiling, so the ratchet only falls,
     as the waiver registries do.
   - It prints `skipped — <id> · <why>` for an entrypoint it could not run.
4. **No clock anywhere**, so it cannot flake on a loaded host. A traced driver call costs about 1.2× an
   untraced one, so the leg is about 1–3 minutes quiet.

What it must announce:
- python and node children are counted as ONE exec each, and their own subprocesses are invisible;
- counts differ between Windows and Linux branches (`cygpath`, the `timeout` probe, resolver
  candidates). Either keep a ceiling per platform, or pin `GOV_PYTHON` and take the max.
- a script that inspects `$-` changes behaviour under xtrace. `run-gates.sh:94` re-execs with `-x`
  when it sees `x`, which is benign. No product script runs `set +x`, checked.
- a script that closes or reuses the trace fd sends trace to stderr. Allocate the fd with `{xfd}>` and
  verify that the trace file is non-empty.

## 5. Top 15 concrete edits, by estimated saving across the bar and the held suites

P is a process creation. Seconds use 0.1 s/P quiet and 0.3 s/P pool-loaded; they are estimates, ±2×,
and NOT additive with the aMeteredSweep levers named in the last column.

| # | edit | file:line | P saved per run (bar + suites) | est. seconds quiet / pool | overlaps |
|---:|---|---|---:|---:|---|
| 1 | Driver prelude: `${0##*/}` for `$(basename)` (`:120`), `${0%/*}` for `$(dirname)` (`:84`); R1 for `resolve_shared_records` (`:653`), `resolve_generated_indexes` (`:656`), `scan_shared_index_overlaps` (`:662`); inside it, parameter expansion in `derive_self_rel`'s loop (`lib-unattended.sh:706-714`, 3 P per level × 2) and `_rg_here` (`:739`); one `mktemp -d` instead of two (`:754`) | `tools/unattended/unattended.sh:84,120,653,656,662`; `lib-unattended.sh:706-714,739,754` | ~17 per call × ~1,450 ≈ 24,000 | 1,500–4,000 pool (8 shards) | lever 8 (lazy preamble) |
| 2 | `fact` call sites to the R1 global-out form, keeping the `fact <file> <key>` spelling the c39 arm greps | `unattended.sh:1208` + 188 sites | 1 per read × 5–15 reads per call × ~1,450 ≈ 7k–22k | 1,000–4,000 pool | lever 8 |
| 3 | `core_of`/`read_bare_const` to ONE `awk` into `declare -A CORE` (R13) | `check-unattended.sh:471,561`; calls `:482-587,1164-1166` | 22 forks + ~2–3 s bash read per invocation × ~450 | 1,500–4,000 pool | lever 2 of the govkit/unattended appendix |
| 4 | Per-record loops: parse every `## Run facts` block once (one `awk` to an assoc array) and `fact_of` via R1 | `check-unattended.sh:3751,3980,651`; `fact_of` `:852` (30 sites) | repo leg 82 × 25–40 ≈ 2,000–3,300 per bar | 200–1,000 on the 3,937 s leg | lever 9 |
| 5 | Memoise `resolve_python` across processes: the runner exports a verified launcher (R7) | `tools/lib/resolve-python.sh:25` (canonical) → 25+ copies; callers `run-gates.sh:191`, `check-memory-hygiene.sh:432`, `check-wiring.sh:454,465`, `push-main.sh:561,590`, `lib/pyrun.sh:30` | ~1,000–1,300 python starts | 1,000–1,800 pool | new |
| 6 | `runleg`: `EPOCHREALTIME` for `$(date +%s%N)` (`:2369`, `:2408`); `{ out=$(<…); } 2>/dev/null` (`:2407`); `printf -v secs` (`:2409`); `ts_now` → `EPOCHSECONDS` (`:1059`, 11 uses incl. the heartbeat `:1060` and wait loop `:1147`) | `tools/run-gates/run-gates.sh` | 7 per leg × (126 + ~600–1,200 legs run by runner suites) ≈ 5k–9k | 500–2,700 pool | lever 6 |
| 7 | Runner git memo: one `git rev-parse --show-toplevel --git-dir --git-common-dir` + one `rev-parse -q --verify HEAD` + one `hash-object`, cached in globals | `run-gates.sh:98,243,1044,1484,2166,2172,2189,3420,3845` | ~10 per run × ~400 runs ≈ 4,000 | 400–1,200 | lever 6 |
| 8 | Hygiene selector counts: one `awk` over `$FILES` for the six PRE_* counts and the other `printf "$FILES" \| grep -c` populations | `check-memory-hygiene.sh:461-485,586-588,668,737-739` | ~30–60 per run × ~100 runs ≈ 3k–6k | 300–1,800 | lever 11 (`--only` cuts the run count first) |
| 9 | Timeout capability probe: lazy in the bounded-runner path, or inherited `GOV_TIMEOUT_K_LIVE` (R8) | `unattended.sh:165`, `check-unattended.sh:1186`, `run-gates.sh:703`, `lib-unattended.sh:1267` | 2 × (1,450 + 450 + 400) ≈ 4,600 | 460–1,400 | new |
| 10 | `build_commit` range memo (`lib-unattended.sh:1084`, rev-list loop `:1127`), consumed per id | `check-pass-order.sh:375`, `check-brief-recorded.sh:393` | ~2,900 per bar → ~60 | 290–870, plus their self-tests | lever 14 |
| 11 | `baseline_units`: drop the `cat \|` (`:1942`), run `extract_run_facts` ONCE per blob, read `base:` and `phase:` with one `case` loop | `lib-unattended.sh:1942-1950`; called per record at `check-unattended.sh:3787` and `unattended.sh:4320,12234` | ~7 per commit × 82 records × 3–10 commits ≈ 1,700–5,700 per bar | 170–1,700 | lever 9 |
| 12 | `$(cat <<'RKD')` → `read -r -d ''` in the canonical `resolve_kit_dir` (R4), re-rendered into its 47 copies | `lib-unattended.sh:133`, `run-gates.sh:145`, `check-wiring.sh:399`, `manifest-check.sh:678`, … | 2 per `resolve_kit_dir` call, ~1,000–2,000 calls | 100–600 | new |
| 13 | Asks: one `awk` over `AW_ROWS` into assoc arrays; `ask_field`/`ask_sort_key`/`ask_sev_rank` become pure lookups; the O(n²) selection sort runs in bash | `unattended.sh:4164,4196-4235`; per-ask loop `:11023` (113 body sites) | n² × ~12 per plan, e.g. 600 at n = 10 | 50–300 (frequency unmeasured) | new |
| 14 | `check-playbook.sh`: `declared_scalar`/`declared_list`/`_conf_key` via R1, and the per-playbook body parsed once | `check-playbook.sh:343,393` (100 body sites) | ~50–100 per playbook | 50–150 | appendix "fork-free readers in check-playbook" |
| 15 | Suites: fixture identity and `core.autocrlf` through the environment (R9); `git init` from a template + `cp -r` | 232 config + 234 init sites, led by `check-memory-hygiene.test.sh`, `pre-push.test.sh`, `run-gates.test.sh`, `check-wiring.test.sh` | 2–4 per fixture × ~1,000+ fixtures ≈ 2k–6k | 200–1,800 | lever 10 |

Two small edits that fall just outside the top 15:
- `unattended.sh:2753,5716,5920,6940`, the newline tests via `| wc -l`, which R10 makes one `[[ … ]]`;
- `manifest-check.sh:269` `getval`, 6 P per call: `printf|sed|head|sed` becomes one bash loop over
  `$BLOCK` with R1.

## 6. Order, and what this pass did not establish

1. Land the gate first, with the three zero-FP bans (`epoch-date`, `cat-heredoc`, `redirected-read`)
   and the counter arm on two entrypoints, the driver prelude and `run-gates.sh` 1-leg. Every later edit
   then shows up as a falling ceiling instead of a claimed saving.
2. Edits 1, 2, 3, 6 and 9 are mechanical and touch only preludes and readers. They are the largest
   shares.
3. Edits 4, 10 and 11 together through `lib-unattended.sh`, under one kit bump. (Memory:
   "Bump kit versions once, after the last move".)
4. Edits 5 and 12 change byte-identical gated copies: one canonical edit, re-render, parity suite.

Not established:
- No bash 5.2 was available to measure whether `$(<f)` forks there. WSL on this machine is 5.3.9.
- The invocation multiplicities are the aMeteredSweep appendices' static figures, not traced.
- `pure-fn-subst` excluded no function for `cd`/`exit`/`trap` side effects, so each R1 conversion still
  needs a read of the callee.
- The per-verb `fact` read counts (5–15 per driver call) are a guess.
- The counter's lower-bound gap was observed on one specimen only.
