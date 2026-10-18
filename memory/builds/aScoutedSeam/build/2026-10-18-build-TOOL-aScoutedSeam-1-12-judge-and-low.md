**Serves:** research TOOL-aScoutedSeam-3

# The blind judge and the `low` arm — the enumerated prompt holds at `medium` and fails at `low`

This record follows the T1 trial (`2026-10-18-build-TOOL-aScoutedSeam-1-10-d1v2-trial.md`) and the method
record (`2026-10-18-build-TOOL-aScoutedSeam-1-11-prompt-method.md`), and does two things the owner asked
for on 2026-10-18. It reads the precision T1 left unmeasured, through a blind judge. It also runs the same
prompt at `low`, to see what effort still buys once the composition is fixed.

```bash
B=memory/builds/aScoutedSeam/build/2026-10-11-build-TOOL-aScoutedSeam-1
python $B-4-bench.py compare $B-3-cases.json $B-5-results.json d1 d1@medium d1v2@medium d1v2@low
python $B-4-bench.py judged  $B-3-cases.json $B-5-results.json d1 d1@medium d1v2@medium d1v2@low
```

## What ran

- **The `low` arm.** The 23 T1 handoffs (`prompts/...-1-13` to `-35-reuse-scout.md`) ran again
  unchanged, as the same typed `gov-reuse-scout`, with the Agent call's effort set to `low`. The prompt,
  role, card, trees and model (`claude-opus-5-5`) are the same, so effort is the one variable. The
  replies were collected as `d1v2@low`.
- **The blind judge.** `-1-10-d1v2.py packets` wrote one packet per diff case through the bench's own
  `judge-packets`, so the four arms sit under labels rotated per case. Each packet was extended with the
  diff and its pre-diff tree. One `gov-skeptic` per case judged the packet. Each was spawned from a
  handoff (`prompts/...-1-36` to `-60-skeptic.md`; -39 and -40 were rendered and discarded) whose
  `input:spec` is `-1-10-judge-task.md`, the bench judge's rubric worded for a diff. The verdicts landed
  under `judge` through `-1-10-d1v2.py judge-collect`. All 23 parsed.

## Results

By the path matcher:

| arm | solved | items | seams | MUST |
|---|---|---|---|---|
| D1, `extra` | 7 of 23 | 13 of 57 | 52 | 12 |
| D1, `medium` | 4 of 23 | 9 of 57 | 34 | 3 |
| T1, `medium` | 14 of 23 | 19 of 57 | 130 | 30 |
| T1, `low` | 6 of 23 | 12 of 57 | 105 | 44 |

By the blind judge:

| arm | primary covered | items | misleading seams | genuine extras | mean score |
|---|---|---|---|---|---|
| D1, `extra` | 11 of 23 | 25 of 57 | 0 | 37 | 2.74 |
| D1, `medium` | 7 of 23 | 14 of 57 | 2 | 21 | 2.09 |
| T1, `medium` | 14 of 23 | 25 of 57 | 11 | 73 | 2.96 |
| T1, `low` | 8 of 23 | 15 of 57 | 19 | 50 | 1.96 |

## What this decides

1. **T1 at `medium` is the best arm under both graders.** The judge reads more primaries into D1 than
   the matcher does (11 against 7 at `extra`), so the margin narrows from 14 against 7 to 14 against 11.
   It does not close. Items covered tie with D1 at `extra` (25 each), and T1's mean score is the
   highest.
2. **The volume is mostly real.** Of T1's 130 seams at `medium`, the judge called 73 genuine reuses
   beyond the ground truth and 11 misleading, about 8%. D1 at `extra` bound none misleading in 52. The
   misleading seams cluster in a few cases. Reaped census has 3: test-harness seams in a kit that cannot
   import them. Design data has 2, and decor texture 2. That is the cost of the enumerated prompt, and the
   precision measures are aimed at it: TOOL-aScoutedSeam-1's cap of five MUSTs and the MUST-names-the-
   duplicate definition.
3. **`low` does not hold the gain.** With the same prompt, `low` covers 8 primaries, one more than D1 at
   `medium` and six fewer than T1 at `medium`. It binds the most misleading seams (19 of 105, about 18%)
   and the most MUSTs (44), and has the lowest mean score. The enumeration makes `low` list more, not find
   more. The composition fix needs `medium` to pay off.
4. **D1 and T1 miss different cases.** D1 at `extra` found the design-data picker and the plan-cards
   generator, which T1 missed. T1 found batched launcher, warded terminal, email image, and both medical
   intake restyles, which D1 missed. No arm found reaped census, declared git common dir, hero accents or
   account area.

## Confounds and limits

- **Judge runner.** The judges ran as typed `gov-skeptic` agents at that role's rendered effort (`high`).
  The pre-spec arms' judge ran as plain Workflow agents. The rubric fields are the same, but the role
  body frames the judge as a refuter.
- **Judges stretched the rubric.** Several scored an arm that missed the primary at 2 or 3, where the
  rubric says 1. Some returned `primary` as `MUST`/`SHOULD` in place of a boolean, and one split
  `valid_extra` by binding. The collector sums a split count and reads any non-empty `primary` as true.
  Mean scores are comparable within this pass, not against the pre-spec judge.
- **Packets point at two trees.** Each carries the pre-spec case tree and the pre-diff tree. For these
  cases the two hold the same code at the cited seams (one judge checked `gen_build_index.py` byte for
  byte).
- **Spawn cap.** The agent-cap hook's per-prompt ledger refused spawns past five in 45 minutes. With the
  owner's authorization ("bypass agent-cap for this test"), its slot files were released by hand as each
  agent finished, and no more than five agents ran at once.
- **One run.** Each arm ran once, with one judge per case.
