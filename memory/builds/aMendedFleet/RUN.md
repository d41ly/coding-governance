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

2026-10-05T00:15:24Z dispatch · item 4c5e5ffc TOOL-aMendedFleet-13 · reason tools/memory-tree/gen_build_index.py tools/memory-tree/kit.toml tools/memory-tree/README.md tools/memory-tree/.memory-tree.conf.example memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-13.md memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-13-1-acceptance-ledger.md memory/builds/aMendedFleet/README.md

2026-10-05T00:25:31Z dispatch · item 3bb291a9 TOOL-aMendedFleet-13 · reason .memory-tree.conf memory/LIVE.md memory/guides/SESSION-KICKOFF.md

2026-10-05T00:27:52Z brief · item TOOL-aMendedFleet-14 · reason ca9f6d277d8a memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T00:30:05Z decision · item TOOL-aMendedFleet-14 has no triage ask id to hold its aged unlabelled asks on · reason Options: the main loop mints one TOOL-aMendedFleet ask id for the triage ask and writes it into this unit's brief, then re-dispatches; or a child mints it. Refused: the unit's spec (design step 1 and its consumes-from edge) parks a pass whose brief names no minted id, and fan-out children never mint ids under template section 2, since only the orchestrator holds the family high-water. Nothing was built or dispatched.

2026-10-05T00:32:33Z brief · item TOOL-aMendedFleet-14 · reason ad4bf7f9b3ec memory/builds/aMendedFleet/prompts/2026-10-05-prompt-TOOL-aMendedFleet-14-1-build-brief.md

2026-10-05T00:34:44Z dispatch · item 7604b576 TOOL-aMendedFleet-14 · reason memory/builds/aMendedFleet/BACKLOG.md memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-14.md memory/builds/aMendedFleet/README.md memory/backlog/TOOL.md memory/backlog/DEPL.md

2026-10-05T00:40:28Z brief · item TOOL-aMendedFleet-15 · reason ca9f6d277d8a memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T00:42:45Z dispatch · item 11d332ee TOOL-aMendedFleet-15 · reason tools/drift-audit/drift_signals.py memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-15.md memory/LIVE.md

2026-10-05T00:50:06Z dispatch · item 11d332ee TOOL-aMendedFleet-15 · reason tools/drift-audit/drift_signals.py memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-15.md memory/builds/aMendedFleet/README.md

2026-10-05T00:54:31Z brief · item TOOL-aMendedFleet-16 · reason ca9f6d277d8a memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T00:56:58Z dispatch · item 6f72841a TOOL-aMendedFleet-16 · reason tools/memory-tree/gotchas.py tools/memory-tree/README.md memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-16.md memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-16-1-acceptance-ledger.md memory/LIVE.md

2026-10-05T01:02:17Z dispatch · item 6f72841a TOOL-aMendedFleet-16 · reason tools/memory-tree/gotchas.py tools/memory-tree/README.md memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-16.md memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-16-1-acceptance-ledger.md memory/LIVE.md memory/builds/aMendedFleet/README.md

2026-10-05T01:04:23Z brief · item TOOL-aMendedFleet-17 · reason ca9f6d277d8a memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T01:07:41Z dispatch · item 43243f9c TOOL-aMendedFleet-17 · reason tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js tools/workflows/README.md tools/workflows/tier2-review.test.sh memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-17.md memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-17-1-acceptance-ledger.md memory/LIVE.md memory/builds/aMendedFleet/README.md

2026-10-05T01:14:29Z brief · item TOOL-aMendedFleet-18 · reason ca9f6d277d8a memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T01:16:59Z dispatch · item 074db83a TOOL-aMendedFleet-18 · reason tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js tools/workflows/README.md memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-18.md

2026-10-05T01:20:06Z dispatch · item 074db83a TOOL-aMendedFleet-18 · reason tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js tools/workflows/README.md tools/workflows/tier2-review.test.sh memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-18.md memory/LIVE.md memory/builds/aMendedFleet/README.md

