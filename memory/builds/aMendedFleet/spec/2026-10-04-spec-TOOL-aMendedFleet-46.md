# TOOL-aMendedFleet-46 — the replay harness measures which shortlist quantity predicts a reuse miss, before any miss signal ships

**Status:** SPECCED · rev-2 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 46

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`reuse_lookup.py` answers every query with the same confidence, and a reader cannot tell an answer
that missed the seam from one that found it. The review asked for a miss signal and, first, for a
predictor that earns one, because the obvious candidate does not: seed coverage scores absent
capabilities higher than real hits. A probe at `fee9f62b` measured eight shortlist quantities against
the replay corpus and none separates hits from misses, since 104 of the 115 misses have ground truth
outside the indexed corpus, which no shortlist quantity can see. This unit commits that measurement
as a `--predictors` mode of `tools/codebase-map/replay-phrases.py` with a stated qualifying rule,
re-runs it after unit 35 lights the shell layer, and records the verdict. A runtime miss line ships
only from a verdict that names a predictor, and then as a unit the run adds.

## 2. Scope (IN)

- **S1** — `measure_predictors(corpus, ref, phrase, truth)` in `replay-phrases.py` returns, beside
  `measure_phrase`'s fields and the phrase's reachability, eight values read off the shortlist
  `rl.assemble_shortlist` returns, using `m.stems` and never a second ranker:
  `seed_coverage`, the best seed's shared query stems over the query's stems; `best_overlap`, that
  shared count; `union_coverage`, the stems any seed shares over the query's stems; `n_seeds`;
  `n_ranked`; `idf_coverage` and `best_idf`, the best seed's shared stems weighted by inverse
  document frequency over candidate names; and `q_len`, the query's stem count. Observed by AC1 and
  AC3.
- **S2** — `derive_auc(pos, neg)` returns the Mann-Whitney AUC with ties counted half, and
  `measure_shuffle_band(rows, trials, seed)` returns the minimum and maximum AUC that any of S1's
  predictors reaches over `trials` shuffles of the hit labels from a fixed seed, 50 and 0 by
  default, so the band is the noise floor of the whole table and not of one row. Observed by AC2.
- **S3** — `derive_predictor_verdict` names a predictor only when, over one population, its AUC is
  at least 0.70 or at most 0.30, lies outside the shuffle band, and that population holds at least
  30 hits and 30 misses; otherwise it returns `none qualifies` with the reason, `too few misses`
  included. It grades two populations: every graded phrase, and the phrases whose truth is
  reachable. Observed by AC1 and AC2.
- **S4** — `--predictors` prints the label split per population, one AUC row per predictor per
  population, the band, and exactly one `miss predictor: <verdict>` line; with `--json` the summary
  gains a `predictors` object carrying the same table, band and verdict, and each row its eight
  values. The run stays under the existing `CEILING_S` and exits as the mode without the flag does.
  Observed by AC1 and AC3.
- **S5** — The verdict, measured at this unit's pass after unit 35 has landed, is recorded with its
  date and sha in this unit's AC4 evidence, and the `## Gaps` of
  `memory/map/features/codebase-map.md` gains one line opening `miss predictor:` that states the
  verdict and cites `TOOL-aMendedFleet-46`, so the next ranker change knows what to re-run and where
  the reading lives. The dossier line carries no date, sha or node: `TOOL-aMendedFleet-89`'s rule
  keeps those in the record that measured them. The module docstring's usage block names
  `--predictors`. Observed by AC4.
- **S6** — `memory/map/generated/symbols.json` is regenerated for the new definitions, and the
  dossier's prose is refreshed in the same commit. Observed by AC5.
- **S7** — A selftest arm drives S2 and S3 over canned rows. NOT OBSERVED by a criterion here: the
  suite runs once at the close, and the arm is declared under `New arm:` in §7.

## 3. Non-goals (OUT)

- A miss line in `reuse_lookup.py`. If S5's verdict names a predictor, the run adds a unit for the
  line, specced against that verdict; if it names none, as the probe at `fee9f62b` did, no line is
  owed and the dossier says why.
- Changing the ranker, its seeds or its corpus. Unit 35 grows the corpus; this unit only measures.
- A floor or a gate on any AUC. `replay-phrases.py` stays on no leg by owner ruling, and unit 41
  owns its `--floor`.
- Re-labelling the replay corpus. Its phrases were written by authors who knew the answer, which the
  review noted inflates both arms; the instrument reports on the corpus it has.

### Edges

- **consumes-from** `TOOL-aMendedFleet-35` — the shell layer moves phrases from unreachable to
  reachable, so S5's verdict is measured after it lands; measured before, it would describe a corpus
  that no longer exists.
