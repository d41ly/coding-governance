# aBriskPreflight - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
asks-at-landing: TOOL-aBriskPreflight-8=OPEN TOOL-aBriskPreflight-9=OPEN TOOL-aBriskPreflight-13=OPEN TOOL-aBriskPreflight-14=OPEN TOOL-aBriskPreflight-15=OPEN TOOL-aBriskPreflight-16=OPEN TOOL-aBriskPreflight-17=OPEN TOOL-aBriskPreflight-18=OPEN
units-at-landing: TOOL-aBriskPreflight-1 TOOL-aBriskPreflight-10 TOOL-aBriskPreflight-5 TOOL-aBriskPreflight-6 TOOL-aBriskPreflight-2 TOOL-aBriskPreflight-4 TOOL-aBriskPreflight-3 TOOL-aBriskPreflight-7 TOOL-aBriskPreflight-11 TOOL-aBriskPreflight-12
hold-run: 
hold-streak: 1 · at 973dc13e
resume-owed: none · owner
held-at: 2026-10-12T05:29:58Z
hold-reason: TOOL-aBriskPreflight-11 (promoted from the closing review's HIGH H1) is parked on spec fork F2: priced at the worst host reading on record, PREFLIGHT_CEILING derives to about 4200 s, above GATE_BOUND 3600 s, and every option the run could take trips spec 7's AC8, raises a bound, or picks the selector by its outcome. The other eleven units are CLOSED and the work is sound; the bar's remaining reds are other builds' offenders on origin/main, read OWN only through the comparator rule. Decide F2, then build unit 11 (or retire it with a reason) and land.
hold-until: owner
hold-code: owner-decision
held-from: VERIFYING
gates-run: unattended-179177613053776420063-779951 4bb77a0d
parked-surfaced: yes
keepalive-reaped: yes
refreshed-at: 37200355d6033895cd156ec962928fd264084c2b · handoff · 0 touching
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 2b0cd160a2b0cc771abd2aad6ebcd0bf1e55ada3
phase: VERIFYING
may: none
mode: prompt
run-branch: refs/heads/branch/sleepy-kapitsa-1f69c8
anchor-kind: local
cli-version: 2.1.293
lease-utc: 2026-10-12T16:10:58Z
pid-image: claude.exe
host: compeeto-agent
pid: 11836
session: 653ff713-97af-487f-8f4e-2f4c9c73a605
keepalive: 50da7a17
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: b726385f2b5b8fd16802925c02104377253a9045
anchor-ref: refs/heads/main
base: 271a90045723817f694de4d22c56f88dbcd0063e

## Parked

2026-10-11T03:40:27Z dispatch · item a0a35056 TOOL-aBriskPreflight-1 · reason tools/check-wiring.sh tools/check-wiring.test.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-1-spawns-ab.md memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-1.md memory/builds/aBriskPreflight/README.md memory/LIVE.md memory/ledger/2026-10.md memory/map/generated/symbols.json

2026-10-11T03:41:11Z brief · item TOOL-aBriskPreflight-1 · reason 8740a5745416 memory/builds/aBriskPreflight/prompts/2026-10-11-prompt-TOOL-aBriskPreflight-1-build-brief.md

2026-10-11T05:59:29Z dispatch · item e8932e9f TOOL-aBriskPreflight-1 · reason tools/check-wiring.sh tools/check-wiring.test.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-1-spawns-ab.md memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-1.md memory/builds/aBriskPreflight/README.md memory/LIVE.md memory/ledger/2026-10.md memory/map/generated/symbols.json

2026-10-11T05:59:38Z brief · item TOOL-aBriskPreflight-1 · reason f39eea28b6eb memory/builds/aBriskPreflight/prompts/2026-10-11-prompt-TOOL-aBriskPreflight-1-rebuild-brief.md

2026-10-11T06:39:36Z dispatch · item d6859204 TOOL-aBriskPreflight-5 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-5-walk-probe.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-5-walk-ab.md memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-5.md memory/builds/aBriskPreflight/README.md memory/LIVE.md memory/ledger/2026-10.md memory/map/generated/symbols.json

2026-10-11T06:39:51Z brief · item TOOL-aBriskPreflight-5 · reason 61f6904962f7 memory/builds/aBriskPreflight/prompts/2026-10-11-prompt-TOOL-aBriskPreflight-5-build-brief.md

2026-10-11T07:28:52Z dispatch · item 138b0c45 TOOL-aBriskPreflight-6 · reason .githooks/pre-push .githooks/straggler-guard.test.sh .githooks/pre-push.test.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-6-claim-push.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-6-claim-push-ab.md memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-6.md memory/builds/aBriskPreflight/README.md memory/LIVE.md memory/ledger/2026-10.md memory/map/generated/symbols.json

2026-10-11T07:29:00Z brief · item TOOL-aBriskPreflight-6 · reason 29e8bec69500 memory/builds/aBriskPreflight/prompts/2026-10-11-prompt-TOOL-aBriskPreflight-6-build-brief.md

2026-10-11T08:09:46Z dispatch · item 20a9e88e TOOL-aBriskPreflight-2 · reason tools/check-wiring.sh tools/check-wiring.test.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-2-spawns-ab.md memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-2.md memory/builds/aBriskPreflight/README.md memory/LIVE.md memory/ledger/2026-10.md memory/map/generated/symbols.json

2026-10-11T08:09:56Z brief · item TOOL-aBriskPreflight-2 · reason 162d8aaea8b6 memory/builds/aBriskPreflight/prompts/2026-10-11-prompt-TOOL-aBriskPreflight-2-build-brief.md

2026-10-11T10:07:31Z dispatch · item 900d74e6 TOOL-aBriskPreflight-4 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/map/features/unattended-stops.md memory/map/generated/symbols.json memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-4.md memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-4-probes-ab.md memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-4-probes-ab.sh memory/builds/aBriskPreflight/README.md memory/LIVE.md memory/ledger/2026-10.md

2026-10-11T10:08:05Z brief · item TOOL-aBriskPreflight-4 · reason 5651db253a5e memory/builds/aBriskPreflight/prompts/2026-10-11-prompt-TOOL-aBriskPreflight-4-build-brief.md

2026-10-11T13:58:36Z dispatch · item 2a64d49b TOOL-aBriskPreflight-3 · reason memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-3-arm-windows.py memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-3-wiring-scope.md memory/builds/aBriskPreflight/BACKLOG.md memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-3.md memory/builds/aBriskPreflight/README.md memory/LIVE.md memory/ledger/2026-10.md memory/map/generated/symbols.json memory/backlog/TOOL.md

2026-10-11T14:00:18Z brief · item TOOL-aBriskPreflight-3 · reason 521337f9e3b3 memory/builds/aBriskPreflight/prompts/2026-10-11-prompt-TOOL-aBriskPreflight-3-build-brief.md

2026-10-11T14:42:25Z rescope · item add TOOL-aBriskPreflight-10 · reason origin/main tracks .githooks/pre-commit 100644 since the aDistilledCharter reconcile 60bea5e80; this build met it as a check-4 refusal of its own A/B fixture after the mid-build merge. Restoring 100755 makes the wiring hooks-mode arm, an observable this repo measures, strictly better and makes nothing worse

2026-10-11T15:02:48Z brief · item TOOL-aBriskPreflight-10 · reason 60d7c4d96e4b memory/builds/aBriskPreflight/prompts/2026-10-11-prompt-TOOL-aBriskPreflight-10-build-brief.md

2026-10-11T15:27:11Z dispatch · item e4fd1b83 TOOL-aBriskPreflight-10 · reason .githooks/pre-commit memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-10.md memory/builds/aBriskPreflight/prompts/2026-10-11-prompt-TOOL-aBriskPreflight-10-build-brief.md memory/builds/aBriskPreflight/README.md memory/LIVE.md memory/ledger/2026-10.md

2026-10-11T19:05:19Z dispatch · item b91d30f7 TOOL-aBriskPreflight-7 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/README.md memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-7.md memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ceilings.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ceiling-rows.log memory/builds/aBriskPreflight/README.md memory/LIVE.md memory/ledger/2026-10.md memory/map/generated/symbols.json

2026-10-11T19:06:10Z brief · item TOOL-aBriskPreflight-7 · reason 0455d49e591f memory/builds/aBriskPreflight/prompts/2026-10-11-prompt-TOOL-aBriskPreflight-7-build-brief.md

2026-10-11T21:19:28Z review · item aBriskPreflight · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED · highs 1 · minors 9 · disposition promote

2026-10-11T21:20:12Z rescope · item add TOOL-aBriskPreflight-11 · reason promoted from the closing diff review round 1, HIGH H1: the ceilings instrument's K_w drops the worst host-row fork reading, so WIRING_CEILING understates its own worst-on-record rule

2026-10-11T21:20:56Z rescope · item add TOOL-aBriskPreflight-12 · reason promoted from the closing diff review round 1: the two MEDIUMs (M1 unbound records and missing ledgers, M2 RB_TOOK start-to-read) and five LOWs (L1-L5) batched into one unit

2026-10-11T22:22:35Z decision · item TOOL-aBriskPreflight-11 F2: under the worst-on-record fork price (ab-AO-2's 2.53 s host reading, F1 resolved (a)), PREFLIGHT_CEILING derives to about 4200 s, above GATE_BOUND 3600 s, which spec 7's AC8 forbids. Which way? · reason Options seen: (i) the instrument's below-GATE_BOUND refusal applies to WIRING_CEILING only, since PREFLIGHT_CEILING kills nothing, built as its own unit (lifts WIRING_CEILING to 840 s, closes review H1) - recommended to the owner; (ii) raise GATE_BOUND to >= 4230 s; (iii) type a value below 3600 s by hand; (iv) price forks from after-arm rows only (F1 (b)). Refused: (i) amends spec 7's AC8, an owner-written-for criterion, and is a second mechanism; (ii) raises a bound, a non-goal of the prompt; (iii) is a typed value spec 7's AC8 reds; (iv) is a selector chosen by its outcome (M3 counter-rule). No survivor, so M3 parks it.

2026-10-11T22:41:23Z dispatch · item 89d72ea1 TOOL-aBriskPreflight-12 · reason tools/check-wiring.sh tools/check-wiring.test.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh .githooks/straggler-guard.test.sh memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-4.md memory/builds/aBriskPreflight/spec/2026-10-12-spec-TOOL-aBriskPreflight-12.md memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-1-host-state.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-1-run-timed.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-1-run-traced.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-1-runs.log memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-1-trace-gaps.py memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-1-trace-spawns.py memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-3-arm-windows.py memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-4-probes-ab.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-5-walk-probe.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-6-claim-push.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ab-prep.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ab-rows.log memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ab-run.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ceiling-rows.log memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ceilings.sh memory/builds/aBriskPreflight/build/2026-10-12-build-TOOL-aBriskPreflight-4-acceptance-ledger.md memory/builds/aBriskPreflight/build/2026-10-12-build-TOOL-aBriskPreflight-7-acceptance-ledger.md memory/builds/aBriskPreflight/build/2026-10-12-build-TOOL-aBriskPreflight-12-acceptance-ledger.md memory/builds/aBriskPreflight/README.md memory/LIVE.md memory/ledger/2026-10.md memory/map/generated/symbols.json memory/backlog/TOOL.md

2026-10-11T22:42:03Z brief · item TOOL-aBriskPreflight-12 · reason 433fe4a9b303 memory/builds/aBriskPreflight/prompts/2026-10-12-prompt-TOOL-aBriskPreflight-12-build-brief.md

2026-10-11T23:26:47Z decision · item TOOL-aBriskPreflight-7 AC10 lexicon half: is python tools/lexicon/lexicon.py --check exit 0 observed for unit 7? · reason Options seen: (i) write AC10 observed on gen_map alone; (ii) re-run lexicon now; (iii) amend spec 7 AC10. Neither feb305b0b nor any record holds the lexicon run. Re-run 2026-10-12 by TOOL-aBriskPreflight-12: rc 1, 1071 verb offenders over pin 1063, none in a file unit 7 touched, so the red is inherited and not unit 7's. Refused (iii): amending another unit's criterion is not this unit's scope. The ledger line names gen_map as its token and states the lexicon half as not observed at exit 0; the close's bar grades the lexicon leg

2026-10-11T23:41:34Z dispatch · item 89d72ea1 TOOL-aBriskPreflight-12 · reason tools/check-wiring.sh tools/check-wiring.test.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh .githooks/straggler-guard.test.sh memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-1.md memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-3.md memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-4.md memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-5.md memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-6.md memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-7.md memory/builds/aBriskPreflight/spec/2026-10-12-spec-TOOL-aBriskPreflight-12.md memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-1-host-state.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-1-run-timed.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-1-run-traced.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-1-runs.log memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-1-trace-gaps.py memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-1-trace-spawns.py memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-3-arm-windows.py memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-4-probes-ab.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-5-walk-probe.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-6-claim-push.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ab-prep.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ab-rows.log memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ab-run.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ceiling-rows.log memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ceilings.sh memory/builds/aBriskPreflight/build/2026-10-12-build-TOOL-aBriskPreflight-4-acceptance-ledger.md memory/builds/aBriskPreflight/build/2026-10-12-build-TOOL-aBriskPreflight-7-acceptance-ledger.md memory/builds/aBriskPreflight/build/2026-10-12-build-TOOL-aBriskPreflight-12-acceptance-ledger.md memory/builds/aBriskPreflight/README.md memory/LIVE.md memory/ledger/2026-10.md memory/map/generated/symbols.json memory/backlog/TOOL.md

2026-10-12T05:30:07Z handoff · item owner-decision · reason in the run worktree: bash tools/push-main.sh --prepare --slug aBriskPreflight && bash tools/push-main.sh --land --slug aBriskPreflight && bash tools/unattended/unattended.sh --settle aBriskPreflight

2026-10-12T05:30:08Z hold · item owner-decision · reason until owner · reaped 0fe01023 · resume none(owner)

2026-10-12T16:12:22Z resume · item aBriskPreflight · reason held · keepalive 50da7a17 · manual

2026-10-12T16:34:49Z dispatch · item 2c038d0d TOOL-aBriskPreflight-11 · reason memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ceilings.sh tools/unattended/unattended.sh tools/unattended/README.md memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-7.md memory/builds/aBriskPreflight/spec/2026-10-12-spec-TOOL-aBriskPreflight-11.md memory/builds/aBriskPreflight/build/2026-10-12-build-TOOL-aBriskPreflight-11-acceptance-ledger.md memory/builds/aBriskPreflight/README.md memory/LIVE.md memory/ledger/2026-10.md memory/map/generated/symbols.json

2026-10-12T16:35:24Z brief · item TOOL-aBriskPreflight-11 · reason 2326d74e6092 memory/builds/aBriskPreflight/prompts/2026-10-12-prompt-TOOL-aBriskPreflight-11-build-brief.md

2026-10-12T16:55:48Z rescope · item add TOOL-aBriskPreflight-19 · reason after the owner's 'land': three legs red on other builds' offenders at origin/main read OWN or MIXED here (install-prefix and both lexicon legs by comparator, harness arms by printed waivers), so the push boundary refuses; draining them is a blocker between the run and its own landing, adopted under protocol section 11

2026-10-12T17:19:48Z dispatch · item ef43b17f TOOL-aBriskPreflight-19 · reason .githooks/pre-push.test.sh tools/unattended/unattended.test.sh memory/project/unarmed-branches.txt memory/builds/aBriskPreflight/spec/2026-10-12-spec-TOOL-aBriskPreflight-19.md memory/builds/aBriskPreflight/build/2026-10-12-build-TOOL-aBriskPreflight-19-acceptance-ledger.md memory/builds/aBriskPreflight/README.md memory/LIVE.md memory/ledger/2026-10.md memory/map/generated/symbols.json

2026-10-12T17:20:18Z brief · item TOOL-aBriskPreflight-19 · reason 1e1294bf7ab4 memory/builds/aBriskPreflight/prompts/2026-10-12-prompt-TOOL-aBriskPreflight-19-build-brief.md
