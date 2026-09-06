**Serves:** research TOOL-dTracedLattice-1 TOOL-dTracedLattice-7

# MEASURER 1 — `reuse_lookup` RECALL: shipped fan-in order vs the confidence re-rank

Node `d`, 2026-09-05. Repo `C:/projects/coding-governance/.claude/worktrees/build-readme-governance-18d6ea`,
HEAD `991153457d30c923151d749e12afedd4e9176689`, tracked tree clean before and after
(`git status --porcelain` empty).

Harness: `m1/lib1.py` (shared), `m1/score1c.py` (lens 1 — four orderings x three resolution arms),
`m1/score1d.py` (lens 1 vs expected_symbols), `m1/score3.py` (lens 3), `m1/analyze1b.py`.
Rows: `m1/rows1.json` `m1/rows1c.json` `m1/rows1d.json` `m1/rows3.json`.

The harness **imports the kit's own `map_lib` and `reuse_lookup`** and drives ranking through
`reuse_lookup.assemble_shortlist`. Three things are reimplemented, all because the kit does not
contain them:

1. **The confidence tier.** It does not exist in the kit. Implemented as the brief spells it —
   `name not in (builtins | dir(str) | dir(list) | dir(Path))`, plus `("_" in name or a lowerUpper
   hump)`, plus `document-frequency(name) <= 15` over the same identifier index `fan_in` reads. A
   wider ambient set (also `bytes`/`dict`/`set`/`int`/keywords, the spelling `scratchpad/rerank.py`
   used) ran as a second arm and produced **identical rows at every K** — the two sets differ on
   nothing in this corpus.
2. **Candidate to file resolution.** `reuse_lookup` resolves candidates only while *rendering* text.
   Symbol rows resolve to `Candidate.file`; affordance-seam and shared-seams rows resolve through
   their dossier's `[paths].globs`; inventory keys resolve through the dossier whose `[claims]` names
   the key. This is `scoring_recipe`'s own recipe, run end to end for the first time.
3. **The orderings**, which are `sorted()` over the list `assemble_shortlist` returns, never a
   re-derivation of it.

## The harness moves, and here is the proof

A probe that cannot move must say so, so three liveness assertions ran before any number below was
believed.

- `m1/score3.py` recomputes lens 3's `shipped_rank` from scratch and agrees with lens 3's own
  independently-built baseline on **28/28** scenarios, and with its declared
  `confidence.tier_identifier_index` on **28/28**.
- `rows1.json` (first run) and `rows1c.json` (third run, different code path) agree on shipped
  hits@20 for **132/132** scenarios.
- The re-orderings are permutations, so `@all` must be invariant. Checked, not assumed: all three
  alternative orderings produce an `@all` hit set identical to shipped's for **132/132** scenarios.
  **A re-rank discards nothing. That half of the design pass's claim is confirmed.**

One graded scenario (`TOOL-aRootedPrefix-1`) returns an **empty** shortlist. It is scored as zero
everywhere rather than dropped, so it drags every headline down by 1/132 in the honest direction.

## The answer in one line

**The re-rank costs recall at every K on both lenses, and it costs the most exactly where the design
pass claimed it would gain.** The confidence tier is not a confidence signal over this corpus: two of
its three components fire on ~99% of symbols, and the third is anti-correlated with being a seam.

## Lens 1 — 179 replay scenarios, 132 graded

Replayed at each spec's own `base_sha` (129 of 132 resolve; 3 fall back to HEAD and are tagged
`era=HEAD-fallback` in the rows). `git archive <base> | tar -x` into scratch, corpus and reference
index rebuilt per sha, HEAD's ranker over the historical corpus. 44 distinct base shas. Dossier count
at base ranges 0 to 20, and one scenario had zero.

Ground truth is the product files the unit actually changed. Two numbers per cell: **any-hit** is the
fraction of scenarios where at least one expected file is reachable from the top K, **file-recall** is
the mean of `|hit ∩ expected| / |expected|`.

### Arm A — file granularity, dossier globs included (the `scoring_recipe` as written)

```
ordering           @1      @5      @10     @20     @all
shipped   any-hit  .068    .303    .606    .720    .848
          f-recall .016    .135    .343    .424    .530
rerank    any-hit  .045    .220    .303    .508    .848
          f-recall .011    .089    .124    .235    .530
fanin_asc any-hit  .227    .538    .727    .765    .848
          f-recall .142    .310    .427    .445    .530
```

