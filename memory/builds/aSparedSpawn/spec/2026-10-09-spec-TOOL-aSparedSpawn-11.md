# TOOL-aSparedSpawn-11 — per-suite levers: five suites stop paying a process for a question they ask once

**Status:** OPEN · rev-1 · 2026-10-09 · node a · Tier-2 · base 22efab65 · streams tooling · order 2

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Five suites each spend most of their time re-creating something they could create once: a `node`
process per file, a whole drift report per signal, a 78 MB scratch tree per arm, a `rev-list` per
unit id over a range every id shares, and a real `claude --version` per card write. Round one priced
them at about 4-5 ks of pool time together on node `a`
(`memory/builds/aMeteredSweep/build/2026-10-09-build-TOOL-aMeteredSweep-1-research2-menu.md`, B7). Each
is one scope item with its own criterion, so any one can land or be cut alone.

## 2. Scope (IN)

- **S1** — The no-regress property arm of `tools/hooks/agent-cap.test.sh` (`:2039-2149`) runs both
  hooks in ONE `node` process. Its embedded Python loop starting `node` per population file becomes a
  node runner that compiles each hook once and runs each payload in a fresh context, by the mechanism
  F1 resolves. The population (every `git ls-files` path plus the `nrfix` fixtures), the class-scoped
  ratification re-run on the stripped `gov:sequential-agents` marker, admission as `exit != 2`, and the
  red on zero ratifications are unchanged. Observed by AC1 and AC3.
- **S2** — A parity sub-arm grades a deterministic sample through both the in-process runner and real
  `node` spawns: every `nrfix` fixture, plus population files picked by a fixed stride over the sorted
  path list. Any disagreement reds naming the payload. Observed by AC2.
- **S3** — In `tools/drift-audit/selftest.py`, an arm that reads one signal calls that signal's
  function in-process over a context built by the suite's own `_build_run_ctx` (`:3284`), widened to
  what that signal reads. The name-to-function map is derived once from one full `report()` over a
  clean fixture, never typed. A handful of `report()` arms grading `main`'s own contract (pins,
  baselines, offline mode, refusals) stay out of process. Observed by AC4 and AC5.
- **S4** — `tools/check-hook-destinations.test.sh` builds `scratch()` once per run, records its
  fixture commit, and starts each arm from `git reset -q --hard <fixture>` plus `git clean -qfdx` in
  that one tree. Its two per-repo `git config` calls ride with this change. Observed by AC6.
- **S5** — `build_commit` in `tools/unattended/lib-unattended.sh` (`:1084`) memoises its `rev-list`
  per (range, order, max-count) in caller-declared globals, opt-in exactly as the `_SUBJ` cache is
  (`:1124`), and also leaves its answer in a global. The callers in
  `tools/unattended/check-pass-order.sh` and `tools/unattended/check-brief-recorded.sh` declare the
  memo and read the global without a `$(…)`, because a memo written inside a command substitution dies
  with the subshell. The driver's call at `tools/unattended/unattended.sh:11182` declares nothing and
  behaves as today. Observed by AC7 and AC8.
- **S6** — `skills/session-kickoff/manifest-check.test.sh` unsets `AI_AGENT` after its prologue, so a
  card write outside the `cli —` block reads no session version and starts no real `claude`. The block's
  own save and restore (`:970`, `:1014`) keeps working. Observed by AC9.
- **S7** — Each suite's seconds are recorded before and after, quiet, with the instrument. Observed
  by AC10.

## 3. Non-goals (OUT)

- Agent-cap's Workflow-payload arms through one harness, its `--print-cap`, env and rule-4 concurrency
  arms (round one's levers 6 and 2 there). They test process and filesystem behaviour on purpose.
- A `--signal NAME` flag on `drift_report.py`. It keeps arms out of process and saves less than S3.
- Hook destinations' per-fragment process trio and its two govkit-importing pythons (govkit lever 9).
- `build_commit`'s per-README `cat-file --batch` (govkit lever 3's second half) and `read_landing_commit`.
- The manifest-check card fixture's sparse clone, and its causal wall-clock arms.

### Edges

none

## 4. Design

### S1 — two hooks, one node

`tools/hooks/agent-cap.js` reads stdin only through `require('fs').readFileSync(0, 'utf8')` (`:99`) and
ends each path in `process.exit`. It also reads the filesystem (`gitCommonDir`, slot files) and
`process.env`, so the runner's context gets the REAL `require`, with an `fs` proxy whose
`readFileSync(0)` returns the payload and every other call passes through. `process.exit(code)` records
the first code and throws a sentinel the runner catches; an uncaught throw maps to 1, as real node
does. The runner keeps the Python loop's cwd and environment. Round one: about 3727 node spawns in this
one arm, about 88 % of the leg, 717 s serial (other-legs report, "agent-cap self-test").

