# aWokenSentinel - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 5f9648d61c020cf3ba902d3c6acc4e8b4992ab2b
phase: RUNNING
branch-sha: 5f9648d61c020cf3ba902d3c6acc4e8b4992ab2b
branch-ref: refs/heads/branch/unattended-kit-keepalive-a29498
mode: prompt
run-branch: refs/heads/branch/unattended-kit-keepalive-a29498
anchor-kind: run-branch
keepalive: f1209d79
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 4cf0944dbdce94714870f26760936bc5edabc64e
anchor-ref: refs/heads/main
base: 5f9648d61c020cf3ba902d3c6acc4e8b4992ab2b

## Parked

2026-09-16T12:00:05Z rescope · item add TOOL-aWokenSentinel-7 · reason Measured 2026-09-16: the Stop hook's stdin carries session_crons, the cron store no script can reach. keepalive-reaped stops being an attestation (TOOL-aPromptedMandate-11, OPEN since 08-18) and becomes a check against the last stop the hook recorded. Discovered by unit 3's probe; a second mechanism, so its own unit, ordered last.

2026-09-20T10:27:09Z review · item aWokenSentinel-spec-set-r1 · reason verdict BLOCKED · blockers 3 · BOUNDED · disposition promote

2026-09-20T10:36:24Z rescope · item add TOOL-aWokenSentinel-8 · reason spec-audit round 1 B1 BLOCKER (raw 18, 29, 43): the --landed refusal's remedy ends a turn spec 3's decision table ALLOWS at FINISHED-UNSTAMPED, so every wired landing wedges at LANDING; promoted to the stop-guard's landing-unstamped BLOCK row, which is the continuation the remedy promises

2026-09-20T10:36:25Z rescope · item add TOOL-aWokenSentinel-9 · reason spec-audit round 1 H1 HIGH (raw 1, 21, 30, 44): spec 7's second --status line reds the suite's whole-output reader at unattended.test.sh:1874 and the driver header's one-line promise; promoted to the listing as a FIELD on the one status line, with the one-line promise made an arm

2026-09-20T10:36:26Z rescope · item add TOOL-aWokenSentinel-10 · reason spec-audit round 1 H2 HIGH (raw 19, 31): STOP_GUARD_BLOCKS reaches the conf example with no protocol section 8 row and no unit owning the root-conf line, so check 22 reds from the hook's commit to the close; promoted to the knob's declaration set across every carrier check 22 and spec 6 AC6 read

2026-09-20T10:36:26Z rescope · item add TOOL-aWokenSentinel-11 · reason spec-audit round 1 H3 HIGH (raw 4, 20, 34): spec 5 spells the sidecar root inline and spec 7's AC12 pins the driver's rev-parse count at 1 with no unit scoped to fix the second spelling; promoted to a kit-gate check that the driver holds ONE sidecar-root derivation, binding every unit

2026-09-20T10:36:27Z rescope · item add TOOL-aWokenSentinel-12 · reason spec-audit round 1 H4 HIGH (raw 22): the resume tick kills a live tree before consulting login, so a logged-out node kills a session it cannot resume; promoted to the login-before-kill order with the arm that observes a surviving process under a logged-out CLI

2026-09-20T10:36:28Z rescope · item add TOOL-aWokenSentinel-13 · reason spec-audit round 1 H5 HIGH (raw 26, 33): the tick's read_bound_key calls read the calling shell with no conf sourced and CONF unset, so every tick takes the defaults and the NOTE names no file; promoted to the tick sourcing the root conf before its bound reads, with arms under a declared key

2026-09-20T10:36:28Z rescope · item add TOOL-aWokenSentinel-14 · reason spec-audit round 1 H6 HIGH (raw 32): both real-driver arms borrow adopt-unattended.test.sh's seed(), which never commits, so --liveness fails 52 on an unborn HEAD and spec 3 AC11 and spec 4 AC10 can never go green; promoted to the seed committing once so every borrower inherits a born HEAD
