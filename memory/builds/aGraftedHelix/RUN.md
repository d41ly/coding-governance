# aGraftedHelix - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: db009f97bc4fea5c7a42471547f117948270abcb
phase: SPECCING
branch-sha: 5266d22eba31cdbf15425773d245cd23d7b9cdf5
branch-ref: refs/heads/branch/helixir-review-gov-adoption-ce32e1
spec-audit: 2026-10-04
may: none
mode: prompt
run-branch: refs/heads/branch/helixir-review-gov-adoption-ce32e1
anchor-kind: run-branch
lease-utc: 2026-10-04T15:42:10Z
pid-image: claude.exe
host: compeeto-agent
pid: 3932
session: 1b37a234-acee-4cd7-8267-704d25af99be
keepalive: 90b28c46
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: ac65de998f094a244540905b35d7c5f6880ab850
anchor-ref: refs/heads/main
base: 5266d22eba31cdbf15425773d245cd23d7b9cdf5

## Parked

2026-10-04T15:45:33Z rescope · item add TOOL-aGraftedHelix-9 · reason M2 decompose: unit 6 named two mechanisms, an exact content-key check (memory-tree) and a near-match relation check (recall index); one mechanism per spec splits them
