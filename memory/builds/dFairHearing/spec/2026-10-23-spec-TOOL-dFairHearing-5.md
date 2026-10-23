# TOOL-dFairHearing-5 — duplicates counted as merged confirmations, the orphan check on both kinds

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 6 · advances TOOL-dFairHearing-19

**Carries:** cl-dClosedLoop-0072@4afd6a04 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md) | research | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |
| [2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md](../reviews/2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md) | spec-audit | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |

<!-- /gen:spec-records -->

## 1. Goal

A skeptic's refutation that names a confirmed survivor in its own batch as the original, `duplicate of
id=<n>`, is counted as a merged confirmation in the review's precision and its verified counts, not as
a refutation; and the orphan-duplicate check, which demotes a duplicate whose original is not a
confirmed survivor, runs on the diff kind as it does on the spec kind. Today the 15 duplicates in 50
reports count as refuted, putting pooled precision at 0.866 against 0.880 merged, and the orphan check
is spec-only (`gap-review-08`; PINNED 2026-10-15,
`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-review-adjudication.md:43-46`).
It is a metric fix: no verdict, item or disposal moves (that record's candidate 2, :92-95).

## 2. Scope (IN)

- **S1** — `extractDuplicateTarget(reason)`, the one reading of the duplicate reason form, in the
  prelude of `tools/workflows/tier2-review.template.js`, used by the orphan check, the merged count and
  the lens yield. Observed by AC1.
- **S2** — the orphan check at template :1470-1487 loses its `isSpec` guard, and its RUN INTEGRITY
  clause (template :1777-1778) prints on both kinds. Observed by AC4.
- **S3** — the diff skeptic's prompt (template :1399) gains the `duplicate of id=<n>` reason form the
  spec skeptic's case (5) already carries (template :1395). Observed by AC5.
- **S4** — `merged`: every finding refuted with a duplicate reason that survived the orphan check.
  It leaves `refuted`, joins precision's numerator and denominator, and is counted in the verified
  counts, the review-shape line, every return carrying `refuted`, the verify log line, RUN INTEGRITY,
  the synthesis's review-shape sentence and the lens yield. The finding's verdict, the confirmed set
  and the synthesis items do not move. Observed by AC2, AC3, AC6.
- **S5** — `REVIEW_SHAPE` reads a value other than base's `lenses5-r3` once this unit lands, so no
  verify file judged under the old diff skeptic prompt is reused. Observed by AC7.
- **S6** — the carriers that state the shape line, the lens yield row or the precision formula:
  `tools/workflows/README.md` and the review protocol, template and render. Observed by AC8.
- **S7** — the suite arms the `New arm:` line in §7 declares. Observed by AC1, AC2, AC3, AC4, AC5,
  AC6 through that line, RED-first at the close.

## 3. Non-goals (OUT)

- No change to any verdict. A merged duplicate keeps `verdict: 'refuted'` and its reason in the
  ledger and the appendix, which are the skeptic's record; the count reads it from that reason.
- No merged duplicate in `confirmed`, `confirmedFindings`, the synthesis's CONFIRMED list or its items,
  so `blockers`, `highs` and the disposal they drive are unchanged.
- No merge of a `duplicate of prior <ref>` refutation: its original is a previous round's finding,
  raised and fixed, not a survivor of this run, so it stays refuted.
- No address key: the check's whole test is membership of the same batch and the original's verdict,
  and §8 F3 settles why this unit calls none.
- No change to the agreeing repeat-verdict counter `duplicates` (template :1452, :1459), a different
  fact that keeps its name.
- No duplicate handling in the drift-audit harnesses: the clause names the review's.
- No help page: no page under `help/` describes the review harness.
- No kit version moved: the lander mints them (`tools/push-main.sh:26-32`).

### Edges

- **hands-off** `TOOL-dFairHearing-7` — a `merged` duplicate already names its original, so it is no
  twin to flag, and the pairs that unit hands the synthesis leave it out
- **hands-off** `TOOL-dFairHearing-23` — finding id 35 of the round-1 spec audit: the key-pinning arms of units 2, 3 and 9 that this spec's `REVIEW_SHAPE` bump moves, re-derived from the current template (its S29, AC20)

## 4. Design

### The reason form, read once

```js
const DUPLICATE_REASON = /^duplicate of id=(\d+)/i
function extractDuplicateTarget(reason) {
  const m = DUPLICATE_REASON.exec(String(reason || '').trim())
  return m ? Number(m[1]) : null
}
```

Defined in the prelude, beside `TOOL-dFairHearing-4`'s address functions, so a slice reaches it. It
replaces the inline regex of the orphan check (template :1481), whose pattern and trim it keeps.

### The orphan check on both kinds

The loop at template :1475-1487 runs for either kind. A refutation whose reason names id `n` is an
orphan when `n` is its own id, is not in its batch, or does not stand confirmed after the conflict
demotion (template :1469), exactly as today on the spec kind. An orphan leaves `verdictById`, so it is
UNVERIFIED with the ledger reason `duplicate of an unconfirmed id` (template :1597). The RUN INTEGRITY
clause at template :1777-1778 drops its `isSpec ?` branch, and the comment above the check loses "spec
kind only". The diff kind's prompt bytes move here, which the comment at template :1777 records as
the reason for the old branch.

### The diff skeptic's duplicate form

The diff kind's verdict sentence (template :1399) keeps its four refutation words and adds one
sentence: a DUPLICATE opens `reason` with `duplicate of id=<n>` for another finding in this batch that
the skeptic CONFIRMS in the same answer. Without it a diff skeptic writes free text and nothing it
refutes as a duplicate can be read as one.

### The merged count

After the orphan demotion (template :1487):

```js
const merged = allFindings.filter((f) => verdictById.get(f.id)?.verdict === 'refuted' &&
  extractDuplicateTarget(verdictById.get(f.id).reason) !== null)
