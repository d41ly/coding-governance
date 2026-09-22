# Acceptance ledger — TOOL-aQuenchedHarness-1

**Serves:** journal TOOL-aQuenchedHarness-1

**Evidences:** TOOL-aQuenchedHarness-1

Tier-2 · node a · 2026-09-07. One line per numbered criterion, naming the observation that answered
it. THE SUITES THAT OWN MOST OF THESE ARMS WERE NOT RUN TO COMPLETION: `run-gates canary` and
`run-gates turnstile` were killed part-way to free the box for a clean whole-bar measurement the
owner had asked for. What replaces them, where it does, is a DIRECT observation taken today and named
as such; where nothing replaces them the line says NOT RE-OBSERVED, which is a different claim from
MET and is recorded as one.

- AC1 — MET, OBSERVED — `GATE_WALL=5 bash tools/run-gates/run-gates.sh` on the real tree exits RED naming the legs still outstanding: `still running at the wall: marker contracts` and `still running at the wall: govkit acceptance matrix`.
- AC2 — NOT RE-OBSERVED. The `GATE_WALL=0` control lives in the canary, which was killed part-way; without it the arm above is not proven to be measuring the wall rather than an unrelated red.
- AC3 — NOT RE-OBSERVED, but bounded by the same run: `GATE_WALL=5` returned in 22 s wall including startup, which is consistent with a 5 s bound and inconsistent with the 1192 s the same bar takes unbounded.
- AC4 — MET AS A MECHANISM, NOT AS A REPORT, and the distinction is the finding. `remove_descendants` deleted its `ps` snapshot one line BEFORE re-scanning it, so the survivor walk returned its seed and the report could never name a descendant. OBSERVED directly: with the snapshot the walk returns three pids, without it one. Fixed; the REPORT path still has no arm, which is AC6.
- AC5 — NOT RE-OBSERVED. The unknown-knob refusal is an arm of `tools/run-gates/run-gates.test.sh`, which was killed part-way.
- AC6 — NOT DONE, and confirmed absent by the closing review rather than merely unrun. No arm captures a pid; arm 4g's seven assertions would all pass if the wall killed only the leg's root and left every child alive. The review also found its fixture's advertised grandchild is a direct child, because bash exec-replaces a subshell whose only command is `sleep` — the same bash behaviour this build documents elsewhere as the reason a deleted probe graded nothing.
- AC7 — MET, OBSERVED — the same `GATE_WALL=5` run printed its profile line, its stuck-leg list and its verdict, and saved both durable records.
- AC8 — NOT RE-OBSERVED. An arm of `tools/run-gates/run-gates.turnstile.test.sh`, killed part-way.
- AC9 — MET, OBSERVED — `GATE_WALL=5 bash tools/run-gates/run-gates.sh` exited 1, not 0 and not 2.
- AC10 — MET, OBSERVED, AND IT WAS THE DEFECT. The breach block `exit 1`'d ABOVE the run record's verdict writer, so a breach left a header with no verdict — which this runner documents as its CRASH signal, making the one condition the wall exists to make legible the one nobody could read. Now `<git-dir>/gate-run/20260907T044630Z-512444/verdict` carries `verdict RED` and `wall_breach 5`. Three older run dirs in this repo still carry the crash signal.
- AC11 — NOT RE-OBSERVED as an arm, but the ordering it depends on was corrected earlier in this build: `$WORK/wall.breach` is written BEFORE the kill loop, so no leg is dispatched after a breach is decided.
