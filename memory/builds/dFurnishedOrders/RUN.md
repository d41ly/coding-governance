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

2026-10-26T21:27:48Z rescope · item add TOOL-dFurnishedOrders-31 · reason spec-audit round1 of the round-1 promotions (memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-22-spec-audit-round1.md) finding id 1 at HIGH, report item H1: unit 24 builds an anyOf branch for the establishes table before the outcome filter lands

2026-10-26T21:27:57Z rescope · item add TOOL-dFurnishedOrders-32 · reason spec-audit round1 of the round-1 promotions (memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-22-spec-audit-round1.md) finding id 2 at HIGH, report item H2: units 22 and 23 hard-code the two reviewer roles the parent build merges, and the merged role re-opens F2

2026-10-26T21:27:58Z rescope · item add TOOL-dFurnishedOrders-33 · reason spec-audit round1 of the round-1 promotions (memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-22-spec-audit-round1.md) finding id 3 at HIGH, report item H3, shared with id 30: a posture that cannot be read still answers attended inside a run's window

2026-10-26T21:27:59Z rescope · item add TOOL-dFurnishedOrders-34 · reason spec-audit round1 of the round-1 promotions (memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-22-spec-audit-round1.md) finding id 30 at HIGH, report item H3, shared with id 3: the posture read has no failure causes and no bound inside a run's window

2026-10-26T21:28:00Z rescope · item add TOOL-dFurnishedOrders-35 · reason spec-audit round1 of the round-1 promotions (memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-22-spec-audit-round1.md) finding id 10 at HIGH, report item H4, shared with id 25: on gov's own tree the call-site scan has no installed-kit subtraction, so it hits files under tools/

2026-10-26T21:28:01Z rescope · item add TOOL-dFurnishedOrders-36 · reason spec-audit round1 of the round-1 promotions (memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-22-spec-audit-round1.md) finding id 25 at HIGH, report item H4, shared with id 10: a kit's own suites spell the retired keys on purpose and stay in the call-site population

2026-10-26T21:28:02Z rescope · item add TOOL-dFurnishedOrders-37 · reason spec-audit round1 of the round-1 promotions (memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-22-spec-audit-round1.md) minors batched in one unit: MEDIUM ids 4 5 14 6 11 34 12 36 18 13 23 20 21 41 22 40 26 27 31 32 28 33 35 38 39 37 43 (items M1-M22) and LOW ids 7 8 9 17 15 16 19 24 29 42 (items L1-L9)

2026-10-26T21:59:12Z review · item dFurnishedOrders-spec-set-r2 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 6 · minors 37 · disposition promote

2026-10-26T22:40:09Z rescope · item add TOOL-dFurnishedOrders-38 · reason spec-audit round1 of the round-2 promotions (memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-31-spec-audit-round1.md) finding id 29 at HIGH, report item H1, related to id 1 at MEDIUM: unit 37 AC3's adopt-unattended arm cannot fail, because git grep -n output never opens with hit

2026-10-26T22:40:10Z rescope · item add TOOL-dFurnishedOrders-39 · reason spec-audit round1 of the round-2 promotions (memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-31-spec-audit-round1.md) finding id 27 at HIGH, report item H2, related to id 21 at MEDIUM: the single bounded runner does not bound a child whose descendant holds stdout open on Windows

2026-10-26T22:40:11Z rescope · item add TOOL-dFurnishedOrders-40 · reason spec-audit round1 of the round-2 promotions (memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-31-spec-audit-round1.md) finding id 28 at HIGH, report item H3, related to id 15 at MEDIUM: unit 36 takes a receipt kit home from merged and seed rows that land at the repo root

2026-10-26T22:40:18Z rescope · item add TOOL-dFurnishedOrders-41 · reason spec-audit round1 of the round-2 promotions (memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-31-spec-audit-round1.md) minors batched, the govkit upgrade-step half: MEDIUM ids 9 10 32 14 19 34 15 17 24 33 31 (items M8 M12 M13 M14 M15 M19 M20 M21) and LOW id 8 (item L1)

