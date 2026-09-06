# TOOL-aQuenchedHarness-5 — a self-test harness whose unit of cost is not a process

**Status:** OPEN · rev-1 · 2026-09-06 · node a · Tier-2 · base faaea5f5 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-06-prompt-TOOL-aQuenchedHarness-1.md](../prompts/2026-09-06-prompt-TOOL-aQuenchedHarness-1.md) | research | TOOL-aQuenchedHarness-1 TOOL-aQuenchedHarness-3 |

<!-- /gen:spec-records -->

## 1. Goal

Build the shared harness the self-test suites are rebuilt onto, so an arm stops costing a fistful of
process creations. On node `a` a bare `/usr/bin/true` measures 319 ms and `python -c pass` 773 ms, so
a suite that forks per arm is paying the operating system and not the check — which is exactly what
`memory/gotchas/process-creation-is-the-suite-cost.md` records, measured independently on node `d`.

## 2. Scope (IN)

- **S1** — `tools/lib/lib-selftest.sh`, a sourced library giving three verbs: `fixture_once` (build
  the scratch subject ONE time per suite and snapshot it), `arm` (stage a break into a cheap copy of
  that snapshot, run the subject, compare), and `arms_report` (the verdict line with its own arm
  count, derived and never typed).
- **S2** — restoring a fixture between arms is a COPY of a snapshot directory, never a fresh
  `git init` plus a re-populate. Where an arm needs git history, the snapshot is created once and
  restored by copying the `.git` directory with it.
- **S3** — a bounded worker pool inside `arms_report`, width read from the same
  `tools/run-gates/gate-profiles.txt` row the bar reads, so parallelism is declared in one place.
  Serial (`width 1`) is the documented rollback and the same code path.
- **S4** — a per-ARM timeout, so one wedged arm reds itself by name instead of hanging the suite and
  charging the whole cost to a leg-level ceiling. It goes through a file-captured, kill-after path
  for the reason `memory/gotchas/bounded-through-a-pipe-is-unbounded.md` states.
- **S5** — DETERMINISTIC REPORTING under concurrency: arms execute in whatever order the pool
  chooses, output is rendered in declaration order. A suite whose output moves with the width is a
  suite whose byte-pins cannot be trusted.
- **S6** — a spawn COUNTER the harness can be asked for, so a suite's cost is attributable to a
  number rather than to a stopwatch. This is what makes a later regression arguable instead of
  merely annoying.
- **S7** — a self-test for the harness itself: a fixture whose arm always fails, one that always
  passes, one that wedges past the arm timeout, and a run at width 1 and width N producing
  byte-identical output.

## 3. Non-goals (OUT)

- Not porting any suite. That is `TOOL-aQuenchedHarness-6`, and keeping them separate is what lets
  the harness be reviewed before six suites depend on it.
- Not rewriting shell checkers in Python. The subject under test is frequently a shell script, so an
  in-process arm would test a re-implementation rather than the shipped checker — the
  `second-implementation-is-not-a-second-opinion` class.
- Not a test framework. No discovery, no fixtures-by-convention, no assertions library. Three verbs.
- Not changing any suite's arm inventory. Arms are preserved exactly; only their execution moves.

## 4. Design

### The cost model, stated because everything here follows from it

A suite's wall clock is approximately `spawns x per-spawn-cost`. Per-spawn cost is a property of the
node and this repo cannot lower it. Spawn count is the only term this repo owns, and
`tools/unattended/run-unattended-gates.sh` records the one prior instance of lowering it: 469 spawns
per invocation became 220 by reading each file once instead of running a `grep` per (item, file).
This harness attacks the OTHER multiplier — the per-arm fixture construction, which is where a suite
with 200 arms pays 200 `git init`s.

### Data model

A suite declares its subject and its fixture builder once. The harness builds the fixture, snapshots
it to a directory under one `mktemp -d`, and every arm restores by copying that snapshot. Copy cost
is filesystem work, not process creation, and it is one spawn where the current pattern is many.

### Inventory

- `fixture_once` · `arm` · `arms_report` — the three verbs, in `tools/lib/lib-selftest.sh`.
- `SELFTEST_WIDTH` — the resolved pool width, named for what it is; sourced from the profile row.
- `SELFTEST_ARM_TIMEOUT` — the per-arm bound.
- `selftest harness self-test` — the new leg's name in `tools/gate-legs.json`, held like every other.

### Files touched (estimate)

`tools/lib/lib-selftest.sh` (new) · `tools/lib/lib-selftest.test.sh` (new) · `tools/gate-legs.json` ·
`tools/lib/` has no `kit.toml` of its own today, so the leg is declared where the resolver's is.

### Alternatives rejected

Recorded per candidate under §8 F1, with the test that rejected it, because a rejected candidate with
no recorded test is indistinguishable from one nobody tried.

