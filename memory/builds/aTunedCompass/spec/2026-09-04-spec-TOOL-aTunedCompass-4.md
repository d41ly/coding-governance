# TOOL-aTunedCompass-4 — the chunk source becomes the rollup, which also de-duplicates the slots

**Status:** SPECCED · rev-1 · 2026-09-04 · node a · Tier-2 · base c4fcf5ad · streams tooling · order 3

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Serve the chunk half of `tools/memory-recall/query.py` through the best-chunk-per-parent rollup that
`bench.py` already implements and nothing runs. Two findings converge on the one change: the rollup
is the only chunk substrate that beats grep once queries carry terms, and best-chunk-per-parent is
the same mechanism that collapses the repeated paths filling half of every result set.

## 2. Scope (IN)

- **S1** — a `run_rollup` in `query.py` that takes a ranked list of chunk hits and keeps the first
  hit per parent, capped at `k`. The parent key is `hit["id"] or hit["path"]`, which is what
  `bench.parent_of` computes for a chunk once the extraction has been through `meta`.
- **S2** — the chunk arm of the fusion pulls `k * ROLLUP_DEPTH` hits and rolls them up to `k`, while
  the records arm is untouched. `ROLLUP_DEPTH` is declared beside `CHUNK_MAX` with a comment naming
  the `k * 8` literal inside `run_rollup` at `tools/memory-recall/bench.py` (`:135`) as the value it
  mirrors.
- **S3** — both call sites of the fusion change together. `query.py` builds the same pair twice, on
  the first attempt and again after a `sqlite3.DatabaseError` forces a cache rebuild, and a rollup
  applied to only one of them makes the served shape depend on whether the cache was healthy.
- **S4** — the ranking rationale block in the module docstring of `query.py` gains a bullet stating
  that the chunk arm is rolled up, why, and what it costs. That block exists so the served
  configuration cannot drift from the instrument, and it is where the correction to `run_rollup`'s
  own stale advice belongs, because `bench.py` is byte-pinned in `verbatim.json`.
- **S5** — the FORKED header of `query.py` names the new construct. It currently says six constructs
  are edited and the rest is upstream's byte for byte, and a re-pull is a three-way merge against
  that list.
- **S6** — the measurement that settles §8's F1 is run and its result recorded in the unit's build
  record, whichever way it comes out. The unit does not land on an assumption about the ensemble.
- **S7** — a corpus-independent arm in `tools/memory-recall/selftest.py`: over a synthetic fixture
  where one anchored record holds several matching chunks, the served result set carries that record
  at most once from the chunk source, and a second record's chunk is present. The arm is observed
  RED against the pre-change code before it is wired.
- **S8** — the duplicate-slot rate is measured before and after over the fixture questions, from the
  `shown_paths` field the log already writes, and the delta is recorded with the unit.

## 3. Non-goals (OUT)

- Not editing `tools/memory-recall/bench.py`. It is byte-pinned in `verbatim.json` and asserted by
  `selftest.py`, and its stale advice is corrected where the served configuration is described.
- Not changing `rrf()`'s key. A per-path cap inside the fusion was the other shape row 4 of the
  findings offered, and it would also drop legitimately distinct record hits; the rollup removes the
  cause at the source instead.
- Not rolling up the records arm. `bench.parent_of` returns a record's own id, so the operation is a
  no-op there and the extra query depth would be paid for nothing.
- Not adding a flag to serve the un-rolled chunk arm. `bench.py` and `union.py` already grade both
  substrates, and that is where the comparison belongs.
- Not deciding whether the chunk half belongs in the served ensemble. The build README parks that on
  a discriminating fixture and an owner call.
- Not changing `DEFAULT_BUDGET`. The emitted set stays a byte-budget prefix of the fused list.
- Not a new gate leg. `memory-recall kit selftest` already runs the arm's home.

## 4. Design

### Why this depends on unit 2

Every figure justifying this change was measured with terms appended by hand to a fixture that
carries none. With terms at the live chunk width, `chunks:roll` scores recall@20 of about 0.33
against `chunks:fts5` at about 0.17 and grep at 0.17, and it is the only chunk substrate that beats
grep. On the bare question both sit at 0.08. `TOOL-aTunedCompass-2` puts the terms in the fixture;
before it lands, any measurement here grades a query shape `query.py` refuses to serve.

### The parent key, verified at source

`_write_set` in `query.py` writes `meta.id` as the document's `id` or its `rec`, and `extract_chunks`
gives a chunk a `rec` naming the anchored record it sits inside. So for a chunk hit, `hit["id"]` is
already the parent record id, and `hit["id"] or hit["path"]` is `bench.parent_of` expressed over the
row shape `search()` returns. The two cannot be a single function: `bench.run_rollup` takes the
in-memory `docs` list and a `bench.build_index` connection, while `query.py` serves dictionaries
joined against its own `meta` table.

