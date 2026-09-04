---
slug: aWeighedCompass
node: a
opened: 2026-09-04
streams: tooling
roster: TOOL
ids: TOOL-aWeighedCompass-1 TOOL-aWeighedCompass-2 TOOL-aWeighedCompass-3 TOOL-aWeighedCompass-4 TOOL-aWeighedCompass-5 TOOL-aWeighedCompass-6 TOOL-aWeighedCompass-7 TOOL-aWeighedCompass-8 TOOL-aWeighedCompass-9 TOOL-aWeighedCompass-10 TOOL-aWeighedCompass-11 TOOL-aWeighedCompass-12 TOOL-aWeighedCompass-13 TOOL-aWeighedCompass-14 TOOL-aWeighedCompass-15 TOOL-aWeighedCompass-16 TOOL-aWeighedCompass-17 TOOL-aWeighedCompass-18 TOOL-aWeighedCompass-19
---

# aWeighedCompass — measuring whether the orientation toolchain actually orients

## The problem this build exists to solve
This repo ships five instruments whose shared purpose is getting an agent to the right context fast:
the memory tree, `memory-recall`, `codebase-map`, the spec template, and the reuse-audit obligation.
Each is individually gated. Nothing measures the CHAIN. `tools/memory-recall/check-recall.py` grades
one substrate against a twelve-question fixture; `gen_map.py --check` byte-compares generated
artifacts; hygiene check 12 grades spec SHAPE. Every one of those asks whether an artifact is
well-formed, and none asks whether a session that used it ended up better oriented. The evidence to
answer that already exists and had never been read: `<git-common-dir>/recall/queries.jsonl` holds
148 real queries with what each returned, and 170 specs record the literal reuse phrase their author
probed with, which is a ground truth for the map half.

## Expected improvements
- The chain's real hit rates are numbers rather than assumptions, reproducible by a recorded command.
- The half of every recall result set that is measurably dead weight is identified and priced.
- A retrieval layer that has been structurally empty since the memory tree flattened is found.
- Recommendations are ranked by cost-removed over effort instead of by which tool felt worst.

## Detriments if this is not built
- The orientation kits keep being tuned against fixtures rather than against the questions sessions
  actually ask, and a floor stays green while live retrieval degrades.
- Every session keeps paying ~14 KB per recall query and ~11 KB per reuse probe with no idea what
  fraction of that is signal.
- Adopters inherit the same unmeasured chain, including a document set that extracts to zero rows in
  any repo with a flat memory root.

## Build-level rules
- **Every number in the report carries the command that produced it.** A figure without a
  reproduction is not a finding here, it is an opinion with a decimal point.
- **Liveness before verdict.** Each measurement harness first probes a case whose right answer is
  known and REFUSES if that case does not hit. The first cut of the reuse harness reported 0/12 and
  was wrong; a broken harness and a broken tool return the same number.
- **MEASURED and INFERRED are labelled separately, per finding.** The `opened` half of the query log
  is heuristic attribution by the kit's own declaration, and any claim resting on it says so on the
  same line.
- **"Nothing exercises this" is a different finding from "this is broken."** They have different
  fixes, and collapsing them is how a working tool gets rewritten.
- **This build changes nothing under `tools/`.** Recommendations leave as backlog rows. The research
  and the remediation are separate units so the owner prioritises the second after reading the first.

## Parked decisions
- **The chunks substrate's floor is a design question, not a bug report.** Its graded score is
  MRR 0.008 against grep's 0.167, but the fixture's expected documents are record-anchored, so a
  600-char slice is a structurally harder target than a whole record. The grep comparison is
  same-task and stands; the absolute number is not a verdict on the substrate's design. Which of
  the three available fixes to take is the owner's.
- **No instrument exists for the counterfactual.** Nothing here measures a session that skipped the
  protocol against one that followed it, because no such record is kept. Every efficacy claim in
  the report is therefore about what the tools RETURN, never about what a session did next.

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aWeighedCompass-1` | OPEN | the orientation chain is measured end to end against the questions sessions actually asked |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 1 unit(s) · node a · opened 2026-09-04 · streams tooling
ids TOOL-aWeighedCompass-1 TOOL-aWeighedCompass-2 TOOL-aWeighedCompass-3 TOOL-aWeighedCompass-4 TOOL-aWeighedCompass-5 TOOL-aWeighedCompass-6 TOOL-aWeighedCompass-7 TOOL-aWeighedCompass-8 TOOL-aWeighedCompass-9 TOOL-aWeighedCompass-10 TOOL-aWeighedCompass-11 TOOL-aWeighedCompass-12
ids TOOL-aWeighedCompass-13 TOOL-aWeighedCompass-14 TOOL-aWeighedCompass-15 TOOL-aWeighedCompass-16 TOOL-aWeighedCompass-17 TOOL-aWeighedCompass-18 TOOL-aWeighedCompass-19

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aWeighedCompass-1 — the orientation chain is measured end to end against the questions sessions actually asked](spec/2026-09-04-spec-TOOL-aWeighedCompass-1.md) | 1 | 1 | CLOSED | rev-2 | 2026-09-04 |
<!-- /gen:build-units -->

Records: 1 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aWeighedCompass-1.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aWeighedCompass-1` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
