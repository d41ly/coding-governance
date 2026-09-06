**Serves:** research TOOL-dTracedLattice-1 TOOL-dTracedLattice-7

# MEASURER 2 — memory-recall RECALL over lens 2's scenarios

Node `d`, 2026-09-05. Repo HEAD `991153457d30c923151d749e12afedd4e9176689`, tracked tree clean
before and after. Scenario set: `scratchpad/scen-2-recall.json`, 95 entries (12 CONTROL / 9 GRADED /
74 STABILITY-ONLY).

## 0. How every number here was produced

Corpus extracted ONCE with the kit's own recipe and reused by every arm:

```
python tools/memory-recall/extract.py . <scratch>/m2/data --chunk-max 600
```

`--chunk-max 600` is `query.CHUNK_MAX`, which is what `check-recall.build_data_dir` passes, so the
graded corpus is the one the CLI actually serves. It yields 907 `records` docs / 504 266 chars,
43 598 `chunks` docs, 678 ids anchored, 217 orphan (24.2% of cited), and `spine` at ZERO docs — any
pin naming `spine` is a dead probe and `check-recall` precondition 3 refuses it. `aliases.json` is
absent in this repo, so the `alias` FTS5 column is empty and `ALIAS_WEIGHT = 0.4` is INERT in every
number below; nothing here tests that tuning.

Ranking goes through `bench.rank_with`. Target resolution goes through `bench.expected_by_target`.
Scoring goes through `bench.score`. The floor arithmetic is `check-recall.py`'s own `parse_pin` /
`measure_run` / `measure_overlap`, imported by path because the filename is hyphenated. The real
CLI expression is `query.query_expr`, called directly. Nothing about retrieval is re-implemented.

The ONE thing I wrote is a deliberately df-BLIND control ranker (§5, arm 4). It is labelled as mine
everywhere it appears and it is mutation-tested; one of its three mutation tests FAILED and that
failure is reported rather than dropped.

Scripts, all under `<scratch>/m2/`: `m2_floor.py` `m2_measure.py` `m2_shape.py` `m2_terms.py`
`m2_rarity.py` `m2_overlap.py` `m2_self.py` `rm3_seed.py`, with raw output beside each as
`floor.txt` `agg.txt` `shape.txt` `terms.txt` `rarity.txt` `overlap.txt` `self.txt`
`bench-records.txt` `union.txt` `check-recall.out` `check-recall-audit.out`.

---

## 1. HEADLINE

**The declared floor still holds, and it holds on the easiest twelve questions in the corpus.** The
same gate arithmetic over 83 harvested questions measures `records:fts5:r@5` = **0.3012** against a
pin of 0.81, and over the 9 GRADED ones it measures **0.0000**. Ceiling is 1.0000 in every class, so
none of that is a dead probe — every expected id resolves, retrieval simply does not return it.

**The gate grades a path the CLI refuses to run.** `query.py` REQUIRES `--terms`; `check-recall.py`
ranks the question string alone and the shipped fixture carries no `terms` field at all. Feeding the
recorded rewrite through `query.query_expr` moves the harvested set from r@5 0.325 to 0.398 and r@20
from 0.446 to 0.614. The half of the mechanism the CLI makes mandatory is invisible to the floor.

**`rm3` is not reproducible run to run** and it is a legal pin substrate. Eight free-seed runs of
the 12-question control give r@5 in {0.6667, 0.75}; `PYTHONHASHSEED=0` gives 0.75 four times out of
four; `fts5` is byte-identical across all fourteen runs. Cause below.

**On the owner's premise: memory-recall does NOT have codebase-map's disease, measured three ways —
but the premise is half right on a different axis.** Its ranking's head is anchored on the RAREST
query terms (median df 7 at rank 1, rising monotonically to 20 at ranks 11-20), the exact opposite
of `reuse_lookup` sorting `fan_in` descending. Take idf away and r@1 halves. But its own largest
lever, the `--terms` rewrite, is itself a rarity rewrite (median df 32 → 19), and its failure mode
is a rarity failure: a question sharing under 10% of its vocabulary with the answer returns nothing
at any k, 23 times out of 95. Both tools live or die on term rarity. Only one of them ranks by it.

