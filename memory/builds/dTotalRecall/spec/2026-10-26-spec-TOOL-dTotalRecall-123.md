# TOOL-dTotalRecall-123 — the map replay run again: more runs per arm, a noise term more runs tighten, and the verdict rule fixed before the first run

**Status:** CLOSED · rev-3 · 2026-11-26 · node d · Tier-2 · base fbe06249 · streams tooling · order 51 · advances TOOL-dTotalRecall-111

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-25-build-TOOL-dTotalRecall-123-1-builder-return.md](../build/2026-11-25-build-TOOL-dTotalRecall-123-1-builder-return.md) | journal | — |
| [2026-11-25-build-TOOL-dTotalRecall-123-2-builder-return.md](../build/2026-11-25-build-TOOL-dTotalRecall-123-2-builder-return.md) | journal | — |
| [2026-11-25-build-TOOL-dTotalRecall-123-3-acceptance-ledger.md](../build/2026-11-25-build-TOOL-dTotalRecall-123-3-acceptance-ledger.md) | log | — |
| [2026-11-25-build-TOOL-dTotalRecall-123-3-builder-return.md](../build/2026-11-25-build-TOOL-dTotalRecall-123-3-builder-return.md) | journal | — |
| [2026-11-25-build-TOOL-dTotalRecall-123-widen-35.md](../build/2026-11-25-build-TOOL-dTotalRecall-123-widen-35.md) | widen | — |
| [2026-11-26-build-TOOL-dTotalRecall-123-deviation-1021.md](../build/2026-11-26-build-TOOL-dTotalRecall-123-deviation-1021.md) | deviation | — |
| [2026-11-26-build-TOOL-dTotalRecall-123-map-replay-manifest.json](../build/2026-11-26-build-TOOL-dTotalRecall-123-map-replay-manifest.json) | research | — |
| [2026-11-26-build-TOOL-dTotalRecall-123-map-replay-verdict.md](../build/2026-11-26-build-TOOL-dTotalRecall-123-map-replay-verdict.md) | research | — |
| [2026-11-25-prompt-TOOL-dTotalRecall-123-build-2-brief.md](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-123-build-2-brief.md) | journal | — |
| [2026-11-25-prompt-TOOL-dTotalRecall-123-build-3-brief.md](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-123-build-3-brief.md) | journal | — |
| [2026-11-25-prompt-TOOL-dTotalRecall-123-build-brief.md](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-123-build-brief.md) | journal | — |
| [2026-11-25-prompt-TOOL-dTotalRecall-123-divergence-fold-brief.md](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-123-divergence-fold-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The map lost its first replay on recall at two runs per arm, where run-to-run variance swamped any map effect
(`2026-11-23-build-TOOL-dTotalRecall-17-map-replay-verdict`). On 2026-11-25 the owner answered ask TOOL-dTotalRecall-111:
"run the replay again with more runs per arm". This unit replaces the one term more runs would worsen, fixes the rule and
the run count before any run, and runs spec 17's replay a second time to a second verdict record.

## 2. Scope (IN)

The design is `TOOL-dTotalRecall-17`'s, CLOSED at rev-3 and frozen: its S2 known sets, S4 runs, S5 map, and §4 subjects and
manifest stand by reference, with the first act as `TOOL-dTotalRecall-121` S10 and `TOOL-dTotalRecall-122` S10 read it. What
follows is the difference.

- **S1** — The noise term. `tools/workflows/replay_scorer.py#measure_map_experiment` derives the figure `noise` through a new
  `measure_rise_noise(runs)`, twice the standard error of the recall rise, in place of the figure `twin`, the summed range
  of the runs. `derive_map_verdict` loses `recall` where the rise is below `noise` plus `RECALL_MARGIN` (§4 "The estimator").
  **Readers:**
  by name: `derive_map_verdict`, `measure_map_experiment` and the arm `map-verdict`, all in
  `tools/workflows/replay_scorer.py`, and the `map-replay` paragraph of `tools/workflows/README.md`, each moved in this pass
  by value: the recall comparison of `derive_map_verdict` and the `term recall` line, both moved in this pass
  Observed by AC1 and AC3.
- **S2** — The count, declared and held. The run count per audit and arm is each arm's `dispatched` over the number of
  audits, no new manifest key. The instance refuses two arms with different counts, a count the audits do not divide,
  fewer than two runs, and any audit and arm whose parsed runs are not exactly that count (§4 "The count").
  Observed by AC2.
- **S3** — The arm `map-noise` in `run_selftest`, the figure key in `map-verdict`, the docstrings, the module docstring and
  the README paragraph. Observed by AC1, AC2, AC3 and AC4.
- **S4** — The deviation record the build's fork rule asks of §8 F1's `relaxes:`, filed through `gov_record.py new deviation`
  in the pass commit (§4 "The record of the relaxation"). Observed by AC5 and AC9.
- **S5** — The manifest before the runs. The pass commit adds
  `memory/builds/dTotalRecall/build/<date>-build-TOOL-dTotalRecall-123-map-replay-manifest.json` with `known`, `arms`, an empty
  `candidates`, `map` null and each `dispatched` at §8 F2's default, 15 (DERIVED, §4's table). Until the first clone is made
  the main loop may change that count in a commit of its own. From the first clone on, only `candidates` and `map` move, the
  main loop writing them at the verdict commit. Observed by AC6 and AC10.
