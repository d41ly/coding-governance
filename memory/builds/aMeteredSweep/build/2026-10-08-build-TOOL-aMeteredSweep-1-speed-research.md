# How the bar and its slow legs reach their goals faster — the ranked synthesis

**Serves:** research TOOL-aMeteredSweep-1

Node `a`, 2026-10-08. The subject is one profiled bar: `fa68a767` (local `main` reconciled with
`origin/main`), `GATE_FULL=1 GATE_SELFTESTS=1`, width 8, from a frozen clone, beside another
repository's bar with used memory at 94 to 96 percent. Its rows are
`2026-10-08-build-TOOL-aMeteredSweep-1-legs.tsv`, made by the `-legtable.py` beside it. Five
read-only research passes, one per cluster, are the `-research-*.md` appendices; they ran nothing, so
every saving below is an ESTIMATE from spawn counts and a list-scheduling simulation over the measured
durations, good to about a factor of two. A saving is quoted on THIS bar unless it says "quiet".

## What the bar cost, and why

- Wall 13,324 s. The pool spent 54,049 leg-seconds, an effective concurrency of about 4 at width 8.
- **Contention, not work.** The nine legs that outran a ceiling ran 3 to 5 times faster on their
  serial retry: memory-hygiene self-test 4801 s in the pool against 1442 s alone, check-wiring 2322
  against 601, pre-push 1786 against 402, run-log line 1201 against 175. The 9 killed attempts cost
  14,217 leg-seconds, 26 percent of the pool's work, and their serial retries another 4050 s, 30
  percent of the wall.
- **The unit of cost is a process.** A spawn measured 0.09 to 0.3 s quiet and 1 to 2 s loaded here; a
  bare `$(:)` fork 89 to 210 ms; a `python` start 0.9 s. Every suite that is slow is slow by spawn
  count, and the repo has recorded this class since 2026-08-23
  (`memory/gotchas/process-creation-is-the-suite-cost.md`).
- **Order.** The clone had no ledger, so legs dispatched in manifest order and the floor leg, the
  `run-gates canary`, started 3445 s in. The profiler called the bar floor-bound at 5769 s; the
  runner pass shows the retries and the order set this run's wall, not the floor.
- **Memory.** Dispatch was held 872 s in three pauses at 94 to 96 percent used.

## The levers, ranked by seconds on this bar

| # | lever | where | est. saved | effort | risk |
|---:|---|---|---:|---|---|
| 1 | Retry a ceiling-killed leg in the pool's drain tail, not serially after the drain | `run-gates.sh` `run_leg_retry` | ~3300 | S-M | low-med |
| 2 | Longest-first with no ledger: dispatch by declared ceiling or the tracked `ceiling-evidence.txt` | one expression in the dispatch-order reader | ~1900 | S | very low |
| 3 | Width from a measured per-host calibration (expect about 4 here), narrowing on spawn pressure as the memory pause narrows on memory | `gate-profiles.txt` and the runner | 2000-5000, conditional | M | med |
| 4 | Run the self-test tier on a host whose spawns are cheap, or as its own tier | procedure | tier is 46,408 of 54,049 leg-s; the push bar here is ~1700 s | S | low |
| 5 | Reuse a leg's verdict keyed on its declared inputs, shared through the common dir; drop `BASE` from the key | runner reuse unit | 25,014 leg-s against a green parent; a records-only commit's bar ~3937 s | M | med |
| 6 | Cut the runner's own spawns: about 45 to 65 per leg down to about 6, and 6 or 7 `rev-parse` per bar down to 1 | `runleg`, `report_one`, the header | direct ~150; the canary family drives the runner 270 times, ~1270 + ~910 quiet there | M | low-med |
| 7 | `foreign-prefix parity` probes one shard per sharded suite, and runs its whole-run rows inside the pool under a hang bound | `foreign-prefix.gov.test.sh` | ~1500 + ~900 | S | low |
| 8 | Unattended driver: out-variable readers for 190 `$(fact …)` and 103 `$(printf …)` sites, and a lazy preamble for verbs that read no index | `unattended.sh`, `lib-unattended.sh` | 2000-4000 pool across the eight held shards | M | med |
| 9 | Unattended kit gate: parse every run-facts block once, memoise `read_landing_commit`, one `cat-file --batch` | `check-unattended.sh` | ~1500 → 300-500 quiet | M | med |
| 10 | `govkit selftest` in shards, then an import shim, then an in-process harness; `blob_at` through one `cat-file --batch` | `selftest.py`, `govkit.py:6123` | wall 3775 → ~1000-1200 | M | low-med |
| 11 | `memory-hygiene self-test`: a `--only N` selector that prints the checks it ran, and the delegates stop re-entering the checker | `check-memory-hygiene.sh` | ~270 quiet, ~1500 pool | M | med |
| 12 | `agent-cap self-test`: the no-regress property in one `node` process, not 3727 | `agent-cap.test.sh:2041-2149` | ~550 quiet, ~1400 pool | M | med |
| 13 | `drift-audit selftest`: one signal per arm through its own `_build_run_ctx`, not 93 whole reports | drift-audit suite | ~100 quiet, ~1200 pool | M | med |
| 14 | `pass-order history` and `brief-recorded`: memoise `build_commit`'s range; batch README reads | `lib-unattended.sh:1084` | ~650 quiet, ~1200 pool | S | low |
| 15 | `run-gates canary`: clamp and profile-line arms through `--print-profile`, shorter control sleeps, then four shards cut by measured section cost | `run-gates.test.sh` | ~650 quiet, then the floor 5769 → ~1500 | S-M | low |
| 16 | `hook destinations self-test`: build its 78 MB scratch once, not nine times | `check-hook-destinations.test.sh:128` | ~300 → 40-60 quiet | S | low |
| 17 | `manifest-check self-test`: `unset AI_AGENT` so a card write stops running the real `claude --version` | the suite's prologue | 55-165 quiet | XS | low |
| 18 | Node and python harnesses fed many cases by one process: unattended-build, gate-guard, scratch-guard, spec-tokens | each suite | 100-170 each | M | low-med |

