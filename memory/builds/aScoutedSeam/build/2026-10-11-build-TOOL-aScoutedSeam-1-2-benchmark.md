**Serves:** research TOOL-aScoutedSeam-1 TOOL-aScoutedSeam-3

# The reuse benchmark — which scout finds the seam a build should have reused, and at what cost

Run 2026-10-11 on node `a`, owner opt-in to real Workflow runs; the owner waived the five-agent
concurrency cap for this benchmark. Every figure below is re-derived from two committed files by the
committed grader, except the cost table, whose transcripts are machine-local (stated there).

```bash
B=memory/builds/aScoutedSeam/build/2026-10-11-build-TOOL-aScoutedSeam-1
python $B-4-bench.py grade   $B-3-cases.json $B-5-results.json m1b
python $B-4-bench.py compare $B-3-cases.json $B-5-results.json m1 m1b
python $B-4-bench.py misses  $B-3-cases.json $B-5-results.json m1 m1b
```

## The corpus

Thirty cases from the failure analysis (`-1-1-failure-analysis.md`), each a real request with the
seams its build should have reused, verified present at the case's point:

| repo | positive | control |
|---|---|---|
| gov | 12 | 2 |
| NicoCares | 7 | 2 |
| inCMS | 5 | 2 |

A control is a request where the tempting seam was WRONG (a visitor upload offered the admin picker)
or where new work was legitimately needed; two controls carry decoys. Nine prompts are reconstructed
from build records because the owner's words were not recoverable, and say so in the corpus.

**Blinding.** Each case runs in a single-branch clone at its POINT, so no later commit is reachable.
The point is the build's kickoff (the parent of the commit that opened its folder) when every
ground-truth seam already existed there, which holds for 10 positives. For the other 13 the point is
the parent of the reinventing commit, with the build's own folder removed in one blinding commit; one
case is as-given. A NicoCares case also gets the inCMS core tree as of the same moment.

**Grading.** A ground-truth item is HIT when a seam names its path and, where its symbol is
code-shaped, one of its tokens appears in the seam's symbol or instruction. A case is SOLVED when its
primary item is hit at MUST or SHOULD. The matcher cannot see a seam that wraps the ground truth (a
field adapter that maps media to the picker), so the misses were adjudicated by hand from `misses`,
and the semantic column below is that reading, stated as such.

## The arms

| arm | shape | agents per case |
|---|---|---|
| M0 | the shipped `reuse_lookup.py` at the case's point, the request's first sentence as the query | 0 |
| M1 | one free-roaming read-only scout, asked to find what the request must reuse | 1 |
| M1b | one scout walking a fixed checklist: orient, frame needs, anchors and the canonical implementation over stale copies, concept search including shell, design system, records, self-refute; a strict MUST | 1 |
| M2 | a framing agent, five fixed lenses, two skeptics, a derived list | 8 |
| M3 | a code scout and a design scout in parallel, then one judge | 3 |
| D1 | one reviewer per REINVENTING DIFF, asked whether it re-implements something the tree already had | 1 |

The arm scripts are `-1-6-*.js`, committed as they ran. M2 ran on three pilot cases only, because
its cost ruled it out (below). M3's judges died at a session limit in 28 of 30 cases while its two
halves had finished, so the M3 row grades the halves' UNION with the judge removed (`m3u`). Eleven
M1b agents and five M1 agents also died at that limit; every comparison below is PAIRED over the cases
both arms answered.

## Results

| arm | positives answered | solved (matcher) | items hit | decoy MUSTs |
|---|---|---|---|---|
| M0 | 24 | 0 | 1 of 59 | 0 |
| M1 | 21 | 12 | 20 of 53 | 0 |
| M1b | 15 | 10 | 17 of 40 | 0 |
| M3, judge removed | 21 | 8 | 16 of 53 | 0 |
| D1, at diff time | 23 | 7 | 13 of 57 | 0 |
| M2, pilot | 2 | 1 | 3 of 8 | 0 |

Unpaired rows are not comparable, because each arm answered a different set; the paired readings
follow.