2026-10-05T01:27:41Z brief · item TOOL-aMendedFleet-19 · reason ca9f6d277d8a memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T01:32:10Z dispatch · item 586b7b48 TOOL-aMendedFleet-19 · reason tools/memory-tree/gen_build_index.py tools/memory-tree/README.md memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-19.md memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-19-1-acceptance-ledger.md memory/builds/aMendedFleet/README.md

2026-10-05T01:43:33Z brief · item TOOL-aMendedFleet-20 · reason ca9f6d277d8a memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T01:48:09Z dispatch · item 5014c3ac TOOL-aMendedFleet-20 · reason tools/memory-tree/gen_build_index.py tools/memory-tree/check-memory-hygiene.sh tools/memory-tree/check-memory-hygiene.test.sh tools/memory-tree/README.md memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-20.md memory/guides/SESSION-KICKOFF.md memory/builds/aMendedFleet/README.md

2026-10-05T01:56:11Z brief · item TOOL-aMendedFleet-21 · reason ca9f6d277d8a memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T01:59:15Z dispatch · item e24fd0d1 TOOL-aMendedFleet-21 · reason tools/drift-audit/drift_report.py tools/drift-audit/drift_signals.py tools/drift-audit/drift_signals.template.py tools/drift-audit/README.md tools/drift-audit/selftest.py memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-21.md memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-21-1-acceptance-ledger.md memory/builds/aMendedFleet/README.md

2026-10-05T02:10:31Z brief · item TOOL-aMendedFleet-22 · reason ca9f6d277d8a memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T02:14:24Z dispatch · item 99a9a09f TOOL-aMendedFleet-22 · reason .gitattributes tools/check-wiring.sh tools/check-wiring.test.sh tools/memory-tree/README.md WIRE-INTO-PROJECT.md memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-22.md memory/LIVE.md memory/ledger/2026-10.md

2026-10-05T02:19:14Z dispatch · item 99a9a09f TOOL-aMendedFleet-22 · reason .gitattributes tools/check-wiring.sh tools/check-wiring.test.sh tools/memory-tree/README.md WIRE-INTO-PROJECT.md memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-22.md memory/builds/aMendedFleet/README.md

2026-10-05T02:24:43Z brief · item TOOL-aMendedFleet-23 · reason ca9f6d277d8a memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T02:27:52Z dispatch · item 741ed948 TOOL-aMendedFleet-23 · reason tools/memory-tree/gotchas.py tools/memory-tree/check-memory-hygiene.sh tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-23.md memory/guides/SESSION-KICKOFF.md memory/LIVE.md memory/ledger/2026-10.md

2026-10-05T02:32:44Z dispatch · item 741ed948 TOOL-aMendedFleet-23 · reason tools/memory-tree/gotchas.py tools/memory-tree/check-memory-hygiene.sh tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-23.md memory/guides/SESSION-KICKOFF.md memory/builds/aMendedFleet/README.md

2026-10-05T02:36:01Z brief · item TOOL-aMendedFleet-24 · reason ca9f6d277d8a memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T02:43:49Z brief · item TOOL-aMendedFleet-24 · reason 37e2c28ec58f memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T02:46:38Z dispatch · item d1b72876 TOOL-aMendedFleet-24 · reason tools/memory-tree/corpus_ids.py tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-24.md memory/LIVE.md

2026-10-05T02:52:57Z dispatch · item d1b72876 TOOL-aMendedFleet-24 · reason tools/memory-tree/corpus_ids.py tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-24.md memory/builds/aMendedFleet/README.md

2026-10-05T02:55:02Z brief · item TOOL-aMendedFleet-25 · reason 37e2c28ec58f memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T02:59:00Z dispatch · item 063a4ca5 TOOL-aMendedFleet-25 · reason tools/check-spec-tokens.py tools/check-spec-tokens.test.sh tools/template-size-limits.txt tools/template-size-highwater.txt memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-25.md

