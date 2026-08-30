# aScouredKit - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 093730e40355d6a04300966f791f2634379e8b45
phase: RESEARCHING
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