**One action outranks every code lever and is not a code change.** A Windows Defender real-time
exclusion for the repository, its worktrees and `%TEMP%`. aGradedDoorway measured this node's spawn
at 6.4 to 13 times node `d`'s and named the scanner the largest single factor. It is a security
setting, so it is the owner's decision; nothing in this build makes it.

## Full rebuilds — what each would buy

- **The runner in Python, or a persistent worker:** not recommended. Every large saving above is
  reachable in bash, and the direct spawn saving is at most about 150 s; the risk is the whole merge bar.
- **A host-wide slot pool (a jobserver)** shared by nested and foreign bars: `foreign-prefix parity`
  opens an 8-wide pool inside the 8-wide bar, and the turnstile serialises one repository only, so two
  repositories' bars stacked here. The saving is unmeasured and large on a contended day.
- **The unattended driver's hot paths in Python:** the fork-free readers of lever 8 reach most of it
  in bash; a rewrite is warranted only if a traced leg run shows the parse of the 13k-line driver
  (0.75 s per call, about 1450 calls a suite) dominating after them.
- **govkit's selftest as an in-process harness:** the third step of lever 10, after sharding and the
  shim, about 360 s quiet on top; `main` returns an int and has two `sys.exit` sites.
- **Per-arm fixtures from one template** (`cp -a` of a repository built once, `git fast-import`
  for history, git identity and `core.autocrlf` from the environment rather than per-repo config):
  a cross-cutting rebuild of every suite's fixture helper, 10 to 30 percent of each small suite.

## Arms whose verdict reads a clock — red on a loaded host

This build fixed four: the memory-pause AC6 and AC14 arms of the canary, and manifest-check's claims
arms and its AC5. The research found more, each with its line in the appendices: the agent-cap
10 s quadratic budget (`agent-cap.test.sh:2165`), the turnstile refresher and R6, the evidence
suite's tree-move window, `unattended.test.sh:7822-7837`, short polls in `resume-tick.test.sh`,
govkit's 30 s lock wait, and `foreign-prefix parity`'s quiet-measured row budgets. The fix that
held here is to order on a leg's row rather than on a sleep, and where one clock must remain, to
give it a margin larger than one leg's own bookkeeping on this node, which passed 6 s under load.

## What this build already took

`--claims` went from 66 s to 18 s under the same load (lever 8's first instance): `normpath` stopped
forking `sed`, its hot callers stopped capturing it through `$(…)`, and the generated-index resolver
reads every descriptor in one `awk`. The other appendix claims superseded here: the gotchas
`--for-paths` arm at a foreign prefix was a hardcoded `tools` path, fixed; the three reds the
remaining-legs pass lists as edits in flight are fixed.

## The order to build them in

1. Measure width 4, 6 and 8 on this node, quiet and loaded. Every run record retained is width 8.
2. Levers 1 and 2: the retry in the tail and the ceiling prior. One unit each, small.
3. Lever 6, then the canary's cheap arms (15), so the floor leg shrinks before it is sharded.
4. Levers 7, 14, 16 and 17: small, low risk, about 3000 s of pool work between them.
5. Levers 8 and 9 together, through `lib-unattended.sh`, under one kit bump.
6. Lever 5, reuse keyed on inputs, once the cheaper wins have moved the floor.