2026-10-05T03:05:07Z dispatch · item 063a4ca5 TOOL-aMendedFleet-25 · reason tools/check-spec-tokens.py tools/check-spec-tokens.test.sh tools/template-size-limits.txt tools/template-size-highwater.txt memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-25.md memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-25-1-acceptance-ledger.md memory/builds/aMendedFleet/README.md memory/LIVE.md

2026-10-05T03:13:06Z brief · item TOOL-aMendedFleet-26 · reason 37e2c28ec58f memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T03:17:18Z dispatch · item fe3aa324 TOOL-aMendedFleet-26 · reason tools/memory-tree/tree_lib.py tools/memory-tree/corpus_ids.py tools/memory-tree/gen_build_index.py tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-26.md

2026-10-05T03:26:37Z dispatch · item fe3aa324 TOOL-aMendedFleet-26 · reason tools/memory-tree/tree_lib.py tools/memory-tree/corpus_ids.py tools/memory-tree/gen_build_index.py tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-26.md memory/builds/aMendedFleet/README.md

2026-10-05T03:33:37Z dispatch · item b717013a TOOL-aMendedFleet-26 · reason memory/gotchas/record-citing-a-foreign-id-defines-or-orphans-it.md memory/gotchas/INDEX.md

2026-10-05T03:35:26Z brief · item TOOL-aMendedFleet-27 · reason 37e2c28ec58f memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T03:39:17Z dispatch · item 902e8408 TOOL-aMendedFleet-27 · reason tools/memory-recall/recall_conf.py tools/memory-recall/extract.py tools/memory-recall/selftest.py tools/memory-recall/README.md .memory-tree.conf memory/guides/SESSION-KICKOFF.md memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-27.md memory/LIVE.md

2026-10-05T03:44:35Z dispatch · item 902e8408 TOOL-aMendedFleet-27 · reason tools/memory-recall/recall_conf.py tools/memory-recall/extract.py tools/memory-recall/selftest.py tools/memory-recall/README.md .memory-tree.conf memory/guides/SESSION-KICKOFF.md memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-27.md memory/LIVE.md memory/builds/aMendedFleet/README.md memory/map/generated/symbols.json

2026-10-05T03:47:58Z brief · item TOOL-aMendedFleet-28 · reason 37e2c28ec58f memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T03:52:29Z dispatch · item 0278aa1f TOOL-aMendedFleet-28 · reason tools/memory-recall/check-recall.py tools/memory-recall/recall-fixture.json tools/memory-recall/test_recall_floor.py tools/memory-recall/README.md .memory-tree.conf memory/guides/SESSION-KICKOFF.md memory/map/features/memory-recall.md memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-28.md memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-28-1-acceptance-ledger.md memory/LIVE.md memory/builds/aMendedFleet/README.md

2026-10-05T04:02:00Z dispatch · item 0278aa1f TOOL-aMendedFleet-28 · reason tools/memory-recall/check-recall.py tools/memory-recall/recall-fixture.json tools/memory-recall/test_recall_floor.py tools/memory-recall/README.md .memory-tree.conf memory/guides/SESSION-KICKOFF.md memory/map/features/memory-recall.md memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-28.md memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-28-1-acceptance-ledger.md memory/LIVE.md memory/builds/aMendedFleet/README.md memory/backlog/TOOL.md

2026-10-05T04:07:12Z dispatch · item 8e84f7ff TOOL-aMendedFleet-28 · reason tools/memory-recall/query.py tools/memory-recall/selftest.py

2026-10-05T04:09:58Z brief · item TOOL-aMendedFleet-29 · reason 37e2c28ec58f memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T04:14:29Z dispatch · item 3eff0503 TOOL-aMendedFleet-29 · reason tools/memory-recall/check-recall.py tools/memory-recall/test_recall_floor.py tools/memory-recall/README.md memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-29.md memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-29-1-acceptance-ledger.md memory/builds/aMendedFleet/README.md memory/LIVE.md

