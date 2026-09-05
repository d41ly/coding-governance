# TOOL-dTracedLattice-1 — fan-in stops counting homonyms and stops discarding real dotted references

**Status:** SPECCED · rev-6 · 2026-09-05 · node d · Tier-2 · base c4fcf5ad · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-build-TOOL-dTracedLattice-1-baseline_ranks.py](../build/2026-09-05-build-TOOL-dTracedLattice-1-baseline_ranks.py) | research | TOOL-dTracedLattice-7 |
| [2026-09-05-build-TOOL-dTracedLattice-1-build_scen3.py](../build/2026-09-05-build-TOOL-dTracedLattice-1-build_scen3.py) | research | TOOL-dTracedLattice-7 |
| [2026-09-05-build-TOOL-dTracedLattice-1-design-dossier.md](../build/2026-09-05-build-TOOL-dTracedLattice-1-design-dossier.md) | research | TOOL-dTracedLattice-2 TOOL-dTracedLattice-3 TOOL-dTracedLattice-4 TOOL-dTracedLattice-5 |
| [2026-09-05-build-TOOL-dTracedLattice-1-grade.py](../build/2026-09-05-build-TOOL-dTracedLattice-1-grade.py) | research | TOOL-dTracedLattice-7 |
| [2026-09-05-build-TOOL-dTracedLattice-1-harness.py](../build/2026-09-05-build-TOOL-dTracedLattice-1-harness.py) | research | TOOL-dTracedLattice-7 |
| [2026-09-05-build-TOOL-dTracedLattice-1-harvest.py](../build/2026-09-05-build-TOOL-dTracedLattice-1-harvest.py) | research | TOOL-dTracedLattice-7 |
| [2026-09-05-build-TOOL-dTracedLattice-1-meas-cost-and-regression.md](../build/2026-09-05-build-TOOL-dTracedLattice-1-meas-cost-and-regression.md) | research | TOOL-dTracedLattice-7 |
| [2026-09-05-build-TOOL-dTracedLattice-1-meas-memory-recall-recall.md](../build/2026-09-05-build-TOOL-dTracedLattice-1-meas-memory-recall-recall.md) | research | TOOL-dTracedLattice-7 |
| [2026-09-05-build-TOOL-dTracedLattice-1-meas-reuse-lookup-recall.md](../build/2026-09-05-build-TOOL-dTracedLattice-1-meas-reuse-lookup-recall.md) | research | TOOL-dTracedLattice-7 |
| [2026-09-05-build-TOOL-dTracedLattice-1-meas-shared-mechanism.md](../build/2026-09-05-build-TOOL-dTracedLattice-1-meas-shared-mechanism.md) | research | TOOL-dTracedLattice-7 |
| [2026-09-05-build-TOOL-dTracedLattice-1-recall-report.md](../build/2026-09-05-build-TOOL-dTracedLattice-1-recall-report.md) | research | TOOL-dTracedLattice-7 |
| [2026-09-05-build-TOOL-dTracedLattice-1-resolver.py](../build/2026-09-05-build-TOOL-dTracedLattice-1-resolver.py) | research | TOOL-dTracedLattice-7 |
| [2026-09-05-build-TOOL-dTracedLattice-1-scen-adversarial-seams.md](../build/2026-09-05-build-TOOL-dTracedLattice-1-scen-adversarial-seams.md) | research | TOOL-dTracedLattice-7 |
| [2026-09-05-review-TOOL-dTracedLattice-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-dTracedLattice-1-spec-audit-round1.md) | spec-audit | TOOL-dTracedLattice-2 TOOL-dTracedLattice-3 TOOL-dTracedLattice-4 TOOL-dTracedLattice-5 |
| [2026-09-05-review-TOOL-dTracedLattice-1-spec-audit-round2.md](../reviews/2026-09-05-review-TOOL-dTracedLattice-1-spec-audit-round2.md) | spec-audit | TOOL-dTracedLattice-2 TOOL-dTracedLattice-3 TOOL-dTracedLattice-4 TOOL-dTracedLattice-5 |

