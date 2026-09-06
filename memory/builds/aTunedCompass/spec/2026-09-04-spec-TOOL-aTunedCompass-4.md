# TOOL-aTunedCompass-4 — the chunk source becomes the rollup, which also de-duplicates the slots

**Status:** CLOSED · rev-4 · 2026-09-05 · node a · Tier-2 · base c4fcf5ad · streams tooling · order 1 · ratified 2026-09-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-build-TOOL-aTunedCompass-4-acceptance-ledger.md](../build/2026-09-05-build-TOOL-aTunedCompass-4-acceptance-ledger.md) | journal | — |
| [2026-09-05-review-TOOL-aTunedCompass-1-closing-diff-round1.md](../reviews/2026-09-05-review-TOOL-aTunedCompass-1-closing-diff-round1.md) | diff-review | TOOL-aTunedCompass-1 TOOL-aTunedCompass-5 TOOL-aTunedCompass-6 TOOL-aTunedCompass-7 TOOL-aTunedCompass-8 TOOL-aTunedCompass-10 TOOL-aTunedCompass-11 |
| [2026-09-05-review-TOOL-aTunedCompass-1-closing-diff-round2.md](../reviews/2026-09-05-review-TOOL-aTunedCompass-1-closing-diff-round2.md) | diff-review | TOOL-aTunedCompass-1 TOOL-aTunedCompass-5 TOOL-aTunedCompass-6 TOOL-aTunedCompass-7 TOOL-aTunedCompass-8 TOOL-aTunedCompass-10 TOOL-aTunedCompass-11 |
| [2026-09-05-review-TOOL-aTunedCompass-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aTunedCompass-1-spec-audit-round1.md) | spec-audit | TOOL-aTunedCompass-1 TOOL-aTunedCompass-2 TOOL-aTunedCompass-3 TOOL-aTunedCompass-5 TOOL-aTunedCompass-6 TOOL-aTunedCompass-7 TOOL-aTunedCompass-8 TOOL-aTunedCompass-9 TOOL-aTunedCompass-10 TOOL-aTunedCompass-11 |
| [2026-09-05-review-TOOL-aTunedCompass-4-spec-audit-round2.md](../reviews/2026-09-05-review-TOOL-aTunedCompass-4-spec-audit-round2.md) | spec-audit | TOOL-aTunedCompass-6 TOOL-aTunedCompass-9 |

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
- **S3** — the two fusion call sites become ONE. `query.py` builds the same pair twice — the first
  attempt at `:1177` and the rebuild after a `sqlite3.DatabaseError` at `:1181` — and a rollup applied
  to only one makes the served shape depend on whether the cache was healthy. Rather than require
  both to be edited in step and then observe neither, the fused call is extracted into a single
  helper both paths call, so the pair cannot be half-edited and the existing arms cover both. The
  duplication is the defect; deleting it is cheaper than gating it.
- **S4** — the ranking rationale block in the module docstring of `query.py` gains a bullet stating
  that the chunk arm is rolled up, why, and what it costs. That block exists so the served
  configuration cannot drift from the instrument, and it is where the correction to `run_rollup`'s
  own stale advice belongs, because `bench.py` is byte-pinned in `verbatim.json`.
- **S5** — the FORKED header of `query.py` names the new construct. It currently says six constructs
  are edited and the rest is upstream's byte for byte, and a re-pull is a three-way merge against
  that list.
- **S6** — the DE-DUPLICATION measurement is run and recorded, which is S8's before-and-after. The
  ensemble-recall measurement is NOT in scope: F1's resolution defers it until
  `TOOL-aTunedCompass-9` reports, and this unit claims nothing about ensemble recall meanwhile. rev-2
  left this item mandating the measurement the same revision's resolution deferred, so a builder
  could not tell whether the unit was done without it.
- **S7** — TWO corpus-independent arms in `tools/memory-recall/selftest.py`, one per branch of the
  parent key, because §4 measures the branches at 0.6% and 99.4% and an arm on the rare one certifies
  nothing about the common one. (a) ANCHORED: over a synthetic fixture where one anchored record holds
  several matching chunks, the served result set carries that record at most once from the chunk
  source, and a second record's chunk is present. (b) UNANCHORED: over a synthetic file with no
  record anchor at all, several of whose chunks match, the served result set carries that FILE at most
  once from the chunk source. Each arm is observed RED against the pre-change code before it is wired.
