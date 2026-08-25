# dCarriedReceipt - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: cb5c7901fad3b9598c2ffef7636a89d8b65a4d2d
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
