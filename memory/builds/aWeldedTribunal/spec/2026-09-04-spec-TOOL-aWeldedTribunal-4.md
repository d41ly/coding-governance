# TOOL-aWeldedTribunal-4 — the tier-2 synthesis prompt carries the liveness counters the run computed

**Status:** CLOSED · rev-3 · 2026-09-04 · node a · Tier-2 · base 9b5ae688 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-review-TOOL-aWeldedTribunal-1-8-diff-round1.md](../reviews/2026-09-04-review-TOOL-aWeldedTribunal-1-8-diff-round1.md) | diff-review | TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8 |
| [2026-09-04-review-TOOL-aWeldedTribunal-1-8-diff-round2.md](../reviews/2026-09-04-review-TOOL-aWeldedTribunal-1-8-diff-round2.md) | diff-review | TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8 |
| [2026-09-04-review-TOOL-aWeldedTribunal-1-8-round1.md](../reviews/2026-09-04-review-TOOL-aWeldedTribunal-1-8-round1.md) | spec-audit | TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8 |
| [2026-09-04-review-TOOL-aWeldedTribunal-1-8-round2.md](../reviews/2026-09-04-review-TOOL-aWeldedTribunal-1-8-round2.md) | spec-audit | TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8 |
| [2026-09-05-review-TOOL-aWeldedTribunal-1-8-diff-round3.md](../reviews/2026-09-05-review-TOOL-aWeldedTribunal-1-8-diff-round3.md) | diff-review | TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/workflows/tier2-review.js` computes how badly its own run degraded — dead lenses, dead
skeptic batches, contradictory verdicts, spurious and duplicate ones — and hands none of it to the
agent that writes the durable report. A run whose lenses half died therefore writes a record that
cannot say so. The two drift-audit siblings were given this block by `TOOL-dTieredTribunal-3`; the
reference harness they were copied from was not.

## 2. Scope (IN)

- **S1** — A `RUN INTEGRITY` block in the synthesis prompt of `tools/workflows/tier2-review.js`,
  adapted to this file's own counter names, plus the instruction the siblings carry: state these in
  the report, and do not describe the run as complete if any is non-zero.
- **S2** — The clause the siblings carry about zero counts: if lenses died, the finding set is
  INCOMPLETE and a zero is not evidence of absence. This is the half that makes the block do work,
  because a report that prints the counters and still opens with "no issues found" has reported
  nothing.
- **S3** — The left-shift is a DOCUMENTED CHECK plus a refresh of
  `memory/gotchas/degradation-known-but-unreported.md`, naming this harness as a closed instance of
  the class and the DoD line that keeps it closed. It is NOT a gate. Rev-1 specified a scanner; §3
  records why that was dropped.

## 3. Non-goals (OUT)

- **A SCANNER, and this is a reversal of rev-1 rather than an omission.** `memory/DECISIONS.md:116`
  records `TOOL-dTieredTribunal-9`: *"the left-shift M8 owed for the closing review's D1 and D2 is a
  `memory/gotchas/` RECORD, not a scanner (owner, 2026-08-26). Named as a documented check, not a
  gate: nothing static separates a fold-created sentence from any other."* Rev-1's S3 built exactly
  the refused thing, and its predicate — assert the literal `RUN INTEGRITY` appears in the file —
  demonstrates the ruling's own reasoning: a comment carrying those two words satisfies it, so the
  gate could not fail for the reason it existed. A standing mandate delegates this build's forks and
  its scope; it does not reach a ratified owner decision, so the disposition is to DROP the scope
  item, not to park the unit and not to build it anyway.
- **Changing what the counters MEAN or how they are computed.** `TOOL-dTieredTribunal-1` and
  `TOOL-aGuardedTally-1` settled the counting, including that an unjudged finding is UNVERIFIED and
  never refuted. This unit moves numbers into a prompt and does not re-adjudicate them.
- **Re-counting the record.** One agent writes the record and returns the integers from one
  adjudication; nothing re-counts it. That property is stated in the file already and is unchanged.
- **A `downgrades` / severity-correction counter.** The siblings interpolate one because they
  compute one. This file does not, and inventing a counter so the block matches the siblings'
  text byte-for-byte would put a number in a report that nothing derives. Rev-1 said the same of
  `conflictIds` and was WRONG: this file computes that one under a different spelling, and §4's
  inventory now carries it.

## 4. Design

### Inventory — the counters this file computes and where

| Counter | Line | Meaning |
|---|---|---|
| `LENSES.length` | 364 | lenses dispatched |
| `liveResults.length` | 364 | lenses that returned |
| `lensesDead` | 364 | the difference |
| `batches.length` | 397 | skeptic batches dispatched |
| `skepticsDead` | 424 | batches that died |
| `conflicts.size` | 434 | findings whose skeptics disagreed, demoted to unverified |
| `spurious` | 436 | verdicts carrying an id this run never assigned |
| `duplicates` | 435 | repeat verdicts agreeing with the standing one |

Every one is already logged to stdout, and stdout is not the record. `allFindings.length`,
`confirmed.length`, `refuted.length`, `unverified.length` and `precision` already reach the prompt;
every counter in the table above describes RUN HEALTH rather than a finding count, and none of them
reaches the prompt.

`conflicts` is the counter rev-1 wrongly excluded. It is bound at `:434`, added to at `:443`, used to
DELETE verdicts at `:445`, warned about at `:455`, and returned as `conflicts:` at `:480` and `:593`.
It is the one counter that says findings were demoted because two skeptics disagreed — precisely the
degradation §1 exists to surface — and it was kept out of the durable record on a premise that
nothing needed inventing. Only the spelling differs from the siblings' `conflictIds`.

### The block

Appended to the synthesis prompt, after the existing review-shape sentence:

```
RUN INTEGRITY - state these in the report and do NOT describe this run as complete if any is non-zero:
lenses <live>/<total> returned, <n> DIED; skeptic batches <live>/<total> returned, <n> DIED;
<n> contradictory verdict(s) demoted to unverified, <n> spurious verdict(s) discarded, <n> duplicate(s).
If lenses died, the finding set is INCOMPLETE and a zero count is not evidence of absence. Say so
where you would otherwise call a zero positive evidence.
```

### The left-shift, and what it can and cannot be

The owner ruling in §3 settles the form: a record and a documented check. The record
`memory/gotchas/degradation-known-but-unreported.md` gains this harness as a closed instance, naming
the counter set, so a future reader of the class sees which carriers are covered. The documented
check is a DoD line: a harness that computes a liveness counter states it where the durable record
is written, and that is verified by reading the prompt, not by a predicate.

Stated plainly because the temptation will return: what a static check CAN see is that the identifiers
in the table above appear inside the synthesis prompt's template literal. What it cannot see is whether the
report used them, and a check that greps for the block's own words is satisfied by a comment quoting
this spec. The ruling is right and rev-1 was wrong.

### Files touched (estimate)

- `tools/workflows/tier2-review.js` — the prompt block.
- `memory/gotchas/degradation-known-but-unreported.md` — the closed-instance entry.

### Alternatives rejected

- **Assert the exact sibling text.** Rejected: the sibling text names a `downgrades` counter this
  file does not compute, so byte-equality would force an invented counter or a permanent exemption.
- **A gate leg for the block.** Refused by owner ruling `TOOL-dTieredTribunal-9`; see §3.
- **Have the harness write the record itself instead of instructing an agent to.** Rejected: the
  harness has no filesystem and no repo access, which is stated in this file already and is why the
  binding line is instructed rather than written.

## 5. Production-readiness checklist

- security — N/A — no write path, no input boundary; the change is prompt text.
- perf / scale — one longer prompt string.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — the block's whole subject IS the degraded state.
- observability — this unit IS the observability fix. The counters existed and went nowhere a
  reader would find them.
- risks — the block is an INSTRUCTION to an agent, not a mechanism. A synthesis agent can ignore it,
  and per §3's ruling no gate can usefully check that it did not. This limit is the reason the
  left-shift is a record, and it is stated rather than implied.
- testing + left-shift gates — S3, which is a record and a documented check, not a gate. The class
  is `memory/gotchas/degradation-known-but-unreported.md`, and this row is its live instance.
- migration / rollback — none; two files, both revert cleanly.
- user docs — none; the harness is internal.

## 6. Acceptance criteria

- **AC1** — When the synthesis prompt in `tools/workflows/tier2-review.js` is read, it interpolates
  every counter in §4's inventory: `lensesDead`, `liveResults.length`, `LENSES.length`,
  `skepticsDead`, `batches.length`, `conflicts.size`, `spurious` and `duplicates`. The criterion is
  the SET, not a sample, so a counter dropped from the block fails it. **And it covers the block's
  two SENTENCES as well as its interpolations** — the do-not-describe-this-run-as-complete
  instruction and the a-zero-is-not-evidence-of-absence clause. S2 calls the second one "the half
  that makes the block do work", and a block carrying all eight numbers and neither sentence is
  exactly the "prints the counters and still opens with no issues found" outcome this unit exists to
  prevent.
- **AC2** — When `tools/workflows/tier2-review.js` is run end to end on a real review, the report it
  writes contains a `RUN INTEGRITY` line carrying those numbers. This is the observation that the
  block reached the record rather than only the source, and it is the one this build can make
  because the closing review of this very build runs that harness.
- **AC3** — When `memory/gotchas/degradation-known-but-unreported.md` is read, it names
  `tools/workflows/tier2-review.js` as a closed instance and names the counter set. This is S3, and
  it is observable by reading one file because the owner ruling says the left-shift is that file.
- **AC4** — When `node tools/workflows/check-workflow-syntax.js` runs, it exits `0`. The block must
  not break the syntax leg, which is subject `repo` and therefore runs on every bar.
- **AC5** — When `bash tools/run-gates/run-gates.sh` runs, the `workflow script syntax` leg is
  green; that leg is `subject = repo`, so the plain bar runs it. **In addition**, when
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` runs, `tier2-review self-test` is
  green — it guards on `tools/workflows/`, which is where this unit's only code change lands.

