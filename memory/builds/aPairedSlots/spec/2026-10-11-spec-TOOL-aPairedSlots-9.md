# TOOL-aPairedSlots-9 — node a's slot count and the shared-width rule, set by the two-bar A/B

**Status:** CLOSED · rev-2 · 2026-10-12 · node a · Tier-2 · base b6cd02bc · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aPairedSlots-9-1-acceptance-ledger.md](../build/2026-10-11-build-TOOL-aPairedSlots-9-1-acceptance-ledger.md) | journal | — |
| [2026-10-11-build-TOOL-aPairedSlots-9-ab-plan.txt](../build/2026-10-11-build-TOOL-aPairedSlots-9-ab-plan.txt) | journal | — |
| [2026-10-11-build-TOOL-aPairedSlots-9-ab-results.md](../build/2026-10-11-build-TOOL-aPairedSlots-9-ab-results.md) | journal | — |
| [2026-10-11-build-TOOL-aPairedSlots-9-ab-results.tsv](../build/2026-10-11-build-TOOL-aPairedSlots-9-ab-results.tsv) | journal | — |
| [2026-10-11-build-TOOL-aPairedSlots-9-ab-samples.tsv](../build/2026-10-11-build-TOOL-aPairedSlots-9-ab-samples.tsv) | journal | — |
| [2026-10-11-build-TOOL-aPairedSlots-9-rule-check.py](../build/2026-10-11-build-TOOL-aPairedSlots-9-rule-check.py) | journal | — |
| [2026-10-11-prompt-TOOL-aPairedSlots-1-1-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aPairedSlots-1-1-build-brief.md) | journal | TOOL-aPairedSlots-1 TOOL-aPairedSlots-2 TOOL-aPairedSlots-3 TOOL-aPairedSlots-4 TOOL-aPairedSlots-5 TOOL-aPairedSlots-6 TOOL-aPairedSlots-7 TOOL-aPairedSlots-8 |
| [2026-10-12-review-TOOL-aPairedSlots-1-9-diff-review-round1.md](../reviews/2026-10-12-review-TOOL-aPairedSlots-1-9-diff-review-round1.md) | diff-review | TOOL-aPairedSlots-1 TOOL-aPairedSlots-2 TOOL-aPairedSlots-3 TOOL-aPairedSlots-4 TOOL-aPairedSlots-5 TOOL-aPairedSlots-6 TOOL-aPairedSlots-7 TOOL-aPairedSlots-8 |

<!-- /gen:spec-records -->

## 1. Goal

The turnstile's header records that three concurrent full bars ran slower than serial ones, and the
owner asked for it to be re-measured for two before anything changes. This unit runs that A/B on
node a and writes what it decides: the `slots` value on the `capable` row of
`tools/run-gates/gate-profiles.txt` and the value of `TS_SHARE_RULE` in
`tools/run-gates/run-gates.sh`. The capability ships either way; this unit decides only whether
node a turns it on and at which width.

## 2. Scope (IN)

- **S1 — the A/B.** The instrument under this build's `build/` runs arm A (two full bars one after
  the other, at the profile's width), arm B (both at once, each at half that width) and arm C (both
  at once, each at the full width) on two frozen clones of one base, each arm-run under a held host
  turnstile after a quiet-host wait, and every bar proving it ran every unheld leg. One repetition
  of each arm, by the owner's ruling of 2026-10-11, with A1 as the arm-A repetition. A concurrent
  arm-run still running once it has passed A1's makespan is stopped there, and its makespan is
  recorded as that lower bound. Observed by AC1.
- **S2 — the results, committed.** The rows, the samples, the arm-run log and a results record
  that grades each arm-run clean or contaminated from its samples, and applies the rule below, are
  committed under `build/`. Observed by AC1, AC2.
- **S3 — the two values.** The `capable` row carries `slots=2` when arm B's or arm C's makespan is
  no worse than arm A's; otherwise it carries no `slots` key and the README's Parked slot records
  the numbers and the reason, so an owner can flip it. `TS_SHARE_RULE` is `half` when arm B's
  makespan is the smaller of B and C, `full` otherwise. Observed by AC2.

## 3. Non-goals (OUT)

- A second repetition of any arm. The owner cut it on 2026-10-11 after the first launches spent
  their hours queued behind other sessions' bars: one repetition each, and building started beside
  the measurement.
- Running a concurrent arm-run to completion once it has passed A1's makespan. Past that point the
  rule's answer for the arm cannot change, and the hours it would cost are what the owner cut.
- Excluding contaminated arm-runs after the fact. Contamination is a graded column; an arm-run the
  results record grades contaminated is said so beside its number, and the decision names it.
- The mechanisms the values switch on (TOOL-aPairedSlots-1, -2 and -3).

### Edges

- **consumes-from** `TOOL-aPairedSlots-1` — the `slots` row key this unit writes a value into.
- **consumes-from** `TOOL-aPairedSlots-3` — the `TS_SHARE_RULE` constant this unit sets.

## 4. Design

### The A/B

The instrument is `2026-10-11-build-TOOL-aPairedSlots-1-ab-instrument.sh`. `init` builds a bare
remote advertising only `main` at the base, origin/main `d19938f3` where aFrugalTurnstile landed,
and two clones of it, so the clones are separate repositories nothing else writes. Each arm-run
first takes the clone runner's `--hold`, so every bar from a runner that knows the host turnstile
queues behind it, then waits inside the hold for bars already running to finish, bounded at an
hour. Both of the arm's bars nest under the hold. An arm runs only when the hold holds: a hold that
waited out the two-hour queue bound runs nothing and is taken again.

