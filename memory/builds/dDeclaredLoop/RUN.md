# dDeclaredLoop - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
hold-run: 
hold-streak: 2 · at 815abf73
resume-owed: none · owner
held-at: 2026-11-13T10:37:19Z
hold-reason: the owner withdrew the ruling to re-run the spec audit before any audit started; check 118 still refuses every dispatch, and the parked decision stands
hold-until: owner
hold-code: host-owner-action
held-from: BUILDING
refreshed-at: 2ba17e9d690eb26ef8796fc0eddf190daba3b43b · park · 0 touching
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 815abf738fef0b0ba867aea8ff516a864d7bf6d8
phase: HELD
spec-audit: 2026-10-21
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-declared-loop-d56bf0
anchor-kind: default-branch
cli-version: 2.1.321
lease-utc: 2026-11-13T10:36:12Z
pid-image: claude.exe
host: compeeto-agent
pid: 25292
session: 7c85732c-fa0c-43e9-83f2-238d293195e0
keepalive: 22094182
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 2ba17e9d690eb26ef8796fc0eddf190daba3b43b
anchor-ref: refs/heads/main
base: 2ba17e9d690eb26ef8796fc0eddf190daba3b43b

## Parked

2026-11-13T04:55:18Z brief · item TOOL-dDeclaredLoop-18 · reason a382adfd781a memory/builds/dDeclaredLoop/prompts/2026-11-13-prompt-TOOL-dDeclaredLoop-18-build-brief.md

2026-11-13T06:04:47Z decision · item the dispatch gate (check 118) refuses every unit of this build run until a spec-audit chain covers all 98 live specs, and the owner ended this build's audit chain at round 12: which stands? · reason options: (a) the owner rules the audit run again, and the run re-invokes the build harness with auditIds over the 98 specs, a chain that ran twelve rounds here without a clean round; (b) the owner sets review.spec-audit.disposal off by-nature or removes spec-audit from the README, so the gate does not read the chain for this build run; (c) the owner rules how the twelve recorded rounds enter a chain-rounds record. Refused to choose: (a) reverses the owner's 2026-10-24 stop, (b) edits an owner-landed README key or a policy value to pass a gate, (c) hand-builds an append-only record; none is delegated

2026-11-13T06:07:18Z hold · item host-owner-action · reason until owner · reaped b9b65262 · resume none(owner)

2026-11-13T10:36:20Z resume · item dDeclaredLoop · reason held · keepalive 22094182 · manual

2026-11-13T10:37:23Z hold · item host-owner-action · reason until owner · reaped 22094182 · resume none(owner)
