# TOOL-dFurnishedOrders-51 — unit 49's interrupt probe reads the pid its kill path targets: a Python stub writing `os.getpid()`, that pid read live before the interrupt in the kill's own namespace, and a no-op tree kill that reds the arm

**Status:** DEFERRED · rev-3 · 2026-10-27 · node d · Tier-2 · base 84ab3c6f · streams tooling · order 28 · advances TOOL-dFurnishedOrders-21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dFurnishedOrders-50-round6-fix-return.md](../build/2026-10-27-build-TOOL-dFurnishedOrders-50-round6-fix-return.md) | research | TOOL-dFurnishedOrders-50 TOOL-dFurnishedOrders-52 |
| [2026-10-27-prompt-TOOL-dFurnishedOrders-50-round6-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dFurnishedOrders-50-round6-fix-brief.md) | research | TOOL-dFurnishedOrders-50 TOOL-dFurnishedOrders-52 |
| [2026-10-27-review-TOOL-dFurnishedOrders-50-spec-audit-round1.md](../reviews/2026-10-27-review-TOOL-dFurnishedOrders-50-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-50 TOOL-dFurnishedOrders-52 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-5 promotions
(`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-47-spec-audit-round1.md`)
confirmed finding **id 24 at HIGH**, report item **H2**. No other id shares that item.

`TOOL-dFurnishedOrders-49` S6 and AC5, and `TOOL-dFurnishedOrders-46` AC17 before them, say "a stub
that writes its pid" and "the pid is gone within 15 s". They do not say which pid namespace the stub
writes in or the check reads. On this host a Git-Bash stub's `$$` is an MSYS pid. The report measured
`$$` 1803, its `/proc/$$/winpid` 37272, and the Popen pid 20264. A Windows liveness read finds no
process at 1803, reads it as gone at once, and greens the arm even when `run_tree_kill` leaves the
child running. That is a check certifying what it does not check.

This unit pins the stub, the pid, the liveness read and a staged break that must red. It repairs
unit 49 and builds one step after it (order 28).

## 2. Scope (IN)

- **S1** — The stub writes the pid the kill path targets. The arm's stub is a Python script run by
  the arm's own interpreter, `sys.executable`, and it writes `os.getpid()` to the pid file, then sleeps
  60 s. No bash stub writes `$$`. The canonical `run_bounded` starts the stub with `Popen`, and
  `run_tree_kill` passes `proc.pid` to `taskkill /F /T /PID` on Windows
  (`tools/run-gates/regen.py:252-257`). This unit's probe on 2026-10-27 found that a `sys.executable`
  child's `os.getpid()` equals the `Popen` pid (30652 both, CPython 3.14.5). So the written pid is the
  one `taskkill` names, never a descendant that `/T` may miss: `/T` killed one process of four in an
  MSYS tree (`memory/builds/aReapedSpinner/build/2026-09-08-build-TOOL-aReapedSpinner-4-signal-namespace-measured.md:45-47`).
  The arm also asserts that the pid in the file equals the `Popen` pid `run_bounded` holds, and fails
  as `DEAD PROBE: stub pid is not the child's pid` otherwise. Observed by AC1.
- **S2** — The liveness read is in the kill's namespace. On Windows the arm reads a pid's state
  through `read_process_created` (`tools/run-gates/measure_legs.py:1474-1493`), with the kernel32
  surface `resolve_job_backend` binds (`:694`). It loads both by path from gov's tool root, because
  the roles suite runs in gov only (`tools/roles/kit.toml:47`, the `project-owned` rule for
  `adopt-roles.test.sh`). That reader answers `live`, `dead` or `unknown`: `OpenProcess`, then
  `GetExitCodeProcess` against `STILL_ACTIVE` (`:182`). On POSIX the arm reads `os.kill(pid, 0)`.
  `unknown` is never read as `dead`. Observed by AC1 and AC2.
- **S3** — The pid is live before the act the arm grades. The patched `Popen.wait` of unit 49 S6
  acts on its first call only, the stub's own wait inside `run_bounded`. Every later call, the kill
  path's `taskkill` child among them, goes to the original `Popen.wait`, so S1's equality check never
  reads another child's pid. That first call waits until the pid file is non-empty. It then reads the
  pid's state, and only on `live` raises `KeyboardInterrupt`. Any other state fails the arm as
  `DEAD PROBE: stub pid <n> not live before the interrupt`, never as a pass. After the interrupt
  reaches the caller, the arm polls the same read for up to 15 s and passes only on `dead`.
  Observed by AC1 and AC2.
- **S4** — A no-op kill reds the arm. With `run_tree_kill` patched to a function that does nothing,
  the interrupted stub stays `live` past 15 s and the arm fails, naming the pid. That is the staged
  break on §7's `New arm:` line. Observed by AC2.
- **S5** — No sleeper outlives a run. Whatever the verdict, the arm ends by killing the stub with
  the single-pid form `taskkill /F /PID <pid>` on Windows, the form measured sound
  (`memory/builds/aReapedSpinner/build/2026-09-08-build-TOOL-aReapedSpinner-4-signal-namespace-measured.md:45-48`).
  On POSIX it uses `os.kill(pid, signal.SIGKILL)`. A red run leaves no 60 s child holding the
  suite's temp dir. Observed by AC2.

## 3. Non-goals (OUT)

- The assertion that the kill path ran whole (report id 9) and the early exit for a stub that never
  starts (id 5). The minors batch `TOOL-dFurnishedOrders-52` takes them, over the patched wait this
  unit hands it. S3's first-call rule is this unit's, because S1's check needs it.
- Changing `run_tree_kill` or the canonical `run_bounded` block. This unit grades them and edits
  neither.
- A shared pid-liveness library. S2 reuses the one reader gov has.
- The report's left-shift gate (a checklist entry and a policy check on `$$` pid files): no clause of
  this build names it.
- Where a landed criterion cannot hold as written, unit 46's ledger (AC17) and unit 49's ledger (AC5)
  answer it AMENDED, naming this unit.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-46` — AC17's interrupt arm in the roles adopter suite, whose stub, pid and liveness read S1 to S3 pin (id 24)
- **consumes-from** `TOOL-dFurnishedOrders-49` — S6's patched `Popen.wait` and AC5, whose readiness wait S3 extends with a live read (id 24)
- **hands-off** `TOOL-dFurnishedOrders-52` — the patched wait with its live read and the arm's cleanup, which unit 52 S15 and S20 hold to a whole kill path and an early exit (ids 24, 9 and 5)
- **hands-off** `TOOL-dFurnishedOrders-58` — the stub, the state read, the cleanup and AC2, which unit 58 S1 to S5 settle (ids 1, 30, 2, 29, 33 of the seventh audit)
- **hands-off** `TOOL-dFurnishedOrders-60` — S5's cleanup, which unit 60 S11 makes end the held child on every branch (id 4 of the eighth audit)

## 4. Design

### The interrupt probe, after this unit

```
stub.py      : open(pidfile, "w").write(str(os.getpid())); time.sleep(60)          S1
state(pid)   : Windows -> read_process_created(resolve_job_backend(), pid)[0]      S2
               POSIX   -> "live" if os.kill(pid, 0) succeeds, else "dead"
patched Popen.wait(self, timeout=None):
    not the first call -> return original Popen.wait(self, timeout)                  S3
    until pidfile is non-empty (unit 49 S6's wait)
    pid := int(pidfile); pid != self.pid      -> DEAD PROBE: stub pid is not the child's pid   S1
    state(pid) != "live"                      -> DEAD PROBE: stub pid <pid> not live before the interrupt   S3
    raise KeyboardInterrupt
caller: KeyboardInterrupt reached it; state(pid) == "dead" within 15 s, else FAIL naming pid   S3
finally: taskkill /F /PID pid (Windows) or SIGKILL (POSIX)                         S5
staged break: run_tree_kill := lambda proc: None  -> FAIL naming pid               S4
```

### What it does not check

- A child the stub itself spawns. The stub spawns none, and `/T`'s reach into a deeper tree is unit
  39's runner's concern, not this arm's.
- Pid reuse inside the 15 s window. A reused pid reads `live` and fails the arm toward red.

### Inventory

Minted: the printed tokens `DEAD PROBE: stub pid is not the child's pid` and
`DEAD PROBE: stub pid <n> not live before the interrupt`. No function, flag or file.

### Migration

None: the arm has never run.

### Rollout

Live at landing, at order 28, after units 46 and 49 and beside unit 50. The suite is the roles kit's
`project-owned` file, withheld from installs, so no shipped byte moves.

### Files touched (estimate)

- `tools/roles/adopt-roles.test.sh`

### Alternatives rejected

- **A bash stub writing `/proc/$$/winpid`.** That pid is a descendant of the `Popen` pid (the report
  measured 37272 under 20264). Its death then depends on `/T` reaching it, which the aReapedSpinner
  record measured failing in an MSYS tree. S1's equality check could not hold for it.
- **A second Windows liveness reader inline in the arm.** gov already has `read_process_created`,
  and the charter's reuse rule extracts at a kind's second instance, never copies it.
- **`tasklist /FI "PID eq <n>"`.** It parses localized text, and its "no task" answer reads the same
  as a failed call.

## 5. Production-readiness checklist

- security — none moved: a test arm that kills only the pid it started.
- perf / scale — adds one state read before the interrupt and at most 15 s of polling after it, the
  same bound unit 46 AC17 states.
- error / empty / loading states — a stub pid that is not the child, or not live, is a named DEAD
  PROBE. `unknown` is never `dead`.
- observability — every failure names the pid it read.
- risks — loading `measure_legs.py` by path couples the roles suite to the run-gates kit's module in
  gov's tree. The suite never ships (S2), so no install sees the coupling.
- testing — AC1 and AC2 by probes; the arm of §7 at the close.
- migration — none.
- user docs — none: a self-test arm.

## 6. Acceptance criteria

- **AC1** — When `python -c` runs S3's patched wait over the canonical `run_bounded` with S1's stub,
  the pid in the file equals the child's `Popen` pid and reads `live` before the raise.
  `KeyboardInterrupt` reaches the caller, and the pid reads `dead` within 15 s.
  Red when: the pid the arm checks is not the pid the kill path targets.
  fixture: a stub `.py` and a pid file under `%TEMP%`.
- **AC2** — When the same probe runs with `run_tree_kill` replaced by a no-op, it fails naming the
  pid still `live` after 15 s, and afterwards the pid reads `dead` (S5's cleanup). When the stub
  instead writes the pid of a process it started and reaped, the probe prints
  `DEAD PROBE: stub pid` and `not live before the interrupt`, and never passes.
  Red when: a no-op kill, or a pid no live process carries, passes the arm.
  fixture: two stub variants and a pid file under `%TEMP%`.
  cost: 15 s for the no-op case.

## 7. Gates

`roles adopter self-test` · `govkit selftest` · `measure-legs selftest` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/adopt-roles.test.sh · covers AC1 AC2 · unit 46's interrupt arm with a Python stub writing `os.getpid()`, the pid asserted equal to the child's and `live` before the raise, staged by replacing `run_tree_kill` with a no-op in the roles kit's copy of the canonical block after deleting `tools/roles/__pycache__` and running Python with `-B` · none

`govkit selftest` is named because unit 50 keeps `{prefix}/roles/` in that leg's guard.

## 8. Open questions

- **F1 — Which stub and which liveness read?** Options: (a) a Python stub writing `os.getpid()`,
  read by `read_process_created`; (b) a bash stub writing `/proc/$$/winpid`, read the same way; (c)
  either stub, read by `tasklist`. (b) names a descendant `/T` may not reach, so a correct kill could
  red. (c) parses localized text. (a) names exactly `proc.pid`, which S1 checks. RESOLVED (agent,
  2026-10-27, delegated): (a), rung 3, the skeptic-judged fix of id 24 and this unit's probe.
  widens: none · relaxes: none
- **F2 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent,
  2026-10-27, delegated): `**Derived:**` naming `PLAY-dClosedLoop-2`, rung 3, the precedent
  `TOOL-dBoundRoles-39` §8 F1 records. widens: none · relaxes: none
- **F3 — The units this one repairs are unbuilt.** Units 46 and 49 and the canonical `run_bounded`
  of unit 39 are specced and unbuilt at `84ab3c6f`. RESOLVED (agent, 2026-10-27, delegated): the
  build run re-grounds on each at the pass and stops this unit if the interrupt arm is still absent
  then, rung 1, the brief's rule. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-5 promotions, id 24
  (HIGH, item H2).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the **hands-off** bullet mirroring TOOL-dFurnishedOrders-58, promoted from the spec audit of the round-6 promotions (`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-50-spec-audit-round1.md`); nothing else moved.
- rev-3 · 2026-10-27 · §3 · the Edges block gains the **hands-off** bullet mirroring TOOL-dFurnishedOrders-60, promoted from the spec audit of the round-7 promotions (`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-53-spec-audit-round1.md`); nothing else moved.

## 10. Reuse audit

The seams extended:

- `read_process_created` and `resolve_job_backend` (`tools/run-gates/measure_legs.py:1474`, `:694`),
  gov's one Windows liveness reader, for S2.
- `run_tree_kill` (`tools/run-gates/regen.py:249-267`), read as the target namespace for S1, and
  graded by S4's break.
- Unit 46's interrupt arm and unit 49 S6's readiness wait, for S3.
- The aReapedSpinner signal-namespace record, for S1 and S5's kill form.

`python tools/codebase-map/reuse_lookup.py "check whether a windows process id is still alive"`
ranked `check`, `checks` and `check_line`, name-token neighbours none of which reads a pid's state.
The source grep for `GetExitCodeProcess` found `read_process_created`, the seam above. The recall
probe returned TOOL-aReapedSpinner-10 (the kill signal is chosen per row, and a native process
ignores MSYS `kill`), the aReapedSpinner-4 namespace record, and the process-monitor dossier's
liveness section. None disagrees with source.

Recall terms used: `python tools/memory-recall/query.py "which pid does a liveness probe read on
Windows under Git Bash" --terms "pid winpid MSYS liveness OpenProcess GetExitCodeProcess taskkill tree
kill stub interrupt"`
