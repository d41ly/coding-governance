# TOOL-dMergedTally-1 — the disposal guard counts raw findings on both sides of its subtraction

**Status:** INPROGRESS · rev-2 · 2026-09-16 · node d · Tier-2 · base 4cf0944d · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-build-TOOL-dMergedTally-1-1-acceptance-ledger.md](../build/2026-09-16-build-TOOL-dMergedTally-1-1-acceptance-ledger.md) | journal | — |
| [2026-09-16-review-TOOL-dMergedTally-1-diff-review-round1.md](../reviews/2026-09-16-review-TOOL-dMergedTally-1-diff-review-round1.md) | diff-review | — |

<!-- /gen:spec-records -->

## 1. Goal

The build harness's DISPOSAL guard subtracts `blockers + highs` from `confirmed`, and the two sides
were counted in different units, so a synthesis that merged raw findings into items made every honest
disposal fail. This unit makes `tier2-review.js` derive both severity counts over the same raw
confirmed findings `confirmed` counts.

## 2. Scope (IN)

- **S1** — The synthesis agent in `tools/workflows/tier2-review.js` returns `items`, each a severity
  from the closed four and the raw confirmed ids it covers, in place of the two integers it typed.
  The prompt says both counts are derived from those ids and asks the review shape to state the
  tally by item and by raw finding. Observed by AC1 and AC5.
- **S2** — `tier2-review.js` counts `blockers` and `highs` over raw confirmed ids. A confirmed id in
  no item, in two, or only under a severity outside the closed four returns both as null with a note
  naming the ids. A non-confirmed id is ignored and severity is case-folded. Observed by AC1, AC2,
  AC3 and AC4.
- **S3** — The disposal prompt in `tools/workflows/unattended-build.template.js` and its render says
  its counts are of raw findings by report id and that a merged finding takes its item's severity.
  The guard is unchanged. Observed by AC6.
- **S4** — Regression arms in `tools/workflows/unattended-build.test.sh` run the REAL callee with only
  its agents doubled and feed its RESULT to the build harness, under a runner switch that makes a
  double answer as its schema allows. Observed by AC1 to AC5 and AC7.
- **S5** — The backlog row and the review-harness dossier's gap line. NOT OBSERVED — they are records,
  and the memory-hygiene leg grades their shape only.

## 3. Non-goals (OUT)

- **The convergence count does not change unit back.** The driver's `--review --blockers` now
  receives the raw count. Round-1 finding C1/S1 argued that lens duplication makes a raw count a
  poor convergence signal, and the skeptic refuted it: this harness audits spec-set subjects bounded
  at one round, and the diff-review skeptics refute duplicates. The residual is named here rather
  than built.
- **Nothing re-reads the written report against `items`.** The dossier records it as a gap.
- **The drift-audit sibling workflows are untouched.** They carry no severity counts.
- **No kit version moves.** Whether a payload change owes a bump is the open row
  `TOOL-aHoistedPass-31`, and this kit's previous payload change also shipped at 1.8.
- **The dLoggedFlight round-1 audit is not re-disposed.** That build disposed it by hand at `82a1ace0`.

### Edges

- **consumes-from** external — the DISPOSAL stage and its severity floors, landed by `TOOL-aProbedUnit-7`; this unit changes the unit of what those floors read and not the floors.

## 4. Design

### Data model

The synthesis schema's required keys are `path`, `summary` and `items`. An item is
`{severity: "BLOCKER"|"HIGH"|"MEDIUM"|"LOW", ids: [integer]}`. The return object keeps its keys:
`blockers` and `highs` are integers when a synthesis ran and placed every confirmed id exactly once,
and null otherwise, which is the stated absence the harness already refuses at
`tools/workflows/unattended-build.js:743`.

The derivation is a join on the orchestrator-assigned integer id, the same key the skeptic verdicts
join on. Each item's severity is folded to upper case and tested against the closed four; an item
outside it is skipped, so its ids surface as unplaced. Ids that are not confirmed are skipped. A
confirmed id seen a second time is recorded as repeated. Any unplaced or repeated id sets
`tallyFault`, nulls both counts and puts the ids in `note`, which ranks below a dead synthesis and
above every other note.

### Inventory

| Minted | Where | Cell |
|---|---|---|
| `items` | synthesis schema field | none, a schema key |
| `tallyFault`, `severityById`, `repeated`, `perItem`, `perRaw`, `holdsConfirmed` | locals in `tier2-review.js` | none, not definitions |
| `build_merged_returns`, `run_merged_review`, `run_merged_build` | `unattended-build.test.sh` | `sh.function`, verb-led |
| `RUN_WF_SCHEMA` | environment switch read by `run_wf`'s node script | none |
| `schemaShaped` | a `const` arrow inside `run_wf`'s node script | none, not an extracted definition |

### Files touched (estimate)

`tools/workflows/tier2-review.js`, `tools/workflows/unattended-build.template.js` and its render,
`tools/workflows/unattended-build.test.sh`, `memory/backlog/TOOL.md`,
`memory/map/features/review-harnesses.md`.

### Alternatives rejected

- **Reword the prompt.** It already said CONFIRMED findings and the measured synthesis counted items
  anyway, so a sentence is the fix that had already failed.
- **Return item counts and compare items with items in the guard.** The guard's sum reconciles
  against `confirmed + unverified`, and both are raw, so one guard would hold two units.
- **Take the higher severity of a repeated id.** That adjudicates on the synthesis's behalf: it would
  promote a finding the report folded.

## 5. Production-readiness checklist

