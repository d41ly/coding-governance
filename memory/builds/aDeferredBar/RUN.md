# aDeferredBar - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
parked-surfaced: yes, 2 surfaced
keepalive-reaped: yes
witness: 8f2f9002ba4c28a1d470d649164463c35c2ca176
phase: VERIFYING
branch-sha: b2a330be17b8e195981002f3a5aa4b07d2256bd8
branch-ref: refs/heads/branch/unattended-build-gates-timing-4af880
mode: prompt
anchor-kind: run-branch
keepalive: ae19e8ee
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 7484d8d7b107c0357943345e11d9b1d9bc337bea
anchor-ref: refs/heads/main
base: b2a330be17b8e195981002f3a5aa4b07d2256bd8

## Parked

2026-09-13T21:09:57Z review · item aDeferredBar-spec-set · reason verdict BLOCKED · blockers 1

2026-09-13T22:45:56Z review · item aDeferredBar-spec-set · reason verdict CLEAN · blockers 0 · CONVERGED

2026-09-13T23:15:24Z dispatch · item 1447605b TOOL-aDeferredBar-1 · reason tools/workflows/unattended-unit.js tools/workflows/unattended-build.js tools/memory-tree/BUILD-METHOD.template.md memory/guides/BUILD-METHOD.md tools/memory-tree/check-memory-hygiene.sh tools/memory-tree/ANNOTATION-STYLE.template.md tools/memory-tree/HYGIENE.template.md tools/memory-tree/SPEC-TEMPLATE.template.md memory/HYGIENE.md memory/TEMPLATE-SPEC.md memory/guides/ANNOTATION-STYLE.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/unattended/unattended.sh tools/unattended/check-unattended.sh tools/unattended/check-pass-order.sh tools/unattended/check-brief-recorded.sh tools/unattended/PLAYBOOK-TEMPLATE.template.md tools/unattended/PROTOCOL.template.md tools/unattended/VERBS.template.md tools/unattended/playbook.fixture.template.md tools/unattended/README.md memory/guides/PLAYBOOK-TEMPLATE.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-VERBS.md tools/unattended/playbook.fixture.md memory/guides/SESSION-KICKOFF.md memory/builds/aDeferredBar/spec/2026-09-13-spec-TOOL-aDeferredBar-1.md memory/builds/aDeferredBar/build/2026-09-14-build-TOOL-aDeferredBar-1-2-acceptance-ledger.md memory/builds/aDeferredBar/README.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-13T23:15:54Z brief · item TOOL-aDeferredBar-1 · reason ed512fb6fd08 memory/builds/aDeferredBar/prompts/2026-09-14-prompt-TOOL-aDeferredBar-1-2-build-brief.md

2026-09-13T23:37:14Z dispatch · item 2ca014fd TOOL-aDeferredBar-2 · reason tools/check-spec-tokens.py tools/check-spec-tokens.test.sh .memory-tree.conf tools/memory-tree/.memory-tree.conf.example tools/memory-tree/SPEC-TEMPLATE.template.md memory/TEMPLATE-SPEC.md tools/memory-tree/check-memory-hygiene.sh tools/memory-tree/HYGIENE.template.md tools/memory-tree/BUILD-METHOD.template.md tools/memory-tree/ANNOTATION-STYLE.template.md memory/HYGIENE.md memory/guides/BUILD-METHOD.md memory/guides/ANNOTATION-STYLE.md memory/guides/SESSION-KICKOFF.md memory/map/features/spec-tokens.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json memory/builds/aDeferredBar/spec/2026-09-13-spec-TOOL-aDeferredBar-2.md memory/builds/aDeferredBar/build/2026-09-14-build-TOOL-aDeferredBar-2-1-acceptance-ledger.md memory/builds/aDeferredBar/README.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-13T23:37:37Z brief · item TOOL-aDeferredBar-2 · reason cbf8e6370636 memory/builds/aDeferredBar/prompts/2026-09-14-prompt-TOOL-aDeferredBar-2-2-build-brief.md

2026-09-14T00:15:45Z brief · item TOOL-aDeferredBar-3 · reason 9b456fc8426e memory/builds/aDeferredBar/prompts/2026-09-14-prompt-TOOL-aDeferredBar-3-2-build-brief.md

2026-09-14T00:17:40Z dispatch · item d59e7022 TOOL-aDeferredBar-3 · reason tools/unattended/gate-guard.js tools/unattended/gate-guard.fragment.json tools/unattended/gate-guard.test.sh .claude/settings.json tools/unattended/unattended.sh tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md tools/unattended/unattended.test.sh tools/unattended/adopt-unattended.test.sh tools/unattended/adopt-unattended.sh tools/unattended/kit.toml tools/run-gates/selftest-budgets.txt tools/install-prefix-carried.txt tools/unattended/README.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/unattended/check-unattended.sh tools/unattended/check-pass-order.sh tools/unattended/check-brief-recorded.sh tools/unattended/PLAYBOOK-TEMPLATE.template.md tools/unattended/VERBS.template.md tools/unattended/playbook.fixture.template.md tools/unattended/playbook.fixture.md memory/guides/PLAYBOOK-TEMPLATE.md memory/guides/UNATTENDED-VERBS.md memory/map/features/unattended.md memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/inventories.json memory/guides/SESSION-KICKOFF.md memory/builds/aDeferredBar/spec/2026-09-13-spec-TOOL-aDeferredBar-3.md memory/builds/aDeferredBar/build/2026-09-14-build-TOOL-aDeferredBar-3-1-acceptance-ledger.md memory/builds/aDeferredBar/build/2026-09-14-build-TOOL-aDeferredBar-3-2-corpus-measurement.md memory/builds/aDeferredBar/README.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-14T02:09:46Z review · item aDeferredBar · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-14T06:59:18Z decision · item Open a round 4 of the closing diff review over the round-3 fold? · reason Refused. Options seen: (a) a round 4 over 28f830bd..8f2f9002; (b) stop at three rounds. The loop converged at 0 blockers in rounds 1, 2 and 3; round 2 found 17 findings of which 3 were the round-1 fold certifying itself, round 3 found 9 of which 5 were the round-2 fold's own arms or comments, and every round-3 finding sits inside the hook's stated ceiling (textual, fail-open). The round-3 fold observed each arm RED-first on stdin, ran every direct check green, and the scoped bar was 48/48 before it. Fold text is unreviewed surface by construction, so a round 4 would review a fold and owe a round 5. Took (b); the residual left-shifts are TOOL-aDeferredBar-17..21.

2026-09-14T12:56:08Z decision · item Adopt the two tested edits that turn the four pre-existing red brief: arms of unattended.test.sh green, inside this build? · reason Refused. Options seen: (a) adopt under protocol section 11 as a rescoped unit — strictly beneficial, but proving nothing else the suite measures gets worse needs the 70-minute driver selftest run whole, twice, on a host another session was contending during this run's VERIFYING pass; (b) file the tested edits as a backlog row and land this build without them. Took (b): TOOL-aDeferredBar-22 carries both edits verbatim. The four arms are red on origin/main today and were born red at dBriefedPass, so this build makes them neither better nor worse.
