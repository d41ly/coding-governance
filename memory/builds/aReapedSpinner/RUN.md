# aReapedSpinner - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
parked-surfaced: yes
keepalive-reaped: yes
witness: ed127313834f9cb9ca2d06996c361c1be221bf12
phase: LANDING
branch-sha: e2b82a53dd8e9e422aea96bd57bcf6e63b5eb96c
branch-ref: refs/heads/branch/gate-runner-process-monitor-0d0fa8
mode: prompt
anchor-kind: run-branch
keepalive: bc67bed5
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: d499258daca17f851ab1e4a359bb6c6aa106c0f6
anchor-ref: refs/heads/main
base: e2b82a53dd8e9e422aea96bd57bcf6e63b5eb96c

## Parked

2026-09-07T22:50:56Z review · item TOOL-aReapedSpinner-1 · reason verdict BLOCKED · blockers 6

2026-09-07T23:28:44Z review · item TOOL-aReapedSpinner-1 · reason verdict BLOCKED · blockers 5

2026-09-08T00:04:36Z review · item TOOL-aReapedSpinner-1 · reason verdict BLOCKED · blockers 8 · NON-CONVERGENT · disposition fold

2026-09-08T00:08:15Z dispatch · item a6352db2 TOOL-aReapedSpinner-6 · reason tools/process-monitor/kit.toml tools/process-monitor/adopt-process-monitor.sh tools/process-monitor/adopt-process-monitor.test.sh tools/process-monitor/README.md .process-monitor.conf tools/govkit/registry.toml .gitattributes

2026-09-08T00:14:42Z brief · item TOOL-aReapedSpinner-6 · reason eabdd4264895 memory/builds/aReapedSpinner/prompts/2026-09-08-prompt-TOOL-aReapedSpinner-6-brief.md

2026-09-08T00:16:16Z dispatch · item 3f798808 TOOL-aReapedSpinner-1 · reason tools/process-monitor/census.py tools/process-monitor/selftest.py tools/process-monitor/kit.toml memory/builds/aReapedSpinner/README.md

2026-09-08T00:24:49Z brief · item TOOL-aReapedSpinner-1 · reason 8c883a99c784 memory/builds/aReapedSpinner/prompts/2026-09-08-prompt-TOOL-aReapedSpinner-1-brief.md

2026-09-08T00:29:59Z brief · item TOOL-aReapedSpinner-2 · reason 3cb4483f7f1a memory/builds/aReapedSpinner/prompts/2026-09-08-prompt-TOOL-aReapedSpinner-2-brief.md

2026-09-08T00:32:20Z brief · item TOOL-aReapedSpinner-3 · reason 8341dd4da563 memory/builds/aReapedSpinner/prompts/2026-09-08-prompt-TOOL-aReapedSpinner-3-brief.md

2026-09-08T00:43:50Z brief · item TOOL-aReapedSpinner-4 · reason 143c183c1514 memory/builds/aReapedSpinner/prompts/2026-09-08-prompt-TOOL-aReapedSpinner-4-brief.md

2026-09-08T00:45:02Z dispatch · item 2033e853 TOOL-aReapedSpinner-7 · reason tools/run-gates/run-gates.sh tools/run-gates/run-gates.test.sh

2026-09-08T00:45:32Z dispatch · item 2033e853 TOOL-aReapedSpinner-7 · reason tools/run-gates/run-gates.sh tools/run-gates/run-gates.test.sh tools/process-monitor/reap.py tools/process-monitor/selftest.py

2026-09-08T01:06:14Z dispatch · item 2033e853 TOOL-aReapedSpinner-5 · reason tools/process-monitor/procmon-hook.js tools/process-monitor/kit.toml tools/process-monitor/adopt-process-monitor.sh tools/process-monitor/adopt-process-monitor.test.sh .claude/settings.json

2026-09-08T01:09:38Z brief · item TOOL-aReapedSpinner-5 · reason ec696ec086bd memory/builds/aReapedSpinner/prompts/2026-09-08-prompt-TOOL-aReapedSpinner-5-brief.md

2026-09-08T01:17:53Z brief · item TOOL-aReapedSpinner-7 · reason 4c6b2ab3ff4b memory/builds/aReapedSpinner/prompts/2026-09-08-prompt-TOOL-aReapedSpinner-7-brief.md

2026-09-08T01:44:44Z review · item aReapedSpinner · reason verdict BLOCKED · blockers 3

2026-09-08T02:32:47Z review · item aReapedSpinner · reason verdict BLOCKED · blockers 3 · NON-CONVERGENT · disposition fold

2026-09-08T19:14:30Z decision · item The full GATE_SELFTESTS bar was never seen green, and landing proceeded on owner instruction to skip it · reason Five legs are red on clean main with verified one-line fixes filed (rows 11, 18, 19) and were deliberately not fixed here, since they sit in govkit, codebase-map and memory-recall, which this build's diff does not touch. A sixth class is new: TOOL-aReapedSpinner-23, ceilings calibrated against the ticker hang. The last bar this build saw was RED at 13/104, and none of the 13 was traced to this kit.

2026-09-08T19:14:32Z decision · item Two pre-existing defects were fixed outside this build's scope · reason The ticker fd-hold and the canary's unreachable wall arm, both in tools/run-gates/ which this build already edits, both one line, both recorded (rows 17 and 21, decisions 20 and 22). Each is independently revertable. Without them no full selftests bar can pass at all, so the alternative was a Definition of Done that could never be met.

2026-09-08T19:24:53Z override · item gates-green · reason Owner instruction, 2026-09-08: skip the bar and land it. The last full GATE_SELFTESTS run was RED at 13/104 and none of the 13 was traced to this kit — five reproduce on clean main at d499258d with verified fixes filed (rows 11, 18, 19), and the rest are TOOL-aReapedSpinner-23, ceilings calibrated against the ticker hang this build removed. The kit's own two legs pass: census selftest 66 assertions, adopter selftest 31.