- **S8** — the duplicate-path rate is measured before and after over the fixture questions, from the
  `shown_paths` field the log already writes, and the delta is recorded with the unit. The measured
  quantity is the TOTAL duplicate-path rate over that field, not a per-source one: `shown_paths` is
  documented in-code as "Paths only" (`tools/memory-recall/query.py` `:1251`) and carries no `set`
  label, so the records arm contributes the same path indistinguishably. The only field carrying
  `set` is `results`, and it is truncated at `RESULT_CAP = 5` (`:136`, emitted at `:1241`), so it
  answers a five-slot prefix rather than the served list. One field, one population.

  **The per-source qualifier is dropped from the LOG-DERIVED criteria only** — AC1 and AC3. S7's arm
  keeps it, and legitimately: that arm builds its own synthetic fixture, so it knows which record each
  slot came from without needing a label the log does not carry. A measurement over live rows and an
  assertion over a constructed one are not the same observation, and only the first is blind here.

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

### Which of this unit's claims need unit 2, and which do not

Historical note, kept because it explains two DEFERRED criteria rather than a live dependency. Every
RECALL figure that originally justified this change was measured with terms appended by hand to a
fixture carrying none: with terms at the live chunk width `chunks:roll` scores recall@20 of about
0.33 against `chunks:fts5` at about 0.17 and grep at 0.17, the only chunk substrate that beats grep,
where on the bare question both sit at 0.08. `TOOL-aTunedCompass-2` puts the terms in the fixture,
and until it lands any RECALL measurement here grades a query shape `query.py` refuses to serve.
That is why AC4 is deferred to unit 2 and AC5 to unit 9.

What this unit LANDS on needs neither. F1's resolution moved it to order 1 precisely because the
de-duplication result is measured from the live query log's own `shown_paths` field and does not
depend on the fixture's headroom at all. The order-1 Definition of Done is therefore AC1, AC2, AC3,
AC6, AC7, AC8, AC9 and AC10; the two deferred criteria are answered by later units and are marked as
such in §6 rather than left to a reader to infer from a resolved fork.

### The parent key, verified at source

`_write_set` in `query.py` writes `meta.id` as the document's `id` or its `rec`, and `extract_chunks`
gives a chunk a `rec` naming the anchored record it sits inside. So for a chunk hit, `hit["id"]` is
the parent record id WHERE ONE EXISTS, and `hit["id"] or hit["path"]` is `bench.parent_of` expressed
over the row shape `search()` returns. The two cannot be a single function: `bench.run_rollup` takes
the in-memory `docs` list and a `bench.build_index` connection, while `query.py` serves dictionaries
joined against its own `meta` table.

**The path branch is the OPERATING MODE, not a fallback, and rev-3 had this backwards.** A chunk gets
`rec` only when a heading line ITSELF defines a record id, and `A_HEADING` requires `#{2,6}`, so an
H1, a bold-list anchor and a table anchor all leave it unset. Measured over the tracked corpus by
running `extract_chunks` across every `memory/**/*.md`:

| Chunk documents | Carrying a `rec` | Keyed by path |
|---|---|---|
| 20056 | 129 (0.6%) | 19927 (99.4%) |

So for 99.4% of the served chunk arm this change is a PER-PATH cap — at most one hit per file — and
the per-record behaviour the section is named for is the 0.6% case. That does not sink the unit: a
per-path cap is exactly what the duplicate-slot problem needs, and S8's measurement is over paths for
the same reason. What it changes is what may be CLAIMED, and it changes what must be tested: S7's
arm exercises the 0.6% branch, so a second arm over an UNANCHORED synthetic file is required, or the
branch the corpus actually takes ships unobserved. The figures above are derived, not authored — the
command is the one named at the head of this paragraph, and §7's left-shift is to have `extract`
print the share rather than have a spec retype it.

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

| File | Why |
|---|---|
| `tools/memory-recall/query.py` | `run_rollup`, `ROLLUP_DEPTH`, the single fused call site S3 extracts, the docstring blocks S4 and S5 |
| `tools/memory-recall/selftest.py` | S7's two arms, one per parent-key branch |
| `tools/memory-recall/recall_conf.py` | `KIT_MEMORY_RECALL_VERSION`, which AC9 is built on |
| `tools/memory-recall/README.md` | the paired `gov:kit memory-recall@` marker at `:3` |
| `memory/map/features/memory-recall.md` | the dossier prose refresh a touch owes |

The last two rows are not bookkeeping. `tools/check-kit-versions.sh` (`:199`-`:205`) greps
`KIT_MEMORY_RECALL_VERSION` out of `recall_conf.py` and REDS unless the `gov:kit memory-recall@`
marker in that README matches it, so the version bump AC9's whole argument rests on has a paired
carrier that must move in the same commit. rev-3 wrote "in every carrier the govkit stamp check
names", which names no carrier and left the pair invisible.

### Migration

The rollup is applied at query time to rows already in the cache, so extraction and the index schema
are unchanged and `CACHE_VERSION` does NOT bump. Bumping it would force every node to rebuild an
index whose bytes are identical.

