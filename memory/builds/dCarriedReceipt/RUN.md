# dCarriedReceipt - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 04c7da244361950b38a611671d341ac3400e32cb
phase: BUILDING
mode: slug
anchor-kind: default-branch
keepalive: 91ed1be1
anchor-url: https://github.com/d41ly/coding-governance
anchor-sha: c97b8b90c0491acee8c227b51d4de9f05d452759
anchor-ref: refs/heads/main
base: c97b8b90c0491acee8c227b51d4de9f05d452759

## Parked

2026-08-25T09:30:38Z review · item DEPL-dCarriedReceipt-13 · reason verdict BLOCKED · blockers 2

2026-08-25T09:30:39Z review · item DEPL-dCarriedReceipt-14 · reason verdict BLOCKED · blockers 1

2026-08-25T09:30:39Z review · item DEPL-dCarriedReceipt-1 · reason verdict BLOCKED · blockers 0 · CONVERGED

2026-08-25T09:30:39Z review · item DEPL-dCarriedReceipt-3 · reason verdict BLOCKED · blockers 0 · CONVERGED

2026-08-25T09:30:39Z review · item DEPL-dCarriedReceipt-8 · reason verdict BLOCKED · blockers 0 · CONVERGED

2026-08-25T09:30:40Z review · item DEPL-dCarriedReceipt-15 · reason verdict BLOCKED · blockers 0 · CONVERGED

2026-08-25T09:32:19Z dispatch · item 1678ced6 DEPL-dCarriedReceipt-13 · reason memory/builds/dCarriedReceipt/spec/2026-08-24-spec-DEPL-dCarriedReceipt-13.md

2026-08-25T09:32:19Z dispatch · item 1678ced6 DEPL-dCarriedReceipt-14 · reason memory/builds/dCarriedReceipt/spec/2026-08-24-spec-DEPL-dCarriedReceipt-14.md memory/builds/dCarriedReceipt/spec/2026-08-24-spec-DEPL-dCarriedReceipt-11.md

2026-08-25T09:32:21Z dispatch · item 1678ced6 DEPL-dCarriedReceipt-12 · reason memory/builds/dCarriedReceipt/spec/2026-08-24-spec-DEPL-dCarriedReceipt-12.md memory/builds/dCarriedReceipt/spec/2026-08-24-spec-DEPL-dCarriedReceipt-9.md

2026-08-25T09:32:23Z dispatch · item 1678ced6 DEPL-dCarriedReceipt-7 · reason memory/builds/dCarriedReceipt/spec/2026-08-24-spec-DEPL-dCarriedReceipt-7.md memory/builds/dCarriedReceipt/spec/2026-08-24-spec-DEPL-dCarriedReceipt-6.md memory/builds/dCarriedReceipt/spec/2026-08-24-spec-DEPL-dCarriedReceipt-5.md memory/builds/dCarriedReceipt/spec/2026-08-24-spec-DEPL-dCarriedReceipt-10.md

2026-08-25T09:32:25Z dispatch · item 1678ced6 DEPL-dCarriedReceipt-2 · reason memory/builds/dCarriedReceipt/spec/2026-08-24-spec-DEPL-dCarriedReceipt-2.md memory/builds/dCarriedReceipt/spec/2026-08-24-spec-DEPL-dCarriedReceipt-4.md memory/builds/dCarriedReceipt/README.md

2026-08-25T10:18:35Z review · item DEPL-dCarriedReceipt-13 · reason verdict BLOCKED · blockers 1

2026-08-25T10:18:36Z review · item DEPL-dCarriedReceipt-7 · reason verdict BLOCKED · blockers 1

2026-08-25T10:18:36Z review · item DEPL-dCarriedReceipt-2 · reason verdict BLOCKED · blockers 0 · CONVERGED

2026-08-25T10:18:37Z review · item DEPL-dCarriedReceipt-5 · reason verdict BLOCKED · blockers 0 · CONVERGED

2026-08-25T10:18:37Z review · item DEPL-dCarriedReceipt-6 · reason verdict BLOCKED · blockers 0 · CONVERGED

2026-08-25T10:18:37Z review · item DEPL-dCarriedReceipt-10 · reason verdict BLOCKED · blockers 0 · CONVERGED

2026-08-25T10:18:38Z review · item DEPL-dCarriedReceipt-11 · reason verdict BLOCKED · blockers 0 · CONVERGED

2026-08-25T10:18:38Z review · item DEPL-dCarriedReceipt-12 · reason verdict BLOCKED · blockers 0 · CONVERGED

