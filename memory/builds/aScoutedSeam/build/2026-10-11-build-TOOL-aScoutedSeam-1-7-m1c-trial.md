**Serves:** research TOOL-aScoutedSeam-1 KICK-aScoutedSeam-1

# The M1c trial — a house index, an implementation sketch and a convention census, against the checklist scout

Run 2026-10-11 on node `a`, at the owner's request, after the benchmark record
(`2026-10-11-build-TOOL-aScoutedSeam-1-2-benchmark.md`) left the two single scouts at 13 of 24 by the
path matcher. Every figure below re-derives from the committed corpus and results with the committed
grader, except the cost row, whose transcripts are machine-local.

```bash
B=memory/builds/aScoutedSeam/build/2026-10-11-build-TOOL-aScoutedSeam-1
python $B-4-bench.py compare $B-3-cases.json $B-5-results.json m1b@medium m1cA@medium m1cB@medium
python $B-4-bench.py judged  $B-3-cases.json $B-5-results.json m1@medium m1b@medium m1cA@medium m1cB@medium
```

## What changed from M1b

M1b, the checklist scout, missed 11 of 24 at `medium`, and reading the misses sorted them into five
causes:
- a need below the request (four cases);
- a house convention its siblings follow (one);
- run-to-run variance (about three);
- the grader undercounting (two);
- one vague question.

M1c is M1b plus three changes, aimed at the first three causes. The arm is
`-1-6-m1c-sketch-scout.js`.

1. **A house index, read first.** `bench.py index` generates it per case from the tree as of the
   case's point, with no agent, into `<tree-root>/<short>/house-index.md`. It holds:
   - the shared libraries;
   - the `# >>> <name>` canonical copies installed in several files;
   - the most-reused symbols, with fan-in derived the way the map derives it;
   - the gate legs and custom lint rules;
   - the recorded bug classes;
   - the dossiers' reuse affordances;
   - the CSS custom properties;
   - the DSL node kinds, for a package case taken from its host tree too.

   Sizes ran from 2 KB on early trees to 33 KB on NicoCares with its host.
2. **An implementation sketch, searched piece by piece.** Before searching, the scout lists 6 to 15
   components a builder would write: tests, wiring, config reads, launchers, phase decisions and styles
   included. It then looks for an existing implementation of each.
3. **A convention census.** When the request builds an instance of a kind with siblings, the scout
   opens five or more of them, tabulates the shared choices, and binds the majority.

Two runs, A and B, went over all 30 cases at effort `medium`, through `-1-6-rerun-effort.js`: 60
agents, all of which returned. A blind judge then read every case at `medium`, `-1-6-judge.js` with
one judge per case. Each judge got the request, the ground truth, the decoys and six anonymous arms
under labels rotated per case: M1 and M1b at `extra`, the same two at `medium`, and M1c A and B.
`bench.py judge-packets` writes the packets and their key; `judge-collect` joins the verdicts back
through the key and files them under `judge` in the results.

## Results

**By the path matcher, all 24 positives:**

| arm, effort medium | solved | items hit | MUST seams | decoy MUSTs |
|---|---|---|---|---|
| M1 | 13 | 20 of 59 | 190 | 1 |
| M1b | 13 | 23 of 59 | 166 | 1 |
| M1c, run A | 16 | 26 of 59 | 213 | 2 |
| M1c, run B | 16 | 24 of 59 | 210 | 1 |

**By the blind judge, all 24 positives and 6 controls.** A primary counts when item 0 is covered at
MUST or SHOULD. A wrong MUST is one the judge says would mislead the build.

| arm, effort medium | primary found | items covered | wrong MUSTs | mean score |
|---|---|---|---|---|
| M1 | 14 | 35 of 59 | 59 | 3.04 |
| M1b | 14 | 37 of 59 | 11 | 3.50 |
| M1c, run A | 17 | 39 of 59 | 20 | 3.50 |
| M1c, run B | 18 | 39 of 59 | 24 | 3.62 |
| M1c A and B, unioned | 18 | 41 of 59 | 44 | 3.71 |
| M1 and M1b, unioned | 16 | 41 of 59 | 70 | 3.67 |

