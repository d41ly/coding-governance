# TOOL-dSweptBranches-21 — the reaper backstops an MSYS signal with the winpid, and the live-tree arm waits for its tree

**Status:** CLOSED · rev-2 · 2026-10-13 · node d · Tier-2 · base 2b852f5f · streams tooling · order 19 · closes TOOL-dSweptBranches-18

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-build-TOOL-dSweptBranches-21-1-acceptance-ledger.md](../build/2026-10-13-build-TOOL-dSweptBranches-21-1-acceptance-ledger.md) | journal | — |
| [2026-10-13-prompt-TOOL-dSweptBranches-19-owner-follow-up.md](../prompts/2026-10-13-prompt-TOOL-dSweptBranches-19-owner-follow-up.md) | research | TOOL-dSweptBranches-19 TOOL-dSweptBranches-20 |
| [2026-10-13-prompt-TOOL-dSweptBranches-21-1-build-brief.md](../prompts/2026-10-13-prompt-TOOL-dSweptBranches-21-1-build-brief.md) | journal | — |
| [2026-10-13-review-TOOL-dSweptBranches-19-20-21-closing-diff-round1.md](../reviews/2026-10-13-review-TOOL-dSweptBranches-19-20-21-closing-diff-round1.md) | diff-review | TOOL-dSweptBranches-19 TOOL-dSweptBranches-20 |

<!-- /gen:spec-records -->

## 1. Goal

`process-monitor census selftest` went red once on the daily held job (run 38247412830, a Windows
runner, at `37200355`) and green on the runs before and on this node. Its only suite arm that races
the clock is `test_live_tree_dies_completely`: it launches a four-member process tree and sleeps a
fixed three seconds before requiring every member in the census. This unit replaces the fixed sleep
with a bounded poll for the members.

Rev-2: measuring the arm found a second, larger cause in the reaper itself. On this node the arm
reds 2 runs in 5, 2 in 6 and 2 in 10 on an unchanged HEAD, every time on the native python
grandchild: `kill -9` on its MSYS id is refused with `Permission denied`, or accepted while the
process runs on past the whole settle. `kill -f` changes nothing (2 in 10). A single-pid taskkill on
the winpid the census read kills it every time.

## 2. Scope (IN)

- **S1** — After launching the tree, the arm reads the census until each staged member — the nested
  shell, the native python grandchild and the bare sleep — appears under the launched pid's row, up
  to a declared bound of 30 s, then proceeds as before. A tree that never completes within the bound
  fails the arm naming the member that never appeared. Observed by AC1.
- **S2** — `reap.run_kill` follows every MSYS signal with a single-pid `taskkill /PID <winpid> /F` on
  the same member, and a refused MSYS signal whose backstop lands, or finds the process gone, is not
  a signal error. The members backstopped are reported as `backstopped`. Whether a member died stays
  the census's answer. Observed by AC2 and AC3.

## 3. Non-goals (OUT)

- No change to `census.py`, the scope fence, the walk or the settle.
- No `/T`: the backstop is single-pid, like the native path.
- No retry of the whole arm: a retry would hide a real kill failure.

### Edges

none

## 4. Design

The poll reads `read_live_census()` every 0.5 s and asks the arm's own member predicates over the
rows whose command does not carry the marker. The predicates are the ones the arm already asserts
after the kill, so the poll waits for exactly what the arm grades. The bound is the module constant
`TREE_SPAWN_BOUND = 30`.

The poll walks only the launched tree, by `reap.build_walk(rows, launched.pid)`: a first draft that
asked the predicates over every row found members of other trees and stopped early.

The backstop runs inside the signal loop, after the MSYS signal and before its outcome is
classified. The MSYS signal still goes first, so a Cygwin process keeps the signal path it had. The
two signal messages share `read_signal_blob` and `check_gone_blob`, which replace the inline
"not found" test. A winpid reused between the census read and the backstop is the same exposure the
native path already carries, which signals that winpid from the same read.

### Files touched (estimate)

- `tools/process-monitor/selftest.py`
- `tools/process-monitor/reap.py`

### Alternatives rejected

- A longer fixed sleep: it only moves the race (gotcha `fixed-sleep-does-not-place-a-signal`).
- `kill -f -9`: measured red 2 runs in 10, the same silent survivor.
- A taskkill only after a refused MSYS signal: measured red 1 run in 8, on the accepted-and-survived
  case, which no exit status reveals.
- taskkill alone for every member: it would drop the MSYS signal path every Cygwin process has today
  and change how the settle classifies an exiting shell, for no measured gain.

## 5. Production-readiness checklist

- security — N/A: a test change.
- perf / scale — the arm waits only as long as the tree takes to spawn, at most 30 s.
- error / empty / loading states — a tree that never spawns names its missing member.
- observability — the arm prints how long the spawn took.
- risks — the CI red's own log needs authentication this node lacks, so its cause is inferred from
  the same arm's local reds; the next daily held job is the proof.
- testing — AC1 with a staged slow spawn, AC2 stubbed, AC3 over repeated live runs.
- migration — N/A.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When the staged tree's members are delayed five seconds behind its launcher,
  `test_live_tree_dies_completely` stays green, and with the old fixed three-second wait the same
  delay reds it.
  Red when: the poll is replaced by the fixed wait.
- **AC2** — With the signal binaries stubbed and the MSYS signal refused on one member,
  `test_msys_signal_is_backstopped_by_winpid` sees a single-pid taskkill on every MSYS-signalled
  member's winpid and no signal error.
  Red when: the backstop is removed from `run_kill`.
- **AC3** — `test_live_tree_dies_completely` stays green over twelve consecutive live runs, where an
  unchanged HEAD reds it in 2 of 6.
  Red when: the backstop is removed and the arm is rerun.

## 7. Gates

`process-monitor census selftest`

New arm: `tools/process-monitor/selftest.py` · covers AC1 · a five-second delay staged in the tree's body · none
New arm: `tools/process-monitor/selftest.py` · covers AC2 · the backstop removed from `run_kill` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft, at the owner's instruction to build the asks.
- rev-2 · 2026-10-13 · S2, AC2 and AC3: measuring the arm found the reaper's MSYS signal missing a
  native grandchild, a larger cause than the fixed sleep.

## 10. Reuse audit

`reuse_lookup.py` ranked only name-token neighbours; the seam is the arm itself and its
`read_live_census` in `tools/process-monitor/selftest.py`. The class is
`memory/gotchas/fixed-sleep-does-not-place-a-signal.md`.

Recall terms used: "why is the process-monitor census selftest flaky on the daily held job" --terms
"process-monitor census selftest live tree winpid reaper fixed sleep held job windows runner flaky"
