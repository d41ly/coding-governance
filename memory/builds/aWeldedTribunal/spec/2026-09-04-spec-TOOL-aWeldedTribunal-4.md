# TOOL-aWeldedTribunal-4 — the tier-2 synthesis prompt carries the liveness counters the run computed

**Status:** OPEN · rev-1 · 2026-09-04 · node a · Tier-2 · base 9b5ae688 · streams tooling · order 4

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`tools/workflows/tier2-review.js` computes how badly its own run degraded — dead lenses, dead
skeptic batches, spurious and duplicate verdicts — and hands none of it to the agent that writes the
durable report. A run whose lenses half died therefore writes a record that cannot say so. The two
drift-audit siblings were given this block by `TOOL-dTieredTribunal-3`; the reference harness they
were copied from was not.

## 2. Scope (IN)

- **S1** — A `RUN INTEGRITY` block in the synthesis prompt of `tools/workflows/tier2-review.js`,
  adapted to this file's own counter names, plus the instruction the siblings carry: state these in
  the report, and do not describe the run as complete if any is non-zero.
- **S2** — The clause the siblings carry about zero counts: if lenses died, the finding set is
  INCOMPLETE and a zero is not evidence of absence. This is the half that makes the block do work,
  because a report that prints the counters and still opens with "no issues found" has reported
  nothing.
- **S3** — A criterion that REDS while the prompt lacks it, in
  `tools/workflows/check-workflow-syntax.js`, which is the merge-bar leg over this population
  (`workflow script syntax` in `tools/gate-legs.json`, subject `repo`, so it runs on every bar).
  Without it the class returns the moment someone writes a fourth harness.
- **S4** — The criterion is verified by a STAGED BREAK: the block is removed, the leg observed RED,
  the removal unstaged. A gate seen only passing is an assertion about nothing.
- **S5** — The criterion's population is DERIVED, not a list of three filenames. A harness that
  computes a liveness counter and does not interpolate it is the defect; naming the three files
  that have the problem today certifies coverage for tomorrow's fourth.

## 3. Non-goals (OUT)

- **Changing what the counters MEAN or how they are computed.** `TOOL-dTieredTribunal-1` and
  `TOOL-aGuardedTally-1` settled the counting, including that an unjudged finding is UNVERIFIED and
  never refuted. This unit moves numbers into a prompt and does not re-adjudicate them.
- **Re-counting the record.** One agent writes the record and returns the integers from one
  adjudication; nothing re-counts it. That property is stated in the file already and is unchanged.
- **A `conflictIds` or `downgrades` counter.** The siblings interpolate those because they compute
  them. This file does not, and inventing a counter so the block matches the siblings' text
  byte-for-byte would put a number in a report that nothing derives.

## 4. Design

### Inventory — the counters this file computes and where

| Counter | Line | Meaning |
|---|---|---|
| `LENSES.length` | 364 | lenses dispatched |
| `liveResults.length` | 364 | lenses that returned |
| `lensesDead` | 364 | the difference |
| `batches.length` | 397 | skeptic batches dispatched |
| `skepticsDead` | 424 | batches that died |
| `spurious` | 436 | verdicts carrying an id this run never assigned |
| `duplicates` | 435 | repeat verdicts agreeing with the standing one |
| `unverified.length` | 449 | findings no skeptic judged |

Every one is already logged to stdout, and stdout is not the record. `allFindings.length`,
`confirmed.length`, `refuted.length`, `unverified.length` and `precision` already reach the prompt;
the six that describe RUN HEALTH rather than finding counts do not.

### The block

Appended to the synthesis prompt, after the existing review-shape sentence:

```
RUN INTEGRITY - state these in the report and do NOT describe this run as complete if any is non-zero:
lenses <live>/<total> returned, <n> DIED; skeptic batches <live>/<total> returned, <n> DIED;
<n> spurious verdict(s) discarded, <n> duplicate(s).
If lenses died, the finding set is INCOMPLETE and a zero count is not evidence of absence. Say so
where you would otherwise call a zero positive evidence.
```

### The criterion, and why it is a derived population

