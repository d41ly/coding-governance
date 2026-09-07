# TOOL-aQuenchedHarness-5 — a self-test harness whose unit of cost is not a process

**Status:** CLOSED · rev-5 · 2026-09-07 · node a · Tier-2 · base faaea5f5 · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-07-build-TOOL-aQuenchedHarness-5-acceptance-ledger-spawn-cheap-harness.md](../build/2026-09-07-build-TOOL-aQuenchedHarness-5-acceptance-ledger-spawn-cheap-harness.md) | journal | — |
| [2026-09-07-build-TOOL-aQuenchedHarness-5-candidate-test.md](../build/2026-09-07-build-TOOL-aQuenchedHarness-5-candidate-test.md) | research | — |
| [2026-09-06-prompt-TOOL-aQuenchedHarness-1.md](../prompts/2026-09-06-prompt-TOOL-aQuenchedHarness-1.md) | research | TOOL-aQuenchedHarness-1 TOOL-aQuenchedHarness-3 |
| [2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round1.md](../reviews/2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round1.md) | spec-audit | TOOL-aQuenchedHarness-1 TOOL-aQuenchedHarness-2 TOOL-aQuenchedHarness-3 TOOL-aQuenchedHarness-4 TOOL-aQuenchedHarness-6 TOOL-aQuenchedHarness-7 |
| [2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round2.md](../reviews/2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round2.md) | spec-audit | TOOL-aQuenchedHarness-1 TOOL-aQuenchedHarness-2 TOOL-aQuenchedHarness-3 TOOL-aQuenchedHarness-4 TOOL-aQuenchedHarness-6 TOOL-aQuenchedHarness-7 TOOL-aQuenchedHarness-8 |

<!-- /gen:spec-records -->

## 1. Goal

Build the shared harness the self-test suites are rebuilt onto, so an arm stops costing a fistful of
process creations. On node `a` a bare `/usr/bin/true` measures 319 ms and `python -c pass` 773 ms, so
a suite that forks per arm is paying the operating system and not the check — which is what
`memory/gotchas/process-creation-is-the-suite-cost.md` records, measured independently on node `d`.

## 2. Scope (IN)

- **S1** — `tools/lib/lib-selftest.sh`, a sourced library giving three verbs, all three checked
  against the lexicon before they were written here: `build_fixture` (construct the scratch subject
  ONE time per suite and snapshot it), `arm` (stage a break into a cheap copy of that snapshot, run
  the subject, compare), and `run_arms` (execute the declared arms and render the verdict with its
  own derived count).
- **S2** — restoring a fixture between arms is a COPY of a snapshot directory, never a fresh
  `git init` plus a re-populate. Where an arm needs git history, the snapshot is created once and
  restored by copying the `.git` directory with it.
- **S3** — a bounded worker pool inside `run_arms`, whose width is read from the variable
  `TOOL-aQuenchedHarness-4` S8 exports, `SELFTEST_INNER_WIDTH`, and falls back to the profile row's
  width ONLY when no outer runner set it. Reading the profile width unconditionally is what would
  square the two pools. Serial (`width 1`) is the documented rollback and the same code path.
- **S4** — a per-ARM timeout, so one wedged arm reds itself by name instead of hanging the suite and
  charging the whole cost to a leg-level ceiling. It goes through a file-captured, kill-after path,
  for the reason `memory/gotchas/bounded-through-a-pipe-is-unbounded.md` states.
- **S5** — DETERMINISTIC REPORTING under concurrency: arms execute in whatever order the pool
  chooses, output is rendered in declaration order. A suite whose output moves with the width is a
  suite whose byte-pins cannot be trusted.
- **S6** — a spawn COUNTER the harness can be asked for, so a suite's cost is attributable to a
  number rather than to a stopwatch. This is what makes a later regression arguable instead of merely
  annoying.
- **S7** — a self-test for the harness itself: a fixture whose arm always fails, one that always
  passes, one that wedges past the arm timeout, and a run at width 1 and width N producing
  byte-identical output.
- **S8** — the harness is GOV-INTERNAL and stays that way. `tools/lib/` ships nothing —
  `tools/govkit/registry.toml` carries a permanent exemption saying so and `AGENTS.md` §12 says it in
  the charter's voice — and after `TOOL-aQuenchedHarness-3` rev-2 the suites that source it do not
  ship either. Nothing an adopter receives references this file.

## 3. Non-goals (OUT)

