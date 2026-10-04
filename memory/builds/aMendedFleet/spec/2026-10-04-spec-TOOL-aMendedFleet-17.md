# TOOL-aMendedFleet-17 — `tier2-review.js` keeps each finding's bug-class label in the committed appendix

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-2 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 17

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Every Tier-2 review hands its finders the project's bug-class checklist, labels each class `C<n>`,
and tells a finder to begin a hit's claim with that label. The claim then rides only the returned
ledger, and the appendix the synthesis copies into the committed record carries eight columns with
no class in them. So no record says which classes a review actually caught, and the checklist can
never be ranked or pruned by its hits. This unit resolves each finding's labels to the class names
the run was handed and writes them into a ninth appendix column, `classes`, so hit counts accrue in
the records from the next review on. Report `[B#4]`, brief unit 17.

## 2. Scope (IN)

- **S1** — A top-level pure function `extractFindingClasses(claim, items)` in
  `tools/workflows/tier2-review.template.js` reads the run of `C<n>` labels at the head of a claim
  and returns the class name each one denotes, in order, without duplicates. A label is `C` and
  digits, optionally in square brackets, optionally followed by a colon or comma; labels are read
  only at the head, so a `C3` inside the claim's prose is not one. Label `n` denotes the run's
  checklist item `n`. The class name is that item's first whitespace-delimited token after an
  optional `[ ]` or `[x]` box, when the token is a lowercase slug; otherwise, and for an `n` outside
  the item list, the name is the label itself, `C<n>`, which no slug can spell. Observed by AC1.
- **S2** — Every ledger entry gains `classes`, the array S1 returns for its claim over the parsed
  checklist items, empty when the claim carries no label or the run had no checklist. Observed by AC1
  and AC2.
- **S3** — `renderAppendix` renders `classes` as a ninth column after `fixVerdict`, its cell the names
  joined by one space and `-` when the array is empty, through the same `renderCell` escaping. The
  eight existing columns keep their names, order and cell rules. Observed by AC2 and AC3.
- **S4** — The edit is made in `tools/workflows/tier2-review.template.js` and the render
  `tools/workflows/tier2-review.js` is regenerated from it with the kit's own render command, never
  edited by hand. Observed by AC4.
- **S5** — The kit README's return-field paragraph names `classes` on the ledger and the ninth
  appendix column, and says that an unresolved label is kept as `C<n>`. Observed by AC5.
- **S6** — The committed review record carries the column, because the synthesis already copies the
  appendix verbatim. NOT OBSERVED by this unit: only a live review writes a record, and this build's
  closing diff review is the first one that will.

## 3. Non-goals (OUT)

- Counting hits across records, and pruning or demoting classes nobody's review ever caught. The
  report names that as the step after this one; it needs the counts this unit starts to accrue.
- Ranking or cutting the checklist itself. That is `TOOL-aMendedFleet-16`, which changes which items
  `gotchas.py --for-diff` selects, not the item shape this unit reads.
- A `claim` column in the appendix. `TOOL-aSightedSkeptic-8` refused it (its §8 F4): free text is the
  cell most likely to break a row of the table `review_replay.py` parses, and this unit leaves that
  ruling standing.
- The two drift-audit harnesses. They take no checklist, so they have no label to keep.
- Moving `REVIEW_SHAPE`. It keys the reuse of lens files written by the lens and skeptic prompts, and
  this unit changes neither a prompt nor a schema.
- The machine shape line with severity counts and output tokens: `TOOL-aMendedFleet-18`, which edits
  the same file and so builds after this unit.

### Edges

- **consumes-from** external — the gotchas checklist item shape, a `[ ]` box then the class slug as
  the first token. A future reshape degrades S1's names to their `C<n>` labels rather than to wrong
  slugs, because a token that is not a lowercase slug is never taken for one.

## 4. Design

### Evidence

Read at base `7af5f564`, re-verified 2026-10-04 against the report's claim at `ac65de998`.

- `deriveChecklistShares` hands item `n` to one lens and the lens block prints it as `C<n> <item
  text>`, ending with the instruction to begin a hit's claim with its `C<n>` label.