2026-10-05T04:23:56Z decision · item TOOL-aMendedFleet-29 spec-probe labels have had no human check · reason Options: the owner hand-checks every harvested label before any figure is quoted or pinned; or the 20-question agent spot-check stands alone. The agent spot-check kept 5 of 20, so the hit@10 figure is noisy. Refused: checking every label is an owner act, which spec section 8 F2 parks.

2026-10-05T04:27:21Z brief · item TOOL-aMendedFleet-31 · reason 37e2c28ec58f memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T04:30:07Z dispatch · item e342c9fe TOOL-aMendedFleet-29 · reason tools/memory-recall/test_recall_floor.py

2026-10-05T04:32:53Z dispatch · item 5b8ddb0f TOOL-aMendedFleet-29 · reason tools/memory-recall/check-recall.py

2026-10-05T04:35:47Z brief · item TOOL-aMendedFleet-31 · reason 4c433d32841d memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T04:39:53Z dispatch · item b17e4a1a TOOL-aMendedFleet-31 · reason tools/memory-recall/query.py tools/memory-recall/selftest.py tools/memory-recall/README.md tools/memory-recall/SKILL.template.md .claude/skills/memory-recall/SKILL.md memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-31.md memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-31-1-acceptance-ledger.md memory/builds/aMendedFleet/README.md memory/LIVE.md

2026-10-05T04:47:57Z brief · item TOOL-aMendedFleet-32 · reason 4c433d32841d memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T04:51:40Z dispatch · item c52b647a TOOL-aMendedFleet-32 · reason tools/memory-recall/query.py tools/memory-recall/selftest.py tools/memory-recall/README.md .memory-tree.conf memory/guides/SESSION-KICKOFF.md memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-32.md memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-32-1-acceptance-ledger.md memory/builds/aMendedFleet/README.md memory/LIVE.md

2026-10-05T05:00:23Z brief · item TOOL-aMendedFleet-33 · reason 4c433d32841d memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T05:01:04Z brief · item TOOL-aMendedFleet-33 · reason 7dc71b65fe63 memory/builds/aMendedFleet/prompts/2026-10-05-prompt-TOOL-aMendedFleet-33-1-build-brief.md

2026-10-05T05:05:24Z dispatch · item 56ccb974 TOOL-aMendedFleet-33 · reason tools/memory-recall/README.md tools/memory-recall/SKILL.template.md .claude/skills/memory-recall/SKILL.md tools/memory-recall/recall_conf.py memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-33.md memory/builds/aMendedFleet/README.md memory/LIVE.md

2026-10-05T05:11:58Z brief · item TOOL-aMendedFleet-34 · reason 4c433d32841d memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T05:15:38Z dispatch · item 37b59edc TOOL-aMendedFleet-34 · reason tools/memory-recall/query.py tools/memory-recall/README.md tools/memory-recall/selftest.py memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-34.md memory/builds/aMendedFleet/README.md

2026-10-05T05:21:31Z dispatch · item 37b59edc TOOL-aMendedFleet-34 · reason tools/memory-recall/query.py tools/memory-recall/README.md tools/memory-recall/selftest.py memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-34.md memory/builds/aMendedFleet/README.md memory/backlog/TOOL.md

2026-10-05T05:27:55Z brief · item TOOL-aMendedFleet-35 · reason 4c433d32841d memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T05:32:38Z dispatch · item 197cd613 TOOL-aMendedFleet-35 · reason tools/codebase-map/map_extractors.py tools/codebase-map/selftest.py .codebase-map.conf memory/map/generated/symbols.json memory/map/features/codebase-map.md .lexicon.conf tools/lexicon/lexicon.py tools/memory-tree/README.md memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-35.md memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-35-1-acceptance-ledger.md memory/builds/aMendedFleet/README.md memory/backlog/TOOL.md memory/LIVE.md