- Not porting any suite. That is `TOOL-aQuenchedHarness-6`, and keeping them separate is what lets
  the harness be reviewed before six suites depend on it.
- Not rewriting shell checkers in Python. The subject under test is frequently a shell script, so an
  in-process arm would test a re-implementation rather than the shipped checker — the
  `second-implementation-is-not-a-second-opinion` class.
- Not a test framework. No discovery, no fixtures-by-convention, no assertions library. Three verbs.
- Not changing any suite's arm inventory. Arms are preserved exactly; only their execution moves.
- Not shipping to adopters, and not inlining per kit either. S8 states why both are unnecessary now.

## 4. Design

### The cost model, stated because everything here follows from it

A suite's wall clock is approximately `spawns x per-spawn-cost`. Per-spawn cost is a property of the
node and this repo cannot lower it. Spawn count is the only term this repo owns, and
`tools/unattended/run-unattended-gates.sh` records the one prior instance of lowering it: 469 spawns
per invocation became 220 by reading each file once instead of running a `grep` per (item, file).
**And that is not the only prior instance, nor the largest.** The `check-pass-order.sh` rebuild,
landed in this build's own base at `4042505a` and `274aa39b`, took 10184 s to 510 s by one pass over
history into a subject cache — a bigger win than the 469-to-220 one, with the same method and the same
claim shape: byte-identical summary, spawn count as the evidence. Rev-2 called the earlier one "the
one prior instance", which was false at HEAD and in this build's own history. Both are inputs to
§8 F1's candidates C1 and C3.

This harness attacks the OTHER multiplier — the per-arm fixture construction, which is where a suite
with 200 arms pays 200 `git init`s.

### Data model

A suite declares its subject and its fixture builder once. The harness builds the fixture, snapshots
it to a directory under one `mktemp -d`, and every arm restores by copying that snapshot. Copy cost
is filesystem work, not process creation, and it is one spawn where the current pattern is many.

### Where it lives, and why that stopped being a problem

Rev-1 placed it in `tools/lib/` while `TOOL-aQuenchedHarness-3` rev-1 kept shipping the suites, which
would have handed adopters `*.test.sh` files sourcing a path their tree can never contain —
reproducing a failure `tools/run-gates/kit.toml`'s header records this repo already making once, where
the runner "sourced `tools/lib/`, which is gov-internal and never travels, and with that path absent
it exited 2 having run ZERO legs". Unit 3 rev-2 stops shipping the suites, so `tools/lib/` is now
exactly the right home and no inline-parity obligation is created.

### Inventory

- `build_fixture` · `arm` · `run_arms` — the three verbs, in `tools/lib/lib-selftest.sh`. Each was
  checked with `python tools/lexicon/lexicon.py --suggest <name> --as sh.function` before being
  written: `build_fixture` and `run_arms` lead with declared verbs; `arm` is itself a declared verb,
  used in its declared sense of making a dormant check live.
- `SELFTEST_INNER_WIDTH` — read, not declared, per S3; owned by `TOOL-aQuenchedHarness-4` S8.
- `SELFTEST_ARM_TIMEOUT` — the per-arm bound.
- `selftest harness self-test` — the new leg's name in `tools/gate-legs.json`, held like every other.

### Files touched (estimate)

`tools/lib/lib-selftest.sh` (new) · `tools/lib/lib-selftest.test.sh` (new) · `tools/gate-legs.json` ·
the descriptor that declares `tools/lib/resolve-python.sh`'s legs, for the new leg's row.

### Alternatives rejected

Recorded per candidate under §8 F1, with the test that rejected it, because a rejected candidate with
no recorded test is indistinguishable from one nobody tried.

## 5. Production-readiness checklist

- security — the harness writes only under its own `mktemp -d`; the scratch-guard hook already
  governs where a session may write and is not weakened.
- perf / scale — this unit IS the perf work. Its own budget is that the harness self-test costs less
  than the suite it replaces, measured. S3's width is bounded by the outer runner, so a sweep cannot
  square the pools.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — an arm that wedges, an arm whose fixture fails to build, and a
  suite that declares no arms are three distinct reports. The last is a refusal: a suite that ran
  nothing must not print a green line.
- observability — the spawn counter and the arm count, both derived and printed.
- risks — CONCURRENCY IS THE HAZARD, in two directions. Arms sharing a fixture directory would
  interfere; S2's copy-per-arm makes them independent and S7's width-1-versus-width-N byte comparison
  proves it. Nested pools would square the width; S3 reads the exported bound rather than the profile.