**M0.** No case had its primary seam in the top 60 rows the committed file keeps. In the full run the
only primary ever reached was at rank 352 of 611. Six inCMS cases predate the tool, one inCMS case hit
the three-week window where it refused its own conf, and every NicoCares case runs on zero symbols.

**M1 against M1b, paired over 14 positives.** M1b solves 10 to M1's 8, hits 16 items to M1's 13, and
emits 94 MUSTs to M1's 132 over 168 seams to 216. Read by hand, three M1 misses are semantic hits
(`toPuckFields`, which maps a media field to `MediaPickerField`; `ResponsiveImage` with
`imageField()`; and a SHOULD at rank 9 naming `MediaPickerField`), which brings the two arms level on
recall at about 11 of 14. They are not level on what they bind: on the hero accents M1 bound
`DECOR_FIELD`, the stale text-URL copy the case's own reinvention had created, as a MUST, while M1b's
canonical-over-copy step bound `imageField`. Both missed the NicoCares account area's `Section` width
and `Eyebrow.bare`, and gov's `resolve_python`, a helper-level need no goal phrase implies.

**What a separate design scout adds.** Paired over 13 positives the M3 union solves 7 to M1b's 9,
because many of its code halves died. The design half alone is the useful reading. On NicoCares it
found three of four ground-truth items for the medical intake where M1b found two, including the
styling contract `help/package-styling-surface.md`; on the plan cards it found the generator, the
`product-cards-live` descriptor and the token layer; on the account area it was the only arm to name
`Section{width}`. On every gov case it returned nothing, after three tool calls and 82 s median.

**M2.** On the inCMS picker case it emitted 49 seams, 43 at MUST, never named `imageField`, and its
two skeptics refuted none of 49 candidates; on the visitor-upload control they refuted one of 42. It
cost 1.6 to 1.9 million subagent tokens per case and 69 to 82 minutes. A skeptic that confirms nearly
everything buys no precision, so the arm was not run further.

**D1.** Reviewing the landed diff solves 5 of 20 where M1 solves 11 of the same 20, but it is not a
weaker copy of the scout: it solved three gov cases that every pre-spec arm answering them missed,
all written below spec granularity (`check_prompt_brief`, the run-gates wall watchdog, the decisions
id regex). It
emitted 12 MUSTs over 45 seams, the lowest noise of any arm.

**Controls.** No arm bound a decoy at MUST. The inCMS entry-image control is the instructive one:
both scouts bound `resolveEntryImage`, which lives in the same file as the picker factory and is the
right render seam, so a decoy must be matched on its symbol, not its path.

## Cost

Per agent, medians, read with `python $B-4-bench.py cost <workflows-dir>` over this session's
transcripts, which are machine-local and not committed (PINNED, 2026-10-11, node a):

| agent | n | output tokens | cache-read tokens | tool calls | wall |
|---|---|---|---|---|---|
| M1 scout | 25 | 53k | 16.6M | 62 | 65 min |
| M1b scout | 19 | 74k | 27.7M | 84 | 116 min |
| M3 design half, non-UI cases included | 24 | 1.7k | 0.4M | 3 | 82 s |
| M3 code half | 14 | 47k | 14.6M | 57 | 73 min |
| D1 reviewer | 23 | 27k | 5.9M | 28 | 31 min |

Cache reads dominate: every tool call re-reads a context that grows past 400k tokens. These agents ran
at the session's own effort, `extra`, with no model override. An orientation step that holds a
session for two hours is not deployable at that setting; the next section measures `medium`.

## Effort: medium against extra, and the benchmark completed

The owner asked for two more runs, both at effort `medium`, through the parent scripts `-1-6-rerun.js`
and `-1-6-rerun-effort.js`:
- every agent the session limit had killed, which completes M1, M1b and the M3 judge;
- every agent that had finished at `extra`, again, so each arm can be compared case by case.

The 195 agents all returned. The results file keeps the earlier arms under their own names and files
every `medium` row under `<arm>@medium`, so nothing is pooled across efforts.

```bash
python $B-4-bench.py compare $B-3-cases.json $B-5-results.json m1b m1b@medium
```

**Quality, paired over the cases each arm answered at both efforts:**