- The ledger entry built just above `renderAppendix` carries `claim`, and `renderAppendix` renders the
  eight columns `id lens ref severity skepticSeverity verdict reason fixVerdict`. The label therefore
  survives only in the returned ledger and in the lens files under `<git-common-dir>/review-lenses/`.
- Five committed records carry the appendix today (the aBatchedMinors, aHalvedInstall,
  aSightedSkeptic and two aWindowedPass closing diff reviews), and none carries a class column.
- Across the seven review keys stored on node a, 37 of 188 finder claims open with a label. Head
  spellings seen: `C34:`, `C5 <slug>`, `C10 <prose>`. PINNED, measured 2026-10-04 with a regex over
  `find-*.json`; the report's figure was 37 of 98 at `ac65de998`, before later reviews added findings.
- `python tools/memory-tree/gotchas.py --for-diff` prints each item as `- [ ] <slug>` or `- [ ] <slug>
  (universal)`, then the description and the gotcha's path on continuation lines; `parseChecklist`
  strips the `- ` and keeps the continuations inside the item.
- `review_replay.py` finds appendix columns by header name and refuses only a missing one, so a
  ninth column is read past.

### Data model

One ledger entry, the addition marked:

```
{ id, lens, ref, severity, skepticSeverity, verdict, reason, fixVerdict, claim,
  classes: ["<slug>" | "C<n>", ...] }          # S2, [] when no label
```

The appendix header after this unit:

```
| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
```

### Inventory