---

## 2. (a) The declared floor reproduces exactly

```
$ python tools/memory-recall/check-recall.py                     # rc=0, 15.97 s wall
check-recall: per-id ok -- every expected id resolves in records (12/12 questions)
check-recall: cell records:fts5:r@5  raw 0.8333  ceiling 1.0000
check-recall: RECALL_FLOOR ok -- normalised 0.8333 >= 0.81

$ python tools/memory-recall/check-recall.py --audit-fixture     # rc=0
overlap: max 0.500 mean 0.362  over 12/12 measured  (OVERLAP_MAX 0.60)
derivation: h=10 R=12  (h-1)/(R-1) = 0.8182  declared RECALL_FLOOR 0.81
```

`h=10 R=12` is the literal `test_recall_floor.py` asserts, and both reproduce. Ten of twelve hit;
the two that miss are `TOOL-aUnmannedHelm-10` (overlap 0.125) and `TOOL-aMouldedFolio-1` (0.167) —
the two lowest-overlap rows in the fixture, which §6 will show is not a coincidence.

**This is not the headline. It is the control, and it passed.**

## 3. (b) The same arithmetic over the harvested scenarios

`m2_floor.py` imports `check-recall.py` and swaps only the question list. Every column is that
program's own.

```
pin: records:fts5:r@5>=0.81  (set=records sub=fts5 metric=r k=5 value=0.81)

fixture               n       R  ceiling      raw  normalised  vs RECALL_FLOOR
control              12      12   1.0000   0.8333      0.8333  ok
graded                9       9   1.0000   0.0000      0.0000  RED
stability            74      74   1.0000   0.3378      0.3378  RED
stability-clean      57      57   1.0000   0.1930      0.1930  RED
harvested            83      83   1.0000   0.3012      0.3012  RED
all                  95      95   1.0000   0.3684      0.3684  RED
```

Mean question/target vocabulary overlap, by the gate's own anti-tautology measure: control 0.362,
graded 0.120, stability 0.319 (17 rows above `OVERLAP_MAX` 0.60, max 0.917), harvested 0.297.

**A floor held by 12 curated questions and missed by 83 harvested ones, by 2.7x.** The gap is real
but it is NOT a single effect, and §6 and §7 decompose it: roughly half is question SHAPE, most of
the rest is the missing `--terms`, and the residue is genuine vocabulary distance.

`stability-clean` (0.1930) is the number to quote if you want one, not `stability` (0.3378) — the
17 excluded rows are the ones `check-recall --audit-fixture` would RED as written-from-the-record,
and they score 0.824 at r@5 because they contain their answer's words.

---

## 4. (c) Substrates

`bench.py --sets records --subs grep,fts5,fts5w,rm3 --ks 1,5,10,20`, its own output:

| set | substrate | r@1 | r@5 | r@10 | r@20 | MRR | b@10 |
|---|---|---|---|---|---|---|---|
| control 12 | grep | 0.08 | 0.17 | 0.17 | 0.17 | 0.125 | 11 658 |
| | fts5 | 0.58 | **0.83** | 0.83 | 0.83 | 0.681 | 6 828 |
| | fts5w | 0.25 | 0.83 | 0.83 | 0.83 | 0.443 | 8 803 |
| | rm3 | 0.42 | 0.75 | 0.75 | 0.75 | 0.519 | 12 070 |
| harvested 83 | grep | 0.07 | 0.10 | 0.11 | 0.11 | 0.083 | 8 894 |
| | fts5 | 0.18 | **0.30** | 0.36 | 0.42 | 0.236 | 16 032 |
| | fts5w | 0.16 | 0.27 | 0.36 | 0.39 | 0.213 | 11 629 |
| | rm3 | 0.19 | 0.34 | 0.40 | 0.48 | 0.255 | 20 196 |
| stability-clean 57 | grep | 0.02 | 0.02 | 0.04 | 0.04 | 0.020 | 9 104 |
| | fts5 | 0.07 | 0.19 | 0.26 | 0.32 | 0.127 | 14 752 |
| | fts5w | 0.07 | 0.16 | 0.28 | 0.32 | 0.121 | 11 224 |
| | rm3 | 0.09 | 0.26 | 0.33 | 0.39 | 0.156 | 18 012 |
| graded 9 | grep | 0.00 | 0.00 | 0.00 | 0.00 | 0.000 | 13 522 |
| | fts5 | 0.00 | 0.00 | 0.11 | 0.11 | 0.012 | 35 364 |
| | fts5w | 0.00 | 0.00 | 0.00 | 0.00 | 0.000 | 13 994 |
| | rm3 | 0.00 | 0.11 | 0.11 | 0.11 | 0.028 | 42 008 |