Every bar is `GATE_FULL=1` with self-tests held, the default full bar. A bar PROVES it ran when its
`GATE ok` plus `GATE FAIL` lines equal the legs its clone's manifest does not hold, and its run
record carries a verdict. A sampler records foreign bars, bash processes, load average, CPU and
free memory through every arm-run.

### What the first launches cost, recorded so the next A/B does not pay it

- The quiet scan counted the hold's own heartbeat ticker as a foreign bar, so A1's quiet wait ran
  its full hour; A1's foreign-bar column is one high throughout.
- A hold that waited out the queue bound behind A1 failed open, exported no holder nonce, and B1's
  two bars did not nest, so they ran one after the other for 80 minutes before it was caught. That
  B1 is void; its rows carry rc 143.
- Arm-runs queued behind other sessions' landing bars for one to three hours each. That cost, not
  the bars, is what the owner cut.

### The decision rule

Owner, 2026-10-11, at one repetition: `slots=2` when `B_1 <= A_1` or `C_1 <= A_1`. `A_1` must be a
MAKESPAN row whose two bars carry proof. A concurrent arm passes `<= A_1` only on a proven row; a row
stopped past `A_1` is a lower bound above it and fails, which it does without proof, since finishing
could only raise it. `TS_SHARE_RULE` is `half` when `B_1 < C_1` is SHOWN, by two proven rows or a
proven `B_1` below `C_1`'s lower bound, and `full` otherwise. At one slot the share rule is never
read, so `full` there is a default, not a measurement.

### Inventory

No function or variable is minted. Records: the results record and the rows beside the instrument.

### Files touched (estimate)

- `tools/run-gates/gate-profiles.txt`
- `tools/run-gates/run-gates.sh`

The results record, its rows and the README's Parked slot are records under this build's own folder.

### Alternatives rejected

- **Two repetitions, as first specified.** The owner ruled it out for its cost on a shared host.

## 5. Production-readiness checklist

- security — N/A — two values in tracked files.
- perf / scale — the subject; the rows are the evidence.
- error / empty / loading states — a void or unproven arm-run decides nothing and is named.
- observability — the results record, and the `slots` field on the profile line above 1.
- risks — one repetition on a host other sessions load; the record grades contamination per
  arm-run, and the shipped `capable` row reaches adopters on capable hosts. The record also states
  the host's kernel pool and spawn cost at the measurement, since a leaked pool makes process
  creation the contended resource and a rebooted host could answer differently.
- testing — the proof column per bar; the decision recomputed from the committed rows.
- migration — none.
- user docs — the build README's Parked slot carries the numbers and how an owner flips the value.
  The kit's own files ship to adopters and name no record of this repository.

## 6. Acceptance criteria

- **AC1** — When `2026-10-11-build-TOOL-aPairedSlots-9-ab-results.md` is read, it carries per arm
  one MAKESPAN row that is either proven, both bars' leg counts equal to the expected count, or a
  lower bound from an arm-run stopped past A1's makespan, and a clean or contaminated grade per
  arm-run derived from its samples.
  Red when: an arm's only row is unproven or void, and the record decides on it anyway, or a lower
  bound decides `<= A_1` or the share rule's `half`.
- **AC2** — When the decision rule in §4 is recomputed from the committed rows, it gives the
  `capable` row's `slots` value and the `TS_SHARE_RULE` value the tree carries.
  Red when: either value disagrees with the rule over the committed rows.
  figure: DERIVED at observation time from the committed rows.

## 7. Gates

`run-gates canary` · `memory hygiene`

## 8. Open questions

- **FACT-QUESTION · F1 — Does node a's `capable` row carry `slots=2`?** The probe is the A/B; the
  observation is A1, B1 and C1's MAKESPAN rows; the rule is §4's. Liveness: arm A can win, and every
  bar must carry proof, so a run that measured nothing cannot decide it. Recommendation: whatever
  the rows say. RESOLVED (agent, 2026-10-12, delegated): no. A1 is 8440 s, and B1 and C1 are lower
  bounds of 11162 s and 8945 s, so the row carries no `slots` key and node a stays at one slot.
- **FACT-QUESTION · F2 — Is `TS_SHARE_RULE` `half` or `full`?** The probe and observation are F1's;
  the rule is §4's. Liveness: either arm can be the smaller. Recommendation: whatever the rows say.
  RESOLVED (agent, 2026-10-12, delegated): `full`. Both are lower bounds, so `B_1 < C_1` is not
  shown, and the rule's other branch applies.

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft, carrying TOOL-aPairedSlots-1's former S4, AC4 and F1 and
  TOOL-aPairedSlots-3's former F1, at one repetition per arm by the owner's ruling of 2026-10-11.
- rev-2 · 2026-10-12 · B1 ran past A1's makespan and was stopped there, and C1 was given the same
  bound. AC1 and the rule now say what a stopped arm-run's lower bound decides and what it cannot.
  User docs move to the README's Parked slot, since the kit's files ship to adopters.

## 10. Reuse audit

The seam is the instrument this build already committed and the knob and constant
TOOL-aPairedSlots-1 and -3 add. `reuse_lookup.py` named no measurement harness to reuse;
`tools/run-gates/profile_bar.py` times one bar, not a pair under a hold. Recall returned
TOOL-aMeteredTurnstile-6, the three-bar measurement re-run here for two.

Recall terms used: `python tools/memory-recall/query.py "why does the gate turnstile serialize bars and admit only one at a time" --terms "turnstile beacon queue ticket serialize concurrent bars width contended CPU host-wide nonce heartbeat reap slots"`
