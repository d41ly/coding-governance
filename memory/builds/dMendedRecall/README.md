---
slug: dMendedRecall
node: d
opened: 2026-10-01
streams: tooling
roster: TOOL
ids: TOOL-dMendedRecall-1 TOOL-dMendedRecall-2 TOOL-dMendedRecall-3
authorized-by: slug
asks: TOOL-dAlignedCarrier-7..9
---

# dMendedRecall — the 3 filed ask(s) this build carries

## The problem this build exists to solve
Read at the working tree, each ask below is filed and live in the build that raised it, and no build's roster claims it. This build is the one that answers them: TOOL-dAlignedCarrier-7 TOOL-dAlignedCarrier-8 TOOL-dAlignedCarrier-9.

## Expected improvements
- Every ask named above has ONE build answering it, so no second build claims one.
- What done means for each is read off its own clauses and is never re-decided here.

## Detriments if this is not built
- Each ask stays live in its home build with nothing carrying it to done.
- The next run pointed at this mandate grades it and stops, because no build claims it.

## Build-level rules
- Scaffolded from the `asks:` key above; the owner's commit of this folder IS the authorization a run asserts.
- This README carries no grant key, so it grants nothing that a spec does not.
- The unattended kit's own self-test suites are WAIVED for this build's landing (owner, 2026-10-01).
  A criterion they would observe is amended citing this rule; their clean reading is owed with
  TOOL-dDerivedDocket-76. The memory-recall kit's self-test is not one of them: it runs at the close.
- Classified at kickoff (M2): all three units MISSING. Each is authored by the build harness's spec
  stage from the shared brief under `prompts/`, and built one at a time, 1 then 2 then 3.
- No spec audit and no pre-code cross-read (owner, 2026-10-01): the specs go straight to building,
  and the closing diff review is where they and the code are first reviewed.

## Parked decisions

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-dMendedRecall-1` | 2 | the memory-recall kit selftest green again in the adopter layout |
| 2 | `TOOL-dMendedRecall-2` | 2 | an in-place close that auto-files an ask commits its record with the views re-rendered |
| 3 | `TOOL-dMendedRecall-3` | 2 | the verb contract's `--status` entry names the pinned-asks and holder-worktree fields |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 3 unit(s) · node d · opened 2026-10-01 · streams tooling
ids TOOL-dMendedRecall-1 TOOL-dMendedRecall-2 TOOL-dMendedRecall-3

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dMendedRecall-1 — the recall selftest's memory-tree fixture carries the kit's python surface, and the spec-H1 arm reads only that](spec/2026-10-01-spec-TOOL-dMendedRecall-1.md) | 1 | 2 | CLOSED | rev-1 | 2026-10-01 |
| [TOOL-dMendedRecall-2 — the inherited-red auto-file re-renders the generated views it makes stale, and stages them with its rows](spec/2026-10-01-spec-TOOL-dMendedRecall-2.md) | 1 | 2 | CLOSED | rev-3 | 2026-10-01 |
| [TOOL-dMendedRecall-3 — the verb contract's `--status` entry names every field the line prints, the pinned-asks and holder-worktree verdicts among them](spec/2026-10-01-spec-TOOL-dMendedRecall-3.md) | 1 | 2 | CLOSED | rev-1 | 2026-10-01 |
<!-- /gen:build-units -->

Records: 7 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dMendedRecall-1 TOOL-dMendedRecall-2 TOOL-dMendedRecall-3.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dMendedRecall-1`, `TOOL-dMendedRecall-2`, `TOOL-dMendedRecall-3` | yes |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
