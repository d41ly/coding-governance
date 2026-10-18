**Serves:** research TOOL-aScoutedSeam-3

# The system on both sets — orientation plus the diff check solves 21 of 23 tuned and 12 of 12 held-out

This record carries out the three steps the owner asked for on 2026-10-18
(`prompts/2026-10-18-prompt-TOOL-aScoutedSeam-3-brief-2.md`):
1. Measure the shipped flow end to end.
2. Apply the general fixes the misses pointed to.
3. Read the result on a case set that no prompt was tuned on.

One judge pass graded every arm on each set.

```bash
B=memory/builds/aScoutedSeam/build
python $B/2026-10-18-build-TOOL-aScoutedSeam-1-13-system.py system $B/2026-10-11-build-TOOL-aScoutedSeam-1-3-cases.json \
  $B/2026-10-11-build-TOOL-aScoutedSeam-1-5-results.json m1cA@medium d1v2@medium t1r@medium t2r@medium
python $B/2026-10-18-build-TOOL-aScoutedSeam-1-13-system.py system $B/2026-10-18-build-TOOL-aScoutedSeam-1-13-held-out-cases.json \
  $B/2026-10-11-build-TOOL-aScoutedSeam-1-5-results.json m1c@medium t1r@medium t2r@medium
```

## The held-out set

`-1-13-held-out-cases.json` holds 12 cases: 5 from gov, 4 from inCMS and 3 from NicoCares. All of them were
mined from commits made after the tuning corpus was cut. Each case has:
- a reinventing commit;
- objective evidence, which is a later dedupe commit, a recorded finding, or a verified near-copy;
- ground-truth seams verified at the parent commit;
- the request as phrased before the spec, without naming the seam.

The set and its trees were frozen and committed at `b6c828a92` before any arm ran on it. No prompt, lister
or rule changed after that. Every prompt is written for the general case, so it applies to these cases
without having been tuned on them.

The set differs in kind from the tuning corpus:
- It has no visual or CSS case.
- 3 of its 12 reinventions are in test code: fixtures, mocks and an install scaffold.
- The rest are helpers, gates and readers.

## What ran

| arm | what it is | handoffs |
|---|---|---|
| `m1cA` / `m1c` | the M1c orientation scout at kickoff: request plus tree, no diff | tuning: earlier pass; held-out `-88` to `-99` |
| `d1v2` | T1, the enumerated per-unit diff check, with no card | `-1-13` to `-35` (record `-1-10`) |
| `t1r` | T1 plus the orientation card's MUST/SHOULD seams as wiring rows | `-65` to `-87`, `-123` to `-134` |
| `t2r` | `t1r` plus the house index, the extended lister and six general rules | `-100` to `-122`, `-135` to `-146` |

- **Agents and effort.** Every arm ran as a typed `gov-reuse-scout` at `medium` on `claude-opus-5-5`, read-only, in the
  tree at the diff's parent. The card for each case came from that case's own orientation arm.
- **T2's fixes.** They are the step-2 fixes from the brief, each written as a general rule (`T2_RULES`,
  `extract_units_t2`):
  - a value-type census;
  - same-module siblings;
  - reachability across a kit boundary;
  - dossier and generator binding;
  - spec scope items as units;
  - CSS literals equal to a token's value.
  
  None of them reads a held-out case.
- **Judges.** One `gov-skeptic` per case judged every arm under rotated labels:
  - tuning: 23 handoffs, `-159` to `-181`;
  - held-out: 12 handoffs, `-147` to `-158`.
  
  The rubric is `-1-10-judge-task.md`. All 35 verdicts parsed, and they are stored under `judge2`.

## Results

| set | arm | primary covered | wrong seams |
|---|---|---|---|
| tuning (23 diff cases) | orientation `m1cA` | 15 | 119 |
| | T1, no card `d1v2` | 13 | 5 |
| | T1 + card `t1r` | **20** | 17 |
| | T2 + card `t2r` | 20 | 13 |
| | **system: orientation + T1** | **21** | |
| | system: orientation + T2 | 21 | |
| held-out (12) | orientation `m1c` | 8 | 70 |
| | T1 + card `t1r` | **11** | 7 |
| | T2 + card `t2r` | 11 | 15 |
| | **system: orientation + T1** | **12** | |
| | system: orientation + T2 | 11 | |

Across both sets, the system of orientation plus T1 covers 33 of 35 primaries (94%). T1 with the card
alone covers 31 of 35 (89%).

## What this decides

1. **The card is the largest single gain.** On the tuning set, T1 went from 13 to 20 when it was handed
   the orientation card's MUST seams as wiring rows. The prompt, tree, model and effort were unchanged.
   The two stages are not just a union: the diff check needs the orientation's output as input.
2. **The held-out set holds the gain.**
   - T1 with the card covers 11 of 12 held-out cases, against 20 of 23 tuned.
   - The system covers 12 of 12 held-out, against 21 of 23 tuned.
   - A prompt overfit to the tuning set would fall on the held-out set. This one did not.
3. **T2 ties T1 and is not adopted as the default.**
   - Coverage: T2 covers 31 of 35 primaries, as T1 does.
   - Wrong seams: 28 for T2 against 24 for T1.
   - System: its union with orientation scores one case lower on the held-out set.
   - Misses: the two arms miss different cases. On tuning, T1 misses hero accents and T2 misses reaped
     census. On held-out, T1 misses the media test scaffold and T2 misses the auth fixtures.
   
   T2 is kept as an optional second pass whose findings are unioned with T1's.
4. **Two tuning cases remain unsolved by every arm.**
   - **Design-data media:** the DSL's `media` field kind should have been used for a design-data image.
   - **Account area v1:** a Section width and a flat eyebrow recipe.
   
   Both are visual-convention cases in a package over a host core. No general rule tried here reached
   them.
5. **The orientation arm's wrong count is not comparable.** The judge grades the orientation against a
   diff it never saw, so seams the diff already used count as wrong. Its 119 and 70 measure that framing,
   not misleading advice.

## Confounds and limits

- **One run.** Each arm ran once, with one judge per case. A difference of one or two cases is noise.
- **Judges stretched the rubric**, as in `-1-12-judge-and-low.md`. Some returned `primary` as MUST or SHOULD, or split
  `valid_extra` by binding. The collector reads any non-empty `primary` as covered and sums a split count.
- **One tuning arm returned no seams** on `gov-declared-gitcommondir`. It is scored as a miss, not as a
  parse failure.
- **One agent was re-run.** The tuning `t1r` agent for `nc-acct-area-v1` hung on a shell call for 42 minutes. It
  was stopped and re-run from the same handoff (`-82`), and only the re-run is collected.
- **The extractor was fixed during the run.** A T2 reply quoted three backticks inside a JSON string. `extract_reply` now decodes one
  JSON value from the last fence. That changes parsing, not any prompt. All replies were re-collected
  after the fix.
- **The denominator was corrected.** `system` now counts only the cases an arm was judged on. The
  tuning case `c14` has no diff and is outside the diff check's population.
- **Spawn cap.** As in `-1-12`, the agent-cap slot files were released by hand under the owner's
  authorization, with no more than five agents running at once.
- **The lister skips tests.** All three held-out test-code cases were still found, through the open
  search and added rows. The held-out set shows this, and no change was made from it.

## Where it goes

`2026-10-18-build-TOOL-aScoutedSeam-3-2-workflow-design-set.md` compiles these settings into the
workflow another session can adopt.
