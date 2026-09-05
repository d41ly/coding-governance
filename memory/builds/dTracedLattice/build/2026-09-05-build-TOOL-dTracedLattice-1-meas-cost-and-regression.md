**Serves:** research TOOL-dTracedLattice-1 TOOL-dTracedLattice-7

# MEASURER 4 — what re-ranking would have changed, and what it costs

*Node `d`, 2026-09-05. Repo `C:/projects/coding-governance/.claude/worktrees/build-readme-governance-18d6ea`,
HEAD `991153457d30c923151d749e12afedd4e9176689`, tracked tree clean at start and at finish. Every
number carries the command that produced it; the scripts are in `scratchpad/m4/` and re-run from
there. Nothing in the tracked tree was touched.*

---

## Verdict

**Re-ranking `reuse_lookup`'s shortlist by the proposed confidence signal changes rank one on
55.9% of the recorded queries and buys nothing measurable.** Against the closed-unit ground truth —
what each unit actually touched — the two orderings are indistinguishable: shipped is ahead by one
to three scenarios at HEAD, re-ranking is ahead by one scenario in the era-correct control, and
every one of those margins is inside the noise of a 17-to-48 scenario population.

**The 1.6%-to-80.0% precision@5 lift is arithmetic on the wrong object.** `rerank.py` ranks ONE
global list of 224 Python symbols and reports the precision of its first five rows.
`reuse_lookup` never emits that list. It emits a per-query shortlist whose membership is decided
lexically before any ordering runs, and re-ordering that shortlist moves precision@5 by nothing.

**Three costs the design has not priced.** 37 seam citations that sit in the shipped top 5 today
fall out of it, 14 of them in specs that are still live. The signal's cheap spelling is
`fan_in <= 14` wearing a hat — verified as an exact identity on all 769 symbol rows here — so it
does not add information to a fan-in sort, it truncates one. And the expensive spelling punishes a
name for being documented: `boundedParallel`, the one fan-out seam AGENTS.md §8 names by hand, has
identifier-DF 4 and text-DF 63, and the text spelling demotes it out of the top 5 for both specs
that cite it.

**Recommendation.** Do not re-rank the shortlist. Re-key the `--converge` affordance WORKLIST with
it instead — that object IS a global fan-in ranking, it is the object `rerank.py` actually measured,
and its shipped top 20 currently opens `main`, `read_text`, `key`, `run`, `resolve`.

---

## What was measured, and what was not

| # | Question | Answer |
|---|---|---|
| a | How many recorded queries change rank one? | 100 of 179 (55.9%) under the cheap spelling, 155 (86.6%) under the expensive one |
| a | Is the new answer better? | No. hit@5 against real ground truth: shipped 43.8%, re-ranked 41.7% / 37.5% (n=48 reachable) |
| b | What does re-ranking cost? | 21 microseconds a query on the cheap spelling. 2.4 s a query on the expensive one |
| c | Which cited seams fall out of the top 5? | 37 of the 92 resolvable citations that are in it today; 14 are in live specs |
| d | Does it make `SEAM_FANIN_THRESHOLD` redundant? | Not in the shortlist. Yes in the worklist, where the threshold never binds in the top 20 |

**Not measured: whether any session would have oriented faster.** Every figure below is a property
of what the tool returns, not of anyone using it. Nobody was watched. The design dossier closes on
this same limitation and this pass does not remove it.

---

## a. Retrospective — the A/B nobody had run

### The replayable corpus is 179, not 248

```
git ls-files 'memory/builds/*/spec/*.md' 'memory/builds/*/spec/**/*.md' | wc -l          # 489
git grep -l '^## 10\. Reuse audit' -- <same> | wc -l                                     # 449
git grep -l 'reuse_lookup' -- <same> | wc -l                                             # 248
```

248 spec files name the tool. 244 name it inside §10. **179 wrote the query string down** — the
other 65 recorded the answer and never the question, so they cannot be replayed at all. That is the
population scen-1 built and it is the population replayed here: 132 graded (the spec is CLOSED and
git attributes real files to the unit) plus 47 stability-only, over 143 distinct query strings.

### Two spellings, because the proposal does not pin one

The signal is `(name not ambient) + (name compound) + (token appears in <= 15 files)`. The third
term needs a corpus and the proposal does not name one. Both are measured throughout:

- **R1-ident** — document frequency over the map's own identifier index, the same index `fan_in`
  reads. Free, because the index is already built.
- **R1-text** — document frequency over the raw text of all 1520 tracked files. Needs its own
  full-corpus scan.

Both arms sort the SAME shortlist. `assemble_shortlist` runs once per query and the arms are two
sorts of its output, so seeds still come before neighbours, nothing is discarded, and every delta
below is attributable to order alone.

### What changed

```
python m4/ab.py && python m4/an1.py
```

| arm | rank-1 changed | top-5 membership changed | fan-in of the new rank 1 (median / max) |
|---|---|---|---|
| R1-ident | 100/179 = **55.9%** | 150/179 = 83.8% | 3 / 13 |
| R1-text | 155/179 = **86.6%** | 178/179 = 99.4% | 1 / 5 |

The two spellings disagree with each other on rank one for 105 of 179 queries (58.7%). Per distinct
query string the picture is the same: 80 of 143 and 124 of 143.

The rank-1 fan-in ceiling is not a coincidence. Under R1-ident the top tier requires
identifier-DF <= 15, which is exactly `fan_in <= 14` (below), so the arm cannot ever put a symbol
with fan-in 15 or more at rank one. The measured max is 13.

### What it bought — nothing that survives its own error bars

Scored against the closed-unit ground truth: does a candidate in the top k point at a file the unit
actually changed? `python m4/an2.py`, `python m4/an3.py`.

**The ceiling first, because a hit rate without one is a lie.** Of the 152 distinct ground-truth
files, only 32 (21.1%) can be named by any candidate in the corpus at all — symbols.json covers
Python and JS, and the truth is 54 `.sh`, 32 `.md`, 30 `.py`, 12 `.toml`, 9 `.js`, 7 `.txt`. **Only
48 of 132 graded scenarios (36.4%) have a truth file reachable in the returned shortlist at any
rank.** The other 84 are dark to this scoring in both arms equally.

Over those 48:

| arm | hit@1 | hit@3 | hit@5 | hit@10 |
|---|---|---|---|---|
| shipped | 14.6% | 29.2% | **43.8%** | 60.4% |
| R1-ident | 12.5% | 25.0% | 41.7% | 58.3% |
| R1-text | 8.3% | 25.0% | 37.5% | 58.3% |

Those gaps are one and three scenarios. Reported as wins and losses instead of rates
(`python m4/an5.py`): at k=5, R1-ident wins 1 scenario and loses 2; R1-text wins 6 and loses 9.

