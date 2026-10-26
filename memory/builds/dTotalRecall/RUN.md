# dTotalRecall - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 581a761f8
phase: REVIEWING
spec-audit: 2026-10-21
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-dtotalrecall-4bf827
anchor-kind: default-branch
cli-version: 2.1.308
lease-utc: 2026-10-25T21:37:34Z
pid-image: claude.exe
host: compeeto
pid: 1700
session: 23826028-3fee-42de-ac69-b4090f699257
keepalive: 2ec9a796
anchor-url: https://github.com/d41ly/coding-governance
anchor-sha: 462d20f3510072a1dddb5b948370937cfd3bbe0e
anchor-ref: refs/heads/main
base: 462d20f3510072a1dddb5b948370937cfd3bbe0e

## Parked

2026-10-25T23:39:11Z rescope · item add TOOL-dTotalRecall-36 · reason spec-audit round 1 (reviews/2026-10-26-review-dTotalRecall-spec-audit-round1.md) id 1 HIGH, item H1: unit 19's causes check reds every record a current writer adds after the seed, because no writer but the door emits a Caused-by line; repairs TOOL-dTotalRecall-19

2026-10-25T23:39:22Z rescope · item add TOOL-dTotalRecall-37 · reason spec-audit round 1 (reviews/2026-10-26-review-dTotalRecall-spec-audit-round1.md) id 16 HIGH, item H2: unit 8 registers tools/workflows/*.js as linguist-generated, which drops the four template sources and three hand-written workflow scripts from the code record; repairs TOOL-dTotalRecall-8

2026-10-25T23:39:23Z rescope · item add TOOL-dTotalRecall-38 · reason spec-audit round 1 (reviews/2026-10-26-review-dTotalRecall-spec-audit-round1.md) id 17 HIGH, item H3: unit 5's reader census finds regex readers only, so the split-on-hyphen id readers stay unpointed and its flip probe still prints ok under the hyphenated in-slug date; repairs TOOL-dTotalRecall-5

2026-10-25T23:39:24Z rescope · item add TOOL-dTotalRecall-39 · reason spec-audit round 1 (reviews/2026-10-26-review-dTotalRecall-spec-audit-round1.md) id 23 HIGH, item H4: unit 19 mints read_header_edges in tree_lib.py beside PLAY-dOrderedCharter-28's edge_grammar adapter of that name, and the two read the bulleted Caused-by form differently; repairs TOOL-dTotalRecall-19

2026-10-25T23:39:24Z rescope · item add TOOL-dTotalRecall-40 · reason spec-audit round 1 (reviews/2026-10-26-review-dTotalRecall-spec-audit-round1.md) id 36 HIGH, item H5: unit 4's routing region compares the retired journal kind raw, so every log record written after unit 18 drops out of it; repairs TOOL-dTotalRecall-4

2026-10-25T23:39:25Z rescope · item add TOOL-dTotalRecall-41 · reason spec-audit round 1 (reviews/2026-10-26-review-dTotalRecall-spec-audit-round1.md) id 49 HIGH, item H6: unit 7's new ask door grades its argument mapping and not the row it writes, so a newline or separator in --text injects ungraded BACKLOG rows past the refuse default; repairs TOOL-dTotalRecall-7

2026-10-25T23:39:26Z rescope · item add TOOL-dTotalRecall-42 · reason spec-audit round 1 (reviews/2026-10-26-review-dTotalRecall-spec-audit-round1.md) id 51 HIGH, item H7: unit 11's shape-run home is the whole build folder, so the record-kinds check misgrades every build record or reds the empty home at its landing; repairs TOOL-dTotalRecall-11

2026-10-25T23:39:26Z rescope · item add TOOL-dTotalRecall-43 · reason spec-audit round 1 (reviews/2026-10-26-review-dTotalRecall-spec-audit-round1.md) the 59 confirmed minors batched into one unit: 46 MEDIUM, ids 2 3 4 5 6 7 8 9 10 11 12 13 18 19 24 25 26 27 28 29 30 31 32 33 37 38 39 40 41 42 43 44 45 46 48 50 52 53 56 57 58 60 62 63 64 65 (items M1 to M44), and 13 LOW, ids 15 20 21 22 34 35 47 54 55 59 66 67 68 (items L1 to L13); lands on several units, so repairs no unit in particular

2026-10-26T00:02:54Z review · item dTotalRecall-spec-set-r1 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 7 · minors 59 · disposition promote
