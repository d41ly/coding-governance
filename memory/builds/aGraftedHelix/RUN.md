# aGraftedHelix - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: b9bb22c36a189968184ed2359181cac601b842f8
phase: SPECCING
branch-sha: 018b5675727d4c3f316e5b6c53b11c688f03a472
branch-ref: refs/heads/branch/helixir-review-gov-adoption-ce32e1
may: none
mode: prompt
run-branch: refs/heads/branch/helixir-review-gov-adoption-ce32e1
anchor-kind: run-branch
lease-utc: 2026-10-05T17:04:11Z
pid-image: claude.exe
host: compeeto-agent
pid: 3932
session: 1b37a234-acee-4cd7-8267-704d25af99be
keepalive: 199408b7
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 290d0d2d5ae893a2d723a2247ad788035d3bffdf
anchor-ref: refs/heads/main
base: 018b5675727d4c3f316e5b6c53b11c688f03a472

## Parked

2026-10-05T17:41:17Z rescope · item add TOOL-aGraftedHelix-33 · reason discovery on the spec-commit stage's first live use (wf_dff1cb65-954): writers reported authored specs as ids (unit 29) and as paths (30-32); the commit stage matched ids alone, committed one of four specs, and handed out a roster with three MISSING units and no refusal