```

and `refuted` (template :1513) excludes every `merged` id. Every finding is then in exactly one of
`confirmed`, `merged`, `refuted` and `unverified`, so `raw` is their sum. Then:

- `judged` (template :1521) is `confirmed + merged + refuted`, and `precision` is
  `(confirmed + merged) / judged`, still `0` with nothing judged. Over the 50-report corpus this reads
  987 / 1122 = 0.880, the record's merged figure, where removing duplicates from the denominator
  instead would read 0.878.
- `verifiedCounts` (template :1639-1640) gains `merged`, and `renderShapeLine` (template :78-83) prints
  `merged=<n|->` after `refuted=`, so a stage that has not produced it prints `-`.
- Every return that carries `refuted` carries `merged` beside it (template :1668-1670, :1700-1701,
  :2025-2033). On the all-refuted path it is always 0, since a merged duplicate needs a confirmed
  original.
- The verify log line (template :1559-1564) and the synthesis's review-shape sentence (template :1755)
  state `merged`, and RUN INTEGRITY states `<n> duplicate refutation(s) counted as merged
  confirmations`.
- The lens yield reads the same fact from the ledger: `deriveLensYield` (template :1256-1277) counts a
  row as `merged` when its verdict is `refuted` and `extractDuplicateTarget(row.reason)` is not null.
  An orphan's ledger row reads `unverified`, so the predicate selects exactly the `merged` set. Each row
  gains `merged`, its `precision` becomes `(confirmed + merged) / (confirmed + merged + refuted)`, and
  `unverified` is `raw` less all three. `renderLensYield` and `printLensYield` (:1280-1292) add the
  column after `refuted`.

The name is `merged` because `duplicates` already counts agreeing repeat verdicts.

### The review key

`REVIEW_SHAPE` (template :970) stands for the prompts a keyed file was judged under, and its comment
says a later prompt change moves it (template :961-966). The diff skeptic's prompt moves here. When the
build's tip at this pass still reads `lenses5-r3`, this unit sets `lenses5-r4`; when an earlier unit of
this build already moved it, this unit leaves it, so the build moves it once, as the review system
record's change list asks (`2026-10-15-build-PLAY-dClosedLoop-1-review-system.md:199-200`).

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `extractDuplicateTarget` | function, `tools/workflows/tier2-review.template.js` | `js.function`, OK |
| `DUPLICATE_REASON` | constant, same file | none |
| `merged` | constant, a return field, a verified count, a shape-line field and a lens-yield column | none |

The function name was asked of `python tools/lexicon/lexicon.py --suggest extractDuplicateTarget --as
js.function` and answered OK.

### Migration

None. Records already written keep their stated precision; a re-derivation reads `merged` from the
appendix as the lens yield does, a refuted row whose reason opens `duplicate of id=`.

### Rollout

Live on landing, not dark: the brief's S9 names units 2, 4, 7 and 8, and this change moves a figure,
never a verdict.

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`, its render
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/README.md`: the review-shape grammar (:291), the lens-yield row fields and its
  precision formula (:318-322)
- `tools/workflows/REVIEW-PROTOCOL.template.md`: the precision sentence at :217
- `memory/guides/REVIEW-PROTOCOL.md`, its render

The renders come from `bash tools/workflows/check-protocol-parity.test.sh --render`. The suite's arm
asserting that a diff-kind duplicate is not scanned (`tools/workflows/tier2-review.test.sh:1637-1643`)
inverts, and its shape-line arms gain the field.

### Alternatives rejected

- **A merged duplicate counted as confirmed.** It would enter the synthesis's CONFIRMED list, so the
  item tally would have to place it and `blockers`, `highs` and the disposal would move: the research
  measured that no verdict, item or disposal should.
- **A merged duplicate dropped from the denominator.** Precision would read 0.878 over the corpus, not
  the merged confirmation the record measured at 0.880.
- **A new ledger verdict `merged`.** It would rewrite the skeptic's verdict in the record and add a
  value to the appendix's verdict column that every reader of it would have to learn.

## 5. Production-readiness checklist

- security — no new write path, no new input. The reason is parsed by one anchored regex.
- perf / scale — one more filter over the raw findings; no agent.
- error / empty / loading states — nothing judged still prints precision `0` with its placeholder
  note; a stage before verify prints `merged=-`; an orphan is demoted and named on both kinds.
- observability — `merged` is in the shape line, the log, RUN INTEGRITY and the lens yield, so a
  report states how much of its precision is merged.
- risks — precision rises by the merged share, +0.013 pooled and +0.03 to +0.07 per report where
  duplicates exist (the research record, :44), which can carry a round across the review protocol's
  0.5 floor in the passing direction; a diff run's duplicates were never orphan-checked before, so a
  diff report can now show unverified findings it did not.
- testing — the pass probes S1 by a prelude slice and S2 to S4 by a stub-agent run on each kind; the
  suite arm in §7 is observed RED then GREEN by the main loop at the close.
- migration — none, as §4 Migration says.
- user docs — none owed: no page under `help/` describes the review harness.

## 6. Acceptance criteria

- **AC1** — When a scratch node probe evaluates the prelude of `tools/workflows/tier2-review.js`, cut
  as `tools/workflows/tier2-review.test.sh:67-81` cuts it and returning `extractDuplicateTarget` as
  `tools/workflows/tier2-review.test.sh:237` returns a function, it reads `duplicate of id=4` as 4,
  `  Duplicate of id=12: same claim` as 12, and `duplicate of prior a.js:3`, `dup of id=4`, an empty
  string and `undefined` each as `null`.
  Red when: the regex loses its `i` flag, so `Duplicate of id=12` reads as `null`.
- **AC2** — When a scratch stub-agent run of `tools/workflows/tier2-review.js`, shaped as
  `tools/workflows/tier2-review.test.sh:333-357` with five lenses of two findings each, so ids 1 and 2
  share a batch, has every finding confirmed but id 2, refuted as `duplicate of id=1`, the return reads
  `confirmed` 9, `merged` 1, `refuted` 0 and `precision` 1, its `shape` carries `refuted=0 merged=1`,
  and the lens-yield row of the lens owning id 2 reads `merged` 1 and `precision` 1. This holds on a
  diff review and on a spec audit.
  Red when: `merged` stays inside `refuted`, so the diff run reads `refuted` 1 and precision 0.90.
  cost: a scratch runner of about 60 lines, modelled on that suite's stubs.
- **AC3** — When the AC2 runs end, the ledger row of id 2 reads `verdict` `refuted` and `reason`
  `duplicate of id=1`, and the appendix row of id 2 reads the same. A refutation of id 2 reading
  `duplicate of prior a.js:3` returns `merged` 0 and `refuted` 1.
  Red when: the merged row's verdict is rewritten, so the appendix no longer records the skeptic's
  refutation.
- **AC4** — When the AC2 runner hands a diff review id 2 refuted as `duplicate of id=3`, an id in
  another batch, and again with id 1 refuted `r` and id 2 refuted as `duplicate of id=1`, each run's
  ledger row 2 reads `unverified` with reason `duplicate of an unconfirmed id`, a `WARNING:` log line
  names `ids 2`, and the synthesis prompt's RUN INTEGRITY carries `1 orphaned duplicate refutation(s)
  demoted to unverified`.
  Red when: the `isSpec` guard stays, so the diff run keeps row 2 `refuted`, as the base arm at
  `tools/workflows/tier2-review.test.sh:1637-1643` observes.
- **AC5** — When the AC2 diff run's verify prompts are read from its trace, every one carries
  `duplicate of id=<n>`.
  Red when: the sentence is added on the spec branch only.
- **AC6** — When the AC2 diff run ends with a synthesis stub placing every CONFIRMED id the prompt
  lists, `confirmedFindings` and the prompt's CONFIRMED list both lack id 2, the tally raises no fault,
  and `blockers` and `highs` equal the counts over the nine confirmed ids.
  Red when: `merged` ids join `confirmed`, so `confirmed` reads 10 and `confirmedFindings` carries
  id 2.
- **AC7** — When `grep -n "^const REVIEW_SHAPE" tools/workflows/tier2-review.template.js` runs at
  this unit's build commit, the value it prints is not `lenses5-r3`.
  Red when: the diff skeptic prompt moves and the literal stays at base's value, so a verify file
  judged under the old prompt keeps a reusable key.
- **AC8** — When `grep -n 'merged=<n|->'` runs over `tools/workflows/README.md`, it finds the
  review-shape grammar line, and `grep -n 'confirmed + merged'` finds the README's lens-yield precision
  formula, the precision sentence of `tools/workflows/REVIEW-PROTOCOL.template.md` and that of
  `memory/guides/REVIEW-PROTOCOL.md`.
  Red when: the shape line gains the field and the README's grammar still lists `refuted=<n|->`
  followed by `unverified=<n|->`.

## 7. Gates

`tier2-review self-test` · `verifier fan-out self-test` · `unattended-build self-test` · `review-join self-test` · `review-join ban (no ref-keyed join)` · `review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `harness arms (fail branches armed or pinned)` · `testsuite counts (every bar self-test prints one)` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/tier2-review.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 · the base harness, which counts a same-batch duplicate as refuted, skips the orphan check on a diff review and gives the diff skeptic no duplicate form · FLOOR_ASSERTIONS in that suite, raised by the arms added

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that a
  legal status?** Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:28`, joined by the header
  regex at `tools/memory-tree/tree_lib.py:377`. Observation, 2026-10-23: `DRAFT` is not in the set, so
  a `DRAFT` header parses as no header and the unit reads MISSING. Liveness: the tuple would carry it
  if the vocabulary admitted it. RESOLVED (agent, 2026-10-23, delegated): `OPEN`, the token
  `memory/TEMPLATE-SPEC.md` gives a spec in drafting.
- **F2 — What does "counted as a merged confirmation" move?** Options: (a) a separate `merged` count
  that leaves `refuted` and joins precision's numerator, the confirmed set untouched; (b) the duplicate
  joins `confirmed`; (c) the duplicate leaves the denominator. (b) moves the items and the disposal,
  which the research measured as unmoved; (c) reads 0.878 over the corpus, not the 0.880 the review
  system record states (`2026-10-15-build-PLAY-dClosedLoop-1-review-system.md:85-86`, :221).
  RESOLVED (agent, 2026-10-23, delegated): (a), by rung 1, the design record's figure.
- **F3 — The brief's S4 says this unit calls `deriveAddressKey`; does it?** The orphan check decides by
  batch membership and the original's verdict, and a duplicate names its original by id, so no address
  enters. Calling the key would add a reading that decides nothing. RESOLVED (agent, 2026-10-23,
  delegated): no call; the brief's reader list for S4 is `TOOL-dFairHearing-7` and
  `TOOL-dFairHearing-18`, by rung 3.
- **F4 — Editing the review protocol's precision sentence changes a governance carrier; does the
  build's grant cover it?** `PLAY-dClosedLoop-3` grants the carrier changes a build's own clauses name;
  this clause moves the precision figure, and clause `cl-dClosedLoop-0077` names
  `tools/workflows/REVIEW-PROTOCOL.template.md` as a record this build brings back in line with the
  code. RESOLVED (agent, 2026-10-23, delegated): covered, rung 3.
  grants: PLAY-dClosedLoop-3 the precision sentence in tools/workflows/REVIEW-PROTOCOL.template.md and its render memory/guides/REVIEW-PROTOCOL.md

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, from the packet's Items 5, the review system record's
  duplicates-ride-with-batching paragraph, and the verify-stage tally read at base `3708a705`.
- rev-2 · 2026-10-23 · §3 · the round-1 spec audit's disposal: hands-off edges to TOOL-dFairHearing-23, naming each finding the promoted unit closes on this spec and the criterion of its own it supersedes, if any.

## 10. Reuse audit

The seams extended are the verify stage's own tally: the orphan check (`tools/workflows/tier2-review.template.js:1470-1487`),
the verdict partition and precision (:1512-1522), `verifiedCounts` and `renderShapeLine` (:1639-1644,
:78-83) and `deriveLensYield` (:1256-1292). The one new function replaces an inline regex rather
than adding a second reading of it. `python tools/codebase-map/reuse_lookup.py "count a duplicate
refutation as a merged confirmation in review precision"` ranked name stems (`counts`, `merge`,
`measure_typed_counts`, `derive_review_verdict` in `tools/runlog/model.py`) and named no seam in the
review harness, so the seams were found by reading the source. `python tools/memory-recall/query.py`
returned the brief's row, the review system record's change paragraph, review 63's owed arm for a
diff-kind orphan (`memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-review-system-a.md:167`),
and `TOOL-aEvidencedLens-3`'s criterion that a diff run's duplicate is not scanned. That last agrees
with source at base (the suite's arm at :1637-1643) and is the behaviour this unit inverts.

Recall terms used: duplicate refutation orphan check precision merged confirmation skeptic batch spec kind diff kind
