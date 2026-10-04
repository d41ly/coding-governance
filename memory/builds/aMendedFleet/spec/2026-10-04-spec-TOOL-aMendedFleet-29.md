# TOOL-aMendedFleet-29 — a recall gold set harvested from spec §10 probes, de-contaminated, graded at hit@10

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-2 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 29

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Every recall figure this repo has published rests on a hand-written question set of 12 to 16, whose
strong terms were written after reading the targets. The committed specs already hold a larger,
independently authored set: each §10 Reuse audit records a real `query.py` question and its terms,
and the rest of the same spec cites the foreign records the author went on to rely on. This unit
harvests that set from the tree, removes the labels the probe itself supplied, and reports how
often the served path puts a label in its top 10. It is a REPORT: it sets no floor, because no
person has checked its labels.

## 2. Scope (IN)

- **S1** — `read_spec_probes(root)` walks the tracked spec files under the memory root's
  `builds/*/spec/`, at any depth, takes the body of the section headed `## 10. Reuse audit`,
  flattens hard wraps, and extracts each `query.py` invocation's question and `--terms` value. The
  question's closing quote must MATCH its opening one, so an apostrophe inside a double-quoted
  question does not truncate it. A probe with no `--terms` takes them from a `Recall terms used:`
  line in the same section; a probe with neither is set aside and counted, since the CLI refuses a
  question without terms. Observed by AC1 and AC4.
- **S2** — `derive_probe_labels(spec, probe)` labels a question with every id in the conf's id
  grammar, `extract.ID_RE`, that the same spec cites OUTSIDE §10 and whose slug is not the spec's own
  build slug. Observed by AC1 and AC2.
- **S3** — de-contamination: every id the spec's §10 itself cites is excluded from that question's
  labels, because §10 is where the author recorded what the probe returned, and grading the probe on
  what it returned is circular. An id no record in the served `records` set anchors is excluded and
  counted as unresolved. A question left with no label is set aside and counted. Observed by AC2.
- **S4** — `check-recall.py --spec-probes` grades each surviving question through unit 28's
  `measure_served` at `k` 10, `SPEC_PROBE_K`, and prints one row per question, then one summary line:
  probes found, the count set aside for each reason, `n` graded, and hit@10 with `n` beside it. It
  exits 0 whenever at least one question was graded. Observed by AC1 and AC4.
- **S5** — liveness: when the harvest finds no probe, or no question survives de-contamination,
  `--spec-probes` prints `DEAD PROBE` naming which stage emptied the set and exits 1. A report of
  hit@10 over nothing must not read as a clean zero. Observed by AC3.
- **S6** — the run records the result as a journal under this build's `build/` folder: the
  reproducing command, the summary line, and an agent spot-check of 20 questions' labels, each with a
  keep or reject verdict and its reason. The full human label check is parked in the run-state file
  as an owner act, per §8 F2. Observed by AC5.
- **S7** — the `--spec-probes` help text and the docstring of `check-recall.py` state what the report
  cannot see: a probe return the author never wrote into §10 survives as a label, the corpus graded
  is today's and includes records written after the probe, and only ids in the four declared
  families are labels. Observed by AC6.

## 3. Non-goals (OUT)

- A floor or pin over this set. The report names hit@10 only; a pin needs labels a person checked.
- Committing the harvested set. It is derived live from tracked specs on every run, so there is
  nothing to keep fresh.
- Harvesting `reuse_lookup.py` probes. Node d's dTracedLattice build committed a harvester for those,
  labelled by files touched, which is a different label source.
- Joining the machine-local query log to recover what each probe actually showed. The log is not in
  the tree and covers only the machine that ran it; the residue is stated by S7.
- Measuring answer-used from later commits, which is unit 34.

### Edges

- **consumes-from** `TOOL-aMendedFleet-28` — `build_served_dir` and `measure_served`; without them
  this report would rank through `bench` and grade a path no session is served.
- **hands-off** external — the owner's hand-check of the harvested labels, and any floor pinned
  after it.

## 4. Design

### Evidence

Measured 2026-10-04 at the worktree tip `580dc980`, with a probe written for this spec; PINNED.

| Figure | Value |
|---|---:|
| tracked spec files | 901 |
| specs with a §10 | 854 |
| §10s holding a double-quoted `query.py` question | 123 |
| of those, carrying `--terms` inline | 116 |
| foreign ids cited in those specs | 455 |
| of which cited in §10 | 166 |
| of which cited ONLY in §10 | 81 |
| questions left with at least one label after de-contamination | 77 |
| questions left with none | 46 |

The report counted 111 probes and 458, 164 and 78 ids at `ac65de998`; the tree has grown and the
proportions hold. 123 is a floor: the probe matched double quotes only, and 99 of the 123 questions
wrap across a line break, which S1's flattening handles.

- `memory/builds/dMispairedQuote/spec/2026-09-01-spec-TOOL-dMispairedQuote-1.md` cites one foreign id
  in both its design and its §10, and two others only in its design: the de-contamination case.
- `memory/builds/dTieredTribunal/spec/2026-08-26-spec-dTieredTribunal-13.md` asks a question that
  wraps and carries an apostrophe: the matched-delimiter case.
- Node d's `2026-09-05-build-TOOL-dTracedLattice-1-harvest.py` documents the apostrophe truncation
  that a character-class closing quote causes, and matches the closing delimiter to the opening one.
  It is committed evidence, not an importable module, so the rule is reused and the code is not.

### Inventory

