# dShippedRelease - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 63ca805ed6cff7c3102009a3275d00dddc10602b
phase: REVIEWING
spec-audit: 2026-10-21
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-dshipped-release-1a351d
anchor-kind: default-branch
cli-version: 2.1.309
lease-utc: 2026-10-30T08:57:56Z
pid-image: claude.exe
host: compeeto
pid: 37156
session: 3b045209-e7b3-481f-972c-10cfbdeab2b1
keepalive: cf38fa37
anchor-url: https://github.com/d41ly/coding-governance
anchor-sha: f4597719e4b1ff0f0f779998bd7b8c2ce5213088
anchor-ref: refs/heads/main
base: f4597719e4b1ff0f0f779998bd7b8c2ce5213088

## Parked

2026-10-30T12:01:11Z review · item dShippedRelease-spec-set-r1 · reason verdict BLOCKED · blockers 7 · BOUNDED · highs 22 · minors 77 · disposition promote

2026-10-30T12:12:52Z rescope · item add DEPL-dShippedRelease-49 · reason closes 2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md id 28 (BLOCKER, item B1, shared with id 70): read_parent_state answers landed for a parent that shipped nothing

2026-10-30T12:12:53Z rescope · item add DEPL-dShippedRelease-50 · reason closes 2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md id 70 (BLOCKER, item B1, shared with id 28): a carry-forward DEFERRED parent and a rotated RUN.LANDED under a live run read landed

2026-10-30T12:12:54Z rescope · item add DEPL-dShippedRelease-51 · reason closes 2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md id 29 (BLOCKER, item B2, shared with id 71): the landing review's base reads the close commit and not the landing

2026-10-30T12:12:55Z rescope · item add DEPL-dShippedRelease-52 · reason closes 2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md id 71 (BLOCKER, item B2, shared with id 29): a landing with no outcome record has no derived base and no stacked-close case

2026-10-30T12:12:56Z rescope · item add DEPL-dShippedRelease-53 · reason closes 2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md id 1 (BLOCKER, item B3): deploy.core writes its verdict onto a landing record that does not exist yet

2026-10-30T12:12:57Z rescope · item add DEPL-dShippedRelease-54 · reason closes 2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md id 57 (BLOCKER, item B4): emitted ci pins is red at every adopter holding the kit

2026-10-30T12:12:58Z rescope · item add DEPL-dShippedRelease-55 · reason closes 2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md id 72 (BLOCKER, item B5): release.pick walks down history and downgrades an environment

2026-10-30T12:12:59Z rescope · item add DEPL-dShippedRelease-56 · reason closes 2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md id 74 (HIGH, item H1): a running core stops the walk, so no landing record exists for the length of the bar

2026-10-30T12:13:00Z rescope · item add DEPL-dShippedRelease-57 · reason closes 2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md id 7 (HIGH, item H2): ci_emit check has no green baseline, so unit 8's fixture cases cannot fail

2026-10-30T12:13:01Z rescope · item add DEPL-dShippedRelease-58 · reason closes 2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md id 2 (HIGH, item H3): the walk has no verb for parents, land, released or recommend

2026-10-30T12:13:02Z rescope · item add DEPL-dShippedRelease-59 · reason closes 2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md id 3 (HIGH, item H4): the records landing has no admission rule, so it can strand the close

2026-10-30T12:13:03Z rescope · item add DEPL-dShippedRelease-60 · reason closes 2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md id 4 (HIGH, item H5): --deploy review is not idempotent, so a placed review can never pass

2026-10-30T12:13:04Z rescope · item add DEPL-dShippedRelease-61 · reason closes 2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md id 6 (HIGH, item H6): install.from's default refuses gov's own suites once any tag exists

2026-10-30T12:13:05Z rescope · item add DEPL-dShippedRelease-62 · reason closes 2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md id 91 (HIGH, item H7): the release-tag refusal runs after LAND has written the target

2026-10-30T12:13:06Z rescope · item add DEPL-dShippedRelease-63 · reason closes 2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md id 46 (HIGH, item H8, shared with id 92): derive_public_remote keeps a token held as a bare https user

2026-10-30T12:13:07Z rescope · item add DEPL-dShippedRelease-64 · reason closes 2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md id 92 (HIGH, item H8, shared with id 46): check_release_field passes a token held as a bare https user

2026-10-30T12:13:08Z rescope · item add DEPL-dShippedRelease-65 · reason closes 2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md id 30 (HIGH, item H9): deleting check-kit-versions.sh silently drops live checks

2026-10-30T12:13:09Z rescope · item add DEPL-dShippedRelease-66 · reason closes 2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md id 58 (HIGH, item H10): retiring sixteen legs reds spec tokens on live specs with no legal write to clear it

2026-10-30T12:13:10Z rescope · item add DEPL-dShippedRelease-67 · reason closes 2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md id 45 (HIGH, item H11): install --all gets a second selection that drops resolve_selection's rules

2026-10-30T12:13:11Z rescope · item add DEPL-dShippedRelease-68 · reason closes 2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md id 73 (HIGH, item H12): the late records landing cannot pass the lander after the tombstone

2026-10-30T12:13:12Z rescope · item add DEPL-dShippedRelease-69 · reason closes 2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md id 75 (HIGH, item H13): the landed tombstone has no answer for a build that lands twice

2026-10-30T12:13:14Z rescope · item add DEPL-dShippedRelease-70 · reason closes 2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md id 76 (HIGH, item H14): the second-node derivation tests the tip, but a take-over comes 24 hours later

2026-10-30T12:13:15Z rescope · item add DEPL-dShippedRelease-71 · reason closes 2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md id 77 (HIGH, item H15): a queue entry has no exit, so a refused or held head blocks every landing

2026-10-30T12:13:16Z rescope · item add DEPL-dShippedRelease-72 · reason closes 2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md id 78 (HIGH, item H16): admission fails open on anything but exit 3

2026-10-30T12:13:17Z rescope · item add DEPL-dShippedRelease-73 · reason closes 2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md id 82 (HIGH, item H17): check_landing_review passes on field text the reviewed session can write

2026-10-30T12:13:18Z rescope · item add DEPL-dShippedRelease-74 · reason closes 2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md id 84 (HIGH, item H18): a rendered row with an opt-in adopter fails apply for every non-opting target

2026-10-30T12:13:19Z rescope · item add DEPL-dShippedRelease-75 · reason closes 2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md id 85 (HIGH, item H19): the codex-retrust orders row has no shape its readers can consume

2026-10-30T12:13:20Z rescope · item add DEPL-dShippedRelease-76 · reason closes 2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md id 86 (HIGH, item H20): unit 16's three credential rules cannot all hold

2026-10-30T12:13:22Z rescope · item add DEPL-dShippedRelease-77 · reason closes 2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md id 94 (HIGH, item H21): the engine has no answer for an empty environment, two services or a failed restart

2026-10-30T12:13:23Z rescope · item add DEPL-dShippedRelease-78 · reason closes 2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md the 77 minors by raw id, MEDIUM ids 5 8 9 10 11 12 13 14 15 16 17 18 20 21 22 24 26 31 33 34 35 36 37 38 39 40 41 42 47 48 49 50 51 52 53 54 55 59 60 61 62 63 66 67 68 69 79 80 81 83 87 88 89 90 93 95 96 97 98 99 100 101 102 103 105 106 107 108 and LOW ids 19 23 25 32 43 44 56 64 109
