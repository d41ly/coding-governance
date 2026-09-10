# aLeakedHandle - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 9f93ac713bf854aa98859bceb81c2a95a07fbf99
phase: REVIEWING
branch-sha: eff1b6b15081355897038b3df3b9497d94f4b069
branch-ref: refs/heads/branch/full-bar-test-results-935278
mode: prompt
anchor-kind: run-branch
keepalive: dde7d163
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 013b1af9611570b3afd3ad99ba53e295e787b035
anchor-ref: refs/heads/main
base: eff1b6b15081355897038b3df3b9497d94f4b069

## Parked

2026-09-10T07:57:39Z review · item TOOL-aLeakedHandle-1 · reason verdict BLOCKED · blockers 1

2026-09-10T07:57:44Z review · item TOOL-aLeakedHandle-2 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-10T07:57:49Z review · item TOOL-aLeakedHandle-3 · reason verdict CLEAN · blockers 0 · CONVERGED

2026-09-10T08:43:19Z review · item TOOL-aLeakedHandle-1 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-10T08:43:58Z decision · item A spec whose review loop CONVERGED can still acquire a BLOCKER in fold text, and the driver refuses the round that would record it. Should the loop re-arm on a rev bump, or should a terminal subject's later blocker take a different route? · reason Observed on TOOL-aLeakedHandle-2 this run. Round 1 graded it CLEAN WITH FIXES at 0 blockers, so its loop recorded CONVERGED and terminated correctly per M4. The fold that answered round 1 then introduced new section 4 prose, and round 2 over that fold text confirmed a BLOCKER in it (D1: the admission rule reads seconds >= ceiling as proof the bound expired, but run-gates.sh:1393 sets bound=0 when the CEILINGS_LIVE probe fails, and the .leg row records no bound field, so a leg that ran unbounded and failed on its own is admitted as evidence - the exact failure-duration-as-floor case the ok-only filter existed to prevent). check 37 then refused --review for that subject because a terminal round exists. Three options seen. (1) Re-arm the loop on a rev bump: correct in principle and it rewrites what CONVERGED means, which is a method change. (2) Route the late blocker through M4's NON-CONVERGENT disposal instead, which is what this run did - the defect is a document defect so it FOLDS and terminates. (3) Leave it and rely on the closing diff review, which reads code and would not have caught a spec-prose defect before the code was written. Not mine: M3 veto 2 puts a governance-carrier change outside the mandate, and memory/guides/BUILD-METHOD.md M4 is the carrier. The gotcha class fold-text-is-unreviewed-surface is selected for exactly this diff and names the general shape; what it does not say is that the loop can be closed before the fold text exists.

2026-09-10T09:01:12Z dispatch · item 7269fda9 TOOL-aLeakedHandle-1 · reason tools/unattended/lib-unattended.sh tools/unattended/unattended.test.sh tools/gate-lint/kit.toml tools/gate-lint/sh_hygiene.py tools/gate-legs.json tools/run-gates/selftest-budgets.txt tools/govkit/subject-pins.tsv tools/dead-path-waivers.txt memory/project/substitution-fed-loops.txt memory/gotchas/bounded-through-a-pipe-is-unbounded.md memory/map/features/gate-lint.md memory/map/baseline.toml memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json

2026-09-10T09:01:37Z brief · item TOOL-aLeakedHandle-1 · reason 151bd90b2ab8 memory/builds/aLeakedHandle/prompts/2026-09-10-prompt-TOOL-aLeakedHandle-1-1-build-brief.md

2026-09-10T09:09:48Z dispatch · item 7269fda9 TOOL-aLeakedHandle-1 · reason tools/unattended/lib-unattended.sh tools/gate-lint/sh_hygiene.py tools/gate-lint/kit.toml tools/gate-lint/README.md tools/gate-legs.json tools/run-gates/selftest-budgets.txt tools/govkit/subject-pins.tsv tools/install-prefix-carried.txt tools/install-prefix-waivers.txt .memory-tree.conf memory/project/substitution-fed-loops.txt memory/gotchas/bounded-through-a-pipe-is-unbounded.md memory/map/features/gate-lint.md memory/map/baseline.toml memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json memory/LIVE.md memory/ledger/2026-09.md memory/builds/aLeakedHandle/README.md memory/builds/aLeakedHandle/spec memory/builds/aLeakedHandle/build

2026-09-10T09:27:35Z dispatch · item 7269fda9 TOOL-aLeakedHandle-1 · reason memory/gotchas/INDEX.md

2026-09-10T10:08:07Z dispatch · item 7269fda9 TOOL-aLeakedHandle-1 · reason memory/guides/SESSION-KICKOFF.md