### S3 — one signal per arm

`report()` (`:411`) starts `drift_report.py --json`, which computes every entry of `SIGNALS`
(`tools/drift-audit/drift_report.py:3518`) in `main` (`:4294-4296`). Round one found 51 call sites
subscripting one signal, 16 of them one signal alone. `main` adds `pin`, and for baselined signals
`baseline`, `new` and `stale`, after the signal returns, so the in-process comparison in AC4 covers the
fields the function returns and an arm reading the post-processed fields stays on `report()`. A
signal reading `ctx.signal_names` is handed the derived name set.

### S4 — one scratch

`scratch()` (`:128-137`) extracts `git archive HEAD` (round one: 3633 files, 78 MB) and commits it.
Arms commit into it (`:163`, `:175`, `:203`, `:214`, `:220`, `:233`), so reset targets the recorded
fixture commit, never `HEAD`. Arm 1 grades the shipped tree before any scratch exists and is unchanged.
An arm that writes outside the work tree's tracked set is caught by `git clean -qfdx`; one that writes
into `.git` is not, and each arm is read for that before the change.

### S5 — the memo and its key

The range string carries symbolic `HEAD` in both checkers, and HEAD does not move during a check. The
driver can commit between two calls, which is why its call site does not opt in. The memo key is the
whole argument tuple that reaches `rev-list`.

### Inventory

| identifier | kind | cell that grades it |
|---|---|---|
| the S1 runner file written by the suite | node script, heredoc | `lexicon naming predicates` if tracked; it is not |
| `one_signal` or the name `--suggest` returns | Python function in a suite | `lexicon naming predicates`, python cell |
| `_BC_OUT`, `_BC_MEMO` | shell globals, the second an associative array | none |

### Files touched (estimate)

- `tools/hooks/agent-cap.test.sh`
- `tools/drift-audit/selftest.py`
- `tools/check-hook-destinations.test.sh`
- `tools/unattended/lib-unattended.sh`, `tools/unattended/check-pass-order.sh`,
  `tools/unattended/check-brief-recorded.sh`, `tools/unattended/check-unattended.test.sh`
- `skills/session-kickoff/manifest-check.test.sh`

### Alternatives rejected