**The df-aware substrate beats the naive one by 3x to 5x at r@5** — 0.30 against 0.10 harvested,
0.83 against 0.17 on the control. This is the cleanest available isolation of RANKING: `run_grep`
is already df-aware in SELECTION (it picks the rarest content word by document frequency) and then
returns corpus order. So the whole 3x-5x is bm25's ordering of the same lexical evidence.

`fts5w` (head weighted 8x) is worse than `fts5` at r@1 (0.16 vs 0.18) and r@5 (0.27 vs 0.30) and
level at r@10. The conf comment claims the two "score IDENTICALLY here (r@10 0.8333 both)" — true on
the 12-question fixture, and false on the 83 harvested ones at every k below 10. Nothing is broken;
the identity is a property of the fixture, not of the substrates, and the conf says so about the
fixture only.

`rm3` looks like the winner at r@10/r@20 (0.40/0.48 harvested against 0.36/0.42). Do not pin it.

### 4b. `rm3` is nondeterministic across processes, and it is a legal pin substrate

`check-recall.SUBS = tuple(bench.LEXICAL) + …`, and `bench.LEXICAL = ("grep","fts5","fts5w","rm3")`,
so `RECALL_FLOOR="records:rm3:r@5>=0.40"` parses and would be graded.

Eight independent processes, same data dir, same fixture (`rm3_seed.py`):

| run | control fts5 r@1/5/10/20 | control rm3 r@1/5/10/20 |
|---|---|---|
| 1 | 0.5833 / 0.8333 / 0.8333 / 0.8333 | 0.4167 / 0.6667 / 0.6667 / 0.75 |
| 2 | identical | 0.4167 / 0.75 / 0.75 / 0.75 |
| 3 | identical | 0.4167 / 0.6667 / 0.75 / 0.75 |
| 4-5 | identical | 0.50 / 0.75 / 0.75 / 0.75 |
| 6 | identical | 0.4167 / 0.75 / 0.75 / 0.75 |
| 7 | identical | 0.50 / 0.6667 / 0.75 / 0.75 |
| 8 | identical | 0.4167 / 0.6667 / 0.75 / 0.75 |

Six free-seed runs on the 83 harvested questions: rm3 r@1 spans 0.1687–0.1928, r@5 0.3373–0.3735,
r@10 0.3976–0.4217, r@20 0.4458–0.4578. `fts5` is byte-identical in all fourteen runs.
`PYTHONHASHSEED=0` pins rm3 to 0.4167 / 0.75 / 0.75 / 0.75, four runs out of four.

Mechanism, from the source: `bench.run_rm3` does `df.update(set(terms(docs[i]["text"])[:400]))` and
then `df.most_common(RM3_TERMS * 3)`. `Counter.most_common` breaks ties by INSERTION order, and the
insertion order comes from iterating a `set` of strings, which PEP 456 hash randomisation varies per
process. Different expansion terms, different second query, different ranking. Fix is one line —
`sorted(set(...))` before the update, or `df.most_common()` keyed by `(-count, term)`.

