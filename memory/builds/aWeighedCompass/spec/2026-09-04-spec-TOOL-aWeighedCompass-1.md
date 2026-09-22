**Status:** CLOSED · rev-2 · 2026-09-04 · node a · Tier-1 · base c4fcf5ad · streams tooling · order 1 · ratified 2026-09-04

# TOOL-aWeighedCompass-1 — the orientation chain is measured end to end against the questions sessions actually asked

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-build-TOOL-aWeighedCompass-1-findings.md](../build/2026-09-04-build-TOOL-aWeighedCompass-1-findings.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal
Establish, by measurement rather than argument, whether this repo's five orientation instruments
compose into a working chain and whether they get a session to the right context with less
irrelevant surface. Produce one report whose every number carries the command that reproduces it,
and one backlog row per recommendation.

## 2. Scope (IN)
- The live query log at `<git-common-dir>/recall/queries.jsonl`, read as an empirical corpus: what
  sessions asked, what came back, what was emitted, and what was opened afterwards.
- `tools/memory-recall/bench.py` run over both document sets at the chunk size `query.py` actually
  serves, so the graded substrate is the substrate sessions read.
- `tools/codebase-map/reuse_lookup.py` graded against two independent ground truths: the product
  files the probing unit went on to change, and the seam that unit's own reuse audit named.
- The read-cost budget of orientation, in bytes, and the prose duplication between its carriers.
- `tools/memory-recall/extract.py` corpus statistics: anchoring, orphan ids, and the `spine` set.
- `python tools/drift-audit/drift_report.py` as a corroborating signal.

## 3. Non-goals (OUT)
- No change to any file under `tools/`, `skills/`, or the charter template. Every recommendation
  leaves this build as a backlog row and is prioritised by the owner separately.
- No new gate leg and no new merge-bar obligation.
- The `lexicon` kit, which a prior build already ruled has no input at orientation.
- Any counterfactual claim about a session that skipped the protocol. No record of such a session is
  kept, so the report bounds itself to what the instruments RETURN.

## 4. Design
Four harnesses, each written to the scratchpad and each carrying a liveness assertion, plus three
direct readings of shipped tools.

The query-log harness parses the log into its two row kinds and reports cost, redundancy and
attributed opens separately, because the first two are arithmetic over emitted bytes and the third
rests on a heuristic the kit itself flags as `inferred`.

The reuse harness is the one that needed the liveness rule. Its first cut mapped commits to ids with
a hand-rolled parse that silently found 31 of 171 cases and reported a 0% hit rate. A corrected parse
finds 503 ids, and the harness now refuses to report at all unless a probe whose right answer is
known returns that answer first.

The benchmark is run twice on purpose. The first run used the extractor's default chunk width and
produced a corpus of 18641 documents; the live index holds 43270. Only the second run, at the width
`query.py` pins, grades the corpus a session is served.

## 5. Production-readiness checklist
This unit ships no product code, so the cross-cutting menu resolves to two live items. Observability:
every harness prints its liveness verdict before its results, and refuses on a dead probe. Testing:
the report's reproduction commands are the check, and they are recorded beside each figure rather
than in a separate file.

## 6. Acceptance criteria
1. The report states a hit rate for `reuse_lookup.py` under two independent ground truths, with the
   harness and its `liveness OK` line recorded.
2. The report states `bench.py` scores for both document sets at the chunk width `query.CHUNK_MAX`
   pins, and names the substrate the live ensemble merges.
3. Every quantitative claim in the report carries the command that reproduces it.
4. Each finding is labelled `MEASURED` or `INFERRED`, and no claim resting on the `inferred` open
   events is labelled otherwise.
5. One row per recommendation lands in `memory/backlog/TOOL.md`.
6. The build folder passes the memory-hygiene leg once staged, and renders into `memory/LIVE.md`.

## 7. Gates
`bash tools/run-gates/run-gates.sh` after staging. This is a records-only change, so the kit-subject
legs guard out and the memory-tree hygiene leg is the one that binds.

## 8. Open questions
Both forks below are RESOLVED (agent, 2026-09-04): routed to a backlog row for the owner rather than
decided here. That routing IS the pick, and it is the one this unit is entitled to make — the agreed
deliverable was a research record, and both questions turn on a preference no measurement settles.

- The chunks substrate scores far below grep on the graded fixture. Three fixes are available and
  they are not equivalent: drop the set from the ensemble, re-weight the fusion toward records, or
  re-grade with a chunk-anchored fixture on the theory that the current fixture asks chunks a
  question they cannot answer. The report states the evidence for each and picks none.
  Routed to `TOOL-aWeighedCompass-4`.
- The `spine` document set extracts to zero rows here. Whether the fix belongs in the kit's `DURABLE`
  pattern or in this repo's layout depends on whether a flat memory root is the shape adopters will
  have, which is a product decision about the memory-tree kit rather than a defect report.
  Routed to `TOOL-aWeighedCompass-5`.

## 9. Revision log
- rev-1 · 2026-09-04 · first draft, written after the measurements it describes.
- rev-2 · 2026-09-04 · CLOSED. The report landed at
  `build/2026-09-04-build-TOOL-aWeighedCompass-1-findings.md` and ten backlog rows landed in
  `memory/backlog/TOOL.md`. Section 8's two open questions are recorded there as
  `TOOL-aWeighedCompass-4` and `-5` rather than resolved here, because both are owner calls.

## 10. Reuse audit
`python tools/codebase-map/reuse_lookup.py "measuring whether the orientation toolchain surfaces the
right context for a session"` returned `measure_overlap` and `measure_run` in
`tools/memory-recall/check-recall.py`, plus `test_audit_measures_chunk_targets` in
`tools/memory-recall/test_recall_floor.py`. Those are the existing measurement seam and this unit
extends them by REUSING `bench.py` and `extract.py` rather than writing a scorer. The probe also
demonstrated the defect this unit went on to measure: twelve of its candidates matched only the name
stem shared with the word "measuring".

Recall terms used: orientation kickoff recall codebase-map reuse_lookup dossier spec-template
memory-tree token cost surface irrelevant retrieval precision
