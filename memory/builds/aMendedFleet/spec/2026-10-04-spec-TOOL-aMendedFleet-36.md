# TOOL-aMendedFleet-36 — `reuse_lookup.py` prints within a byte budget and names what it cut

**Status:** CLOSED · rev-1 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · closes TOOL-aProbedToolkit-9 · order 36

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The reuse probe prints every candidate it ranks: over the 360 replayed phrases its answer runs from
8 KB to 96 KB, median 25 KB, and its reader is a model with a context window. Its sibling
`query.py` already bounds output by bytes. This unit gives `reuse_lookup.py` a `--budget` in bytes,
always shows the first candidate, ends with one line saying how many it cut and that `--budget 0`
shows them all, and sets the default by measuring hit@budget with `replay-phrases.py`, which gains
the same flag. A plain top-30 cut was measured and rejected: it drops the hit rate from 0.672 to
0.540.

## 2. Scope (IN)

- **S1** — `derive_budget_cut(shortlist, corpus, budget)` in `tools/codebase-map/reuse_lookup.py`
  returns the candidates to show and the count cut. It walks the ranked candidates in order, costing
  each as its printed `_line` plus the source lines it adds that no earlier candidate added, and
  stops before the first candidate that would take the header, candidate and sources blocks past
  `budget`. The first candidate is always shown, so a tight budget never reads as "no seam fits".
  `budget` 0 shows everything. Observed by AC1, AC2.
- **S2** — `render` prints only the shown candidates and their sources, then, when any were cut,
  one ASCII line: `cut <n> of <m> candidate(s) past the <budget>-byte budget - rerun with --budget 0 to see them all`.
  The partial-recall paragraph and the `Decision:` line are printed after it at every budget,
  outside the bound, because they are the liveness facts and the remedy. Observed by AC1, AC2.
- **S3** — `main` takes `--budget <bytes>`, a non-negative integer defaulting to `DEFAULT_BUDGET`; a
  negative or non-integer value exits 2 through argparse. Observed by AC2.
- **S4** — `DEFAULT_BUDGET` is the smallest value on the ladder 4096, 8192, 12288, 16384, 24576,
  32768 whose hit@budget over the replay corpus is at least 0.97 of the unbounded hit rate, measured
  at this pass after unit 35 has landed. The constant's comment records the measurement: the date,
  the hit rate and the hit@budget at the chosen value and at the one below it. Observed by AC3.
- **S5** — `tools/codebase-map/replay-phrases.py` takes `--budget <bytes>`, defaulting to
  `rl.DEFAULT_BUDGET`, and reports hit@budget: a phrase hits when its first correct candidate is
  among those `derive_budget_cut` shows. It calls that function and never re-derives the cut. The
  text summary gains one line and the JSON summary the keys `budget` and `hit_at_budget`.
  Observed by AC3.
- **S6** — The lookup log row's `shown_paths` and `n_sources` are derived from the SHOWN candidates,
  and the row gains `n_cut`. `n_shown` keeps its documented meaning, the ranked count, so an old row
  and a new one never disagree on what a field counts. Observed by AC4.
- **S7** — The `reuse_lookup.py` row of `tools/codebase-map/README.md` names the budget, the cut
  line and `--budget 0`. Observed by AC5.

## 3. Non-goals (OUT)

- Changing the ranking, the seeds or `NEIGHBOUR_CAP`. The budget cuts the ranked list's tail.
- A budget on `map_diff.py` or any other map CLI.
- A floor or gate on hit@budget. `replay-phrases.py` stays off the bar by owner ruling, and unit 41
  owns its `--floor`.
- Sharing code with `query.py`'s `emit`. It sits in another kit, which this kit may not import;
  the rule is copied, not the function.

### Edges

- **consumes-from** `TOOL-aMendedFleet-35` — the shell layer grows the corpus and the output, so the
  default is measured after it lands; measured before, it would be fitted to a corpus that no longer
  exists.