- **S6** — The runs, the main loop's: that count of harness calls per arm for each of the three audits, in new clones under
  the next free `<n>` (§4 "The runs"). No run of the first experiment is pooled into this one. Observed by AC6 and AC7.
- **S7** — The verdict record,
  `memory/builds/dTotalRecall/build/<date>-build-TOOL-dTotalRecall-123-map-replay-verdict.md`, opened by
  `gov_record.py new research` with `--unit TOOL-dTotalRecall-123` and the other flags and the shape of spec 17 S6, and its
  routes (§4 "The routes"). It, the filled manifest and the header's flip to `CLOSED` are the main loop's, in one verdict
  commit. Observed by AC7 and AC8.

## 3. Non-goals (OUT)

- Any edit of spec 17, of its manifest or of its verdict record, which stand as the first experiment.
- A re-score of the first experiment: its transcripts stand outside the repository, under another account's profile that
  does not resolve here. Its figures are read from its record alone, to state the spread.
- The two other terms, their figures and their boundaries, `RECALL_MARGIN`, the known sets, the scored lenses and the map.
- Retiring, re-opening or editing units 14, 15 and 26, re-homing a clause, or answering an ask: the main loop's and the
  owner's, after the verdict.
- A rule that stops early, adds runs after a figure is read, or drops a run for its figure.
- A power model in the scorer: §4's table is arithmetic over the first record, and no code reads it.

### Edges

- **consumes-from** external — the landed units 17, 121 and 122, whose instance, byte term and `map-experiment` arm this extends
- **consumes-from** external — the owner's answer naming a run count, where one comes
- **hands-off** external — the runs, the verdict record and the acts on units 14, 15 and 26, each the main loop's or the owner's

## 4. Design

Read at `fbe06249` on 2026-11-25.

### Why the twin difference cannot take more runs

