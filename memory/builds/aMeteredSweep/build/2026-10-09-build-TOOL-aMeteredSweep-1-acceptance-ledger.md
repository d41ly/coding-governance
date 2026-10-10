# Acceptance ledger — TOOL-aMeteredSweep-1

**Serves:** journal TOOL-aMeteredSweep-1

Node `a`, 2026-10-07 to 2026-10-09. Every observation below ran beside another repository's bars,
which put one process spawn at 0.07 to 0.8 s against this clone's recorded floor of 21 ms; the
timings are about that machine. Three bars ran: the profiled bar at `fa68a767` (9 red), the
verification bar at `a3531d5e` (9 red: four fixed after it, two artifacts of a clone whose
`origin/HEAD` named the branch, two load timeouts and the canary), and a `GATE_FULL=1` bar at
`670436cd` with every non-self-test leg (one red, `drift-audit records`, which reads an open spec
cited by product code and clears at this close). The touched self-tests ran directly at `670436cd`
and the canary at `ac54a5c4`.

**Evidences:** TOOL-aMeteredSweep-1
- AC1 — `gate-legs.json` argv per leg, run in a frozen clone at `670436cd` — `python resolver`,
  `codebase-map kit selftest`, `run-gates gov canary`, `foreign-prefix parity`, `spec-tokens
  self-test`, `manifest-check self-test`, `run-gates run-log line` and `govkit selftest` each exited
  0; `run-gates canary` at `ac54a5c4` redded its width-clamp arm on a typed 60 s budget and its arm
  2, which had redded every bar since TOOL-aGraftedHelix-45 with a line that does not say FAIL. At
  `9c60d9e6` the clamp arms passed their slice with a calibrated 525 s budget, and arm 2 passed its
  slice of 13 assertions while still collecting a planted missing script path.
- AC2 — `unattended.sh --claims` — 66 s before the fix and 18 s after, timed back to back on node
  `a` beside the profiled bar's load; the resolver's output byte-identical across the change.
- AC3 — `core.autocrlf=true` and the gov canary — the canary passed 17 assertions and redded both
  pointer arms with the guide's two pointers renamed; the spec-tokens suite failed 5 of 135 under
  the node's `core.autocrlf=true` before the fold and passed 135 of 135 after.
- AC4 — `run_row` and `measure_load_ratio`, sliced — a 1 s-budget row sleeping 300 s was killed at
  60x (3x, load x20) with a spawn at 820 ms against the 21 ms floor; with no floor recorded the ratio
  stayed 1, said so, and the row died at 3x; a fast row stayed green.
- AC5 — `check_mp_value`, the memory-pause section sliced — three runs of three passed beside a
  neighbouring bar, AC6 printing its calibration each time (one-leg bars of 45, 53 and 54 s).

## Announced gaps

- The unattended kit's pooled parity verdict, which its Definition of Done names for a change under
  that kit, was NOT taken. The pooled run refused: the eight driver-suite shards TOOL-aGraftedHelix-41
  cut carry no calibrated reading. The base calibration ran almost six hours beside the neighbouring
  bars and the owner stopped it, on the evidence that the suites' cost is per-arm process creation
  and is the next build's subject. This unit's one change there is `lib-unattended.sh`'s fork
  removal, whose resolver output was compared byte-for-byte and whose callers' bar legs are green.
- The canary exited 1 once with no FAIL line, in the verification bar at `a3531d5e`. It did not
  reproduce in three later runs, each of which named its red. Recorded, not explained.