<!-- /gen:spec-records -->

## 1. Goal

Raise the precision of `map_lib.fan_in` so that `reuse_lookup`'s ranked output is worth the mandate
that makes reading it compulsory. Measured against AST-resolved import edges, the shipped heuristic
scores 14.5% precision overall and 7.2% in the fan-in band that `reuse_lookup` prints first.

## 2. Scope (IN)

Ordered by MEASURED value. The ordering changed at rev-5: what led this list for four revisions was
a precision fix, and scenario-based recall showed precision does not predict the answer.

- **S1** The name-merge defect. `Candidate.file: str` becomes `files: tuple[str, ...]` and
  `load_corpus` stops keeping `file or prev.file`, so a symbol defined in several files is reachable
  through every definer instead of through one arbitrary winner. 124 of 769 definitions (16.1%) are
  unreachable today; `repo_root` has four definers and the shortlist prints one. This is not a
  ranking change and it is worth more than every ranking change measured.
- **S2** Retrieval: a behaviour-phrase to seam bridge. 17 of 17 misses on the adversarial set and
  roughly 15% of the graded replays fail on an EMPTY STEM INTERSECTION between the phrase a session
  types and the symbol's name — unreachable at any K, and lifting `NEIGHBOUR_CAP` to infinity reaches
  none of them. Cheapest credible probes, both stdlib and both to be MEASURED rather than assumed:
  stem the query against each candidate's docstring first line as well as its name, and match on
  stem prefixes for names not otherwise matched.

  **This is ADJACENT to two units node `a` has already specced, and the boundary is worth stating
  because all three touch `reuse_lookup`'s candidate pool.** `TOOL-aTunedCompass-6` moves the
  neighbour cap to AFTER the ranking, so the twelve slots go to the twelve the ranking would keep
  rather than the twelve whose names sort earliest. `TOOL-aTunedCompass-10` narrows the `same kind`
  arm, which today admits almost the whole symbol corpus. Both change candidates that are ALREADY IN
  the pool. S2 is about candidates that never enter it at any pool size, which is what the 17 of 17
  measurement establishes — and that measurement is evidence FOR `-10`, since a cap over a pool
  admitting the whole corpus is spent before relevance is consulted. S2 must not re-implement either;
  if they land first it extends them, and if it lands first it leaves the pool and the cap alone.
- **S3** A stem-specificity SECONDARY sort key, derived from `build_reference_index`'s own output at
  STEM granularity — 4934 tokens to 1924 stems in 0.0164 s, nothing committed, drift structurally
  impossible. NOT the identifier document frequency, which is `fan_in` itself. Lands only if it
  clears AC3's chance control, because its margin is currently indistinguishable from a random seed
  shuffle at r@20.
- **S4** Report a miss as a miss. A harness that folds an unfound answer in as `rank = len(shortlist)`
  reads a recall failure as a ranking change, which is how the rev-4 design mistook one for the other.
- **S5** Subtract same-name definers in `fan_in`. Retained from rev-1 and DEMOTED: it raises
  ast-edge precision from 14.5% to 33.8%, and that yardstick is now known not to predict the answer.
  It has never been scored against the scenario sets, so it lands only under the same ACs as S3.
- **S6** Report the index's own coverage on every call: attribute sites bound, sites left unresolved,
  and every language layer not scanned at all.
- **S7** Amend `TOOL-aScouredKit-16` with the measurement rejecting its dot-prefix proposal, and
  carry `TOOL-dTracedLattice-3` S3's three corrections to the same row. This unit is the ONLY one
  that edits it.
- **S8** Land the scoring instruments as tracked files under `tools/codebase-map/`: the variant
  harness, the scenario sets, and the graded corpus as FIXTURES rather than as remembered numbers.
  The AST resolver comes from `TOOL-dTracedLattice-6` at order 1. A fixture measured against THIS
  corpus is withheld from adopters, the way `recall-fixture.json` is.
