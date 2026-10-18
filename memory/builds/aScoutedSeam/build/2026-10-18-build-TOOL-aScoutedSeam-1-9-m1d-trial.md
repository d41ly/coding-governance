**Serves:** research TOOL-aScoutedSeam-1

# The M1d trial — drafting the code and expanding every cited file finds none of the six misses

Run 2026-10-18 on node `a`, at the owner's choice of option 3: test fork F3 cheaply on the six positives
both M1c runs missed and the six calibration cases, before building it. The previous step is the
offline reading (`2026-10-13-build-TOOL-aScoutedSeam-1-8-precision-and-misses.md`). It found that
listing the definitions of every cited file would REACH five of the six misses, and it said that
reach is not discovery. This trial measures discovery.

```bash
B=memory/builds/aScoutedSeam/build/2026-10-11-build-TOOL-aScoutedSeam-1
python $B-4-bench.py compare $B-3-cases.json $B-5-results.json m1dA@medium m1cA@medium m1cB@medium m1b@medium
```

## What ran

M1d is M1c's checklist with three additions and two census rules:
- **Draft.** The scout writes the code a builder would type, as a return field.
- **Expand.** The scout lists the definitions of every file it cites or anchors on, constants included,
  with the `defs` subcommand of `-1-8-precision.py`.
- **Owners.** The scout greps for the existing owner of every literal, regex and launcher in the draft.
- **Census rules.** A majority of local copies of a helper is never a convention, and the census covers
  the exact prop the request adds.
- **Return.** Build work goes to `edits`, and the scout binds at most five MUSTs.

The roles kit's spawn guard admits a `Workflow` call only for a listed harness, so the arm ran as 12
typed `gov-reuse-scout` agents, one per case. Each was spawned from a handoff `handoff.py render`
wrote. Every handoff was rendered against an EMPTY card, because this session's card names the
benchmark's ground truth. The questions are built by `-1-9-m1d-trial.py questions`, and the handoff
records are under `prompts/` as `2026-10-18-prompt-DEPL-aScoutedSeam-1-<n>-reuse-scout.md`. The
replies were collected into `-1-5-results.json` as `m1dA@medium` by `-1-9-m1d-trial.py collect`.
Only run A ran; see "What this decides".

## Results, by the path matcher, same 12 cases

| arm | solved | items hit | MUST seams | decoy MUSTs |
|---|---|---|---|---|
| M1d run A | 4 of 10 | 8 of 28 | 56 | 0 |
| M1c run A | 4 of 10 | 8 of 28 | 80 | 2 |
| M1c run B | 4 of 10 | 6 of 28 | 76 | 1 |
| M1b, `medium` | 4 of 10 | 8 of 28 | 54 | 1 |

**None of the six misses was found.** Read case by case from the replies:
- **gov pooled wall:** the scout opened `run-gates.sh`, called its dispatcher a lure for a fixed batch,
  and left `arm_wall` in its unmet "searched" note.
- **gov keyed decisions:** it bound `corpus_ids.py`'s orphan-id check and never reached `map_lib.py`.
- **gov warded terminal:** it reframed the request as reading the opt-in at a git base, so the terminal
  phase set never entered its draft.
- **inCMS DSL design data:** it reached the picker through `toPuckFields` again, as every arm has.
- **gov conf parser:** the census rule held. The scout called the five local `load_conf` copies debt
  and extended `corpus_ids.py`. It still bound no canonical `load_conf`, so the matcher misses it.
- **gov batched launcher:** its draft launched `node`, not Python, so `resolve_python` never came up.
  That held even though the handoff's Facts block names `resolve-python.sh`.

**The calibration cases held.** All four positives were solved, as by M1c. The health-log control bound
no decoy at MUST, where both M1c runs had.

## What this decides

1. F3 does not pay off for recall. Listing a cited file's definitions puts the missed name within the
   scout's reach, and the scout still does not bind it. Its draft follows its own framing of the
   request, and the missed seam lies outside that framing. Reach was the offline reading's measure, and
   this trial shows it does not become discovery.
2. Option 1 is therefore not run with F3. The second run was dropped: M1c's two runs agreed on every
   case, and run A moved none of the six.
3. The return-contract changes do pay off for precision. These are the `edits` bucket, the cap of five
   MUSTs and the MUST definition naming the duplicate. MUSTs fell from 80 and 76 to 56 at equal recall,
   and the decoy was not bound. This supports TOOL-aScoutedSeam-1's merge cap and its return contract.
4. Recall on the pre-spec scout has plateaued at the misses that need code to read. The diff-time mode,
   TOOL-aScoutedSeam-3, reads the builder's actual diff, and it is the measured route to them. It found
   the pooled-wall and keyed-decisions seams in the benchmark.

## Confounds and limits

- **Runner.** M1d ran as typed role agents carrying the role body, its rule and gov's Facts block. M1c
  ran as plain Workflow agents. The precision gain may partly come from the runner.
- **Speed.** These agents were faster than M1c's: 166 to 541 seconds, median about 4.5 minutes,
  against M1c's 22. The same confound applies.
- **Contamination.** Gov's Facts block names `resolve-python.sh`, the ground truth of the
  batched-launcher case. It was missed anyway, so the contamination did not change a verdict.
- **Grading.** One run on 12 cases, graded by the path matcher only; no blind judge was run. The
  conf-parser and design-data readings above are case-by-case reads of the replies.