- testing + left-shift gates — S7, and every ported suite in unit 6 is a further exercise of it.
- migration / rollback — a suite not yet ported is untouched; the library is additive until something
  sources it.
- user docs — the library header, and one line in `AGENTS.md` naming where a new self-test goes.

## 6. Acceptance criteria

- **AC1** — When `bash tools/lib/lib-selftest.test.sh` runs at width 1 and at the profile width, the
  two outputs are byte-identical, proving reporting order is independent of execution order.
- **AC2** — When an arm sleeps past `SELFTEST_ARM_TIMEOUT`, that arm alone reds by name and the suite
  completes, rather than the suite hanging.
- **AC3** — When a suite declares zero arms, `run_arms` exits non-zero saying it graded nothing.
- **AC4** — When the same arm set is executed through `tools/lib/lib-selftest.sh` and through a
  per-arm `git init` control in the same run, the harness's spawn count is lower by a factor the
  report states, measured rather than asserted.
- **AC5** — When an `arm`'s staged break is reverted, that arm reds in
  `tools/lib/lib-selftest.test.sh` — the harness's own failing case, observed before landing, per
  charter §7.
- **AC6** — When `SELFTEST_INNER_WIDTH` is exported by an outer runner, `run_arms` uses that value
  and not the profile row's width, asserted by an arm that sets the two to different numbers.
- **AC7** — When the `lexicon naming predicates` leg runs over the new file, it is green, and unit 5's
  three verb names appear in no offender report.

## 7. Gates

`bash tools/run-gates/run-gates.sh` · the new `selftest harness self-test` leg · the
`lexicon naming predicates` leg, which guards on `tools/` and therefore grades this file on the
branch bar rather than only at the lander · `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` at
the Definition of Done · `bash tools/run-gates/run-selftests.sh` once `TOOL-aQuenchedHarness-4` has
landed.

## 8. Open questions

- **F1 — FACT-QUESTION · which mechanism actually removes the cost?** Four candidates, differing in
  mechanism, to be tested against ONE real suite before the harness is written. The probe is a
  measurement over the existing tree, and the liveness assertion is that a candidate showing no
  improvement must be recordable as such: the control is the unported suite, run in the same
  conditions.
  - **C1 — one fixture per suite instead of one per arm.** Loses if the ported suite's spawn count
    does not fall, which happens if fixture construction was never the multiplier.
  - **C2 — bounded intra-suite parallelism.** Loses if wall clock does not fall at width N against
    width 1 on the same arms, or if output ceases to be byte-stable. **NOT decided on a single-shot
    wall-clock reading**: this build's own research record measures the same leg varying 5.5x median
    and 47.1x worst across readings on this node, so one loaded stopwatch decides nothing. Take
    repeated readings at both widths and report S6's SPAWN COUNT beside the seconds, which is the
    figure `memory/gotchas/process-creation-is-the-suite-cost.md` names as the claim to write down.
  - **C3 — batching the subject invocation** so one checker process grades many staged subjects.
    Loses if the shipped checkers do not accept a multi-subject invocation, which is the likely
    outcome and must be RECORDED rather than assumed.
  - **C4 — moving arms in-process by rewriting suites in Python.** Loses on the
    `second-implementation-is-not-a-second-opinion` class wherever the subject is a shell script,
    which is most of them; and it is the only candidate that changes what is being tested.
  Resolution happens in the build's TESTING position, and §4's `### Alternatives rejected` records
  the test that rejected each loser.
- **F2 — does the harness ship to adopters?** RESOLVED (agent, 2026-09-06, delegated), REVISED at
  rev-2: no, and after `TOOL-aQuenchedHarness-3` rev-2 nothing that sources it ships either, so the
  question dissolves rather than being answered. Rev-1 answered "it ships as part of whichever kit
  carries it", and the audit established that no kit carries `tools/lib/` — `registry.toml` exempts
  the path with the words "it ships nothing: it is gov-internal".
- **F3 — is the inline-canon pattern prior art this unit should have used?** RESOLVED (agent,
  2026-09-06, delegated): it is prior art, it was missed at rev-1, and it is NOT adopted.
  `tools/lib/resolve-python.sh` is inlined into each shipping kit and joined by the
  `python resolver (behaviour + inline parity + idiom ban)` leg, which is the right answer for a
  file that must travel. This one does not travel, so inlining would create a parity obligation
  across ten kits to solve a problem F2 already removed.

## 9. Revision log