## 5. Production-readiness checklist

- security — the harness writes only under its own `mktemp -d`; the scratch-guard hook already
  governs where a session may write and is not weakened.
- perf / scale — this unit IS the perf work. Its own budget is that the harness self-test costs less
  than the suite it replaces, measured.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — an arm that wedges, an arm whose fixture fails to build, and a
  suite that declares no arms are three distinct reports. The last is a refusal: a suite that ran
  nothing must not print a green line.
- observability — the spawn counter and the arm count, both derived and printed.
- risks — CONCURRENCY IS THE HAZARD. Arms that share a fixture directory would interfere; S2's
  copy-per-arm is what makes them independent, and S7's width-1-versus-width-N byte comparison is
  what proves it rather than asserting it.
- testing + left-shift gates — S7, and every ported suite in unit 6 is a further exercise of it.
- migration / rollback — a suite not yet ported is untouched; the library is additive until something
  sources it.
- user docs — the library header, and one line in `AGENTS.md` naming where a new self-test goes.

## 6. Acceptance criteria

- **AC1** — When `bash tools/lib/lib-selftest.test.sh` runs at width 1 and at the profile width, the two
  outputs are byte-identical, proving reporting order is independent of execution order.
- **AC2** — When an arm sleeps past `SELFTEST_ARM_TIMEOUT`, that arm alone reds by name and the suite
  completes, rather than the suite hanging.
- **AC3** — When a suite declares zero arms, `arms_report` exits non-zero saying it graded nothing.
- **AC4** — When the same arm set is executed through `tools/lib/lib-selftest.sh` and through a
  per-arm `git init` control in the same run, the harness's spawn count is lower by a factor the
  report states, measured rather than asserted.
- **AC5** — When an `arm`'s staged break is reverted, that arm reds in
  `tools/lib/lib-selftest.test.sh` — the harness's own failing case, observed before landing, per
  charter §7.

## 7. Gates

`bash tools/run-gates/run-gates.sh` · the new `selftest harness self-test` leg ·
`GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` at the Definition of Done, because this is kit
work · `bash tools/run-gates/run-selftests.sh` once `TOOL-aQuenchedHarness-4` has landed.

## 8. Open questions

- **F1 — FACT-QUESTION · which mechanism actually removes the cost?** Four candidates, differing in
  mechanism, to be tested against ONE real suite before the harness is written. The probe is a
  measurement over the existing tree, not an argument, and the liveness assertion is that a candidate
  showing no improvement must be recordable as such: the control is the unported suite, run in the
  same conditions.
  - **C1 — one fixture per suite instead of one per arm.** Loses if the ported suite's spawn count
    does not fall, which happens if fixture construction was never the multiplier.
  - **C2 — bounded intra-suite parallelism.** Loses if wall clock does not fall at width N against
    width 1 on the same arms, or if output ceases to be byte-stable.
  - **C3 — batching the subject invocation** so one checker process grades many staged subjects.
    Loses if the shipped checkers do not accept a multi-subject invocation, which is the likely
    outcome and must be RECORDED rather than assumed.
  - **C4 — moving arms in-process by rewriting suites in Python.** Loses on the
    `second-implementation-is-not-a-second-opinion` class wherever the subject is a shell script,
    which is most of them; and it is the only candidate that changes what is being tested.
  Resolution happens in the build's TESTING position, and §4's `### Alternatives rejected` records
  the test that rejected each loser.
- **F2 — does the harness ship to adopters?** RESOLVED (agent, 2026-09-06, delegated): it ships as
  part of whichever kit carries it, exactly as the suites do, and — by `TOOL-aQuenchedHarness-3` —
  no leg that uses it reaches an adopter's bar. The file travelling and the leg not running is the
  same disposition unit 3 already took.

## 9. Revision log

- rev-1 · 2026-09-06 · initial draft.

## 10. Reuse audit

No existing seam fits, and that is the finding rather than a failure to look. The reuse probe
returned `run` and `check` as high-fan-in name stems across thirteen `selftest.py` modules and
`tools/codebase-map/rank_harness.py`'s `run_constant_control`, none of which is a shared harness:
every suite in this tree builds its own scratch subject inline, which is precisely the duplication
this unit removes. The closest prior art is `tools/unattended/run-unattended-gates.sh`, which shares
the BUDGET discipline but runs whole suites rather than arms, and is `TOOL-aQuenchedHarness-4`'s seam
rather than this one's. Because no seam fits, `memory/guides/BUILD-METHOD.md` M12 governs: §8 F1
carries the candidate set and the test that decides it, and the losers' tests land in §4.

Recall terms used: `selftest gate leg ceiling guard GATE_SELFTESTS run-gates scratch repo mktemp
spawn wall-clock adopter kit.toml`