## 4. Design

### Evidence

Read at base `7af5f564`, whose bytes for every file below equal HEAD's at `580dc980e`.

- `render` in `tools/codebase-map/reuse_lookup.py` prints a six-line header, every ranked
  candidate, every source, then the partial-recall paragraph and the decision line, and cuts
  nothing. `write_lookup` records `n_shown` as the ranked count and `shown_paths` from every ranked
  candidate.
- `emit` in `tools/memory-recall/query.py` is the shape copied: render in rank order until the next
  item would pass the budget, show the first item even alone, and say what was cut.
- A scratch probe rendering the shortlist for every graded replay phrase, PINNED 2026-10-04 on node
  a, measuring the byte offset of the end of the first correct candidate's line within the header
  and candidate blocks, against an unbounded hit rate of 0.689 over 360 phrases:

| budget (bytes) | hit@budget | share of unbounded | answers over the budget |
|---:|---:|---:|---:|
| 4096 | 0.533 | 0.77 | 360 |
| 8192 | 0.614 | 0.89 | 360 |
| 12288 | 0.661 | 0.96 | 340 |
| 16384 | 0.675 | 0.98 | 310 |
| 24576 | 0.681 | 0.99 | 190 |
| 32768 | 0.686 | 1.00 | 122 |

  The probe left the sources block out of the cost, which S1 includes, so a real hit@budget reads
  lower at each value; by S4's rule this reading picks 16384. The value is re-derived at the pass.

### Mechanism

`derive_budget_cut` reuses `_line` and `_scan_sources`, so the cost it charges is the bytes `render`
prints; `render` and `write_lookup` both read the shortlist it returns, so the reader and the log
see one cut. The header's bytes are charged first, from the same lines `render` builds.

### Inventory

- `derive_budget_cut` — cell `py.function`; `python tools/lexicon/lexicon.py --suggest derive_budget_cut --as py.function` answered OK.
- `DEFAULT_BUDGET` — a module constant of `reuse_lookup.py`.
- `--budget` on both CLIs, and `n_cut`, a new key of the lookup log row.

### Rollout

Unit 35 lands first. Unit 38 later edits the same README and the agent instruction beside it, at
other rows, and unit 41 later edits `replay-phrases.py`. The codebase-map kit version moves once,
at the build's close.

### Files touched (estimate)

- `tools/codebase-map/reuse_lookup.py`
- `tools/codebase-map/replay-phrases.py`
- `tools/codebase-map/selftest.py`
- `tools/codebase-map/README.md`

### Alternatives rejected

- **A top-N candidate cap.** The review measured top-30 at 0.540 against 0.672; candidates differ
  in size by their definer lists, so a count bounds bytes no better than it bounds recall.
- **Cutting the sources block only.** It is the smaller block; the candidates are what grows.
- **Matching `query.py`'s 20,000.** That figure was measured on a different output; S4 measures
  this one.

## 5. Production-readiness checklist

- security — N/A: the output of a local read-only CLI gets shorter.
- perf / scale — one pass over the ranked list, summing lengths `render` computes anyway.
- error / empty / loading states — an empty shortlist prints "no seam fits" as today and no cut
  line; a budget smaller than the header still shows the first candidate.
- observability — the cut line names the count and the remedy on every cut answer; `n_cut` puts it
  in the log.
- risks — a reader that never reruns misses a seam ranked past the cut; S4's rule bounds that loss
  at 3% of the measured hits.
- testing — a fixture arm in the kit selftest, declared in §7, and AC1 to AC5 run directly.
- migration — N/A: old log rows lack `n_cut`, which reads as unknown.
- user docs — S7.

## 6. Acceptance criteria

- **AC1** — When `python tools/codebase-map/reuse_lookup.py "read the build record and derive the status of every unit"`
  runs, its stdout carries one `cut <n> of <m>` line, and the bytes printed before that line are at
  most the default budget; with `--budget 0` the same query prints `n` more candidate lines and no
  cut line.
  Red when: no line is cut, or the two runs disagree on `n`.
  figure: at base this query printed 82,941 bytes, PINNED 2026-10-04, past every ladder value.
