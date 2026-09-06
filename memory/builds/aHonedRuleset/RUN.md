# aHonedRuleset - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
parked-surfaced: yes, 1 surfaced
keepalive-reaped: yes
witness: 84383ffd78a1e8fee9207b15d1f050b68a0e339e
phase: LANDING
mode: slug
anchor-kind: default-branch
keepalive: 62177af0
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 6ec402bd3eb7f9cb5ce6257b0f60348ae3e593fc
anchor-ref: refs/heads/main
base: 6ec402bd3eb7f9cb5ce6257b0f60348ae3e593fc

## Parked

2026-09-05T22:58:28Z review · item TOOL-aHonedRuleset-2 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-05T22:58:33Z review · item TOOL-aHonedRuleset-3 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-05T22:58:39Z review · item TOOL-aHonedRuleset-4 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-05T22:58:46Z review · item TOOL-aHonedRuleset-5 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-05T22:58:52Z review · item TOOL-aHonedRuleset-6 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-05T23:38:30Z review · item TOOL-aHonedRuleset-8 · reason verdict BLOCKED · blockers 2

2026-09-06T00:12:12Z review · item TOOL-aHonedRuleset-8 · reason verdict BLOCKED · blockers 1

2026-09-06T00:53:42Z review · item TOOL-aHonedRuleset-8 · reason verdict BLOCKED · blockers 1 · NON-CONVERGENT · disposition fold

2026-09-06T01:43:46Z dispatch · item 1e352f9d TOOL-aHonedRuleset-3 · reason tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md skills/session-kickoff/SKILL.md tools/unattended/check-unattended.sh tools/unattended/check-unattended.test.sh tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md .unattended.conf tools/unattended/.unattended.conf.example tools/memory-tree/BUILD-METHOD.template.md memory/guides/BUILD-METHOD.md memory/guides/SESSION-KICKOFF.md

2026-09-06T01:44:17Z brief · item TOOL-aHonedRuleset-3 · reason 744fd41d496d memory/builds/aHonedRuleset/spec/2026-09-04-spec-TOOL-aHonedRuleset-3.md

2026-09-06T13:28:56Z brief · item TOOL-aHonedRuleset-3 · reason ec4e6e194c19 memory/builds/aHonedRuleset/spec/2026-09-04-spec-TOOL-aHonedRuleset-3.md

2026-09-06T13:29:01Z brief · item TOOL-aHonedRuleset-5 · reason 36a4b8a1e0cb memory/builds/aHonedRuleset/spec/2026-09-04-spec-TOOL-aHonedRuleset-5.md

2026-09-06T16:02:33Z review · item aHonedRuleset · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-06T21:21:46Z decision · item The merge bar cannot go green on this branch: tools/drift-audit/drift_report.py --check exits 1 at BASE 6ec402bd and at HEAD, on two signals this build did not cause — .lexicon.conf's LANGS ratchet moved .sh parser->dark with no justification beside it, and closed_specs_with_no_product_commit sits at 2 against a pin of 1. Should this run fix another build's ratchet to land, or land on an override naming them? · reason REFUSED to fix them. Both are outside this build's stated goal, and the .lexicon.conf ratchet is a governance-carrier declaration owned by whoever weakened it, which M3 veto 2 puts beyond a delegated resolver. Widening a prose-trim build into someone else's ratchet repair would answer an open question that is not this build's, which is exactly what this build's own README forbids. The alternative considered and rejected: raising the drift pins, which weakens a shrink-only ratchet to make a red look green and is the one move the signal exists to prevent. Landing therefore goes through a gates-green override that NAMES both signals and records that each reproduces at base, so the next reader can tell a pre-existing red from one this build introduced. Verified by running the leg in a scratch worktree at 6ec402bd: exit 1 there, exit 1 here, and the two entries are the same two.

2026-09-06T21:22:07Z brief · item TOOL-aHonedRuleset-3 · reason 9b7bbd89fb33 memory/builds/aHonedRuleset/spec/2026-09-04-spec-TOOL-aHonedRuleset-3.md

2026-09-06T21:22:08Z brief · item TOOL-aHonedRuleset-5 · reason 438ecaa24bcd memory/builds/aHonedRuleset/spec/2026-09-04-spec-TOOL-aHonedRuleset-5.md

2026-09-06T23:18:58Z override · item gates-green · reason 1 of 43 legs failed and it is drift-audit records, which is RED AT BASE. Verified by running it in a scratch worktree at 6ec402bd: exit 1 there, exit 1 here, and the two entries are the same two — the .lexicon.conf LANGS ratchet weakened (.sh parser->dark) with no justification beside it, and closed_specs_with_no_product_commit at 2 against a pin of 1. Neither is this build's: git log over .lexicon.conf across 6ec402bd..HEAD is empty. This run introduced two drift regressions of its own and FIXED both — a stale trace-waiver row, and a product-source citation of a still-SPECCED sibling spec — so the leg is back to exactly the base failure set. Fixing what remains means editing another build's ratchet declaration, which M3 veto 2 puts beyond a delegated resolver, and raising the pins would weaken a shrink-only ratchet to make a red look green. Parked as a decision for the owner. Every other leg is green: 43 ran, 1 failed, 1 skipped. Self-tests are HELD by explicit owner directive mid-run, and unit 4 AC12 and unit 8 AC10 record that as a SKIP in their acceptance ledgers rather than as a pass.

2026-09-06T23:18:58Z override · item specs-audited · reason The one unaudited unit is TOOL-aHonedRuleset-1, and its code was written and CLOSED before this run began. It is a Tier-1 prose census whose deliverable is a report and a re-runnable script, landed by an earlier session at a commit predating this run's BASE. M4 requires a spec audit BEFORE the unit's code is written, which is not satisfiable retroactively — auditing its design now would grade a decision already shipped and would be a record of a review that could change nothing. Every unit this run actually BUILT was audited before its code: units 2, 3, 4, 5 and 6 through two rounds (round 1 BLOCKED with 3 blockers, round 2 CLEAN WITH FIXES with 0), and unit 8 through three (2 blockers, then 1, then 1 — non-convergent, so the loop stopped and the surviving blocker was DISPOSED by fold, recorded on its --review row). Nothing this run built is unaudited.
