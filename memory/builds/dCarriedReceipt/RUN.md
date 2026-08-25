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
