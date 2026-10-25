# dOrderedCharter - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
asks-at-landing: PLAY-dOrderedCharter-38=DEFERRED
units-at-landing: PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55
gates-run: unattended-179279903129518517354-1951 32165a70
parked-surfaced: yes
keepalive-reaped: yes
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 04cbc65b9fff5553a1f993396e4ab8fe5d7c0d90
phase: LANDING
spec-audit: 2026-10-21
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-dorderedcharter-10a315
anchor-kind: default-branch
cli-version: 2.1.308
lease-utc: 2026-10-23T15:00:26Z
pid-image: claude.exe
host: compeeto
pid: 27964
session: 74d36c28-2550-4cf3-9384-4e645df92da1
keepalive: 97682d1b
anchor-url: https://github.com/d41ly/coding-governance
anchor-sha: ce13efbe3d90cc8fcad100267e18ec2c9d03bdf8
anchor-ref: refs/heads/main
base: ce13efbe3d90cc8fcad100267e18ec2c9d03bdf8

## Parked

2026-10-23T21:09:30Z rescope · item add PLAY-dOrderedCharter-39 · reason closes spec-audit round 1 finding 1 (HIGH, item H1, shared with finding 49): the card import survives the agent-instructions retirement

2026-10-23T21:09:30Z rescope · item add PLAY-dOrderedCharter-40 · reason closes spec-audit round 1 finding 2 (HIGH, item H2): gov's first instruction unit rows written

2026-10-23T21:09:31Z rescope · item add PLAY-dOrderedCharter-41 · reason closes spec-audit round 1 finding 30 (HIGH, item H3): the cross-os block kept live

2026-10-23T21:09:32Z rescope · item add PLAY-dOrderedCharter-42 · reason closes spec-audit round 1 finding 31 (HIGH, item H4): the new record kinds admitted by the bindings reader

2026-10-23T21:09:32Z rescope · item add PLAY-dOrderedCharter-43 · reason closes spec-audit round 1 finding 49 (HIGH, item H1, shared with finding 1): the card import written by the one renderer

2026-10-23T21:09:33Z rescope · item add PLAY-dOrderedCharter-44 · reason closes spec-audit round 1 finding 76 (HIGH, item H5): tag index freshness keyed on the extractor

2026-10-23T21:09:34Z rescope · item add PLAY-dOrderedCharter-45 · reason closes spec-audit round 1 finding 79 (HIGH, item H6): the merge-rows TOML-table class conflict envelope

2026-10-23T21:09:35Z rescope · item add PLAY-dOrderedCharter-46 · reason closes spec-audit round 1 finding 80 (HIGH, item H7): the overlay's landed revision defined

2026-10-23T21:09:35Z rescope · item add PLAY-dOrderedCharter-47 · reason closes spec-audit round 1 finding 81 (HIGH, item H8): citations grandfathered by authorship

2026-10-23T21:09:36Z rescope · item add PLAY-dOrderedCharter-48 · reason closes spec-audit round 1 finding 82 (HIGH, item H9): the citation producers derived by a query

2026-10-23T21:09:41Z rescope · item add PLAY-dOrderedCharter-49 · reason closes spec-audit round 1 minors batch, MEDIUM findings 3 4 5 6 7 8 9 10 11 12 13 14 16 17 18 19 20 21 22 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 51 52 53 54 55 59 60 65 66 67 68 69 70 71 77 78 83 84 85 86 and LOW findings 15 23 24 25 26 27 28 29 47 50 57 61 63 64 72 73 74 75 87

2026-10-23T21:34:30Z review · item dOrderedCharter-spec-set-r1 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 10 · minors 73 · disposition promote

2026-10-23T22:17:19Z rescope · item add PLAY-dOrderedCharter-50 · reason closes spec-audit round 2 finding 23 (HIGH, item H1): the bar-keeping rows a new leg, key or retirement owes are written by the pass that creates them

2026-10-23T22:17:20Z rescope · item add PLAY-dOrderedCharter-51 · reason closes spec-audit round 2 finding 30 (HIGH, item H2): the shared tag index keyed per extractor version, each worktree reading its own

2026-10-23T22:17:21Z rescope · item add PLAY-dOrderedCharter-52 · reason closes spec-audit round 2 finding 33 (HIGH, item H3): the TOML-table merge envelope made total, theirs-side deletes and adds included

2026-10-23T22:17:21Z rescope · item add PLAY-dOrderedCharter-53 · reason closes spec-audit round 2 finding 36 (HIGH, item H4): file:line citations grandfathered per line by the commit that wrote them

2026-10-23T22:17:22Z rescope · item add PLAY-dOrderedCharter-54 · reason closes spec-audit round 2 finding 39 (HIGH, item H5): the card file owner's liveness defined, a dead owner's card taken over