2026-09-10T10:33:59Z dispatch · item 0aa54c96 TOOL-aLeakedHandle-1 · reason .unattended.conf

2026-09-10T10:34:25Z dispatch · item 0aa54c96 TOOL-aLeakedHandle-1 · reason memory/guides/SESSION-KICKOFF.md memory/builds/aLeakedHandle/spec memory/builds/aLeakedHandle/build memory/builds/aLeakedHandle/README.md memory/LIVE.md memory/ledger/2026-09.md tools/gate-lint/sh_hygiene.py

2026-09-10T10:52:00Z decision · item TOOL-aLeakedHandle-1's build commit c0964657 wrote memory/builds/aLeakedHandle/prompts/2026-09-10-prompt-TOOL-aLeakedHandle-1-1-build-brief.md, which no --dispatch row declared. check 23 REPORTS it and the unattended kit gate still exits 0 — it is one of 30 such lines across the corpus, so the class is reported and not gated. · reason Options seen: (a) declare the path now, which silences the report because check 23 unions rows per (anchor, unit) with no time ordering; (b) leave the report standing and record why. Taking (b). REFUSED (a) as the exact dodge the declare-before-you-write rule exists to prevent: a declaration written after the commit hides a write, and the brief's own text says narrowing after the fact is refused for that reason. The cause is that the file arrived STAGED before this pass began - the --brief verb stages it - so it was never in a set this pass composed, and the re-declaration that widened for .memory-tree.conf and the spec did not think to include it. The general shape is worth an owner turn: every build in the corpus that records a brief produces this line, which is why there are 30 of them, and a class 30 records deep is either a rule nobody can follow or a checker that should exclude what --brief itself stages.

2026-09-10T10:54:22Z dispatch · item 5c3c32e7 TOOL-aLeakedHandle-2 · reason tools/run-gates/derive-ceilings.py tools/run-gates/run-gates.evidence.test.sh tools/run-gates/ceiling-evidence.txt tools/gate-legs.json

2026-09-10T10:54:49Z brief · item TOOL-aLeakedHandle-2 · reason 4350847250da memory/builds/aLeakedHandle/prompts/2026-09-10-prompt-TOOL-aLeakedHandle-2-1-build-brief.md

2026-09-10T10:59:37Z dispatch · item 5c3c32e7 TOOL-aLeakedHandle-2 · reason tools/run-gates/derive-ceilings.py tools/run-gates/run-gates.evidence.test.sh tools/run-gates/ceiling-evidence.txt tools/gate-legs.json memory/builds/aLeakedHandle/spec memory/builds/aLeakedHandle/build memory/builds/aLeakedHandle/README.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-10T12:03:13Z dispatch · item 2489d058 TOOL-aLeakedHandle-3 · reason tools/run-gates/run-gates.sh tools/run-gates/run-gates.test.sh tools/run-gates/README.md memory/builds/aLeakedHandle/spec memory/builds/aLeakedHandle/build memory/builds/aLeakedHandle/README.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-10T12:03:34Z brief · item TOOL-aLeakedHandle-3 · reason 0aaede9bd899 memory/builds/aLeakedHandle/prompts/2026-09-10-prompt-TOOL-aLeakedHandle-3-1-build-brief.md

2026-09-10T12:22:11Z decision · item TOOL-aLeakedHandle-3 section 8 F1 says the fork is carried as a TOOL backlog row, and no such row exists in memory/backlog/TOOL.md · reason The fork was resolved by the delegated fold pass, not by this build pass, and memory/backlog is a SHARED_RECORDS member in .unattended.conf — --dispatch refuses a pass declaration that overlaps one, so this pass may not write the row and did not try. Options seen: widen the write set (refused by the verb, correctly); write it anyway outside the declaration (that is the exact act the shared-record rule exists to stop); park it. The row is owed by whichever commit next opens the shared records, and until it lands the spec's RESOLVED mark cites a record that is not there. The decision it records is unaffected: F1 stays out of this unit, all 104 legs in tools/gate-legs.json declare a ceiling, so the branch it would add would ship dead today.

2026-09-10T12:39:06Z dispatch · item 2489d058 TOOL-aLeakedHandle-3 · reason tools/run-gates/run-gates.sh tools/run-gates/run-gates.test.sh tools/run-gates/README.md memory/builds/aLeakedHandle/spec memory/builds/aLeakedHandle/build memory/builds/aLeakedHandle/README.md memory/LIVE.md memory/ledger/2026-09.md memory/guides/SESSION-KICKOFF.md

2026-09-10T13:13:19Z review · item aLeakedHandle · reason verdict BLOCKED · blockers 1

2026-09-10T14:16:22Z review · item aLeakedHandle · reason verdict BLOCKED · blockers 1 · NON-CONVERGENT · disposition fold
