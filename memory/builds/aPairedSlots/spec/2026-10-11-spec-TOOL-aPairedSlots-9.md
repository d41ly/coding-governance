# TOOL-aPairedSlots-9 — node a's slot count and the shared-width rule, set by the two-bar A/B

**Status:** INPROGRESS · rev-1 · 2026-10-11 · node a · Tier-2 · base b6cd02bc · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-prompt-TOOL-aPairedSlots-1-1-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aPairedSlots-1-1-build-brief.md) | journal | TOOL-aPairedSlots-1 TOOL-aPairedSlots-2 TOOL-aPairedSlots-3 TOOL-aPairedSlots-4 TOOL-aPairedSlots-5 TOOL-aPairedSlots-6 TOOL-aPairedSlots-7 TOOL-aPairedSlots-8 |

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
  of each arm, by the owner's ruling of 2026-10-11, with A1 as the arm-A repetition. Observed by AC1.
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

Owner, 2026-10-11, at one repetition: `slots=2` when `B_1 <= A_1` or `C_1 <= A_1`, where each is a
MAKESPAN row whose two bars carry proof. `TS_SHARE_RULE` is `half` when `B_1 < C_1`, else `full`.

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
  arm-run, and the shipped `capable` row reaches adopters on capable hosts.
- testing — the proof column per bar; the decision recomputed from the committed rows.
- migration — none.
- user docs — the profile table's row comment and the README's turnstile section cite the record.

## 6. Acceptance criteria

- **AC1** — When `2026-10-11-build-TOOL-aPairedSlots-9-ab-results.md` is read, it carries one
  proven MAKESPAN row per arm with both bars' leg counts equal to the expected count, and a clean or
  contaminated grade per arm-run derived from its samples.
  Red when: an arm's only row is unproven or void, and the record decides on it anyway.
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
  the rows say.
- **FACT-QUESTION · F2 — Is `TS_SHARE_RULE` `half` or `full`?** The probe and observation are F1's;
  the rule is §4's. Liveness: either arm can be the smaller. Recommendation: whatever the rows say.

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft, carrying TOOL-aPairedSlots-1's former S4, AC4 and F1 and
  TOOL-aPairedSlots-3's former F1, at one repetition per arm by the owner's ruling of 2026-10-11.

## 10. Reuse audit

The seam is the instrument this build already committed and the knob and constant
TOOL-aPairedSlots-1 and -3 add. `reuse_lookup.py` named no measurement harness to reuse;
`tools/run-gates/profile_bar.py` times one bar, not a pair under a hold. Recall returned
TOOL-aMeteredTurnstile-6, the three-bar measurement re-run here for two.

Recall terms used: `python tools/memory-recall/query.py "why does the gate turnstile serialize bars and admit only one at a time" --terms "turnstile beacon queue ticket serialize concurrent bars width contended CPU host-wide nonce heartbeat reap slots"`
