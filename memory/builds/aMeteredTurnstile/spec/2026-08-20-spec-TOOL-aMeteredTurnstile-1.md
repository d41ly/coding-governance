# TOOL-aMeteredTurnstile-1 — the merge bar gets an instrument, not another guess

**Status:** INPROGRESS · rev-2 · 2026-08-20 · node a · Tier-2 · base 56b945cb · streams tooling

## 1. Goal

Ship one profiling verb in the `run-gates` kit that measures a bar run as a RUN — width, wall clock,
per-leg cost, and the regime the bar is in — and appends it to a record a later run can be compared
against. Use it once on node `a` to produce the measurement this repo has been designing against by
hand, and emit the recommendations that follow from it.

## 2. Scope (IN)

- **S1** — `tools/run-gates/profile_bar.py`, a verb that drives `run-gates.sh` as a subprocess at a
  pinned width, times the whole run, and never modifies the runner.
- **S2** — A per-run record appended to `<git-dir>/gate-profile.jsonl`: run id, ISO-8601 timestamp
  with offset, commit sha, host, pool width, `GATE_FULL` state, observed wall clock, and one entry
  per leg carrying its name, verdict, and measured duration.
- **S3** — Regime classification computed from that record and printed: `floor` is the longest single
  leg, `throughput` is the sum of leg durations divided by width, `bound` is whichever dominates, and
  `packing` is observed wall clock over the theoretical floor.
- **S4** — Leg attribution that excludes the cache's carried-forward and dead rows: only legs this run
  actually executed enter the record, determined from the runner's own stdout verdict lines.
- **S5** — An environment assertion block recorded alongside every run, naming each condition the
  measurement depends on and whether the harness could verify it. A condition it cannot verify is
  recorded as unverified, never as satisfied.
- **S6** — `tools/run-gates/profile_bar.test.sh`, a self-test that drives the verb over two fixture
  manifests via `GATE_LEGS`, each built so one regime is forced by construction, and asserts the
  CLASSIFICATION and the ORDERING rather than any absolute duration. Both arms observed RED first.
- **S7** — The recommendations report under `memory/builds/aMeteredTurnstile/build/`, every figure in
  it read from a `profile_bar.py` run rather than typed, and each recommendation bound to a backlog id.

## 3. Non-goals (OUT)

- No edit to `tools/run-gates/run-gates.sh`. `aPacedTurnstile` holds seven specs against that file and
  a collision here costs more than the measurement is worth.
- No scheduling change, no width change, no per-leg deadline, no guard widening, no leg sharding. The
  per-leg deadline in particular is `TOOL-aBoundedVerdict-10` and stays there.
- No repair of `gate-timings.tsv`. Its defects are reported and the profiler routes around them; the
  fix belongs to whichever unit next edits the runner.
- No CI wiring. Wiring the bar into remote CI needs a `workflow`-scoped push and is a separate unit.
- No historical backfill. The record starts empty; a series needs a second run, not a reconstruction.
- No duplication of `TOOL-aPacedTurnstile-5`. That unit specs `<git-dir>/gate-run/<run-id>/` and a
  `gate-ledger.tsv` emitted from INSIDE the runner, and it is OPEN at rev-7. This unit measures from
  OUTSIDE precisely because it may not edit the runner. When `-5` lands, this verb reads its ledger
  instead of wrapping a run, and the wrapping path is deleted rather than kept beside it.

## 4. Design

The instrument is a wrapper, not a patch. `run-gates.sh` already measures every leg and already prints
a parseable verdict per leg. What it does not do is record the RUN those numbers came from. The
profiler supplies exactly that missing envelope, and computes the one number this repo has never had,
which is how much of the wall clock is structural rather than schedulable.

### Data model

One JSON object per line in `<git-dir>/gate-profile.jsonl`, append-only. The fields are the run
envelope the timing cache lacks, plus the per-leg array the runner already knows.

