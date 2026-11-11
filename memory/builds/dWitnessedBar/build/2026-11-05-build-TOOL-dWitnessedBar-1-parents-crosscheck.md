**Serves:** research TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-21

# dWitnessedBar's specs against the parent revisions it had not read: a read-only cross-check

Node d, 2026-11-05, base `ab976b5b3` (origin/main). dWitnessedBar's last cross-read was `443775a2f`. Since then `git log 443775a2f..ab976b5b3 -- memory/builds/<parent>/spec/` over its parents (dDeclaredLoop) names `63669d505` (2026-11-02, TOOL-dFoldedAudit-8: TOOL-dDeclaredLoop-20 and -32 to rev-3, TOOL-dFairHearing-17 to rev-4), generated-region rewrites and the no-op merge `e5de11e9e` apart. The owner asked for this pass on 2026-11-05, after a verification found these revisions unread. This record is not an audit: no spec was edited by it; it found no mismatch, so no re-ground brief is owed.

**Counts:** 3 assumptions · 3 AGREES · 0 MISMATCH · 0 UNKNOWN UNTIL BUILT, over 1 spec with rows. No spec holds a MISMATCH. By rule: none.

## Method

- **Population by citation.** `grep -P` over `spec/*.md` outside the generated regions, for the three revised units as `TOOL-<build>-<n>`, a bare `<build>-<n>`, a continuation list or a `dl`/`fh` alias: 1 spec, 21 (dl32 at :76).
- **Population by rule.** The SA probe (`review_state`, `no-fall`, `NON-CONVERGENT`, `non-decrease`, `strict fall`, `precision floor`, `until-clean`, `review.design.rounds`, `promotion_target`, `item.review.dispose`, `chain stop`, `review.max-rounds`, `review.follow-up`, `rework budget`) named no spec but 21. The rules: **SA**, the spec-audit rules: a spec subject takes `no-fall`, ends at its target or bound and is promoted ` · to units`; dl20's dispose row folds a local finding on an unbuilt spec; a chain's stop is BUILD-METHOD M4's derived verdict (dl32:47-63, dl20:86-89, :128, fh17:64-65).
- **Readers.** One `gov-spec-reviewer` agent, read-only, one per group of the brief [`2026-11-05-prompt-TOOL-dWitnessedBar-1-parents-crosscheck`](../prompts/2026-11-05-prompt-TOOL-dWitnessedBar-1-parents-crosscheck.md), their handoffs beside it (group A, led by spec 21). Their returns, every MISMATCH's both sides quoted with its `Change:` and `Cause:`, are [`2026-11-05-build-TOOL-dWitnessedBar-1-crosscheck-returns`](2026-11-05-build-TOOL-dWitnessedBar-1-crosscheck-returns.md).
- **The main loop** assembled the table below from the returns' tables by script, stable-sorted by spec, and derived the counts from it. It re-read both sides of the rows the re-ground brief names and changed no verdict.
- **Aliases:** `wbN:L` is line L of this build's spec N; `dlN:L`, `fhN:L`, `trN:L`, `prN:L`, `ksN:L`, `brN:L` and `llN:L` of dDeclaredLoop's, dFairHearing's, dTotalRecall's, dPlacedRequest's, dKeptSession's, dBoundRoles' and dLinkedLibrary's spec N; all at `ab976b5b3`.
- **What it does not check:** the rules an earlier re-ground applied (R1 to R9 of dWellOiledMachine's 2026-10-28 brief), read by this build's 2026-10-26 cross-read; anything a parent's build run decides. dOrderedCharter's and dFairHearing's live build runs on node a were not read, only their specs on main. The probes are a text heuristic. No skeptic re-ran the verdicts; the writer re-reads both sides before it edits.
- **The fork fold.** A sibling session was folding the owner's picks on the chain's 47 open forks while the readers ran. Rows are read at `ab976b5b3`; the re-ground re-checks every row that fold moved before it edits.

## Summary table

| # | Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|---|
| 1 | 21 | dl32 owns a `--fix-pass` loop, and wb21 leaves the counting of fix passes to it (wb21:75-76, §3 non-goal) | cite | AGREES | wb21:75-76 "Counting fix passes against a budget: TOOL-dDeclaredLoop-30's `flow.rework-budget` draw and TOOL-dDeclaredLoop-32's `--fix-pass` loop." dl32:64-71 S5 still reads "The fix-pass loop. A verb `--fix-pass <slug> --unit <id> --reds <N>` records one fix pass … as a `fix-pass` row through `park()`". `git show 63669d505` has no S5 hunk. |
| 2 | 21 | That fix-pass loop keeps a budget-bound exit (strict fall, bounds, and a promotion target from the budget), so it can be the place where counting against a budget lives | SA | AGREES | dl32:21-22 "every fix pass against one acceptance red ends at the first round whose blocker and high count does not strictly fall". dl32:51-52 "The non-decrease test keeps reading the blocker and high count on the build slug and on a fix pass." dl32:69-70 "Its target is `promotion_target`'s answer as it stands, ` · to units` or ` · to on-exhausted`". The rev-3 log, dl32:378-380, says "follow-ups and fix passes keep the rule". |
| 3 | 21 | dl30's `flow.rework-budget` draw counts fix passes (wb21:75) | cite | AGREES | dl30:47 lists `fix-pass` among the closed draw causes. dl30:55 "`fix-pass` for a dispatch of a unit whose earlier pass committed". `git log 443775a2f..ab976b5b3` names no dl30 revision, apart from the e5de11e9e no-op merge. |

## What the one spec relies on

wb21:75-76 leaves the counting of fix passes to dl30's `flow.rework-budget` draw and dl32's `--fix-pass` loop. dl32 rev-3 keeps strict fall and budget routing for fix passes (dl32:21-22, :51-52, the rev-3 line at :378-380), so all three rows read AGREES. wb21 is byte-identical between `443775a2f` and `ab976b5b3`.

## For the re-ground

None owed: the pass found no MISMATCH, no UNKNOWN UNTIL BUILT and no parent text that looks wrong. No dWitnessedBar spec is revised.

## After the re-ground

The owner's fork fold landed on origin/main at `11ebd1e87` after the readers ran, and this branch fast-forwarded to it before any spec was edited. Row 3 cites TOOL-dDeclaredLoop-30, which the fold and this re-ground both revised; it still reads AGREES, since the `flow.rework-budget` draw still counts fix passes and only a spec subject's `review-round` draw stopped ending its loop.

No spec of this build is revised: its three rows agree, and the re-ground wrote no brief for it.