### What the fallback costs, stated rather than discovered

A chunk sitting in no anchored record has an empty `meta.id`, so it collapses on its path. A large
document carrying no anchored records therefore contributes exactly one chunk slot to the fused
pool, however many of its sections match. That is a real loss of within-file diversity, and it is
the same fallback the measured 0.33 was measured under, so the number already prices it.

### The claim this unit must not inherit

`run_rollup`'s docstring says rollup is worth "+0.04 to +0.05 on CHUNK-ONLY retrieval, and exactly
+0.000 once the records set is in the ensemble", and advises against expecting it to move a two-set
ensemble. That was measured on the bare question. The terms-carrying re-measurement puts chunk-only
rollup far above the quoted band, at about +0.16 over `chunks:fts5` at recall@20, so the first half
of the sentence is stale for the served query shape. The second half is NOT refuted and is also not
confirmed: with terms at `k=20`, `records:fts5` alone already reaches recall 1.000 on this fixture,
so `records:fts5+chunks:fts5` and `records:fts5+chunks:roll` both read 1.000 because there is no
headroom left to move. An equal pair under saturation is an absence of evidence.

### What settles it

Run `union.py` against the terms-carrying fixture at a `k` where `records:fts5` alone scores below
1.000, and compare the two ensembles there. If they stay equal wherever headroom exists, the
docstring's ensemble claim holds for the served shape and this unit's value is the de-duplication
alone, which S8 measures independently. If the rollup ensemble scores higher, the advice is stale
for the served shape as well and the change buys recall too. Both outcomes are recorded; neither is
assumed. This is AC4 and AC5.

### Files touched (estimate)

`tools/memory-recall/query.py` and `tools/memory-recall/selftest.py`, plus
`memory/map/features/memory-recall.md` for the dossier prose refresh a touch owes. The kit version
constant in `recall_conf.py` bumps with the body change, in every carrier the govkit stamp check
names.

### Migration

None. The rollup is applied at query time to rows already in the cache, so extraction and the index
schema are unchanged and `CACHE_VERSION` does NOT bump. Bumping it would force every node to rebuild
an index whose bytes are identical.

### Alternatives rejected

- **Rolling up in SQL with a `GROUP BY` over the parent key.** It would need `bm25()` inside an
  aggregate, and a Python loop over eight times `k` rows is boring, obviously correct, and cheap.
- **Capping hits per path inside `rrf()`.** It attacks the symptom across both sets and would also
  thin the records arm, where each hit is already a distinct record.
- **Extracting a shared rollup into `bench.py` for both callers.** That file is byte-pinned and
  re-pulled wholesale from upstream, and the two callers do not share a row shape anyway.
- **Waiting for the discriminating fixture before changing anything.** The de-duplication value does
  not depend on that fixture, and the rollup is already implemented and already graded.

## 5. Production-readiness checklist

- security — N/A. The query path still writes nothing inside the worktree.
- perf / scale — the chunks SELECT returns eight times as many rows, each carrying `d.body` up to
  `CHUNK_MAX` characters, so about 160 rows at the default `k`. It is one extra in-process SQLite
  read against a warm local index. The build measures the CLI's wall clock before and after rather
  than asserting the cost is negligible.
- a11y — N/A. No user-facing surface.
- i18n — N/A. No user-facing strings.
- error / empty / loading states — a chunks database that matches nothing still returns an empty
  list, and the rollup over an empty list is an empty list. The `PARTIAL RECALL` notice for a
  missing document set is unchanged.
- observability — `n_hits` and `shown_paths` keep their meaning, and S8's before-and-after reads
  from `shown_paths` rather than from a new field.
- risks — the within-file diversity loss described in §4 is the real one, and it is bounded by the
  measurement that already prices it. A second risk is asserting the ensemble result instead of
  measuring it, which S6 and AC5 exist to prevent.
- testing + left-shift gates — S7 and S8, with the arm's red observed before it is wired.
- migration / rollback — no cache version bump, no index change, and the diff is confined to one
  helper and two call sites, so a revert is a revert.
- user docs — the rendered Skill describes the CLI's arguments and not its substrates, so it is
  unchanged. The module docstring is the carrier per S4.

## 6. Acceptance criteria

- **AC1** — When a question is served whose chunk matches concentrate in one anchored record, the
  `shown_paths` field of the new row in the recall query log carries that record's path at most once
  from the chunk source, where the same question at base `c4fcf5ad` carried it repeatedly.