| Field | Meaning |
|---|---|
| `run` | derived id, so the same commit at the same width sorts adjacently |
| `at` | ISO-8601 datetime with offset |
| `sha` | the commit profiled |
| `host` | the node, since a wall clock is not portable between machines |
| `width` | the pool width this run used |
| `full` | whether guards were bypassed |
| `wall` | observed wall clock in seconds |
| `env` | the S5 assertion block |
| `legs` | one entry per executed leg: name, verdict, duration |

### Inventory

The regime arithmetic, which is the whole analytic payload and is repo-independent:

| Quantity | Definition | What it licenses |
|---|---|---|
| `floor` | the largest single leg duration | the wall clock no width can beat |
| `throughput` | sum of leg durations over width | the wall clock perfect packing would give |
| `bound` | whichever of those two is larger | which lever is the only one that works |
| `packing` | observed wall over that larger value | scheduling loss, where 1.0 is perfect |

A bar that is `floor`-bound cannot be helped by more workers or by trimming small legs, and every
scheduling mechanism competes for the remainder. That is the sentence this repo has been missing. It
is true of any bounded-pool bar, which is why the verb ships to adopters rather than staying here.

### Rollout

One commit adds the verb, its self-test, the `[[gate_leg]]` row in `tools/run-gates/kit.toml`, and the
matching row in `tools/gate-legs.json`. The descriptor and the manifest move together or govkit
selfcheck reds. A second commit carries the measurement and the report, because the measurement must
be taken against a tree where the first commit has already landed.

### Files touched (estimate)

`tools/run-gates/profile_bar.py` and `tools/run-gates/profile_bar.test.sh` are new.
`tools/run-gates/kit.toml`, `tools/gate-legs.json`, `tools/run-gates/README.md`,
`memory/map/features/run-gates.md`, `memory/backlog/TOOL.md` and `memory/DECISIONS.md` are edited,
alongside this build folder.

### Alternatives rejected

Reading `gate-timings.tsv` as the profile was rejected. It is last-write-wins across runs at different
widths, carries no run envelope, and never evicts a renamed leg, so any series built on it compares
numbers that were never comparable. Adding an emission to `run-gates.sh` was rejected on the collision
cut-line in §3, and a wrapper is the better shape regardless, because an adopter can then profile a
bar this kit did not write.

## 5. Production-readiness checklist

- security — the record carries leg names and durations only; the runner's existing `redact` covers
  leg output and the profiler stores none of it.
- perf / scale — the profiler costs one subprocess and one file append; the JSONL grows one line per
  deliberate measurement, not one per bar run.
- a11y — N/A — a command-line verb with no interface surface.
- i18n — N/A — operator-facing diagnostic output in the language of the surrounding kit.
- error / empty / loading states — an absent git dir, an unparseable stdout, and a zero-leg run each
  produce a named refusal rather than a record asserting zero.
- observability — the verb IS the observability unit, and its own liveness assertion is S5.
- risks — the measurement is contaminated by concurrent bars and the harness cannot prove the machine
  is quiet, so S5 records that as unverified rather than pretending otherwise.
- testing + left-shift gates — S6, wired as a `[[gate_leg]]`, with the RED arm observed before wiring.
- migration / rollback — additive; deleting the two new files and their two rows reverts it whole.
- user docs — `tools/run-gates/README.md` gains the verb and the regime table.

## 6. Acceptance criteria

- **AC1** — When `python tools/run-gates/profile_bar.py --width 8` completes,
  `<git-dir>/gate-profile.jsonl` gains exactly one line whose `legs` array length equals the leg count
  that run's own stdout reported.
- **AC2** — When the same commit is profiled twice at the same width, the two records agree on
  `regime.bound`. No acceptance criterion in this unit asserts a wall clock against a literal: a
  wall-clock arm graded against load the runner does not control is the class `TOOL-cFinalBerth-5` and
  `TOOL-aTimedTurnstile-8` already retired twice, and the measured seconds go to the report as a
  MEASUREMENT rather than into a gate as a pin.
