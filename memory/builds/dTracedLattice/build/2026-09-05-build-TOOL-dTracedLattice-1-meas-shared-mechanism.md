**Serves:** research TOOL-dTracedLattice-1 TOOL-dTracedLattice-7

# MEASURER 3 — is it the same mechanism?

Node `d`, 2026-09-05, repo HEAD `991153457d30c923151d749e12afedd4e9176689`, tracked tree clean.
Every number below carries the command that produced it. Scripts and raw JSON in
`scratchpad/m3/`.

---

## Verdict

**The premise is right, but not in the shape it was stated.** `codebase-map` is not *missing* a df
correction. It computes document frequency, calls it `fan_in`, and **sorts by it descending** —
which is the inverse of what `memory-recall` does with the same quantity. The two tools do not
share a mechanism; they share a *quantity* and apply it with **opposite sign**.

Three measured claims, in decreasing order of how much I would bet on them:

1. **`fan_in` IS a document frequency, exactly.** Over all 645 distinct symbol ids,
   `identifier-DF − fan_in = +1` for 645/645. Not "resembles". Is.
2. **Ranking by that quantity descending is worse than not ranking at all.** Ported onto
   `memory-recall`'s corpus, `reuse_lookup`'s algorithm (boolean match → sort by fan-in desc)
   scores r@5 = 0.000 against 0.074 for the identical match set left in arbitrary corpus order,
   over 95 scen-2 queries. It is not a weak signal. It is an anti-signal.
3. **df correction is what protects `memory-recall` — but you cannot see that by ablating idf
   alone, because the kit corrects for df TWICE and either copy covers for the other.** Removing
   bm25's idf costs r@5 0.341 → 0.329 on the joint set. Removing the 101-word stop list *as well*
   costs 0.341 → 0.207, a 39% relative loss. The single ablation the brief asked for returns
   "barely moves", and that answer is a trap.

**The failures do not correlate.** On 82 queries both tools can answer, `phi = +0.058`,
permutation `p = 0.76`. Statistically indistinguishable from independence. The two tools fail on
different questions for different reasons, which is what you would expect from opposite-sign use
of the same quantity rather than from a shared defect.

**Transferable? Yes, and it is measured, not proposed.** Re-ordering `reuse_lookup`'s existing
shortlist by matched-stem specificity, with `fan_in` demoted to a tiebreak, moves strict r@5 from
0.159 to 0.212 over 132 scenarios with **zero recall cost** (nothing is discarded; only the
reading order moves). The added cost is 0.005 s. The `df` it needs is **not** the one already
inside `build_reference_index` — that one is `fan_in` restated. Details in §D.

---

## §A — The two ranking functions, characterised from source

### A.1 `codebase-map`

Matching, `reuse_lookup.assemble_shortlist`: a candidate is a **seed** iff
`stems(query) & stems(name)` is non-empty. That is a **boolean** test. No weight, no count, no
notion that one stem is rarer than another.

Ranking, `reuse_lookup.py:246`:

```python
ranked.sort(key=lambda r: (not r.is_seed, -r.fanin, r.candidate.name))
```

Seeds before neighbours, then **fan-in descending**, then name. And `map_lib.py:828`:

```python
return len(index.get(symbol_id, set()) - {def_file})
```

`index` is `build_reference_index`'s `token -> {files mentioning it}`. So `fan_in(name)` is
`|postings(name)| − 1`: **the document frequency of the identifier over the code corpus, minus its
own def file.** Measured, not inferred:

```
python scratchpad/m3/char.py <repo> scratchpad/m3/char.json
  symbol candidates with a def file: 645
  distribution of (identifier-DF − fan_in):  delta=+1  n=645  (100.0%)
  Spearman fan_in vs identifier-DF:  rho = +1.0000
```

Where does df enter? **At the ranking, with a positive sign.** Nowhere else. There is a 21-word
English stop list (`map_lib._STOPWORDS`) that keeps `the`/`of`/`for` out of the stem sets, and
tokens shorter than 2 characters are dropped. Neither touches the code vocabulary — `run`, `read`,
`key`, `main`, `check`, `resolve` all survive and all rank at the top.

The seed set is wide and unweighted. Over the 132 graded scenarios:

```
python scratchpad/m3/wider.py <scratch> <repo>
  seeds per query: min 6  median 63  mean 65.6  max 158
  widest-pulling query stems actually used:
     stem test    pulls 128 candidates    stem check  pulls 37 (used by 17 of 132 queries)
     stem read    pulls  40 candidates    stem run    pulls 25 (used by 26 of 132 queries)
```

A query containing "test" admits 128 of the 839 candidates on equal footing, and the 128 are then
ordered by which identifier is most common in the tree.

### A.2 `memory-recall`

Two substrates, and df enters each at a different place.

**`bench.run_grep`** — the corpus's pre-index retrieval path. df enters at **term selection**
(`bench.py:298`):

```python
needle = min(ts, key=lambda t: (dfreq.get(t, 0) == 0, dfreq.get(t, 10**9)))
```

Rarest content word wins; a term absent from the corpus is pushed last by the first tuple element
so an out-of-vocabulary word never becomes the needle. The *result list is unranked* — corpus
order, first `k` matches. So for grep, the idf **is** the entire ranking function.

**`bench.run_fts` / `query.py`** — the shipped CLI path. `query.py:654` issues the same
`ORDER BY bm25(d, 1.0, 1.0, ALIAS_WEIGHT)` as `bench.py:172`, so what is measured here is what
ships. df enters at **scoring**, inside SQLite's `bm25()`. I did not take its shape on trust:

```
python scratchpad/m3/bm25_probe.py
  synthetic corpus N=100, term "common" in 90 docs, "rare" in 2, equal doc lengths
  rare-only doc   score 3.660336
  common-only doc score 0.000001
  okapi idf(2)  = +3.673766      okapi idf(90) = −2.153975
```

fts5 uses Okapi `idf = log((N−n+0.5)/(n+0.5))` **clamped to 1e-6 when negative**. The clamp is the
sharp part: idf goes non-positive at `n ≥ N/2`, so **a term appearing in half the corpus or more
contributes literally nothing to the score.** `memory-recall` does not merely down-weight a common
term. It deletes it.

There is a second df correction upstream of that: `bench.terms()` drops a **101-word** stop list
and every token of length ≤ 2 before a query is ever built. Those words are the corpus's
highest-df terms by a wide margin — `the` 791/907, `a` 663/907, `and` 631/907, `is` 524/907. A
hand-authored idf, applied as a hard filter. §C shows this matters enormously.

### A.3 The comparison, stated once

| | `codebase-map` | `memory-recall` |
|---|---|---|
| what is scored | a candidate **name** | a **document** |
| match | boolean stem intersection | boolean OR over content terms |
| the df quantity | `fan_in` = df of the matched name in code | `n` = df of the query term in the corpus |
| **sign** | **higher df ranks HIGHER** | **higher df ranks LOWER, and is zeroed past N/2** |
| second df correction | 21 English glue words | 101 stop words + len ≤ 2, and the bm25 clamp |

They are the same quantity used with opposite sign. That is why I do not accept "shares a
mechanism" as stated, and also why I do not dismiss the premise: the owner's intuition points at
the right variable.

One honest complication. In IR terms `fan_in` is defensible as a **document prior** ("this seam is
hot"), not as an inverted idf. The trouble is that in a code corpus the popularity of an identifier
and the commonness of the English word are **the same number** — `run` is popular *because* it is a
word everybody reaches for. So the prior and the term weight are physically identical and pull in
opposite directions, and `reuse_lookup` resolves that conflict in favour of the wrong one.

---

## §B — One query set both tools can answer

**Construction** (`scratchpad/m3/build_joint.py` → `m3/joint.json`). A reuse-audit question
recorded verbatim in a spec's §10 has, at HEAD, two answers: the **code** the unit actually
touched (scen-1's `expected_files`, derived from git, never from the spec's prose) and the
**decision record** it left behind (its own id, when that id is a document in the extracted
`records` set). 82 of scen-1's 132 graded rows satisfy both; 50 drop because the spec id is not a
records document.

```
joint set: 82 queries (67 distinct) from 132 graded scen-1 rows
record_overlap  min 0.000  mean 0.206  max 1.000   (check-recall.py's anti-tautology measure)
rows above OVERLAP_MAX 0.60: 5
```

Both sides carry the **same** anachronism — the answer post-dates the question — which is why this
set compares the two tools *to each other* and is not quoted as either tool's absolute performance.

**Scores at HEAD** (`m3/run_map.py`, `m3/ablate.py`):

```
memory-recall (fts5, shipped)   r@1 0.195  r@5 0.341  r@10 0.402  r@20 0.500  MRR 0.262
reuse_lookup  (strict)          r@1 0.061  r@5 0.183  r@10 0.232  r@20 0.256  MRR 0.113
reuse_lookup  (feature-resolved) r@1 0.061 r@5 0.268  r@10 0.549  r@20 0.805  MRR 0.188
```

*strict* = a candidate hits only via its own printed def file. *resolved* = feature-tagged
candidates (inventory keys, affordance seams) additionally hit when their dossier **owns** one of
the expected files, via `map_lib.attribute_paths`. That resolution step was specified by the scen-1
phase and never run; this is its first end-to-end execution. It is much coarser — a dossier owns
many files — so read *resolved* as "the right area", not "the right file".

**Do the failures correlate? No.** (`m3/correlate.py`, 20 000-trial permutation test holding both
marginals.)

```
memory-recall@5 vs reuse_lookup@5 (strict)     both 6 | only recall 22 | only map 9 | neither 45
   expected-if-independent 'both' = 5.1 ; observed 6   phi = +0.058  p = 0.7646
memory-recall@10 vs reuse_lookup@10 (strict)   phi = +0.080  p = 0.6009
memory-recall@5 vs reuse_lookup@5 (resolved)   phi = +0.086  p = 0.6017
```

Positive but nowhere near significant. If the two tools shared a defect, their per-query successes
should co-vary; they do not. What co-varies is *nothing* — 22 queries only `memory-recall` gets, 9
only `reuse_lookup` gets, 45 neither.

**Slices, because a headline number here is cheap** (r@5):

```
slice                                      n   recall  map-strict
all                                        82  0.341   0.183
record_overlap <= 0.30 (low leakage)       61  0.230   0.213
record_overlap >  0.60 (tautological)       5  0.800   0.200
max_file_freq >= 20 (guessable file)       65  0.262   0.123
max_file_freq <  10 (rare file)             5  0.600   0.200
deduped to distinct queries                67  0.328   0.119
```

On the low-leakage slice — where the record does not simply restate the question — the gap between
the tools **closes to 0.230 vs 0.213**. `memory-recall`'s headline advantage on this set is largely
the five tautological rows plus vocabulary the record shares with the question. Say that plainly:
the joint set shows the two tools are *comparably bad* at this, not that one is good.

---

## §C — The decisive test

### C.1 The naive ablation, and why it misleads

`m3/ablate.py`. Seven arms over identical query/target pairs. `py_idf` is a pure-python
re-implementation of fts5's bm25 (three columns, weights `1.0/1.0/0.4`, k1 1.2, b 0.75, clamped
Okapi idf) whose only purpose is to make the ablation arms credible. It reproduces the shipped
substrate **exactly**: mean Jaccard of top-10 against sqlite = **1.000** over 82 queries, and every
metric matches to 4 decimals.

```
                    JOINT 82                FIXTURE 12              SCEN-2 95
arm                 r@1    r@5    r@20      r@1    r@5    r@20      r@1    r@5    r@20
grep_rarest (ship)  0.061  0.146  0.220     0.083  0.167  0.167     0.074  0.105  0.116
grep_first          0.037  0.085  0.244     0.167  0.333  0.333     0.032  0.074  0.137
grep_common         0.012  0.049  0.146     0.083  0.500  0.500     0.011  0.074  0.126
fts5 (shipped)      0.195  0.341  0.500     0.583  0.833  0.833     0.232  0.368  0.474
py_idf (control)    0.195  0.341  0.500     0.583  0.833  0.833     0.232  0.368  0.474
py_noidf            0.159  0.329  0.537     0.500  0.750  0.833     0.200  0.358  0.442
py_invidf           0.110  0.146  0.317     0.417  0.500  0.583     0.158  0.221  0.326
```

Read straight, this says **idf barely matters**: `py_noidf` costs 0.012 r@5 on the joint set, 0.010
on scen-2, and *gains* 0.037 at r@20. That is the answer the brief's experiment returns, and I
believe it is wrong as an account of the mechanism.

The grep arms are messier than they look. `grep_common` beats `grep_rarest` on the 12-query shipped
fixture (0.500 vs 0.167) and loses on both larger sets. That inversion is an artifact, not a
finding — see C.4.

### C.2 The 2×2 that settles it

If removing idf costs nothing, the obvious rival explanation is that something else already did the
job. `bench.terms()` deletes the 101 highest-df words before scoring. Test both together
(`m3/stoplist.py`):

```
                                    JOINT 82   FIXTURE 12   SCEN-2 95      (r@5)
py_idf          (stop, idf)          0.341      0.833        0.368
py_noidf        (stop, no idf)       0.329      0.750        0.358
py_idf_nostop   (NO stop, idf)       0.329      0.750        0.368
py_noidf_nostop (NO stop, no idf)    0.207      0.500        0.263
```

That is the answer. **The stop list and bm25's idf are redundant df corrections. Either one alone
recovers almost all of the protection. Removing both costs 39% of r@5 on the joint set, 40% on the
fixture, 29% on scen-2.** Ablating one and concluding "df does not matter" is exactly the
guard-that-shares-a-variable-with-the-thing-it-guards error, one level up: the backstop covered for
the removal.

So: **yes, df correction is what protects `memory-recall`.** It is applied twice, and the
measurement only shows it when both copies are removed.

### C.3 The transplant, both directions

Ablation asks "what if the correction were absent". The stronger question is "what if it were
*inverted*", because inverted is what `codebase-map` actually does.

**`reuse_lookup`'s algorithm ported onto the records corpus** (`m3/port.py`). A record's fan-in is
how many *other* records cite its id — the same "referenced from N distinct places" quantity, on
the other corpus. Boolean OR match, then sort:

```
                    JOINT 82           FIXTURE 12         SCEN-2 95        (r@1/5/10/20)
port_fanin_desc   0.024/0.073/0.134/0.195  0.000/0.000/0.083/0.167  0.000/0.000/0.021/0.074
port_fanin_asc    0.012/0.024/0.049/0.049  0.000/0.000/0.083/0.083  0.000/0.000/0.032/0.042
port_corpus_order 0.024/0.061/0.110/0.207  0.000/0.500/0.833/1.000  0.011/0.074/0.126/0.179
```

On scen-2 (n = 95, the largest set with neutral corpus order) **sorting by fan-in descending is
worse at every k than leaving the identical match set in arbitrary file order.** Not "a weaker
signal than bm25" — worse than no signal. And `port_fanin_asc` is also worse, so this is not a
simple sign error: record-fan-in is close to noise, and sorting a match set by noise costs you the
ordering you had.

The joint 82 does not reproduce that cleanly — `port_fanin_desc` edges corpus order at r@5 (0.073
vs 0.061) and loses at r@20 (0.195 vs 0.207). Call it a tie there. The claim rests on scen-2, and
on the fixture only after C.4's positional confound is accounted for, which removes it as evidence
in either direction.

`fan_in` on the *code* corpus is not pure noise — it is anti-correlated with what the query wanted,
because the highest-fan-in identifiers are the commonest English words. Which is the same failure
with a mechanism attached.

**bm25's shape ported into `reuse_lookup`** (`m3/shape.py`), over all 132 graded scenarios. Every
arm re-orders the *same* shortlist, so recall@len is unchanged by construction and nothing is
discarded:

```
key            r@1     r@3     r@5     r@10    r@20    MRR      (strict, n=132)
map_shipped    0.053   0.106   0.159   0.220   0.242   0.102
map_lexico     0.023   0.152   0.212   0.265   0.303   0.103    <- specificity, fan_in as tiebreak
map_idfonly    0.023   0.136   0.205   0.258   0.303   0.102
map_bm25ish    0.038   0.129   0.159   0.220   0.242   0.100    <- idf x log1p(fan_in), multiplicative
map_faninasc   0.015   0.030   0.030   0.098   0.250   0.045    <- sign-flip control
map_namesort   0.023   0.030   0.030   0.098   0.235   0.048    <- no popularity signal control

sole-attribution subset (evidence not inherited from a sibling unit closed in the same commit):
map_shipped    0.022   0.054   0.098   0.152   0.174   0.056
map_lexico     0.011   0.120   0.163   0.207   0.239   0.075    <- MRR +34% relative
```

Three things fall out. The lexicographic shape (specificity first, `fan_in` as tiebreak) wins at
every k from 3 up. The **multiplicative** bm25 shape does *not* — `log1p(fan_in)` re-dominates and
collapses back onto the shipped numbers, so "just multiply by idf" is the wrong transfer. And both
controls (`faninasc`, `namesort`) sit far below everything, which is the check that matters: the
gain is not "burying common names", because burying them without a specificity signal scores 0.030.

`map_shipped` still wins at r@1 (0.053 vs 0.023). Sometimes the hottest seam *is* the answer. So
the recommendation in §D is a composite key, not a replacement.

### C.4 What I do not claim from these numbers

`port_corpus_order` is **not** a neutral baseline on the shipped 12-query fixture. Its targets sit
at corpus positions with median 32 of 907, clustered at the front of the file listing, so "corpus
order" is a strong prior there by accident. On JOINT (median 310) and SCEN-2 (median 453) it is
neutral, and those are the sets I read the claim off. Same reason `grep_common` "wins" the fixture:
it returns early docs and the fixture's answers are early docs. n=12 with a positional confound
supports nothing.

---

## §D — Is a df correction transferable to `fan_in`?

**Yes for the ranking. No for the seam threshold. And the df you want is not the one already
computed.**

### D.1 The trap: which df

`build_reference_index` already computes, for every one of 4934 tokens, the set of files mentioning
it. `|postings(t)|` is a df, it is free, and it is **useless here** — because it is `fan_in + 1`
exactly for 645/645 symbols, `rho = +1.0000`. An "idf correction" computed over that corpus is
`sort ascending by fan-in`, which is the `map_faninasc` control above, and it scores 0.030 at r@5.
A previous phase reached the same conclusion and stopped there. That stopping point is correct
about that corpus and wrong about the design.

The df that carries information is over a **different population**: the candidate pool itself.
`stemdf(s)` = how many of the 839 merged candidates carry stem `s`. It is a different number:

```
python scratchpad/m3/char.py …
  Spearman fan_in vs min_stemdf:  rho = +0.1653   (n = 645)
```

Nearly uncorrelated. The two extremes show why:

```
top by fan_in (ranked first today)        rarest-stemmed seams (a bm25 would rank first)
main       fan_in 37  min_stemdf  2       leading_verb        fan_in  4  min_stemdf 1
resolve    fan_in 26  min_stemdf 36       seam_fanin_threshold fan_in 3  min_stemdf 1
check      fan_in 19  min_stemdf 37       compute_coverage    fan_in  4  min_stemdf 1
run        fan_in 28  min_stemdf 25       regen_cmd           fan_in  3  min_stemdf 1
```

`resolve` and `check` are top-ranked *and* share their stem with 36 and 37 other candidates — the
query stem that matched them matched a third of the pool. That is precisely the case bm25's idf
exists to suppress, and `reuse_lookup` promotes it.

### D.2 The shape

The measured winner is lexicographic, not multiplicative:

```python
ranked.sort(key=lambda r: (not r.is_seed,
                           matched_stemdf(query, r.candidate.name),   # NEW: rarest matched stem
                           -r.fanin,                                   # unchanged, now a tiebreak
                           r.candidate.name))
```

where `matched_stemdf` is `min(stemdf[s] for s in stems(query) & stems(name))`, and a structural
neighbour — which matched nothing — keeps a sentinel that sorts it after every seed, exactly as
today. Two changes to two lines, both inside `assemble_shortlist`, both pure.

Because `map_shipped` still wins at r@1, a naive swap trades r@1 for r@3–r@20. So I measured the
composite rather than proposing it (`m3/composite.py`): give slot 1 to the single highest-fan-in
seed, order every other seed by specificity, leave neighbours alone.

```
key              r@1     r@3     r@5     r@10    r@20    MRR      (strict, n=132)
map_shipped      0.053   0.106   0.159   0.220   0.242   0.102
map_lexico       0.023   0.152   0.212   0.265   0.303   0.103
map_composite    0.053   0.121   0.212   0.258   0.303   0.110   <- >= shipped at every k AND on MRR
map_composite2   0.053   0.106   0.197   0.258   0.303   0.110   <- two hot slots is worse than one

sole-attribution subset:
map_shipped      0.022   0.054   0.098   0.152   0.174   0.056
map_lexico       0.011   0.120   0.163   0.207   0.239   0.075
map_composite    0.022   0.065   0.152   0.196   0.239   0.066
```

**`map_composite` is a Pareto improvement over the shipped key** on this set: equal or better at
every k measured, and better on MRR (0.110 vs 0.102). It gives up `map_lexico`'s r@3 (0.121 vs
0.152) to buy back r@1. Reserving *two* slots for fan-in is worse than reserving one, which is
itself a small piece of evidence for the direction of the effect. That is the shape I would land,
and it is 0.005 s of extra work.

**What must NOT change:** `SEAM_FANIN_THRESHOLD` and the `SEAM` label. `fan_in >= 3` is shared with
`map_diff --converge` and `seed_affordances`, and it answers a different question ("is this
referenced widely enough to be worth declaring") from the one ranking answers ("did this match the
query specifically"). Re-defining a seam would break the convergence worklist to fix a sort order.

### D.3 Cost

```
python scratchpad/m3/correlate.py …    (node d, single readings, AV taxes each exec ~0.022 s)
  load_corpus                        0.006 s
  build_reference_index              0.626 s    <- unchanged, already paid on every run
  stem posting list over 839 cands   0.005 s    <- the entire added cost
  assemble_shortlist, per query      0.0109 s
```

**0.005 s, once per process, stdlib only, no new parsing, no new artifact, nothing committed.** The
posting list is built from `map_lib.stems` over names already in memory. It is derived live, so
there is nothing to keep fresh and drift is structurally impossible — the §12 rule for a
same-language single consumer.

### D.4 What this does not fix

Nothing here touches recall. The adversarial set measured 17 of 28 as **recall misses** — names the
shortlist never contained — and no re-ordering reaches those. The scen-4 set found `read` and
`merge` pointing at the wrong file because `load_corpus.merge` keeps `file or prev.file` and
discards 124 of 769 definers; that is a data-model defect, not a ranking one. A specificity
re-rank is a real but bounded improvement to the *order* of a shortlist whose *contents* are the
larger problem.

---

## §E — What would falsify this

- **On A.1:** show a corpus where `identifier-DF − fan_in ≠ 1`. It would take a symbol whose def
  file never mentions its own name.
- **On C.2:** run the 2×2 on a corpus whose stop-list words are *not* the highest-df terms. If
  `py_noidf_nostop` does not collapse there, the redundancy claim is corpus-specific.
- **On C.3:** a set where `port_fanin_desc` beats `port_corpus_order`. One exists in principle —
  a corpus where citation count predicts relevance — and this repo's records are not it.
- **On D.1:** if `min_stemdf` and `fan_in` correlate strongly in an adopting repo (rho ≫ 0.17),
  the transfer degenerates into `faninasc` and the recommendation is void. `char.py` re-derives
  the rho in any repo; run it before adopting.

## §F — Caveats

- **One repo, one corpus, one node.** 907 records, 839 candidates, 132 scenarios drawn from 26
  days of this tool's own home tree. Nothing here says how either tool behaves elsewhere, and the
  `codebase-map` half is Python/JS only — 94 tracked shell scripts are outside its symbol corpus
  and `reuse_lookup` prints a partial-recall notice for them on every run.
- **The joint set is anachronistic on both sides.** Every target post-dates its question. It is
  used to compare the tools to each other, never as an absolute score, and the low-leakage slice
  (0.230 vs 0.213) is the honest read of the gap.
- **82 rows, 67 distinct queries.** 20 queries are shared across sibling specs recorded in the same
  build. The deduped row is reported; treating the 82 as independent samples over-counts those.
- **`resolved` mode is coarse.** A dossier owns many files, so a "hit" there means the right area.
  It is reported beside `strict` and never instead of it. Its large jump under `namesort`
  (0.598 vs 0.268) is substantially an artifact of feature-tagged candidates having `fan_in = 0`
  and therefore sorting last under the shipped key — a real effect, but its size is inflated by
  the coarse target.
- **`py_idf` matching fts5 exactly is a strong control but not a proof of the ablations.** It shows
  my scorer reproduces the shipped ranking; it does not prove `idf(t) := 1` is the only thing that
  changed in `py_noidf`. I read the diff of the two call sites; that is the extent of the check.
- **The permutation test assumes exchangeability under the null** and holds both marginals fixed.
  With 82 rows and success rates of 0.34 and 0.18 it has limited power: it can rule out a strong
  correlation, not a weak one. A `phi` of +0.06 is *consistent with* independence, not proof of it.
- **The record fan-in in C.3 is a citation count over 907 documents, mean 1.29, median 1.** That is
  a thin graph and the arm inherits its thinness; the claim rests on `port_fanin_desc` losing to
  corpus order, which is robust to the graph being thin, not on the exact values.
- **`map_composite` is tuned on the set it is scored on.** "Reserve one slot" was chosen after
  seeing that `map_shipped` won r@1; reserving two was then measured and lost. That is one
  hyper-parameter fitted on 132 rows with no held-out split, so treat the composite's margin over
  `map_lexico` as suggestive and the margin of both over `map_shipped` as the durable part.
- **The 132-scenario ground truth is inherited** from the scen-1 phase, including its
  commit-message attribution, its 25-file sweep cutoff, and its `memory/**` exclusion. I re-scored
  against `expected_files_sole_attribution` throughout precisely because 40 of the rows have
  inherited evidence, and the conclusions hold on that subset.
- **Everything is HEAD-specific** at `991153457d`. `fan_in`, `stemdf` and every rank move with the
  tree.

## §G — Reproduction

All scripts in `scratchpad/m3/`, run with the repo as cwd, stdlib only, offline.

```
python m3/char.py      <repo> m3/char.json        # A.1  fan_in == df, and the stemdf rho
python m3/bm25_probe.py                           # A.2  where df enters fts5's bm25
python m3/build_joint.py <scratch> <repo>         # B    the 82-query joint set
python m3/run_map.py   <scratch> <repo>           # B    reuse_lookup scored on it
python m3/ablate.py    <scratch> <repo>           # C.1  the 7-arm ablation + the fts5 control
python m3/stoplist.py  <scratch> <repo>           # C.2  THE 2x2 -- the decisive one
python m3/port.py      <scratch> <repo>           # C.3  the transplant, both directions
python m3/wider.py     <scratch> <repo>           # C.3  n=132 re-rank + seed-set shape
python m3/shape.py     <scratch> <repo>           # D.2  the candidate re-ranking shapes
python m3/correlate.py <scratch> <repo>           # B    phi + permutation test + cost
python m3/composite.py <scratch> <repo>           # D.2  the composite key
```

**Cost is a verdict, so here is the bill, timed rather than guessed.** The whole set re-runs in
**27 s** on node `d` — char 1.6 / bm25_probe 0.2 / build_joint 0.1 / run_map 1.9 / ablate 2.4 /
stoplist 3.0 / port 2.9 / wider 3.2 / shape 4.5 / correlate 2.7 / composite 4.4. No agents, no network, no
dependency outside the standard library. `git status --porcelain` empty before and after; the
tracked tree was never written to.
