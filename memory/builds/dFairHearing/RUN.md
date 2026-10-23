# dFairHearing - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: a593e640134ad47f4e67314a4dbf6545c5956e14
phase: REVIEWING
spec-audit: 2026-10-21
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-dfairhearing-439b9e
anchor-kind: default-branch
cli-version: 2.1.304
lease-utc: 2026-10-22T22:13:38Z
pid-image: claude.exe
host: compeeto-agent
pid: 8532
session: af899cba-95b6-48f9-ac03-ed873f30fc08
keepalive: 8f94ea01
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 3708a705e834709f340a2d160f9acdf9c18b699f
anchor-ref: refs/heads/main
base: 3708a705e834709f340a2d160f9acdf9c18b699f

## Parked

2026-10-23T00:42:41Z rescope · item add TOOL-dFairHearing-20 · reason closes round-1 spec-audit finding id 37 (item H1), HIGH, of memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md

2026-10-23T00:42:42Z rescope · item add TOOL-dFairHearing-21 · reason closes round-1 spec-audit finding id 39 (item H2), HIGH, of memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md

2026-10-23T00:42:44Z rescope · item add TOOL-dFairHearing-22 · reason closes round-1 spec-audit finding id 40 (item H3), HIGH, of memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md

2026-10-23T00:42:52Z rescope · item add TOOL-dFairHearing-23 · reason closes the round-1 spec-audit minors of memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md, batched: MEDIUM ids 1 2 3 4 5 6 7 8 10 13 14 15 16 19 21 23 25 26 27 28 29 30 31 32 33 34 35 38 41 42 43 44 45 46 47 48 49 (items M1 to M28) and LOW ids 9 11 12 18 20 22 24 36 50 51 52 53 (items L1 to L12)

2026-10-23T00:46:07Z review · item dFairHearing-spec-set-r1 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 3 · minors 49 · disposition promote