2026-10-26T22:40:18Z rescope · item add TOOL-dFurnishedOrders-42 · reason spec-audit round1 of the round-2 promotions (memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-31-spec-audit-round1.md) minors batched, the roles runlog unattended and kickoff half, a write set disjoint from TOOL-dFurnishedOrders-41 by M6: MEDIUM ids 1 2 23 3 22 4 5 6 25 7 11 12 13 21 26 30 35 (items M1-M7 M9-M11 M16-M18 M22) and LOW ids 16 20 (items L2 L3)

2026-10-26T22:58:20Z review · item dFurnishedOrders-spec-set-r3 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 3 · minors 31 · disposition promote

2026-10-27T00:03:40Z rescope · item add TOOL-dFurnishedOrders-43 · reason spec-audit round1 of the round-3 promotions (memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-38-spec-audit-round1.md) finding id 1 at HIGH, report item H1, shared with id 14: unit 40 derives a receipt kit's home by a formula, never from where apply lands the kit

2026-10-27T00:03:41Z rescope · item add TOOL-dFurnishedOrders-44 · reason spec-audit round1 of the round-3 promotions (memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-38-spec-audit-round1.md) finding id 14 at HIGH, report item H1, shared with id 1: no criterion holds the step's receipt homes to where apply lands each shipped kit, so a parallel formula passes AC1

2026-10-27T00:03:42Z rescope · item add TOOL-dFurnishedOrders-45 · reason spec-audit round1 of the round-3 promotions (memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-38-spec-audit-round1.md) minors batched, the govkit upgrade-step half: MEDIUM ids 25 9 31 32 (items M1 M5 M12) and LOW ids 5 13 18 27 (items L2 L5 L7 L10)

2026-10-27T00:03:43Z rescope · item add TOOL-dFurnishedOrders-46 · reason spec-audit round1 of the round-3 promotions (memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-38-spec-audit-round1.md) minors batched, the roles run-gates unattended kickoff and gate-manifest half, a write set disjoint from TOOL-dFurnishedOrders-45 by M6: MEDIUM ids 2 3 8 10 15 16 20 22 29 (items M2 M3 M4 M6 M7 M8 M9 M10 M11) and LOW ids 4 11 12 17 19 24 28 30 33 (items L1 L3 L4 L6 L8 L9 L11 L12 L13)

2026-10-27T00:27:15Z review · item dFurnishedOrders-spec-set-r4 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 2 · minors 26 · disposition promote

2026-10-27T01:06:39Z rescope · item add TOOL-dFurnishedOrders-47 · reason spec-audit round1 of the round-4 promotions (memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-43-spec-audit-round1.md) finding id 10 at HIGH, report item H1: unit 44's apply --all arm fails on a refused apply, and that apply exits 1 at HEAD from adopter and render problems unrelated to home parity

2026-10-27T01:06:39Z rescope · item add TOOL-dFurnishedOrders-48 · reason spec-audit round1 of the round-4 promotions (memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-43-spec-audit-round1.md) minors batched, the govkit step, parity-arm, guard and ratchet half: MEDIUM ids 1 2 3 4 9 11 12 13 14 15 17 19 22 23 24 25 30 31 32 33 35 (items M1-M13) and LOW ids 5 18 21 28 34 (items L1 L2 L5 L6 L8)

2026-10-27T01:06:40Z rescope · item add TOOL-dFurnishedOrders-49 · reason spec-audit round1 of the round-4 promotions (memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-43-spec-audit-round1.md) minors batched, the roles-suite budget, interrupt probe and write-set record half, a write set disjoint from TOOL-dFurnishedOrders-48 by M6: LOW ids 6 7 16 20 26 27 (items L3 L4 L7 L9)

2026-10-27T01:22:33Z review · item dFurnishedOrders-spec-set-r5 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 1 · minors 32 · disposition promote

2026-10-27T02:25:10Z rescope · item add TOOL-dFurnishedOrders-50 · reason spec-audit round1 of the round-5 promotions (memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-47-spec-audit-round1.md) finding id 17 at HIGH, report item H1: unit 48 S17's guard rows red spec tokens across live specs in this and other builds