- **S9** Update `tools/codebase-map/map_diff.py`, which calls `fan_in` at `:204` and computes the
  dead-export figure at `:207`.

## 3. Non-goals (OUT)

- **No confidence re-ranking, and this is a REVERSAL.** Rev-4's successor design proposed sorting by
  a tier built from name shape and token frequency. Measured against scenarios it takes recall@5 on
  the adversarial set from 11/28 to 2/28, nine answers move down and none moves up, McNemar exact
  p = 0.0039. §4 records why it looked right.
- **No re-derivation of `SEAM_FANIN_THRESHOLD`.** Rev-3 added that as S8 and rev-5 removes it: the
  threshold is shared with `--converge` and `seed_affordances` and answers a different question, so
  redefining a seam to fix a sort order breaks the convergence worklist.
- No committed relation artifact; that is answered in this build's README on `AGENTS.md` §12 grounds.
- No change to `symbols.json`, its schema, or the freshness gate — `TOOL-dTracedLattice-2` owns the gate.
- No type inference. A receiver that cannot be bound by import analysis alone stays unresolved and is
  REPORTED as unresolved.
- No receiver-binding pass in this unit. It was rev-1's S2; the measurements put it behind S1 and S2
  and it needs its own spec once those have landed and moved the numbers.
- No re-keying of `seed_affordances`, and no fix to `bench.run_rm3` — that is
  `TOOL-dTracedLattice-7`, in a different kit.

## 4. Design

### Data model

`build_reference_index` gains a per-file record of whether each occurrence was bare or attribute-form,
and for attribute form, the receiver name. A second pass resolves receiver names to repo modules using
the import statements already parseable with `ast`. `fan_in` then takes a definer set rather than a
single `def_file`.

`fan_in` has FOUR PRODUCTION call sites across THREE files: `map_diff.py:204`, `map_lib.py:1240`,
and `reuse_lookup.py:264` and `:274`. `selftest.py` holds five more, at `:898` through `:901` and
`:936`. Each production site must supply the definer set.

`map_lib.py:1240` is the hard case and rev-2's enumeration omitted it while the sentence beside it
called `detect_collisions` "the hard case" — naming a problem and not locating it. That call sits
INSIDE `detect_collisions`, which sees only the union of base and new rows and never the head symbol
table, so it cannot build a head definer set itself. It is therefore given one by its caller; keeping
the old signature there behind a compatibility path is rejected, because a silent fallback to the old
behaviour at one call site is exactly how a precision fix half-lands — which is what rev-2's own
omission would have caused.

### Alternatives rejected

`TOOL-aScouredKit-16` proposes discarding dotted occurrences outright. **Measured, that is harmful:**
scored against 329 AST-verified edges over 127 rows, the bare-only variant scores 4.9% precision and
25.2% recall against the shipped 14.5% and 100%, and combined with S1 it scores 11.2% and 8.1%. It
discards 198 of 211 verified edges because this repo's dominant idiom is aliased-module dotted calls.
S1 alone scores 33.8% precision at 82.9% recall and 0.46 mean absolute error against the shipped 1.38.
S1 plus S2 is the design; S1 alone is the fallback if S2 does not pay for its cost.

### What node `a` measured independently, and where we differ

`aWeighedCompass` graded 170 recorded reuse phrases against two ground truths and landed CLOSED on
2026-09-04, before this unit's measurement existed. The two passes agree where it counts and the
agreement is the strongest evidence either produces, because the harnesses, the node and the scoring
were all different: their `hit@1` against files the unit changed is 6.0% over n=133 and this unit's
is 6.8% over n=132.

