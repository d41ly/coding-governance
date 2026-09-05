---
slug: aTunedCompass
node: a
opened: 2026-09-04
streams: tooling
roster: TOOL
ids: TOOL-aTunedCompass-1 TOOL-aTunedCompass-2 TOOL-aTunedCompass-3 TOOL-aTunedCompass-4 TOOL-aTunedCompass-5 TOOL-aTunedCompass-6 TOOL-aTunedCompass-7 TOOL-aTunedCompass-8 TOOL-aTunedCompass-9 TOOL-aTunedCompass-10 TOOL-aTunedCompass-11
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
- **The FIRST pass built nothing** — the units landed at `SPECCED` awaiting owner scope approval,
  because a Tier-2 DoR is a design pass and approval precedes building. That approval has since
  happened: it is the restructure recorded three bullets down. The unattended run of 2026-09-05
  carries the build from there, so this rule is history rather than a live constraint, and it is
  reworded rather than deleted because the sentence "nothing here is built in this pass" read as
  binding on every later pass.
- **The roster below carries no Status column, and that is deliberate.** Status is DERIVED — the
  generated region a few lines down renders it from the spec headers. The authored roster held a
  Status cell per row until the round-1 audit found eight of the eleven disagreeing with the
  generated table in the same file. One fact in one place; a column that cannot exist cannot go
  stale.
- **Unit 1 is the only records-only unit and it corrects two documents, not one.** Both are the same
  mechanism — a record asserting a fact its own source refutes — applied to two files. Splitting one
  mechanism across two units to satisfy a document count would make the closing diff less readable,
  which is what M2's rule exists to protect.
- **RESTRUCTURED at scope approval, under M3.** Twelve forks went to the owner; eleven are answered
  and unit 3's second stays open with the unit it belongs to. Three units were ADDED: 9 builds the
  discriminating fixture that 2 and 3 are now BLOCKED on, 10 takes the predicate narrowing that would
  have made 6 two mechanisms, 11 lands the reader 8 is blocked on. Unit 4 moved to order 1 on the
  de-duplication result, which the query log measures without any fixture. Each resolution is a
  RESOLVED mark in its own spec, never restated here.
- **No unit re-measures what `aWeighedCompass` already recorded.** Its report is the evidence base and
  each spec cites it rather than re-deriving. A unit that needs a NEW number says so in its §8.
- **This build sets no floor.** The owner blocked pinning on unit 9 rather than derive one from a
  saturated 12-question fixture. A figure quoted anywhere here carries its n.

- **WHAT THE UNATTENDED RUN OF 2026-09-05 BUILT, and what it did not.** Seven units CLOSED: 1, 4,
  5, 6, 7, 8, 10. Unit 11 is IMPLEMENTED and committed but its spec stays `SPECCED`, because its
  verification did not complete — see the next rule. Units 2, 3 and 9 are UNBUILT: 2 and 3 are
  blocked on 9, and 9 is the largest single piece in the build, so starting it without finishing it
  would have left a half-authored fixture that `TOOL-aTunedCompass-3` is due to pin the merge bar
  against. The run stopped building rather than start it. Unit 9's spec gained a measured candidate
  pool at rev-5 so the next run does not rediscover it.
- **UNIT 11 IS UNVERIFIED, and this is the run's largest caveat.** Its reader, its six declaration
  carriers and its record corrections are committed, and `unattended kit gate`, `memory hygiene`,
  `spec tokens`, `dead paths`, `kit version markers`, `install prefix`, `lexicon` and wiring are all
  green over it. What did NOT run is the kit's own driver suite, which carries the three new MAP_CLI
  arms and eight existing arms this unit re-worded. Two attempts were made; each produced ZERO
  output and was killed at its bound, one at 50 minutes and one at 90. A pristine-tree baseline
  behaved identically for the first 100 seconds, so the silence is buffering rather than a hang
  introduced here — but that is not the same as knowing the suite passes, and the difference is why
  the spec is not CLOSED. The one live exercise the run did get is its own `--close`, which
  evaluates `reuse-probed` against this tree with both CLIs declared and both logs present.
- **The spec audit ran TWO rounds and exited NON-CONVERGENT.** Round 1 over all eleven specs: 20
  distinct defects, 3 blockers. Round 2 over the three that carried a blocker: 16 defects, 2
  blockers, and fifteen of the sixteen were created by round 1's own fold. The count did not
  strictly shrink, so M4 stops the loop; both standing blockers were FOLDED, and the disposition is
  recorded on the exiting round. Precision was 0.47 in both rounds.

## Parked decisions
- **Whether the chunk set earns its place at all is still NOT decided.** `union.py` puts
  `records:fts5` alone at the same recall as the live two-set ensemble for 116% fewer snippet bytes,
  but `records` saturates at k=20 so the fixture cannot show chunks contributing. Unit 9 builds the
  fixture that could; the owner blocked units 2 and 3 on it rather than pin a floor against
  saturation. The set's fate is a decision for after unit 9 reports.
- **Whether to index private symbols stays a backlog row** (`TOOL-aWeighedCompass-13`). Its
  measurement is its own, and unit 10 narrows the neighbour predicate without touching what the index
  admits. The name-stem arm (`-14`) is likewise untouched: unit 10 changes which candidates are
  NEIGHBOURS, never which are SEEDS.
