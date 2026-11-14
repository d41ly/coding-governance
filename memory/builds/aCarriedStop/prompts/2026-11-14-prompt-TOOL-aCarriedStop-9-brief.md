# Brief — aCarriedStop: unit 9, the routed-commits leg's ceiling over a recorded reading

**Serves:** research TOOL-aCarriedStop-1

The owner's order arrived in this session's chat on 2026-11-14, after the run was held, and is quoted whole.

## The prompt

> raise the routed-commits ceiling and land it

## The brief

### Goal
The close's bar finishes the leg `routed commits name a specced unit` on node a, so this build can land.

### Items
1. The leg's out-of-band reading is recorded in `tools/run-gates/ceiling-evidence.txt` by `derive-ceilings.py --write --observed`, never typed [planned TOOL-aCarriedStop-9]
2. The leg's `ceiling` in `tools/gate-legs.json` is raised to the evidence rule's minimum over that reading, rounded up to a whole minute [planned TOOL-aCarriedStop-9]

### Acceptance
- `python tools/run-gates/derive-ceilings.py --check` exits 0 and names the leg backed, out of band.
- The leg's row in the evidence file carries the reading this brief records for TOOL-aCarriedStop-9 and its `--how` account.
- `tools/gate-legs.json` parses, and only that leg's `ceiling` value changed in it.

### The readings
- The second close's bar at 41c93c8b7 killed the leg at its 760 s ceiling twice, with a spawn at 3.6x this clone's floor (TOOL-aCarriedStop-9).
- Run alone at 41c93c8b7 with `GATE_PUSH_BASE` set to 8db6f4be, the leg exited 0 in 957 s (TOOL-aCarriedStop-9).
- Run alone on a detached tree at 5e2451f22 with `GATE_PUSH_BASE` unset, graded whole as the close's bar does, it exited 0 in 1491.2 s; 3 foreign gate processes were live at its start and 26 at its end, a full bar of another session having started in the primary tree (TOOL-aCarriedStop-9).
- The rule in `tools/run-gates/ceiling-margin.txt` asks headroom of max(120 s, 1.0 x max) over the evidenced maximum (TOOL-aCarriedStop-9).

### Gates
The merge bar at the close; `derive-ceilings.py --check` in the pass.

### Non-goals
- No change to `routed_commits.py` or to how it grades: its cost is a separate question.
- No other leg's ceiling, budget row or pass-leg row.
- No reading of the leg taken on a quiet host: the close's bar runs beside other sessions' work on this node.

### Limitations
- The governing reading is contended: it records the cost under load, which is the load the close meets.
- The ceiling is a hang bound, not a cost verdict, so the raise says nothing about whether the leg is too slow.

### Reuse
- `derive-ceilings.py --write --observed '<leg>=<seconds>' --how '<how>'` is the one door for an out-of-band row; cf2c673f3 raised two ceilings the same way under TOOL-aNimbleMend-15.

## Drawn from the session

- The three readings above, taken by the main loop of this session.

## Owner confirmation

The order is the owner's own words in chat; nothing else was asked.
