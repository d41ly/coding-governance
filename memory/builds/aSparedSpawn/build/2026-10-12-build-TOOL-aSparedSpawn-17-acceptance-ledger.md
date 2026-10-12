# Acceptance ledger — TOOL-aSparedSpawn-17

**Serves:** journal TOOL-aSparedSpawn-17

Node `a`, 2026-10-12, bash 5.3 under MSYS. The pass ran no bar, no suite, no held leg and no slice
of a suite. AC1 and AC2 were observed through the instrument committed beside this ledger,
`2026-10-12-build-TOOL-aSparedSpawn-17-direct-checks.sh`, over a hand-built two-leg scratch repo,
once with the changed runner and once with the base runner `3f100e9e` (whose `run-gates.sh` is
f479ba42's). Its `sampled` case is the control: both runners print the same lines, so the existing
sampled branch is unchanged. `bash -n` passed on the runner, the evidence suite and the instrument.
The spawn counts did not move: `fork-count.sh --only run-gates-1leg` measured 51 and
`fork-count.sh --only run-gates-2leg` 53, the figures `TOOL-aSparedSpawn-16` AC3 pins at f479ba42 (both rows still read
STALE against their old ceilings, which that unit lowers). `sh_hygiene.py --spawn-idioms` over the
runner reports `cat-file` at 16 against 15 declared; the diff adds no `$(`, and the runner's `cat`
lines are identical to the base's, so that count predates this unit and is `TOOL-aSparedSpawn-16`
AC2's. `check-arms.py --check` names the same six unarmed runner sites it named before.

**Evidences:** TOOL-aSparedSpawn-17
- AC1 — `direct-checks.sh aged` — changed runner: the aged bar printed `pa was reused on 10 runs in a row, so it executes`, `GATE FAIL  pa`, rc 1 and `cache disagreement · pa · <key>`; the entry was erased, a quarantine file was written, and after a clean green bar re-earned the key the reuse bar printed `GATE ok    pa` beside `GATE reuse pb`. Base runner: the same aged red left the entry and wrote no quarantine, and the next reuse bar printed `GATE reuse pa`, the red the criterion names. The suite arm `17-AC1` in `run-gates.evidence.test.sh` is OWED at VERIFYING.
- AC2 — `direct-checks.sh plain` — changed runner: a plain bar with no `GATE_REUSE` redded `pa` against its cached `ok`, printed `cache disagreement · pa · <key>`, erased the entry and quarantined the leg; after a clean green bar re-earned the key, the next `GATE_REUSE=1` bar printed `GATE ok    pa` and its control `GATE reuse pb`. Base runner: the entry survived, no quarantine, and the reuse bar printed `GATE reuse pa`. The suite arm `17-AC2` in `run-gates.evidence.test.sh` is OWED at VERIFYING.
- AC3 — `grep -n 'by TOOL-aSparedSpawn-17' tools/run-gates/run-gates.evidence.test.sh` — one `RAISED 151 -> 163` line, and `FLOOR_ASSERTIONS=163`, the two arms' twelve assertions read in the diff (five and seven). Whether the floor sits at or below the executed count is OWED at VERIFYING, when the suite runs.
- AC4 — `grep -n 'whatever drew the execution' tools/run-gates/README.md` — prints the reuse section's new rule, under the soundness sample paragraph.
