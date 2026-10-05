# TOOL-aMendedFleet-41 — `replay-phrases.py --floor` grades a frozen phrase population against recorded floors

**Status:** CLOSED · rev-2 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 41

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`replay-phrases.py` is the graded reference for the reuse probe's ranking, and it reports figures
nobody compares against anything: a ranking change that costs hits is visible only to someone who
remembers the last reading. This unit gives it a `--floor` mode that grades a FROZEN population of
recorded phrases against floors recorded in the script and exits non-zero on a breach, and adds the
definition-of-done line that a ranking change runs it. It stays off the merge bar, per the owner
ruling of 2026-08-23 that keeps kit self-tests and corpus graders off it.

## 2. Scope (IN)

- **S1** — `--floor` grades only the phrases harvested from records whose FILENAME date is on or
  before a module constant `FLOOR_CORPUS_DATE`; a record with no date prefix is outside the
  population. The filter applies before the phrase de-duplication, so the population's ground truth
  never comes from a later record. `derive_record_date` reads the date from the basename. Observed
  by AC1 and AC4.
- **S2** — The population is pinned by a module constant `FLOOR_PHRASES`, the graded-phrase count it
  held when the floors were measured. A `--floor` run whose population counts any other number exits
  2 naming both counts, because a floor graded over a different population compares nothing.
  Observed by AC3.
- **S3** — A module constant `FLOOR` maps `hit_rate`, `hit5_rate`, `hit10_rate` and `hit_at_budget`
  to the value each read over that population at the pass. `derive_floor_breaches` returns every
  metric under its floor, and a `--floor` run with any breach exits 1, printing one line per breach
  with the metric, the reading and the floor. Observed by AC1 and AC2.
- **S4** — Without `--floor` the output is unchanged. With it the text output adds one block naming
  the population date, its count and each metric beside its floor, and `--json` adds a `floor`
  object carrying the same. `--floor` with `--limit` exits 2, since a partial population cannot be
  graded against a floor of the whole, and so does `--floor` with a `--budget` other than
  `rl.DEFAULT_BUDGET`, since the `hit_at_budget` floor was read at that default. The floor block
  names the budget it graded at. Observed by AC1 and AC5.
- **S5** — The constants are measured at this unit's pass, after units 35 and 36 have landed, and
  their comment records the date, the node, the base sha and the readings. `FLOOR_CORPUS_DATE` is the
  day before the pass, so no record written later that day enters the population. The comment states
  the rule for moving a floor: raising one is free, and lowering one writes the old and new values and
  the reason beside it. Observed by AC1.
- **S6** — The definition-of-done line lands in the `codebase-map` dossier's `## Constraints & why`:
  a change to the reuse probe's ranking, its candidate lines or the fan-in it reads runs
  `replay-phrases.py --floor` before it lands and records the line it printed. The script's module
  docstring names `--floor` in its usage block. Observed by AC5.

## 3. Non-goals (OUT)

- A merge-bar leg or a hook running it. The owner ruling stands, and AC5 observes it still holds.
- Enforcing the lowering rule in code. A floor value is project data in a project-owned script, and
  its comment is where a reviewer reads the move.
- Fixing the harvester's known inflation, where a §10 sentence naming a path the probe got WRONG
  counts as ground truth. The script's docstring declares it, and it biases both sides of a floor
  comparison equally.
- Grading `rank_harness.py`'s scenario set the same way; it has its own controls.

### Edges

- **consumes-from** `TOOL-aMendedFleet-36` — `hit_at_budget` and the `--budget` default this unit
  floors; measured before that unit lands, the fourth floor would not exist.

## 4. Design

### Evidence

Measured 2026-10-04 on node a at `fee9f62ba`, whose codebase-map kit and generated map are byte
equal to the review's `ac65de998`, so only the phrase corpus moved between the two readings:

| reading | phrases graded | hit rate | hit@5 | hit@10 |
|---|---:|---:|---:|---:|
| review, at `ac65de998` | 335 | 0.672 | 0.400 | 0.454 |
| this writing | 378 | 0.696 | 0.410 | 0.463 |

The hit rate moved 0.024 with no ranker or symbol change, because 43 records written in between
added phrases. A floor over the live harvest would therefore red or pass on record traffic alone,
and a tolerance wide enough to absorb that hides a ranking loss of the 0.014 the dossier records for
the neighbour-cap narrowing. A frozen population moves only when the ranker or the symbol corpus
moves, which is what a floor exists to grade. Figures PINNED as read; S5 re-derives the constants.

### Inventory

| Name | Kind | Cell |
|---|---|---|
| `derive_record_date` | function in `replay-phrases.py` | `py.function`; `--suggest` answered OK |
| `derive_floor_breaches` | function in `replay-phrases.py` | `py.function`; `--suggest` answered OK |
| `FLOOR`, `FLOOR_PHRASES`, `FLOOR_CORPUS_DATE` | module constants | none |
| `--floor` | flag | none; the lexicon declares no flag cell |

### Files touched (estimate)

- `tools/codebase-map/replay-phrases.py`
- `memory/map/features/codebase-map.md`

### Alternatives rejected

- **A floor over the live harvest with a tolerance.** §4's evidence prices the tolerance above the
  smallest ranking loss on record.
- **A committed fixture of phrase and truth pairs.** It freezes the population too, but it is a
  second copy of what the records already say, and it would need its own freshness rule; a date cut
  derives the same population from the tree and commits nothing.
