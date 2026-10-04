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
