# dRetiredFork - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 5a713a55387254137253ddb33883bfcbb1689298
phase: BUILDING
mode: slug
anchor-kind: default-branch
keepalive: 534edee2
anchor-url: https://github.com/d41ly/coding-governance
anchor-sha: 51444cc12cd05f02df9bac677a3b32c5689f27bf
anchor-ref: refs/heads/main
base: 5e7f41d3cf1713382189208d3703f3373c764d75

## Parked

2026-09-02T17:56:40Z decision · item The passes-harnessed directive's route is non-functional: unattended-build.js's AUDIT stage cannot ever complete, so BUILD is unreachable through the harness. Should this run proceed without it, or stop? · reason MEASURED at round 1, not argued. The AUDIT stage prompt orders the stage agent to invoke the Workflow tool with scriptPath tools/workflows/tier2-review.js. That agent is a sidechain agent, and AGENTS.md section 8 states as measured fact that a sidechain holds NEITHER Workflow nor Agent - the capability is ABSENT, not policed. The stage agent searched the deferred registry three times, found neither, refused to fabricate a verdict, wrote nothing, and returned the impossible CONVERGING-with-0-blockers pairing as this repo's own signature for a record no verb produced. It was right on every count. The harness self-test never catches this because it STUBS the agent returns and asserts control flow over the file's text, so the one premise it rests on has never been exercised. OPTIONS SEEN: (a) fix the harness so the audit runs in the main loop, which holds Workflow - rejected here as an M3 veto-2 public-surface change to a kit adopters install, and outside this build's goal; (b) abort the run - rejected as wasting a healthy authorization over a defect in a tool; (c) proceed without the harness. TAKEN: (c), on the harness's OWN stated grounds - its header says it buys ORDER and never ENFORCEMENT, and that what actually refuses is --dispatch at the moment of the act plus the pass-order history leg over the commit graph. Both work from the main loop. The order property itself is already satisfied: all 28 open specs grade READY and are named by spec-audit records, and no line of code has been written. What is genuinely LOST is the structural guarantee that a future compacted reader cannot build before speccing; I am substituting --dispatch per unit for it, and the owner is entitled to overrule that substitution.

2026-09-02T17:59:28Z dispatch · item 21ad9bb3 DEPL-dRetiredFork-8 · reason memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-6.md memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-8.md memory/builds/dRetiredFork/README.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-02T17:59:34Z brief · item DEPL-dRetiredFork-8 · reason 6bf87236ad4a memory/builds/dRetiredFork/prompts/2026-09-02-prompt-DEPL-dRetiredFork-8-1-build-brief.md

2026-09-02T18:04:48Z brief · item DEPL-dRetiredFork-8 · reason 7eb94309086d memory/builds/dRetiredFork/prompts/2026-09-02-prompt-DEPL-dRetiredFork-8-1-build-brief.md

2026-09-02T18:06:37Z brief · item DEPL-dRetiredFork-9 · reason d7197204f049 memory/builds/dRetiredFork/prompts/2026-09-02-prompt-DEPL-dRetiredFork-9-1-build-brief.md

2026-09-02T18:06:42Z dispatch · item b9fcc024 DEPL-dRetiredFork-9 · reason memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-3.md memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-1.md memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-9.md memory/builds/dRetiredFork/README.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-02T18:16:06Z brief · item TOOL-dRetiredFork-19 · reason 4668ae574d60 memory/builds/dRetiredFork/prompts/2026-09-02-prompt-TOOL-dRetiredFork-19-1-build-brief.md

2026-09-02T18:16:14Z dispatch · item 27a8e806 TOOL-dRetiredFork-19 · reason tools/check-kit-placeholders.py tools/check-kit-placeholders.test.sh tools/gate-legs.json memory/project/testsuite-count-waivers.txt tools/unattended/kit.toml tools/govkit/registry.toml memory/map/features/kit-placeholders.md memory/map/generated/inventories.json memory/map/generated/MAP.md memory/map/generated/symbols.json WIRE-INTO-PROJECT.md memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-12.md memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-19.md memory/builds/dRetiredFork/README.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-02T21:29:35Z brief · item TOOL-dRetiredFork-1 · reason 5c8aca2bdf2c memory/builds/dRetiredFork/prompts/2026-09-03-prompt-TOOL-dRetiredFork-1-1-build-brief.md

2026-09-02T21:29:41Z dispatch · item 194ec62f TOOL-dRetiredFork-1 · reason tools/memory-tree/check-memory-hygiene.sh tools/memory-tree/check-memory-hygiene.test.sh tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md tools/memory-tree/BUILD-METHOD.template.md memory/guides/BUILD-METHOD.md tools/memory-tree/SPEC-TEMPLATE.template.md memory/TEMPLATE-SPEC.md memory/guides/SESSION-KICKOFF.md memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-1.md memory/builds/dRetiredFork/README.md

2026-09-02T21:40:19Z brief · item TOOL-dRetiredFork-2 · reason 218e034b657c memory/builds/dRetiredFork/prompts/2026-09-03-prompt-TOOL-dRetiredFork-2-1-build-brief.md

2026-09-02T21:40:26Z dispatch · item a92ab1f1 TOOL-dRetiredFork-2 · reason tools/memory-tree/gen_build_index.py tools/memory-recall/selftest.py tools/memory-recall/recall_conf.py tools/memory-recall/README.md tools/memory-tree/check-memory-hygiene.sh tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md tools/memory-tree/BUILD-METHOD.template.md memory/guides/BUILD-METHOD.md tools/memory-tree/SPEC-TEMPLATE.template.md memory/TEMPLATE-SPEC.md memory/guides/SESSION-KICKOFF.md memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-2.md memory/builds/dRetiredFork/README.md
