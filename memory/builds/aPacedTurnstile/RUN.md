# aPacedTurnstile - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
keepalive-reaped: yes
parked-surfaced: yes
witness: 73b22de5810a8cc16ca01e9027aeec45b37f3470
phase: LANDING
branch-sha: 497d25d0ab47e29b29f08189473adf05f926399f
branch-ref: refs/heads/branch/unattended-apaced-turnstile-8bd231
anchor-kind: run-branch
keepalive: 29c9dc29
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 098bebd9876c8f2f61a528b5cc9ac0a6b5d7719a
anchor-ref: refs/heads/main
base: 497d25d0ab47e29b29f08189473adf05f926399f

## Parked

2026-08-18T10:53:26Z decision · item Six of the seven units are specced, audited and READY, and this run built only TOOL-aPacedTurnstile-1. Should the remaining six be carried by further unattended runs against this same build folder, or re-scoped now that unit 1 has moved the ground under them? · reason Refused because it is a SCOPE decision, which a standing mandate does not delegate (BUILD-METHOD M3). Options seen: (a) carry on in this run - rejected, each remaining unit is comparable in size to unit 1, which took the whole run and four review rounds, and a run that starts a unit it cannot finish leaves the tree half-moved with no green state, which is exactly what unit 1's own Rollout section forbids; (b) re-run /unattended per unit against the same build folder - viable, the build order sequences them and each lands its own green commit, and preflight now rotates a finished RUN.md so the folder is reusable; (c) re-scope the remaining six - the owner's call, and worth taking because unit 1 moved ground three of them stand on. What actually changed for them: the canary SPLIT into a shipped half and a gov-only half, so -3 AC6, -6 AC12 and -7 AC9 now have a named home that did not exist when they were written; the manifest is DERIVED rather than spelled, which -3's reorder must preserve; the report tail is a two-space contract every later report verb must conform to; and the leg count moved 70 to 73, which -3's chunk arithmetic reads.

2026-08-18T15:20:03Z override · item build-complete · reason Unmet for TWO independent reasons and neither is a machine-checkable claim this run can honestly satisfy. FIRST, the build README carries no roster marker pair, so build-complete cannot read a roster at all; that is a pre-existing gap in the authorization artifact, filed as TOOL-aPacedTurnstile-14 and deliberately NOT patched at close time, because editing the record a gate blocks on, at the moment it blocks, is the shape this kit exists to refuse. SECOND, and the substantive one: six of the seven units are OPEN. This run built exactly one, TOOL-aPacedTurnstile-1, and landed it green at 73/73 with its closing diff review folded. The other six are specced, four-times audited and READY, and the scope question of who carries them is parked as a decision the standing mandate does not delegate. What IS true and worth the override: the build's own order sequences units so each lands its own green commit, and unit 1 is a complete, reviewed, landable increment rather than a half-moved tree - its own Rollout section forbids the latter and the tree is not in it.