It is, summed over the audits, the larger arm's largest less smallest count over its runs
(`tools/workflows/replay_scorer.py#measure_map_experiment`). A range never shrinks as runs join. Driven through
`check_experiment` over one audit of seven items, both arms alike, counts 2 and 6 read twin difference 4 and a losing line
of 9; counts 2, 6, 1 and 7 read 6 and 11 (DERIVED 2026-11-25, a probe of today's scorer). Both samples have mean 4, so the
added runs left the mean better known and the line harsher.

### The estimator

The rise is unchanged: the with-map arm's figure less the without arm's, an arm's figure being the sum over the audits of
the mean of its n runs. What it is compared with becomes:

```python
NOISE_FACTOR = 2

def measure_rise_noise(runs):
    """NOISE_FACTOR standard errors of the recall rise, `runs` one list of known items found per arm and audit."""
    return NOISE_FACTOR * math.sqrt(sum(statistics.variance(counts) / len(counts) for counts in runs))
```

`runs` is `found.values()`. Each list is one arm's counts on one audit. `variance` is the sample variance, which estimates
the spread without growing with n, and the division by n is how the mean enters. The arms and audits run independently, so
the variances of their means add. **The losing line for recall: the map loses `recall` when the rise is below `noise` plus
5**, `RECALL_MARGIN`, strictly, as today. A rise on the line wins the term.

The factor is 2 for two reasons. It is the conventional two standard errors. And over the first experiment's counts the
term reads 15.46, so its line would have been 20.46 where the twin difference read 18 and 23 (DERIVED 2026-11-25, the
function over that record's counts). A factor of 1 reads 7.73 there and would more than halve the noise the clause priced.
The first experiment's rise of -0.5 loses under either.

Over the probe's fixture the lines become `noise 5.65685 at 2 run(s) per arm · loses below 10.6569` and `noise 4.16333 at 4
run(s) per arm · loses below 9.16333`, so the same added runs lower the line (DERIVED 2026-11-25, the patched scorer in a
scratch copy). Equal counts read noise 0 and a line of 5. The `term recall` line prints that text where it printed the twin
difference, and the rest of it stands.

### The count

After `measure_parsed`, which first checks that each `dispatched` is a count its parsed runs do not exceed:

```python
sent = {a["dispatched"] for a in arms}
want, rest = divmod(min(sent), len(sets))
if len(sent) > 1 or rest or want < 2:
    raise Refusal(f"arms: dispatched {', '.join(map(str, sorted(sent)))} over {len(sets)} audit(s): both arms take one "
                  "count, the audits times one run count of at least two")
...
if n != want:
    raise Refusal(f"arm {name} case {case}: {n} parsed run(s), not the {want} the manifest declares")
```

It takes the place of the fewer-than-two refusal. So the instance gives no figure while a run is missing, which leaves no
interim reading to stop on, and none once a run too many is added. The first experiment's manifest, `dispatched` 6 over
three audits with two runs each, still satisfies it.

| Runs per arm and audit | `dispatched` per arm | Harness calls | Two standard errors | Losing line |
|---|---|---|---|---|
| 2 | 6 | 12 | 15.46 | 20.46 |
| 5 | 15 | 30 | 9.78 | 14.78 |
| 10 | 30 | 60 | 6.91 | 11.91 |
| 18 | 54 | 108 | 5.15 | 10.15 |
| 20 | 60 | 120 | 4.89 | 9.89 |

**The spread behind it.** The first record's counts are, without, 18 and 29, 3 and 8, 7 and 7, and with, 28 and 20, 10 and
5, 5 and 3. Their sample variances sum over the audits to 73 without and 46.5 with, mean 59.75, so one run's total over the
three audits has a standard deviation of 7.73, about eight items. The standard error of the rise at n runs is the square
root of 119.5 over n. Every figure of this section's table and of this paragraph is DERIVED 2026-11-25 from those counts.

A count resolves an effect when two standard errors are no larger than it: five runs resolve a rise near ten, eighteen one
near five, and twenty is the first to come under five. Resolving is not winning. The clause's 5 items stand on top, so a
true rise equal to the losing line wins the term about half the time. The sample is two runs per cell, so the spread is
rough, and the verdict uses the second experiment's own.

### The runs

Spec 17 S4 as written, with these differences. The first experiment's record lists `f1n1` to `f1n3`, `f1m1` and `f1m2`, and
`<n>` 1 and 2 for audits 2 and 3, so audit 1's without arm opens at `f1n4` and every other arm at its `<n>` 3. The placement
of audit 1's subjects, and the inputs neither arm is handed, are that record's Departures, reproduced. Spec 17 S5's map is
derived again and must hash to the first one's blob `d38a3a8f2ed8`; another blob is a stop, since it would be another map.

Within an audit the calls alternate arms, without first, so a change of model or load over the hours falls on both. Every
call runs from one orchestrating head, as the README's per-arm step says. A call that returns no report, or leaves a scored
lens with no readable transcript, is re-run in a fresh clone under the next `<n>`, at most once; a second failure stops the
experiment with no verdict. A run is never re-run for its figure. So the bound is twice the declared calls, and the
expected spend is the table's.

### The verdict rule, fixed before the first run

This section, S1's code and the manifest's `dispatched` are committed before the first clone exists, and none moves from
then until the verdict record lands. The instance is run over the complete manifest, and its last line is the verdict:

- `verdict lose <terms>` where the rise is below `noise` plus 5, or the searches' fall is below 1, or the bytes' rise is
  above the map's bytes.
- `verdict unarmed bytes` where no term lost and every lens run read zero bytes before its first act.
- `verdict win` otherwise.

### The routes

The record opens as spec 17 S6's does, with `**Verdict:** win`, `**Verdict:** lose` or `**Verdict:** unarmed` and the terms. Then
come the manifest and the orchestrating sha that held it, the run count, each clone's name, `HEAD` and status before its call, every
re-run with its cause, each term's figures, the second experiment's own variances and the map's bytes. Then, under Routing:

- **`win`** — the main loop re-opens units 14, 15 and 26, each re-grounded before its pass. The record names the three asks
  spec 17 S7 filed, TOOL-dBoundRoles-77, TOOL-dWellOiledMachine-961 and TOOL-dCalibratedLens-57, as resting on a verdict this
  one replaces; their own builds answer them. The accept clause of ask TOOL-dTotalRecall-111 is met by the record.
- **`lose`** — units 14, 15 and 26 are to be retired as `WONTDO`, and their clauses cl-dClosedLoop-0225, -0226 and -0237
  re-homed, as the accept clause of ask TOOL-dTotalRecall-111 says. No run does either by itself: the units stay `DEFERRED`
  and the ask open until the owner's turn. The three asks stand, and nothing is filed again.
- **`unarmed`** — no verdict either way. The units stay `DEFERRED`, the ask open, and the record says which lens runs were
  read.

### The record of the relaxation

`gov_record.py new deviation --build dTotalRecall --unit TOOL-dTotalRecall-123`, its name and number the door's, one `--field` each:

| Field | Value |
|---|---|
| Departs from | `TOOL-dTotalRecall-17@rev-3` [§4 "The terms"] |
| Hand-off | design-to-spec |
| Before | the recall term's noise is the twin runs' difference, each arm run twice |
| After | it is two standard errors of the rise, each arm run the count the manifest declares |
| Cause | owner ruling |
| Reason | the owner ordered more runs per arm on 2026-11-25, and a range grows with the runs |
| Evidence | §4's probes, and `2026-11-25-prompt-TOOL-dTotalRecall-17-replay-rerun-brief`, which quotes the ruling |
| Risk | loosening |
| Approver | spec writer, resolving §8 F1 under the run's standing mandate |
| Follow-through | ask TOOL-dTotalRecall-111 |
| Caused-by | `TOOL-dTotalRecall-111` |
| Bound | the twin runs' difference as the recall term's noise |
| Tier | strongest, a bound the carried clause states in its text |

What it relaxes: at the first experiment's spread the line is 20.46 where the clause's was 23 at two runs, and lower again
as runs join. What it does not: the 5 items, the strict comparison, and the other two terms.

The as-built view keeps the baseline text of cl-dClosedLoop-0228. Its words "the twin runs' difference" are therefore departed
from under this record and not amended: `tools/memory-tree/asbuilt_view.py#resolve_clause_rows` refuses a record departing from
a clause with no amends or supersedes row, and an amends row would leave the `Carries:` hash of frozen spec 17 stale. Amending
the clause is the owner's, and the main loop names it to them at the close.

### Inventory

Minted: `measure_rise_noise` and `NOISE_FACTOR` in `tools/workflows/replay_scorer.py`, the figure key `noise`, the arm
`map-noise` and the local builder it shares. The lexicon admits the function for cell `py.function` (DERIVED 2026-11-25, its
`--suggest`).

### The arm

`map-noise` drives `check_experiment` over one audit of seven items (PINNED, the arm), both arms alike, at counts 2 and 6, then
2, 6, 1 and 7. It asserts the two whole `term recall` lines, so a term wired to another figure reds as a wrong term does.
Then it drops one run of the second set and expects a refusal naming 3 and 4, and declares two counts and expects one
naming both. Its report and manifest builder is the one `map-experiment` holds, lifted out of `check_map_experiment_arm` at
its second caller. It skips as `map-experiment` does where no runlog kit resolves. The planted sets of `map-verdict` carry
`noise` for `twin`, values unchanged, and gain one whose noise alone loses.

### Migration

None: no committed manifest is re-scored, and the first one still parses. Reverting the commit restores the old term.

### Rollout

The pass lands S1 to S5 in one commit: the scorer, its arms, the deviation record and the manifest, `candidates` empty. Its
header STAYS `INPROGRESS` there, and its ledger answers AC1 to AC5 and AC10, with AC6 to AC8 owed to the main loop and AC9 to
the close. The main loop then makes S6's runs and S7's verdict commit, which answers AC6 to AC8 in the ledger and flips the
header to `CLOSED`, as TOOL-dTotalRecall-17 stayed `INPROGRESS` at `30c21c834` and closed at `cb97caf03`.

### Files touched (estimate)

- `tools/workflows/replay_scorer.py`
- `tools/workflows/README.md`
- `memory/map/generated/`
- `memory/LIVE.md` and `memory/builds/dTotalRecall/README.md`, rendered by the build index
- `memory/builds/dTotalRecall/build/` (the deviation record, the ledger, the manifest and the verdict record)
- `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md`, the as-built view, whose head counts the records

### Alternatives rejected

- **The larger of the noise and 5 as the line.** It reads 9.78 at five runs and drops the clause's "plus 5 items", a second
  relaxation.
- **The range divided by its expected growth.** It needs a constant per count and is a noisier estimate than the variance.
- **Student's t in place of 2.** It needs a degrees-of-freedom rule over six cells of unequal variance.
- **A new manifest key for the count.** `dispatched` already states it, and two places could disagree.
- **Both estimators kept, chosen by the count.** A verdict with two rules to pick from is not fixed before its run.

## 5. Production-readiness checklist

- security — no new write path in product code; the runs write under `%TEMP%` clones and this build's records.
- perf / scale — the table's calls; the new arm is in-memory fixtures inside the `review-replay selftest` ceiling of
  300 s (PINNED 2026-11-23, spec 17 §5).
- error / empty / loading states — a missing, extra or unequal run count refuses, naming the arm and the case.
- observability — the recall line prints the noise and the count; the record carries the variances.
- risks — at five runs a true rise of ten loses more often than it wins, the line being 14.78 at the first spread. That spread
  is an estimate from two runs per cell. The harness may have moved since the first experiment, which is one more reason
  none of its runs is pooled.
- testing — AC1 to AC5 and AC10 by the pass; AC6 to AC8 by the main loop at the verdict commit; AC9 and §7's arms at the
  close.
- migration — none.
- user docs — `tools/workflows/README.md`; no page under `help/` states the replay.

## 6. Acceptance criteria

- **AC1** — When a probe calls `check_experiment` over §4's seven-item fixture at counts 2 and 6, then 2, 6, 1 and 7, the two
  `term recall` lines end `noise 5.65685 at 2 run(s) per arm · loses below 10.6569` and
  `noise 4.16333 at 4 run(s) per arm · loses below 9.16333`.
  Red when: the line rises with the runs, as today's 9 and 11 do, or a variance is not divided by its count.
  figure: PINNED here, DERIVED 2026-11-25 by the probe §4 names.
- **AC2** — When the probe drops one run of four, declares two counts, declares over two audits a count they do not divide,
  or declares one run, each `check_experiment` call raises `Refusal` naming the counts; over the complete set it returns lines.
  Red when: a partial or extended set is scored. Today a set of three runs against four is.
- **AC3** — When `derive_map_verdict` reads the boundary set with `noise` 0 and a rise of 5, it returns `win`; with a rise of 4,
  `lose` on `recall` alone; with `noise` 1 and a rise of 5, `lose` on `recall` alone. `measure_rise_noise` over the first record's
  six pairs returns 15.46 to two places.
  Red when: the noise does not enter the line, or the margin does not.
  figure: PINNED here, DERIVED 2026-11-25 from that record's counts.
- **AC4** — When `grep -nE "twin difference|twin runs'|\"twin\"" tools/workflows/replay_scorer.py tools/workflows/README.md` runs,
  it prints nothing, and the README's `map-replay` paragraph names the noise, its factor and the count rule.
  Red when: a docstring or the README states the old line. The `review-twin runs=` line of `tier2-review.js`'s twin runs is
  no hit.
- **AC5** — When a probe calls `deviation_join.py#read_record` over the new deviation record, its `malformed` is empty, its
  `address` is `TOOL-dTotalRecall-17@rev-3`, its `follow` is `ask TOOL-dTotalRecall-111`, and its `bound` is §8 F1's `relaxes:` value; and `grep -rlE "^- \*\*Bound:\*\* the twin runs' difference as the recall term's noise$"
  memory/builds/dTotalRecall/build/` names that one file.
  Red when: a field is refused, or no record or two carry the bound.
- **AC6** — When the manifest is read at the one orchestrating sha every `run.log` line names, its `candidates` is empty and
  both `dispatched` are three times one count of at least two; and `dispatched` at the verdict commit is the same.
  Red when: the count is written or moved after the first clone.
  permission: the main loop's.
- **AC7** — When `python tools/workflows/replay_scorer.py --experiment <manifest>` runs over the complete manifest, it exits 0.
  The verdict record quotes its lines, opens its verdict with `**Verdict:**`, and lists one clone per declared call with an empty
  status. A script joining the two manifests finds no `report` and no transcript path in both.
  Red when: a clone is reused or dirty, a run of the first experiment is pooled, or a call is re-run for its figure.
  cost: 30 harness calls at five runs and 108 at eighteen (DERIVED, §4's table), hours to days and their token spend.
  permission: the main loop's.
  fixture: the three audits' commits and blobs, as spec 17 AC4 states.
- **AC8** — When the verdict record is read, its Routing holds the one branch of §4 its verdict names; and a `git log` over the
  specs of units 14, 15 and 26 from the manifest's commit to the verdict commit lists none.
  Red when: a run retires or re-opens a unit by itself, or files spec 17's three asks again.
  permission: the main loop's.
- **AC9** — When `python memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py --report dTotalRecall`
  runs on the prepared merge, as the build README's close rule has it, the entry of §8 F1's mark reads `relaxes [the twin runs'
  difference as the recall term's noise] joins` and the new record's stem.
  Red when: the `relaxes:` mark joins nobody.
  cost: past ten minutes on node a, where the instrument's `--policy report` did not return within 600 s (DERIVED 2026-11-25,
  `2026-11-25-build-TOOL-dTotalRecall-123-1-builder-return`).
  permission: the close's.
- **AC10** — When the pass commit's manifest is read, `candidates` is empty, `map` is null and both `dispatched` are 15; and
  `python tools/workflows/replay_scorer.py --experiment <manifest>` exits 2 naming `map None: not a source of a non-empty map`.
  Red when: the manifest is absent from the pass commit, or it can be scored before a run.
  figure: PINNED here, DERIVED §4's table at five runs per arm.

## 7. Gates

`review-replay selftest` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `recall floor` · `recall floor arms` · `memory hygiene` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `python reads (a name never bound, an import outside its guard)` · `python resolver (behaviour + inline parity + idiom ban)` · `ratchet (never gains)` · `ratchet (both ways)` · `chain-packet self-test` · `policy fixtures`

New arm: tools/workflows/replay_scorer.py · covers AC1 AC2 · `map-noise`, staged by the range put back in `measure_rise_noise`, by its division by the count cut, and by the exact-count refusal cut · `ARMS_DECLARED` raised from 33 (PINNED 2026-11-25, `tools/workflows/replay_scorer.py#ARMS_DECLARED`) by the one arm
New arm: tools/workflows/replay_scorer.py · covers AC3 · `map-verdict` moved to the figure `noise`, with a set whose noise alone loses, staged by the comparison reading the margin alone · none

What the arms do not check: that the runs were independent, that the manifest was committed before them, which AC6 reads,
and that a run was not re-run for its figure, which the record's re-run list states and nothing joins.

## 8. Open questions

- **F1 — Which noise term replaces the twin difference, and does the 5 stay?** Options: (a) the twin difference kept, which
  rises with the runs the owner ordered; (b) two standard errors of the rise, plus the clause's 5; (c) the larger of two
  standard errors and 5; (d) one standard error plus 5. (a) defeats the ruling. (c) drops the clause's margin, and (d) more
  than halves its noise at two runs. (b) is rung 1: the clause's own shape, a noise plus 5 items, read for any count, under the
  owner's words in `2026-11-25-prompt-TOOL-dTotalRecall-17-replay-rerun-brief`.
  RESOLVED (agent, 2026-11-25, delegated): (b). widens: none · relaxes: the twin runs' difference as the recall term's noise
- **F2 — How many runs per arm?** The owner's words name no number. Options: (a) five, resolving a rise near ten in 30 calls (DERIVED 2026-11-25, §4's table);
  (b) eighteen, near five in 108; (c) a count picked after a figure is read, which the fixed rule refuses. The brief has the
  main loop take the owner's answer, or five where none came before the first clone. `dispatched` holds either, so no line of
  the code moves with it.
  RESOLVED (agent, 2026-11-25, delegated): (a) unless the owner names another count before that clone. widens: none · relaxes: none
- **F3 — Which binding line does this unit carry?** Options: (a) `**Derived:**` naming `PLAY-dClosedLoop-2`, as `TOOL-dTotalRecall-122`
  §8 F1; (b) a part of cl-dClosedLoop-0228, which unit 17 carries whole. (b) fails the carries join.
  RESOLVED (agent, 2026-11-25, delegated): (a), the one survivor. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-25 · initial draft, from `2026-11-25-prompt-TOOL-dTotalRecall-17-replay-rerun-brief`, spec 17 at rev-3, its
  verdict record and the scorer read at `fbe06249`.
- rev-2 · 2026-11-25 · S4 S5 S7 · §4 · §5 · AC4 AC5 AC6 AC9 AC10 · §8 · per `2026-11-25-prompt-TOOL-dTotalRecall-123-divergence-fold-brief`,
  re-read at `b4d582a2d`: AC4's grep leaves the twin-run line alone, AC5 reads the build records by `read_record`, the departures
  join is AC9 at the close, the manifest with `map` null joins the pass commit under AC10, and the header stays `INPROGRESS`
  until the verdict commit. No estimator, line or count moved.
- rev-3 · 2026-11-26 · §4 · AC5 · §7 · per `2026-11-25-build-TOOL-dTotalRecall-123-2-builder-return`: the deviation record departs from spec 17.

## 10. Reuse audit

The seam extended is the `map-replay` row of `tools/workflows/replay_scorer.py#INSTANCES`: `measure_map_experiment` and
`derive_map_verdict`, dispatched by `check_experiment`, with the factory's `dispatched` as the count and the builder of
`map-experiment` as the new arm's. `statistics` is already imported there. `python tools/codebase-map/reuse_lookup.py "standard
error of a difference of two means over replay runs"`, run 2026-11-25, ranked name-stem neighbours alone, of `run` and `err`, and a grep
of the Python under `tools/` for `statistics.variance`, `stdev` and `pstdev` finds no caller, so no existing seam fits the
spread.

Recall terms used: `python tools/memory-recall/query.py "map replay verdict twin difference noise term runs per arm" --terms "map-replay replay_scorer twin difference losing line runs per arm derive_map_verdict recall margin verdict record relaxes deviation Bound"`
