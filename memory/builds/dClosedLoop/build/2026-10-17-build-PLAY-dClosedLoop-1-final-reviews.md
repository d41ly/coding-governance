# The folds' closing review, and the systems and retrofit audit

**Serves:** research PLAY-dClosedLoop-1

The owner asked for two reviews once the debt round's folds and the systems and retrofit fold had landed.
This record holds their runs, and their folds once they return. The args, and the script that wrote them,
are in `build/2026-10-17-build-PLAY-dClosedLoop-1-final-reviews-instruments.md`.

## [words] The owner's words, 2026-10-17

> delete the duplicate artifact first, then do both the closing review of the folds and a tier-2 review of the systems and retrofit rounds.

## [runs] The two runs

| Dispatch | Review | Kind | Subject | Round | Report |
|---|---|---|---|---|---|
| 85 | the closing review of the folds | diff review, full | `9b188202a..cdcea2c9b`, without the review reports, the session log and the generated files | 1 | `reviews/2026-10-17-review-PLAY-dClosedLoop-1-debt-folds.md` |
| 86 | the systems and retrofit rounds | spec audit, full | the systems record at blob `9335a3533` and the retrofit record at blob `cec90968d` | 1 | `reviews/2026-10-17-review-PLAY-dClosedLoop-1-systems-retrofit.md` |

## [method] How they run

- **The duplicate artifact first.** The delete of `4UyRaoozVkbK6ECCCBvDg1` needs the owner's confirmation,
  which this session cannot show, so nothing was deleted. The owner deletes it from the artifact's own menu.
- **One at a time.** Each run reaches five agents at once, the review protocol's bound, so dispatch 86
  goes once dispatch 85 returns.
- **Efforts.** Each run takes what `handoff.py stage-efforts` prints for its workflow: the closing review
  runs at high at every stage, and the spec audit at medium.
- **Full intensity.** The closing review runs all five diff lenses, security and intent among them, since
  the folds change the dispatcher's binding, the release hold and the adopter sandbox. A spec audit runs
  only the full set.
- **The closing review's subject** is every commit since the debt round's twelfth review returned: the six
  pairs' folds, the two folds' owed fixes, and the systems and retrofit fold into v2. The comparison
  record's maps and each fold section are its statement of intent. It is round 1, since no review read the
  folds, and the twelve runs' findings are not handed in as a prior set: each map row names the fix to
  check.
- **The spec audit's opt-in.** As for dispatches 61 to 64, the README's `spec-audit:` line is set aside and
  `.unattended.conf` dates `SPEC_AUDIT_DEFAULT` around the audit's dispatch call, in the working tree only.
  Both are restored once the call is admitted, and neither change is committed.

- **What dispatch 86 read** (recorded 2026-10-17, once it returned). Dispatch 86 went once dispatch
  85's return was recorded, and the fold of 85 was written while it ran. The fold wrote both subjects at
  11:44:56Z: a three-line re-run note in the systems record, and the retrofit record's offered-update
  bullet and its dTotalRecall owners row. Each of the five finders read the subjects between 11:35:42Z
  and 11:42:28Z, before that write. Each of the five skeptics found both subjects moved with `git
  hash-object`, and read the pinned blobs from git. So the audit covers the pinned text, and the fold's
  lines in the two subjects are 85's fold text, unreviewed like every fold. The timing probe and its
  output are in the final instruments' `[read-86]`.

## [fold-debt-folds] Dispatch 85's findings, folded 2026-10-17

The folds' closing review returned CLEAN WITH FIXES, 22 of 27 findings confirmed in 20 items
(`reviews/2026-10-17-review-PLAY-dClosedLoop-1-debt-folds.md`). Ids 9, 15, 16, 17, 20 were refuted. Each item went
here, and each row's classes are its confirmed findings' own, from the ledger:

| Item | Ids | Disposition | Where the fix sits | Its classes |
|---|---|---|---|---|
| H1 | 1 | fork, asked as RT-4 | layer-runtime `[act]`'s decision by binding, once the owner answers | — |
| M1 | 7, 14 | amend | flow-steps' `review.pin`; review-system `[lenses]`; v2's dFairHearing row | — |
| M2 | 8, 25 | amend | v2's dTotalRecall row | — |
| M3 | 2 | amend | layer-runtime `[supervise]`'s fencing, `named-acts` and the `fencing` fixture | — |
| M4 | 3 | amend | layer-runtime `[enforce]`'s preflight population and the `fail-closed` plugin arm | — |
| M5 | 6 | amend | flow-steps' closing review | — |
| M6 | 10 | amend | layer-runtime `[decide]`'s `awaiting` row and the `next` arm | `route-names-an-output-its-actor-never-emits` |
| M7 | 11 | amend | layer-expansions' `kits.offer`; `gap-deploy-13`; retrofit `[seed]`; v2's dShippedRelease row; the foreign-code class's fixture | `foreign-code-runs-on-the-ambient-credential` |
| M8 | 12 | amend | v2's dOrderedCharter row; layer-memory `[names]`; layer-library `[consult]` | `retirement-inventory-misses-readers-by-value` |
| M9 | 13 | amend | the both-runs probe revised in `[probes-final]`; the systems record's re-run; the one-run class | — |
| M10 | 18 | amend | the target-spawn probe's failing arm in `[probes-final]`; `kits.offer`; the foreign-code class | — |
| M11 | 22 | amend | flow-steps' `build.unit-pass` | — |
| M12 | 23 | amend | layer-roles `[matrix]`' counts and its run of 2026-10-17 | — |
| M13 | 24 | amend | review-system `[lenses]`' scorer; v2's dFairHearing row | — |
| M14 | 26 | amend | v2's dTotalRecall row; retrofit `[owners]` | — |
| L1 | 4 | amend | as M12 | — |
| L2 | 5 | amend | layer-runtime's two rows indented; the table-shape probe in `[probes-final]`; the pipe class | — |
| L3 | 19 | amend | `gap-design-05`; the reuse-token probe in `[probes-final]` | — |
| L4 | 21 | amend | the debt record's `[fold-fold-round3]` row; the layers record's `[folded]` and its tally script | — |
| L5 | 27 | amend | v2's dRankedPlan row | — |

- **The one fork.** H1 changes what the runtime design promised for attended sessions, and it rests on
  RT-2 and on the owner's ruling that auto mode stays, so it goes to the owner as RT-4.
- **What M10's probe found beyond the item.** Its revision reads git calls in the target too. Update's git
  writes there fire the target's own hooks, a seventh kind of target-side code today, and `kits.offer`
  now runs git there with `core.hooksPath` pointed at an empty directory.
- **The fold is unreviewed text,** like every fold before it.