Two of their findings refine figures here and are carried rather than re-derived. **The hit rate is
size-biased**: 37.5% for a unit touching three product files or fewer against 66.0% for one touching
eight or more, because a larger truth set gives the probe more targets. So the corpus-weighted
figure flatters exactly the large unit the charter's "keep units small" rule discourages, and the
number that matters for a small focused unit is the lower one. And **the probe's top is better than
its bulk**: graded against the seam a §10 author actually chose, the median correct hit sits at rank
2, against rank 6 when graded against files eventually edited.

That last figure sits in TENSION with this unit's band analysis, which found ast-edge precision of
7.2% in the highest fan-in band. Both can hold — they measure different objects, one the edges under
a symbol and the other the position of the first correct path — but nobody has reconciled them, and
a unit that changes the ranking should not proceed as though only one exists. Recorded as a known
disagreement rather than resolved by preferring the convenient number.

### Alternatives rejected — the confidence re-rank

Sorting by a tier built from name shape and token frequency, ahead of fan-in. It is recorded here
rather than deleted because it was measured twice with opposite results, and the second measurement
is the one that counts.

Against ast-resolved import edges it looked decisive: precision@5 rose from 1.6% to 80.0%, and that
lift is real and transfers to the per-query shortlist, 28.3% to 81.7% against a 39.6% random-order
control. Against SCENARIOS it loses: recall@5 on the 28-row adversarial set falls from 11/28 to 2/28,
nine answers move down and none moves up, McNemar exact p = 0.0039, and the sign is negative at @1
and @5 across all four arm and predicate combinations of the graded replay.

Both are true, and the reconciliation is the lesson: **edge precision and answer hit-rate measure two
different objects, and only the second is the question a session asks.** Three of the tier's own terms
also failed independently. The `token df <= 15` term is `fan_in <= 14` over the corpus the tool
already holds — identifier-DF minus `fan_in` is +1 for 645 of 645 symbols, rho +1.0000 — so a
proposal reading "tier, then fan-in" was "fan-in, then fan-in" in its third term. The `ambient` filter
discriminates 4 names of 645 and its only catch among the seven highest-fan-in common names is
`resolve`, a false positive costing rank 1 to rank 83. And a raw-text spelling of document frequency
costs 1.554 s per query and demotes `boundedParallel` for being documented.

### Rollout

S1 first and alone: it is the largest measured gain, it changes no ranking, and it needs no new
pass. S2 second, because retrieval failures are unreachable at any K and no ordering change touches
them. S3 and S5 only after both, and only if they clear AC3's chance control — they are the two
items whose value is currently indistinguishable from a random shuffle at depth.

## 5. Production-readiness checklist

- security — N/A, no new input surface; the scan reads tracked source it already reads.
- perf / scale — the receiver-binding pass measured a median 1.761 s against `build_reference_index`'s
  0.595 s. AC8 is the ceiling now: at most 0.05 s added, and no second full-corpus scan. Rev-4 gave
  the re-declaration to a scope item; rev-5 makes it an acceptance criterion instead, because a
  ceiling nothing grades is a ceiling nobody meets.
- a11y — N/A, a CLI.
- i18n — N/A.
- error / empty / loading states — an unparseable file is skipped fail-open, as today, because this
  feeds a ranking and not a gate. The skip is counted and reported by S6.
- observability — S3 is the observability item.
- risks — the fan-in-0 population grows, so `dead_exports` inflates; §8 carries the disposition.
- testing + left-shift gates — arms in `tools/codebase-map/selftest.py`, each observed RED first.
- migration / rollback — no committed artifact moves, so rollback is reverting the functions.
- user docs — `tools/codebase-map/README.md` and `reuse-lookup.agent.md` state what the ranking means.

## 6. Acceptance criteria

Thresholds are the measured shipped baselines, so a change that does not beat them is not landed.

- **AC1 — do not lose on the adversarial set.** recall@5 over the 28 rows in
  `2026-09-05-build-TOOL-dTracedLattice-1-scen-adversarial-seams.md` is at least the shipped `11/28`.
  The rejected confidence re-rank scores `2/28`.