This also explains a 0.06 discrepancy you will find between `bench-records.txt` (rm3 stability 0.41)
and `agg.txt` (0.351): two processes, two hash seeds, same code, same data. Neither is wrong.

### 4c. The ensemble the CLI actually serves

`union.py <data> <fixture> --k 20`, per-source depth 20:

| fixture | records:fts5 | +chunks:fts5 | bytes_full | bytes_snippet |
|---|---|---|---|---|
| control 12 | 0.833 | 0.833 | 20 045 → 31 258 | 8 106 → 17 613 |
| graded 9 | 0.111 | 0.111 | 53 106 → 64 195 | 9 312 → 19 018 |
| stability-clean 57 | 0.316 | 0.333 | 32 720 → 44 221 | 9 008 → 18 731 |
| harvested 83 | 0.422 | 0.434 | 33 079 → 44 545 | 9 030 → 18 768 |

Adding the chunks index buys **+0.012 recall for +108% snippet bytes** on the harvested set, and
+0.000 on control and graded. On this question set the second index is not paying for itself.

---

## 5. (d) The name-shape probe — four arms

### Arm 1 — observational bands. UNINFORMATIVE, and saying so is the finding.

fts5 recall by the df of each query's rarest PRESENT content term:

| band | n (all) | r@1 | r@5 | r@10 | r@20 |
|---|---|---|---|---|---|
| 1-2 | 59 | 0.220 | 0.356 | 0.424 | 0.492 |
| 3-8 | 29 | 0.207 | 0.345 | 0.379 | 0.414 |
| 9-25 | 6 | 0.500 | 0.500 | 0.500 | 0.500 |
| 26-80 | 1 | 0.000 | 1.000 | 1.000 | 1.000 |

Zero queries have no corpus-present content term. **88 of 95 questions contain a term appearing in
8 or fewer of 907 records**, so the "common-anchored query" population barely exists observationally
and the top two bands are n=6 and n=1. This arm cannot answer the question and is reported so a
green-looking band table is not mistaken for evidence. Arm 2 is the load-bearing one.

### Arm 2 — minimal pairs, query LENGTH held constant

Same question, same targets, cut to its N rarest present terms versus its N commonest. Length is
identical between arms, so only rarity moves.

| N | eligible n | mean df kept (rare / common) | arm | r@1 | r@5 | r@10 | r@20 |
|---|---|---|---|---|---|---|---|
| 3 | 89 | 7.1 / 172.7 | full question | 0.236 | 0.371 | 0.427 | 0.483 |
| | | | 3 rarest | 0.090 | 0.213 | 0.247 | 0.315 |
| | | | 3 commonest | 0.067 | 0.157 | 0.191 | 0.258 |
| 5 | 66 | 8.8 / 147.6 | full question | 0.182 | 0.333 | 0.409 | 0.485 |
| | | | 5 rarest | 0.121 | 0.227 | 0.273 | 0.333 |
| | | | 5 commonest | 0.091 | 0.167 | 0.227 | 0.288 |
| 8 | 40 | 10.4 / 127.5 | full question | 0.100 | 0.250 | 0.325 | 0.375 |
| | | | 8 rarest | 0.100 | 0.225 | 0.275 | 0.325 |
| | | | 8 commonest | 0.075 | 0.125 | 0.175 | 0.200 |

Paired at r@5, rare-only versus common-only: 14 win / 9 lose / 66 tie at N=3; 9 / 5 / 52 at N=5;
6 / 2 / 32 at N=8.

**Rare terms beat common terms in every one of the twelve cells, and the margin grows with N** —
+0.056 at N=3, +0.060 at N=5, +0.100 at N=8 (r@5). Directionally clean and consistent. It is also
SMALL in absolute terms and the paired win counts are 14-9, 9-5, 6-2, so at these n it is a
direction, not a magnitude. And both halves lose badly to the full question at every N, which is the
other half of the answer: this retriever needs the whole query, not its best third.

### Arm 3 — the direct analogue of "precision by fan-in band". THE decisive measurement.

