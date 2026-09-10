# aLeakedHandle - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 7269fda93629d45a4c41d8888f9fb47b1f644115
phase: BUILDING
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
