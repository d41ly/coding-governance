# aMendedFleet - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 7af5f564641d231f8b78f6b183dde1b6bf53111d
phase: RUNNING
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