For every doc `fts5` retrieved, the df of the RAREST query term that doc actually contains, bucketed
by rank position:

| rank bucket | n docs | median rarest-matched df | mean |
|---|---|---|---|
| rank 1 | 95 | **7.0** | 10.7 |
| ranks 2-5 | 380 | 11.0 | 14.7 |
| ranks 6-10 | 475 | 16.0 | 21.1 |
| ranks 11-20 | 950 | **20.0** | 25.0 |

Monotone. **The head of memory-recall's list is anchored on the rarest evidence available and the
tail on the commonest.** `reuse_lookup` sorts `fan_in` DESCENDING, so its head is anchored on the
commonest names by construction, and that is where the measured precision collapses from 51.8% to
7.2%. The two tools order by opposite signs of the same axis. That is what the owner's premise asked
for and it is measured, not argued.

### Arm 4 — the df-blind control (MINE, not the kit's), and its failed mutation test

Same FTS5 candidate pool, re-ranked by the raw count of distinct query terms each doc contains, ties
by corpus order. Pool depth 400 against fts5's 20, so the control is HANDICAPPED IN ITS FAVOUR by a
20x deeper candidate set.

Three mutation tests, because a double you wrote grades nothing:

1. **PASS** — the control's top-5 is identical to fts5's on **0 of 95** queries. It is not a copy.
2. **FAILED, as designed and reported** — I predicted the control's top-5 would sit at a HIGHER
   rarest-matched df than fts5's. Measured: fts5 median 10.0, control median 8.0. The control's docs
   match RARER terms, because a doc matching many query terms usually also matches a rare one. The
   prediction was wrong; the test is kept and printed rather than deleted.
3. **PASS** — the control's top-5 covers **59.2%** of the query's content terms against fts5's
   **41.4%** (mean over 475 docs each). It demonstrably sorts on coverage count, which is the exact
   quantity bm25 does not sort on. This is what makes it a live df-blind control despite test 2.

| set | ranker | r@1 | r@5 | r@10 | r@20 |
|---|---|---|---|---|---|
| ALL 95 | fts5 | **0.232** | **0.368** | 0.421 | 0.474 |
| | df-blind | 0.116 | 0.263 | 0.358 | 0.432 |
| CONTROL 12 | fts5 | 0.583 | 0.833 | 0.833 | 0.833 |
| | df-blind | 0.167 | 0.500 | 0.833 | **1.000** |
| harvested 83 | fts5 | 0.181 | 0.301 | 0.361 | 0.422 |
| | df-blind | 0.108 | 0.229 | 0.289 | 0.349 |

**Removing idf halves r@1 (0.232 → 0.116) and costs a quarter of r@5, from a 20x deeper pool.** At
r@20 the gap closes to 0.042, and on the control the df-blind ranker actually WINS at r@20 (1.000
against 0.833) — which is the pool depth, not the ranker. Read together: **idf buys ORDER, not
REACH.** That is precisely the property `reuse_lookup` lacks, and precisely the property the
proposed reuse_lookup re-ranking was measured to add (precision@5 1.6% → 80.0% at no recall cost).

### Arm 5 — and yet: `--terms` IS a rarity rewrite

Over the 83 scenarios carrying a recorded `Recall terms used:` line:

| token population | tokens/query | median df | mean df | share with df=0 |
|---|---|---|---|---|
| the question's own content words | 16.4 | 32.0 | 59.4 | 3.5% |
| the session's supplied `--terms` | 15.2 | **19.0** | **35.3** | 7.4% |

Supplied terms are quoted as WHOLE phrases into the MATCH expression, and a phrase's df is at most
the min df of its sub-tokens, which is what I measured — so 19.0 is a ceiling on their true rarity
and the gap is a floor. Sessions also supply ~15 terms, not the 8-14 the CLI's own help asks for.

