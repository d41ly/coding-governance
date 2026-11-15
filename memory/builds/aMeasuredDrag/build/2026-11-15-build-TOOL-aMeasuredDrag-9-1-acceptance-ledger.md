# TOOL-aMeasuredDrag-9 — acceptance ledger

**Serves:** journal TOOL-aMeasuredDrag-9

No merge bar and no self-test suite ran in this pass. The pass started at 662d712d. The spec's §4
probe ran as `u9probe.py` in the session scratchpad, with `python` from the worktree root in Git
Bash. Every "before" reading was taken before the edit at 662d712d, every "after" reading on the
edited tree at the same HEAD.

**Evidences:** TOOL-aMeasuredDrag-9
- AC1 — `read_mode_calls` — the probe printed `commits=8768 read_mode_calls=8738` before and
  `commits=8768 read_mode_calls=273` after, PINNED at 662d712d. The §4 pipeline printed `273`
  distinct blobs at the same HEAD, PINNED at 662d712d. `commits` did not move.
- AC2 — `digest` — the probe printed `digest=cb051eafa2ec7a18fc47c24839dbea2c86a342b9` before
  and after, the same string, at 662d712d.
- AC3 — `--expect-builds`, `--report`, `--pin` — `transition_audit.py` ran with no flag and with
  each of the three, once to warm the delta cache and once captured, before and after the edit.
  `cmp` found each run's stdout, stderr and exit status byte-identical: twelve of twelve captures,
  every exit 0. The no-flag run printed `transitions examined 4 · merges walked 694` before and
  after, PINNED at 662d712d.
- AC4 — `read_modes_s` — with `time (for i in 1 2 3 4 5 6 7 8 9 10; do /usr/bin/true; done)` in
  the same shell, PINNED at 662d712d:
  - the spawn-pinned pair: before 2.68 s with baseline 1.42 s real; after 0.68 s with baseline
    2.74 s real (PINNED at 662d712d).
  - two paired rounds in one shell, the before side run from HEAD's blob of the module in a
    scratch copy: round 1 before 2.56 s, after 0.57 s, baseline 2.05 s real; round 2 before
    2.46 s, after 0.57 s, baseline 1.78 s real (PINNED at 662d712d).
  - the drop is 1.89 s to 2.00 s, a 4.3x speedup, PINNED at 662d712d. It clears the
    baseline taken beside it in three readings of five and falls short of it in two (2.05 s and
    2.74 s, PINNED at 662d712d). The spec's baseline is 0.35 s, PINNED at 6d98c39ca, so this
    machine was under load when sampled, as TOOL-aMeasuredDrag-7's and -8's ledgers also found;
    the drop clears that pinned baseline fivefold (PINNED at 662d712d).

**Owed to the close (the main loop, after every unit is terminal):**
- No new arm. Spec §6 adds none, so no RED-first observation is owed.
- The gates in spec §6: `transition-audit arms`, `straggler-guard arms`, `memory-hygiene
  self-test`, `backlog migration selftest`, and `kit epoch (shipped bytes move, the version
  moves)`, which prints `owed at the lander` off the push boundary.
- AC4 on an unloaded machine, if the close wants the comparison against a same-shell baseline
  that is not inflated by load.