## 7. Gates

`GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, **and rev-2 was wrong to say no
`GATE_SELFTESTS` was owed here.** This unit's only code file is `tools/workflows/tier2-review.js`,
and `tools/gate-legs.json` carries THREE kit-subject legs guarding on `tools/workflows/`:
`tier2-review self-test` (ceiling 1800), `verifier fan-out self-test` and `review-join self-test`.
The edited file sits inside that guard, so a prompt edit breaking that suite would land green under
rev-2's command. The plain `bash tools/run-gates/run-gates.sh` still covers the `workflow script
syntax` leg, which is `subject = repo` and runs on every bar.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft. Confirmed against source: `drift-audit-code.js:467` and
  `drift-audit-state.js:490` carry the block, `tier2-review.js` carries none, and every counter the
  block would name is already bound in that file.
- rev-2 · 2026-09-04 · folded spec-audit round 1 (B2, H6, H9). **B2, blocker:** rev-1's S3 built the
  scanner owner ruling `TOOL-dTieredTribunal-9` refused at `memory/DECISIONS.md:116`, with a
  predicate a comment satisfies. S3/S4/S5, AC2, AC3 and AC4 of rev-1 are DROPPED and the left-shift
  is now the record the ruling names. **H6** dies with them, as the review said it would.
  **H9, high:** rev-1's third non-goal claimed this file computes no contradictory-verdict counter.
  False — `conflicts` at `:434`. It is now in §4's inventory, in the block and in AC1, and the
  non-goal is narrowed to `downgrades` alone.

- rev-3 · 2026-09-04 · folded spec-audit round 2 (H3, M2, M5). The loop exited NON-CONVERGENT at
  round 2, so this is the disposing fold and there is no round 3. **H3, high:** §7 said flatly that
  no `GATE_SELFTESTS` was owed, while `tools/gate-legs.json` carries three kit-subject legs guarding
  on `tools/workflows/` — the directory holding this unit's only code file. A prompt edit breaking
  `tier2-review self-test` would have landed green, and the sentence also put two opposite rules
  about one leg class inside one spec set. **M2:** after rev-2 dropped the scanner ACs, nothing
  observed S2's incompleteness clause, so a block with all eight counters and neither sentence passed
  every criterion; AC1 now covers the block's TEXT. **M5:** the fold grew §4's inventory to eight rows
  and left two sentences beside it saying "the seven"; both now point at the table, per the same
  no-count-in-prose rule.

## 10. Reuse audit

The seam is the `RUN INTEGRITY` block already in `tools/workflows/drift-audit-code.js` and
`tools/workflows/drift-audit-state.js`, built by `TOOL-dTieredTribunal-3`. This unit copies that
established shape onto the third harness rather than designing a new one. The left-shift reuses
`memory/gotchas/degradation-known-but-unreported.md`, the class record that already exists for
exactly this defect. Found by `python tools/codebase-map/reuse_lookup.py "fan-out cap hook scans a
script for loop shapes and array literals"` and by direct grep for the block literal across
`tools/workflows/`.

Recall terms used: `--terms "agent-cap blankLiterals capFindings fanoutFindings landed phase check34
lander marker unrepairable govkit renormalize memory-tree conf"`
