# TOOL-aRepatriatedFork-40 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-40

Written by the unit pass on node a, 2026-09-28. The old-extractor runs used a temp slice of the
recall selftest, its prologue plus the two new arms, inside the kit dir. The fixture kit's
`extract.py` was overwritten with the bytes `d486ea50` holds, and the slice was removed after. The
inCMS runs used read-only `git clone --local --shared` copies under the temp root. The first is at
`63439e269`, carrying the new `extract.py`, `tree_lib.py` and `gen_build_index.py`. The second is at
`905e99b68`, before the check-13 rewrite, unmodified.

**Evidences:** TOOL-aRepatriatedFork-40
- AC1 — `selftest.py` — `ok   a spec H1 anchors the id it defines, by the index generator's own predicate`. Over the d486ea50 extractor the same arm reports `the spec H1 did not anchor`, and `anchors.json` holds only the two decision-row ids
- AC2 — `selftest.py` — the same arm asserts that the journal H1 and the fenced H1 write no anchor, and that the citing file writes no record. Its detail line reads `the journal H1, the fenced H1 and the citation do not`
- AC3 — `selftest.py` — the same arm's detail reads `H1-anchored ['TOOL-aQuill-6', 'TOOL-aQuill-9'] == spec_ids`, so the extractor's H1 set equals `gen_build_index.spec_ids` over one fixture, sub-spec included
- AC4 — `selftest.py` — `ok   a query for a spec-defined id returns the defining spec's record first`, with hit 1 the spec's record and the citing file at hit 4. Over the d486ea50 extractor, hit 1 is `TOOL-aFoo-1 · memory/tooling/DECISIONS.md:3`. A one-line file's record and chunk share the fusion key and sum in `rrf`, so the sub-spec fixture carries a status line as every real spec does
- AC5 — `check-recall.py` — gov reads `normalised 0.8333 >= 0.81` and 12/12 questions resolve, as at d486ea50, and all twelve per-question hits are unchanged. `test_recall_floor.py` reads `21/21 arms green` before and after. The recall selftest reads `78/78 checks passed`, against 76/76 at d486ea50. `extract.py` over gov reads records 1201 -> 1974 documents and 734 844 -> 805 928 indexed characters, with orphan ids 433 -> 0. At inCMS `63439e269` the recall-regression leg read exit 1 before, with `ARCH-dHushedEmbargo-2 resolves to nothing`, `ARCH-aLeasedGauntlet-1 resolves to nothing` and `1610/1613 alias ids anchored`. After, it reads exit 0 with `275/275 declared targets resolve` and `1613/1613 alias ids anchored`, records_r20 0.778, records_mrr 0.457 and ensemble_fused 0.919. At `905e99b68`, unmodified, it reads records_r20 0.768, records_mrr 0.457 and ensemble_fused 0.919. `bash tools/check-kit-versions.sh` exits 0 at memory-recall 1.18 and memory-tree 2.101
