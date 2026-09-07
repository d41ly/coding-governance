# aQuenchedHarness - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
parked-surfaced: yes
keepalive-reaped: yes — CronDelete 6a7a6206, and CronList is now empty
witness: d6623cd863d1209a391470364d8ad16a53369f59
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

2026-09-06T22:55:27Z decision · item TOOL-aQuenchedHarness-9 · reason A THIRD instance, and the count is now half the population. 'unattended driver selftest' is RED at 2569s against its declared 970s — 2.6x over budget AND failing. Three arms fail the same way: the suite's --brief argument-validation arms expect a refusal about the forged field, and the driver refuses earlier with check 49 (the unit is not in the README's generated units region), so the arms grade the wrong refusal. The unattended kit is untouched by this build, so this is pre-existing like its two siblings. THREE of the SIX suites in that kit are red, and the kit left the merge bar in 2026-08 under the owner ruling this build generalises — which is the thesis of the whole build arriving as evidence rather than as an argument: a suite nobody can afford to run is a suite that rots, and the only reason anyone knows is that unit 6 needed its seconds for a ranking.

2026-09-07T01:36:05Z decision · item TOOL-aQuenchedHarness-9 · reason A FOURTH instance, and now it is the majority of that kit. 'unattended gate selftest' — check-unattended.test.sh — measured 9067s (2h31m) against its declared 3800s and came back RED. It is the single largest row in the whole declared population: 25.2% of 36031s of recorded self-test time, more than three times the next suite. FOUR of the SIX unattended suites are red (adopter e2e, cross-component, driver, gate); only pass-order and playbook are green, and pass-order is green because 274aa39b already rebuilt it. All four are red at BASE. This is the direct measurement behind unit 7: the checker whose test costs two and a half hours is the same checker that is the longest leg on the bar.

2026-09-07T06:52:42Z decision · item TOOL-aQuenchedHarness-7 · reason OWNER DECISION, asked and unanswered because the turn was a keepalive. Measured a clean full bar on a quiet box at 1192s (19.9 min), 47 legs, leg-sum 2671s, pool efficiency 2.2x against width 8 — because ONE leg, 'unattended kit gate', is 1118s of it, 94 percent of the wall. Wall clock cannot fall below the longest leg however wide the pool is, so the bar is that one leg plus noise. This unit took it from 5420 external processes to 2321 with stdout byte-identical, which is 1.44-2.43x standalone, and the bar is correspondingly cheaper but still twenty minutes. To make the bar POOL-limited rather than leg-limited that leg has to drop under about 334s. The next lever is identified and not taken: 703 of its remaining 1022 git spawns are per-item rev-parse, cat-file -e and merge-base answering existence and ancestry about a small set of shas, which one batch pass would collapse. NOT DONE HERE because it changes what the checker asks git rather than how often, and this unit's entire safety property is that its stdout does not move. The owner chooses: keep cutting, or land.

2026-09-07T06:53:36Z rescope · item add TOOL-aQuenchedHarness-9 · reason The run discovered a unit it did not start with. Measuring the declared self-test population for unit 6's ranking meant RUNNING the six unattended suites, and four of them came back RED — all four red at BASE, so none is this build's doing and nobody could say how long they had been broken. Four parked decisions already named TOOL-aQuenchedHarness-9 and no spec carried it, which is the citing-a-dangling-id shape. It enters the roster DEFERRED: the findings are measured, the repair is not this build's, and folding an unbounded repair job into a unit whose job is a measured cost reduction would make both unfalsifiable.

2026-09-07T07:49:01Z review · item aQuenchedHarness · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-07T08:22:00Z rescope · item retire TOOL-aQuenchedHarness-9 · reason Retired from this build's roster, not abandoned. The id ALREADY had a home before this run touched it: a backlog row in memory/backlog/TOOL.md, open since the govkit selftest's two red arms were found. Adding it as a unit gave one question two answers, which is the class this repo files most often. The spec stays as the record of what was MEASURED — four of six unattended suites red, with seconds, budgets and a diagnosed cause for two — and points at the backlog row, which is where the repair will be scheduled. The measurement was worth keeping; the roster slot was not.
