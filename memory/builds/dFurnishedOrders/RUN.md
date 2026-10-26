# dFurnishedOrders - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 4d726ef2723c6f3f368fde2d48ec7ea61fc5da33
phase: REVIEWING
spec-audit: 2026-10-21
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-furnished-orders-b4ef78
anchor-kind: default-branch
cli-version: 2.1.308
lease-utc: 2026-10-26T17:14:46Z
pid-image: claude.exe
host: compeeto
pid: 14260
session: 56bbd6e7-78b5-422f-b186-74bf31f37f19
keepalive: ad49c165
anchor-url: https://github.com/d41ly/coding-governance
anchor-sha: 5fede642ad2ff1418f12b5d7117129edc8287d7e
anchor-ref: refs/heads/main
base: c8d46e188985ce49caad48cf874934661ad3fc7c

## Parked

2026-10-26T19:33:57Z review · item dFurnishedOrders-spec-set-r1 · reason verdict BLOCKED · blockers 2 · BOUNDED · highs 5 · minors 51 · disposition promote

2026-10-26T19:48:54Z rescope · item add TOOL-dFurnishedOrders-22 · reason spec-audit round1 (memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md) finding id 1 at BLOCKER, report item B1, shared with id 48: the verifier exemption keys on class words no input block carries

2026-10-26T19:48:55Z rescope · item add TOOL-dFurnishedOrders-23 · reason spec-audit round1 (memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md) finding id 48 at BLOCKER, report item B1, shared with id 1: AC2 certifies the exemption on a block name no shipped role reads

2026-10-26T19:48:56Z rescope · item add TOOL-dFurnishedOrders-24 · reason spec-audit round1 (memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md) finding id 4 at HIGH, report item H2: the per-order return schema has no rule for alternative outcome arms

2026-10-26T19:48:57Z rescope · item add TOOL-dFurnishedOrders-25 · reason spec-audit round1 (memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md) finding id 50 at HIGH, report item H3: the upgrade-step scan flags frozen records so up fails on every update

2026-10-26T19:49:06Z rescope · item add TOOL-dFurnishedOrders-26 · reason spec-audit round1 (memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md) finding id 3 at HIGH, report item H1, shared with ids 19 and 52: the run's launch prompt reads as owner presence at derive_attended

2026-10-26T19:49:07Z rescope · item add TOOL-dFurnishedOrders-27 · reason spec-audit round1 (memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md) finding id 19 at HIGH, report item H1, shared with ids 3 and 52: a FORKED --dispatch reads the launch turn as presence and holds the fork asked live

2026-10-26T19:49:08Z rescope · item add TOOL-dFurnishedOrders-28 · reason spec-audit round1 (memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md) finding id 52 at HIGH, report item H1, shared with ids 3 and 19: a gated --phase before the first keepalive is held asked live with nobody present

2026-10-26T19:49:09Z rescope · item add TOOL-dFurnishedOrders-29 · reason spec-audit round1 (memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md) minors batched, roles hooks and runlog half: MEDIUM ids 2 5 7 23 24 51 25 29 30 31 32 33 34 35 36 39 43 44 45 56 57 58 59 (items M1 M2 M4 M7-M18 M20-M22 M25-M28) and LOW ids 10 12 14 38 15 16 26 27 37 47 60 61 (items L1 L3 L5-L9 L11 L13-L15)

2026-10-26T19:49:10Z rescope · item add TOOL-dFurnishedOrders-30 · reason spec-audit round1 (memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md) minors batched, workflows unattended kickoff and memory-tree half, a write set disjoint from TOOL-dFurnishedOrders-29 by M6: MEDIUM ids 6 20 49 8 22 42 53 21 40 41 54 55 (items M3 M5 M6 M19 M23 M24) and LOW ids 11 13 28 46 (items L2 L4 L10 L12)