- **AC2** — When `python tools/memory-recall/selftest.py` runs, the new S7 arm passes, and the arm
  was seen RED against the pre-change `query.py` before it was wired.
- **AC3** — When the fixture questions are replayed through
  `python3 tools/memory-recall/query.py` before and after the change, the duplicate-path rate over
  `shown_paths` falls, and both rates are recorded with the unit rather than quoted from the parent
  build's 54.5 percent.
- **AC4** — When `python tools/memory-recall/bench.py <data-dir> tools/memory-recall/recall-fixture.json
  --sets chunks --subs fts5,roll --ks 5,10,20` runs against the terms-carrying fixture at
  `--chunk-max 600`, `roll` scores above `fts5` at recall@20, reproducing the parent build's figure
  on a fixture that now carries the terms in its own bytes.
- **AC5** — When `python tools/memory-recall/union.py <data-dir> tools/memory-recall/recall-fixture.json`
  is run at a `--k` where `records:fts5` alone scores below 1.000, comparing
  `records:fts5+chunks:fts5` against `records:fts5+chunks:roll`, the result is recorded in the build
  record, and the §4 paragraph naming the docstring's ensemble claim is rewritten to state which way
  it came out. A run in which no `--k` leaves headroom is itself the recorded answer and says so.
- **AC6** — When the module docstring of `tools/memory-recall/query.py` is read, its ranking
  rationale block names the rollup on the chunk arm, and its FORKED header counts the constructs
  including this one.
- **AC7** — When `python tools/memory-recall/selftest.py` runs, `tools/memory-recall/verbatim.json`
  still matches `bench.py` and `union.py` byte for byte.
- **AC8** — When `python3 tools/memory-recall/check-recall.py` runs after this change, it is green.
  The floor grades ranking and not the CLI's fusion, so this is a no-regression observation and not
  evidence that the served shape improved.
- **AC9** — When a query runs against a cache built before this change, `CACHE_VERSION` has not
  moved and the run reports `cached` rather than a rebuild.

## 7. Gates

`memory-recall kit selftest`, `recall floor`, `recall floor arms`, `memory-recall skill wiring`,
`govkit selfcheck`, and `codebase-map coverage + freshness` because the dossier prose is refreshed on
touch. The full bar is `bash tools/run-gates/run-gates.sh`, and the kit self-tests need
`GATE_SELFTESTS=1` because this is kit work. No new leg is added.

## 8. Open questions

- **F1 — FACT-QUESTION · does the rollup still buy +0.000 in a two-set ensemble once the queries
  carry terms?** `run_rollup`'s docstring says it does and advises against expecting otherwise, but
  that measurement was taken on the bare question, and the terms-carrying run at `k=20` cannot test
  it because `records:fts5` alone saturates at 1.000. The probe that decides it is AC5: compare the
  two ensembles at a `k` with headroom. Options for what follows: if they are equal, land the change
  for the de-duplication alone and correct only the chunk-only half of the docstring's claim; if the
  rollup ensemble is higher, land it for both and record that the advice is stale for the served
  shape as well; if the de-duplication delta from AC3 also comes back small, the owner may prefer to
  park the unit until `TOOL-aWeighedCompass-18`'s discriminating fixture exists.
  Recommendation: land on the de-duplication result alone, because it is measured on the live query
  log's own field and does not depend on the fixture's headroom at all. The recall answer is then a
  bonus the record states honestly either way.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "keep only the best ranked chunk per parent record when
serving results"` returned `parent_of` in `tools/memory-recall/bench.py`, which is the seam this
unit reuses as a definition, together with `rank_with` in the same file and `extract_chunks` in
`tools/memory-recall/extract.py`. The probe did not return `run_rollup` itself, which is the
mechanism, so the seam was confirmed by reading: `run_rollup` at `tools/memory-recall/bench.py`
(`:135`) holds the loop, `rank_with` dispatches it as `roll` at (`:322`), and `parent_of` at
(`:130`) is the key both this unit and that loop compute. No existing seam in `query.py` fits,
because `search()` returns dictionaries joined against its own `meta` table rather than the
in-memory `docs` list `bench.run_rollup` takes, so the mechanism is reused and the code is not.

Recall terms used: `run_rollup roll chunks rrf duplicate slots parent best-per-parent query.py bench
substrate 600-character flooding`. The question was why the CLI serves raw chunk hits instead of the
rollup substrate. It returned 38 hits, and the ones that bind are the open row naming the rollup as
the only chunk substrate that beats grep with terms, the open row measuring 54.5 percent of live
result slots as repeated paths, and the earlier review finding that half the graded surface was
pinned against a chunk width the CLI never served.
