# aEvidencedLens - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
refreshed-at: fd82e883102c570ea66f4f3244a92c70f7c19083 · park · 0 touching
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 32645a03d6d16676afbcbb48908ae620e6668967
phase: REVIEWING
branch-sha: 3640cf580d9df31e5cbe74be89024dd5a40e9f85
branch-ref: refs/heads/branch/spec-review-improvements-f59dad
spec-audit: 2026-10-05
may: none
mode: prompt
run-branch: refs/heads/branch/spec-review-improvements-f59dad
anchor-kind: run-branch
lease-utc: 2026-10-04T22:23:51Z
pid-image: claude.exe
host: compeeto-agent
pid: 20412
session: 6b5d9f56-af37-4095-82f4-be050a2179ba
keepalive: 15cbf130
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 028b5cac6504b37b99d83180b65bf211deb972b6
anchor-ref: refs/heads/main
base: 3640cf580d9df31e5cbe74be89024dd5a40e9f85

## Parked

2026-10-04T23:27:25Z rescope · item add TOOL-aEvidencedLens-12 · reason spec-audit round 1 (reviews/2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md) id 36 HIGH: unit 3 folds skeptic evidence through renderCell, which escapes every pipe, so a pipe-bearing evidence command reaches the skeptic altered and a true finding can be refuted; repairs TOOL-aEvidencedLens-3

2026-10-04T23:27:40Z rescope · item add TOOL-aEvidencedLens-13 · reason spec-audit round 1 (reviews/2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md) id 25 HIGH: unit 6 AC7 compares diff-kind prompts against an unbound base that predates unit 1's REVIEW_SHAPE move, so it is red on a correct build and invites undoing that move; repairs TOOL-aEvidencedLens-6

2026-10-04T23:27:46Z rescope · item add TOOL-aEvidencedLens-14 · reason spec-audit round 1 (reviews/2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md) id 37 HIGH: unit 9's round scan walks a terminal record's exclusions only on a grant-scan hit, so an owner REVIEW_ROUNDS raise merged into the run before its witness reds an archived record on every bar; repairs TOOL-aEvidencedLens-9

2026-10-04T23:32:23Z decision · item spec-audit promotion chain generation bound (round-1 spec audit finding 45, TOOL-aEvidencedLens-8 section 8 F3) · reason question: does a chain of spec-audit promotions need a bound beyond M4's precision rule, now that unit 8 promotes a minors batch on nearly every terminal round and unit 3 confirms at any severity, which raises the precision that must fall to end a chain (TOOL-aWokenSentinel-30 measured the cascade not converging); options: (a) close a spec-audit minors batch unit under M4's recorded specs-audited override instead of auditing it as a fresh subject, (b) leave M4 as it is and let the owner set a generation cap; refused because (a) rewrites M4, a governance carrier, and sets the owner's audit cost, which M3 veto 2 reserves to the owner

2026-10-04T23:37:07Z review · item aEvidencedLens-spec-set-r1 · reason verdict CLEAN · blockers 0 · CONVERGED · disposition promote

2026-10-04T23:39:15Z dispatch · item 7f714a32 TOOL-aEvidencedLens-1 · reason tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js tools/workflows/tier2-review.test.sh tools/workflows/unattended-build.test.sh tools/workflows/README.md memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-1.md

2026-10-04T23:39:21Z brief · item TOOL-aEvidencedLens-1 · reason 06fc74268f80 memory/builds/aEvidencedLens/prompts/2026-10-05-prompt-TOOL-aEvidencedLens-1-2-build-brief.md

2026-10-04T23:40:57Z dispatch · item e7e5feef TOOL-aEvidencedLens-1 · reason tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js tools/workflows/tier2-review.test.sh tools/workflows/unattended-build.test.sh tools/workflows/README.md memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-1.md

2026-10-04T23:47:44Z dispatch · item e7e5feef TOOL-aEvidencedLens-1 · reason tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js tools/workflows/tier2-review.test.sh tools/workflows/unattended-build.test.sh tools/workflows/README.md memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-1.md memory/builds/aEvidencedLens/README.md

2026-10-04T23:50:09Z dispatch · item c49655e6 TOOL-aEvidencedLens-2 · reason tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js tools/workflows/tier2-review.test.sh tools/workflows/unattended-build.test.sh memory/map/features/review-harnesses.md memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-2.md memory/builds/aEvidencedLens/README.md

