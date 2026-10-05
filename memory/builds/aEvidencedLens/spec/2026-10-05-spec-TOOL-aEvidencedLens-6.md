# TOOL-aEvidencedLens-6 — the review returns a per-lens yield over defect clusters, unique defects counted

**Status:** SPECCED · rev-3 · 2026-10-05 · node a · Tier-2 · base 028b5cac · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-prompt-TOOL-aEvidencedLens-1-1-spec-brief.md](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-1-1-spec-brief.md) | journal | TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-4 TOOL-aEvidencedLens-5 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-8 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-10 TOOL-aEvidencedLens-11 |
| [2026-10-05-prompt-TOOL-aEvidencedLens-6-2-build-brief.md](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-6-2-build-brief.md) | journal | — |
| [2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md](../reviews/2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md) | spec-audit | TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-4 TOOL-aEvidencedLens-5 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-8 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-10 TOOL-aEvidencedLens-11 |

<!-- /gen:spec-records -->

## 1. Goal

Nobody can tell which review lens earns its cost, because the harness counts findings per RUN and
never per LENS. The ledger already carries every finding's lens and verdict, and the synthesis's
`items` already group confirmed raw ids into adjudicated defects, so the per-lens figures are a
derivation over data the harness holds. This unit derives `lensYield`, one row per lens that ran,
and scores each lens on the DEFECTS it found and the ones only it found, not on its raw count.

## 2. Scope (IN)