- security — N/A: no write path, no sanitization or egress surface; the change is a count.
- perf / scale — one pass over the items per review; negligible beside the agents.
- error / empty / loading states — an empty confirmed set counts 0 and 0 (AC4); an unplaced or repeated id is a named null (AC2).
- observability — the note names the faulting ids, and a log line gives the tally by item and by raw finding.
- risks — a synthesis that places ids badly now costs a degraded round instead of a wrong disposal; accepted.
- testing — the MT arms of S4, staged RED against the base and by eight mutations (AC7).
- migration — N/A for data; a convergence sequence recorded before this change carries item counts (§3).
- user docs — N/A: no user-facing page; the dossier gap line is the maintainer-facing record.

## 6. Acceptance criteria

The fixture every criterion below uses: the suite's preamble through `audit()` plus the block headed
`TOOL-dMergedTally-1`, sourced with `HERE` pointing at a directory holding the landed
`tier2-review.js`, `unattended-build.js` and `unattended-unit.js`. Those lines define every helper
and run only the block's own arms.

- **AC1** — When `run_merged_review` runs the callee over the measured shape and `run_merged_build`
  feeds its RESULT to the harness with a disposal of 9 promoted and 4 folded, the callee RESULT
  carries `"blockers":3,"highs":6` and the harness logs `disposal: done — promoted 9 · folded 4`.
  Red when: the callee returns the item counts 1 and 5, or the guard refuses with `do not split by severity`.
  figure: 48 raw, 13 confirmed and the merges 14/26/40 and 16/4 are PINNED from the dLoggedFlight round-1 record at `5cccfc06`.
- **AC2** — When the item list drops id 33, the callee RESULT carries `"blockers":null,"highs":null`
  and a note naming `confirmed id(s) 33 sit in no item`; when id 4 sits in two items, the note names
  `sit in more than one item` and the harness prints `non-integer blocker count` with no `phase:Disposal` line.
  Red when: a count comes back with an id unplaced, or the harness reaches the disposal stage.
- **AC3** — When id 48 is left unjudged and listed at BLOCKER, the RESULT carries `"unverified":1,`
  beside `"blockers":3,"highs":6`; when id 33's item says `CRITICAL`, the note names id 33 unplaced;
  when id 1's item says `high`, the counts stay 3 and 6.
  Red when: an unverified id moves a count, an out-of-set severity places an id, or a lowercase severity unplaces one.
- **AC4** — When no finding is judged and `items` is empty, the RESULT carries `"blockers":0,"highs":0`
  beside `"unverified":48`, and the harness logs `disposal: done — promoted 0 · folded 48`.
  Red when: an empty confirmed set reads as a tally fault and the harness throws instead of disposing.
- **AC5** — When the callee runs under `RUN_WF_SCHEMA=strict`, its `prompt:synth:` trace line carries
  `Return JSON {path, items, summary}`, and a synthesis double with no `items` key yields the note
  `the synthesis agent died` with both counts null.
  Red when: the schema or the prompt reverts to `blockers` and `highs`, which the double would otherwise mask.
- **AC6** — When `diff tools/workflows/unattended-build.js tools/workflows/unattended-build.template.js`
  runs, it prints only the six install-token line pairs; and `grep -c 'Every count above is of RAW'`
  over each file prints 1.
  Red when: the render and the template disagree beyond the tokens, or either lacks the sentence.
- **AC7** — When the fixture runs against `4cf0944d`'s `tier2-review.js` and render, 18 of its 22
  arms fail and the 4 that pass are liveness controls; and when each of eight mutations of the
  derivation is applied alone, at least one arm fails.
  Red when: an arm claiming the fix passes on the base code, or a mutation survives every arm.
  figure: 18 and 22 are DERIVED by running the fixture; the mutations are counting per item, no partition refusal, repeats unseen, unverified counted, no closed severity list, no case fold, the schema and prompt reverted, and an empty confirmed set nulled.

## 7. Gates

`workflow script syntax` · `verifier fan-out` · `review-protocol parity (kit vs dogfood)` · `install-prefix (shipped surface)` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/unattended-build.test.sh · the MT block, staged RED against the base callee and render and by eight mutations of the derivation · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial record, written after the code at `ff8f1a4c`. The unit was taken
  Tier-1 at kickoff and re-tiered to Tier-2 because `tier2-review.js` ships to adopters, which is the
  class `memory/gotchas/shipped-checker-edit-is-an-adopter-contract-change.md` records.
- rev-2 · 2026-09-16 · §4 · S4 · AC4 · AC5 · AC7 · folded round 1 of the closing diff review: T1, the
  schema-strict runner switch, the prompt arm and the absent-`items` arm; T3, the zero-confirmed arm.
  Fourteen findings refuted, C1/S1 named in §3.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "derive a severity count from the ids a synthesis agent
returns instead of an integer it types"`, run on 2026-09-16 at `ff8f1a4c`, ranked `inventory_ids`
and `derive_scope`, neither of them this seam, and reported `.sh` as an unscanned layer. No existing
seam fits by the map. The seam was found by reading source: the verdict join in `tier2-review.js`
keys skeptic verdicts on the orchestrator-assigned integer id and counts spurious ids rather than
trusting them (`TOOL-aFoldedQuarry-2`), and the derivation here joins on that same id with the same
skip-the-unassigned rule. On the suite side the seam is `run_wf` and the `has`/`hasnt_` helpers.

Recall terms used: `python tools/memory-recall/query.py "why do the synthesis blockers and highs
counts disagree with the confirmed count in disposal" --terms "tier2-review synthesis blockers highs
confirmed disposal severity promote fold mustFold raw findings adjudicated items"`.