**One rebuild IS forced, though, and rev-2 claimed otherwise.** `KIT_MEMORY_RECALL_VERSION` moves
with any engine change, and that constant sits inside the blob `Conf.digest()` hashes
(`tools/memory-recall/recall_conf.py` `:229`); `ensure_cache` compares `man['conf_digest']` against
it (`tools/memory-recall/query.py` `:602`) and prints `rebuilt Ns` when they differ (`:1197`). So the
first post-change run on any node rebuilds, once, attributable to `conf_digest` and not to
`CACHE_VERSION`. The digest's own docstring prices exactly this — one rebuild per kit bump — and
sibling `TOOL-aTunedCompass-5`'s S7 states the same mechanism for the same kit. AC9 observes that
sequence rather than asserting a cache hit the version bump forbids.

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
- migration / rollback — no CACHE_VERSION bump and no index change; one forced rebuild attributable
  to `conf_digest`, which §4 Migration prices and AC9 observes. The diff is confined to `run_rollup`
  and the single fused call site S3 extracts, so a revert is a revert.
- user docs — the rendered Skill describes the CLI's arguments and not its substrates, so it is
  unchanged. The module docstring is the carrier per S4.

## 6. Acceptance criteria

- **AC1** — When a question is served whose chunk matches concentrate in one anchored record, the
  `shown_paths` field of the new row in the recall query log carries strictly fewer duplicate entries
  of that record's path than the same question at base `c4fcf5ad` did. The claim is a total
  duplicate count over that field, per S8: `shown_paths` carries no source label, so "at most once
  FROM THE CHUNK SOURCE" is not observable from it and rev-2's wording could only be satisfied by
  reading a field that does not exist.
- **AC2** — When `python tools/memory-recall/selftest.py` runs, the new S7 arm passes, and the arm
  was seen RED against the pre-change `query.py` before it was wired.
- **AC3** — When the fixture questions are replayed through
  `python3 tools/memory-recall/query.py` before and after the change, the duplicate-path rate over
  `shown_paths` falls, and both rates are recorded with the unit rather than quoted from the parent
  build's 54.5 percent.
- **AC4** — **DEFERRED — `TOOL-aTunedCompass-2`.** When
  `python tools/memory-recall/bench.py <data-dir> tools/memory-recall/recall-fixture.json --sets
  chunks --subs fts5,roll --ks 5,10,20` runs against the TERMS-CARRYING fixture at `--chunk-max 600`,
  `roll` scores above `fts5` at recall@20. That fixture is created by `TOOL-aTunedCompass-2`, which is
  order 2 and BLOCKED, so this criterion is not part of an order-1 Definition of Done and is answered
  when unit 2 lands.
- **AC5** — **DEFERRED — `TOOL-aTunedCompass-9`.** When `python tools/memory-recall/union.py` is run
  over the DISCRIMINATING fixture that unit produces — not the committed one — comparing
  `records:fts5+chunks:fts5` against `records:fts5+chunks:roll`, the result is recorded in the build
  record and the §4 paragraph naming the docstring's ensemble claim is rewritten to state which way it
  came out. The fixture is named here once unit 9 names it. rev-3 left this criterion pointing at
  `recall-fixture.json` while its own tail said no `--k` on that file leaves headroom, so it stayed
  unsatisfiable even after the unit it waits on lands — a deferral to an unblocker that does not
  unblock it.
- **AC6** — When the module docstring of `tools/memory-recall/query.py` is read, its ranking
  rationale block names the rollup on the chunk arm, and its FORKED header counts the constructs
  including this one.
- **AC7** — When `python tools/memory-recall/selftest.py` runs, `tools/memory-recall/verbatim.json`
  still matches `bench.py` and `union.py` byte for byte.
- **AC8** — When `python3 tools/memory-recall/check-recall.py` runs after this change, it is green.
  The floor grades ranking and not the CLI's fusion, so this is a no-regression observation and not
  evidence that the served shape improved.
- **AC9** — When a query runs against a cache built before this change: `man['version']` still equals
  `CACHE_VERSION` on the old manifest, the FIRST post-change run REBUILDS with `conf_digest` named as
  the cause, and the SECOND run reports `cached`. rev-2 asserted the first run would report `cached`,
  which this unit's own Files-touched forbids —  `KIT_MEMORY_RECALL_VERSION` is inside the hashed blob
  `Conf.digest()` builds (`tools/memory-recall/recall_conf.py` `:229`) and `ensure_cache` keys
  freshness on `man.get("conf_digest") == CONF.digest()` (`tools/memory-recall/query.py` `:602`), so
  the bump moves the digest and the run rebuilds at any ordering. The criterion was unsatisfiable, and
  its two tempting exits were dropping the version bump `check-kit-versions.sh` requires, or
  "verifying" it by checking `CACHE_VERSION` alone and reporting a cached run that never happened.
  What this criterion now observes is the true statement: the cache format did not change, exactly one
  rebuild is forced, and its cause is attributable.
