**Serves:** journal TOOL-dSafePassage-32

# TOOL-dSafePassage-32 — acceptance ledger

The unit as built, at spec rev-3. In `tools/govkit/upgrade_steps.py`: `read_boot_clock` returns
`time.clock_gettime(time.CLOCK_BOOTTIME)` where `time` defines the clock and None elsewhere;
`add_boot_start` returns a record with `started_boot` beside `started`, the key left out on None,
and both `take_write_lock` (`tools/govkit/govkit.py`) and the reclaim guard `write_reclaimed_lock`
writes go through it (deviation 172). `check_holder_dead` reads `time.time()` and
`read_boot_clock()` on one line immediately before `census.scan_processes()`; a `windows-join` row
is estimated `t0 - age_s` against `started`, a `posix-ps` row `t0_boot - age_s` against
`started_boot`, and a `posix-ps` row with either boot reading missing falls back to the wall, where
it may read `live` but never reused: a would-be reused holder reads `unknown`, which
TOOL-dSafePassage-2 S7's branch refuses. The `lock` fixture family gains `lock-wall-step` and its
no-boot-reading variant `lock-wall-step-no-boot` (the holder's lock written without
`started_boot`); `FIXTURE_LOCK_CHILD` takes `wall-step <pid> <born>`, which, in the child only,
makes the census one `posix-ps` row of the holder aged on `time.monotonic` from `<born>`, stands
`time.monotonic` in for `read_boot_clock`, and steps `time.time` 10 s forward. The self-test's
fixture table gains the two rows, tagged `[dSP-32]`.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on
node d (Windows) by the fixture CLI or a `python` probe of the changed code. Node d now has no WSL
distro named `Ubuntu` (`wsl.exe -l -q` lists `claude-u26` and `docker-desktop`), so AC1's WSL half
ran under `wsl.exe -d claude-u26`, a Linux distro on the same node; the fixture changed, not the
criterion.

Red when, observed: a scratch copy of `tools/govkit`, `tools/process-monitor` and `tools/lib`
whose `check_holder_dead` sets `boot = False` (every row on the wall clock) printed, for
`fixture lock --plant lock-wall-step`, `govkit update — reclaimed ...`, `lock: FAILED · a refusing
take changed the lock` and `lock: FAILED · the stepped wall clock did not leave the holder live`;
for `--plant lock-wall-step-no-boot` the same reclaim and `lock: FAILED · the stepped wall clock
did not leave the holder unknown`.

Real `posix-ps` census, under `wsl.exe -d claude-u26`, `check_holder_dead` over the probe's own pid:
`started` and `started_boot` now read `live`; `started` 600 s back with `started_boot` now (a
wall step) read `live`; `started_boot` 600 s back read `dead` (`a reused pid`); `started` 600 s back
with no `started_boot` read `unknown`; `started` now with no `started_boot` read `live`.

Unbroken neighbours: `fixture lock --plant` `lock-dead` rc 0, `lock-reused` rc 0, `lock-live` rc 1,
`lock-live-slow-census` rc 1, `lock-foreign-host` rc 1, `lock-unreadable` rc 1, `guard-dead` rc 0
with the guard cleared, `lock-race` rc 0, none printing `lock: FAILED`.

Owed at the close: `govkit selftest` (the two `[dSP-32]` rows, and the New arm's RED-first
observation staged by a judge copy that estimates every row on the wall clock, as above), `govkit
refusal join`, `govkit acceptance matrix`, `govkit selfcheck`, `recall floor arms`, `policy
fixtures`, `spec tokens`.

**Evidences:** TOOL-dSafePassage-32
- AC1 — `fixture lock --plant lock-dead` rc 0; a `python -c` take through `take_write_lock` on a scratch target wrote a lock whose keys were `host`, `pid`, `started`, `started_utc`, `verb`, no `started_boot`, and `read_boot_clock` printed `None`; under `wsl.exe -d claude-u26` the `python3 -c` probe printed `wsl read_boot_clock 355123.343443064 · add_boot_start keys ['pid', 'started', 'started_boot']` beside `/proc/uptime` `355123.34`.
- AC2 — `git grep -n -e "read_boot_clock()" -e "scan_processes(" -- tools/govkit/upgrade_steps.py` printed, inside `check_holder_dead` (from line 1467), `1490: now, now_boot = time.time(), read_boot_clock()` before `1491: rows, _counts = census.scan_processes()`, the docstring's mention at 1476 above both; no clock read follows the census.
- AC3 — `python tools/govkit/upgrade_steps.py fixture lock --plant lock-wall-step`, the plant `lock-wall-step`, rc 1: `refusing rather than joining in: live, pid <holder> is still running and was started before it took the lock`, the holder described as `pid <holder> on host ... running update, started ..., 10s ago`, `lock: the planted lock unchanged`, no `lock: FAILED`.
- AC4 — `fixture lock --plant lock-wall-step-no-boot` (the holder's lock without `started_boot`) rc 1: `refusing rather than joining in: unknown, pid <holder> is still running, and its lock records no boot-clock start to compare its age with`, `lock: the planted lock unchanged`; `--plant lock-reused` and `--plant lock-dead` each rc 0, reclaimed, no `lock: FAILED`.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch b, `2026-10-28-prompt-TOOL-dSafePassage-1-close-arms-b-researcher.md`), each break staged alone and restored: `check_step_walk`, cut to `lock-wall-step` and `lock-wall-step-no-boot`. Break: `boot = False`, so every row is estimated on the wall clock. RED: `FAIL [dSP-32] fixture lock lock-wall-step exits 1 and names refusing rather than joining in: live, …` with `lock: FAILED · the stepped wall clock did not leave the holder live`. The `-no-boot` arm stayed ok. GREEN restored: both ok.
