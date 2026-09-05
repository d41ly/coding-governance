**Serves:** research TOOL-dTracedLattice-1 TOOL-dTracedLattice-7

# Recall, measured against scenarios — `reuse_lookup` and `memory-recall`

*Synthesis over 4 scenario sets (320 scenarios), 4 measurement passes and 38 adversarially verified
claims. Node `d`, 2026-09-05. Repo HEAD `991153457d30c923151d749e12afedd4e9176689`, tracked tree
clean. Sources: `scen-1-replay.json` `scen-2-recall.json` `scen-3-adversarial.json`
`scen-4-orientation.json`, `meas-1-lookup.md` `meas-2-recall.md` `meas-3-shared.md`
`meas-4-cost.md`, `refute-recall-1.md` … `refute-recall-5.md`, all under this scratchpad.*

---

## 0. The answer, before the tables

**Do not ship the confidence re-rank.** On the one set built to test exactly this question it takes
recall@5 from 11/28 to 2/28, nine surfaced answers move down and none moves up, McNemar exact
p = 0.0039. That verdict survived a full adversarial pass; four of the arguments originally offered
for it did not.

**But the design pass was not measuring a phantom.** Its 1.6%→80.0% precision@5 lift transfers to
the per-query shortlist essentially intact (28.3% → 81.7% at p@5 over 179 shortlists, against a
39.6% random-order control). Re-ranking by confidence really does put symbols with cleaner
ast-resolved import edges first. It does that and still fails, because **edge precision does not
predict whether the shortlist named a file the unit went on to change.** The yardstick was wrong,
not the arithmetic.

**The owner's premise is right about the variable and wrong about the mechanism.** `fan_in` IS a
document frequency — identifier-DF minus `fan_in` = +1 for 645/645 symbols, rho = +1.0000 — and
`reuse_lookup` sorts it DESCENDING while `memory-recall`'s bm25 weights the same quantity inversely
and zeroes it past N/2. Same quantity, opposite sign. They do not share the defect.

**What to spend on instead, in order:** the name-merge defect (124 of 769 definers unreachable),
retrieval (17 of 17 adversarial misses fail on empty stem intersection and no K reaches them), and
only then a stem-specificity secondary sort key that costs 0.0164 s and needs a held-out split
before anyone believes its margin.

---

## 1. THE REAL NUMBERS

Rules observed throughout: GRADED and STABILITY-ONLY are never averaged; every figure carries its n
and the command; a figure that could not move is reported as unable to move rather than as a score.

### 1.1 `reuse_lookup` — lens 1, the 132 graded replay scenarios

Ground truth is the product files each closed unit actually changed, derived from git, never from
the spec's own prose. Replayed at each spec's own `base_sha` (129 of 132 resolve; 3 fall back to
HEAD). **any-hit** = at least one expected file reachable within K.

**Arm A — file granularity, feature rows expanded through their dossier's `[paths].globs`.**

| ordering | @1 | @5 | @10 | @20 | @all |
|---|---|---|---|---|---|
| shipped | .068 | .303 | .606 | **.742** | .848 |
| confidence re-rank (harness predicate) | .045 | .220 | .303 | **.530** | .848 |
| confidence re-rank (design pass's own predicate) | .053 | .295 | .485 | .614 | .848 |
| `fanin_asc` | .227 | .538 | .727 | **.788** | .848 |

`python m1/analyze1b.py` (n=132) for rows 1, 2 and 4; `python sk1/verify_faithful.py` for row 3.
**The @20 column is corrected.** `m1/score1c.py` initialises `per['20']=[]` and never fills it when
a shortlist is shorter than 20, so three scenarios recorded recall@20 below recall@10 — impossible
for a cumulative measure. Published .720/.508/.765 become .742/.530/.788 (skeptic [10],
`refute-recall-2.md`). The lost/gained comparisons are unaffected.

**Two predicates, and the difference is most of the magnitude.** `rerank.py` (the design pass)
spells `compound` as `"_" in n or any(c.isupper() for c in n[1:])`; `m1/lib1.py` reimplements it as
`("_" in name.strip("_")) or /[a-z][A-Z]/`. They disagree on 12 of 839 candidates, all uppercase
inventory keys whose rows expand through globs. Under the proposal's own predicate the @5 loss falls
from 11 scenarios to 1 (p=1.00). Report both rows or report neither.

**Arm B — symbol granularity, one file per row. The arm that removes the glob artifact.**

| ordering | @1 | @5 | @10 | @20 | @all |
|---|---|---|---|---|---|
| shipped | .061 | .144 | .182 | .205 | .288 |
| re-rank | .045 | .136 | .189 | .250 | .288 |
| `fanin_asc` | .008 | .030 | .114 | .227 | .288 |
| shipped, **all definers credited** (the name-merge fix) | .106 | .189 | .220 | .242 | .311 |

`python m1/score1c.py` + `python sk1/score_symall.py` (n=132). In 71.2% of graded scenarios **no
symbol row anywhere** points at a file the unit changed. The .848 in Arm A is dossier coverage, not
seam hits — dossier glob fan-out is median 6 files, mean 10.9, max 44 (`python sk1/verify_c6.py`,
n=21 dossiers).

**Arm C — scored against `expected_symbols`: DEAD BY CONSTRUCTION.** any-hit@all = .066 for every
ordering (n=106, `python m1/score1d.py`). `expected_symbols` holds only symbols the unit CREATED,
which did not exist at `base_sha`. Reported as unable to move, not as a low score.

**The control that has to ride with every file-granularity number.** Answer the K globally most
frequently changed files, ignoring the query. In-sample it scores .265/.515/.720/.879; leave-one-out
— the honest form, since the frequency map was fit on the same 132 rows — it scores
**.098/.515/.720/.841** (`python sk1/verify_c7.py`, n=132). It still beats the tool at K=5, 10 and
20 and edges it at K=1. No lens-1 file-recall figure is evidence the tool works. They are valid as
an ordering comparison and nothing else.

**The 47 STABILITY-ONLY replay scenarios are not scored here at all.** Their `expected_files` and
`expected_symbols` are empty by construction; only 32 of 47 carry usable `cited_seams`. Any
precision figure aggregating them with the graded 132 is meaningless.

### 1.2 `reuse_lookup` — the resolution choice moves the answer more than the ordering does

Measurement 4 scored a hit only when a candidate's own def FILE is a truth file, and reported a
36.4% ceiling. That ceiling is a scoring choice, not the tool's reach (`python sk5_b.py`, n=132):

```
reachable, STRICT   (def file only)                48/132 = 36.4%   32 of 152 truth files
reachable, RESOLVED (feature rows via dossier)    112/132 = 84.8%   93 of 152 truth files
```

84.8% independently reproduces measurer 1's Arm A .848. Scored both ways, over all 132:

| arm | mode | @1 | @3 | @5 | @10 | @20 |
|---|---|---|---|---|---|---|
| shipped | strict | 7 | 14 | 21 | 29 | 32 |
| shipped | resolved | 8 | 18 | 31 | 65 | **97** |
| R1-ident re-rank | strict | 6 | 12 | 20 | 28 | 38 |
| R1-ident re-rank | resolved | 6 | 13 | 27 | 38 | **52** |
| R1-text re-rank | strict | 4 | 12 | 18 | 28 | 38 |
| R1-text re-rank | resolved | 6 | 16 | 26 | 36 | 53 |

`python sk5_b.py`, n=132. **Strict says the re-rank wins at @20 (38 vs 32). Resolved says shipped
wins it by 45.** M4's "shipped ahead by one to three scenarios" was an artifact of the resolution it
chose, in both directions. The resolved arm is coarse — it credits "pointed at the owning feature",
not "named the file" — and was checked against being green-by-construction: median one owning
feature per scenario, only 9% of file-less top-20 rows credited (`python sk5_f.py`).

M4's own restricted arm, for the record: over the 48 strict-reachable scenarios, hit@5 is shipped
43.8% / R1-ident 41.7% / R1-text 37.5%, hit@1 14.6% / 12.5% / 8.3% (`python m4/an3.py`). Those gaps
are three discordant scenarios; a sign test on n=3 cannot fall below p=0.25, so that arm could not
have detected an improvement of any size (`python sk4/power.py`).

### 1.3 `reuse_lookup` — lens 3, the 28 adversarial common-name seams

Ground truth is one symbol, so granularity is uniform and no glob artifact exists. HEAD, clean tree.

| ordering | @1 | @5 | @10 | @20 | @all |
|---|---|---|---|---|---|
| shipped | 4/28 | **11/28** | 11/28 | 11/28 | 11/28 |
| confidence re-rank | 2/28 | **2/28** | 2/28 | 4/28 | 11/28 |
| `fanin_asc` | 0/28 | 0/28 | 0/28 | 0/28 | 11/28 |

`python m1/score3.py` and `python sk1/verify3.py` (n=28), reproduced independently and identical
under the design pass's own `compound` predicate (`python sk1/verify_faithful.py`). `fanin_asc`'s
0/28 at every finite K computed separately (`python sk1/verify_c8.py`). Liveness: the harness
recomputes lens 3's independently derived `shipped_rank` 28/28 and its declared tier 28/28.

Of the 11 the shipped order surfaces, all 11 are already inside the top 5 and 9 point at an
acceptable def file.

### 1.4 `memory-recall` — the same gate arithmetic across four classes

`m2/m2_floor.py` imports `check-recall.py` and swaps only the question list; every column is that
program's own. Pin `records:fts5:r@5>=0.81` from `.memory-tree.conf`.

| class | n | ceiling | raw = normalised | vs floor | mean overlap |
|---|---|---|---|---|---|
| CONTROL (the shipped fixture) | 12 | 1.0000 | **0.8333** | ok | 0.362 |
| GRADED | 9 | 1.0000 | **0.0000** | RED | 0.120 |
| STABILITY-ONLY | 74 | 1.0000 | 0.3378 | RED | 0.319 |
| STABILITY-ONLY, overlap-clean | 57 | 1.0000 | **0.1930** | RED | — |
| harvested (GRADED + STABILITY) | 83 | 1.0000 | 0.3012 | RED | 0.297 |

`python tools/memory-recall/check-recall.py` for row 1 (rc=0, raw 0.8333, ceiling 1.0000, h=10 R=12,
(h-1)/(R-1) = 0.8182 under `--audit-fixture`). `python m2/m2_floor.py . m2/fixtures m2/data` for the
rest. **Ceiling is 1.0000 in every class**, so no class contains a dead probe: every expected id
resolves and retrieval simply fails to return it.

`stability-clean` (0.1930) is the number to quote, not `stability` (0.3378) — the 17 excluded rows
are the ones `check-recall --audit-fixture` REDs as written-from-the-record and they score 0.824 at
r@5 because they contain their answer's words.

**GRADED's 0.0000 is a tripwire, not a recall estimate.** n=9, and the class is by construction the
residue of ids the section did NOT attribute to the tool's return (any id also named in a
returned-sentence was demoted to STABILITY). With the sessions' recorded `--terms` those 9 move to
r@5 0.111 / r@20 0.333, so 2 to 3 of them are reachable.

**Substrates, harvested 83, records set** (`python bench.py m2/data m2/fixtures/harvested.json --sets records --subs grep,fts5,fts5w,rm3 --ks 1,5,10,20`):

| substrate | r@1 | r@5 | r@10 | r@20 |
|---|---|---|---|---|
| grep (rarest-needle, corpus order) | 0.07 | 0.10 | 0.11 | 0.11 |
| fts5 (shipped) | 0.18 | **0.30** | 0.36 | 0.42 |
| fts5w | 0.16 | 0.27 | 0.36 | 0.39 |
| rm3 | 0.19 | 0.34 | 0.40 | 0.48 |

**The real CLI path, which the gate cannot see** (`python m2/m2_terms.py`, n=83, `query.query_expr`):
question only 0.325 r@5 / 0.446 r@20; question + the session's recorded `--terms` **0.398 / 0.614**.
`recall-fixture.json` has no `terms` field and `check-recall` ranks the question string alone, while
`query.py` REQUIRES `--terms`. Every gate number in this repo describes the weaker of the tool's two
input paths. Paired over the same 83, the r@20 gain is +16/-2 (p=0.0013); the r@5 gain is +10/-4
(p=0.18) and should not be quoted (`python sk_terms.py`).

### 1.5 The two tools on one question set

82 queries where a recorded reuse-audit question has both a code answer (the files the unit changed)
and a record answer (its own decision id, when that id is a records document).

| tool | r@1 | r@5 | r@10 | r@20 | MRR |
|---|---|---|---|---|---|
| `memory-recall` fts5 | 0.195 | **0.341** | 0.402 | 0.500 | 0.262 |
| `reuse_lookup` strict | 0.061 | 0.183 | 0.232 | 0.256 | 0.113 |
| `reuse_lookup` feature-resolved | 0.061 | 0.268 | 0.549 | 0.805 | 0.188 |

`python m3/run_map.py` and `python m3/ablate.py` (n=82, 67 distinct queries). Both sides are
anachronistic — the answer post-dates the question — so this compares the tools to each other and is
never either tool's absolute score.

---

## 2. DOES RE-RANKING COST RECALL

**Yes, at the K a human reads, and the decisive evidence is the adversarial set.**

### 2.1 The decisive number

recall@5 goes **11/28 → 2/28**. Nine of the eleven surfaced answers move down by a median of 34
ranks, zero move up, McNemar exact two-sided **p = 0.0039** (`python sk1/verify3.py`, n=28). The
result is byte-identical under the design pass's own `compound` predicate, so the predicate defect
that gutted the lens-1 magnitude does not touch this.

| id | symbol | shipped | re-ranked | fan-in | tier |
|---|---|---|---|---|---|
| ADV-04 | `resolve` | **1** | 83 | 26 | 0 |
| ADV-15 | `load_conf` | 2 | 62 | 18 | 2 |
| ADV-13 | `read` | 4 | 62 | 9 | 2 |
| ADV-14 | `write` | 2 | 51 | 19 | 1 |
| ADV-27 | `extract` | **1** | 38 | 7 | 2 |
| ADV-12 | `git` | 4 | 35 | 7 | 2 |
| ADV-11 | `tracked` | 3 | 26 | 7 | 2 |
| ADV-09 | `anchors` | 2 | 20 | 4 | 2 |
| ADV-19 | `merge` | 2 | 15 | 2 | 2 |

`ADV-04 resolve` is the worst and the most instructive: `recall_conf.resolve`, whose docstring says
every module in the kit calls it at import, ranks FIRST today and scores 0/3 on the proposed signal.
It is demoted by the ambient filter — the filter's only catch among the seven highest-fan-in common
names, and that catch is a false positive.

The magnitude has a mechanical cause: because 86.7% of symbols are tier 3, a demoted name is not
moved down a few places, it is moved behind every tier-3 candidate in the shortlist — 61 rows in
ADV-04's case.

**Two caveats that must ride with the number.** "None moves up" is guaranteed rather than observed:
only 2 of the 11 surfaced answers are tier 3 and both already sit at rank 1, so the count that could
have gained is zero. And 23 of 28 scenarios are single-word names, exactly the class the signal's
only working component demotes — 11/28 → 2/28 is a harm probe, not a recall estimate.

### 2.2 On the replay set the loss is real in sign and small in magnitude

Scenarios shipped answered within K and the re-rank did not, Arm A, harness predicate:

```
@1  -3/+0  (p=0.25)     @5  -18/+7 (net -11, p=0.043)
@10 -43/+3 (p<1e-4)     @20 -30/+2 (p<1e-4)      @all  0/0
```

Under the design pass's own predicate the same arm reads @1 -2 (p=0.63), **@5 -1 (p=1.00)**, @10 -16
(p=0.009), @20 -14 (p=0.0013) (`python sk1/verify_sig.py`, n=132). In the symbol-only arm the
re-rank is net **+6 at @20** (p=0.031) and +1 at @10 — the only cells anywhere where it clearly wins,
and they are at a depth nobody scrolls to. On the resolved arm it loses at depth by 45 scenarios
(97 vs 52 at @20).

**The honest summary: the sign is negative at @1 and @5 in all four arm/predicate combinations, and
the only defensible magnitude is lens 3's.** "Costs recall at every finite K" as originally written
is false, and was refuted.

### 2.3 What the re-rank actually is, mechanically

Over 645 HEAD symbols: `not_ambient` fires on 641 (99.4%), `df<=15` on 635 (98.4%), `compound` on
562 (87.1%); tier 3 covers 559/645 (86.7%) (`python sk1/verify_df.py`). Only `compound` has spread,
so the sort does one thing: it pushes single-word names behind everything else. Of the 68 symbols at
or above `SEAM_FANIN_THRESHOLD=3`, **31 are non-compound and are demoted; 37 are compound and are
promoted** (`python sk1/verify_c4.py`) — so "it demotes the seam set" over-claims, and the
defensible form is enrichment: 31 of the 83 demoted symbols are seams (37%) against 37 of 562
promoted (6.6%).

And `df<=15` is `fan_in<=14`: identifier-DF minus `fan_in` = +1 for 645/645 symbols and 769/769
symbol rows, `(df<=15) == (fan_in<=14)` on the same populations, because `map_lib.py:828` is
`len(index[id] - {def_file})` over the very index the DF is read from. Over the 839-candidate pool
the equivalence fails on 3 rows — the inventory keys `print`, `set`, `add`, which take `fanin=0`
because they carry no def file (`python sk1/verify_df.py`). That third term restates the tie-breaker
it sits above; it is not an independent axis. It is also NOT true that the whole signal reduces to a
fan-in band cut: tested directly, zero of 179 orderings are identical to that cut and three quarters
of top-5 memberships differ (`python sk4/m4probe.py`).

### 2.4 The lift the design pass measured is real — on a yardstick that does not predict the answer

Running `rerank.py`'s OWN metric (ast-resolved import-edge precision, same `resolver.json` edges,
same confidence function) over the per-query shortlists `assemble_shortlist` actually emits
(`python sk4/transfer.py`, 179 queries, median 11 edge-carrying symbols per shortlist):

| ordering | p@5 | p@10 | p@20 |
|---|---|---|---|
| shipped | 28.3% | 34.5% | 37.0% |
| confidence re-rank | **81.7%** | 80.6% | 78.1% |
| random shortlist order (chance control) | 39.6% | 45.7% | 46.2% |
| the global 224-symbol list (liveness: reproduces `rerank.py`) | 1.6% | 1.0% | 10.4% |

**The lift transfers.** 2.9x over shipped and 2.1x over chance, on the object the tool emits. So the
reason not to ship is not "the measurement was on the wrong population" — it is that ordering by
confidence puts symbols with cleaner import edges first, everywhere, and doing so does not make the
shortlist name a file the unit changed. Per-row on the answer yardstick the two metrics agree in
sign and differ only in magnitude: tier-3/fan-in-1-2 rows hit 7.7% (70/911) against tier-1/fan-in-18+
rows at 1.5% (1/66) (`python sk5_c.py`) — 5x, not the 131x the edge yardstick reports.

### 2.5 Costs the re-rank carries even where it is neutral

- **37 of the 92 resolvable cited seams currently in a shipped top 5 fall out of it** under R1-ident,
  14 of them in still-live specs; 72 (20 live) under R1-text (`python m4/an8.py`, over 400 scraped
  citations, 188 resolvable). None leaves the shortlist — they move to median rank 60
  (`python sk4/m4probe.py`) — so this is discoverability, not invalidation, and no gate reds
  (`check-memory-hygiene.sh` check 12 is a substring presence test).
- **The tie-break decides more of the answer.** Rank-1 answers decided by nothing but the first byte
  of the name: 17.9% shipped, 36.3% R1-ident, **53.6% R1-text** (`python sk5_a.py`, n=179). A
  candidate with no def file has df=0, scores a full 3, and a name starting with a backtick beats
  every lowercase name alphabetically.
- **The raw-text spelling punishes a name for being documented.** `boundedParallel` has
  identifier-DF 4 and text-DF 63 and is demoted out of the top 5 for both specs citing it — the one
  fan-out seam the charter names by hand.

### 2.6 Cost

Quote the ratios, not the seconds — every timing on node `d` is a single draw on an instrument this
repo already documents as 3x-variable, and re-running M4's own script moved its denominator 42% and
its numerator 34% (`python m4/cost.py`, re-run under skeptic [31]).

| stage | re-measured median | as published |
|---|---|---|
| the re-rank sort itself | +9 µs | +21 µs |
| confidence tier for all 839 candidates (identifier DF) | 0.000299 s | 0.00035 s |
| raw-text DF over 1520 tracked files (**R1-text**) | 1.554 s (n=5) | 2.368 s |
| `build_reference_index` | 1.082 s (n=7) | 1.155 s |
| end-to-end `reuse_lookup.py` | 0.936 s (n=7) | 1.605 s |

**"Needs no new parsing" is true of the identifier spelling and false of the text spelling**, which
adds a second full-corpus scan that more than doubles the command. That conclusion is structural and
survives the timing disagreement.

---

## 3. RETRIEVAL PROBLEM OR PRESENTATION PROBLEM

Different fixes, so the split is worth making per tool and per lens. It comes out differently on the
two lenses and both answers are real.

### 3.1 `reuse_lookup`, lens 3 — pure RETRIEVAL, and no K reaches it

```
recall@20 == recall@all == 11/28
```

All 17 misses ARE in `corpus.candidates`, and all 17 fail because
`m.stems(query) & m.stems(name)` is EMPTY (`python sk1/verify_c5.py`, n=17/17). Worked examples:

- `subtokens` against *"split a camelCase or snake_case identifier into lowercase word pieces"* —
  query stems `{camel, cas, identifi, lowercas, piec, snak}` against name stems `{subtoken}`.
- `fan_in` against *"count how many files reference a symbol"* — `{count, fil, how, many, referenc,
  symbol}` against `{fan}`.
- `unfenced` / `unfenced_lines` fail on stemmer granularity alone: the query stems to `fenc`, the
  name to `unfenc`.

One entry route the original claim missed: all 17 DO sit in the uncapped structural-neighbour set
and are cut by `NEIGHBOUR_CAP = 12`, which pre-selects neighbours ALPHABETICALLY before the fan-in
sort. That attack fails on impact — lifting the cap to infinity puts **0 of 17 inside K=20** (best
is `run` at rank 35 of a 639-row list) (`python sk1/verify_c5b.py`). So the operative conclusion
stands: no ordering and no K reaches these.

### 3.2 `reuse_lookup`, lens 1 — a genuine presentation component, plus a granularity defect

Splitting the 132 graded scenarios by where the shipped tool's failure lives, on the corrected @20
figures:

```
20 of 132 (15.2%)   RETRIEVAL   no expected file anywhere in the shortlist, at any rank
14 of 132 (10.6%)   PRESENTATION  the answer is in the list, below rank 20
98 of 132 (74.2%)   answered within 20
```

`python m1/analyze1b.py` with skeptic [10]'s @20 correction applied. Median shortlist is 52 rows;
the presentation group's median is **75 rows, max 111**, and only 9 of 132 shortlists fit inside 20.
Those 14 are what a cap or a better order can buy — and the confidence re-rank buys none of them.

The retrieval group includes `TOOL-aRootedPrefix-1`, whose query is *"resolve the repo root of a kit
installed under a path prefix by finding its conf"* against a corpus containing `resolve_root`, and
which returns an **empty shortlist**.

**A third category the retrieval/presentation dichotomy hides: GRANULARITY.** `load_corpus.merge`
keeps `file or prev.file`, so 124 of 769 symbol definitions (16.1%) are unreachable — the shortlist
prints one arbitrary definer per name. `repo_root` has four definers and prints one;
`boundedParallel` has three and prints one. Crediting every definer lifts Arm A @1 from .068 to .114
and @5 from .303 to .348, and symbol-only @1 from .061 to .106 with @all from .288 to .311
(`python sk1/score_symall.py`). **Duplicates are exactly what a reuse audit hunts, so the tool is
least reliable on the class of finding §10 exists to produce.**

### 3.3 `memory-recall` — overwhelmingly RETRIEVAL

**50 of 95 questions return NOTHING at any k up to 20** (48 of the 83 harvested, 2 of the control's
12) (`python -c` over `m2/per-query.json`). And recall is close to a step function of one variable —
the question's lexical overlap with its target documents, measured with `check-recall`'s own
anti-tautology statistic:

| overlap band | n | r@1 | r@5 | r@10 | r@20 |
|---|---|---|---|---|---|
| 0.00–0.10 | 23 | 0.000 | **0.000** | 0.000 | 0.000 |
| 0.10–0.20 | 16 | 0.000 | 0.125 | 0.125 | 0.250 |
| 0.20–0.30 | 18 | 0.000 | 0.222 | 0.333 | 0.389 |
| 0.30–0.45 | 13 | 0.462 | **0.692** | 0.769 | 0.769 |
| 0.45–0.60 | 8 | 0.625 | 0.750 | 1.000 | 1.000 |
| 0.60+ (tautological, never averaged in) | 17 | 0.647 | 0.824 | 0.824 | 0.941 |

`python m2/m2_overlap.py`, n=95. The shipped fixture's mean sits at 0.362, just above the knee; the
harvested set at 0.297, just below it. This survived three attacks (`python sk3/p17.py`): the
targets come from `bench.expected_by_target`, i.e. the ground truth, not from retriever output;
equal-COUNT quintiles put their largest jump at the same place; and restricted to the 86 reachable
rows, the median rank of the first true target by band runs **334 / 45 / 24 / 2 / 1 / 1**, so the
relation holds with the definitional floor removed entirely.

Presentation is almost irrelevant here. Adding the chunks index to the records one buys +0.012
recall@20 for +108% snippet bytes on the harvested set and +0.000 on control and graded
(`python union.py m2/data m2/fixtures/harvested.json --k 20 ...`). The lever is the QUERY: the
recorded `--terms` rewrite is worth +0.168 at r@20 (p=0.0013).

**The fix is a better bridge into the vocabulary, not a better order.** For `reuse_lookup` that is a
behaviour-phrase-to-seam matcher; for `memory-recall` it is `--terms`, which already exists and
which the gate cannot see.

---

## 4. THE SHARED-MECHANISM VERDICT

**Refuted at the ranking layer. Confirmed at a layer nobody was looking at.**

### 4.1 They share the quantity and apply it with opposite sign

`map_lib.py:828` is `len(index.get(symbol_id, set()) - {def_file})` over
`build_reference_index`'s `token -> {files}` map. So `fan_in` is that identifier's document
frequency minus its own def file. Measured: **identifier-DF minus `fan_in` = +1 for 645/645 distinct
symbol ids and 769/769 symbols.json rows, Spearman rho = +1.0000, and zero def files are absent from
their own postings** (`python sk3/p20.py`, `python m3/char.py`). This is closer to a theorem than a
measurement, which strengthens it.

`reuse_lookup.py:246` then sorts `(not is_seed, -fanin, name)` — **higher df first**.

`memory-recall` does the opposite twice over. `bench.run_grep` picks the argmin-df needle and returns
unranked corpus order, so idf IS the whole ranking there. `query.py:654` and `bench.py:172` both
`ORDER BY bm25(...)`, and SQLite's bm25 uses Okapi `log((N-n+0.5)/(n+0.5))` **clamped to 1e-6 when
non-positive**. I swept the clamp rather than taking two points: at N=100 the single-term score is
0.0387 at n=49 and 9.8e-7 at n=50, holding that floor through n=99 (`python sk3/p21` sweep in
`refute-recall-3.md`; `python m3/bm25_probe.py` for the two published points). **A term in half the
corpus or more contributes literally nothing.** It is not down-weighted. It is deleted.

Same axis, opposite sign, and in a code corpus the two are physically the same number: `run` is a
popular identifier BECAUSE it is a word everybody reaches for.

### 4.2 The idf-stripping experiment, and why the naive version misleads

Ablating bm25's idf alone returns "barely moves": r@5 0.341 → 0.329 on the joint 82. That answer is
a trap, because `memory-recall` corrects for df TWICE — `bench.terms()` deletes a 101-word stop list
(`the` 791/907, `a` 663/907, `and` 631/907) before a query is ever built. The 2x2
(`python m3/stoplist.py`, joint n=82):

| arm | r@5 |
|---|---|
| stop list + idf (shipped) | 0.341 |
| stop list, no idf | 0.329 |
| no stop list, idf | 0.329 |
| **neither** | **0.207** |

**With one numeric correction that must ride with it.** `stoplist.py`'s no-stop arm also silently
dropped `bench.terms`'s `len(t) > 2` filter, so it changed two things. Holding the length filter
constant, the "neither" arm is **0.244 on joint 82 (−28%) and 0.316 on scen-2 (−14%)**, not
0.207/0.263 (−39%/−29%) (`python sk3/p23.py`). A third of the joint collapse and half the scen-2
collapse was the length filter. The interaction survives: with the stop list held, removing idf
costs a net 1 row; with it removed and the length filter held, removing idf costs a net 7 rows on
joint and 5 on scen-2.

**The test that actually settles it is a substitution the original pass never ran.** A
corpus-derived top-101-by-df stop list with idf OFF scores **0.341** at r@5 on joint 82 — identical
to the shipped idf-on arm. A RANDOM same-size stop list with idf off scores **0.232**
(`python sk3/p23.py`). A df cut fully substitutes for idf; an arbitrary cut of the same size does
not. **So yes: df correction is what protects `memory-recall`, and it is applied twice.**

### 4.3 Do they share the DEFECT? No — and "independent" is not established either

On the 82 joint queries at k=5: both 6, only-recall 22, only-map 9, neither 45, **phi = +0.058,
permutation p = 0.7646** over 20 000 trials (`python m3/correlate.py`). But the conclusion drawn
from that ("so they do not share a defect") was refuted as accepting a null a low-powered test could
not reject: walking the both-cell up through the same machinery, the first significant table is
both=9 at phi +0.258 (p 0.031), and both=8 at phi +0.191 still reads p 0.134. De-duplicating the 82
rows to 67 distinct queries gives **phi +0.211 at p 0.102** — 3.6x the headline (`python sk3/p22.py`).

**The defensible statement: the two tools' failures are not strongly correlated, and the design
cannot distinguish independence from a correlation up to about +0.19.** The mechanism argument is
what carries the verdict, not the phi.

Confirmed on a different axis, though. Both tools stand or fall on term rarity. `memory-recall`'s
single largest lever is a manual rarity rewrite (`--terms` median df 19.0 against the question's
32.0) — but that framing is itself refuted as a MECHANISM: replacing each session's terms with the
same number of random corpus terms at matched df scores 0.301 r@5, BELOW the question-only baseline
of 0.325 (`python sk_terms.py`, n=83). Rarity without relevance buys nothing. The lever is *which
jargon*, not *how rare*.

### 4.4 Is the fix already shipped one kit over? Partly — and the cheap version is cheaper than proposed

The transplant tests both directions. `reuse_lookup`'s algorithm ported onto the records corpus
scores r@1/5/10/20 = 0.000/0.000/0.021/0.074 against 0.011/0.074/0.126/0.179 for the identical match
set in corpus order (`python m3/port.py`, n=95). But "worse than not ranking at all" was **refuted**:
corpus order is not a null — it beats a true random permutation 2.7x at r@5 (0.074 vs 0.027) — and on
the joint 82 `port_fanin_desc` (0.024/0.073/0.134/0.195) beats a 40-shuffle random null
(0.007/0.034/0.054/0.092) at every k (`python sk3/p24.py`). The honest form is **"worse on one
corpus, better than chance on the other"**, not "an anti-signal".

Transferring bm25's SHAPE into `reuse_lookup` is where the measurable win is. Re-ordering the same
shortlist by matched-stem specificity with `fan_in` demoted to a tiebreak, over 132 graded scenarios
(`python m3/shape.py`, `python m3/composite.py`, `python sk4/ctrl.py`):

| key | r@1 | r@3 | r@5 | r@10 | r@20 | MRR |
|---|---|---|---|---|---|---|
| `map_shipped` | 0.053 | 0.106 | 0.159 | 0.220 | 0.242 | 0.102 |
| `map_lexico` (candidate-pool stem df) | 0.023 | 0.152 | 0.212 | 0.265 | 0.303 | 0.103 |
| `map_composite` (slot 1 to the hottest seed) | 0.053 | 0.121 | 0.212 | 0.258 | 0.303 | 0.110 |
| **`map_lexico_SRCDF`** (stem df from `build_reference_index`'s OWN output) | 0.038 | 0.144 | 0.212 | **0.273** | 0.295 | **0.113** |
| `map_bm25ish` (idf x log1p(fan_in), multiplicative) | 0.038 | 0.129 | 0.159 | 0.220 | 0.242 | 0.100 |
| `map_faninasc` (sign-flip control) | 0.015 | 0.030 | 0.030 | 0.098 | 0.250 | 0.045 |
| `map_namesort` (no popularity signal control) | 0.023 | 0.030 | 0.030 | 0.098 | 0.235 | 0.048 |

Three things fall out.

1. **The df inside `build_reference_index` CAN supply the correction**, contrary to measurement 3's
   claim that a second corpus is needed. Build stem postings out of the index's own output —
   4934 tokens to 1924 stems in **0.0164 s median (n=9)**, no new parsing, no new scan, no new
   artifact (`python sk4/ctrl.py`). It matches the pool-df version at r@5, beats it at r@10, and has
   the best MRR in the table. In an adopting repo that is the difference between reusing an artifact
   and adding a scan.
2. **The multiplicative bm25 shape does NOT transfer.** `log1p(fan_in)` re-dominates and collapses
   onto the shipped numbers. Lexicographic works; multiplicative does not.
3. **Do not oversell the margin.** The composite's "Pareto improvement at every k" was refuted: at
   k=2 it loses 3 scenarios and the reported 1/3/5/10/20 grid skips exactly that k; r@5 is
   p=0.0889 over 13 discordant pairs; and at r@20 a **random shuffle of the seeds matches it** —
   composite's 0.303 IS the 95th percentile of 200 random draws and shipped's 0.242 is the 5th
   (`python sk4/grid.py`, `python sk4/ctrl.py`). The durable finding there is about the SHIPPED key:
   **it is worse than chance at depth, and nearly any perturbation beats it.**

`SEAM_FANIN_THRESHOLD` must not move. `fan_in >= 3` is shared with `map_diff --converge` and
`seed_affordances` and answers a different question ("is this referenced widely enough to be worth
declaring") from the one ranking answers ("did this match the query specifically").

---

## 5. WHAT THE SKEPTICS KILLED

38 claims went to a verify stage. **16 survived, 22 were refuted.** Below is every refutation and
what it forces. Nothing in this report treats a refuted claim as confirmed, and where a skeptic's own
arm has not itself been independently re-run it is marked UNVERIFIED.

### Refutations that change a conclusion

| # | claim | what forces |
|---|---|---|
| [1] | re-rank "costs recall at every finite K" | FALSE in the symbol-only arm (+1 @10, +6 @20, p=0.031) and the magnitude was an undisclosed reimplementation of `compound` (12 of 839 candidates). Under the proposal's own predicate the @5 loss is 1 scenario, p=1.00. **The verdict now rests on lens 3, not on lens 1.** |
| [28] | the 1.6%→80.0% lift "does not transfer, it was measured on a list the tool never produces" | The lift transfers on the per-query shortlist (28.3%→81.7% p@5, chance 39.6%). **The problem is the YARDSTICK, not the population.** Also, `reuse_lookup` does ship a global fan-in ranking — `seed_affordances`. |
| [38] | "36.4% ceiling, both arms equally blind so the A/B is fair" | Resolved scoring lifts reachability to 112/132 (84.8%) and REVERSES the direction at depth: strict says the re-rank wins @20 (38 vs 32), resolved says shipped wins by 45 (97 vs 52). **Every A/B must report both resolutions.** |
| [15] | "removing idf halves r@1 (0.232→0.116)" | The df-blind control was not df-blind (it drew its pool from an idf-ranked selection) and ablated three things at once; its own mutation test 2 had failed. A validated ablation on the same 95 queries gives 0.232→0.200 at r@1 and 0.368→0.358 at r@5 — 4-10x smaller. **The (d) verdict rests on arms 2 and 3, not arm 4.** |
| [18] | "the CLI hands a session its own document 96% of the time" | True of `chunks:fts5` in isolation, **5% through the CLI** (4/83 with `--no-terms`), because `query.py:1177` fuses records and chunks by reciprocal rank fusion and the records set takes rank 1. The immunity clause's reason was also wrong by 10x (21 of 907 records docs come from spec files, not 2). |
| [19] | "the class gap is half question SHAPE" | 6/12 vs 19/71 is Fisher p=0.1702, and "shape" is perfectly confounded with provenance (all 12 interrogative rows are recorded `query.py` invocations, selected on the tool having worked) and with overlap (interrogative mean 0.427 vs declarative 0.276). **Overlap is the better-supported explanation; shape is not established.** |
| [25] | "the df inside `build_reference_index` cannot supply the correction" | It can, read at STEM granularity — `map_lexico_SRCDF`, 0.0164 s, no new corpus, best MRR in the table. **The recommendation gets cheaper.** |
| [26] | the composite key is "a Pareto improvement at every k, on MRR" | k=2 loses and the grid skips it; r@5 p=0.0889; r@20 is matched by a random shuffle; `map_lexico` beats composite on the sole-attribution and deduped slices; head=1 is fitted with no held-out split. |
| [30] | the identifier spelling is "arithmetically identical to a fan-in band cut" | The identity holds for ONE of three terms. Against the named band cut: 0 of 179 orderings identical, top-5 membership agrees on 24.6%. **Keep the narrow version; the generalisation would send an implementer to drop the tier and keep a threshold.** |
| [24] | "fan-in descending is worse than not ranking at all" | Corpus order is not a null (2.7x a random permutation) and the sign REVERSES on the joint 82, where fanin_desc beats random at every k. |
| [22] | "the failures are statistically independent, so no shared defect" | The test could not have rejected below phi ≈ +0.19; de-duplicated the estimate is +0.211 (p 0.102). Accepting a null on a low-powered design. |
| [27] | "the tools are comparably bad once leakage is removed" | The slice selects on one arm's own outcome variable at half the repo's declared `OVERLAP_MAX` (0.30 vs 0.60); at 0.60 memory-recall leads 0.312 vs 0.182, and the map arm's score goes UP on the "harder" slice. |
| [4] | "the tier demotes the corpus's own seam set", with 25 named symbols | There are 31 non-compound symbols at fan-in >= 3, not 15; the "25" reproduces at no threshold. And 37 of the 68 seams are compound and PROMOTED. **A count of a derived population was stated in prose, inside the report that forbids it.** |
| [10] | "the harness is live and reproducible" | Reproducibility is real, but `score1.py`/`score1c.py` are not different code paths and their 132/132 agreement at @20 hid a shared bug. **Every published @20 figure moves.** |
| [9] | "symbol-only at deep K is mildly positive" | Recomputed as @10 -3/+4 (not +2/-0) and the @20 effect flips sign on the sole-attribution slice. |
| [16] | "`--terms` is a rarity rewrite" | Rarity-matched random terms score BELOW the question-only baseline. The r@5 half (+0.073) is p=0.18. **Quote +0.168 at r@20 only.** The `check-recall`-cannot-see-it half is confirmed and kept. |
| [29] | "changes the answer on half the corpus while improving nothing measurable" | True and empty: 3 discordant scenarios at hit@5 cannot reach p<0.25. |
| [32] | "37 seam citations invalidated" | Zero leave the shortlist (median new rank 60), the 37 are dominated by answers the same report calls worthless, and its two clauses undercut each other. |
| [33] | "raises plausibility without raising correctness" | Vacuous on 27 of the 36 (unreachable under strict scoring); on the 9 scoreable the re-rank is AHEAD. No measurement of plausibility exists anywhere in the pass. |
| [35] | "a rare symbol is a precise edge and a useless answer" | The two yardsticks agree in sign at row level (7.7% vs 1.5%); the real mechanism is discrimination — tier 3 covers 84.1% of shortlist rows, so promoting it hands rank 1 to the alphabetical tie-break. |
| [36] | "the signal's real home is `seed_affordances`" | The non-binding threshold is a consequence of the sort key, not a finding; there is no ground truth; and 12 of the re-keyed top 20 become codebase-map's own internal renderers. |
| [37] | "receiver-binding is 1.84x, not 3x" | The ratio paired medians from two scripts and omitted a stage. Interleaved A/B/C in one process: ast-only 1.77x, **complete E2 pass 2.80x** — back to ~3x. The ranking half of the claim survives. |

### The 16 that survived, in one line each

[2] lens 3's 11/28 → 2/28, p=0.0039. [3] `df<=15` is `fan_in<=14` (836/839 candidates, 645/645
symbols). [5] the 17 lens-3 misses are unreachable by any K or ordering. [6] the .848 headline is
dossier globs; symbol-only it is .288. [7] a query-ignoring constant answer beats the tool (LOO
.098/.515/.720/.841). [8] `fanin_asc` is a glob artifact (0/28 on lens 3). [11] the declared
RECALL_FLOOR reproduces exactly. [12] 0.3012 harvested / 0.0000 graded with ceiling 1.0000. [13]
`rm3` is hash-seed nondeterministic and `fts5` is not. [14] rank-1 docs are anchored on rarer terms,
monotonically — direction only, not the effect size. [17] recall is a step function of overlap with a
knee at ~0.30. [20] `fan_in` is exactly a document frequency. [21] the two tools use it with opposite
sign, and bm25's clamp bites at exactly n = N/2. [23] `memory-recall` corrects for df twice (with the
numeric correction in §4.2). [31] the cheap spelling is free and the text spelling is not. [34] a
candidate with no evidence scores as maximally distinctive.

### UNVERIFIED, and named as such

- The **resolved-arm hit table** in §1.2 is one skeptic's arm (`sk5_b.py`), written this pass and not
  itself adversarially reviewed. It independently reproduces measurer 1's .848, which is the only
  cross-check it has.
- **`sk4/transfer.py`'s 81.7%** (§2.4) is one run by one author. Its liveness assertion is real (the
  same scorer reproduces `rerank.py`'s 1.6% exactly), but nobody attacked it.
- **`map_lexico_SRCDF`** (§4.4) was measured once, by a skeptic, on the set it would be tuned on. It
  has no held-out split and no permutation test of its own.
- **The `--terms` matched-rarity control** (§4.3) is one construction of "same rarity, different
  words"; a different construction could give a different answer.
- Nobody re-ran the skeptics. Every refutation above had exactly one reader.

---

## 6. SPEC CHANGES — what `TOOL-dTracedLattice-1` should now say

### 6.1 DROP outright

1. **The confidence tier as a sort key.** Lens 3: 11/28 → 2/28 at @5, p=0.0039. Lens 1: negative in
   sign at @1 and @5 in all four arm/predicate combinations. Resolved scoring: -45 scenarios at @20.
   No arm anywhere shows it helping at a K a human reads.
2. **The `token df <= 15` term.** Over the corpus the tool already has, it is `fan_in <= 14`
   (645/645 symbols, 769/769 rows, 836/839 candidates). A proposal reading "confidence tier, then
   fan-in" is, in its third term, "fan-in, then fan-in".
3. **The raw-text DF spelling.** 1.554 s per query of new scan (median, n=5) on a 0.936 s command;
   demotes `boundedParallel` for being documented; puts a file-less row at rank 1 on 24 of 179
   queries and lets the alphabetical tie-break decide 53.6% of rank-1 answers.
4. **The `ambient` filter as specified.** It discriminates 4 names of 645, and its only catch among
   the seven highest-fan-in common names — `resolve` — is a false positive that costs rank 1 to 83.
5. **`precision@5` over the global symbol list as an acceptance criterion.** It is a real
   measurement (and it does transfer to the shortlist, 28.3% → 81.7%), and it does not predict the
   answer. Keep it as a diagnostic; never as the AC.
6. **`fanin_asc`**, if it is anywhere in the spec as the obvious alternative. Its Arm A win is the
   glob artifact; symbol-only it is worst of four at @5 (.030) and it scores 0/28 at every finite K
   on lens 3.

### 6.2 KEEP, re-scoped, in priority order

**S1 — the name-merge defect (`file: str` → `files: tuple[str,...]`).** Highest measured value and
it is not a ranking change. 124 of 769 definitions (16.1%) are unreachable; `repo_root` has four
definers and prints one. Crediting all definers lifts Arm A @1 .068 → .114, @5 .303 → .348, and
symbol-only @all .288 → .311. Duplicates are what a reuse audit hunts.

**S2 — retrieval: a behaviour-phrase to seam bridge.** 17 of 17 lens-3 misses and ~15% of lens-1
scenarios fail on empty stem intersection, and lifting `NEIGHBOUR_CAP` to infinity reaches 0 of 17.
Cheapest credible probes, all stdlib: stem the query against the candidate's *docstring first line*
as well as its name; and fix the `unfenced`/`fenc` class by matching on stem prefixes for names not
otherwise matched. Both must be measured, not assumed.

**S3 — a stem-specificity SECONDARY key, built from `build_reference_index`'s own output.** Not the
identifier df (that is `fan_in`), but stem postings derived from the same index: 4934 tokens → 1924
stems in 0.0164 s, nothing committed, drift structurally impossible. Measured r@5 0.212 vs shipped
0.159, r@10 0.273 vs 0.220, MRR 0.113 vs 0.102. **Land it only if it clears the ACs below**, because
its margin is currently indistinguishable from a random seed shuffle at r@20.

**S4 — report misses as misses.** 17 of 28 lens-3 rows and 20 of 132 lens-1 rows are recall failures.
A harness that folds a miss in as `rank = len(shortlist)` reads a ranking change as a recall change.

**S5 — leave `SEAM_FANIN_THRESHOLD` alone.** It is shared with `--converge` and `seed_affordances`
and answers a different question. Re-defining a seam to fix a sort order breaks the convergence
worklist.

**S6 — `seed_affordances` re-keying: MEASURE FIRST, do not land blind.** The claim that the signal's
"real home" is the worklist has no ground truth; the non-binding threshold is a consequence of the
sort key, and 12 of the re-keyed top 20 become codebase-map's own internal renderers. If it goes in
the spec at all, it goes in as a unit whose AC is a scored comparison, not a read-and-judge.

**S7 — a separate unit, different kit: fix `bench.run_rm3`'s hash-seed nondeterminism.** One
`sorted()` before `df.update`. `rm3` is a legal `RECALL_FLOOR` substrate
(`check-recall.SUBS = tuple(bench.LEXICAL) + …`), so pinning it today gives a flaky gate: eight
free-seed runs give control r@5 in {0.6667, 0.75} while `fts5` is byte-identical in all fourteen.

### 6.3 Acceptance criteria, with thresholds drawn from these measurements

Any ranking change to `reuse_lookup` must, before landing:

- **AC1 — not lose on the adversarial set.** recall@5 over `scen-3-adversarial.json` must be
  **>= 11/28** (the shipped baseline). The confidence re-rank scores 2/28.
- **AC2 — be scored under BOTH resolutions and report both.** Strict (def file only) and resolved
  (feature rows through `[paths].globs`). At @20 over 132 graded, shipped scores 32 strict and 97
  resolved; a change that wins one and loses the other has not been measured, it has been framed.
- **AC3 — beat chance, not just the shipped key.** Compare against 200 random seed-shuffles of the
  same shortlist and clear the **95th percentile** at the k claimed. Shipped sits at the 5th
  percentile at r@20 (0.242 against a 0.242–0.303 band), so beating shipped at depth is not evidence.
- **AC4 — report paired significance with the discordant count.** McNemar exact or a 20 000-trial
  paired permutation. **No delta with fewer than 6 discordant pairs may be reported as a finding**
  (that is the minimum that can reach p<0.05 at these n).
- **AC5 — replay at each spec's own `base_sha`, not only HEAD.** 129 of 132 graded scenarios resolve
  one. The dossier corpus grew from 2 to 20 across the graded window, and rank-1 changes on 48.1% of
  scenarios between base and HEAD, so a HEAD-only measurement credits the tool with dossiers the
  graded unit itself wrote.
- **AC6 — quote the predicate.** Any `compound`/ambient/df predicate is pinned by source in the spec
  and any harness re-implementation is byte-compared against it. Two spellings of `compound`
  disagreeing on 12 of 839 candidates moved the headline by 10 scenarios.
- **AC7 — cost ceiling: <= 0.05 s added to a ~1 s command, no second full-corpus scan.** The
  identifier-index spelling adds 9 µs and the stem-posting key adds 0.0164 s; the raw-text spelling
  adds 1.554 s and is out on this criterion alone.
- **AC8 — report the constant-answer control beside any file-granularity number.** Leave-one-out,
  the K most-frequently-changed files, query ignored: .098/.515/.720/.841 at K=1/5/10/20. A file
  recall figure that does not beat it establishes nothing.
- **AC9 — carry the citation-churn number.** Count how many of the 92 resolvable cited seams
  currently in a shipped top 5 leave it, and how many are in live specs. Under R1-ident that was 37
  and 14. Nothing gates it, so it is a disclosure, not a blocker.

### 6.4 What the spec should say about the yardstick, in one sentence

Edge precision and answer hit-rate are two measurements of two objects, they are only 5x apart at
row level and 131x apart in the cells the design pass quoted, and **only the second one is the
question a session asks.**

---

## 7. WHAT WE STILL CANNOT MEASURE

**Nobody was watched.** Every number in this report is a property of what a tool returns, not of
anyone orienting faster. The scen-4 orientation set closes on the same limitation and does not remove
it: 14 of its 18 questions have a working one-command `git grep` answer, and `reuse_lookup` wins none
of them outright.

**No true negatives, anywhere.** 102 of the harvested §10 sections record that the probe found
nothing, and a scenario with empty `expected_ids` cannot be scored by recall@k, so all of them were
dropped. Nothing here measures either tool returning confident junk for a question with no answer —
which is exactly what §2.5's tie-break finding suggests happens often.

**The questions sessions did not write down.** 65 of the 244 §10s naming `reuse_lookup` recorded the
answer and never the question, and they read overwhelmingly like failed probes. Selection is biased
toward probes that worked, so measured recall is biased HIGH on both tools.

**The bash layer is dark and it is where the product lives.** `symbols.json` covers py+js;
`RECALL_DARK_LAYERS="bash"`; the graded ground truth is 283 `.md`, 281 `.sh`, 123 `.py`. Nothing here
says anything about a shell-layer common-word seam, and `reuse_lookup` prints a partial-recall notice
for it on every run.

**Two whole scenario classes cannot measure correctness by construction.** The 47 STABILITY-ONLY
replay rows have empty `expected_*`; the 74 STABILITY-ONLY recall rows have lost their attribution
(40 of them are prose citations that could have come from the tool, from grep, or from the author's
own memory). Both are stability tripwires only.

**GRADED is 9 questions.** One question moves r@5 by 0.111. Every graded delta in §1.4 is at or below
the resolution of the set, and the class is by construction the residue of ids the section did not
attribute to the tool — the self-grading trap running in reverse, deflating rather than inflating.

**Phrasing variance is unexplored.** One invocation per tool per question, everywhere. Lens 3's
queries were written after reading the answers, so its 11/28 is an UPPER bound. A different `--terms`
rewrite changes memory-recall's answers; a differently phrased behaviour string changes
`reuse_lookup`'s.

**Ground-truth attribution cannot separate implementing an id from mentioning one.** It is by commit
message. 106 of the 233 kept commits name more than one unit, and 40 of the 132 graded rows have an
empty sole-attribution set. Every conclusion here was re-checked on that subset and held, but the
subset is n=92, not 132.

**Anachronism is handled, not eliminated.** Every graded row carries `base_sha` and 129 resolve, but
3 fall back to HEAD, the replay uses HEAD's ranker over a historical corpus (deliberately — the
question is how today's ranker would have answered yesterday's question), and the resolved-arm
scoring credits a dossier that may post-date the unit.

**One repo, 26 days, two dominant kits, one node, one platform.** 152 distinct ground-truth files,
907 records documents, this project's id grammar and §10 convention and jargon. Nothing here is a
property of either KIT and none of it should be quoted as one. `ALIAS_WEIGHT` is inert
(`aliases.json` absent), the `spine` document set extracts to ZERO documents so any pin naming it is
a dead probe, and every timing is a single draw on a node whose wall readings vary 3x.

**And nobody checked the checkers.** The skeptic pass found a scorer bug that moved every published
@20 figure, a predicate mismatch that moved a headline by 10 scenarios, and an ablation that changed
two variables at once. It had one reader and was not itself reviewed.