- `read_spec_probes`, `derive_probe_labels`, `print_spec_probes` and `SPEC_PROBE_K = 10` in
  `check-recall.py`. The lexicon's `--suggest` answered the first two OK for cell `py.function` and
  steered `report_spec_probes` to `print_spec_probes`. A name the lexicon leg refuses at build time
  is replaced with its `--suggest` answer and this list amended.

### Files touched (estimate)

- `tools/memory-recall/check-recall.py`
- `tools/memory-recall/test_recall_floor.py`
- `tools/memory-recall/README.md`

The journal S6 writes sits under this build's `build/` folder. The kit version bump owed by the
README edit is taken once at this build's close.

### Alternatives rejected

- **A new `harvest` script beside the kit.** `check-recall.py` is already `project-owned` and already
  holds the served scorer after unit 28; a second file needs a second `kit.toml` claim.
- **A mode on `bench.py`.** Its flag set is closed and `verbatim.json` pins it byte for byte.
- **Labels from every record of the build, not the one spec.** Measured per build, the label set
  swells with backlog and review citations unrelated to the question.

## 5. Production-readiness checklist

- security — N/A — reads tracked files, writes a scratch dir it removes.
- perf / scale — one served-cache build plus about 80 fused queries; seconds.
- error / empty / loading states — S5's DEAD PROBE for an empty harvest; every drop is counted by
  reason, never silent.
- observability — the summary line carries `n` beside hit@10 and every drop count.
- risks — label noise: a cited id is evidence the author relied on it, not proof it answers the
  question. The spot-check prices it and the owner's check is parked.
- testing — arms in `test_recall_floor.py` for the DEAD PROBE branch and the matched-delimiter parse.
- migration — N/A — no stored data.
- user docs — the kit README's floor section gains the `--spec-probes` line.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-recall/check-recall.py --spec-probes` runs on the tree, it
  prints one row per graded question and a summary line carrying probes found, a count per drop
  reason, `n` and hit@10, and exits 0.
  Red when: the summary line is missing, `n` is absent beside hit@10, or the exit is non-zero.
  figure: every count DERIVED at observation time.
- **AC2** — When `python tools/memory-recall/check-recall.py --spec-probes` runs, the row for
  `memory/builds/dMispairedQuote/spec/2026-09-01-spec-TOOL-dMispairedQuote-1.md` lists the two ids
  that file cites only outside its §10, and not the id its §10 also cites.
  Red when: the §10-cited id appears as a label.
- **AC3** — When, in a throwaway clone with every §10 `query.py` line deleted from the specs,
  `python tools/memory-recall/check-recall.py --spec-probes` runs, it prints `DEAD PROBE` naming the
  harvest stage and exits 1.
  Red when: it exits 0 or prints a hit@10 over nothing.
  fixture: a `git clone --local` under a short `%TEMP%` root; the tree holds none today.
- **AC4** — When `python tools/memory-recall/check-recall.py --spec-probes` runs, the row for
  `memory/builds/dTieredTribunal/spec/2026-08-26-spec-dTieredTribunal-13.md` carries its question
  whole, through the word after the apostrophe.
  Red when: the question is cut at the apostrophe or at the line break.
- **AC5** — When `git grep -n "hit@10" -- memory/builds/aMendedFleet` runs after the pass, it hits
  a journal carrying the summary line, the reproducing command and 20 spot-check verdicts.
  Red when: no journal carries the figure, or the spot-check is absent.
- **AC6** — When `python tools/memory-recall/check-recall.py --help` runs, the `--spec-probes` line
  says the report sets no floor and names the three blind spots S7 lists.
  Red when: the help text omits them.

## 7. Gates

`recall floor` · `recall floor arms` · `memory-recall kit selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `kit version markers`

New arm: tools/memory-recall/test_recall_floor.py · a fixture root with no §10 probe, and a probe whose question carries an apostrophe across a wrap · none

`recall floor arms` and `memory-recall kit selftest` are held self-test legs; the close runs them.

## 8. Open questions

- **F1 — What counts as a "later-cited" label?**
  Options: ids the same spec cites outside §10; ids any record of the build cites; or ids the
  build's commits cite after the spec's commit. The report's 458, 164 and 78 reproduce under the
  first, measured at 455, 166 and 81. The second swells with backlog and review citations. The third
  needs a history walk for an ordering the spec body already approximates.
  RESOLVED (agent, 2026-10-04, delegated): the same spec outside §10, S2.
- **F2 — Who hand-checks the labels?**
  Options: the owner checks every label before any figure is reported; the run's agent spot-checks a
  declared sample and the owner's full check is parked; no check. The first is an owner act no run
  can take, and the mandate parks those. The third reports noise as a measurement.
  RESOLVED (agent, 2026-10-04, delegated): a 20-question agent spot-check, the full check parked, S6.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from a measured harvest of the tracked spec set.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "harvest questions and expected ids from committed spec
reuse audit sections"` returned `expected_by_target` in `tools/memory-recall/bench.py`, which unit
28's `measure_served` already routes through, and `parse_spec_h1` in `tools/memory-tree/tree_lib.py`,
which parses a spec's title line and not its sections. No candidate harvests §10 probes, so no
existing seam fits; the seam extended is `check-recall.py`, after unit 28. Recall returned the floor
asks `TOOL-aWeighedCompass-16` and `TOOL-aProbedToolkit-10`, and node d's dTracedLattice measurement
records, whose harvester for `reuse_lookup.py` probes supplied the matched-delimiter rule in §4.
Where the report and the tree disagree: 111 probes then, 123 now.

Recall terms used: `python tools/memory-recall/query.py "is there a gold question set harvested
from spec section 10 recall probes labelled by cited ids" --terms "gold set spec section 10 recall
probe harvest labels cited ids contamination hit@10 fixture bench query log"`