- **A full `agent-cap.test.js` rebuild** (round one's (e)). One to two days for the rest of the arms,
  which test process behaviour on purpose.
- **A hand-typed signal-name map.** Two answers to a question `report()` already answers.
- **Hoisting `rev-list` into each caller.** Two copies of the cap and order rules `build_commit` owns.
- **Archiving only the paths the hook-destinations gate reads.** Arm 1's control then grades a tree
  the gate never sees in production.

## 5. Production-readiness checklist

- security — No product surface changes except `build_commit`, whose answers are unchanged.
- perf / scale — Round one's estimates: S1 ~550 s serial, S3 ~100 s quiet, S4 160-400 s quiet,
  S5 ~380 s and ~290 s primary, S6 55-165 s quiet.
- error / empty / loading states — S1 keeps the empty-population and zero-ratification reds.
- observability — S1's summary line and S2's disagreement list print on every run.
- risks — An in-process path diverging from real node (S2 guards it); module state across drift
  fixtures; an arm leaving state in `.git` that a reset keeps.
- testing — AC1 to AC9 each stage the break that would turn its criterion red.
- migration — Kit versions bump once after the last move; `lib-unattended.sh` owes the unattended kit.
- user docs — N/A — suite and checker internals only.

## 6. Acceptance criteria

- **AC1** — When the no-regress arm runs after the pass, its summary line
  `population <n> scanned, <d> denied at BASE` reports the same n and d as at base 22efab65 on the same
  tree, and `node` is started once for the property rather than per file.
  Red when: n or d differ, or a trace of the arm shows one `node` exec per population file.
  permission: kit suites are the owner's manual run of the merged tree (owner ruling, 2026-10-06).
- **AC2** — When the runner's `process.exit` stub is staged to drop its code in a scratch copy of the
  agent-cap suite, the parity sub-arm reds naming a disagreeing payload.
  Red when: the staged break passes, which means the sample never reaches a deny path.
- **AC3** — When the `gov:sequential-agents` strip is staged to a no-op in a scratch copy, the
  no-regress arm reds on zero ratifications, as TOOL-dFoldedVerdict-4's AC14 observed for the Python
  loop.
  Red when: the arm passes with the strip disabled.
- **AC4** — When every signal in the derived map is called through `_build_run_ctx` on a violating
  and a clean fixture, each record equals that signal's `report()` record on the same fixture, over
  the fields the signal function returns.
  Red when: any signal differs, or the derived map is empty.
- **AC5** — When `git grep -nE` for a literal list of signal names runs over
  the drift-audit selftest source, it finds none outside arms that assert one signal by name, and
  `CHECK_FLOOR` still holds.
  Red when: a hand-typed name map exists, or the executed count falls below `CHECK_FLOOR`.
- **AC6** — When the hook-destinations suite runs, `git archive` runs once, every arm's verdict
  equals the base's, and with the per-arm reset staged out in a scratch copy a later arm reds.
  Red when: the staged break passes, which means no arm depends on a clean start and the reset is
  unobserved; or `FLOOR_ASSERTIONS` is not met.
- **AC7** — When `build_commit` is called twice for one range in one shell with `_BC_MEMO` declared and
  `GIT` shadowed by a counting function, `rev-list` runs once and both calls answer what an
  undeclared call answers; with no memo declared it runs twice.
  Red when: the second declared call re-runs `rev-list`, or any answer differs.
- **AC8** — When `bash tools/unattended/check-pass-order.sh` and
  `bash tools/unattended/check-brief-recorded.sh` run at base and after the pass on the same tree,
  their output is identical, including the units-graded and unbuilt-in-range lines.
  Red when: any line differs.
  cost: round one measured 576 s and 490 s primary before; both legs, twice.
- **AC9** — When the manifest-check suite runs with a stub `claude` first on `PATH` that appends to a
  log, the log holds only calls made inside the `cli —` block.
  Red when: a card write outside that block records a call, which means `AI_AGENT` still leaks in.
- **AC10** — When each touched suite and the two checkers, `check-pass-order.sh` and
  `check-brief-recorded.sh`, run once at base and once after, quiet, on a frozen clone, the seconds
  are recorded with the instrument in the build folder, and each after figure is lower.
  Red when: a figure is not lower.
  figure: DERIVED at observation; round one's figures in §5 are estimates, not targets.

## 7. Gates

`agent-cap self-test` · `drift-audit selftest` · `hook destinations self-test` · `lexicon naming predicates` ·
`manifest-check self-test` · `review-join self-test` · `scratch-guard self-test` ·
`verifier fan-out self-test` · `pass-order history` · `brief-recorded` · `unattended kit gate` ·
`kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` ·
`harness arms (fail branches armed or pinned)` · `codebase-map coverage + freshness` ·
`testsuite counts (every bar self-test prints one)` · `memory hygiene` ·
`spec tokens (a spec's own names resolve)`

New arm: tools/hooks/agent-cap.test.sh · covers AC2 · the runner's exit stub staged to drop its code · none
New arm: tools/drift-audit/selftest.py · covers AC4 · one signal's in-process context missing an attribute it reads · CHECK_FLOOR rises by the arms added
New arm: tools/unattended/check-unattended.test.sh · covers AC7 · the memo key staged to omit the range · none
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC9 · the unset staged out with a logging stub claude on PATH · FLOOR_ASSERTIONS rises by one

## 8. Open questions

- **F1 — How the no-regress property runs the hooks in one process.**
  - (a) `vm.Script`, compiled once per hook, a fresh context per payload; round one estimated about 5 s
    for the population.
  - (b) `worker_threads`, one worker per payload with `fs.readFileSync` patched in the worker; keeps
    real `process.exit` semantics, about 20-40 ms per payload, round one's ~110 s.
  - Recommendation: (a), with S2's parity sample as the guard against the divergence (a) risks.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.

## 10. Reuse audit

The probe `tools/codebase-map/reuse_lookup.py "memoise a rev-list range per build commit"` ranks
`build_commit` (`tools/unattended/lib-unattended.sh`, fan-in 7, SEAM), the function S5 extends in
place. For S1 and S3, "run a hook in one node process over many payloads" and "build a run context for
one drift signal" ranked only name-stem hits (`run`, `run_arms`, `build`); the seams reused are the
suite's own `_build_run_ctx` and `report()`, named from the file.

Recall terms used: agent-cap no-regress BASE hook population ratification build_commit _SUBJ cache
drift-audit _build_run_ctx scratch AI_AGENT
