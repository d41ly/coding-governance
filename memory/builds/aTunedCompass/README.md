---
slug: aTunedCompass
node: a
opened: 2026-09-04
streams: tooling
roster: TOOL
ids: TOOL-aTunedCompass-1 TOOL-aTunedCompass-2 TOOL-aTunedCompass-3 TOOL-aTunedCompass-4 TOOL-aTunedCompass-5 TOOL-aTunedCompass-6 TOOL-aTunedCompass-7 TOOL-aTunedCompass-8
parents: aWeighedCompass
---

# aTunedCompass — the orientation chain returns the right thing, and can be measured saying so

## The problem this build exists to solve
`aWeighedCompass` measured the chain and found the value leaking in one place: the instruments are
graded on shapes no session sends. The recall fixture carries terms on 0 of 12 queries while
`query.py` refuses without them; the floor grades one document set while the CLI fuses two; the only
scorer that grades the served shape is run by nothing. Two shipped defects sit under that: `extract.py`'s
`DURABLE` still requires the pre-flatten tree, so the `spine` set is empty here and in any adopter
with a flat memory root, and `reuse_lookup.py` truncates its neighbour pool alphabetically one line
before it sorts by fan-in. Two records state facts their own sources refute.

## Expected improvements
- The one merge-bar leg that grades orientation QUALITY grades the query shape and the result shape a
  session actually gets.
- The chunk half is sourced through the rollup that measurement showed doubles its recall, which is
  the same change that collapses the duplicate slots.
- The `spine` layer stops being silently empty, here and for every adopter with a flat memory root.
- Both liveness logs record what came back, not only that something ran.

## Detriments if this is not built
- The recall floor stays green while the served configuration goes ungraded, which is the
  green-by-absence shape this repo names.
- Every session keeps paying for a chunk half nothing has priced.
- Adopters inherit an empty document set with no signal that it is empty.

## Build-level rules
- **M2 classification, recorded before acting: every unit is MISSING.** No conforming spec carries
  any of these ids at BASE; each is authored by this build and is therefore unreviewed by definition,
  so M4's spec audit is owed before any code.
- **Nothing here is built in this pass.** The units land at `SPECCED` awaiting owner scope approval.
  A Tier-2 DoR is a design pass, and approval precedes building — this build stops at the spec set.
- **Unit 1 is the only records-only unit and it corrects two documents, not one.** Both are the same
  mechanism — a record asserting a fact its own source refutes — applied to two files. Splitting one
  mechanism across two units to satisfy a document count would make the closing diff less readable,
  which is what M2's rule exists to protect.
- **Unit 2 sequences before units 3 and 4, and the reason is measurement, not taste.** Both grade or
  tune the chunk half, and every figure that would justify them was taken with terms appended by
  hand. Until the fixture carries terms, 3 and 4 would be measured against the shape this build
  exists to stop measuring against.
- **No unit re-measures what `aWeighedCompass` already recorded.** Its report is the evidence base and
  each spec cites it rather than re-deriving. A unit that needs a NEW number says so in its §8.
- **A pin this build sets is measured on this corpus and stated with its n.** Every figure behind
  these units came from a 12-question fixture; a floor set from n=12 is a floor set from noise unless
  it says so.

## Parked decisions
- **Whether the chunk set earns its place at all is NOT decided here.** `union.py` puts
  `records:fts5` alone at the same recall as the live two-set ensemble for 116% fewer snippet bytes,
  but `records` already saturates at k=20 so the fixture cannot show chunks contributing. Unit 4
  improves the set; deciding its fate needs a discriminating fixture, which is
  `TOOL-aWeighedCompass-18` and an owner call.
- **Whether to index private symbols, and whether to demote the name-stem arm**, both stay backlog
  rows (`TOOL-aWeighedCompass-13`, `-14`). Each needs its own measurement before its own design, and
  this build specs only the reuse-probe defect that is already proven at source.