- **S1** — `tools/workflows/tier2-review.template.js` gains `deriveLensYield(rows, items)`, which
  returns one row per key in `runningLensKeys`, in dispatch order. A row carries `lens`, `returned`
  (the lens's agent came back, its file reused or freshly written), `raw`, `confirmed`, `refuted`,
  `uncertain`, `unverified`, `precision`, `defects` and `unique`. `unverified` counts every finding
  with neither a confirmed nor a refuted verdict and so includes `uncertain`, exactly as the run-level
  return counts them; `raw = confirmed + refuted + unverified`. Observed by AC1 and AC2.
- **S2** — `precision` is `confirmed / (confirmed + refuted)`, and `null` when both are 0. The run-level
  `precision` keeps its 0 placeholder; the per-lens figure does not copy it, because a 0 beside a lens
  nobody judged reads as a measured failure. Observed by AC2.
- **S3** — `defects` is the number of synthesis items holding at least one CONFIRMED id whose finding
  came from this lens. `unique` is the number of items holding at least one confirmed id whose every
  confirmed id came from this lens. Items are read exactly as the tally reads them: a severity outside
  the closed four skips its item, and an id that is not confirmed is ignored. Observed by AC1 and AC3.
- **S4** — `defects` and `unique` are `null` on every row when no item list can be trusted: no
  synthesis ran, the synthesis died, or the tally fault fired (a confirmed id in no item or in two).
  The tally refuses to guess a split for `blockers`, and this unit refuses for the same reason.
  Observed by AC3 and AC4.
- **S5** — `lensYield` is on EVERY return of the harness, so a caller never tests for its presence.
  The two exits before the verify stage carry rows whose counts are what exists there (a dead lens a
  row with `returned: false` and zeros); every path past the verify stage carries the ledger-derived
  counts. Observed by AC4 and AC5.
- **S6** — The counts known before the synthesis, `raw` to `precision`, with `returned`, reach the
  synthesis prompt as a VERBATIM block rendered by `renderLensYield(rows)`, a markdown table the
  synthesis is told to copy into the report directly after its review-shape sentence. `defects` and
  `unique` are derived after the synthesis returns, so they are returned and logged and never in the
  report. Observed by AC6.
- **S7** — Every path that returns `lensYield` logs it as one `lens yield:` line per row, through
  `printLensYield(rows)`. Observed by AC6.
- **S8** — Both kinds. The block is a synthesis-prompt input and a return field; no lens or skeptic
  prompt moves on either kind, and `REVIEW_SHAPE` and `inputPrint` do not move, because neither the
  lens files nor the verify files a review key guards change. Observed by AC7.
- **S9** — `tools/workflows/README.md`'s return-field list, which says every return carries three
  fields beside the counts, names `lensYield` as the fourth with its row shape and the null rule of S4.
  Observed by AC8.
- **S10** — `tools/workflows/tier2-review.test.sh` gains arms for S1 to S7 and the light-run case of
  AC9. NOT OBSERVED inside the pass, because shared invariant 9 keeps suites out of passes; the
  `New arm:` lines in §7 declare them and the suite runs once at `VERIFYING`.

## 3. Non-goals (OUT)

- Any change to a lens or skeptic prompt, a lens catalogue, the evidence rule or the round brief.
  Those are units 1 to 4 of this build.
- A per-lens figure in the RECORD's appendix. The appendix is a contract `review_replay.py` parses by
  header name, and the ledger's `lens` column already lets a reader count per lens.
- Recording `lensYield` anywhere durable. It is a return field; a caller that wants it kept writes it
  down, as with `ledger`.
- Moving `REVIEW_SHAPE`. Shared invariant 5 moves it once, in unit 1, and this unit changes nothing a
  review key guards.
- A precision floor per lens, or any verdict drawn from the numbers. This unit measures; deciding which
  lens to keep is the owner's.
- A kit version bump. The main loop bumps once at the close (shared invariant 7).

### Edges

- **hands-off** `TOOL-aEvidencedLens-13` — the cumulative observation that no diff-kind probe, lens
  or skeptic prompt moved from BASE through this unit, compared with the review key masked; AC7 here
  observes only this pass's own step.

## 4. Design

### Evidence

Read at base `028b5cac`, which is `origin/main` at preflight; the run branch's later commits touch only
`memory/builds/aEvidencedLens/`.

- Every finding carries `lens`, the dispatched key, from `allFindings` at
  `tools/workflows/tier2-review.template.js:810`. The ledger at `:1034` keeps it per row beside
  `verdict`.
- `confirmed`, `refuted`, `unverified` and `uncertainFindings` are derived at `:979` to `:985`, with
  `unverified` holding `uncertain`.
- The synthesis returns `items: [{severity, ids}]` (schema at `:1291`). The tally at `:1319` to `:1353`
  reads them: unknown severity skips the item, a non-confirmed id is ignored, and a missing or repeated
  confirmed id sets `tallyFault` and nulls `blockers` and `highs`.
- `runningLensKeys` at `:537` excludes the lenses a light run skips; `finderResults` at `:752` is
  indexed like `LENSES`, and a null entry is a dead lens.
- There are FIVE returns: every lens dead (`:823`), no finding raised (`:843`), every finding refuted
  (`:1086`), a partial fan deferred (`:1113`), and the final return (`:1379`), which also covers a dead
  synthesis.
- Prior art: `TOOL-aSightedSkeptic-8` §3 listed "a per-lens yield summary line or table" as a non-goal
  and said "the ledger carries every value it would be derived from". This unit is that derivation.

### Data model

```js
// one row per runningLensKeys entry, dispatch order
{ lens: 'coherence', returned: true, raw: 4, confirmed: 2, refuted: 1, uncertain: 1, unverified: 1,
  precision: 0.67, defects: 2, unique: 1 }      // defects/unique: null when S4 applies
```

`deriveLensYield(rows, items)` takes the ledger rows (or `[]` before the verify stage) and the
synthesis items (or `null`). It reads `finderResults` and `skippedLenses` for `returned`, never
`verdictById`, so the two early exits can call it before `verdictById` exists.

```text
| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 4 | 2 | 1 | 1 | 1 | 0.67 |
```

The block reaches the prompt between marker lines, as the appendix does, with the instruction to copy
it verbatim directly after the review-shape sentence. The copy is not verified, as the appendix's is
not; the return holds the exact rows.

The log line, per row: `lens yield: <lens> returned <yes|no> · raw r · confirmed c · refuted f ·
uncertain u · unverified v · precision <p|-> · defects <d|-> · unique <q|->`.

### Inventory

| Name | Cell | Kind |
|---|---|---|
| `deriveLensYield` | `js.function` | new function |
| `renderLensYield` | `js.function` | new function |
| `printLensYield` | `js.function` | new function |
| `lensYield` | return field | new key on every return |

All three names were checked with `python tools/lexicon/lexicon.py --suggest <name> --as js.function` and
answered OK.

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/README.md`

The render is regenerated by the parity tool's `--render` form in the same commit, never hand-edited
(shared invariant 1).

### Alternatives rejected

- **Counting `unique` by raw finding rather than by item.** Two lenses confirming one defect are two
  raw findings and one item; a raw-finding count credits both as unique, which is the inflation the
  owner's fifth improvement point names.
- **`defects` and `unique` in the synthesis prompt.** They need the synthesis's own items, so they can
  only exist after it returns.
- **Precision 0 when nothing was judged, to match the run-level field.** The run-level field logs
  "the number is a placeholder" beside it; a per-lens row has no such sentence, and `null` is the
  stated absence this file already uses for `blockers`.

## 5. Production-readiness checklist

- security — no new input, no new write path; the block is built from the harness's own counters and
  the lens keys, which are literals.
- perf / scale — one pass over the ledger and one over the items; no agent, no spawn.
- error / empty / loading states — every return carries the field; a dead lens is a row marked
  `returned: false`; an untrusted item list nulls `defects` and `unique` rather than guessing.
- observability — one log line per lens on every return, and the verbatim block in the report.
- risks — the synthesis may not copy the block, as it may not copy the appendix; the return is the
  source of record and the README says so.
- testing — stub runs of the render (§6); the suite arms run once at `VERIFYING`.
- migration — none: a new return field, absent in no caller's contract today.
- user docs — `tools/workflows/README.md`'s return-field list (S9).

## 6. Acceptance criteria

Every stub-run criterion below evaluates the RENDER `tools/workflows/tier2-review.js` with `node`, in
the `runReview` AsyncFunction shape of the review harness's self-test, copied into a scratch script
under the run's scratch directory and run there, never by running the suite. Its `ALL_OK` doubles
give each of the five diff lenses one finding.

- **AC1** — When the stub runs the diff kind with every verdict `confirmed` and a synthesis placing
  each id in its OWN item, the return's `lensYield` has 5 rows with `raw` 1, `confirmed` 1,
  `precision` 1, `defects` 1 and `unique` 1 each; with one item holding all five ids, every row reads
  `defects` 1 and `unique` 0.
  Red when: `unique` counts raw findings, so the shared item credits every lens.
- **AC2** — When the stub returns `refuted` for one lens's finding and `uncertain` for another's, the
  first row reads `refuted` 1, `precision` 0 and `defects` 0, and the second reads `uncertain` 1,
  `unverified` 1 and `precision` `null`.
  Red when: an unjudged lens reads `precision` 0, or `unverified` excludes `uncertain`.
- **AC3** — When the synthesis double leaves one confirmed id out of every item, the run logs the tally
  WARNING and every `lensYield` row carries `defects` `null` and `unique` `null` while `confirmed`
  stays an integer.
  Red when: a split is guessed over an item list the tally refused.
- **AC4** — When the synthesis double returns `null`, the final return's `lensYield` carries the
  ledger counts and `null` for `defects` and `unique`; when one lens double returns `null`, the
  deferred return carries that lens's row with `returned` `false`.
  Red when: a dead synthesis or a dead lens drops `lensYield` or drops the dead lens's row.
- **AC5** — When every lens double returns no finding, separately when every verdict is `refuted`,
  and separately when every lens double returns `null`, each return carries `lensYield` with one row
  per running lens; in the all-dead run every row reads `returned` `false` with zero counts.
  Red when: an early exit, the every-lens-dead exit included, returns no `lensYield` key.
- **AC6** — When the stub runs the spec kind with `SPEC` args, carrying the `scratch` that
  `TOOL-aEvidencedLens-2` makes required there, the `synth` prompt carries the marker
  lines and one table row per running lens with its `precision`, and the run log carries one
  `lens yield:` line per lens naming `defects` and `unique`.
  Red when: the block or a log line is missing for a lens that ran.
- **AC7** — When the diff-kind `find:` and `verify:` prompts of one stub run are compared against the
  same stub run of the pass-start render, every one is byte-identical, and the return's `key` is
  identical.
  Red when: a lens or skeptic prompt moved, or the review key moved.
  fixture: the pass-start render is the `git show` of `tools/workflows/tier2-review.js` at HEAD taken
  before the pass edits anything, saved to the scratch directory. The comparison is to this unit's
  predecessor and not to BASE, because `TOOL-aEvidencedLens-1` moved the review key every
  DURABILITY line carries, so a BASE render differs on a correct build.
- **AC8** — When `grep -n lensYield tools/workflows/README.md` runs, it prints the field's line naming
  `defects`, `unique` and the `null` rule, and `grep -c 'carries three fields' tools/workflows/README.md`
  prints 0.
  Red when: the README still says every return carries three fields.
- **AC9** — When the stub runs the diff kind with `intensity: 'light'`, `lensYield` carries a row for
  each running lens and none for a skipped one.
  Red when: a skipped lens appears as a row of zeros, read as a lens that found nothing.

## 7. Gates

`tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `verifier fan-out self-test` · `review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/tier2-review.test.sh · a synthesis placing all five ids in one item, which a raw-finding `unique` credits five times · `FLOOR_ASSERTIONS` raised by the assertions added
New arm: tools/workflows/tier2-review.test.sh · a tally fault, under which a guessed split reads as data · `FLOOR_ASSERTIONS` raised by the assertions added
New arm: tools/workflows/tier2-review.test.sh · a dead lens and a dead synthesis, each of which a missing row would hide · `FLOOR_ASSERTIONS` raised by the assertions added
New arm: tools/workflows/tier2-review.test.sh · every return site, the no-finding, every-refuted and every-lens-dead exits included, returning no `lensYield` key · `FLOOR_ASSERTIONS` raised by the assertions added

## 8. Open questions

- **F1 — Do the counts known before the synthesis reach the report as a verbatim block, with
  `defects` and `unique` returned only?** The alternative is a return field only, which leaves the
  durable record with no per-lens figure at all. The brief recommends the split.
  RESOLVED (agent, 2026-10-05, delegated): the split, S6 — the block carries what exists before the
  synthesis, and the two figures that need its items are returned and logged.
- **F2 — Does a lens that died get a row?** Omitting it makes a dead lens indistinguishable from one
  that was never dispatched; a row of zeros makes it read as a lens that found nothing.
  RESOLVED (agent, 2026-10-05, delegated): a row with `returned: false`, S1 and AC4.

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, from the spec brief's unit 6 and the template read at
  `028b5cac`.
- rev-2 · 2026-10-05 · §3 §7 §10 S6 AC5 AC7 AC8 · round-1 spec audit fold. Id 1 (MEDIUM): AC7's
  fixture is the pass-start render, and the criterion says why BASE is excluded. Id 11 (MEDIUM): AC5
  adds the every-lens-dead exit. Id 12 (LOW): AC8 asserts the "carries three fields" sentence is
  gone. Id 30 (LOW, its unit-6 half): §7's arms raise `FLOOR_ASSERTIONS` by the assertions added.
  Id 35 (LOW): S6 no longer calls six counts four. Id 49 (LOW): §10 cites `TOOL-aWeldedTribunal-4`
  as the built precedent. §3 gains the hands-off edge to `TOOL-aEvidencedLens-13`, the unit the
  same defect's HIGH, id 25, was promoted to.
- rev-3 · 2026-10-05 · S7 §4 Inventory · build pass. The five return sites each log the rows, so the
  log line is one function, `printLensYield(rows)`, rather than five copies of its template; S7 names
  it and the inventory carries it as a third new function, checked with the lexicon like the other two.

## 10. Reuse audit

The seam extended is the ledger `TOOL-aSightedSkeptic-8` built in
`tools/workflows/tier2-review.template.js`, read beside the synthesis `items` the `TOOL-dMergedTally-1`
tally already parses; `deriveLensYield` reads both with the tally's own rules and adds no second
parser. `python tools/codebase-map/reuse_lookup.py "per-lens yield of a review: confirmed, refuted
and unique defects per lens"` returned no per-lens seam (its JavaScript hits were name-stem matches
such as `deriveReviewKey`), and `grep -rn -i "lensYield\|per-lens"` over `tools/` found only
`review_replay.py`'s candidate-side per-lens line, which scores recall against a past record and is
not a per-run yield. The recall query's hits were `TOOL-aSightedSkeptic-8`, whose §3 deferred exactly
this derivation, and `TOOL-dTieredTribunal-16`, the open ask for run counters in the synthesis
prompt. The built precedent S6 follows is `TOOL-aWeldedTribunal-4`, which shipped the RUN INTEGRITY
block (`tools/workflows/tier2-review.template.js:1164`) that answered that ask.

Recall terms used: `python tools/memory-recall/query.py "is there a per-lens precision or yield measure of review lenses" --terms "lens precision yield confirmed refuted unique defect synthesis items ledger appendix tier2-review spec-audit"`
