# Synthesis brief: the audit's closing pair, compared

**Serves:** research PLAY-dClosedLoop-1

**Your task is to merge the whole-design audit's two closing reviews, run A and run B, into one comparison record,
written to `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-audit-closing-reviews-compared.md`.**
Every finding of both runs is placed on the defect it names, and every confirmed defect gets the fold that closes it.
This brief is your instructions, not the subject of your review.

## What you read

1. **The two reports**, each with its findings, its skeptics' verdicts and corrected fixes, and a `## Appendix — every
   finding` table:
   - run A: `memory/builds/dClosedLoop/reviews/2026-10-20-review-PLAY-dClosedLoop-1-audit-closing-a.md`
   - run B: `memory/builds/dClosedLoop/reviews/2026-10-20-review-PLAY-dClosedLoop-1-audit-closing-b.md`
2. **The last pair's comparison record,** for its shape and its method:
   `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-parked-debt-reviews-compared.md`. Its
   `[method]` points at the flow adoption's comparison, which you may read too.
3. **The design records a finding cites,** at the head commit `8d21999a9`, only to place a finding or to settle what a
   fold changes. Do not re-review them.
4. **The round record's `[fold]` and `[fold-applied]`** (`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`).
   They hold the owner's answers verbatim. A fold may not re-argue an answer.

Read nothing else. In particular, read neither run's transcripts nor the sealed copy.

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
   map. For a fold, name the records, sections, clauses or items it changes and what each change is, specifically
   enough for a spec writer to write it without the reports. For a fork, name the question, the options and the one
   you recommend.

## The runs

- **Subject:** `8d21999a9` over `6ba4eaaa1`. It covers every design commit since the parked debt's closing pair: that
  pair's fold, the owner's final questions and answers, the clause ids, Stage 0 and the walk kit, the owner's readings,
  the walk's records and the audit's fold (the args' context names each commit).
- **Harness:** `tools/workflows/tier2-review.js`, a full diff review. Each run had five `gov-diff-reviewer` lenses
  (security, correctness, seams, verification, intent), five `gov-skeptic` batches and one `gov-synthesizer`, every
  role at the owner's medium. The 32 design and research records the range touches or rests on were the intent
  inputs, and `gotchas.py --for-diff` gave the 35-class checklist.
- **Runs and reports:** dispatch 208 is run A, `wf_fe1512b8-f16`, `reviews/2026-10-20-review-PLAY-dClosedLoop-1-audit-closing-a.md`.
  Dispatch 209 is run B, `wf_e897bbe0-97d`, `reviews/2026-10-20-review-PLAY-dClosedLoop-1-audit-closing-b.md`.
- **The args:** `build_args_closing.py` wrote both. The runs differ only in the run label, the report path and the
  scratch path, and they ran one after the other.
- **Independence:** run A's report was moved out of the tree about thirty seconds into run B, and restored byte for byte
  after it (sha256 `d7b8e69ee5ab`). Run B's transcripts name it only in the git status the harness injects at start,
  six times, never in a tool call or a tool result.

## What you return

Your final message, nothing else:
- the record's path;
- the map's rows by disposition (fold, fork, no fold);
- each fork's question, one line each;
- any finding id you could not place, or `none`.