- **consumes-from** `TOOL-aMendedFleet-37` — AC5 reads `map_diff.py --stale-dossiers`, which that
  unit builds.
- **hands-off** external — the runtime miss line, owed only from a qualifying verdict, as a unit the
  run adds.

## 4. Design

### Evidence

Read at base `7af5f564`, whose bytes for every file below equal HEAD's at `fee9f62b`.

- `assemble_shortlist` in `tools/codebase-map/reuse_lookup.py` ranks seeds first, then fan-in, then
  name, and carries no score; every quantity a predictor can read is a property of the seeds and the
  query's stems, which is why S1 derives from those and nothing else.
- `measure_phrase` in `replay-phrases.py` already labels each phrase `hit`, and `main` already
  computes reachability over the corpus files; S1 reuses both.
- A read-only probe, PINNED 2026-10-04 on node a at `fee9f62b`, ran the shipped ranker over the
  shipped corpus, 378 graded phrases, 263 hits, 104 with unreachable truth:

| Predictor | AUC, all phrases | AUC, reachable only |
|---|---:|---:|
| `seed_coverage` | 0.451 | 0.585 |
| `best_overlap` | 0.508 | 0.745 |
| `union_coverage` | 0.518 | 0.487 |
| `n_seeds` | 0.524 | 0.789 |
| `n_ranked` | 0.524 | 0.789 |
| `idf_coverage` | 0.458 | 0.568 |
| `best_idf` | 0.501 | 0.688 |
| `q_len` | 0.568 | 0.699 |

  The shuffled-label band over 50 trials, taken on `idf_coverage` alone, was 0.433 to 0.554; S2's
  band spans every predictor and is at least that wide. Over all phrases nothing reaches 0.70;
  the reachable population holds 274 phrases and only 11 misses, so its high readings rest on too
  few misses to qualify under S3. The verdict read `none qualifies`.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `measure_predictors` | function, `replay-phrases.py` | `py.function`, verb `measure`; `--suggest` answered OK |
| `derive_auc` | function, `replay-phrases.py` | `py.function`, verb `derive`; `--suggest` answered OK |
| `measure_shuffle_band` | function, `replay-phrases.py` | `py.function`, verb `measure`; `--suggest` answered OK |
| `derive_predictor_verdict` | function, `replay-phrases.py` | `py.function`, verb `derive`; `--suggest` answered OK |
| `--predictors` | CLI flag | none |

### Rollout

Units 35, 36 and 41 change the corpus and `replay-phrases.py` first, in order. The verdict is
measured at this pass, never copied from §4's table.

### Files touched (estimate)