- **AC2 — S1 recovers the unreachable definers.** After the name-merge fix, every one of the 124
  definitions currently unreachable is reachable, asserted by an arm over `symbols.json` that fails
  when any `id` with several definers yields fewer candidates than it has definers.
- **AC3 — beat chance, not merely the shipped key.** Any ranking change is scored against 200 random
  seed-shuffles of the same shortlist and clears the 95th percentile at the k claimed. Shipped sits
  at the 5th percentile at `r@20`, so beating shipped at depth is not evidence.
- **AC4 — paired significance with the discordant count.** McNemar exact or a 20000-trial paired
  permutation, and no delta with fewer than `6` discordant pairs is reported as a finding.
- **AC5 — score under BOTH resolutions.** Strict, def-file only, and resolved through
  `[paths].globs`. At @20 over the 132 graded scenarios shipped scores `32` strict and `97` resolved;
  a change winning one and losing the other has been framed, not measured.
- **AC6 — replay at each spec's own `base_sha`, not only at HEAD.** 129 of 132 graded scenarios
  resolve one, and rank one changes on 48.1% of scenarios between base and HEAD, so a HEAD-only
  measurement credits the tool with dossiers the graded unit itself wrote.
- **AC7 — quote the predicate.** Any name-shape or frequency predicate is pinned by source in this
  spec and any harness re-implementation is byte-compared against it; two spellings of `compound`
  disagreeing on 12 of 839 candidates moved a headline by 10 scenarios.
- **AC8 — cost ceiling.** At most `0.05` s added to a roughly 1 s command, and no second
  full-corpus scan. The stem-posting key adds `0.0164` s; a raw-text document-frequency spelling adds
  `1.554` s and fails this criterion alone.
- **AC9 — beat the constant-answer control.** A leave-one-out control that ignores the query and
  returns the K most-frequently-changed files scores .098, .515, .720 and .841 at K of 1, 5, 10 and
  20. Any file-granularity `recall@K` that does not beat those establishes nothing. The figures are
  written unbackticked on purpose: a slash-separated numeric list inside backticks reads as a path
  citation to the spec-tokens leg, which is how this criterion reddened the bar once already.
- **AC10 — disclose citation churn.** Report how many of the 92 resolvable seams cited in a
  `## 10. Reuse audit` and currently in a shipped top 5 leave it, and how many sit in live specs. A
  disclosure, not a blocker.
- **AC11 — the amendment lands.** `memory/backlog/TOOL.md`'s `TOOL-aScouredKit-16` names the rejected
  dot-prefix half with the measurement rejecting it, and no longer claims the reinvention backlog is
  tracked, permanent, or shipped to adopters.

`precision@5` over the global symbol list is a DIAGNOSTIC and never an acceptance criterion. It is a
real measurement that transfers to the shortlist — `28.3%` to `81.7%` against a `39.6%` chance
control — and it still does not predict whether the shortlist named a file the unit changed.

## 7. Gates

`codebase-map kit selftest` · `codebase-map coverage + freshness` · `memory hygiene` ·
`harness arms (fail branches armed or pinned)`. No new leg: the arms join the kit's existing selftest.

Both `codebase-map kit selftest` and `codebase-map coverage + freshness` are kit-subject legs and are HELD on a plain bar; a builder verifying this unit needs `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`. The runner names every held leg, so they are announced rather than silent.

## 8. Open questions

- **Q1 — the `dead_exports` disposition.** S1 grows the fan-in-0 population from 451 to 532, and the
  hint is already weak: it is a bare scalar with no list, and its 451 rows are dominated by 120
  selftest definitions, 13 name-dispatched `cmd_*` handlers and a block of module-private dataclasses
  that read dead only because `fan_in` subtracts the definition file. **The follow-up already exists:**
  `TOOL-aScouredKit-17` owns the dead-export disposition and says it should land with `-16`, the row
  S5 amends. Its `412` was measured at `093730e4` and reads `451` at `c4fcf5ad`, so its next reader is
  not comparing two trees. RESOLVED (agent, 2026-09-05): the disposition belongs to
  `TOOL-aScouredKit-17`; this unit reports the movement per AC8 and declines the co-landing, because
  narrowing the population is a second mechanism and M2 forbids two mechanisms in one spec.