**The single largest measured lever in this tool is a 40%-lower-median-df restatement of the same
question.** Worth +0.073 r@5 and +0.168 r@20 on the harvested set (§7). So the owner's premise is
half right after all — just not where it was aimed. memory-recall does not RANK by commonness, but
its performance is dominated by how rare the query's vocabulary is, and its one required human input
is a manual idf boost.

---

## 6. The variable that actually explains the class gap: vocabulary overlap

`check-recall.measure_overlap` computes, per question, the share of its distinct content terms that
appear anywhere in the union of the documents that answer it. It exists to RED a question written
from its own answer. Used the other way round it is the cleanest proxy available for how much
lexical bridge a purely lexical retriever is given.

| overlap band | n | r@1 | r@5 | r@10 | r@20 |
|---|---|---|---|---|---|
| 0.00–0.10 | 23 | 0.000 | **0.000** | 0.000 | 0.000 |
| 0.10–0.20 | 16 | 0.000 | 0.125 | 0.125 | 0.250 |
| 0.20–0.30 | 18 | 0.000 | 0.222 | 0.333 | 0.389 |
| 0.30–0.45 | 13 | 0.462 | **0.692** | 0.769 | 0.769 |
| 0.45–0.60 | 8 | 0.625 | 0.750 | 1.000 | 1.000 |
| 0.60+ (tautological) | 17 | 0.647 | 0.824 | 0.824 | 0.941 |

Mean overlap: CONTROL 0.362 (r@5 0.833), GRADED 0.120 (0.000), STABILITY-ONLY 0.319 (0.338).

