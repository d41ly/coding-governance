# TOOL-aBriskPreflight-4 — acceptance ledger

**Serves:** journal TOOL-aBriskPreflight-4

Back-filled by TOOL-aBriskPreflight-12 (S2), after the closing diff review's M1 found unit 4 closed
with no journal record evidencing its criteria. Nothing here was re-run: every line is read from
`2026-10-11-build-TOOL-aBriskPreflight-4-probes-ab.md`, the unit's own A/B record of its build
pass on node `a`, 2026-10-11, at spec rev-3. Spec 4's later rev-4 moved only §4 prose and no
criterion, so every answer is in the OBSERVED form.

**Evidences:** TOOL-aBriskPreflight-4
- AC1 — `cmp` — the A/B record: fixture F1 under old and new, stdout, stderr and status
  byte-identical, status 0.
- AC2 — `WIRE-OUT` — the A/B record: F2 byte-identical under both drivers; new's stdout orders
  check 4, `WIRE-OUT`, check 60, `CARRY-OUT` and the wall line on lines 1, 2, 4, 5 and 6, and
  `PREP-OUT` appears nowhere.
- AC3 — `OVERLAP` — the A/B record: F3 under new took 285 s with `OVERLAP` present, under old
  810 s with it absent, outputs byte-identical.
- AC4 — `tRun.procs` — the A/B record: after F2, new's ledger held four rows naming one driver
  pid, against old's three, which never started `--prepared`.
- AC5 — `PREP-DONE` — the A/B record: F4 green on new, and red on both its marker and row
  assertions against old. At the 30 s sleeper the arm printed its NOTE on this host, an announced
  gap the record names.
- AC6 — `exec sleep 600` — the A/B record: F5 green on new at rev-2's 600 s sleeper and 300 s
  backstop, with `UNATTENDED check 61 FAILED` naming the probe.
- AC7 — `WIRE-RAN` — the A/B record: F6 green on new for both the `--session` and the blank
  declaration.
- AC8 — `bash wire.sh --check` — the A/B record: F7 byte-identical, and new's ledger held that
  one row.
- AC9 — `run_bounded` — the A/B record: the halves sliced alone killed a 30 s sleeper (rc 124),
  returned over a backgrounded grandchild, kept the capture, the exec-marker wait and an inert
  bound's status, and two handles read in reverse order returned their own status and output.
- AC10 — `2026-10-11-build-TOOL-aBriskPreflight-1-host-state.sh` — the A/B record: three
  interleaved pairs with the host-state line before each arm, each arm proving it ran; median arm
  B 224.7 s below median arm A 284.6 s.