- **AC2** — When `python tools/codebase-map/reuse_lookup.py "read the build record and derive the status of every unit" --budget 1`
  runs, it prints exactly one candidate line, a cut line naming the rest, and ends with the
  `Decision:` line; `--budget -1` exits 2.
  Red when: it prints no candidate, or drops the trailer.
- **AC3** — When `python tools/codebase-map/replay-phrases.py --budget 0` runs, its hit@budget equals
  its hit rate; at the shipped default, hit@budget is at least 0.97 of the hit rate; at the ladder
  value below the default, it is under 0.97.
  Red when: the default is not the smallest ladder value meeting the rule, or `--budget 0` differs
  from the unbounded rate.
  figure: DERIVED at the pass; §4's probe read 16384 at 0.675 of 0.689.
- **AC4** — When one lookup that cuts runs and the last row of the lookups log under the common git
  dir is read with `python -c`, it carries `n_cut` equal to the printed count, and `n_sources`
  equals the number of distinct source paths of the shown candidates.
  Red when: `n_cut` is absent, or `shown_paths` includes a path only a cut candidate carries.
- **AC5** — When `grep -n -- "--budget 0" tools/codebase-map/README.md` runs, it hits the
  `reuse_lookup.py` row.
  Red when: the README is unchanged.

## 7. Gates

`codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: tools/codebase-map/selftest.py · a fixture shortlist whose candidates pass a small budget, asserting the shown count, the cut line and the first-candidate rule, staged red by removing the first-candidate exception · none

## 8. Open questions

- **F1 — What does the budget bound?**
  Options: the candidate block alone; the header, candidate and sources blocks; the whole output.
  The trailer is the partial-recall warning and the decision prompt, and cutting either is the
  confident-answer-from-a-partial-read failure the probe's banner exists to prevent.
  RESOLVED (agent, 2026-10-04, delegated): header, candidates and sources; the trailer is outside.
- **F2 — How is the default chosen?**
  Options: copy `query.py`'s 20,000; pick from today's probe; derive it at the pass by a stated
  rule over the replay corpus after unit 35 lands. The third is what the review asked for and the
  only one fitted to the corpus the default will serve.
  RESOLVED (agent, 2026-10-04, delegated): the S4 rule, measured at the pass.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the synthesis's item [#40], `render` and `write_lookup`,
  and a byte-offset probe over the replay corpus at base.

## 10. Reuse audit

The seams extended are `render`, `_line`, `_scan_sources` and `write_lookup` in
`tools/codebase-map/reuse_lookup.py`, and `measure_phrase` in `tools/codebase-map/replay-phrases.py`;
the cut copies the rule of `emit` in `tools/memory-recall/query.py`, which sits in another kit and
cannot be imported. `python tools/codebase-map/reuse_lookup.py "bound printed output to a byte
budget and say how many were cut"` returned name-stem neighbours, `boundedParallel` and
`derive_window_bounds` among them, none of which bounds printed bytes, so no in-kit seam fits; the
probe printed `unscanned layers: .sh`. Recall returned `TOOL-aProbedToolkit-9`, the ask this
closes, which itself points at `query.py`'s budget, and `TOOL-aWeighedCompass-7`, which measured
10,782 B of mean output at precision 0.056.

Where the report and the tree disagree: the report's 9 to 49 KB range and its 0.672 hit rate were
read over 335 phrases; at base the replay corpus is 360 phrases, 8 to 96 KB, and 0.689.

Recall terms used: `python tools/memory-recall/query.py "how should reuse_lookup bound its output
size" --terms "reuse_lookup output budget bytes shortlist emit overflow replay-phrases hit@5
NEIGHBOUR_CAP top-30 cap context"`