| arm | paired positives | solved, extra → medium | items hit, extra → medium | MUST seams, extra → medium |
|---|---|---|---|---|
| M1 | 21 | 12 → 12 | 20 → 17 | 186 → 180 |
| M1b | 15 | 10 → 9 | 17 → 17 | 97 → 114 |
| M3 halves, unjudged | 21 | 8 → 9 | 16 → 18 | all SHOULD |
| D1, diff time | 23 | 7 → 4 | 13 → 9 | 12 → 3 |
| M2, pilot | 2 | 1 → 2 | 3 → 5 | 100 → 71 |

**Cost, per agent, medians** (PINNED, 2026-10-11, node a, `cost` over the two runs' transcripts):

| agent | output tokens | cache-read tokens | tool calls | wall |
|---|---|---|---|---|
| M1b scout | 74k → 16k | 27.7M → 4.3M | 84 → 23 | 116 → 10 min |
| M1 scout | 53k → 11k | 16.6M → 3.1M | 62 → 18 | 65 → 8 min |
| M3 code half | 47k → 11k | 14.6M → 2.9M | 57 → 18 | 73 → 8 min |
| M3 design half, every case run | n/a → 6.6k | n/a → 1.8M | n/a → 12 | n/a → 5 min |
| D1 reviewer | 27k → 4k | 5.9M → 1.2M | 28 → 8 | 31 → 4 min |
| M3 judge | n/a → 7k | n/a → 0.8M | n/a → 5 | n/a → 3 min |

**The scouts hold their recall at a fifth to a seventh of the cost.** Across the three scout arms the
paired movement is at most one solved case either way. The diff-time reviewer is the exception: at
`medium` it solves 4 of 23 where `extra` solved 7, and it binds a quarter as many MUSTs. Reviewing
a large diff evidently needs the deeper reading.

**The full corpus at medium.** M1 and M1b each solve 13 of 24 positives. M1b hits 23 of 59 items
against M1's 20, still with the canonical-over-copy step.

**The judge, measured at last.** M3 with its judge, at `medium`, solves 12 of 23 positives. M1b at
`medium` solves the same 12 on the same 23 cases, hits more items (22 against 20), and uses a third
of the agents. A judge adds nothing a checklist scout does not already do.

**The design pass at medium.** Added on top of M1b's own seams, the design half's seams raise the
UI cases from 6 solved to 7 and from 10 items of 28 to 13. All three extra items are NicoCares design
seams: the medical intake, the account area and the plan cards.

**One false MUST, in one place.** All three `medium` scouts bound `runlog_lib.read_journal` at MUST
on gov's health-log control. That is the decoy: a review once raised it as prior art and a skeptic
refuted it. At `extra` both scouts had died on that case, so effort cannot be blamed. A tempting
seam that is wrong for the request still reaches MUST, which is what `TOOL-aScoutedSeam-2`'s
override-with-a-reason exists for.

## What this decides

1. The mechanism is an agent that reads code; the name-matching lookup is a tool it may call.
2. ONE checklist scout is the core. It matched the free scout's recall with fewer MUSTs and was the
   only shape that refused a stale copy.
3. A DESIGN pass runs beside it and costs seconds when the request has no UI.
4. No skeptic and no judge agent: the measured skeptics confirmed nearly everything. The merge of the
   two passes is deterministic, and the binding is checked downstream instead.
5. A DIFF-TIME duplicate check is a separate mode, because a third of gov's misses happen after §10.
6. The scout and the design pass default to effort `medium`. That costs about ten minutes and 4M
   cache-read tokens per scout, against two hours and 28M at `extra`, for the same recall.
7. The diff mode defaults to a higher effort than the scout, because it is the one arm whose recall
   fell at `medium`.

## Limits

One node, one day, and a corpus biased toward duplicates a reviewer later noticed and named. Each arm
ran ONCE per effort, so run-to-run variance is unmeasured, and a movement of one case is within it.
Grading by path is a lower bound and the semantic reading is one person's. Nine prompts are
reconstructed. `high` was not measured, so the diff mode's default is a recommendation, not a
reading.