- `tools/codebase-map/replay-phrases.py`
- `tools/codebase-map/selftest.py`
- `memory/map/features/codebase-map.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **Ship a miss line on seed coverage.** The review measured its median at 0.12 for hits and misses
  alike, and the probe read its AUC at 0.451, inside the shuffle band.
- **Ship a miss line on `n_seeds` from the reachable population.** It read 0.789 over 11 misses; a
  threshold fitted to 11 cases would be a guess with a number attached.
- **Record the probe and build nothing.** The verdict is due again after unit 35 and after every
  ranker change, and a probe in a scratchpad is re-written each time; a mode of the existing
  harness is one flag.

## 5. Production-readiness checklist

- security — N/A: a local harness reads committed records and prints a table.
- perf / scale — one extra pass over shortlists the harness already builds, plus 50 shuffles of a
  list of a few hundred labels; the probe ran the whole measurement in 14 s.
- error / empty / loading states — a population with no hits or no misses has no AUC and the
  verdict says `too few misses` rather than reporting 0.5.
- observability — the band is printed beside every table, so an AUC is read against noise.
- risks — the corpus labels come from authors who knew their answer, so a predictor qualifying here
  may still fail on a cold query; S3's rule and the added unit's own spec are where that is weighed.
- testing — AC2 drives the rule directly; S7's arm.
- migration — N/A: a new flag on a tool on no leg.
- user docs — the docstring usage line and the dossier's verdict line, S5.

## 6. Acceptance criteria

- **AC1** — When `python tools/codebase-map/replay-phrases.py --predictors` runs at the unit's tip,
  it exits 0 within its declared ceiling and prints, for both populations, the label split and one
  AUC row for each of the eight predictors S1 names, the shuffle band, and exactly one line opening
  `miss predictor:`.
  Red when: a predictor row is missing, the verdict line is absent or repeated, or the ceiling is
  breached.
  figure: DERIVED at observation time; §4's probe read `none qualifies` at `fee9f62b`.
- **AC2** — When a `python -c` caller loads `tools/codebase-map/replay-phrases.py` with `importlib`
  and calls `derive_auc` with positives 3, 4, 5 and negatives 0, 1, 2 it returns 1.0, and with
  three ones on each side it returns 0.5; `derive_predictor_verdict` given an AUC of 0.90 outside the
  band with 40 hits and 40 misses names that predictor, and given the same AUC with 29 misses
  returns `none qualifies` naming too few misses.
  Red when: the AUC is miscomputed, or a verdict names a predictor on too few misses.
- **AC3** — When `python tools/codebase-map/replay-phrases.py --predictors --json` runs, its output
  parses with `python -m json.tool`, the summary carries a `predictors` object with a `verdict` key,
  and every row carries the eight predictor values.
  Red when: the JSON lacks the object, or a row lacks a value.
- **AC4** — When `git grep -n "miss predictor" -- memory/map/features/codebase-map.md` runs, it hits
  one line citing `TOOL-aMendedFleet-46`, and that unit's AC4 evidence states the verdict with the
  date and sha it was measured at; and `git grep -n -e "--predictors" -- tools/codebase-map/replay-phrases.py`
  hits the docstring's usage block.
  Red when: the verdict is measured and not recorded, or the dossier line cites no record of when it
  was measured.
- **AC5** — When `python tools/codebase-map/gen_map.py --check` runs at the tip it exits 0, and
  `python tools/codebase-map/map_diff.py --stale-dossiers` does not list `codebase-map`.
  Red when: the symbol index is stale, or the unit leaves its own dossier older than its paths.

## 7. Gates

`codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/codebase-map/selftest.py` · canned rows with a separable and an inseparable predictor and a population one miss short of the floor, through `derive_auc` and `derive_predictor_verdict`; staged red by dropping the minimum-misses clause · none

## 8. Open questions

- **FACT-QUESTION · F1** — Does any shortlist quantity predict a miss well enough to ship a signal
  on it today?
  Probe: §4's read-only run of the shipped ranker over the shipped replay corpus at `fee9f62b`,
  computing S1's eight quantities per phrase and their AUC against the hit label, with a 50-trial
  shuffled-label control. Observation: whether any AUC clears S3's rule. Liveness: the reachable
  population produced readings of 0.745 and 0.789, so the probe can produce a value far from 0.5,
  and the control band sits around 0.5 as it must.
  RESOLVED (agent, 2026-10-04, delegated): no, today. This unit therefore builds the instrument and
  the rule, records the verdict after unit 35, and builds no runtime line; a qualifying verdict at
  the pass becomes a unit the run adds rather than code in this one.
- **F2** — Which miss does the signal predict: a ranker miss, or a capability the corpus lacks?
  RESOLVED (agent, 2026-10-04, delegated): both populations are graded, because the probe showed
  they behave differently: misses with unreachable truth dominate the whole set and are invisible
  to every predictor, while ranker misses among reachable phrases are where a signal could exist.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the synthesis's item [#39], `assemble_shortlist`,
  `measure_phrase`, and an eight-predictor probe over the replay corpus at `fee9f62b`.
- rev-2 · 2026-10-04 · S5 AC4 · the M2 cross-read: S5 wrote the verdict's date and sha into the
  `codebase-map` dossier, while `TOOL-aMendedFleet-89` adds the map rule that when, where and on
  which node a figure was measured live in the record and the dossier cites its id; the date and sha
  now sit in this unit's AC4 evidence, and the dossier line cites this unit.

## 10. Reuse audit

The seams extended are `measure_phrase` and the reachability count in `main` of
`tools/codebase-map/replay-phrases.py`, the harness that already grades the ranker against the
replay corpus, and `assemble_shortlist` with `m.stems`, read and not changed. `python
tools/codebase-map/reuse_lookup.py "predict whether a reuse lookup answer missed the right seam"`
ranked `seam_fanin_threshold`, `resolve_answers`, `write_lookup` and shared-seams prose neighbours,
none of which predicts anything, so no existing seam fits the predictor; it printed `unscanned
layers: .sh`. Recall returned the synthesis's item 10, `TOOL-aWeighedCompass-8`, which counted
truth that is entirely shell as unhittable by construction, and `TOOL-aWeighedCompass-11`, which
calls the `opened` signal too thin to grade retrieval. Where the report and the tree disagree: the
report's "absent capabilities score 0.17 to 0.25" was not re-measured; its conclusion was, since
seed coverage read an AUC of 0.451.

Recall terms used: `python tools/memory-recall/query.py "how can reuse_lookup tell the reader its
answer probably missed, and what predicts a miss" --terms "reuse_lookup miss signal predictor seed
coverage replay-phrases hit rate unreachable dark layer no seam fits"`
