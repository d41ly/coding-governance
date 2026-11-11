**Serves:** research TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-21

# dWitnessedBar — the parents cross-check readers' returns, verbatim

The `gov-spec-reviewer` return the cross-check record [`2026-11-05-build-TOOL-dWitnessedBar-1-parents-crosscheck`](2026-11-05-build-TOOL-dWitnessedBar-1-parents-crosscheck.md) is assembled from, extracted by script from each agent's transcript and not retyped. The brief is [`2026-11-05-prompt-TOOL-dWitnessedBar-1-parents-crosscheck`](../prompts/2026-11-05-prompt-TOOL-dWitnessedBar-1-parents-crosscheck.md); each group's handoff sits beside it.

## Group A, citation, led by spec 21 (spec 21)

1. Assumption table

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 21 | dl32 owns a `--fix-pass` loop, and wb21 leaves the counting of fix passes to it (wb21:75-76, §3 non-goal) | cite | AGREES | wb21:75-76 "Counting fix passes against a budget: TOOL-dDeclaredLoop-30's `flow.rework-budget` draw and TOOL-dDeclaredLoop-32's `--fix-pass` loop." dl32:64-71 S5 still reads "The fix-pass loop. A verb `--fix-pass <slug> --unit <id> --reds <N>` records one fix pass … as a `fix-pass` row through `park()`". `git show 63669d505` has no S5 hunk. |
| 21 | That fix-pass loop keeps a budget-bound exit (strict fall, bounds, and a promotion target from the budget), so it can be the place where counting against a budget lives | SA | AGREES | dl32:21-22 "every fix pass against one acceptance red ends at the first round whose blocker and high count does not strictly fall". dl32:51-52 "The non-decrease test keeps reading the blocker and high count on the build slug and on a fix pass." dl32:69-70 "Its target is `promotion_target`'s answer as it stands, ` · to units` or ` · to on-exhausted`". The rev-3 log, dl32:378-380, says "follow-ups and fix passes keep the rule". |
| 21 | dl30's `flow.rework-budget` draw counts fix passes (wb21:75) | cite | AGREES | dl30:47 lists `fix-pass` among the closed draw causes. dl30:55 "`fix-pass` for a dispatch of a unit whose earlier pass committed". `git log 443775a2f..ab976b5b3` names no dl30 revision, apart from the e5de11e9e no-op merge. |

2. MISMATCH

None.

3. UNKNOWN UNTIL BUILT

None. wb21 relies on dl32 only through the §3 non-goal, and today's parent text decides that.

4. Rule-wide hits that no rule binds

- wb21:75 (the `rework budget` / `flow.rework-budget` hit). It routes fix passes, not a spec audit, to the budget. SA keeps strict fall and budget routing for fix passes (dl32:21-28, :51-52), so this line breaks no SA clause. The line is classified as a cite row above and is not an SA MISMATCH. No other probe term (`review_state`, `no-fall`, `NON-CONVERGENT`, `promotion_target`, `item.review.dispose`, `review.design.rounds`, precision floor, chain stop, `REVIEW_ROUNDS`) occurs in wb21. Probe: `git show ab976b5b3:<wb21> | grep -niE '<SA terms>|budget|dDeclaredLoop|dFairHearing'` printed only lines 75 and 76.

5. Revised parent sections the citation spec does not depend on

- wb21: none of its assumptions depend on these sections of dl32 rev-3: §1 (the spec-audit sentence, dl32:23-25), S2 (route-backs only for the build slug, :43), S3 (`no-fall`, :52-55), S4 (spec subject always ` · to units`, :61-63), §4's `review_state` grammar (the sixth argument), AC11, or the new consumes-from edge on M4 (:110-111). wb21 reaches no surface of dl20 or fh17. wb21 is byte-identical between `443775a2f` and `ab976b5b3` (the `git diff` output is empty).

6. Parent text that looks wrong

None found.

Files read:
- C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-21.md
- C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dDeclaredLoop\spec\2026-10-24-spec-TOOL-dDeclaredLoop-32.md
- C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dDeclaredLoop\spec\2026-10-24-spec-TOOL-dDeclaredLoop-30.md