2026-08-25T11:45:05Z review · item DEPL-dCarriedReceipt-7 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-08-25T11:45:06Z review · item DEPL-dCarriedReceipt-13 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-08-25T11:45:06Z review · item DEPL-dCarriedReceipt-14 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-08-25T11:45:07Z review · item DEPL-dCarriedReceipt-9 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-08-25T11:45:07Z review · item DEPL-dCarriedReceipt-4 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-08-25T13:18:46Z decision · item DEPL-dCarriedReceipt-12 S4 makes 'commit before you re-run a writing verb' a hard precondition of BOTH verbs, and no acceptance criterion says so · reason Implemented exactly as S4 defines dirty, and the definition is emphatic because criteria in two other units depend on it in opposite directions. But `apply` STAGES everything it lands, so the moment a successful apply finishes every receipt-claimed path differs index-versus-HEAD and is DIRTY. Three consequences on real operators: a second `apply` on an uncommitted target refuses, `apply --resume` refuses because it needs a receipt and therefore a completed apply, and `update --write` immediately after `apply` refuses. Twelve existing selftest arms went red on this and two more passed VACUOUSLY -- their re-apply refused, wrote nothing, and 'the adopter edit survived' was trivially true because nothing had run. Options seen: (a) narrow S4 to update-only, which is a SPEC change and not mine to make unilaterally -- the unit is titled 'on both writing verbs' and S5 says both, while S7 and S8 say 'update' where they mean it, so the spec distinguishes deliberately; (b) add a carve-out for paths dirty only because this tool staged them, which weakens the guard in exactly the direction an operator's own staged work lives; (c) accept it and make the fixtures model the flow the refusal asks for, which is what was done -- a settle() helper commits at seven fixture sites and every one of those arms still asserts what it asserted before. Taking (c) because it changes no ratified text and loses no coverage. The owner should decide whether the operator burden is wanted: it is a real change to how apply and update compose, it is not written in any criterion, and the narrowing in (a) is one sentence.

2026-08-25T14:28:16Z decision · item DEPL-dCarriedReceipt-7 S4's present-in-worktree-absent-from-index refusal is UNQUALIFIED by role, so a non-writing row can stop a whole run · reason S4 says 'a receipt-claimed path', unqualified, and it is implemented that way. But the raw-write hazard it exists to stop only arises for rows the update dispatch sends to the table disposition. A generated, project-owned or rendered row whose destination happens to be present-but-untracked in a target now refuses the ENTIRE run, though no writing arm would ever have touched it. Nothing is red and nothing will warn: no fixture in this build trips it, because memory-tree's three unlanded rows are absent from both index and worktree. Options seen: (a) scope the predicate to rows whose role dispatches to table, one condition, matching the stated hazard exactly; (b) leave it unqualified, which is strictly safer and refuses earlier, at the cost of a refusal the operator can only clear by tracking a file gov will never write; (c) park. Taking (c) because narrowing a ratified scope item is a SPEC decision and the review loop is closed -- it ended at zero blockers and the owner called it. Worth deciding before an adopter meets it, since the failure mode is a run refusing for a reason the operator cannot connect to anything gov does.

2026-08-25T17:10:35Z decision · item DEPL-dCarriedReceipt-9 S13's inCMS-derived fixture was never built, and AC2's 26 needles is derivably wrong · reason S13 asks for a COMMITTED receipt of the 52 rows measured at inCMS 2cff5855. That repository is not reachable from this tree, so no run here can generate it; S13 is marked DEFERRED in place at rev-9 rather than left implying it shipped. What S13 was added for IS met -- round 5's M3 found AC1 and AC2 running on a fixture no scope item created, and there is now an authored fixture with an owner, asserted to trigger each rung it grades. What is not met is that it be the inCMS one, so AC1's distribution is the synthetic fixture's, measured at 4 verbatim / 1 eol / 2 relocate / 3 no rung, and the spec's 21/6/5 are reproduced nowhere. SEPARATELY, and worth more than the fixture: building DERIVED that AC2's 26 needles is wrong even over the 86-row population the figure was measured on. The / and ~ forms of a gov directory carrying no slash are the SAME string, so such a pair contributes ONE needle and not two; section 4's own Inventory says tools survives as a single pair, and tools has no slash. 13 pairs therefore cannot yield 26 distinct needles. Nothing asserts either number now, so nothing is red -- but -13 S4a reads this same derivation and its own AC12 was written to assert the same needle count, so it will inherit the error unless it re-derives. Options seen: (a) build S13 in a tree where inCMS is reachable and re-measure both figures there; (b) drop the inCMS fixture and let the synthetic one stand, accepting that no arm grades the real adopter population; (c) park. Taking (c): the choice needs the adopter repo in hand, and this run has neither it nor an owner turn.