- **The 261 KB backlog shard is not touched.** Rotation provably cannot fix it and the live remedy is
  a split or a curation sweep, which is an owner call carried at `TOOL-aWeighedCompass-3`.

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aTunedCompass-1` | OPEN | the two records this build's parent refuted are corrected in place |
| 2 | `TOOL-aTunedCompass-2` | OPEN | the recall fixture carries the terms every real query supplies |
| 3 | `TOOL-aTunedCompass-3` | OPEN | the recall floor grades the two-set ensemble the CLI serves |
| 4 | `TOOL-aTunedCompass-4` | OPEN | the chunk source becomes the rollup, which also de-duplicates the slots |
| 5 | `TOOL-aTunedCompass-5` | OPEN | `DURABLE` matches a flat memory root, so `spine` stops being empty |
| 6 | `TOOL-aTunedCompass-6` | OPEN | the reuse probe ranks its neighbour pool before it truncates it |
| 7 | `TOOL-aTunedCompass-7` | OPEN | the manifest declares the recall kit and narrows the tooling entrypoint |
| 8 | `TOOL-aTunedCompass-8` | OPEN | the map log records what a probe returned, not only that it ran |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 8 unit(s) · node a · opened 2026-09-04 · streams tooling
ids TOOL-aTunedCompass-1 TOOL-aTunedCompass-2 TOOL-aTunedCompass-3 TOOL-aTunedCompass-4 TOOL-aTunedCompass-5 TOOL-aTunedCompass-6 TOOL-aTunedCompass-7 TOOL-aTunedCompass-8

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aTunedCompass-1 — the two records this build's parent refuted are corrected in place](spec/2026-09-04-spec-TOOL-aTunedCompass-1.md) | 1 | 1 | SPECCED | rev-2 | 2026-09-05 |
| [TOOL-aTunedCompass-5 — `DURABLE` matches a flat memory root, so `spine` stops being empty](spec/2026-09-04-spec-TOOL-aTunedCompass-5.md) | 1 | 2 | SPECCED | rev-2 | 2026-09-05 |
| [TOOL-aTunedCompass-6 — the reuse probe ranks its neighbour pool before it truncates it](spec/2026-09-04-spec-TOOL-aTunedCompass-6.md) | 1 | 2 | SPECCED | rev-2 | 2026-09-05 |
| [TOOL-aTunedCompass-7 — the manifest declares the recall kit and narrows the tooling entrypoint](spec/2026-09-04-spec-TOOL-aTunedCompass-7.md) | 1 | 1 | SPECCED | rev-1 | 2026-09-04 |
| [TOOL-aTunedCompass-2 — the recall fixture carries the terms every real query supplies](spec/2026-09-04-spec-TOOL-aTunedCompass-2.md) | 2 | 2 | SPECCED | rev-2 | 2026-09-05 |
| [TOOL-aTunedCompass-8 — the map log records what a probe returned, not only that it ran](spec/2026-09-04-spec-TOOL-aTunedCompass-8.md) | 2 | 2 | SPECCED | rev-2 | 2026-09-05 |
| [TOOL-aTunedCompass-3 — the recall floor grades the two-set ensemble the CLI serves](spec/2026-09-04-spec-TOOL-aTunedCompass-3.md) | 3 | 2 | SPECCED | rev-2 | 2026-09-05 |
| [TOOL-aTunedCompass-4 — the chunk source becomes the rollup, which also de-duplicates the slots](spec/2026-09-04-spec-TOOL-aTunedCompass-4.md) | 3 | 2 | SPECCED | rev-1 | 2026-09-04 |
<!-- /gen:build-units -->

Records: 0 bound to this build, across 1 record folder(s).

Ids no record names: TOOL-aTunedCompass-1 TOOL-aTunedCompass-2 TOOL-aTunedCompass-3 TOOL-aTunedCompass-4 TOOL-aTunedCompass-5 TOOL-aTunedCompass-6 TOOL-aTunedCompass-7 TOOL-aTunedCompass-8.

Ids no `spec-audit` record has ever named: TOOL-aTunedCompass-1 TOOL-aTunedCompass-2 TOOL-aTunedCompass-3 TOOL-aTunedCompass-4 TOOL-aTunedCompass-5 TOOL-aTunedCompass-6 TOOL-aTunedCompass-7 TOOL-aTunedCompass-8.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aTunedCompass-1`, `TOOL-aTunedCompass-5`, `TOOL-aTunedCompass-6`, `TOOL-aTunedCompass-7` | yes |
| 2 | `TOOL-aTunedCompass-2`, `TOOL-aTunedCompass-8` | yes |
| 3 | `TOOL-aTunedCompass-3`, `TOOL-aTunedCompass-4` | yes |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [aWeighedCompass](../aWeighedCompass/README.md)
<!-- /gen:build-edges -->