2026-10-04T23:50:15Z brief · item TOOL-aEvidencedLens-2 · reason 1fe9a059f36c memory/builds/aEvidencedLens/prompts/2026-10-05-prompt-TOOL-aEvidencedLens-2-2-build-brief.md

2026-10-04T23:51:54Z dispatch · item 6eab527a TOOL-aEvidencedLens-2 · reason tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js tools/workflows/tier2-review.test.sh tools/workflows/unattended-build.test.sh memory/map/features/review-harnesses.md memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-2.md

2026-10-04T23:57:11Z dispatch · item 6eab527a TOOL-aEvidencedLens-2 · reason tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js tools/workflows/tier2-review.test.sh tools/workflows/unattended-build.test.sh memory/map/features/review-harnesses.md memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-2.md memory/builds/aEvidencedLens/README.md

2026-10-04T23:59:27Z dispatch · item bcd020ac TOOL-aEvidencedLens-3 · reason tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js tools/workflows/tier2-review.test.sh tools/workflows/unattended-build.test.sh memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-3.md memory/builds/aEvidencedLens/README.md

2026-10-04T23:59:32Z brief · item TOOL-aEvidencedLens-3 · reason b2c1be8f892c memory/builds/aEvidencedLens/prompts/2026-10-05-prompt-TOOL-aEvidencedLens-3-2-build-brief.md

2026-10-05T00:01:20Z dispatch · item 7a2d3f5f TOOL-aEvidencedLens-3 · reason tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js tools/workflows/tier2-review.test.sh tools/workflows/unattended-build.test.sh memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-3.md memory/builds/aEvidencedLens/README.md

2026-10-05T00:07:27Z dispatch · item d262cb8b TOOL-aEvidencedLens-4 · reason tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js tools/workflows/tier2-review.test.sh memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-4.md memory/builds/aEvidencedLens/README.md

2026-10-05T00:07:31Z brief · item TOOL-aEvidencedLens-4 · reason a40356c1bb64 memory/builds/aEvidencedLens/prompts/2026-10-05-prompt-TOOL-aEvidencedLens-4-2-build-brief.md

2026-10-05T00:08:50Z dispatch · item 55784614 TOOL-aEvidencedLens-4 · reason tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js tools/workflows/tier2-review.test.sh memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-4.md

2026-10-05T00:15:24Z dispatch · item 55784614 TOOL-aEvidencedLens-4 · reason tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js tools/workflows/tier2-review.test.sh memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-4.md memory/builds/aEvidencedLens/README.md

2026-10-05T00:17:03Z brief · item TOOL-aEvidencedLens-6 · reason 2cb8353145cb memory/builds/aEvidencedLens/prompts/2026-10-05-prompt-TOOL-aEvidencedLens-6-2-build-brief.md

2026-10-05T00:19:55Z dispatch · item 288622ce TOOL-aEvidencedLens-6 · reason tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js tools/workflows/tier2-review.test.sh tools/workflows/README.md memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md memory/builds/aEvidencedLens/README.md

2026-10-05T00:21:29Z dispatch · item 9f4101fe TOOL-aEvidencedLens-6 · reason tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js tools/workflows/tier2-review.test.sh tools/workflows/README.md memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md memory/builds/aEvidencedLens/README.md

2026-10-05T00:30:18Z dispatch · item 62a1cf2a TOOL-aEvidencedLens-6 · reason tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js tools/workflows/tier2-review.test.sh tools/workflows/README.md memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md memory/builds/aEvidencedLens/README.md memory/map/generated/symbols.json

2026-10-05T00:33:24Z dispatch · item 2704dbf0 TOOL-aEvidencedLens-5 · reason tools/workflows/unattended-build.template.js tools/workflows/unattended-build.js tools/workflows/unattended-build.test.sh tools/workflows/README.md memory/map/generated/symbols.json memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-5.md memory/builds/aEvidencedLens/README.md

2026-10-05T00:33:28Z brief · item TOOL-aEvidencedLens-5 · reason f050c40d95ce memory/builds/aEvidencedLens/prompts/2026-10-05-prompt-TOOL-aEvidencedLens-5-2-build-brief.md
