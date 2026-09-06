# aQuenchedHarness - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: c3eee6ee9fdf1a200c65b04a110614baf7b9c48d
phase: REVIEWING
branch-sha: faaea5f5693deffbb3d2c44dee2453d9e01fa460
branch-ref: refs/heads/branch/self-test-gates-performance-7e2cf2
mode: prompt
anchor-kind: run-branch
keepalive: 6a7a6206
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 274aa39b786c886991726896927337c0e3048e0c
anchor-ref: refs/heads/main
base: faaea5f5693deffbb3d2c44dee2453d9e01fa460

## Parked

2026-09-06T13:39:19Z rescope · item add TOOL-aQuenchedHarness-8 · reason Probing unit 2's ceiling-band FACT-QUESTION uncovered the actual root cause of the owner's 9h and 6h stalls, and it is neither a slow leg nor a loose ceiling. run-gates.sh calls ts_hb at exactly ONE site, leg completion (line 1150), while TS_TTL is 1800s because every shipped gate-profiles.txt row sets timeout=0. The longest leg, unattended kit gate, is recorded at 3837s. So on every full bar the holder's beacon goes stale mid-leg, the next bar reaps it as a stalled holder, and two bars run concurrently. Cross-ledger measurement over 12 worktree ledgers: the SAME leg varies 5.5x median and up to 47.1x across readings, exactly the contention that predicts. The runner's own source already carries a ponytail: comment naming this cliff, and the remedy it names (set timeout= on the profile row) has never been applied and would push TS_MAXWAIT to 12.8h if it were. Strictly beneficial, makes an observable this repo already measures better, makes nothing worse, and no M3 veto is tripped.