2026-10-05T05:40:32Z brief · item TOOL-aMendedFleet-36 · reason 4c433d32841d memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T05:44:09Z dispatch · item 6ad4569d TOOL-aMendedFleet-36 · reason tools/codebase-map/reuse_lookup.py tools/codebase-map/replay-phrases.py tools/codebase-map/selftest.py tools/codebase-map/README.md memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-36.md

2026-10-05T05:53:02Z dispatch · item 6ad4569d TOOL-aMendedFleet-36 · reason tools/codebase-map/reuse_lookup.py tools/codebase-map/replay-phrases.py tools/codebase-map/selftest.py tools/codebase-map/README.md memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-36.md memory/map/generated/symbols.json memory/backlog/TOOL.md memory/builds/aMendedFleet/README.md

2026-10-05T05:57:29Z dispatch · item eb955732 TOOL-aMendedFleet-36 · reason tools/codebase-map/reuse_lookup.py tools/codebase-map/replay-phrases.py tools/codebase-map/selftest.py tools/codebase-map/README.md memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-36.md memory/map/generated/symbols.json memory/backlog/TOOL.md memory/builds/aMendedFleet/README.md memory/map/features/codebase-map.md

2026-10-05T05:59:33Z brief · item TOOL-aMendedFleet-37 · reason 4c433d32841d memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T06:06:50Z dispatch · item 2829d460 TOOL-aMendedFleet-37 · reason tools/codebase-map/map_lib.py tools/codebase-map/map_diff.py tools/codebase-map/selftest.py tools/codebase-map/README.md tools/drift-audit/drift_report.py tools/drift-audit/drift_signals.py tools/drift-audit/selftest.py tools/drift-audit/README.md memory/map/generated/symbols.json memory/map/features/codebase-map.md memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-37.md memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-37-1-acceptance-ledger.md memory/backlog/TOOL.md memory/builds/aMendedFleet/README.md

2026-10-05T06:33:12Z brief · item TOOL-aMendedFleet-38 · reason 4c433d32841d memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T06:39:54Z dispatch · item 67d3b341 TOOL-aMendedFleet-38 · reason tools/codebase-map/map_diff.py tools/codebase-map/map_lib.py tools/codebase-map/selftest.py tools/codebase-map/README.md tools/codebase-map/reuse-lookup.agent.md tools/codebase-map/INVENTORY-DERIVATION.md tools/codebase-map/reuse_lookup.py tools/codebase-map/scen-adversarial.json tools/codebase-map/.codebase-map.conf.example .codebase-map.conf WIRE-INTO-PROJECT.md tools/check-install-prefix.test.sh memory/project/encoding-posture-sites.txt memory/map/generated/symbols.json memory/map/features/codebase-map.md memory/map/features/install-prefix.md memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-38.md memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-38-1-acceptance-ledger.md memory/builds/aMendedFleet/README.md

2026-10-05T06:52:07Z dispatch · item 67d3b341 TOOL-aMendedFleet-38 · reason memory/backlog/TOOL.md

2026-10-05T06:56:38Z dispatch · item 67d3b341 TOOL-aMendedFleet-38 · reason memory/backlog/TOOL.md .codebase-map.conf WIRE-INTO-PROJECT.md memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-38-1-acceptance-ledger.md memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-38.md memory/builds/aMendedFleet/README.md memory/map/features/codebase-map.md memory/map/features/install-prefix.md memory/map/generated/symbols.json memory/project/encoding-posture-sites.txt tools/check-install-prefix.test.sh tools/codebase-map/.codebase-map.conf.example tools/codebase-map/INVENTORY-DERIVATION.md tools/codebase-map/README.md tools/codebase-map/map_diff.py tools/codebase-map/map_lib.py tools/codebase-map/reuse-lookup.agent.md tools/codebase-map/reuse_lookup.py tools/codebase-map/scen-adversarial.json tools/codebase-map/selftest.py