- **AC3** — When `profile_bar.py` runs against a `GATE_LEGS` fixture built so that one leg's duration
  necessarily exceeds the sum of the others over the width, `tools/run-gates/profile_bar.test.sh`
  asserts `regime.bound` is `floor`, and asserts the ORDERING `floor > throughput`. It asserts no
  absolute duration, because every duration on this bar is load-dependent.
- **AC4** — When the fixture is rebalanced so no single leg can dominate, the same test asserts
  `regime.bound` is `throughput` and the ORDERING `throughput > floor`. Both arms were observed RED
  against a deliberately inverted classifier before the leg was wired, per the gate-arming rule.
- **AC5** — When the profiler cannot verify the machine is quiet, the emitted record's `env.quiet`
  reads `unverified` and the printed summary says so; it never reads `true` by default.
- **AC6** — When a leg present in `<git-dir>/gate-timings.tsv` was not executed by this run, it is
  absent from the record's `legs` array, verified against the 3 dead rows measured on node `a`.
- **AC7** — When `GATE_FULL=1 bash tools/run-gates/run-gates.sh` runs after this unit lands, the new
  leg appears in its output, the bar is GREEN, and `python tools/govkit/govkit.py selfcheck` is clean.
- **AC8** — When the verb runs, it reports the orphan count of `<git-dir>/gate-timings.tsv` — rows
  naming a leg the manifest no longer declares — as a diagnostic. It reports; it does not gate. Making
  that a gate would red the bar today on 3 known orphans and belongs to a follow-up unit.

## 7. Gates

Every leg of `GATE_FULL=1 bash tools/run-gates/run-gates.sh`, which is this unit's Definition of Done.
The legs this unit specifically adds or moves: the new profile-bar selftest leg, `govkit selfcheck` and
`govkit selftest` for the descriptor and manifest rows, `run-gates canary` for a new manifest row,
codebase-map coverage and freshness for a new tracked file under `tools/`, the kickoff-manifest
ratchet, and `memory hygiene` for this build folder and spec.

## 8. Open questions

- **F1 — does the profiler run the bar, or attach to a run the operator starts?** Running it is simpler
  and makes width and `GATE_FULL` state facts rather than guesses. Attaching would let a push-boundary
  run be profiled for free, but it requires the runner to emit a marker, which §3 forbids.
  RESOLVED (agent, 2026-08-20, delegated): run it, per the §3 cut-line.
- **F2 — does the new leg run the full profiler on every bar?** It must not. Profiling the bar from
  inside the bar is unbounded recursion and would dominate the very wall clock this unit measures.
  RESOLVED (agent, 2026-08-20, delegated): the leg runs the fixture self-test only, never the real
  manifest.
- **F3 — where does the recommendations report live?** The build's own `build/` folder is the
  sanctioned home for a non-spec recording and keeps it out of the memory root.
  RESOLVED (agent, 2026-08-20, delegated): `memory/builds/aMeteredTurnstile/build/`.

## 9. Revision log

- rev-1 · 2026-08-20 · initial draft.
- rev-2 · 2026-08-20 · folded workflow `wf_385dfe29-e10`. AC2 and AC3 rewrote a wall-clock-against-a-
  literal assertion into an ordering-and-classification one, the arm class `TOOL-cFinalBerth-5` and
  `TOOL-aTimedTurnstile-8` retired twice. §3 gained the `TOOL-aPacedTurnstile-5` overlap and the
  supersession path. AC8 added the timing-cache orphan diagnostic, reporting and never gating.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "measure and record how long the gate bar and each of its
legs take"` returned no profiling, timing-record or benchmark seam anywhere in the corpus. The nearest
candidates were `do_measure` in `tools/memory-tree/corpus_ids.py`, which measures a byte budget rather
than elapsed time, and the `run-gates` affordance seam `KITDIR`/`ROOTN`/`KITREL`/`LEGS_FILE`, which is
the path derivation this unit reuses rather than re-deriving. No existing seam fits. The seam this unit
wires through is `GATE_LEGS`, the manifest override the runner already exposes for exactly this purpose.