`python m1/analyze1b.py`, reading `m1/rows1c.json`, n=132.

Sole-attribution subset (n=92, dropping every file whose only evidence is a multi-unit commit) has
the same shape, slightly lower: shipped `.043/.272/.565/.696/.804`, rerank `.011/.152/.239/.435/.804`.

Query-deduplicated (104 distinct queries, each query's rows averaged before the mean) has the same
shape: shipped `.067/.279/.611/.744/.864`, rerank `.043/.208/.314/.502/.864`. The 20 shared queries
are not driving anything.

Fixing the name-merge defect in resolution — crediting a symbol with **all** its definers rather than
the one `file or prev.file` keeps — lifts shipped's @1 from `.068` to `.114` and @5 from `.303` to
`.348`, and does not change the ordering verdict at all.

### Arm B — symbol granularity, and this is the arm that matters

A dossier `[paths].globs` row is a **coarse pointer**, not a seam hit. Fan-out is a median of 6 files
and up to 44 (`codebase-map` 44, `govkit` 37, `unattended` 30). Any ordering that front-loads
feature-tagged rows harvests file-recall it did not earn. Scoring only rows that name exactly one file:

```
ordering           @1      @5      @10     @20     @all
shipped   any-hit  .061    .144    .182    .205    .288
rerank    any-hit  .045    .136    .189    .250    .288
fanin_asc any-hit  .008    .030    .114    .227    .288
```

Two things fall out of this arm and both are load-bearing.

`fanin_asc`'s apparent win in Arm A was the glob artifact. Its @5 goes from `.538`, best of four, to
`.030`, worst of four, the moment every row is made to point at one file. I built that arm because the
design pass's "precision is 51.8% at fan-in 1-2" invited exactly this ordering; on real scenarios it
does not survive contact with uniform granularity.

And in 71.2% of graded scenarios, no symbol candidate anywhere in the shortlist points at a file the
unit actually changed (any-hit@all `.288`). The `.848` headline in Arm A is dossier coverage.

### Arm C — scored against `expected_symbols` — DEAD BY CONSTRUCTION, reported anyway

106 graded scenarios carry at least one expected symbol. any-hit@all is `.066` for every ordering.
That is not a measurement. `expected_symbols` holds only symbols the unit **created**, which by
definition did not exist in the corpus at `base_sha`. The arm cannot move, so it is reported as unable
to move rather than as a low score. Command: `python m1/score1d.py`.

### The control that should worry everybody

Answer the K globally most frequent ground-truth files, ignoring the query entirely:

```
K=1   any-hit .265   file-recall .051   tools/unattended/unattended.sh
K=5   any-hit .515   file-recall .206   + .memory-tree.conf, PROTOCOL.template.md, unattended.test.sh, unattended/SKILL.md
K=10  any-hit .720   file-recall .373
K=20  any-hit .879   file-recall .604
```

The constant answer beats the tool at K=5 (`.515` against `.303`), beats it at K=10 (`.720` against
`.606`) and beats it at K=20 (`.879` against `.720`). Lens 1 warned this would happen and emitted
`corpus_file_frequency` so it could be checked. It happens.

That is a property of the corpus, not a verdict on the tool. But it means no file-level recall number
from this set can be read as evidence the tool works, in either ordering. It can only be read as a
comparison between orderings, which is what was asked.

## Lens 3 — 28 adversarial common-name scenarios

Ground truth is one symbol, so granularity is uniform by construction and no glob artifact exists.
Run at HEAD `991153457d30`, the sha lens 3's own numbers were taken at, on a clean tree.

```
ordering          @1      @5      @10     @20     @all
shipped          4/28   11/28   11/28   11/28    11/28
rerank           2/28    2/28    2/28    4/28    11/28
fanin_asc        0/28    0/28    0/28    0/28    11/28
```

Every one of the 11 answers the shipped order surfaces is inside its top 5. The re-rank keeps 2.

| id | symbol | shipped | rerank | fan-in | tier | role |
|----|--------|---------|--------|--------|------|------|
| ADV-04 | `resolve` | **1** | 83 | 26 | 0 | harm-ambient-filter |
| ADV-27 | `extract` | **1** | 38 | 7 | 2 | harm-if-demoted |
| ADV-25 | `repo_root` | **1** | **1** | 13 | 3 | control-signal-agrees |
| ADV-24 | `leading_verb` | **1** | **1** | 4 | 3 | control-signal-agrees |
| ADV-09 | `anchors` | 2 | 20 | 4 | 2 | harm-low-fanin |
| ADV-14 | `write` | 2 | 51 | 19 | 1 | harm-if-demoted |
| ADV-15 | `load_conf` | 2 | 62 | 18 | 2 | disambiguation |
| ADV-19 | `merge` | 2 | 15 | 2 | 2 | harm-collision |
| ADV-11 | `tracked` | 3 | 26 | 7 | 2 | harm-if-demoted |
| ADV-12 | `git` | 4 | 35 | 7 | 2 | disambiguation |
| ADV-13 | `read` | 4 | 62 | 9 | 2 | disambiguation-semantics-differ |

Nine of eleven move down, none moves up, and the only two that hold rank 1 are the two
`compound-rare` controls the set included precisely so a re-ranker could not win by burying
everything common.

## Why the tier does nothing: it is one signal wearing three hats

Measured over the 645 symbols in the HEAD corpus.

| signal | fires on | discriminates |
|--------|----------|---------------|
| `not ambient` | 641/645 = **99.4%** | four names total: `read_text`, `resolve`, `walk`, `write_text` |
| `df <= 15` | 635/645 = **98.4%** | ten names: `main` `read_text` `run` `key` `resolve` `search` `write` `check` `write_text` `load_conf` |
| `compound` | 562/645 = **87.1%** | the single-word names |

Tier 3 covers **559/645 symbols (86.7%)** and **566/839 candidates (67.5%)**. Only 14 candidates in
the whole corpus sit below tier 2. Sorting by tier therefore does one thing: it takes the ~13% of
names that are single words and pushes them behind everything else.

**The `df <= 15` signal is `fan_in` restated, and that is a theorem, not a coincidence.**
`map_lib.fan_in(index, id, def_file)` is `len(index[id] - {def_file})` over the same index the DF is
read from, and a symbol's own def file always contains its own identifier token. So `df = fan_in + 1`
exactly. Measured at **645/645 symbols at HEAD and 580/580 at base `1d83cc94`**, with
`(df<=15) == (fan_in<=14)` over the same populations. Lens 3 found this at HEAD; it holds at an
arbitrary historical base too, because it cannot not hold.

That leaves `compound` as the only signal with spread. What it demotes is the 25 single-word symbols
carrying fan-in >= 3, which is the corpus's own seam set: `main` 37, `run` 28, `key` 28, `resolve` 26,
`search` 23, `write` 19, `check` 19, `why` 13, `tree` 12, `parse` 11, `read` 9, `tracked` 7, `git` 7,
`extract` 7, `subtokens` 4. The ambient signal's one genuine catch, `resolve`, is a **false
positive** — it is `recall_conf.resolve`, whose docstring says every module in the kit calls it at
import.

## The three questions

### (a) Does re-ranking cost recall at all, at any K? Yes, at every K, on both lenses.

`@all` is identical by construction and verified 132/132, so nothing is *discarded*. Everything below
is a *presentation* loss, which is the only kind an ordering can cause, and it is exactly the loss a
reader who stops scrolling actually suffers.

Lens 1, Arm A, scenarios shipped answered within K and rerank did not:

```
@1    lost  3   gained  0   net  -3
@5    lost 18   gained  7   net -11
@10   lost 43   gained  3   net -40
@20   lost 30   gained  2   net -28
@all  lost  0   gained  0   net   0
```

The 18 lost at @5, by spec id: `TOOL-aBoundedVerdict-2`, `TOOL-aBranchedMandate-3`,
`TOOL-aDeclaredCeiling-1`, `TOOL-aDeclaredCeiling-3`, `TOOL-aPrimedKeepalive-1`,
`TOOL-aSealedCaravan-1`, `TOOL-aTetheredRecord-2`, `TOOL-aWrittenMethod-2`, `TOOL-aWrittenMethod-6`,
`TOOL-cBriefedPilot-17`, `TOOL-cBriefedPilot-6`, `TOOL-cBriefedPilot-7`, `TOOL-cBriefedPilot-8`,
`KICK-cKeyedLaunchpad-4`, `TOOL-cKeyedLaunchpad-5`, `DEPL-dRatifiedSeam-1`, `TOOL-dUnstalledConvoy-1`,
`TOOL-dUnstalledConvoy-6`. Fourteen of the eighteen have a `tools/unattended/` file in their expected
set.

The 7 gained at @5: `TOOL-aDeclaredBound-1`, `TOOL-aDeclaredCeiling-2`, `TOOL-aShardedFloor-1`,
`TOOL-dFoldedVerdict-4`, `DEPL-dGaugedVintage-3`, `TOOL-dMispairedQuote-1`, `TOOL-dMispairedQuote-3`.

The 30 lost at @20 are printed in full by `m1/analyze1b.py` and include `TOOL-aProvenReuse-1` and `-2`,
`TOOL-aGradedMandate-1`, `TOOL-dUnstalledConvoy-1` through `-9`, `TOOL-aRuledFrontispiece-10`,
`TOOL-aLoosenedCeiling-1` and `DEPL-dSealedTally-5`.

Lens 3: 9 scenarios lost — `resolve`, `anchors`, `tracked`, `git`, `read`, `write`, `load_conf`,
`merge`, `extract` — and **0 gained at any K**.

The one place the re-rank is not negative is lens 1 Arm B at deep K. Symbol-only, at `@20` it is
`+6/-0`, at `@10` `+2/-0`, and only `-1` net at `@5`. So on the question "which files did this unit
touch", pushing compound-rare names up is roughly neutral to mildly positive once the glob artifact is
removed. It is still negative at the K a human reads.

### (b) On the adversarial common-name scenarios, it hurts, and it hurts hard.

recall@5 goes **11/28 to 2/28**. recall@1 goes 4/28 to 2/28. Nine of the eleven surfaced answers move
down by a median of 34 ranks. The worst is `ADV-04 resolve`, **rank 1 to rank 83**, and that one is
demoted by the *ambient* signal firing on a name whose own docstring states every module in the kit
calls it at import. The two survivors are the two tier-3 controls, which is the definition of a signal
that has learned its training set.

The magnitude has a mechanical cause worth stating. Because 86.7% of symbols are tier 3, a demoted
name is not moved down a few places — it is moved behind **every tier-3 candidate in the shortlist**,
which in ADV-04's shortlist is 61 rows.

One caveat, stated because it cuts the other way: lens 3 is adversarially selected and its queries were
written after reading the answers. `11/28` is an upper bound on the shipped tool's real recall and
`2/28` is a worst case for the re-rank. What transfers is the direction and the mechanism, not the
ratio.

### (c) recall@20, and the presentation/retrieval split the design pass never made.

**Lens 1: shipped any-hit@20 = `.720`, any-hit@all = `.848`.** Median shortlist length is 52, mean
55.6, max 136, and only 9 of 132 shortlists fit inside 20 rows. Splitting the 132:

- **20 scenarios (15.2%) are a RETRIEVAL failure.** No expected file anywhere in the shortlist, at any
  rank. One of those is an empty shortlist: `TOOL-aRootedPrefix-1`, query *"resolve the repo root of a
  kit installed under a path prefix by finding its conf"*, against a corpus that contains
  `resolve_root`. Median shortlist length for this group is 29.
- **17 scenarios (12.9%) are a PRESENTATION failure.** The answer is in the list, below rank 20.
  Median shortlist length for this group is **75**, max 111. These are the rows a cap or a better
  order can buy.
- 95 scenarios (72.0%) are answered within 20.

**Lens 3: recall@20 = recall@all = 11/28.** There is no presentation component here at all — all 11
hits are in the top 5, and all 17 misses are absent from the list entirely. And the misses are not a
corpus gap: **all 17 expected symbols ARE in the corpus**, and every one fails because
`m.stems(query) & m.stems(name)` is empty. `subtokens` against *"split a camelCase or snake_case
identifier into lowercase word pieces"* is query stems `{camel, cas, identifi, lowercas, piec, snak}`
against name stems `{subtoken}`. `fan_in` against *"count how many files reference a symbol"* is
`{count, fil, how, many, referenc, symbol}` against `{fan}`. Two of them, `unfenced` and
`unfenced_lines`, fail on stemmer granularity alone — the query says `fenc`, the name stems to
`unfenc`.

So the two lenses answer (c) differently and both answers are real. On "did the shortlist point at the
files this unit changed", the tool has a *presentation* problem worth about 13 points of any-hit, and
the median offending list is 75 rows long. On "did it find the one seam a session should have reused",
it has a pure *retrieval* problem — a lexical stem intersection that a behaviour phrase routinely
fails to satisfy — and re-ordering is provably irrelevant to 17 of 28 cases.

## What this says about the recommendation

- **Do not ship the confidence re-rank.** It loses at @1, @5, @10 and @20 on the replay set, loses
  9 of 11 on the adversarial set, gains nothing anywhere at any K, and its measured mechanism is
  "demote single-word names", which over this corpus means "demote the seams".
- **`df <= 15` must be dropped from any future proposal, or re-specified over a different corpus.**
  Over the corpus `reuse_lookup` already has, it is algebraically `fan_in <= 14`. A proposal reading
  "confidence tier, then fan-in" is, in its third term, "fan-in, then fan-in".
- **The 1.6% to 80.0% precision@5 figure does not reproduce as recall.** It was measured over
  ast-resolved *edges* on a symbol population with a precision metric; on real scenarios with a
  scenario-level recall metric it inverts. Both can be true — a re-ordering that improves the average
  correctness of an edge can still bury the one row the reader needed — but only one of them is the
  question a session asks.
- **The two defects worth spending on are not ranking.** First, retrieval: a stem intersection cannot
  reach `subtokens` from "split an identifier into word pieces", which is 17/28 of lens 3 and ~15% of
  lens 1, and no K fixes it. Second, granularity: 71.2% of graded scenarios get no symbol row pointing
  at a changed file, and the name-merge fix alone (`file: str` to `files: tuple`) buys +4.6pp at @1.
- **`fanin_asc` is not the answer either**, and it was the most plausible alternative on the design
  pass's own band evidence. Its Arm A win is a glob artifact; under uniform granularity it is the worst
  of the four at @5 on lens 1 and scores 0/28 at every K on lens 3.

## Caveats

- **Every lens-1 file-recall number sits under a control that beats it.** Guessing the top-5
  most-frequently-changed files scores `.515` any-hit against the shipped tool's `.303`. Treat the
  lens-1 numbers strictly as an ordering comparison; they do not establish that the tool works.
- **Lens 3 is adversarially selected and its queries were written after reading the answers.** Its
  ratios are bounds, not expectations.
- **The replay uses HEAD's ranker over a historical corpus.** That is deliberate — the question is how
  today's ranker would have answered yesterday's question — but it means the ranker measured is not the
  one that actually ran, and `provenance.cited_seams` was never compared against, which avoids the
  self-grading trap at the cost of not detecting ranker drift.
- **3 of 132 graded scenarios could not be replayed at their own base** (`TOOL-aRelaxedShard-1`,
  `TOOL-aUnmannedHelm-5`, `TOOL-aUnmannedHelm-7`) and ran at HEAD, which flatters them.
- **`AMBIENT` is a reconstruction of "builtin/str/list/Path attribute", not the original code.** The
  literal set and a deliberately wider one produced identical rows at every K on both lenses, so the
  verdict does not turn on the reconstruction. A materially different member set would move the ambient
  column, which today discriminates four names.
- **Inventory-key resolution is the weakest link in the scoring recipe.** A key resolves through the
  dossier whose `[claims]` names it, and a key claimed by no dossier resolves to nothing and silently
  scores zero. I did not count how many keys that affects.
- **One repo, 26 days, 152 distinct ground-truth files, dominated by two kits.** Nothing here says how
  `reuse_lookup` ranks in an adopting repo or on a different language mix. The 94 tracked shell scripts
  are outside the corpus entirely, per `RECALL_DARK_LAYERS="bash"`.
- **Cost.** First lens-1 pass 331 s, dominated by 44 `git archive` extractions; cached re-runs 34 to
  36 s; lens 3 about 8 s. Scratch cost is 662 MB of extracted trees under `m1/tree_*`, all disposable.

## Commands, so no number here is unreproducible

```
python m1/score1.py     # lens 1, first pass          -> rows1.json   (331 s)
python m1/score1b.py    # lens 1, four orderings      -> rows1b.json  (36 s, trees cached)
python m1/score1c.py    # lens 1, + symbol-only arm   -> rows1c.json  (34 s)
python m1/score1d.py    # lens 1 vs expected_symbols  -> rows1d.json
python m1/score3.py     # lens 3 at HEAD              -> rows3.json
python m1/analyze1b.py  # every lens-1 table above
```
