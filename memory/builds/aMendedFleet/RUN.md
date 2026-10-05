# aMendedFleet - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 0c1b078160d534884082f13029fd4ba86de23846
phase: BUILDING
branch-sha: 7af5f564641d231f8b78f6b183dde1b6bf53111d
branch-ref: refs/heads/branch/coding-governance-review-1460c9
may: none
mode: prompt
run-branch: refs/heads/branch/coding-governance-review-1460c9
anchor-kind: run-branch
lease-utc: 2026-10-04T17:55:59Z
pid-image: claude.exe
host: compeeto-agent
pid: 4344
session: f1d79f53-d62b-4e17-bc23-00d6c2d7114d
keepalive: 02179d97
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 35438ba0a188cf38c1d73b6e1df7b3a1342a17de
anchor-ref: refs/heads/main
base: 7af5f564641d231f8b78f6b183dde1b6bf53111d

## Parked

2026-10-04T17:56:18Z decision · item Update the Claude Code CLI on node a (claude update): the PATH CLI is 2.1.178 · reason Options: the owner runs it, or a run does. Refused: it changes the installed toolchain on the owner's machine, an act outside the repository and outside any mandate a build folder can grant. Report [B#40].

2026-10-04T17:56:21Z decision · item Register the out-of-process resume tick (gov-resume-tick) on node a's OS scheduler · reason Options: the owner registers it per the unattended kit README, or a run does. Refused: it creates a persistent OS scheduled task, standing configuration on the owner's machine that a run may not create. One run sat 13.3 h with no driver call. Report [B#13]; unit 61 makes the missing tick loud.

2026-10-04T17:56:23Z decision · item Reverse owner ruling D11-c so a remote ruleset can bind unattended landings, and move runs to --permission-mode auto · reason Options: keep direct-push landing; or reverse D11-c, add a non-admin run credential and a GitHub ruleset, then switch to auto mode once the CLI is 2.1.281 or later. Refused: reversing a ratified owner ruling and changing repository protection settings are owner acts. Report [B#41], roadmap item 21.

2026-10-04T17:56:25Z decision · item Label about 30 closing-review findings by hand so review precision is calibrated against a human · reason Options: the owner spends about an hour labelling, scored through tools/workflows/review_replay.py; or skip calibration. Refused: the labels ARE the owner's judgement; a run supplying them would grade itself. Report [B#44], roadmap item 19.

2026-10-04T17:56:28Z decision · item Run the /goal spike in an interactive session, and retire the idle-wake machinery if it holds · reason Options: spike /goal attended and delete idle-wake plus register/release-task if it covers the silent-background case; or keep the machinery. Refused: in -p sessions /goal delivers check-ins only at turn end, so only an interactive owner session can measure it. Report [B#42], roadmap item 24.

2026-10-04T18:40:36Z rescope · item add TOOL-aMendedFleet-81 · reason split from TOOL-aMendedFleet-22 at its F1: the shard renderer and the merge attribute share no file and are two mechanisms, and this build's rule is one per spec

2026-10-04T19:01:23Z rescope · item retire TOOL-aMendedFleet-30 · reason the live aGraftedHelix build owns supersession labels in recall as its unit 4 (SPECCED rev-2, ratified 2026-10-04); a second copy here would conflict with it at landing

2026-10-04T19:01:37Z rescope · item add TOOL-aMendedFleet-82 · reason split from TOOL-aMendedFleet-34 at its F2: the HEAD field changes the served query path, a second mechanism

2026-10-04T19:01:40Z rescope · item add TOOL-aMendedFleet-83 · reason split from TOOL-aMendedFleet-37 at its F1: the close block lives in the unattended kit with its own conf declaration

2026-10-04T19:26:57Z rescope · item add TOOL-aMendedFleet-84 · reason discovered at speccing: an 83-unit roster's generated README regions pass check 6's cap; adopted under protocol section 11 — the build cannot land without it

2026-10-04T19:26:59Z rescope · item add TOOL-aMendedFleet-85 · reason split from TOOL-aMendedFleet-39 at its F1: a second mechanism in another file

2026-10-04T19:27:02Z rescope · item add TOOL-aMendedFleet-86 · reason split from TOOL-aMendedFleet-39 at its F1: a second mechanism in another file

2026-10-04T19:27:04Z rescope · item add TOOL-aMendedFleet-87 · reason split from TOOL-aMendedFleet-42 at its F1: a second mechanism with its own readers

2026-10-04T19:27:07Z rescope · item add TOOL-aMendedFleet-88 · reason split from TOOL-aMendedFleet-42 at its F1: a second mechanism with its own readers

2026-10-04T19:27:10Z rescope · item add TOOL-aMendedFleet-89 · reason split from TOOL-aMendedFleet-43 at its F1: dossier prose edits, disjoint from the card renderer

2026-10-04T19:27:12Z rescope · item add TOOL-aMendedFleet-90 · reason split from TOOL-aMendedFleet-51 at its F1: the DEAD-for-N rule needs unit 48's history

2026-10-04T19:27:23Z rescope · item retire TOOL-aMendedFleet-45 · reason the live aGraftedHelix build owns the invariants registry as reviewers' default by-design source (its unit 3, ratified 2026-10-04); the report itself says make it the one source and drop a second pipeline

2026-10-04T19:54:38Z rescope · item add TOOL-aMendedFleet-91 · reason split from TOOL-aMendedFleet-57 at its F1: a spec-header grammar change apart from the low-water grade

2026-10-04T19:54:41Z rescope · item add TOOL-aMendedFleet-92 · reason split from TOOL-aMendedFleet-62 at its F1: check 23's range mode and budget are a hygiene-gate mechanism apart from the history legs

2026-10-04T19:54:43Z rescope · item add TOOL-aMendedFleet-93 · reason split from TOOL-aMendedFleet-67 at its F1: the A/B experiment and the default it sets follow the agent type

2026-10-04T20:15:11Z rescope · item add PLAY-aMendedFleet-3 · reason split from TOOL-aMendedFleet-69 at its F1: a charter-template clause is a governance-carrier edit apart from the kit's warning

2026-10-04T20:15:14Z rescope · item add TOOL-aMendedFleet-94 · reason split from TOOL-aMendedFleet-74 at its F1: path-scoped rules and the pre-build checklist are two mechanisms

2026-10-04T20:15:16Z rescope · item add KICK-aMendedFleet-4 · reason split from KICK-aMendedFleet-2 at its F1: the stale-CLI note is a second card line with its own reader

2026-10-04T20:15:19Z rescope · item add PLAY-aMendedFleet-4 · reason split from PLAY-aMendedFleet-1 at its F1: the registry dedup is a separate edit from the wrapper trim

2026-10-04T20:58:20Z brief · item TOOL-aMendedFleet-1 · reason ca9f6d277d8a memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-04T20:59:28Z dispatch · item d3695f29 TOOL-aMendedFleet-1 · reason tools/unattended/unattended.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-1.md memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-1-1-acceptance-ledger.md memory/LIVE.md memory/guides/SESSION-KICKOFF.md

2026-10-04T21:09:13Z dispatch · item d3695f29 TOOL-aMendedFleet-1 · reason tools/unattended/unattended.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-1.md memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-1-1-acceptance-ledger.md memory/LIVE.md memory/guides/SESSION-KICKOFF.md memory/builds/aMendedFleet/README.md

2026-10-04T21:10:34Z brief · item TOOL-aMendedFleet-2 · reason ca9f6d277d8a memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-04T21:15:45Z dispatch · item b93c1133 TOOL-aMendedFleet-2 · reason memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-2-1-acceptance-ledger.md memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-2-2-merge-census.md memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-2.md memory/builds/aMendedFleet/README.md memory/LIVE.md

2026-10-04T21:18:15Z brief · item TOOL-aMendedFleet-3 · reason ca9f6d277d8a memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-04T21:21:45Z dispatch · item bbcae380 TOOL-aMendedFleet-3 · reason tools/lexicon/lexicon.py tools/lexicon/selftest.py tools/lexicon/README.md .githooks/pre-push .githooks/pre-push.test.sh .githooks/pre-push.runlog.test.sh tools/push-main.sh tools/push-main.test.sh memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-3.md memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-3-1-acceptance-ledger.md memory/builds/aMendedFleet/README.md memory/LIVE.md

2026-10-04T21:36:27Z brief · item TOOL-aMendedFleet-4 · reason ca9f6d277d8a memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-04T21:37:53Z dispatch · item 703dae10 TOOL-aMendedFleet-4 · reason tools/govkit/matrix.py memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-4.md

2026-10-04T21:40:27Z dispatch · item 703dae10 TOOL-aMendedFleet-4 · reason tools/govkit/matrix.py memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-4.md memory/builds/aMendedFleet/README.md

2026-10-04T21:41:49Z dispatch · item 91a09113 TOOL-aMendedFleet-4 · reason tools/govkit/matrix.py memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-4.md memory/builds/aMendedFleet/README.md memory/project/encoding-posture-sites.txt

2026-10-04T21:44:26Z dispatch · item 2b06daf1 TOOL-aMendedFleet-3 · reason tools/lexicon/selftest.py

2026-10-04T21:44:59Z brief · item TOOL-aMendedFleet-5 · reason ca9f6d277d8a memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-04T21:46:10Z dispatch · item c410904e TOOL-aMendedFleet-5 · reason tools/memory-tree/transition_audit.py tools/memory-tree/transition-audit.test.sh memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-5.md

2026-10-04T21:49:31Z dispatch · item c410904e TOOL-aMendedFleet-5 · reason tools/memory-tree/transition_audit.py tools/memory-tree/transition-audit.test.sh memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-5.md memory/builds/aMendedFleet/README.md

2026-10-04T21:50:51Z brief · item TOOL-aMendedFleet-6 · reason ca9f6d277d8a memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-04T21:52:31Z dispatch · item a3f63d19 TOOL-aMendedFleet-6 · reason tools/lexicon/lexicon_conf.py tools/lexicon/selftest.py memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-6.md memory/LIVE.md

2026-10-04T21:54:28Z dispatch · item a3f63d19 TOOL-aMendedFleet-6 · reason tools/lexicon/lexicon_conf.py tools/lexicon/selftest.py memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-6.md memory/LIVE.md memory/builds/aMendedFleet/README.md

2026-10-04T21:55:42Z brief · item TOOL-aMendedFleet-7 · reason ca9f6d277d8a memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-04T21:57:41Z dispatch · item b566f345 TOOL-aMendedFleet-7 · reason memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-7-1-held-red-census.md memory/builds/aMendedFleet/README.md memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-7.md

2026-10-04T22:08:42Z rescope · item add TOOL-aMendedFleet-97 · reason held-red census cause C1 (TOOL-aMendedFleet-7): Python stdio follows the hosted runner's cp1252 code page, so a child's em dash reaches a UTF-8 reader as 0x97 and a printed check mark cannot encode; nine held suites

2026-10-04T22:08:45Z rescope · item add TOOL-aMendedFleet-98 · reason held-red census cause C2 (TOOL-aMendedFleet-7): a Python suite spawns bare bash, which Windows resolves to the System32 WSL launcher before Git-Bash on PATH; lexicon selftest

2026-10-04T22:08:48Z rescope · item add TOOL-aMendedFleet-99 · reason held-red census cause C3 (TOOL-aMendedFleet-7): the held job runs from actions/checkout on D: while the bar job clones to the primary-tree path; manifest-check and process-monitor adopter

2026-10-04T22:08:50Z rescope · item add TOOL-aMendedFleet-100 · reason held-red census cause C4 (TOOL-aMendedFleet-7): a check-unattended fixture commits in a bare origin with no identity and the runner has no global git identity; gate shard 2/8

2026-10-04T22:09:00Z rescope · item add TOOL-aMendedFleet-101 · reason held-red census cause C5 (TOOL-aMendedFleet-7): the G0 fixture's sed lines still write tools/lander-granted.sh where its greps expect bin/lander-granted.sh; gate shard 8/8

2026-10-04T22:09:03Z rescope · item add TOOL-aMendedFleet-102 · reason held-red census cause C6 (TOOL-aMendedFleet-7): the inline resolve_kit_dir blocks in backlog.py and transition_audit.py drifted from tools/lib/resolve_kit_dir.py; python resolver

2026-10-04T22:09:06Z rescope · item add TOOL-aMendedFleet-103 · reason held-red census cause C7 (TOOL-aMendedFleet-7): corpus_ids.py reads GRAMMAR_WHERE through globals() and the hygiene suite's python-parity arm does not exempt it; memory-hygiene self-test

2026-10-04T22:09:09Z rescope · item add TOOL-aMendedFleet-104 · reason held-red census cause C8 (TOOL-aMendedFleet-7): review_replay.py --selftest neither prints the foreign-prefix probe marker nor is declared a whole run; foreign-prefix parity

2026-10-04T22:09:12Z rescope · item add TOOL-aMendedFleet-105 · reason held-red census cause C9 (TOOL-aMendedFleet-7): the census live-tree arm's kill is refused Permission denied on the runner in two of three runs with no tree change between; process-monitor census

2026-10-04T22:12:03Z dispatch · item b566f345 TOOL-aMendedFleet-7 · reason memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-7-1-held-red-census.md memory/builds/aMendedFleet/README.md memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-7.md memory/LIVE.md memory/ledger/2026-10.md

2026-10-04T22:41:55Z brief · item TOOL-aMendedFleet-8 · reason ca9f6d277d8a memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-04T22:43:47Z dispatch · item b82db0e0 TOOL-aMendedFleet-8 · reason tools/drift-audit/drift_report.py tools/drift-audit/drift_signals.py tools/drift-audit/drift_signals.template.py tools/drift-audit/selftest.py tools/drift-audit/README.md memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-8.md

2026-10-04T22:52:40Z dispatch · item b82db0e0 TOOL-aMendedFleet-8 · reason tools/drift-audit/drift_report.py tools/drift-audit/drift_signals.py tools/drift-audit/drift_signals.template.py tools/drift-audit/selftest.py tools/drift-audit/README.md memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-8.md memory/builds/aMendedFleet/README.md

2026-10-04T22:55:51Z brief · item TOOL-aMendedFleet-9 · reason ca9f6d277d8a memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-04T23:00:24Z dispatch · item e0907712 TOOL-aMendedFleet-9 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md tools/unattended/README.md tools/unattended/.unattended.conf.example tools/unattended/kit.toml .unattended.conf memory/guides/SESSION-KICKOFF.md memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-9.md memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-9-1-acceptance-ledger.md memory/builds/aMendedFleet/README.md memory/LIVE.md memory/ledger/2026-10.md memory/map/generated/symbols.json

2026-10-04T23:18:31Z brief · item TOOL-aMendedFleet-97 · reason ca9f6d277d8a memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-04T23:25:06Z brief · item TOOL-aMendedFleet-10 · reason ca9f6d277d8a memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-04T23:28:12Z dispatch · item 693f1055 TOOL-aMendedFleet-10 · reason tools/memory-tree/gen_build_index.py tools/memory-tree/backlog.py tools/memory-tree/README.md memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-10.md memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-10-1-acceptance-ledger.md

2026-10-04T23:37:25Z dispatch · item 693f1055 TOOL-aMendedFleet-10 · reason tools/memory-tree/gen_build_index.py tools/memory-tree/backlog.py tools/memory-tree/README.md memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-10.md memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-10-1-acceptance-ledger.md memory/builds/aMendedFleet/README.md

2026-10-04T23:41:35Z brief · item TOOL-aMendedFleet-11 · reason ca9f6d277d8a memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-04T23:44:58Z dispatch · item 1df0632e TOOL-aMendedFleet-11 · reason tools/workflows/REVIEW-PROTOCOL.template.md memory/guides/REVIEW-PROTOCOL.md tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-11.md

2026-10-04T23:47:55Z dispatch · item 1df0632e TOOL-aMendedFleet-11 · reason tools/workflows/REVIEW-PROTOCOL.template.md memory/guides/REVIEW-PROTOCOL.md tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-11.md memory/builds/aMendedFleet/README.md

2026-10-04T23:50:03Z brief · item TOOL-aMendedFleet-12 · reason ca9f6d277d8a memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-04T23:55:58Z dispatch · item 51d942a4 TOOL-aMendedFleet-12 · reason tools/memory-tree/gen_build_index.py tools/memory-tree/README.md tools/memory-tree/.memory-tree.conf.example .memory-tree.conf memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-12.md memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-12-1-acceptance-ledger.md memory/guides/SESSION-KICKOFF.md memory/builds/aMendedFleet/README.md

2026-10-05T00:08:54Z dispatch · item a22f3d72 TOOL-aMendedFleet-12 · reason .memory-tree.conf memory/LIVE.md memory/guides/SESSION-KICKOFF.md

2026-10-05T00:10:56Z brief · item TOOL-aMendedFleet-13 · reason ca9f6d277d8a memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md