- `extractFindingClasses`, a top-level function so a `node` slice can evaluate it alone. `extract` is
  the declared verb for pulling a declared shape out of a larger one. A name the lexicon leg refuses
  is replaced with its `--suggest` answer at build time, and this list is amended with a rev bump.

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`
- `tools/workflows/README.md`

### Rollout

Additive to the return and the record. The review key does not move, so a re-run of an earlier review
reuses its lens files and only its appendix gains the column. `TOOL-aMendedFleet-18` writes the same
template and therefore builds after this unit, never beside it. The review-harness kit version bump is
owed once, at this build's close.

### Alternatives rejected

- **Keep the raw `C<n>` label in the column.** It is an ordinal of one run's checklist, so `C5` names
  a different class in every review and no count over records means anything.
- **Ask the finder schema for a `classes` field.** It changes the finder prompt and schema, which moves
  `REVIEW_SHAPE` and discards every stored lens file, and the label convention already carries the
  same fact.
- **Read the slug out of the claim's prose.** Finders sometimes echo it after the label and mostly do
  not; the item list is the authority the run itself built.

## 5. Production-readiness checklist

- security — a claim is agent text, so the cell passes through `renderCell`'s pipe and line-break
  escaping like every other cell, and a name is only ever a slug or a `C<n>` label.
- perf / scale — one regex per finding over at most a few hundred findings.
- error / empty / loading states — no checklist, or no label, renders `-`; an out-of-range label
  renders `C<n>` rather than vanishing.
- observability — the column is the observation; it is what makes a class's hits countable.
- risks — a finder that omits its label still loses the class. The column measures that rate too.
- testing — a node slice over fixture claims and items, a replay compatibility probe, and a new arm
  in the harness's own suite at the close.
- migration — none. Older records keep eight columns and the replay reads both.
- user docs — the kit README's return-field paragraph, S5.

## 6. Acceptance criteria

- **AC1** — When `node -e` slices the `extractFindingClasses` function out of
  `tools/workflows/tier2-review.js` and evaluates it over the items `[ ] alpha-one (universal)`,
  `[ ] beta-two` and `[ ] gamma-three`, the claims `C2 — x`, `[C1] C3: y`, `C3, C3 z`, `no label`,
  `see C2 later` and `C9 out of range` return `[beta-two]`, `[alpha-one, gamma-three]`,
  `[gamma-three]`, `[]`, `[]` and `[C9]`.
  Red when: any label resolves to the wrong item, a head label is dropped, a duplicate is kept, or a
  mid-claim `C2` is read as a label.
- **AC2** — When the same `node -e` slice evaluates `renderCell` and `renderAppendix` over two ledger
  rows, one with `classes` `[alpha-one, gamma-three]` and one with `[]`, the header line reads the
  eight existing columns then `classes`, the first row's last cell is `alpha-one gamma-three`, and
  the second's is `-`.
  Red when: the column is absent, out of position, or an empty array renders anything but `-`.
- **AC3** — When `python tools/workflows/review_replay.py --known` names
  `memory/builds/aWindowedPass/reviews/2026-10-04-review-TOOL-aWindowedPass-1-2-3-4-5-closing-diff-round1.md`
  and `--candidate` names a scratchpad copy of that record whose appendix gains a ninth `classes`
  column, the replay scores every known finding matched and exits 0.
  Red when: the replay refuses the nine-column table or matches fewer than all.
  fixture: the copy is made in the run's scratchpad; the known record is tracked today.
- **AC4** — When `node tools/workflows/check-workflow-syntax.js` runs after the render, it exits 0, and
  `grep -c extractFindingClasses` over `tools/workflows/tier2-review.template.js` and
  `tools/workflows/tier2-review.js` reports the same non-zero count for both.
  Red when: the render was skipped, so the two counts differ, or the render does not parse.
- **AC5** — When `grep -n classes tools/workflows/README.md` runs, the return-field paragraph names the
  ledger's `classes` field, the ninth appendix column and the `C<n>` fallback.
  Red when: the paragraph still says the appendix has eight columns.

## 7. Gates

`workflow script syntax` · `review-protocol parity (kit vs dogfood)` · `tier2-review self-test` · `verifier fan-out self-test` · `unattended-build self-test` · `review-join self-test` · `review-replay selftest` · `lexicon naming predicates`

New arm: tools/workflows/tier2-review.test.sh · an appendix arm whose ledger carries labelled and unlabelled claims, asserting the nine-column header and the `classes` cells; the existing header pin moves to nine columns · the suite's assertion floor rises by the arms added

## 8. Open questions

- **F1 — What does the column record: the run's `C<n>` label, or the class it denotes?**
  Options: the raw label, which needs no item lookup; the class slug, resolved through the run's own
  item list. Only the slug is the same string across two reviews, which is the whole point of
  counting hits.
  RESOLVED (agent, 2026-10-04, delegated): the slug, with the label kept verbatim only where no slug
  can be resolved.
- **F2 — Where does the column sit?**
  Options: beside `lens`, where it reads naturally; last, after `fixVerdict`. The replay reads by
  header name either way, but the harness's own suite pins the header bytes and a reader scanning by
  position finds the eight columns where they were.
  RESOLVED (agent, 2026-10-04, delegated): last.
- **F3 — Should the claim gain its own column alongside?**
  Options: yes; no, as `TOOL-aSightedSkeptic-8` ruled. The slug is the countable fact and is never
  free text.
  RESOLVED (agent, 2026-10-04, delegated): no.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from `deriveChecklistShares`, the ledger and `renderAppendix` at
  base, and the stored lens files on node a.

## 10. Reuse audit

The seams extended are the ledger map and `renderAppendix` in
`tools/workflows/tier2-review.template.js`, with `parseChecklist`'s item list as the class authority
and `renderCell` as the escaping. `python tools/codebase-map/reuse_lookup.py "keep a finding's bug
class label in the review record appendix"` returned `records` in `tools/memory-tree/gotchas.py` and
the runlog record writers, none of which reads a review appendix, so no existing seam fits the
label-to-class join. The map's symbol tier does hold `renderAppendix` and `deriveChecklistShares`,
but the behaviour phrase did not reach them, so the harness seams were found by reading the template. Recall returned the report row this unit implements, `TOOL-aSightedSkeptic-4`'s
spec (where the `C<n>` convention was decided) and that build's closing review, whose M1 finding is
why the replay counts raw appendix rows. The report said 37 of 98 labelled findings; node a's stored
lens files now say 37 of 188.

Recall terms used: tier2-review appendix ledger checklist C<n> label class gotchas hit counts finder claim review_replay
