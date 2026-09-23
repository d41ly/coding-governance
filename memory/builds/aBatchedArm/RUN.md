# aBatchedArm - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
parked-surfaced: yes
keepalive-reaped: yes
witness: 0bda01304f3dda643cfcbf9444f886e84c0ea810
phase: LANDING
branch-sha: c2db2f5d2d6100af08a09da113086d114c67b603
branch-ref: refs/heads/branch/unattended-checks-performance-a37d8d
mode: prompt
anchor-kind: run-branch
keepalive: c1d67ccd
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 09a22d2bf5c3fc51bdc3ccee8c727b0793664106
anchor-ref: refs/heads/main
base: c2db2f5d2d6100af08a09da113086d114c67b603

## Landing order

Restated at the closing fix (D3(a) of the round-1 closing review), because unit 5's S5 ordered the
calibrate first and unit 1's golden-writing step was owed "at the final pass" with no order pinned
between them — and either order wasted the pass. The eight direct shard runs come FIRST:
`bash tools/unattended/check-unattended.test.sh --shard k/8` for k in 1..8, each output to a file.
Then the paste: every `check_emitted "?"` call takes its group's observed set from the
`    observed:` lines beneath its `FAIL check_emitted:` line, the shard run it was read from named
beside the call. Re-run the affected shards until no `FAIL check_emitted:` line remains. Only then
the calibrate, `bash tools/run-gates/run-selftests.sh --pooled --calibrate --kit tools/unattended`,
which now refuses a sentinel-carrying row as UNTRAILED and keeps each row's output under
`<git-dir>/gate-logs/selftests/`; commit the evidence rows; then
`bash tools/unattended/run-unattended-gates.sh --pooled` GREEN; then the DoD flip. Shard 8's
`DERIVED, not measured` budget reading (D13) is re-measured at those direct shard runs, in the
closed vocabulary `measured <n>s on node a <date>, direct serial run …`, so `--rank` ranks again.

## Parked

2026-09-13T10:09:42Z rescope · item add TOOL-aBatchedArm-4 · reason Owner ruling 2026-09-10 on the parked scope question: the route is the shared runner. tools/run-gates/run-selftests.sh gets a slash-tolerant row checker and DECLARED execution modes, so pooled is available and serial stays possible when it is deliberately declared. This is the unit that unblocks TOOL-aBatchedArm-3, whose eight shard rows cannot be declared today (the row checker reds any slash-bearing argv token) and would run serially if they could (OUTER=1 except under --sweep, which withholds cost verdicts). A change to a shared runner grading 61 suites, added by owner instruction rather than by the run's own authority.

2026-09-13T10:50:23Z review · item TOOL-aBatchedArm-4 · reason verdict BLOCKED · blockers 8

2026-09-13T10:53:13Z rescope · item add TOOL-aBatchedArm-5 · reason Spec-audit round 1 of TOOL-aBatchedArm-4 B5: its S5 pooled hang bound was a scalar factor over the serial reading, the shape TOOL-dRetiredFork-40, TOOL-aPooledSweep-2 section 3 and the full-sweep record all rejected, and derive-ceilings.py already owns the evidence shape - a per-row observed reading under the declared condition, monotone, with ceiling-margin.txt's max(120s, 1.0 x max) headroom. That bound is the mechanism that killed 14 of 58 suites once, so it is its own unit under M2 rather than a paragraph in the mode unit. Consumes the rows from unit 3 and the modes from unit 4.

2026-09-13T11:20:53Z review · item TOOL-aBatchedArm-4 · reason verdict BLOCKED · blockers 3

2026-09-13T11:53:08Z review · item TOOL-aBatchedArm-4 · reason verdict BLOCKED · blockers 4 · NON-CONVERGENT · disposition fold

2026-09-13T11:59:15Z brief · item TOOL-aBatchedArm-4 · reason b56f676efee7 memory/builds/aBatchedArm/prompts/2026-09-13-prompt-TOOL-aBatchedArm-4-build-brief.md

2026-09-13T12:06:10Z dispatch · item 1ed8bf22 TOOL-aBatchedArm-4 · reason tools/run-gates/run-selftests.sh tools/run-gates/run-selftests.test.sh tools/unattended/run-unattended-gates.sh tools/unattended/README.md tools/unattended/kit.toml .githooks/gate-env.sh AGENTS.md memory/guides/SESSION-KICKOFF.md memory/builds/aBatchedArm/spec/2026-09-13-spec-TOOL-aBatchedArm-4.md memory/builds/aBatchedArm/build/2026-09-13-build-TOOL-aBatchedArm-4-1-acceptance-ledger.md memory/builds/aBatchedArm/README.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-13T13:40:07Z review · item TOOL-aBatchedArm-3 · reason verdict BLOCKED · blockers 9

