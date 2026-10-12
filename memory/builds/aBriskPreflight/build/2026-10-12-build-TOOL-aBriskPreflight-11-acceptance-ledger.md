# TOOL-aBriskPreflight-11 — acceptance ledger

**Serves:** journal TOOL-aBriskPreflight-11

No merge bar and no self-test suite ran in this pass. Every criterion was observed directly on node
`a`, 2026-10-12, at spec rev-2, against the built instrument and the committed rows. Each staged
break ran as a copy of the instrument under the run's scratchpad, never as an edit of the tracked
file. The legs of spec §7 are owed to the close.

**Evidences:** TOOL-aBriskPreflight-11
- AC1 — `K_w=0.91` — `S_w=2.50` — `--selftest` on the built file printed its ok line naming
  K_w=9.00 and S_w=4.00 from the old-arm host row, and exited 0. A scratchpad copy with the host
  branch's kw raise deleted printed a pricing line carrying K_w=0.91 and exited 1; a copy with the
  sw raise deleted printed one carrying S_w=2.50 and exited 1.
- AC2 — `the worst of 7 host rows` — `K_w=2.53` — the instrument's stderr over the committed rows
  opened with the pricing line: S_w=2.50 s per spawn and K_w=2.53 s per fork, the worst of 7 host
  rows and the pinned floors.
- AC3 — `WIRING_CEILING="840"` — `PREFLIGHT_CEILING="4200"` — `CEILING_SPAWN_MS="2500"` — the
  instrument's stdout and exit status, diffed against the driver's three constant lines and a zero
  status, compared empty, exit 0.
- AC4 — `grep -n 'every host row' tools/unattended/README.md tools/unattended/unattended.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ceilings.sh`
  — printed one line from the README, one from the driver and two from the instrument.
- AC6 — `GATE_BOUND` — `PREFLIGHT_CEILING` — over the committed rows the instrument exited 0,
  printed the preflight line at 4200, and named on stderr that 4200 s sits at or above the declared
  3600 s bound. A scratchpad copy in its own repository, with cw-after-1's wall raised to 3500.0,
  exited 1 naming the wiring subject at 4200 s against the 3600 s bound.
- AC5 — `git diff bb388384 -- .unattended.conf` — printed nothing, and the grep for this unit's id
  in spec 7 printed its rev-4 line in §9.