- rev-5 · 2026-09-07 · CLOSED, after the first real port measured the harness at 62 s against the 32 s of the suite it replaced and sent it back for the rewrite it needed. Declarations moved into arrays the arm subshell inherits, the capture is read with `read -d ""`, the substring test is a `case`, setup and subject share one `bash -c` under one `timeout`: eleven processes per arm down to three. `wait -n || wait` was collapsing the pool to a barrier per arm. `build_fixture` now resets the batch, a silent-wrongness defect found by reading rather than running. Seventeen arms green, including the shrink floor that moved in from the suites so eighteen ports need not carry eighteen copies of it.

- rev-1 · 2026-09-06 · initial draft.
- rev-4 · 2026-09-07 · M12 CANDIDATE TEST RUN, and it inverted §8 F1's framing. Traced
  `tools/check-line-length.test.sh`: 36 s, 18 arms, 31 python spawns in the outer script alone at
  773 ms each — and `bash -x` cannot see the subject's own 12 python call sites, so the real count is
  higher. **The dominant term is the SUBJECT'S cost per invocation**, not the harness and not fixture
  construction, which is three file writes.
  C3 REJECTED: each arm asks one question about a different staged break, so a batched checker would
  need to accept N trees — a public surface added to a shipped checker for its own test. C4 REJECTED:
  the subjects are shell scripts, so in-process means re-implementing them and grading the
  re-implementation. **C1 REJECTED AS A COST LEVER AND KEPT AS A PREREQUISITE**, which is the finding
  the test produced and the reasoning had not: `W="$TMP/repo"` is ONE shared fixture that `reset()`
  mutates in place before every arm, so C2's parallelism is not merely unhelpful without per-arm
  isolation, it is WRONG — and wrong in the worst way, because the arms would still pass most of the
  time. F1 had C1 and C2 as alternatives; they compose, in that order.
  BUILT and verified: 11 arms in `tools/lib/lib-selftest.test.sh`, all green, including the failing
  case, the isolation property, byte-identical arm lines at width 1 and width 4, a wedged arm that
  reds without stalling the suite, and an empty population that refuses.
- rev-3 · 2026-09-06 · folded spec-audit round 2. M3: §4 no longer calls the 469-to-220 reduction
  "the one prior instance" — the `check-pass-order.sh` rebuild is in this build's own base, is larger,
  and is now an input to F1's C1 and C3. M4: C2 may not be decided on a single-shot wall clock on a
  node whose own measurements move 5.5x median across readings; repeated readings plus the spawn count
  decide it.
- rev-2 · 2026-09-06 · folded spec-audit round 1. B3: `tools/lib/` ships nothing, which rev-1's F2
  contradicted; resolved by unit 3 rev-2 no longer shipping the suites, so the placement is now
  correct and needs no inline-parity obligation — F3 records the inline canon as prior art considered
  and rejected with its reason. H4: S3 now reads `SELFTEST_INNER_WIDTH` from the outer runner instead
  of reading the profile width a second time, which would have squared the pools to 64 processes at
  node `a`'s width 8. M1: the verb names were run through
  `python tools/lexicon/lexicon.py --suggest ... --as sh.function` — `fixture_once` and `arms_report`
  were refusals and are now `build_fixture` and `run_arms`; `arm` is a declared verb and is kept in
  its declared sense. §7 now names the lexicon leg, which no spec in the set did.

## 10. Reuse audit

No existing seam fits for the harness itself, and that is the finding rather than a failure to look:
every suite in this tree builds its own scratch subject inline, which is precisely the duplication
this unit removes. `tools/codebase-map/reuse_lookup.py` returned `run` and `check` as high-fan-in
name stems across thirteen `selftest.py` modules and `tools/codebase-map/rank_harness.py`'s
`run_constant_control`, none of which is a shared arm harness. What rev-1 MISSED and the audit
supplied is the placement prior art: `tools/lib/resolve-python.sh`'s inline canon plus its parity
leg is this tree's settled answer for a `tools/lib/` file that must reach adopters, and F3 records
why this unit does not need it. The BUDGET discipline is `tools/unattended/run-unattended-gates.sh`'s
and is `TOOL-aQuenchedHarness-4`'s seam, not this one's. Because no seam fits the harness,
`memory/guides/BUILD-METHOD.md` M12 governs: §8 F1 carries the candidate set and the test that
decides it, and the losers' tests land in §4.

Recall terms used: `selftest gate leg ceiling guard GATE_SELFTESTS run-gates scratch repo mktemp
spawn wall-clock adopter kit.toml`
