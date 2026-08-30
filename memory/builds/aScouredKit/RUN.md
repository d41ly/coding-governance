# aScouredKit - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 3eaf38d0d57dd0206103835628a27f2c57831547
phase: REVIEWING
branch-sha: 093730e40355d6a04300966f791f2634379e8b45
branch-ref: refs/heads/branch/kit-adversarial-review-15ed31
mode: prompt
anchor-kind: run-branch
keepalive: eb5c4bfb
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 14e21399f7dd0559224837a2754fcbf9fc4a754b
anchor-ref: refs/heads/main
base: 093730e40355d6a04300966f791f2634379e8b45

## Parked

2026-08-30T10:47:26Z rescope · item add TOOL-aScouredKit-3 · reason the two fields that decide a gate leg's hold are pinned and counted by ONE predicate (wave-1 F18, F19)

2026-08-30T10:47:27Z rescope · item add TOOL-aScouredKit-4 · reason shrink_only_lists_not_shrinking can reach its own tolerance of zero (wave-1 F21)

2026-08-30T10:47:28Z rescope · item add TOOL-aScouredKit-5 · reason drift-audit's conf parser matches the source its docstring claims to copy, failing case observed first (wave-1 F10)

2026-08-30T10:47:28Z rescope · item add TOOL-aScouredKit-6 · reason the three per-file grep loops on the bar batch, at byte-identical output (wave-1 F14, F15, F16)

2026-08-30T10:47:29Z rescope · item add TOOL-aScouredKit-7 · reason the dead scope helpers in unattended.sh are deleted or wired (wave-1 F3)

2026-08-30T10:47:30Z rescope · item add TOOL-aScouredKit-8 · reason drift-audit stops printing a cardinality claim its own source retracted (wave-1 F22)

2026-08-30T10:47:31Z rescope · item add TOOL-aScouredKit-9 · reason drift-audit-state.js gains the two run-integrity fields its sibling harness has (wave-1 F12)

2026-08-30T11:20:20Z rescope · item add TOOL-aScouredKit-10 · reason the leg-hold predicate is now written twice and nothing asserts the pair; reported as a backlog row rather than half-gated here

2026-08-30T11:25:41Z rescope · item add TOOL-aScouredKit-11 · reason the gate-leg manifest write-back guards on THIS step's problems, not the whole run's (wave-2 blocker 6)

2026-08-30T11:25:42Z rescope · item add TOOL-aScouredKit-12 · reason two shipped gate legs receive the path the descriptor already holds, instead of a literal (wave-2 blocker 1, high 3)

2026-08-30T11:25:43Z rescope · item add TOOL-aScouredKit-13 · reason plan and apply honour the target's own declared kits list (wave-2 high 7)

2026-08-30T11:25:44Z rescope · item add TOOL-aScouredKit-14 · reason three prose defects in the load-bearing documents: two rules stated three times, one count contradicting its own breakdown (wave-2 15, 19, 14)

2026-08-30T11:41:30Z rescope · item add TOOL-aScouredKit-15 · reason the drift-audit adopter renders a Skill pointing at a sibling directory govkit never creates, and --check was blind because it compared two renders (wave-2 F9)

2026-08-30T11:43:04Z rescope · item add TOOL-aScouredKit-16 · reason reported with its measurement as a backlog row rather than half-built in this run

2026-08-30T11:43:05Z rescope · item add TOOL-aScouredKit-17 · reason reported with its measurement as a backlog row rather than half-built in this run

2026-08-30T11:43:06Z rescope · item add TOOL-aScouredKit-18 · reason reported with its measurement as a backlog row rather than half-built in this run

2026-08-30T11:43:06Z rescope · item add TOOL-aScouredKit-19 · reason reported with its measurement as a backlog row rather than half-built in this run

2026-08-30T11:43:07Z rescope · item add TOOL-aScouredKit-20 · reason reported with its measurement as a backlog row rather than half-built in this run

2026-08-30T11:43:08Z rescope · item add TOOL-aScouredKit-21 · reason reported with its measurement as a backlog row rather than half-built in this run

2026-08-30T11:43:09Z rescope · item add TOOL-aScouredKit-22 · reason reported with its measurement as a backlog row rather than half-built in this run

2026-08-30T11:43:09Z rescope · item add TOOL-aScouredKit-23 · reason reported with its measurement as a backlog row rather than half-built in this run

2026-08-30T11:43:10Z rescope · item add TOOL-aScouredKit-24 · reason reported with its measurement as a backlog row rather than half-built in this run

2026-08-30T11:43:11Z rescope · item add TOOL-aScouredKit-25 · reason reported with its measurement as a backlog row rather than half-built in this run

2026-08-30T11:43:11Z rescope · item add TOOL-aScouredKit-26 · reason reported with its measurement as a backlog row rather than half-built in this run

2026-08-30T12:10:12Z review · item aScouredKit · reason verdict BLOCKED · blockers 4

2026-08-30T12:14:19Z rescope · item add TOOL-aScouredKit-27 · reason closing-review finding reported with its measurement rather than half-built

2026-08-30T12:14:21Z rescope · item add TOOL-aScouredKit-28 · reason closing-review finding reported with its measurement rather than half-built

2026-08-30T12:14:22Z rescope · item add TOOL-aScouredKit-29 · reason closing-review finding reported with its measurement rather than half-built