**Recall is a step function of shared vocabulary with a knee at ~0.30.** Fifty of the ninety-five
questions return NOTHING at any k up to 20 (48 of the 83 harvested ones, and 2 of the control's 12);
all 23 in the lowest overlap band are among them, and no question above 0.45 overlap is. The shipped
fixture's mean sits at 0.362, just ABOVE the knee. The harvested set sits at 0.297, just BELOW it.
That single number predicts the 0.83-versus-0.30 gap better than the class label does, and it says
what the tool is: a lexical bridge that works when one exists and returns zero when it does not. No
re-ranking reaches the 23 zero rows; only a non-lexical signal or a better rewrite does.

There is a trap in using this measure and I am walking into it deliberately: the 0.60+ band is the
17 rows `check-recall --audit-fixture` REDS as written-from-the-record. Their 0.824 is a tautology
score and must never be averaged into a headline. It is in the table because the SHAPE of the curve
is the finding.

---

## 7. The real CLI path, and the question-shape confound

`query.query_expr` ORs the question's terms with each supplied `--terms` token quoted WHOLE, plus
every id as a quoted phrase. It differs from `bench.match_expr` on 5 of 95 questions (ids) and is
slightly better: ALL r@5 0.389 against 0.368.

| group | arm | r@1 | r@5 | r@10 | r@20 |
|---|---|---|---|---|---|
| harvested 83 | question only (bench path — what the gate grades) | 0.181 | 0.301 | 0.361 | 0.422 |
| | question only (query.py expression) | 0.193 | 0.325 | 0.386 | 0.446 |
| | question + terms (query.py) | 0.217 | **0.398** | 0.482 | **0.614** |
| | terms only (query.py) | 0.217 | 0.398 | **0.530** | 0.602 |
| GRADED 9 | question only | 0.000 | 0.000 | 0.111 | 0.111 |
| | question + terms | 0.000 | 0.111 | 0.222 | 0.333 |
| | terms only | 0.111 | 0.222 | 0.333 | 0.444 |
| STABILITY 74 | question only | 0.216 | 0.365 | 0.419 | 0.486 |
| | question + terms | 0.243 | 0.432 | 0.514 | 0.649 |
| ..overlap-clean 57 | question only | 0.088 | 0.228 | 0.298 | 0.351 |
| | question + terms | 0.105 | 0.298 | 0.404 | **0.561** |

`terms only` beating `question + terms` on GRADED is ONE question at n=9 and is noise. `terms only`
beating it at r@10 on the harvested set (0.530 against 0.482) is four questions and is worth a second
look, not a claim.

**0 of the 12 CONTROL entries carry a `terms` line**, because `recall-fixture.json` has no such
field. So the floor cannot measure the rewrite even in principle, and every gate number in this repo
describes the weaker of the tool's two input paths.

### The question-shape confound, sliced as far as this set allows

| slice | n | question only r@5 | question+terms r@5 | question+terms r@20 |
|---|---|---|---|---|
| CONTROL (12/12 interrogative) | 12 | 0.833 | n/a — no terms | n/a |
| harvested, interrogative | 12 | 0.500 | 0.750 | **1.000** |
| harvested, declarative goal | 71 | 0.268 | 0.338 | 0.549 |

Roughly half the CONTROL-versus-harvested gap is question SHAPE (0.268 → 0.500 just by asking a
question instead of stating a goal), most of the remainder is the missing rewrite (0.500 → 0.750),
and the residue against CONTROL's 0.833 is small at n=12. Lens 2 flagged this confound as its
biggest and it is the correct call: the class gap is not mostly about target difficulty.

---

## 8. A finding the brief did not ask for: the CLI hands a session its own document

`chunks:fts5` over the 83 harvested questions, matching each retrieved chunk's path against the file
the question was mined from:

- rank-1 chunk is the question's OWN source file on **80 of 83 (96%)**
- **156 of 415 top-5 slots (38%)** are chunks of that same file

The record-level numbers everywhere else in this report are IMMUNE: only 2 of the 907 `records` docs
come from a spec file (387 backlog, 240 archive, 177 build records, 103 `DECISIONS.md`). But the CLI
serves records+chunks fused, so this is what a session sees.

Two readings, and the honest one is the second:

- As a measurement of live behaviour it is an ARTIFACT. `extract.py` reads `git ls-files`, so an
  uncommitted spec is not in the corpus, and a session probing before it commits does not see itself.
- As a live cost it is real for exactly one workflow, and that workflow is mandated: `.memory-tree.conf`
  documents M7 regrounding step 5 as re-running the recall probe with the terms recorded in the spec.
  By then the spec IS committed, and 38% of the top 5 will be the spec asking the question.

Observed directly in the one live CLI run (`m2/cli-run1.txt`): ranks 1, 3 and 5 of nine displayed
hits are the querying spec's own title, its own §1 Goal, and its own §10 recall-terms sentence.

---

## 9. Cost — every reading a single draw on node `d`, whose AV taxes each process creation ~0.022 s

| operation | wall |
|---|---|
| `extract.py . <dir> --chunk-max 600` (907 records + 43 598 chunks) | 3.65 s |
| `check-recall.py` end to end (extract + index + 12 queries) | 15.97 s |
| `check-recall.py --audit-fixture` | comparable |
| records FTS5 index build (907 docs) | 0.02 s |
| chunks FTS5 index build (43 598 docs) | ~4 s of a 5.02 s script |
| per query, records: `fts5` / `fts5w` | ~1 ms |
| per query, records: `grep` / `rm3` | ~4 ms / ~4-5 ms |
| `query.py` CLI, warm cache, one question + 14 terms | **0.567 s** |

The gate costs 16 s and is dominated by a re-extract it performs on every run into a fresh temp dir.
Nothing here argues that is wrong — a graded corpus built from the live tree is the point — but it
is 4x the extract and 800x the ranking.

---

## 10. Verdict on each part of the brief

**(a)** The floor holds. `records:fts5:r@5` normalised 0.8333 against the pinned 0.81, `h=10 R=12`,
`(h-1)/(R-1) = 0.8182`. Not the headline.

**(b)** The same arithmetic gives 0.3012 over 83 harvested questions and 0.0000 over the 9 graded
ones, with ceiling 1.0000 in both — every target resolves, retrieval does not reach it. The floor is
measured on the easy end, exactly as lens 2 predicted. But the gap decomposes: about half is
question shape, most of the rest is the `--terms` rewrite the gate cannot see, and the residue is
vocabulary distance measured by the gate's own overlap statistic.

**(c)** `fts5` beats `grep` by 3x-5x at r@5 (0.30 vs 0.10 harvested, 0.83 vs 0.17 control) — and
because `grep` is ALREADY df-aware in selection, that entire margin is bm25's ORDERING. `fts5w`
loses to `fts5` below k=10 on the harvested set despite the conf note that they score identically,
which is a fixture property, not a substrate property. `rm3` leads at r@10/r@20 and is
NOT REPRODUCIBLE across processes; it is a legal pin substrate and pinning it would give a flaky
gate. The df-aware substrate does beat the naive one, decisively.

**(d)** memory-recall does NOT have codebase-map's disease, and it is measured three ways: its
rank-1 doc is anchored on a query term of median df 7 rising monotonically to df 20 by ranks 11-20;
at matched query length, rare terms beat common terms in all twelve cells; and stripping idf out of
the ranking halves r@1 from a 20x deeper candidate pool. The owner's premise that the two tools
share a mechanism is REFUTED at the ranking layer. It is CONFIRMED at a different layer: the tool's
largest lever is a manual rarity rewrite (median df 32 → 19, worth +0.073 r@5), and its total
failure mode is a rarity failure — 23 of 95 questions share under 10% of their vocabulary with their
answer and return zero at every k — and fifty of the ninety-five return zero at every k up to 20.
Both tools stand or fall on term rarity. One of them ranks by it.

---

## 11. What is weak here

- **n=9 GRADED. One question is 0.111.** Every graded delta in this document is at or below the
  resolution of the set. The 0.0000 is worth reporting because it is a floor, not a point estimate.
- **`rm3` numbers are single draws** unless a range is given. Where I quote one (the bench table) it
  is one seed's; the ranges in §4b are the honest form.
- **Arm 2 strips a question to bare terms, which no session does.** It isolates the mechanism at the
  cost of realism, and its effect sizes must not be read as what a session would gain.
- **Mutation test 2 on my df-blind control failed.** The control is validated by tests 1 and 3 only.
  If a reviewer rejects test 3 as insufficient, arm 4 falls and arm 3 carries the (d) verdict alone.
- **The df-blind control draws from a 400-deep pool against fts5's 20.** That handicap is in the
  control's favour at r@20 and is why it wins there on the CONTROL slice. Only the r@1 and r@5 rows
  should be read as evidence.
- **`ALIAS_WEIGHT` is untested.** `aliases.json` is absent in this repo, so the alias column is empty
  in every measurement and the swept 0.4 is inert here.
- **The overlap analysis uses `check-recall`'s own measure**, whose denominator is the question's
  terms and whose numerator ranges over the run's OWN resolved targets. 17 of 95 rows are
  tautological by that tool's standard and are shown separately for shape, never averaged in.
- **`terms` df is measured per sub-token**, while the CLI quotes each term as a whole phrase. My
  numbers are a ceiling on the terms' rarity, so §5 arm 5's gap is a floor, not an estimate.
- **One repo, one corpus, one node, one platform.** 907 records docs with this project's id grammar,
  its §10 convention, and its jargon. Nothing here is a property of the memory-recall KIT and none
  of it should be quoted as one.
- **The self-retrieval number in §8 is an artifact for the pre-commit case** and only live for the
  regrounding re-run. I have stated both and measured only the artifact.
- **Selection bias inherited from lens 2**: these are the questions sessions WROTE DOWN in a section
  a gate makes them fill. The 102 §10s recording that the probe found nothing are not scoreable by
  recall@k and are absent, so the true harvested recall is BELOW 0.3012, not above it.
- **No true negatives anywhere.** Nothing here measures the tool returning confident junk for a
  question with no answer.

## 12. Housekeeping

Tracked tree clean before and after (`git status --porcelain` empty at both ends). One live
`query.py` run appended a row to `<git-common-dir>/recall/queries.jsonl` and warmed its cache; that
path is outside the worktree and outside the index, by the kit's design.