- **The 261 KB backlog shard is not touched.** Rotation provably cannot fix it and the live remedy is
  a split or a curation sweep, which is an owner call carried at `TOOL-aWeighedCompass-3`.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aTunedCompass-1` | the two records this build's parent refuted are corrected in place |
| 2 | `TOOL-aTunedCompass-2` | the recall fixture carries the terms every real query supplies |
| 3 | `TOOL-aTunedCompass-3` | the recall floor grades the two-set ensemble the CLI serves |
| 4 | `TOOL-aTunedCompass-4` | the chunk source becomes the rollup, which also de-duplicates the slots |
| 5 | `TOOL-aTunedCompass-5` | `DURABLE` matches a flat memory root, so `spine` stops being empty |
| 6 | `TOOL-aTunedCompass-6` | the reuse probe ranks its neighbour pool before it truncates it |
| 7 | `TOOL-aTunedCompass-7` | the manifest declares the recall kit and narrows the tooling entrypoint |
| 8 | `TOOL-aTunedCompass-8` | the map log records what a probe returned, not only that it ran |
| 9 | `TOOL-aTunedCompass-9` | a recall fixture that can tell the two-set ensemble from its records half |
| 10 | `TOOL-aTunedCompass-10` | the neighbour predicate selects a pool a cap can meaningfully bound |
| 11 | `TOOL-aTunedCompass-11` | the map log gains the run-state reader a closed unit's acceptance claimed |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** BLOCKED · 11 unit(s) · node a · opened 2026-09-04 · streams tooling
ids TOOL-aTunedCompass-1 TOOL-aTunedCompass-2 TOOL-aTunedCompass-3 TOOL-aTunedCompass-4 TOOL-aTunedCompass-5 TOOL-aTunedCompass-6 TOOL-aTunedCompass-7 TOOL-aTunedCompass-8 TOOL-aTunedCompass-9 TOOL-aTunedCompass-10 TOOL-aTunedCompass-11

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aTunedCompass-1 — the two records this build's parent refuted are corrected in place](spec/2026-09-04-spec-TOOL-aTunedCompass-1.md) | 1 | 1 | CLOSED | rev-2 | 2026-09-05 |
| [TOOL-aTunedCompass-4 — the chunk source becomes the rollup, which also de-duplicates the slots](spec/2026-09-04-spec-TOOL-aTunedCompass-4.md) | 1 | 2 | CLOSED | rev-4 | 2026-09-05 |
| [TOOL-aTunedCompass-5 — `DURABLE` matches a flat memory root, so `spine` stops being empty](spec/2026-09-04-spec-TOOL-aTunedCompass-5.md) | 1 | 2 | CLOSED | rev-3 | 2026-09-05 |
| [TOOL-aTunedCompass-6 — the reuse probe ranks its neighbour pool before it truncates it](spec/2026-09-04-spec-TOOL-aTunedCompass-6.md) | 1 | 2 | CLOSED | rev-5 | 2026-09-05 |
| [TOOL-aTunedCompass-7 — the manifest declares the recall kit and narrows the tooling entrypoint](spec/2026-09-04-spec-TOOL-aTunedCompass-7.md) | 1 | 1 | CLOSED | rev-2 | 2026-09-05 |
| [TOOL-aTunedCompass-9 — a recall fixture that can tell the two-set ensemble from its records half](spec/2026-09-04-spec-TOOL-aTunedCompass-9.md) | 1 | 2 | SPECCED | rev-5 | 2026-09-05 |
| [TOOL-aTunedCompass-10 — the neighbour predicate selects a pool a cap can meaningfully bound](spec/2026-09-04-spec-TOOL-aTunedCompass-10.md) | 2 | 2 | CLOSED | rev-3 | 2026-09-05 |
| [TOOL-aTunedCompass-11 — the map log gains the run-state reader a closed unit's acceptance claimed](spec/2026-09-04-spec-TOOL-aTunedCompass-11.md) | 2 | 2 | SPECCED | rev-3 | 2026-09-05 |
| [TOOL-aTunedCompass-2 — the recall fixture carries the terms every real query supplies](spec/2026-09-04-spec-TOOL-aTunedCompass-2.md) | 2 | 2 | BLOCKED | rev-4 | 2026-09-05 |
| [TOOL-aTunedCompass-3 — the recall floor grades the two-set ensemble the CLI serves](spec/2026-09-04-spec-TOOL-aTunedCompass-3.md) | 3 | 2 | BLOCKED | rev-3 | 2026-09-05 |
| [TOOL-aTunedCompass-8 — the map log records what a probe returned, not only that it ran](spec/2026-09-04-spec-TOOL-aTunedCompass-8.md) | 3 | 2 | CLOSED | rev-4 | 2026-09-05 |
<!-- /gen:build-units -->

Records: 8 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aTunedCompass-1`, `TOOL-aTunedCompass-4`, `TOOL-aTunedCompass-5`, `TOOL-aTunedCompass-6`, `TOOL-aTunedCompass-7`, `TOOL-aTunedCompass-9` | yes |
| 2 | `TOOL-aTunedCompass-10`, `TOOL-aTunedCompass-11`, `TOOL-aTunedCompass-2` | yes |
| 3 | `TOOL-aTunedCompass-3`, `TOOL-aTunedCompass-8` | yes |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [aWeighedCompass](../aWeighedCompass/README.md)
<!-- /gen:build-edges -->