2026-10-23T22:17:27Z rescope · item add PLAY-dOrderedCharter-55 · reason closes spec-audit round 2 minors batch, MEDIUM findings 1 2 3 4 5 6 7 8 10 11 12 14 15 16 19 20 22 24 26 28 31 32 34 37 40 41 and LOW findings 9 17 18 29 35

2026-10-23T22:33:35Z review · item dOrderedCharter-spec-set-r2 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 5 · minors 31 · disposition promote

2026-10-23T22:53:29Z rescope · item defer PLAY-dOrderedCharter-1 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:29Z rescope · item defer PLAY-dOrderedCharter-10 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:30Z rescope · item defer PLAY-dOrderedCharter-11 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:31Z rescope · item defer PLAY-dOrderedCharter-12 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:32Z rescope · item defer PLAY-dOrderedCharter-13 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:32Z rescope · item defer PLAY-dOrderedCharter-14 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:33Z rescope · item defer PLAY-dOrderedCharter-15 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:34Z rescope · item defer PLAY-dOrderedCharter-16 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:35Z rescope · item defer PLAY-dOrderedCharter-17 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:35Z rescope · item defer PLAY-dOrderedCharter-18 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:36Z rescope · item defer PLAY-dOrderedCharter-19 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:37Z rescope · item defer PLAY-dOrderedCharter-2 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:38Z rescope · item defer PLAY-dOrderedCharter-20 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:38Z rescope · item defer PLAY-dOrderedCharter-21 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:39Z rescope · item defer PLAY-dOrderedCharter-22 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:40Z rescope · item defer PLAY-dOrderedCharter-23 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:40Z rescope · item defer PLAY-dOrderedCharter-24 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:41Z rescope · item defer PLAY-dOrderedCharter-25 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:42Z rescope · item defer PLAY-dOrderedCharter-26 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:43Z rescope · item defer PLAY-dOrderedCharter-27 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:43Z rescope · item defer PLAY-dOrderedCharter-28 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:44Z rescope · item defer PLAY-dOrderedCharter-29 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:45Z rescope · item defer PLAY-dOrderedCharter-3 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:46Z rescope · item defer PLAY-dOrderedCharter-30 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:46Z rescope · item defer PLAY-dOrderedCharter-31 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:47Z rescope · item defer PLAY-dOrderedCharter-32 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:48Z rescope · item defer PLAY-dOrderedCharter-33 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:48Z rescope · item defer PLAY-dOrderedCharter-34 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:49Z rescope · item defer PLAY-dOrderedCharter-35 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:50Z rescope · item defer PLAY-dOrderedCharter-36 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:51Z rescope · item defer PLAY-dOrderedCharter-37 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:51Z rescope · item defer PLAY-dOrderedCharter-4 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:52Z rescope · item defer PLAY-dOrderedCharter-5 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:53Z rescope · item defer PLAY-dOrderedCharter-6 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:53Z rescope · item defer PLAY-dOrderedCharter-7 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:54Z rescope · item defer PLAY-dOrderedCharter-8 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:55Z rescope · item defer PLAY-dOrderedCharter-9 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:56Z rescope · item defer PLAY-dOrderedCharter-39 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:56Z rescope · item defer PLAY-dOrderedCharter-40 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:57Z rescope · item defer PLAY-dOrderedCharter-41 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:58Z rescope · item defer PLAY-dOrderedCharter-42 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:59Z rescope · item defer PLAY-dOrderedCharter-43 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:53:59Z rescope · item defer PLAY-dOrderedCharter-44 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:54:00Z rescope · item defer PLAY-dOrderedCharter-45 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:54:01Z rescope · item defer PLAY-dOrderedCharter-46 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:54:02Z rescope · item defer PLAY-dOrderedCharter-47 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:54:02Z rescope · item defer PLAY-dOrderedCharter-48 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:54:03Z rescope · item defer PLAY-dOrderedCharter-49 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:54:04Z rescope · item defer PLAY-dOrderedCharter-50 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:54:05Z rescope · item defer PLAY-dOrderedCharter-51 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:54:05Z rescope · item defer PLAY-dOrderedCharter-52 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:54:06Z rescope · item defer PLAY-dOrderedCharter-53 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:54:07Z rescope · item defer PLAY-dOrderedCharter-54 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T22:54:07Z rescope · item defer PLAY-dOrderedCharter-55 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing PLAY-dOrderedCharter-38

2026-10-23T23:54:23Z override · item closing-review-recorded · reason the spec run's closing diff review is not run: the owner capped spec review at two rounds ('no more than 2 rounds of spec reviews', memory/builds/dOrderedCharter/prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-owner-review-cap.md), and this run's diff is spec and record text only, already read by both rounds; the build run's closing diff review over its code meets it
