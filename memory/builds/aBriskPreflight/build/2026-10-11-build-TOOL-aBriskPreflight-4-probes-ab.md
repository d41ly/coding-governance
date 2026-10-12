# TOOL-aBriskPreflight-4 — the A/B: preflight's four probes started together

**Serves:** research TOOL-aBriskPreflight-4

Node `a`, 2026-10-11, the build pass, spec rev-2. "Old" is the driver at `900d74e67`, the commit the
pass started from; "new" is the pass's driver. A concurrent full bar from another session ran on the
host for the whole pass, so every wall below is a loaded one, and only same-host interleaved pairs
are compared.

## AC10 — the four real probes, through the runner's halves

The instrument is `2026-10-11-build-TOOL-aBriskPreflight-4-probes-ab.sh`; its header states what each
arm runs and how it proves it ran. Each arm read this worktree's `.unattended.conf` and ran
`WIRING_CHECK`, the lander's `--carry` and `--prepared` for `aBriskPreflight`, and
`GATE_PROFILE_CMD`, under `GATE_BOUND` 3600. `2026-10-11-build-TOOL-aBriskPreflight-1-host-state.sh`
ran before each arm, interleaved A, B, A, B, A, B.

| Run | At (UTC) | Five spawns | Fork | CPU | Wall | Wiring (its own `RB_TOOK`) | carry · prepared · profile | ran |
|---|---|---|---|---|---|---|---|---|
| A1 | 11:47:25 | 3.00 s | 0.04 s | 15% | 424.4 s | 0 (259 s) | 0 · 1 · 0 | yes |
| B1 | 11:55:14 | 2.30 s | 0.63 s | 52% | 200.7 s | 0 (183 s) | 0 · 1 · 0 | yes |
| A2 | 11:59:25 | 5.51 s | 0.06 s | 26% | 284.6 s | 0 (175 s) | 0 · 1 · 0 | yes |
| B2 | 12:04:39 | 1.81 s | 0.55 s | 30% | 224.7 s | 0 (205 s) | 0 · 1 · 0 | yes |
| A3 | 12:08:56 | 1.52 s | 0.04 s | 30% | 270.3 s | 0 (186 s) | 0 · 1 · 0 | yes |
| B3 | 12:14:08 | 4.21 s | 0.08 s | 30% | 285.8 s | 0 (261 s) | 0 · 1 · 0 | yes |

Median A 284.6 s, median B 224.7 s: B is below A, so AC10 is green and the unit ships. Arm B's wall
tracks its wiring child, which was the longest child in every arm; arm A's exceeds its wiring
child by the other three's sum, 85 s to 165 s here. The wiring check itself is not this unit's
cost (§3).

## AC1 to AC8 — stub fixtures, old against new

Each fixture was built by the suite's own prologue helpers with fixed commit dates, so both drivers
ran over the same commit, and every run's stdout, stderr and exit status were captured apart.

- AC1, F1 (every stub answers at once): stdout, stderr and status byte-identical, status 0.
- AC2 and AC4, F2: byte-identical; new's stdout orders check 4, `WIRE-OUT`, check 60, `CARRY-OUT`
  and the wall line on lines 1, 2, 4, 5 and 6, and `PREP-OUT` appears nowhere. New's ledger holds
  four rows naming one driver pid; old's held three, having never started `--prepared`.
- AC3, F3: new 285 s with `OVERLAP` present, old 810 s with it absent; outputs byte-identical.
- AC8, F7: byte-identical; new's ledger holds the one `bash wire.sh --check` row.
- AC5, F4: green on new; the same arm run against old reds on both of its marker and row
  assertions, which is the sequential driver's failing case. Its OTHER failing case, a driver that
  starts `--prepared` and never reads it (the `read_preflight_probes` call deleted), passed at
  rev-2's 5 s sleeper, because the verb ran 109 s to 125 s past `--carry` on this host and the unread
  probe finished alone first. Rev-3's 30 s sleeper still cannot see that here, and the arm now prints
  its NOTE saying so, on both drivers; with the sleeper raised to 300 s in a scratch copy the same
  break red on both assertions. On this host that break is an announced gap, not coverage.
- AC6, F5: green on new at spec rev-2's 600 s sleeper and 300 s backstop; rev-1's 40 s wall red at
  154 s for host load, the change rev-2 records.
- AC7, F6: green on new, both the `--session` and the blank declaration.
- AC9: the halves sliced alone kill a 30 s sleeper (rc 124), return over a backgrounded grandchild,
  keep the capture and the exec-marker wait, keep an inert bound's status, and two handles read in
  reverse order return their own status and output. Run alternately against old under the same load,
  the killed sleeper took 14 s and 14 s against old's 18 s and 10 s.

The arms ran as slices of the suite's prologue and region five's `run_bounded` span; no suite and no
bar ran. Three pre-existing timing arms in that span red at 21 s, 24 s and 357 s on the same load,
over code paths whose walls matched old's.