- **Floors in `.codebase-map.conf`.** The conf ships to adopters as a grammar, and this script and its
  readings are `project-owned` and never reach one.

## 5. Production-readiness checklist

- security — N/A — a local read-only grader.
- perf / scale — the population is a subset of the run that already happens; one date parse per path.
- error / empty / loading states — a moved population exits 2 naming both counts; an empty one hits
  the existing graded-zero refusal; `--floor` with `--limit` exits 2.
- observability — the floor block prints every metric beside its floor on every `--floor` run, a
  pass included.
- risks — a symbol-corpus change unrelated to ranking can lower a reading; the run names the metric,
  and S5's comment rule makes the re-pin visible in review.
- testing — AC2 to AC4 stage each outcome in a scratch clone; the script is on no leg by ruling.
- migration — N/A — new constants and a new flag.
- user docs — the dossier line and the docstring, per S6.

## 6. Acceptance criteria

- **AC1** — When `python tools/codebase-map/replay-phrases.py --floor` runs at the worktree root after
  the unit's commit, it exits 0, prints the population date and a count equal to `FLOOR_PHRASES`, and
  prints each of the four metrics beside its floor.
  Red when: the population count differs from the pin on the tree it was measured on, or a metric is
  missing from the block.
  figure: DERIVED at the pass; the constants are that reading.
- **AC2** — When a scratch clone under the TEMP root reverses the ranked list `assemble_shortlist`
  returns in `tools/codebase-map/reuse_lookup.py`, the same command in it exits 1 and names at least
  `hit5_rate` with its reading and floor.
  Red when: a ranking that puts the worst candidate first passes the floor.
- **AC3** — When the same scratch clone instead gains one record under the memory builds tree, dated
  before `FLOOR_CORPUS_DATE`, carrying one probe invocation and a §10 naming a tracked path, the
  command exits 2 and prints both population counts.
  Red when: a moved population is graded rather than refused.
- **AC4** — When that record is dated after `FLOOR_CORPUS_DATE` instead, `--floor` exits 0 with the
  pinned count, and `python tools/codebase-map/replay-phrases.py` without the flag reports one more
  graded phrase than before.
  Red when: the frozen population admits a later record, or the plain run stops seeing it.
- **AC5** — When `git grep -n -F "replay-phrases" -- tools/gate-legs.json .github .githooks` runs it
  prints nothing; `grep -n -F -- "--floor" memory/map/features/codebase-map.md` hits the
  definition-of-done line; `python tools/codebase-map/replay-phrases.py --floor --limit 5` exits 2;
  and `python tools/codebase-map/replay-phrases.py --floor --budget 0` exits 2.
  Red when: the script reached a leg, the line is absent, a partial population is graded, or the
  budget floor is graded at a budget it was not read at.

## 7. Gates

`codebase-map coverage + freshness` · `codebase-map gate coverage` · `codebase-map kit selftest` · `codebase-map adopter e2e` · `encoding posture (text IO names its encoding)` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

No arm is added: the script is on no leg by owner ruling, and AC2 to AC4 stage its three outcomes.

## 8. Open questions

- **F1 — Which population does the floor grade?**
  Options: the live harvest with a tolerance; a committed fixture; records dated on or before a
  declared date, with the count pinned.
  RESOLVED (agent, 2026-10-04, delegated): the dated population with a pinned count. §4 measured the
  live harvest moving 0.024 on record traffic alone, and the dated cut derives the frozen set without
  a second copy of it.
- **F2 — Which metrics carry a floor?**
  RESOLVED (agent, 2026-10-04, delegated): all four the summary reports as rates, so a loss at the
  ranks a reader scans, hit@5, is not hidden behind a steady hit rate.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the synthesis's item [#50], `replay-phrases.py` at base and
  two readings of it.
- rev-2 · 2026-10-04 · S4 AC5 · the M2 cross-read: `TOOL-aMendedFleet-36` gives the same CLI a
  `--budget` flag, and a `--floor` run at another budget graded `hit_at_budget` against a floor read
  at the default; S4 refuses that combination at exit 2 and AC5 observes it.

## 10. Reuse audit

The seam extended is `replay-phrases.py` itself: `scan_tracked_specs`, `extract_phrases` and
`measure_phrase` stay as they are, and the floor filters their input and reads their summary. The
ceiling exit in its `main` is the shape copied for the breach exit. `python
tools/codebase-map/reuse_lookup.py "fail a harness when a measured rate falls below a declared floor"`
returned name-stem neighbours, `measure_ranks` in `rank_harness.py` and `count_never_falls` in
`govkit.py` among them, none of which grades a rate against a floor; the probe printed `unscanned
layers: .sh`. `check-recall.py` in the memory-recall kit grades `RECALL_FLOOR` from a conf, which is
the same idea in another kit and a conf this script's readings must not enter, per §4. The recall
probe returned the dossier's two recorded replays and a closing review that found a replay figure
stale after symbols moved, which is the drift §4 measures. Where the report and the tree disagree:
the review read 335 phrases at 0.672; this writing reads 378 at 0.696 with no code change.

Recall terms used: `python tools/memory-recall/query.py "why is replay-phrases kept off the merge bar
and is there a floor on the reuse lookup hit rate" --terms "replay-phrases hit rate hit@10 floor ranker
reuse_lookup owner ruling 2026-08-23 off the bar project-owned graded corpus ceiling"`