2026-10-05T07:05:53Z brief · item TOOL-aMendedFleet-39 · reason 4c433d32841d memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T07:11:59Z dispatch · item 65e28b22 TOOL-aMendedFleet-39 · reason tools/codebase-map/map_extractors.py memory/map/FOUNDATION.md memory/map/features/agent-cap.md memory/map/features/annotation-style.md memory/map/features/build-method.md memory/map/features/build-readme-surface.md memory/map/features/codebase-map.md memory/map/features/gate-lint.md memory/map/features/govkit.md memory/map/features/install-prefix.md memory/map/features/kit-placeholders.md memory/map/features/lexicon.md memory/map/features/memory-recall.md memory/map/features/memory-tree-backlog.md memory/map/features/memory-tree-hygiene.md memory/map/features/memory-tree-merge-driver.md memory/map/features/playbook-mode.md memory/map/features/playbook.md memory/map/features/process-monitor.md memory/map/features/review-harnesses.md memory/map/features/row-grammar.md memory/map/features/run-gates.md memory/map/features/runlog.md memory/map/features/session-kickoff.md memory/map/features/spec-tokens.md memory/map/features/testsuite-counts.md memory/map/features/unattended-mandate.md memory/map/features/unattended-stops.md memory/map/features/unattended.md memory/map/generated/inventories.json memory/map/generated/MAP.md memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-39.md memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-39-1-acceptance-ledger.md memory/builds/aMendedFleet/README.md

2026-10-05T07:21:15Z dispatch · item 65e28b22 TOOL-aMendedFleet-39 · reason tools/codebase-map/map_extractors.py memory/map/FOUNDATION.md memory/map/features/agent-cap.md memory/map/features/annotation-style.md memory/map/features/build-method.md memory/map/features/build-readme-surface.md memory/map/features/codebase-map.md memory/map/features/gate-lint.md memory/map/features/govkit.md memory/map/features/install-prefix.md memory/map/features/kit-placeholders.md memory/map/features/lexicon.md memory/map/features/memory-recall.md memory/map/features/memory-tree-backlog.md memory/map/features/memory-tree-hygiene.md memory/map/features/memory-tree-merge-driver.md memory/map/features/playbook-mode.md memory/map/features/playbook.md memory/map/features/process-monitor.md memory/map/features/review-harnesses.md memory/map/features/row-grammar.md memory/map/features/run-gates.md memory/map/features/runlog.md memory/map/features/session-kickoff.md memory/map/features/spec-tokens.md memory/map/features/testsuite-counts.md memory/map/features/unattended-mandate.md memory/map/features/unattended-stops.md memory/map/features/unattended.md memory/map/generated/inventories.json memory/map/generated/MAP.md memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-39.md memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-39-1-acceptance-ledger.md memory/builds/aMendedFleet/README.md memory/backlog/TOOL.md

2026-10-05T07:25:36Z dispatch · item 80071a02 TOOL-aMendedFleet-39 · reason tools/check-spec-tokens.py memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-39-1-acceptance-ledger.md

2026-10-05T07:28:58Z brief · item TOOL-aMendedFleet-40 · reason 4c433d32841d memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T07:33:19Z dispatch · item b8545960 TOOL-aMendedFleet-40 · reason tools/codebase-map/map_lib.py tools/codebase-map/test_codebase_map.template.py tools/codebase-map/test_codebase_map.py tools/codebase-map/selftest.py tools/codebase-map/README.md tools/codebase-map/INVENTORY-DERIVATION.md memory/map/baseline.toml memory/map/features/codebase-map.md memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-40.md memory/LIVE.md

2026-10-05T07:37:39Z dispatch · item b8545960 TOOL-aMendedFleet-40 · reason tools/codebase-map/map_lib.py tools/codebase-map/test_codebase_map.template.py tools/codebase-map/test_codebase_map.py tools/codebase-map/selftest.py tools/codebase-map/README.md tools/codebase-map/INVENTORY-DERIVATION.md memory/map/baseline.toml memory/map/features/codebase-map.md memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-40.md memory/LIVE.md

