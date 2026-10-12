# TOOL-aBriskPreflight-7 — acceptance ledger

**Serves:** journal TOOL-aBriskPreflight-7

Back-filled by TOOL-aBriskPreflight-12 (S2), after the closing diff review's M1 found unit 7 closed
with no journal record evidencing its criteria. The source of every line but two is the message of
the unit's build commit `feb305b0b`, at spec rev-3, which records the sliced arms of the driver
suite run from the scratchpad with the kit dir pinned. AC11 is recorded nowhere, so this pass
re-ran its `grep` on 2026-10-12 and says so on that line. AC10's lexicon half is recorded nowhere
either; this pass re-ran it, and that line says what it saw. TOOL-aBriskPreflight-11, which may
revise spec 7's constants, is parked on an owner fork and revised no criterion, so no line is in
the AMENDED form.

**Evidences:** TOOL-aBriskPreflight-7
- AC1 — `mutate` — `feb305b0b`: the sliced wiring-ceiling block over a driver copy with
  `WIRING_CEILING` rewritten to 2 went green; the first slice's one red was AC1's fixture
  assumption, fixed by spec rev-3 and re-run green, 32 assertions across AC1 to AC7.
- AC2 — `WIRING_CEILING="9999"` — `feb305b0b`: green in the same slice, the conf's value
  overwritten by the constants assigned after it.
- AC3 — `unattended: preflight OK` — `feb305b0b`: green in the same slice, and GATE_BOUND's
  refusal keeps its bytes when it is the smaller or equal.
- AC4 — `its own 1s wall-clock ceiling` — `feb305b0b`: green in the same slice; the breach line
  is printed without moving the status or the run-state file.
- AC5 — `--preflight refused; the run-state file is unchanged` — `feb305b0b`: green in the same
  slice; the compare runs on every return path.
- AC6 — `DRIVER_T0_US` — `feb305b0b`: green in the same slice.
- AC7 — `timeout` — `feb305b0b`: green in the same slice; a host with no working `timeout -k`
  prints a second NOTE naming the ceiling inert.
- AC8 — `GATE_BOUND` — `feb305b0b`: the committed ceilings instrument prints the three constants
  byte-identically, and staged breaks of a host row, a timed row, the window rows and an inflated
  count each exit 1 naming the subject. Re-run by this pass on 2026-10-12 as its AC2: it printed
  `WIRING_CEILING="570"`, `PREFLIGHT_CEILING="3060"` and `CEILING_SPAWN_MS="2500"`, exit 0.
- AC9 — `python tools/memory-tree/check-arms.py --check` — `feb305b0b`: check-arms names
  unattended.sh check 4 branch 3 with the longest-slice hit deleted, and loses that line restored.
- AC10 — `python tools/codebase-map/gen_map.py --check` — `feb305b0b`: gen_map --check rc 0. The
  lexicon half was not recorded there. Re-run by this pass on 2026-10-12, `lexicon.py --check`
  exited 1 at 1071 verb offenders over a pin of 1063, none of them in a file unit 7 touched, so it
  shows no unit-7 name leading with an undeclared verb but did not exit 0; parked in `RUN.md`.
- AC11 — `grep -n -E 'WIRING_CEILING|PREFLIGHT_CEILING|CEILING_SPAWN_MS' tools/unattended/README.md`
  — re-run by this pass on 2026-10-12: it printed lines 285 to 311 of one section naming both
  ceilings, what each does on a breach, the formula's inputs and why no conf key exists.
- AC12 — `WIRING_CHECK="true"` — `feb305b0b`: trace-spawns over a traced fixture preflight, the
  parent driver 244 forks and 221 execs, the built driver 244 forks and 221 execs.
