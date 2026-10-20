# Synthesis brief: the execution plan's fold review, compared

**Serves:** research PLAY-dClosedLoop-1

**Your task is to merge the two Tier-2 reviews of the execution plan's fold, run A and run B, into one comparison
record, written to `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-fold-reviews-compared.md`.**
Every finding of both runs is placed on the defect it names, and every confirmed defect gets the fold that closes it.
This brief is your instructions, not the subject of your review.

## What you read

1. **The two reports.** Each has its findings, its skeptics' verdicts and corrected fixes, and a `## Appendix — every
   finding` table:
   - run A: `memory/builds/dClosedLoop/reviews/2026-10-20-review-PLAY-dClosedLoop-1-execution-fold-a.md`
   - run B: `memory/builds/dClosedLoop/reviews/2026-10-20-review-PLAY-dClosedLoop-1-execution-fold-b.md`
2. **The last pair's comparison record,** for its shape and its method:
   `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan-reviews-compared.md`. Its
   `[fold]` table is what the fold under review applied, so a finding that a row landed wrong places against it.
3. **The plan and the records a finding cites,** at the head commit `fde10e6be`. Read them only to place a finding or to
   settle what a fold changes, and do not re-review them. The plan is
   `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md`. Its schedule script is
   `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py`.
4. **The execution record's `[answers]` to `[answers-4]`**
   (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution.md`). They hold the owner's answers
   verbatim, and a fold may not re-argue one. A risk an answer accepts knowingly is no defect. A place where the plan
   fails to surface that risk as the answer requires is a defect.

Read nothing else. In particular, read neither run's transcripts.

## What you write

One file, the record named above, with these sections in this order:

1. **The head:** an H1, a blank line, then `**Serves:** research PLAY-dClosedLoop-1`, then one paragraph naming the two
   runs and their subject.
2. **`## [runs] The two runs`:** copy the facts under *The runs* below. Restate nothing a report already says.
3. **`## [method] How the runs were compared`:** the last pair's method, applied unchanged. Say so and point at it.
4. **`## [map] Every finding, placed`:** one table, `| Defect | What | A | B | Disposition |`.
   - **Defect** is a short kebab-case slug.
   - **What** is one line saying what is wrong and where.
   - **A** and **B** list the run's finding ids from its appendix, comma-separated, or `—` for none.
   - Every finding id of both appendices appears in at least one row, confirmed or refuted. A finding naming two
     defects lands on both.
   - A row's ids are that run's ids for that defect only. Never write a claim one run made as what both found.
   - **Disposition** is exactly one of:
     - `fold`, adding `: <run>'s skeptic's corrected fix` where a skeptic judged the finder's fix unsound;
     - `fork: <the owner's question>`, where closing the defect needs a choice the owner has not made;
     - `no fold: <reason>`, for a refuted-only row, or one whose defect a later commit already fixed, with the reason
       in a few words.
5. **`## [summary] The two runs side by side`:** this one line only, which the main loop replaces with
   `compare_rounds.py`'s output: `(the comparison tool's output, written by the main loop)`.
6. **`## [fold] The fold plan`:** one table, `| Defect | Where it folds |`, one row per `fold` or `fork` row of the
   map.
   - For a fold, name the plan's sections, steps, rows or the script's parts it changes and what each change is,
     specifically enough for the plan's writer to write it without the reports.
   - For a fork, name the question, the options and the one you recommend.

## The runs

- **Subject:** `fde10e6be` over `8d33694d7`, the fold of the first pair. The range covers:
  - the 36 fold rows of the first pair's comparison record, applied to the plan and its schedule script;
  - the owner's two fork answers, `[answers-4]`;
  - the writer's return and the session log's rows.
- **Harness:** `tools/workflows/tier2-review.js`, a full diff review. Each run had:
  - five `gov-diff-reviewer` lenses (security, correctness, seams, verification, intent);
  - five `gov-skeptic` batches;
  - one `gov-synthesizer`.

  Every role ran at the owner's medium. The intent inputs were 14 records: the plan, the first pair's comparison
  record and two reports, the execution record, the five returns, the instruments record, v2, final-questions and
  the gap register. `gotchas.py --for-diff` gave the
  18-class checklist.
- **Runs and reports:**
  - run A: dispatch 226, `wf_13a913fe-7dc`, `reviews/2026-10-20-review-PLAY-dClosedLoop-1-execution-fold-a.md`;
  - run B: dispatch 227, `wf_06650e2e-9f6`, `reviews/2026-10-20-review-PLAY-dClosedLoop-1-execution-fold-b.md`.
- **The args:** `build_args_fold_review.py` wrote both. The runs differ only in the run label, the report path and the
  scratch path. They ran one after the other.
- **Independence:** run A's report was moved out of the tree before run B started and restored byte for byte after it.
  The session log took no row for either run until run B had returned.

## What you return

Your final message, nothing else:
- the record's path;
- the map's rows by disposition (fold, fork, no fold);
- each fork's question, one line each;
- any finding id you could not place, or `none`.