2026-10-05T07:41:11Z dispatch · item b8545960 TOOL-aMendedFleet-40 · reason tools/codebase-map/map_lib.py tools/codebase-map/test_codebase_map.template.py tools/codebase-map/test_codebase_map.py tools/codebase-map/selftest.py tools/codebase-map/README.md tools/codebase-map/INVENTORY-DERIVATION.md memory/map/baseline.toml memory/map/features/codebase-map.md memory/map/features/playbook.md memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-40.md memory/LIVE.md

2026-10-05T07:42:54Z dispatch · item b8545960 TOOL-aMendedFleet-40 · reason tools/codebase-map/map_lib.py tools/codebase-map/test_codebase_map.template.py tools/codebase-map/test_codebase_map.py tools/codebase-map/selftest.py tools/codebase-map/README.md tools/codebase-map/INVENTORY-DERIVATION.md memory/map/baseline.toml memory/map/features/codebase-map.md memory/map/features/playbook.md memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-40.md memory/builds/aMendedFleet/README.md memory/backlog/TOOL.md

2026-10-05T07:46:00Z brief · item TOOL-aMendedFleet-41 · reason 4c433d32841d memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T07:50:28Z dispatch · item ef0995af TOOL-aMendedFleet-41 · reason tools/codebase-map/replay-phrases.py memory/map/features/codebase-map.md memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-41.md memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/inventories.json memory/LIVE.md memory/ledger/2026-10.md

2026-10-05T07:58:51Z dispatch · item ef0995af TOOL-aMendedFleet-41 · reason tools/codebase-map/replay-phrases.py memory/map/features/codebase-map.md memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-41.md memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/inventories.json memory/LIVE.md memory/ledger/2026-10.md memory/builds/aMendedFleet/README.md

2026-10-05T08:01:42Z brief · item TOOL-aMendedFleet-42 · reason 4c433d32841d memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T08:09:30Z dispatch · item 8cc18a9a TOOL-aMendedFleet-42 · reason tools/codebase-map/map_lib.py tools/codebase-map/reuse_lookup.py tools/codebase-map/gen_map.py tools/codebase-map/selftest.py tools/codebase-map/README.md memory/map/features/codebase-map.md memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-42.md memory/builds/aMendedFleet/README.md memory/LIVE.md memory/ledger/2026-10.md

2026-10-05T08:26:21Z dispatch · item 04b65a0e TOOL-aMendedFleet-42 · reason tools/codebase-map/map_lib.py tools/codebase-map/reuse_lookup.py tools/codebase-map/gen_map.py tools/codebase-map/selftest.py tools/codebase-map/README.md memory/map/features/codebase-map.md memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-42.md memory/builds/aMendedFleet/README.md memory/LIVE.md memory/ledger/2026-10.md tools/codebase-map/.codebase-map.conf.example .codebase-map.conf

2026-10-05T08:29:14Z brief · item TOOL-aMendedFleet-43 · reason 4c433d32841d memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T08:33:20Z dispatch · item 6616a4e6 TOOL-aMendedFleet-43 · reason tools/codebase-map/map_lib.py tools/codebase-map/gen_map.py tools/codebase-map/test_codebase_map.py tools/codebase-map/test_codebase_map.template.py tools/codebase-map/selftest.py tools/codebase-map/README.md memory/map/README.md memory/map/features/codebase-map.md memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-43.md

2026-10-05T08:58:15Z dispatch · item 36387492 TOOL-aMendedFleet-43 · reason tools/codebase-map/map_lib.py tools/codebase-map/selftest.py memory/map/generated

2026-10-05T09:02:16Z dispatch · item 66e04e3d TOOL-aMendedFleet-43 · reason tools/codebase-map/gen_map.py tools/codebase-map/test_codebase_map.py tools/codebase-map/test_codebase_map.template.py memory/map/features/codebase-map.md memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-43.md memory/LIVE.md