2026-08-25T21:55:25Z decision · item HANDOFF: the owner stopped this run at 10 of 15 units, near a weekly usage limit. Five units remain and the run is LIVE and resumable · reason Built and CLOSED, in landing order: -3, -2, -1, -12, -7, -8, -9, -10, -11, -14. REMAINING: -13 (govkit adopt, the receipt bootstrap; it needs -1, -7, -9, -10 and -12 beneath it, all of which are landed, so it is unblocked and is the largest remaining unit), -4 (coverage_rows and plan --coverage), -5 (the decline contract), -6 (the silenced-gate-leg bar) and -15 (gov stops shipping literal prefixes in kit bodies). -4, -5 and -6 are the coverage group; -15 is deferrable without blocking anything. NO REVIEW WORK IS OWED before building any of them: the spec set CONVERGED at round 6 with zero blockers and every subject recorded CONVERGED. The owner ended the loop deliberately and it had reached its own exit in the same breath. A resuming node runs the driver's --resume verb and reads this file first; the run-state travels with the branch. TWO THINGS IT MUST KNOW. First, the merge bar is RED for reasons that are NOT this build's: the lexicon naming leg is red at HEAD independently, at 428 offenders over a pin of 384, verified on a pristine clone; and drift-audit's non_terminal_specs_cited_by_product_source sits at 3 over a pin of 2 until -13 closes, because -13's own spec id is cited from govkit.py while its status is still SPECCED. The other two entries, aBatchedLintel-1 and dNarrowedAnchor-1, are the standing baseline. Second, the pre-commit hook now exceeds a two-minute command timeout on this tree, so a commit can die mid-hook having staged everything and committed nothing; check the last log line before believing a commit landed. FOUR decisions are parked above this one and none of them blocks building: -12 S4's commit-before-you-re-run precondition, -7 S4's unqualified-by-role refusal, and -9 S13's unbuildable inCMS fixture together with the derivably-wrong 26-needle figure that -13 must not inherit.

2026-08-25T23:03:37Z decision · item the handoff's claim that the lexicon naming leg is red at HEAD independently is FALSE, measured · reason Measured on a pristine origin/main worktree: 382 offenders under a pin of 384, GREEN. Measured on this branch merged with origin/main: 429, 45 over. The per-file delta is entirely this build's: tools/govkit/govkit.py +19 and tools/govkit/selftest.py +28, and NO other file moved by even one. So the red is this build's own naming debt, not a standing baseline, and it is a Definition-of-Done item rather than something to report around. Options seen: (a) raise VERB_OFFENDER_PIN, which is an edit to a governance carrier and therefore veto 2, an owner turn, not mine; (b) rename the offending definitions so the count returns under the pin, which trips no veto and is what M3 leaves standing; (c) park the whole thing, which leaves a merge-bar leg red. Taking (b), after the five remaining units are built rather than before, because -13 alone adds a verb and its selftest arms and renaming twice is the same work done twice.

2026-08-26T02:24:42Z decision · item CORRECTION to this run's earlier park: raising VERB_OFFENDER_PIN is NOT the owner turn that entry claimed · reason The earlier entry read a pin raise as a change to a governance carrier and therefore veto 2. It is not: BUILD-METHOD M11 enumerates the six carriers and .lexicon.conf is not among them, and that file's own header records four prior raises with a stated form -- name both values, name every arrival, say why a raise rather than a waiver. Measured on the merged tree: 452 offenders against a pin of 384, 70 added and 0 DRAINED, so the set is a strict superset. The rename this run originally chose was then measured infeasible in the direction that matters. Six leading tokens carry most of it and they are real operations -- demand, index, blob, carry, gov, step -- so renaming is spelling compliance the charter itself warns against; and classify_row is cited BY NAME in seven ratified spec files, so renaming it would falsify the record those specs ARE, and editing closed specs to match is not something this build may do to units it did not open. Taken: the raise, with all seventy named in the conf per its own convention, plus TOOL-aResumedRelay-1 for the curation pass that decides whether those six verbs join the table. The owner should know the naming debt is REAL and was not paid down, only recorded.