The judge reads two more primaries than the matcher for every arm, mostly seams that route the build
through the ground truth without naming its file. On the 14 positives every arm answered at both
efforts, M1b at `extra` found 11 primaries with 1 wrong MUST, and M1c found 11 and 12 at `medium`.

**Stability.** M1c's two runs agree on all 24 positives by the matcher. The old scouts flipped on
about seven between runs, so a second M1c run adds no primary. The M1c union's only gain is items.

**Cost per agent, medians** (PINNED, 2026-10-11, node a, `bench.py cost` over the run's transcripts):
28k output tokens, 9.3M cache-read tokens, 40 tool calls and 22 minutes. That is about double M1b at
`medium` (16k, 4.3M, 23 calls, 10 minutes) and a fifth of M1b at `extra`.

## Case by case, by the judge

| case | M1b medium | M1c A | M1c B | what moved it |
|---|---|---|---|---|
| inCMS email image | miss | found | found | the picker reached through the sketch's "image field" component |
| NicoCares legal pages | miss | found | found | the core `Article` block and the page shape, both runs |
| gov lexicon tokenizer | miss | found | found | `subtokens`, via the index's most-reused symbols |
| gov README marker index | miss | found | found | `unfenced_lines`, searched as a sketched component |
| NicoCares account area | miss | miss | found | the census: Section `width: normal` in 49 of 67 descriptors |
| gov conf parser | found | miss | miss | the census (see below) |

Still missed by every arm:
- the run-gates wall watchdog;
- the driver's terminal-phase set;
- the Python launcher;
- the vague keyed-decisions question;
- `imageField` on the DSL design-data case, where every arm reaches the picker only through
  `toPuckFields`.

The house index named the launcher. The sketch for that case never listed "launch an interpreter from
a shell test", so the index entry was never searched.

**Controls.** Both M1c runs bound the health-log decoy at MUST: `runlog_lib`'s `read_journal` and
`PRODUCER_FILES`, run A in two seams and run B in one. Every `medium` scout in the benchmark bound
it too. Neither run bound a decoy on any other
control.

## What broke, and what to fix

**Precision.** By the judge, roughly 20 of M1c's 22 wrong MUSTs per run are build work. 14 are edits,
registrations or regenerations, and 6 are tests or gates to write or keep green. M1b had 8 of those in
11. The sketch asks the scout to list the plumbing, and the plumbing then lands in the seam list. The
fix is a destination: a separate `edits` output for the work a sketched component needs, and the rule
that a seam names an existing implementation of a need, never a change to make.

**The census pitfall.** On the conf-parser case, the census found its majority convention: each module
keeps a local `load_conf` copy, four of four. It bound that at MUST. The four copies ARE the
duplication the case records, and M1b had found the canonical reader instead. A census binds the
majority for a CHOICE: a prop, a token, a layout, a test harness. For a HELPER it binds the canonical
implementation and names the copies in `not`, because a majority of copies is a debt and not a
convention.

**The census does not reach the seam list by itself.** The account-area census line was right in
both runs and reached a seam in one. The deployed section therefore carries census results as their
own line kind, `- convention <choice>: <majority> (<n> of <m>)`, instead of relying on the scout to
restate them as seams.

## What this decides

1. The deployed role is M1c's: the house index first, the sketch, the census and the search of every
   sketched component. It carries the three fixes above.
2. The house index is a deployed, deterministic generator run by the caller before the scout. A
   scout cannot be relied on to discover a launcher ban or a canonical copy unaided.
3. One scout, not two. M1c's runs agreed case for case, so an ensemble buys no primary at twice the
   cost.
4. Effort stays `medium`. M1c at `medium` matches M1b at `extra` on the paired cases at a fifth of the
   wall.

## Limits

Each M1c variant ran twice, and every other arm once per effort. The judge is one model reading
blind, once per case, and it was not itself measured against a second judge. The three fixes above
are recommendations from this reading, NOT measured: `TOOL-aScoutedSeam-1`'s calibration criterion is
where they are first observed. Nine prompts are reconstructed, as before.