- **AC10** — When the fused pair is read after the change, `query.py` holds ONE call site rather than
  the two at `:1177` and `:1181`, so a rollup cannot be applied to the healthy path and not the
  rebuild path. This is S3's observation and it replaces a criterion set in which every arm ran the
  healthy path and a half-applied rollup passed all of them.

## 7. Gates

`memory-recall kit selftest`, `recall floor`, `recall floor arms`, `memory-recall skill wiring`,
`govkit selfcheck`, and `codebase-map coverage + freshness` because the dossier prose is refreshed on
touch. The full bar is `bash tools/run-gates/run-gates.sh`, and the kit self-tests need
`GATE_SELFTESTS=1` because this is kit work. No new leg is added.

## 8. Open questions


**F1 RESOLVED (owner, 2026-09-05): land on the de-duplication result alone, and move the unit to order 1.**
The de-duplication is measured from the live query log's own `shown_paths` field and does not depend
on the fixture's headroom at all, so it does not wait on `TOOL-aTunedCompass-9`.
[rev-4 note: the owner's resolution as originally written named the `results` field. S8 corrected
the field to `shown_paths` at rev-3 — `results` is truncated at `RESULT_CAP = 5` and so answers a
five-slot prefix rather than the served list — and this clause is amended to match rather than left
naming a field the same fold refuted. The decision itself, to land on the de-duplication alone, is
the owner's and is unchanged.] The recall comparison
does need a `k` with headroom, so AC5 is explicitly deferred until unit 9 reports and this unit
claims nothing about ensemble recall in the meantime. The rollup's effect on recall becomes a bonus
the record states honestly either way, which is what this fork recommended.

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
- rev-2 · 2026-09-05 · F1 resolved by the owner: the unit's claim is the de-duplication, AC5's recall
  comparison defers to after `TOOL-aTunedCompass-9`, and the unit moves from order 3 to order 1
  because nothing it now claims depends on the fixture.
- rev-3 · 2026-09-05 · round-1 spec audit folded, findings B2, H4, H6, H7 and M8. Four of the five are
  one shape: rev-2's resolution and reorder were never propagated out of §8 into scope and acceptance.
  B2 — AC9 required a warm cache to report `cached` while §4 Files-touched bumps
  `KIT_MEMORY_RECALL_VERSION`, which is inside the hashed digest blob, so the criterion was
  unsatisfiable at any ordering and its tempting exits were dropping the version bump or "verifying"
  it against `CACHE_VERSION` alone. AC9 now asserts the true sequence — format unmoved, exactly one
  rebuild, cause attributable — and §4 Migration stops claiming no rebuild is forced. H4 — AC1 and AC3
  asked for a per-source count from `shown_paths`, which carries no `set` label, while F1's resolution
  named `results`, which is capped at five: two populations, neither answering the question. S8 picks
  `shown_paths` and the total rate, and the "from the chunk source" qualifier is gone. H6 — the header
  reads order 1 while §4 carried a live dependency on order-2 unit 2 and AC4 needed its fixture; the
  heading is now historical and AC4 is marked DEFERRED. H7 — S6 mandated the very measurement F1
  defers, so the Definition of Done contained a criterion the resolution forbids meeting; S6 is now
  the de-duplication alone and AC5 carries its DEFERRED marker in §6 where a ledger can see it. M8 —
  S3 required both fusion call sites to change together and then observed neither, so a half-applied
  rollup passed every criterion and would surface only on a corrupted cache; the two call sites are
  now extracted into one, which is the smaller diff and the root-cause fix, and AC10 observes it.
- rev-4 · 2026-09-05 · round-2 spec audit folded, findings H1, H2, H4 and H6 — all four in rev-3's
  own fold. H4 is the material one: §4 called the path branch a FALLBACK, and measuring
  `extract_chunks` over the tracked corpus gives 129 of 20056 chunks carrying a `rec`, so the path
  branch is 99.4% of the served arm and the per-record behaviour the section is named for is the
  0.6% case. The unit survives — a per-path cap is what the duplicate-slot problem needs — but the
  claim is restated and S7 gains a second arm over an UNANCHORED file, because rev-3's single arm
  exercised only the rare branch. H1 — the F1 RESOLVED block still named `results` after the same
  fold moved the measurement to `shown_paths`, so the binding resolution contradicted the scope it
  authorised; amended in place with a bracketed note, the owner's decision left verbatim. H2 — AC5
  deferred to unit 9 while still naming `recall-fixture.json`, whose lack of headroom is the reason
  for the deferral, so it stayed unsatisfiable after its unblocker lands; it now names unit 9's
  discriminating fixture. H6 — Files-touched said "every carrier the govkit stamp check names",
  naming none; it is now a table, and it carries `README.md`, whose `gov:kit` marker
  `check-kit-versions.sh` reds on unless it moves with the constant AC9 rests on.

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
