# aQuenchedHarness - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: ea03caa54f5bca040144048c09954efb5af6d355
phase: BUILDING
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

2026-09-06T14:02:12Z review · item TOOL-aQuenchedHarness-1 · reason verdict BLOCKED · blockers 6

2026-09-06T14:45:43Z review · item TOOL-aQuenchedHarness-1 · reason verdict BLOCKED · blockers 8 · NON-CONVERGENT · disposition fold

2026-09-06T14:55:04Z dispatch · item b91a206a TOOL-aQuenchedHarness-8 · reason tools/run-gates/run-gates.sh tools/run-gates/run-gates.turnstile.test.sh .lexicon.conf

2026-09-06T22:19:37Z decision · item TOOL-aQuenchedHarness-9 · reason Two more instances of the -9 class, both measured on a frozen clone of c63e4177 while taking unit 6's ranking readings, and both RED at BASE faaea5f5 as well, so neither is this build's doing. 'unattended cross-component': its fixture cp list never grew the verb carrier when TOOL-dFoldedVerdict-5 split VERBS.template.md out of the protocol, so check 10 and check 26 fire on the FIXTURE and every arm downstream grades that refusal instead of its own subject. 'unattended adopter e2e': arms 3b and 4 fail with the rendered .claude/skills/unattended/SKILL.md absent from the adopting tree. Both are the rot this build's thesis predicts for a suite that left the bar in 2026-08 and that nobody can afford to run. NOT fixed in unit 6: its spec section 3 says only the suites being ported move.