2026-09-13T14:14:49Z review · item TOOL-aBatchedArm-3 · reason verdict BLOCKED · blockers 8

2026-09-13T15:22:35Z review · item TOOL-aBatchedArm-3 · reason verdict BLOCKED · blockers 4

2026-09-13T15:51:57Z review · item TOOL-aBatchedArm-3 · reason verdict BLOCKED · blockers 12 · NON-CONVERGENT · disposition fold

2026-09-13T16:16:02Z brief · item TOOL-aBatchedArm-3 · reason 15b11de5028a memory/builds/aBatchedArm/prompts/2026-09-13-prompt-TOOL-aBatchedArm-3-build-brief.md

2026-09-13T16:26:37Z dispatch · item ecc3a3cc TOOL-aBatchedArm-3 · reason tools/unattended/check-unattended.test.sh tools/run-gates/selftest-budgets.txt tools/install-prefix-carried.txt tools/run-gates/run-selftests.sh tools/run-gates/run-selftests.test.sh tools/unattended/run-unattended-gates.sh memory/builds/aBatchedArm/spec/2026-09-10-spec-TOOL-aBatchedArm-3.md memory/builds/aBatchedArm/build/2026-09-13-build-TOOL-aBatchedArm-3-1-acceptance-ledger.md memory/builds/aBatchedArm/README.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-13T19:40:19Z brief · item TOOL-aBatchedArm-3 · reason de469904de2f memory/builds/aBatchedArm/prompts/2026-09-13-prompt-TOOL-aBatchedArm-3-build-brief.md

2026-09-13T19:42:22Z dispatch · item 77f3946f TOOL-aBatchedArm-3 · reason tools/unattended/check-unattended.test.sh tools/run-gates/selftest-budgets.txt tools/install-prefix-carried.txt tools/run-gates/run-selftests.sh tools/run-gates/run-selftests.test.sh tools/unattended/run-unattended-gates.sh memory/guides/SESSION-KICKOFF.md memory/builds/aBatchedArm/spec/2026-09-10-spec-TOOL-aBatchedArm-3.md memory/builds/aBatchedArm/build/2026-09-13-build-TOOL-aBatchedArm-3-1-acceptance-ledger.md memory/builds/aBatchedArm/README.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-14T08:24:27Z review · item TOOL-aBatchedArm-5 · reason verdict BLOCKED · blockers 3

2026-09-14T09:00:12Z review · item TOOL-aBatchedArm-5 · reason verdict BLOCKED · blockers 2

2026-09-14T09:39:59Z review · item TOOL-aBatchedArm-5 · reason verdict BLOCKED · blockers 1

2026-09-14T10:27:15Z review · item TOOL-aBatchedArm-5 · reason verdict BLOCKED · blockers 2 · NON-CONVERGENT · disposition fold

2026-09-14T10:34:15Z brief · item TOOL-aBatchedArm-5 · reason f5c01a60e141 memory/builds/aBatchedArm/prompts/2026-09-14-prompt-TOOL-aBatchedArm-5-build-brief.md

2026-09-14T10:44:23Z dispatch · item e82d4053 TOOL-aBatchedArm-5 · reason tools/run-gates/run-selftests.sh tools/run-gates/run-selftests.test.sh tools/run-gates/selftest-pooled-evidence.txt tools/run-gates/kit.toml tools/run-gates/selftest-budgets.txt tools/gate-legs.json tools/unattended/run-unattended-gates.sh tools/unattended/kit.toml .githooks/gate-env.sh memory/guides/SESSION-KICKOFF.md memory/builds/aBatchedArm/spec/2026-09-13-spec-TOOL-aBatchedArm-5.md memory/builds/aBatchedArm/build/2026-09-14-build-TOOL-aBatchedArm-5-1-acceptance-ledger.md memory/builds/aBatchedArm/README.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-14T11:13:18Z brief · item TOOL-aBatchedArm-1 · reason 266624e19ca0 memory/builds/aBatchedArm/prompts/2026-09-14-prompt-TOOL-aBatchedArm-1-build-brief.md