- **Q2 — whether S2 pays for its cost.** FACT-QUESTION · the probe is the precision harness of AC1 run
  with and without S2, and the observation that decides it is whether S2's precision exceeds S1's by
  more than the ratio its wall clock grows. LIVENESS: the harness already distinguishes four variants
  at four different scores, so it can return a negative. RESOLVED (agent, 2026-09-05, delegated): the
  probe runs before S2 lands and S1 ships regardless.

## 9. Revision log

- rev-1 · 2026-09-05 · initial draft, from the dTracedLattice design pass and its skeptic round.
- rev-6 · 2026-09-05 · reconciled against node `a`'s `aWeighedCompass` and `aTunedCompass`, landed
  on main while this build was in flight. S2 names `TOOL-aTunedCompass-6` and `-10` and states the
  boundary; §4 carries their independent `hit@1` corroboration, their size-bias refinement, and the
  unreconciled tension between their rank-2 median and this unit's 7.2% top band.
- rev-5 · 2026-09-05 · folded the scenario-based recall measurement, which REVERSED the successor
  design this spec was heading toward. The confidence re-rank is refused in §3 and recorded in §4
  with both measurements. Scope is re-ordered by measured value: the name-merge defect leads, the
  retrieval bridge is second, the precision fix is demoted to S5, and rev-3's
  `SEAM_FANIN_THRESHOLD` re-derivation is removed. §6 is rewritten against measured baselines and
  `precision@5` is demoted to a diagnostic.
- rev-4 · 2026-09-05 · the owner ratified the lexicon rescue, so S6 extends
  `TOOL-dTracedLattice-6`'s resolver instead of building one, and this unit moves to order 2.
- rev-3 · 2026-09-05 · folded the round-2 spec audit: B1 (S5 and AC6 widened to RECEIVE the three
  corrections unit 3 S3 hands over — rev-2 declared the sole-editor rule and left them owned by
  nobody), B2 (§4's call-site list was false in both directions and omitted `map_lib.py:1240`, the
  very call it called the hard case), H1 (AC9 grades S8, which AC7 could not), M1 (§7 discloses that
  the kit legs are held).
- rev-2 · 2026-09-05 · folded the round-1 spec audit: B2 (S6 lands the scoring instrument AC1 and AC2
  are scored by), H1 (§4 names `fan_in`'s four call sites and the `detect_collisions` case), H6 (§8 Q1
  cites `TOOL-aScouredKit-17`), H7 (S8 re-derives `SEAM_FANIN_THRESHOLD`, AC7 pins the seam
  population), and B1's reassignment of `map_diff.py` into this unit's write set as S7 with AC8.

## 10. Reuse audit

The seam this unit extends is `map_lib.fan_in` together with `map_lib.build_reference_index`, cited
from `python tools/codebase-map/reuse_lookup.py "derive relations between symbols and expose them to
the orientation tools"`, which returns `render_symbols_json` (`tools/codebase-map/map_lib.py`,
fan-in 4, SEAM) at rank two and no seam for the reference index itself — a result this unit's own
subject explains, since the ranking that produced it is the thing being repaired. `resolve_import` in
`tools/lexicon/lexicon.py` already performs AST import resolution and is the prior art for S2, but it
is SPECCED for deletion by `TOOL-aSurfacedLexicon-2` at order 1, so it is prior art rather than a seam
to wire through.

Recall terms used: codebase-map relations fan-in reference index symbols dossier reuse_lookup
memory-recall corpus retrieval seam affordance converge