2026-10-05T09:08:12Z dispatch · item b7bae832 TOOL-aMendedFleet-43 · reason tools/codebase-map/gen_map.py tools/codebase-map/README.md memory/map/README.md memory/map/features/codebase-map.md

2026-10-05T09:14:30Z brief · item TOOL-aMendedFleet-44 · reason 4c433d32841d memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T09:22:30Z dispatch · item 4740c13e TOOL-aMendedFleet-44 · reason tools/codebase-map/map_lib.py tools/codebase-map/test_codebase_map.py tools/codebase-map/test_codebase_map.template.py tools/codebase-map/selftest.py tools/codebase-map/README.md memory/map/README.md memory/map/features/run-gates.md memory/map/features/codebase-map.md memory/map/generated/symbols.json

2026-10-05T09:28:45Z dispatch · item 4740c13e TOOL-aMendedFleet-44 · reason tools/codebase-map/map_lib.py tools/codebase-map/test_codebase_map.py tools/codebase-map/test_codebase_map.template.py tools/codebase-map/selftest.py tools/codebase-map/README.md memory/map/README.md memory/map/features/run-gates.md memory/map/features/codebase-map.md memory/map/generated/symbols.json memory/LIVE.md

2026-10-05T09:32:36Z dispatch · item 53cfc60c TOOL-aMendedFleet-44 · reason tools/codebase-map/gen_map.py memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-44.md memory/LIVE.md memory/ledger/2026-10.md

2026-10-05T09:36:55Z dispatch · item eadf0ed6 TOOL-aMendedFleet-44 · reason memory/builds/aMendedFleet/README.md memory/LIVE.md

2026-10-05T09:41:23Z dispatch · item 0c7feff9 TOOL-aMendedFleet-44 · reason tools/codebase-map/README.md memory/LIVE.md

2026-10-05T09:44:18Z brief · item TOOL-aMendedFleet-46 · reason 4c433d32841d memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T09:50:04Z dispatch · item d0e673fd TOOL-aMendedFleet-46 · reason tools/codebase-map/replay-phrases.py tools/codebase-map/selftest.py memory/map/features/codebase-map.md memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-46.md memory/LIVE.md memory/builds/aMendedFleet/README.md

2026-10-05T10:01:22Z brief · item TOOL-aMendedFleet-47 · reason 4c433d32841d memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T10:05:25Z dispatch · item ede47737 TOOL-aMendedFleet-47 · reason tools/drift-audit/drift_report.py tools/drift-audit/drift_signals.py tools/drift-audit/selftest.py memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-47.md memory/LIVE.md memory/ledger/2026-10.md

2026-10-05T10:17:04Z dispatch · item ede47737 TOOL-aMendedFleet-47 · reason tools/drift-audit/drift_report.py tools/drift-audit/drift_signals.py tools/drift-audit/selftest.py memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-47.md memory/LIVE.md memory/ledger/2026-10.md memory/builds/aMendedFleet/README.md

2026-10-05T10:21:39Z dispatch · item 6a30bf5e TOOL-aMendedFleet-47 · reason tools/drift-audit/drift_report.py tools/drift-audit/drift_signals.py tools/drift-audit/selftest.py memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-47.md memory/LIVE.md memory/ledger/2026-10.md memory/builds/aMendedFleet/README.md tools/drift-audit/README.md

2026-10-05T10:24:28Z brief · item TOOL-aMendedFleet-48 · reason 4c433d32841d memory/builds/aMendedFleet/prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md

2026-10-05T10:30:08Z dispatch · item 25ae3386 TOOL-aMendedFleet-48 · reason tools/drift-audit/drift_report.py tools/drift-audit/selftest.py tools/drift-audit/README.md memory/map/generated/symbols.json memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-48.md memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-48-1-acceptance-ledger.md memory/builds/aMendedFleet/README.md