2026-10-27T02:25:16Z rescope · item add TOOL-dFurnishedOrders-51 · reason spec-audit round1 of the round-5 promotions (memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-47-spec-audit-round1.md) finding id 24 at HIGH, report item H2: unit 49's interrupt probe never pins whose pid it checks, so a pid from another namespace reads as gone and the arm passes unchecked

2026-10-27T02:25:17Z rescope · item add TOOL-dFurnishedOrders-52 · reason spec-audit round1 of the round-5 promotions (memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-47-spec-audit-round1.md) minors batched in one unit: MEDIUM ids 1 20 28 2 7 23 6 13 27 8 26 9 12 18 29 (items M1-M8) and LOW ids 10 19 22 4 5 11 14 30 15 16 21 (items L1-L10)

2026-10-27T02:45:26Z review · item dFurnishedOrders-spec-set-r6 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 2 · minors 26 · disposition promote

2026-10-27T03:26:15Z review · item dFurnishedOrders-spec-set-r7 · reason verdict BLOCKED · blockers 1 · BOUNDED · highs 4 · minors 27 · disposition promote

2026-10-27T03:34:47Z rescope · item add TOOL-dFurnishedOrders-53 · reason spec-audit round1 of the round-6 promotions (memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-50-spec-audit-round1.md) finding id 11 at BLOCKER, report item B1: unit 52 S16's --legs-for route reads every home directory as covered by its own kit.toml descriptor row, so the guard arm never reds on a dropped home row

2026-10-27T03:34:47Z rescope · item add TOOL-dFurnishedOrders-54 · reason spec-audit round1 of the round-6 promotions (memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-50-spec-audit-round1.md) finding id 3 at HIGH, report item H1, shared with ids 18 and 25: unit 52 AC6's scratch legs copy cannot reach the --legs-for reader S16 mandates, so the arm grades gov's own manifest

2026-10-27T03:34:48Z rescope · item add TOOL-dFurnishedOrders-55 · reason spec-audit round1 of the round-6 promotions (memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-50-spec-audit-round1.md) finding id 18 at HIGH, report item H1, shared with ids 3 and 25: read_legs_for drops every UNEVALUATED line, so unit 52 S16's glob row has no source in the seam the arm reads

2026-10-27T03:34:49Z rescope · item add TOOL-dFurnishedOrders-56 · reason spec-audit round1 of the round-6 promotions (memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-50-spec-audit-round1.md) finding id 25 at HIGH, report item H1, shared with ids 3 and 18: unit 52 AC6 certifies a covered rule it never exercises, since nothing shows the rows it graded came from the copy it was handed

2026-10-27T03:34:50Z rescope · item add TOOL-dFurnishedOrders-57 · reason spec-audit round1 of the round-6 promotions (memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-50-spec-audit-round1.md) finding id 23 at HIGH, report item H2: unit 50 computes its reach over home rows only, so its waiver table keys tokens the spec-token checker never prints

2026-10-27T03:34:54Z rescope · item add TOOL-dFurnishedOrders-58 · reason spec-audit round1 of the round-6 promotions (memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-50-spec-audit-round1.md) minors batched in one unit: MEDIUM ids 1 30 2 4 28 6 13 7 8 9 12 19 22 24 27 29 31 (items M1-M14) and LOW ids 5 26 10 21 15 34 17 20 32 33 (items L1-L7)

2026-10-27T04:36:27Z rescope · item add TOOL-dFurnishedOrders-59 · reason spec-audit round1 of the round-7 promotions (memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-53-spec-audit-round1.md) finding id 19 at HIGH, report item H1: unit 53 AC1's fixture plants no row below tools/roles/, so it cannot exercise the one-way directory rule it certifies

2026-10-27T04:36:32Z rescope · item add TOOL-dFurnishedOrders-60 · reason spec-audit round1 of the round-7 promotions (memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-53-spec-audit-round1.md) minors batched in one unit: MEDIUM ids 1 5 16 4 7 8 10 26 23 24 27 (items M1-M10) and LOW ids 2 3 6 9 11 17 12 13 14 15 18 21 28 (items L1-L12)

2026-10-27T04:56:19Z review · item dFurnishedOrders-spec-set-r8 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 1 · minors 24 · disposition promote
