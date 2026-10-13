# TOOL-dSweptBranches-21 — the census suite's live-tree arm waits for its tree, not for three seconds

**Status:** OPEN · rev-1 · 2026-10-13 · node d · Tier-2 · base 2b852f5f · streams tooling · order 19 · closes TOOL-dSweptBranches-18

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-prompt-TOOL-dSweptBranches-19-owner-follow-up.md](../prompts/2026-10-13-prompt-TOOL-dSweptBranches-19-owner-follow-up.md) | research | TOOL-dSweptBranches-19 TOOL-dSweptBranches-20 |

<!-- /gen:spec-records -->

## 1. Goal

`process-monitor census selftest` went red once on the daily held job (run 38247412830, a Windows
runner, at `37200355`) and green on the runs before and on this node. Its only suite arm that races
the clock is `test_live_tree_dies_completely`: it launches a four-member process tree and sleeps a
fixed three seconds before requiring every member in the census. This unit replaces the fixed sleep
with a bounded poll for the members.

## 2. Scope (IN)

- **S1** — After launching the tree, the arm reads the census until each staged member — the nested
  shell, the native python grandchild and the bare sleep — appears under the launched pid's row, up
  to a declared bound of 30 s, then proceeds as before. A tree that never completes within the bound
  fails the arm naming the member that never appeared. Observed by AC1.

## 3. Non-goals (OUT)

- No change to `census.py`, the reaper or the scope fence.
- No retry of the whole arm: a retry would hide a real kill failure.

### Edges

none

## 4. Design

The poll reads `read_live_census()` every 0.5 s and asks the arm's own member predicates over the
rows whose command does not carry the marker. The predicates are the ones the arm already asserts
after the kill, so the poll waits for exactly what the arm grades. The bound is the module constant
`TREE_SPAWN_BOUND = 30`.

### Files touched (estimate)

- `tools/process-monitor/selftest.py`

### Alternatives rejected

- A longer fixed sleep: it only moves the race (gotcha `fixed-sleep-does-not-place-a-signal`).

## 5. Production-readiness checklist

- security — N/A: a test change.
- perf / scale — the arm waits only as long as the tree takes to spawn, at most 30 s.
- error / empty / loading states — a tree that never spawns names its missing member.
- observability — the arm prints how long the spawn took.
- risks — the real cause of the CI red is unproven without its log; the next daily held job is the proof.
- testing — AC1, with a staged slow spawn.
- migration — N/A.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When the staged tree's members are delayed five seconds behind its launcher,
  `test_live_tree_dies_completely` stays green, and with the old fixed three-second wait the same
  delay reds it.
  Red when: the poll is replaced by the fixed wait.

## 7. Gates

`process-monitor census selftest`

New arm: `tools/process-monitor/selftest.py` · covers AC1 · a five-second delay staged in the tree's body · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft, at the owner's instruction to build the asks.

## 10. Reuse audit

`reuse_lookup.py` ranked only name-token neighbours; the seam is the arm itself and its
`read_live_census` in `tools/process-monitor/selftest.py`. The class is
`memory/gotchas/fixed-sleep-does-not-place-a-signal.md`.

Recall terms used: "why is the process-monitor census selftest flaky on the daily held job" --terms
"process-monitor census selftest live tree winpid reaper fixed sleep held job windows runner flaky"
