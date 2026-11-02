# dCalibratedLens - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 5e8c07f79254053765e2bfb0813a7503d2d7a29c
phase: REVIEWING
spec-audit: 2026-10-21
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-dcalibratedlens-9622f6
anchor-kind: default-branch
cli-version: 2.1.309
lease-utc: 2026-11-02T15:35:25Z
pid-image: claude.exe
host: compeeto-agent
pid: 20616
session: 8628a15b-1e85-404c-a4a6-275883b9a078
keepalive: fa87da63
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 8bec4cefd957d194660a8d7c2916f420b7299074
anchor-ref: refs/heads/main
base: 8bec4cefd957d194660a8d7c2916f420b7299074

## Parked

2026-11-02T19:49:56Z rescope · item add TOOL-dCalibratedLens-19 · reason spec-audit round 1 (reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) id 1 HIGH, item H1: the value-ledger, loop-review and keep rows share one home, so each record falls under three rows' fields; repairs TOOL-dCalibratedLens-3

2026-11-02T19:49:59Z rescope · item add TOOL-dCalibratedLens-20 · reason spec-audit round 1 (reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) id 36 HIGH, item H2: no Loop Review record carries a Serves line, so the record-kinds field check grades none of them; repairs TOOL-dCalibratedLens-3

2026-11-02T19:50:01Z rescope · item add TOOL-dCalibratedLens-21 · reason spec-audit round 1 (reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) id 2 HIGH, item H3 (shares its fix with id 45, M25): units 4, 6 and 16 add multi-line record fields the shared writer refuses; repairs TOOL-dCalibratedLens-4

2026-11-02T19:50:03Z rescope · item add TOOL-dCalibratedLens-22 · reason spec-audit round 1 (reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) id 3 HIGH, item H4: gather-time proposals have no route to file and no accept text; repairs TOOL-dCalibratedLens-3

2026-11-02T19:50:06Z rescope · item add TOOL-dCalibratedLens-23 · reason spec-audit round 1 (reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) id 4 HIGH, item H5: the instruction-eval seed may land owed, which reds the unattended close bar; repairs TOOL-dCalibratedLens-10

2026-11-02T19:50:10Z rescope · item add TOOL-dCalibratedLens-24 · reason spec-audit round 1 (reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) id 16 HIGH, item H6: unit 1 AC3 feeds the agent-cap hook no payload, so it passes before the unit is built; repairs TOOL-dCalibratedLens-1

2026-11-02T19:50:22Z rescope · item add TOOL-dCalibratedLens-25 · reason spec-audit round 1 (reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) id 35 HIGH, item H7: unit 5's trailing units field breaks the format guard's agent-id test and its self-test fixtures; repairs TOOL-dCalibratedLens-5

2026-11-02T19:50:25Z rescope · item add TOOL-dCalibratedLens-26 · reason spec-audit round 1 (reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) id 48 HIGH, item H8: an empty catch source reads every leg as catches 0 and unit 5 then proposes retiring all of them; repairs TOOL-dCalibratedLens-2

2026-11-02T19:50:27Z rescope · item add TOOL-dCalibratedLens-27 · reason spec-audit round 1 (reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) id 49 HIGH, item H9: a deterministic item failure re-runs the period forever and re-files every proposal on each wake; repairs TOOL-dCalibratedLens-3

2026-11-02T19:50:29Z rescope · item add TOOL-dCalibratedLens-28 · reason spec-audit round 1 (reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) id 50 HIGH, item H10: units 9, 16 and 6 read populations through gov_record.py find and ignore its 40-row cap; repairs TOOL-dCalibratedLens-9

2026-11-02T19:50:32Z rescope · item add TOOL-dCalibratedLens-29 · reason spec-audit round 1 (reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) id 52 HIGH, item H11: unit 6 passes every work-order path as argv, past the Windows command-line limit; repairs TOOL-dCalibratedLens-6

2026-11-02T19:50:34Z rescope · item add TOOL-dCalibratedLens-30 · reason spec-audit round 1 (reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) minors batched into one unit, 30 MEDIUM and 11 LOW by raw id: 5 32 6 7 8 9 10 46 17 18 25 26 27 28 29 30 31 33 37 38 39 40 41 42 43 44 45 51 53 54 11 12 13 14 20 21 22 23 24 34 47; repairs no unit in particular

2026-11-02T20:23:30Z review · item dCalibratedLens-spec-set-r1 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 11 · minors 41 · disposition promote
