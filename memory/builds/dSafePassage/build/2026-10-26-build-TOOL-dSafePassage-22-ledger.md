**Serves:** journal TOOL-dSafePassage-22

# TOOL-dSafePassage-22 — acceptance ledger

The unit as built, at spec rev-2. In `tools/govkit/upgrade_steps.py`: the constant `REUSE_MARGIN_S =
2.0`, its comment stating it covers the census's rounding and no latency, replaces the bare `2` in
`check_holder_dead`; that function's one clock read moves from before the census load to the line
immediately before `scan_processes`, and no later reading enters the estimate. The `lock` family
gains the plant `lock-live-slow-census`: a holder whose lock is planted at once after its spawn, and
a taker child (`FIXTURE_LOCK_CHILD`, given a sixth argument of `3`) that wraps the loaded
`gk_lock_census` module's `scan_processes` so it returns three seconds after it sampled, in that
fixture process only. `tools/govkit/selftest.py`'s `check_step_walk` gains the row, tagged
`[dSP-22]`: the `New arm:` line's arm.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed by
running `python3 tools/govkit/upgrade_steps.py fixture lock --plant <case>` on node d (Windows); its
repositories sit under `%TEMP%`. The red was staged as §7 names: the judge reading the clock after
the census (`now = time.time()` moved below `scan_processes`), in place, then restored from a
scratch copy.

Owed at the close: `govkit selftest` (with `check_step_walk`'s `[dSP-22]` row and its RED-first
observation, staged by the after-census clock read above), `govkit refusal join`, `govkit acceptance
matrix`, `govkit selfcheck`, `recall floor arms`, `spec tokens`.

**Evidences:** TOOL-dSafePassage-22
- AC1 — `fixture lock --plant lock-live-slow-census`, rc 1: `lock: refused · another govkit write holds … — pid <holder> on host … running `update`, … refusing rather than joining in: live, pid <holder> is still running and was started before it took the lock. … A lock whose holder has ended is reclaimed by the next run on this host, by itself`, `lock: the planted lock unchanged`, no `lock: FAILED`. Red staged: `govkit update — reclaimed …, pid <holder> now names a process started after the lock was taken, a reused pid`, `lock: the planted lock CHANGED`, two `lock: FAILED` lines, rc 1.
- AC2 — `fixture lock --plant lock-reused`, rc 0: `govkit update — reclaimed … started …, 601s ago, pid <holder> now names a process started after the lock was taken, a reused pid`, `lock: taken`, `lock: held by pid <taker> · host …`. `git grep -n "REUSE_MARGIN_S" -- tools/govkit/upgrade_steps.py` printed `:170:REUSE_MARGIN_S = 2.0` and `:1243:    if any(b <= record["started"] + REUSE_MARGIN_S for b in born):`.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch b, `2026-10-28-prompt-TOOL-dSafePassage-1-close-arms-b-researcher.md`), each break staged alone and restored: `check_step_walk`, cut to `lock-live-slow-census`. Break: the judge reads the clock after the census (the two lines swapped). RED: `FAIL [dSP-22] fixture lock lock-live-slow-census exits 1 and names refusing rather than joining in: live, …` with `lock: FAILED · a refusing take changed the lock`. The holder was reclaimed as "a reused pid". The staged-copy arm `[dSP-35] AC4` also goes red because its text no longer matches the module. GREEN restored: both arms ok.
