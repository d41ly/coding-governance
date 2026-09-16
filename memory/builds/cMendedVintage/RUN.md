# cMendedVintage - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 1f42235793aedbff4ab821b4dd777e404d345abb
phase: BUILDING
branch-sha: 859daa67e728ae273d5278536fb462c04077f16f
branch-ref: refs/heads/branch/govkit-update-rollbacks-0502c4
mode: prompt
run-branch: refs/heads/branch/govkit-update-rollbacks-0502c4
anchor-kind: run-branch
keepalive: 84ee75f8
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 4cf0944dbdce94714870f26760936bc5edabc64e
anchor-ref: refs/heads/main
base: 859daa67e728ae273d5278536fb462c04077f16f

## Parked

2026-09-16T12:43:39Z decision · item The charter's §16 R1 requires an emitted micro-format to be a markdown list item ('- ' at column 0), but skills/session-kickoff/manifest-check.sh:478 counts READY lines with grep -c '^READY — ', anchored at column 0 with no list marker. A card body that follows the charter is read as carrying NO ready line: the append reports success, leaves the 'READY — none yet' sentinel in place, skips the tree-cell re-render, and the scratch-guard then blocks the session's next commit. · reason Two options and both change a governance carrier, which M3 veto 2 reserves to the owner. Either §16 R1 gains an explicit carve-out for a machine-read on-disk record, or manifest-check.sh accepts an optional leading '- ' on the lines it anchors. I will not pick: the charter is the carrier this repo is most careful about, and the fix is one line either way. Observed live this run — it cost 71 minutes and a refused commit.

2026-09-16T12:43:51Z rescope · item add TOOL-cMendedVintage-9 · reason Building uncovered it: manifest-check.sh:128 resolves the session id by reading stdin for the SessionStart hook's JSON, guarded only by '[ -t 0 ]'. That covers the hook (pipe then EOF) and a human at a terminal, but not stdin being an open pipe that never sends EOF — which is what every tool-invoked shell has. --card --write then blocks in sed forever: measured 71 minutes at 4.4s CPU with no children, cleared instantly with '< /dev/null'. Passing --session does not avoid it, because the stdin read runs first and CARD_SID is only the fallback. The skill's own Step 5 prescribes this exact invocation as the card repair, so the documented remedy hangs. Strictly beneficial, no veto tripped (a kit engine, not a governance carrier), and it is a blocker between this run and its own landing.

2026-09-16T16:08:37Z review · item cMendedVintage-spec-set-r1 · reason verdict BLOCKED · blockers 1 · BOUNDED · disposition promote

2026-09-16T16:12:01Z rescope · item add DEPL-cMendedVintage-15 · reason promoted from review record 2026-09-16-review-cMendedVintage-spec-set-spec-audit-round1 finding B1 at severity blocker, disposed by BUILD-METHOD M4 which admits no other route for a blocker or a high

2026-09-16T16:12:03Z rescope · item add DEPL-cMendedVintage-16 · reason promoted from review record 2026-09-16-review-cMendedVintage-spec-set-spec-audit-round1 finding H1 at severity high, disposed by BUILD-METHOD M4 which admits no other route for a blocker or a high

2026-09-16T16:12:06Z rescope · item add DEPL-cMendedVintage-17 · reason promoted from review record 2026-09-16-review-cMendedVintage-spec-set-spec-audit-round1 finding H2 at severity high, disposed by BUILD-METHOD M4 which admits no other route for a blocker or a high

2026-09-16T16:12:09Z rescope · item add DEPL-cMendedVintage-18 · reason promoted from review record 2026-09-16-review-cMendedVintage-spec-set-spec-audit-round1 finding H3 at severity high, disposed by BUILD-METHOD M4 which admits no other route for a blocker or a high

2026-09-16T16:12:11Z rescope · item add DEPL-cMendedVintage-19 · reason promoted from review record 2026-09-16-review-cMendedVintage-spec-set-spec-audit-round1 finding H4 at severity high, disposed by BUILD-METHOD M4 which admits no other route for a blocker or a high

2026-09-16T16:12:14Z rescope · item add DEPL-cMendedVintage-20 · reason promoted from review record 2026-09-16-review-cMendedVintage-spec-set-spec-audit-round1 finding H5 at severity high, disposed by BUILD-METHOD M4 which admits no other route for a blocker or a high

2026-09-16T16:12:16Z rescope · item add DEPL-cMendedVintage-21 · reason promoted from review record 2026-09-16-review-cMendedVintage-spec-set-spec-audit-round1 finding H6 at severity high, disposed by BUILD-METHOD M4 which admits no other route for a blocker or a high