**The anachronism control does not reproduce the direction, which is the point.** Replaying the
54 scenarios on the six most common base shas, over the map corpus that existed when the question
was asked (8 to 18 dossiers, against HEAD's 20) — `python m4/era.py`:

```
rank-1 changed: 26/54 (48.1%)
truth reachable in the shortlist:  17/54
hit@1   shipped 2/17 (11.8%)   re-ranked 2/17 (11.8%)
hit@5   shipped 9/17 (52.9%)   re-ranked 10/17 (58.8%)
```

Tied at rank one, re-ranking ahead by ONE scenario at five. Set against the HEAD result where
shipped is ahead by two, the honest reading is not "shipped wins" — it is **"no difference either
way, on a corpus far too small to see one, while more than half the answers change."**

### Six hand judgements on the biggest moves

`python m4/an4.py`, `python m4/an6.py <spec-id>...`

| spec | query | shipped rank 1 | re-ranked rank 1 | verdict |
|---|---|---|---|---|
| scenario `TOOL-aCollapsedScan-7` | resolve the repository root for a kit invoked by git | `resolve` (recall_conf.py, fan-in 26) — **the seam the spec cites** | `repo_root` #1, `resolve` gone from the top 20 | **worse**; R1-text loses both, fatal |
| scenario `DEPL-aFusedCharter-1` | render a shipped template into a target repo from a conf | `render` (render_playbook.py) at #4 | `render` below 20; nearest truth-carrying row at #20 | **worse** |
| scenario `TOOL-cKeyedLaunchpad-5` | select records by the paths a change touches | `records` (gotchas.py) at #3 | `cmd_for_paths` (gotchas.py) at #16 | **worse position, apter name** — call it a wash |
| scenario `DEPL-dRatifiedSeam-1` | selftest arm asserting a tracked file count invariant | `tracked` (govkit.py) #1 — **cited** | `count_never_falls` (govkit.py) #4 | **equivalent**; right file either way, arguably the apter symbol |
| scenario `TOOL-dRetiredFork-3` | distinguish a present-but-unparseable record header from an absent one | `StaleHeader` at #6 | `StaleHeader` at #5, six truth-carrying rows in the top 20 against three | **better**, mildly |
| scenario `TOOL-aSealedCaravan-1` | deploy a kit into a target repo | `write_text` #2 (in truth) | `kit_rel` #2 (in truth) | **equivalent**; R1-text worse |

Three worse, two equivalent, one better. Consistent with the aggregate.

### The failure mode the rates hide

`python m4/an7.py`. **36 of 132 graded queries have `run`, `read_text`, `write` or `read` as the
shipped rank one, and the shipped rank one hits the truth on ZERO of them.** Re-ranking replaces
that junk on all 36 — and hits the truth on zero of them too.

What actually changes is how the junk LOOKS. Shipped answers "resolve a repository root" with
`run` in `settings-merge.py` at fan-in 28; a reader discards it in a second. R1-ident answers
"unattended run authorization anchor observed from the remote" with `anchor_at` in
`memory-recall/extract.py`, and "write a run-state fact after validating it" with `cmd_write` in
`gotchas.py`. Both are wrong. Both read like they might be right. **The re-ranking raises the
plausibility of the wrong answer without raising its correctness**, which is a cost, not a wash.

The degenerate answers get worse, not better. Most frequent rank-1 across the 179 queries:

- shipped: `run` 32 times
- R1-ident: `build_reference_index` 25
- R1-text: `build_form_index` (a lexicon-internal helper in `tools/lexicon/canon.py`) **25 times**,
  and the multi-name affordance string `` `KITDIR`/`ROOTN`/`KITREL`/`LEGS_FILE` `` **20 times**

That last one is a defect, not a tie-break. A candidate with no def file has fan-in 0 and never
appears in the identifier index, so `df = 0 <= 15` reads as maximum rarity and the row scores a
perfect 3. Under R1-text, **24 of 179 rank-1 answers are file-less rows** — an inventory key or an
affordance-seam line — against 6 today. The confidence signal as written treats "I have no evidence
about this name" as "this name is highly distinctive".

### Why the 1.6% -> 80.0% headline does not transfer

`python rerank.py` reproduces byte-for-byte: p@5 1.6% shipped, 80.0% re-ranked. Read the script.
It builds ONE list — `scored`, the 224 Python symbols carrying at least one edge — sorts it twice,
and reports the precision of rows 1..5. There is no query anywhere in it.

`reuse_lookup` produces a per-query shortlist whose membership is fixed by `m.stems(query)` before
any sort. Its median length here is 75 rows with 63 seeds. Precision@5 over a global symbol ranking
and hit@5 over a query shortlist are two different measurements of two different objects, and the
first one's 50x lift shows up in the second as -2.1 points.

---

## b. Cost

`python m4/cost.py`, n>=7 per stage, medians, node `d` (whose AV taxes every process creation
~0.022 s and whose wall readings are known to vary 3x).

| stage | median | note |
|---|---|---|
| `load_corpus` (committed artifacts + dossiers) | **0.008 s** | 839 candidates |
| `build_reference_index` (the on-demand scan) | **1.155 s** (n=21, min 0.804, max 1.345) | 52 covered-layer files |
| `assemble_shortlist`, one query | **0.012 s** | |
| sort, shipped ordering | **0.000016 s** | 115 rows |
| sort, re-ranked ordering | **0.000037 s** | +21 microseconds |
| confidence tier for the WHOLE 839-name corpus (ident DF) | **0.00035 s** | computed once, reused |
| raw-text DF over 1520 tracked files (**the R1-text spelling**) | **2.368 s** (n=5) | a second full-corpus scan |
| end-to-end `python tools/codebase-map/reuse_lookup.py "..."` | **1.605 s** (n=7) | |

**"The confidence signal needs no new parsing" is true of one spelling and false of the other.**
R1-ident is free: the DF it needs is `len(IDX.get(name))` off an index `fan_in` already built. It
adds 21 microseconds to a 1.6 s command — 0.0013%, unmeasurable in practice, and the brief's
prediction is confirmed rather than asserted. **R1-text costs 2.368 s**, more than doubling the
command, because raw-text DF is a second scan over 29x more files than the covered layer.

### Against the two reference costs

The dossier's `build_reference_index` figure is 0.595 s median (n=153, min 0.383, max 0.807).
My 21-run distribution has a MINIMUM of 0.804 — above their median. I did not chase this: node `d`'s
process/IO timings are known to swing 3x and neither reading is wrong, so **use the ratio, not the
absolute.** Measured back-to-back in one session:

```
python sk2_cost.py      # ast receiver-binding pass: median 2.124 s (min 1.932, max 2.290, n=7)
                        # build_reference_index:     median 1.155 s (n=21)
```

Ratio 1.84x, against the 3x the earlier pass computed from two readings taken hours apart.

### Does re-ranking make the receiver-binding pass unnecessary?

**Neither unnecessary nor cheaper to defer — they are fixes to different defects, and on this
evidence neither one moves the answer.** `python m4/e2ab.py` runs a third arm: the shipped ORDER
over an E2 fan-in (bare occurrence, or a dotted occurrence whose receiver binds to a repo module,
minus same-name definers), rebuilt in 1.520 s on this run.

| arm | hit@1 | hit@5 | most frequent rank-1 |
|---|---|---|---|
| shipped | 7 | 21 | `run` x26 |
| re-rank (R1-ident) | 6 | 20 | `build_reference_index` x19 |
| E2 fan-in, shipped order | **8** | 20 | `check` x16 |

E2 kills the `run` degenerate that re-ranking also kills, and replaces it with a `check` degenerate.
All three arms land within two scenarios of each other over 132. Re-ranking corrects the ORDER and
leaves a wrong count; receiver-binding corrects the COUNT and leaves the ordering that count feeds.
Neither substitutes for the other and neither earns its place in the shortlist path on this
evidence — so the cost comparison is moot until something demonstrates a benefit.

---

## c. Regression risk — the citations that fall out

`python m4/an8.py`. scen-1's `cited_seams` is scraped prose and its own caveat says so, so every
citation is first resolved against the live candidate corpus; one that does not resolve is reported
as unresolvable, never as a pass or a fail.

```
cited seams scraped:                                400
resolvable to a live candidate name:                188 (47.0%)  across 94 specs
of those, in the SHIPPED top 5 today:                92
```

| arm | fall out of the top 5 | in a still-live spec |
|---|---|---|
| R1-ident | **37 of 92 (40.2%)** | **14** |
| R1-text | **72 of 92 (78.3%)** | **20** |

Spec status across the 179 replayed scenarios: 145 CLOSED, 26 SPECCED, 6 WONTDO, 1 OPEN, 1 DEFERRED.

The 14 live-spec casualties under R1-ident, by citing spec:

- `TOOL-aSurfacedLexicon-3/-4/-5/-6/-9/-14` — `extract`, `key`, `parse`, `classify`, `check`, `report`
- `TOOL-aMendedLedger-6/-7` — `claims`, `anchors`, `records`
- `TOOL-aStagedLane-3/-4` — `write`, `write_text`, `classify`

R1-text adds `boundedParallel` (cited by `TOOL-dFoldedVerdict-4` and `TOOL-dTieredTribunal-13`),
`build_reference_index`, `repo_root`, `tracked_files`, `kit_rel`, `read_descriptors` and
`cmd_check`, among others.

**No gate breaks.** `tools/memory-tree/check-memory-hygiene.sh` check 12 requires a §10 to RECORD a
probe result and tests for it by substring:

```awk
hasP = (index(s10p, "reuse_lookup") > 0 || index(s10p, "reuse-lookup") > 0 ...)
```

It never re-runs the tool and never compares a citation to live output, and `SPEC10_EVIDENCE_CUTOFF`
is `2026-09-01` in `.memory-tree.conf`. So re-ranking cannot red the bar. The cost is entirely
human: a reviewer who re-runs the probe named in a live spec's §10 gets a different top 5 than the
record claims, on 14 to 20 citations, with nothing to tell them the tool changed rather than the
tree.

**And R1-text's demotions run backwards.** The text spelling punishes a name for being written
about:

| name | identifier-DF | text-DF | tier under text |
|---|---|---|---|
| `boundedParallel` | 4 | **63** | 2 — demoted |
| `resolve` | 27 | 531 | 0 |
| `render` | 5 | **522** | 2 — demoted |
| `records` | 3 | **1058** | 2 — demoted |
| `repo_root` | 14 | **47** | 2 — demoted |
| `kit_rel` | 5 | **16** | 2 — demoted, by one file |

`boundedParallel` is the fan-out seam AGENTS.md §8 names by hand and `REVIEW-PROTOCOL.md` binds; the
text spelling demotes it precisely because the charter documents it. The 15-file cut is arbitrary
and `kit_rel` misses it by a single file.

---

## d. The threshold interaction

`python m4/an9.py`, `python m4/an10.py`. `SEAM_FANIN_THRESHOLD=3` in `.codebase-map.conf`.

### The definer-subtraction number, re-derived

```
seams under shipped fan_in (A):               177 rows / 68 distinct ids
seams under definer-subtracted fan_in (B):    106 rows / 59 distinct ids
fall out of seam-hood under B:                 71 rows (40.1%)
```

71 confirms; the denominator is 177 rows here, not 165.

### The signal and the threshold are the same axis, cut at two points

```
identifier-index DF minus fan_in == 1 for 769 of 769 symbol rows (100.0%)
(DF <= 15) == (fan_in <= 14)        for 769 of 769 symbol rows (100.0%)
```

Confirmed in this tree, not inherited from scen-3. It is arithmetic, not a coincidence: the index
counts the def file, `fan_in` subtracts it. So the cross-tab has a structural zero:

| tier (ident DF) | fan-in 0 | 1-2 | 3-9 | 10-17 | 18+ | total |
|---|---|---|---|---|---|---|
| 3 | 418 | 116 | 52 | 5 | **0** | 591 |
| 2 | 33 | 25 | 38 | 7 | 9 | 112 |
| 1 | 0 | 0 | 1 | 0 | 64 | 65 |
| 0 | 0 | 0 | 0 | 0 | 1 | 1 |

**Tier 3 and fan-in 18+ are disjoint by construction.** R1-ident is therefore not a new signal
layered over fan-in — it is "sort by fan-in descending, having first moved everything above 14 to
the bottom". A band selection wearing a hat.

### Is a tier-3 symbol at fan-in 2 worth more than a tier-1 at fan-in 30?

Against the ast-resolved import edges (the weak yardstick, and the one the proposal used):

| cell | confirmed / edges | precision |
|---|---|---|
| tier 3 AND fan-in 1-2 (**below** the threshold) | 80 / 122 | **65.6%** |
| tier 3 AND fan-in >= 3 (a seam today) | 140 / 157 | 89.2% |
| tier 1 AND fan-in >= 18 (top of the seam list) | 2 / 441 | **0.5%** |
| everything at/above the threshold | 241 / 826 | 29.2% |

Yes — 131x, per edge. **And it does not follow that the threshold is redundant, because that
yardstick and the scenario yardstick disagree, and they disagree for a reason worth stating.**

Precision-per-EDGE asks "is this occurrence a real import?" — a property of the symbol.
Hit-rate-per-ANSWER asks "did the tool point the session at the file it went on to change" — a
property of the answer. A rare compound symbol has few edges and nearly all of them are real, which
makes it a precise EDGE and a useless ANSWER, because a symbol almost nothing calls is not a reuse
seam. **The two are anti-correlated here, and optimizing the first is what degraded the second in
section (a).** The 89.2% and 0.5% cells are real; they are just not measuring usefulness.

### Where the threshold IS redundant: the worklist

`seed_affordances` — the `--converge` big-bang worklist — is a global fan-in ranking over
undeclared seams. That is exactly the object `rerank.py` measured. Its shipped top 20 opens:

```
main       tools/settings-merge.py                 fan-in 37  conf 1
read_text  tools/memory-tree/gen_build_index.py    fan-in 29  conf 1
key        tools/memory-tree/merge-rows.py         fan-in 28  conf 1
run        tools/settings-merge.py                 fan-in 28  conf 1
resolve    tools/memory-recall/recall_conf.py      fan-in 26  conf 0
```

Re-keyed on confidence with the threshold kept:

```
repo_root              recall_conf.py       fan-in 13  conf 3
parse_args             govkit.py            fan-in 10  conf 3
inventory_ids          map_extractors.py    fan-in  6  conf 3
MapError               map_lib.py           fan-in  5  conf 3
map_root               map_lib.py           fan-in  5  conf 3
build_reference_index  map_lib.py           fan-in  4  conf 3
kit_rel                gen_build_index.py   fan-in  4  conf 3
...
```

The two top-20s share **2 names**. And with the threshold DROPPED entirely, the confidence-keyed
top 20 is unchanged — its fan-ins are `[13, 10, 6, 5, 5, 4, 4, ...]`, all at or above 3, so
**the threshold never binds in the worklist's top 20 once confidence is the primary key.** That is
the one place the brief's redundancy hypothesis measures TRUE.

Caveat on this one, stated plainly: the second list is judged better by reading it, against the
worklist's stated purpose of converging the reinvention-prone surface first. It is not scored
against anything, because a worklist has no ground truth here — nobody has worked it.

---

## Caveats

1. **The scoring ceiling is 36.4%, and it is the dominant limit on everything in (a).** 84 of 132
   graded scenarios have no truth file the shortlist could name at any rank, because symbols.json
   covers Python and JS while the ground truth is 54 `.sh` and 32 `.md`. Both arms are equally
   blind there, so the A/B is fair — but the absolute hit rates describe a corpus a third visible
   to the tool, and no figure here says anything about the bash layer, which is where this repo's
   product lives and which `reuse_lookup` already declares recall-dark.
2. **The margins are one to three scenarios.** hit@1 14.6% vs 12.5% is 7 scenarios against 6 of 48.
   No delta in section (a) should be reported as a finding; the finding is the ABSENCE of one
   beside a 55.9% churn.
3. **scen-1's own caveats ride along in full**, and I did not re-derive them: attribution is by
   commit message and cannot separate implementing an id from mentioning one; 40 of 132 graded rows
   have an empty sole-attribution set; 20 queries are shared by up to 4 scenarios and are counted
   as independent samples in every rate above (the distinct-query figures in (a) are the correction
   for that one and move the headline by 0.0 points).
4. **The era-correct control covers 6 bases and 54 scenarios, of which 17 are reachable.** It was
   run to check that the HEAD result is not an artifact of dossiers the graded units wrote, and it
   does its job — it fails to reproduce the direction, which is why the verdict is "no difference"
   rather than "shipped wins". It is not itself a measurement of anything at n=17.
5. **`cited_seams` is scraped prose and 53% of it does not resolve to a candidate name.** Section
   (c)'s 37 and 14 are counted over the 92 that resolve AND sit in the top 5 today. A citation that
   failed to resolve is neither counted as safe nor as lost, and I did not read the 212
   unresolvable ones to find out which they were.
6. **AMBIENT is a reconstruction.** `dir(str) | dir(list) | dir(Path) | builtins`, spelled to match
   scen-3's `build_scen3.py` so the tiers are the same numbers in both files. It is not the original
   proposal's member set, which was never written down, and `walk` for instance is a `Path`
   attribute only on 3.12+.
7. **Every timing is one node on one afternoon.** node `d` taxes process creation ~0.022 s and its
   wall readings vary 3x; my `build_reference_index` minimum (0.804 s) exceeds the earlier pass's
   median (0.595 s) and I did not resolve the disagreement. Use the RATIOS: re-rank is ~5 orders of
   magnitude below the scan it rides on, receiver-binding is ~1.8x that scan, raw-text DF is ~2x it.
8. **No session was observed.** Everything here is an argument from tool output.
9. **One repo, 26 days, two dominant kits.** Nothing here says how `reuse_lookup` behaves in an
   adopting repo, on a different language mix, or on a corpus it did not grow up beside.

---

## Reproduction

All scripts read the tracked tree read-only and write only into the scratchpad.

```
cd <scratchpad>/m4
python ab.py        # replay 179 queries, both arms -> ab.json
python an1.py       # rank-1 / top-5 churn
python an2.py       # scored against closed-unit ground truth
python an3.py       # the scoring CEILING, first
python an4.py       # biggest rank-1 moves, for hand judgement
python an5.py       # wins and losses, named
python an6.py TOOL-aCollapsedScan-7 ...   # one scenario in full
python an7.py       # the ambient-junk rank-1 class
python an8.py       # (c) citations that fall out of the top 5
python an9.py       # (d) cross-tab and per-cell precision
python an10.py      # (d) the DF identity and the worklist
python era.py       # (a) era-correct control at base shas
python cost.py      # (b) every stage, medians
python e2ab.py      # (b) re-rank vs receiver-binding, same shortlists
```
