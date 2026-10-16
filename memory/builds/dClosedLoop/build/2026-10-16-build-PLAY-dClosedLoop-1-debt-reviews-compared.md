# The review debt's six pieces, each reviewed twice, compared

**Serves:** research PLAY-dClosedLoop-1

The state record's `[unreviewed]` named six pieces of the design that no review had read
(`build/2026-10-16-build-PLAY-dClosedLoop-1-state.md`). The owner asked for each to be reviewed twice at
medium effort. This record holds the twelve runs, and their comparison once they return. The args, and the
script that wrote them, are in `build/2026-10-16-build-PLAY-dClosedLoop-1-debt-reviews-compared-instruments.md`.

## [words] The owner's words, 2026-10-16

> fix everything that's stale, then review all 6 unreviewed pieces - medium effort, twice each.

## [runs] The twelve runs

| Dispatch | Piece | Kind | Subject | Round | Prior set | Reports |
|---|---|---|---|---|---|---|
| 61, 62 | the lexicon | spec audit, full | `lexicon.md` at `424d2a7de` | 1 | — | `reviews/2026-10-16-review-PLAY-dClosedLoop-1-lexicon-a.md`, `-b.md` |
| 63, 64 | the review system | spec audit, full | `review-system.md` at `40738693d` | 1 | — | `reviews/2026-10-16-review-PLAY-dClosedLoop-1-review-system-a.md`, `-b.md` |
| 65, 66 | the runtime fold and its two settlements | diff review, light | `6cfd21619..3611a60e9` | 1 | none; the two audit reports ride as specs | `reviews/2026-10-16-review-PLAY-dClosedLoop-1-runtime-fold-a.md`, `-b.md` |
| 67, 68 | the layers round's follow-up fold | diff review, light | `cc4c83ad5..1bc4883fe` | 3 | round 2's 31 confirmed, from `wf_e26eda01-523` | `reviews/2026-10-16-review-PLAY-dClosedLoop-1-fold-round3-a.md`, `-b.md` |
| 69, 70 | the library round's fold | diff review, light | `d4fc4bb51..0dd962724` | 2 | round 1's 25 confirmed, from `wf_9d4cc07b-2f2` | `reviews/2026-10-16-review-PLAY-dClosedLoop-1-library-followup-a.md`, `-b.md` |
| 71, 72 | the expansion round's follow-up fold | diff review, light | `67c79f7cc..5e139d377` | 3 | round 2's 24 confirmed, from `wf_c69ed990-543` | `reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-fold-round3-a.md`, `-b.md` |

## [method] How they run

- **Medium effort.** Every stage, finder, skeptic and synthesis, runs at `medium`, as the owner asked, and
  as the layers' and the runtime layer's audits ran.
- **Kinds.** The two designs no review read get the spec audit the layers got: round 1, full, the record
  at its blob as the subject, and the same six questions. The four folds get the light diff review every
  fold review got. A fold that answers an earlier round is that chain's next round, handed that round's
  confirmed set from its workflow's own ledger.
- **At HEAD.** The worktree is past each fold, and later commits changed some of its text. So each fold
  review reports a defect only if HEAD still carries it, and cites HEAD's line.
- **Independent pairs.** Runs A and B share every field but the run label, the report path and a spec
  audit's scratch directory, which the instruments' `[pairs]` checks. Each run is told the other run's
  report is not evidence.
- **One at a time.** No more than five agents run at once, the review protocol's at-once bound, and one
  run already reaches five. So the twelve run in the table's order, each after the one before returns,
  as dispatches 57 and 58 did.
- **The spec audits' opt-in.** This build's README carries `spec-audit:` under `authorized-by: prompt`,
  and agent-cap admits no audit on a key under that mode. So, as for dispatches 39 to 46, the README's line
  is set aside and `.unattended.conf` dates `SPEC_AUDIT_DEFAULT` around each spec audit's dispatch call,
  in the working tree only. Both are restored as soon as the call is admitted, and neither change is
  committed.
- **The comparison** follows the layers' method: each pair's findings are placed on shared defects, and
  what one run alone found is named.
