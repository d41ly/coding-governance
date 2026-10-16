# Brief — dRedressedBar: the canary's memory-pause arm that hangs instead of redding

**Serves:** research TOOL-dRedressedBar-8

## The prompt

> let the canary run, confirm 12-15 then fix all the traced reds

## The brief

### Goal
The `run-gates canary` leg (`tools/run-gates/run-gates.test.sh`) timed out at its 13200 s ceiling
on its first attempt over `ebce889c7`, and its retry hung at the same place: arm 11g AC14, the
memory pause's forced-progress branch (run-gates.test.sh:3568-3627). The ledger shows the canary
otherwise costs 400 to 3400 s. Fix the arm so a dead fixture server ends the arm red within a
bound, and so the server no longer dies on a transient FIFO open failure.

### Items
1. **TOOL-dRedressedBar-8 — arm 11g AC14 bounded, its FIFO server kept alive.** Observed in the
   retry's fixture `…/gate-work.ca8UP9EB/tmp/tmp.QQMdypyuDs/`:
   - `serve.sh` (written at run-gates.test.sh:3590) was not running, `x/ac14.go` was never written,
     and the `ac14` run held one `.leg` row: A14, `fx/await.sh`, which gave up after its 60 s bound
     (74 s wall) and exited 0. C14 and Y14 were never dispatched.
   - The nested runner sat in a `sleep 60` hold loop for over an hour. Its profile line read
     `wall off`, so nothing bounded the hold, and the outer leg ran to its 13200 s ceiling.
   - `serve.sh`'s loop opens the FIFO with `exec 3>"$f" || exit 0`. One failed open ends the server
     silently, and the arm's own comment already records MSYS FIFO opens misbehaving
     (TOOL-aMeteredSweep-1). Root-cause which open failed if a probe can show it; otherwise make
     the server survive a failed open without changing what it serves.
   - Bound the arm's nested bar (`run_mp_bar ac14 …`), for example with `GATE_WALL`, so a dead or
     silent server reds the arm with its own line rather than holding the leg to its ceiling. Check
     the server is alive before reading the verdict, and name it dead when it is not.
   - The first attempt's log also stops right after `memory pause — AC6 calibrated`. Confirm AC6 to
     AC13 completed in the retry's records (they did: `x/ac13.json` and the AC14 seed exist) before
     calling AC14 the only hang.

### Acceptance
A probe built from the suite's own setup runs arm 11g with the server killed before the run's
first 95 % read and observes the arm RED inside its bound, naming the server. Restored, the arm
passes. The canary leg completes under its 13200 s ceiling in the closing bar.

### Gates
`run-gates canary` · `run-gates gov canary` · `shell hygiene (a fork spent on builtin work)` · `harness arms (fail branches armed or pinned)`

### Non-goals
- No edit to `tools/run-gates/run-gates.sh`; the mempause hold is the subject under test, not the defect.
- `GATE_REGEN_CHECK` reaching nested runners stays a separate finding.

### Limitations
- Children run no bar and no whole suite. The canary costs up to an hour, so verify with a hermetic
  probe of the arm, never the whole leg. The main loop runs the leg at the close.
- Under MSYS, `/tmp` and `C:/…/Temp` name one directory; compare through git.

### Reuse
The arm's own serve/await fixtures, the `run_mp_bar` and `resolve_mp_record` helpers, and the
`GATE_WALL` knob the profile row declares.

## Drawn from the session

> both canary attempts hung in arm 11g AC14 — serve.sh dead, no ac14.go, the nested bar holding with wall off
— agent, 2026-10-14 00:05

## Owner confirmation

Asked: Ready — say go and I'll start, or adjust any field.
Answer: go