2026-09-16T17:15:48Z decision · item unattended-build.js's disposal reconciliation compares disposed ROWS against raw CONFIRMED findings, so a legitimate synthesis-time merge of two raw findings into one row reports DEGRADED and withholds the roster. Hit live this run: 14 confirmed collapsed to 13 rows because raw 14 and raw 25 were the same defect on the same two sentences of DEPL-cMendedVintage-10, reached from two directions. Every finding WAS disposed - 7 promoted with specs and rescope rows on disk, 6 folded as rev-2 bumps with section 9 lines - and I verified both halves by hand before proceeding. · reason The obvious fix, relaxing the equality, is NOT strictly beneficial: that arithmetic is the only thing standing between a dropped finding and a roster handed out as if nothing were missing, and relaxing it makes a real drop invisible. The correct fix is for the synthesis stage to emit an explicit merge map the reconciliation can consume, which is a design change in another kit and outside this build's goal. So this is neither an adoption nor a backlog row I may mint: a cMendedVintage id for work this build will not do would put a specless unit in its own roster and block build-complete. Owner decides.

2026-09-16T17:20:45Z dispatch · item 09c9415a TOOL-cMendedVintage-9 · reason skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh

2026-09-16T17:21:24Z brief · item TOOL-cMendedVintage-9 · reason 3b5378a72ff0 memory/builds/cMendedVintage/prompts/2026-09-16-prompt-TOOL-cMendedVintage-9-2-build-brief.md

2026-09-16T17:22:15Z dispatch · item 09c9415a TOOL-cMendedVintage-9 · reason skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh memory/builds/cMendedVintage/spec/2026-09-16-spec-TOOL-cMendedVintage-9.md

2026-09-16T17:29:04Z dispatch · item 09c9415a TOOL-cMendedVintage-9 · reason skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh memory/builds/cMendedVintage/spec/2026-09-16-spec-TOOL-cMendedVintage-9.md memory/builds/cMendedVintage/README.md memory/builds/cMendedVintage/build/2026-09-16-build-TOOL-cMendedVintage-9-acceptance-ledger.md memory/guides/SESSION-KICKOFF.md

2026-09-16T17:36:36Z dispatch · item 1900b591 DEPL-cMendedVintage-1 · reason tools/govkit/govkit.py tools/govkit/selftest.py

2026-09-16T17:36:37Z brief · item DEPL-cMendedVintage-1 · reason aa8c0a836794 memory/builds/cMendedVintage/prompts/2026-09-16-prompt-DEPL-cMendedVintage-1-2-build-brief.md

2026-09-16T17:39:29Z dispatch · item 1900b591 DEPL-cMendedVintage-1 · reason tools/govkit/govkit.py tools/govkit/selftest.py WIRE-INTO-PROJECT.md memory/builds/cMendedVintage/spec/2026-09-16-spec-DEPL-cMendedVintage-1.md

2026-09-16T17:48:17Z dispatch · item 56055917 DEPL-cMendedVintage-1 · reason tools/govkit/govkit.py tools/govkit/selftest.py WIRE-INTO-PROJECT.md tools/workflows/README.md memory/builds/cMendedVintage/spec/2026-09-16-spec-DEPL-cMendedVintage-1.md

2026-09-16T17:51:24Z dispatch · item 03ba97f1 DEPL-cMendedVintage-2 · reason tools/govkit/govkit.py tools/govkit/selftest.py

2026-09-16T17:51:25Z brief · item DEPL-cMendedVintage-2 · reason d4e603c689f7 memory/builds/cMendedVintage/prompts/2026-09-16-prompt-DEPL-cMendedVintage-2-2-build-brief.md

2026-09-16T17:54:56Z dispatch · item 03ba97f1 DEPL-cMendedVintage-2 · reason tools/govkit/govkit.py tools/govkit/selftest.py WIRE-INTO-PROJECT.md memory/builds/cMendedVintage/spec/2026-09-16-spec-DEPL-cMendedVintage-2.md memory/LIVE.md

2026-09-16T18:05:59Z dispatch · item 03ba97f1 DEPL-cMendedVintage-2 · reason tools/govkit/govkit.py tools/govkit/selftest.py WIRE-INTO-PROJECT.md memory/builds/cMendedVintage/spec/2026-09-16-spec-DEPL-cMendedVintage-2.md memory/builds/cMendedVintage/README.md memory/LIVE.md