`tools/workflows/check-workflow-syntax.js` already discovers its population by a marker
(`export const meta =`) rather than a filename list, which is the shape this criterion needs. The
predicate: for each discovered harness that BINDS a liveness counter — an identifier matching the
degradation vocabulary this corpus already uses, `lensesDead` and `skepticsDead` — assert the
literal `RUN INTEGRITY` appears in the file. A harness that computes no such counter is not in the
population and is not red for lacking a block it has nothing to put in.

The predicate is run over the tracked tree before wiring, printing hits and near-misses, per the
charter's §7 rule; the result goes in §9.

### Files touched (estimate)

- `tools/workflows/tier2-review.js` — the prompt block.
- `tools/workflows/check-workflow-syntax.js` — the criterion.

### Alternatives rejected

- **Assert the exact sibling text.** Rejected: the sibling text names counters this file does not
  compute, so byte-equality would force an invented counter or a permanent exemption.
- **Put the criterion in a new gate leg.** Rejected: `workflow script syntax` already owns this
  population, runs on every bar, and discovers by marker. A second leg over the same population is
  a second answer to one question.
- **Have the harness write the record itself instead of instructing an agent to.** Rejected: the
  harness has no filesystem and no repo access, which is stated in this file already and is why the
  binding line is instructed rather than written.

## 5. Production-readiness checklist

- security — N/A — no write path, no input boundary; the change is prompt text and a gate predicate.
- perf / scale — one longer prompt string and one regex per discovered harness.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — the block's whole subject IS the degraded state.
- observability — this unit IS the observability fix. The counters existed and went nowhere a
  reader would find them.
- risks — the block is an INSTRUCTION to an agent, not a mechanism. A synthesis agent can ignore it,
  and no gate can check that it did not. Stated here rather than implied: what S3 makes checkable is
  that the counters REACH the prompt, never that the report used them. That is the honest boundary
  and the gate's own header will say so, per the charter's rule that a gate states what it does not
  check.
- testing + left-shift gates — S3 is the left-shift and S4 is its staged RED. The class is
  `memory/gotchas/degradation-known-but-unreported.md`, and this row is its live instance.
- migration / rollback — none; two files, both revert cleanly.
- user docs — none; the harness is internal.

## 6. Acceptance criteria

- **AC1** — When `tools/workflows/tier2-review.js` is read, the synthesis prompt interpolates
  `lensesDead`, `liveResults.length`, `LENSES.length`, `skepticsDead`, `batches.length`, `spurious`
  and `duplicates`.
- **AC2** — When the `RUN INTEGRITY` block is deleted from `tools/workflows/tier2-review.js` and
  `node tools/workflows/check-workflow-syntax.js` is run, it exits non-zero and names that file.
  This is S4's staged break and it is an acceptance criterion because a gate nobody has seen fail
  is not a gate.
- **AC3** — When the block is restored, `node tools/workflows/check-workflow-syntax.js` exits `0`.
- **AC4** — When a harness that binds no liveness counter is placed in the population,
  `node tools/workflows/check-workflow-syntax.js` does NOT red it. The negative arm; without it the
  predicate could red every workflow script and still look correct on the three that matter.
- **AC5** — When `bash tools/run-gates/run-gates.sh` runs the `workflow script syntax` leg, it is
  green with the block present.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — the `workflow script syntax` leg, whose name and argv are in
`tools/gate-legs.json` and read from there.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft. Confirmed against source: `drift-audit-code.js:467` and
  `drift-audit-state.js:490` carry the block, `tier2-review.js` carries none, and every counter the
  block would name is already bound in that file at the lines §4 tabulates.

## 10. Reuse audit

The seam is the `RUN INTEGRITY` block already in `tools/workflows/drift-audit-code.js` and
`tools/workflows/drift-audit-state.js`, built by `TOOL-dTieredTribunal-3`. This unit copies that
established shape onto the third harness rather than designing a new one, and the criterion extends
`tools/workflows/check-workflow-syntax.js`, which already owns this population and already discovers
it by marker. Found by `python tools/codebase-map/reuse_lookup.py "fan-out cap hook scans a script
for loop shapes and array literals"` and by direct grep for the block literal across `tools/workflows/`.

Recall terms used: `--terms "agent-cap blankLiterals capFindings fanoutFindings landed phase check34
lander marker unrepairable govkit renormalize memory-tree conf"`