2026-09-14T11:27:52Z dispatch · item 1d8abce4 TOOL-aBatchedArm-1 · reason tools/unattended/check-unattended.test.sh memory/builds/aBatchedArm/spec/2026-09-10-spec-TOOL-aBatchedArm-1.md memory/builds/aBatchedArm/build/2026-09-14-build-TOOL-aBatchedArm-1-1-acceptance-ledger.md memory/builds/aBatchedArm/README.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-14T11:35:21Z decision · item TOOL-aBatchedArm-1 S2: which groups, and from what expected set · reason QUESTION: TOOL-aBatchedArm-1 S2 converted ZERO groups at 46b12b93 and the run cannot decide how to convert any. Measured by a classifier over the 332 reset_tree-led blocks (rules and counts in the unit's acceptance ledger): with every existing hit line byte-identical as the build brief requires, 10 blocks are batchable and no two are adjacent; allowing the one token hit "$(run)" to hit "$out" gives 112 batchable blocks and 19 contiguous groups of 2 or 3 (43 blocks, 24 of 285 invocations). But emitted grades the SET of signatures the tree fires, the brief derives that set from the arms, and three of the 19 are proven from the checker's source to fire branches their arms never name (PHASES_CORE blank fires the TERMINAL-phase loop and check 4; DOD_CORE blank fires check 16's table join; rm VERBS.template.md fires check 26 beside check 10), so a derived set is incomplete, emitted reds on it by design, and the spec's own rollout rule reverts the tranche; the other 16 are unknowable without an observed run, which the 2026-09-14 ruling forbids. OPTIONS: (a) write each group's expected set from an OBSERVED run at the final pass - the recorded-golden shape the spec's section 4 rejected, so not the run's to take; (b) weaken emitted to a subset check (every expected signature present, extras ignored), which deletes the collateral detection AC2 grades; (c) convert only the groups whose complete emission is proven from the checker's source, group by group, with the observed run as the proof - a per-group reading the owner has not priced; (d) retire S2 and keep the helper as the mechanism unit 2's linter grades. REFUSED because every option either takes a rejected alternative, narrows a stated acceptance criterion, or needs the run the ruling forbids, and M3 delegates none of those.

2026-09-14T13:55:47Z brief · item TOOL-aBatchedArm-1 · reason 2bd069988f26 memory/builds/aBatchedArm/prompts/2026-09-14-prompt-TOOL-aBatchedArm-1-build-brief-2.md

2026-09-14T13:58:00Z dispatch · item 7ab53fac TOOL-aBatchedArm-1 · reason tools/unattended/check-unattended.test.sh memory/builds/aBatchedArm/spec/2026-09-10-spec-TOOL-aBatchedArm-1.md memory/builds/aBatchedArm/build/2026-09-14-build-TOOL-aBatchedArm-1-2-acceptance-ledger.md memory/builds/aBatchedArm/README.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-14T14:28:38Z dispatch · item 4792ad4c TOOL-aBatchedArm-1 · reason tools/unattended/check-unattended.test.sh memory/builds/aBatchedArm/spec/2026-09-10-spec-TOOL-aBatchedArm-1.md memory/builds/aBatchedArm/build/2026-09-14-build-TOOL-aBatchedArm-1-2-acceptance-ledger.md memory/builds/aBatchedArm/build/2026-09-14-build-TOOL-aBatchedArm-1-1-acceptance-ledger.md memory/builds/aBatchedArm/README.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-14T14:33:04Z brief · item TOOL-aBatchedArm-2 · reason 13c75edc8465 memory/builds/aBatchedArm/prompts/2026-09-14-prompt-TOOL-aBatchedArm-2-build-brief.md

2026-09-14T14:45:04Z dispatch · item 85a47ca3 TOOL-aBatchedArm-2 · reason tools/unattended/check-arms-groups.sh tools/unattended/check-arms-groups.test.sh tools/gate-legs.json tools/run-gates/selftest-budgets.txt tools/install-prefix-carried.txt tools/unattended/kit.toml tools/govkit/subject-pins.tsv memory/guides/SESSION-KICKOFF.md memory/builds/aBatchedArm/spec/2026-09-10-spec-TOOL-aBatchedArm-2.md memory/builds/aBatchedArm/build/2026-09-14-build-TOOL-aBatchedArm-2-1-acceptance-ledger.md memory/builds/aBatchedArm/README.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-14T16:04:55Z review · item TOOL-aBatchedArm-1 · reason verdict BLOCKED · blockers 4

2026-09-14T17:45:59Z review · item TOOL-aBatchedArm-1 · reason verdict CLEAN · blockers 0 · CONVERGED

2026-09-15T11:14:16Z rescope · item add TOOL-aBatchedArm-2 · reason LATE record at the landing: this unit was specced under M2 on 2026-09-10 in the commits after the run's first live-phase commit d5e301f5 (unit 1's spec), so the roster the run entered BUILDING with held unit 1 alone; check 24's ADD arm named the gap at the final gate pass and the row is written now rather than the record left contradicting the roster it built

2026-09-15T11:14:18Z rescope · item add TOOL-aBatchedArm-3 · reason LATE record at the landing: this unit was specced under M2 on 2026-09-10 in the commits after the run's first live-phase commit d5e301f5 (unit 1's spec), so the roster the run entered BUILDING with held unit 1 alone; check 24's ADD arm named the gap at the final gate pass and the row is written now rather than the record left contradicting the roster it built

2026-09-15T11:27:40Z review · item aBatchedArm · reason verdict BLOCKED · blockers 13

2026-09-15T11:27:40Z review · item aBatchedArm · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED
