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
