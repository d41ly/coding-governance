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
lease-utc: 2026-11-01T09:07:33Z
pid-image: claude.exe
host: compeeto
pid: 27284
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

2026-10-30T13:56:02Z review · item dShippedRelease-spec-set-r2 · reason verdict BLOCKED · blockers 8 · BOUNDED · highs 19 · minors 79 · disposition promote

2026-11-01T09:22:53Z rescope · item add DEPL-dShippedRelease-79 · reason closes 2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md id 1 (BLOCKER, item B1, shared with id 28): the record writes review pending, so never fired cannot be told from fired

2026-11-01T09:22:54Z rescope · item add DEPL-dShippedRelease-80 · reason closes 2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md id 28 (BLOCKER, item B1, shared with id 1): run_deploy_review reads the field before the row, so no landing review ever fires

2026-11-01T09:22:55Z rescope · item add DEPL-dShippedRelease-81 · reason closes 2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md id 2 (BLOCKER, item B2, shared with id 87): the queue's parent skip carries no spec-run exemption

2026-11-01T09:22:56Z rescope · item add DEPL-dShippedRelease-82 · reason closes 2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md id 87 (BLOCKER, item B2, shared with id 2): an exempt spec run passes deploy.parents and is never admitted

2026-11-01T09:22:56Z rescope · item add DEPL-dShippedRelease-83 · reason closes 2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md id 29 (BLOCKER, item B3, shared with ids 47, 88): the disposed path is confined to no build's reviews

2026-11-01T09:22:57Z rescope · item add DEPL-dShippedRelease-84 · reason closes 2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md id 47 (BLOCKER, item B3, shared with ids 29, 88): any Verdict line passes, with no closed set read

2026-11-01T09:22:58Z rescope · item add DEPL-dShippedRelease-85 · reason closes 2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md id 88 (BLOCKER, item B3, shared with ids 29, 47): the disposed count is compared with nothing

2026-11-01T09:22:59Z rescope · item add DEPL-dShippedRelease-86 · reason closes 2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md id 86 (BLOCKER, item B4): release.pick steps to the next older SHA after any outcome but verified

2026-11-01T09:22:59Z rescope · item add DEPL-dShippedRelease-87 · reason closes 2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md id 3 (HIGH, item H1, shared with ids 49, 89): render's no-table exit 0 cannot be told from a lost render

2026-11-01T09:23:00Z rescope · item add DEPL-dShippedRelease-88 · reason closes 2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md id 49 (HIGH, item H1, shared with ids 3, 89): an ok row at code 0 with an absence probe hides a lost render and trips an opting run

2026-11-01T09:23:01Z rescope · item add DEPL-dShippedRelease-89 · reason closes 2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md id 89 (HIGH, item H1, shared with ids 3, 49): no case stages a render that exits 0 and writes nothing, or a stale file

2026-11-01T09:23:02Z rescope · item add DEPL-dShippedRelease-90 · reason closes 2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md id 4 (HIGH, item H2): disposed accepts a report with no binding to this landing

2026-11-01T09:23:02Z rescope · item add DEPL-dShippedRelease-91 · reason closes 2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md id 5 (HIGH, item H3): after a recorded non-verified outcome the walk picks an older SHA

2026-11-01T09:23:03Z rescope · item add DEPL-dShippedRelease-92 · reason closes 2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md id 6 (HIGH, item H4): test_records_landing is false on the default records landing, which holds two commits

2026-11-01T09:23:04Z rescope · item add DEPL-dShippedRelease-93 · reason closes 2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md id 7 (HIGH, item H5): a landed spec run's queue entry is never removed and returns to the head

2026-11-01T09:23:04Z rescope · item add DEPL-dShippedRelease-94 · reason closes 2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md id 8 (HIGH, item H6, shared with id 96): the late records route admits a terminal build lease alone

2026-11-01T09:23:05Z rescope · item add DEPL-dShippedRelease-95 · reason closes 2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md id 96 (HIGH, item H6, shared with id 8): check_unleased goes false once the build run leases the slug

2026-11-01T09:23:06Z rescope · item add DEPL-dShippedRelease-96 · reason closes 2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md id 22 (HIGH, item H7, shared with ids 33, 48, 93): derive_public_remote leaves an ssh url's password

2026-11-01T09:23:07Z rescope · item add DEPL-dShippedRelease-97 · reason closes 2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md id 33 (HIGH, item H7, shared with ids 22, 48, 93): test_remote_userinfo passes an ssh url with a password

2026-11-01T09:23:07Z rescope · item add DEPL-dShippedRelease-98 · reason closes 2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md id 48 (HIGH, item H7, shared with ids 22, 33, 93): the block mints a second predicate nothing compares with the first

2026-11-01T09:23:08Z rescope · item add DEPL-dShippedRelease-99 · reason closes 2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md id 93 (HIGH, item H7, shared with ids 22, 33, 48): nothing re-reads the value after the strip, so a surviving credential ships

2026-11-01T09:23:09Z rescope · item add DEPL-dShippedRelease-100 · reason closes 2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md id 30 (HIGH, item H8): the ended-leg record leaves the path arm red, so unit 10 still cannot land green

2026-11-01T09:23:10Z rescope · item add DEPL-dShippedRelease-101 · reason closes 2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md id 35 (HIGH, item H9): the refusal is keyed on a --to that always has a value

2026-11-01T09:23:10Z rescope · item add DEPL-dShippedRelease-102 · reason closes 2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md id 70 (HIGH, item H10): the apply census is graded before later harnesses exist and lists a README

2026-11-01T09:23:11Z rescope · item add DEPL-dShippedRelease-103 · reason closes 2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md id 91 (HIGH, item H11): a head that exits with an unchanged tree can never re-enter the queue

2026-11-01T09:23:12Z rescope · item add DEPL-dShippedRelease-104 · reason closes 2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md id 94 (HIGH, item H12): adopt is left with no refusal and a copy-mode update with no --to is unstated

2026-11-01T09:23:12Z rescope · item add DEPL-dShippedRelease-105 · reason closes 2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md id 95 (HIGH, item H13): read-current's exit 2 reuses refused after the host has changed

2026-11-01T09:23:13Z rescope · item add DEPL-dShippedRelease-106 · reason closes 2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md the 79 minors by raw id, MEDIUM ids 9 71 10 31 55 90 11 12 34 101 13 68 14 102 15 16 39 56 73 17 113 18 74 19 40 20 21 38 23 92 32 99 37 76 41 50 53 54 57 59 110 75 77 78 79 80 106 82 97 98 100 103 104 105 107 108 109 111 112 114 and LOW ids 25 26 81 85 27 42 43 44 45 46 84 51 58 60 61 62 63 64 65
