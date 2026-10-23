# TOOL-dSafePassage-32 — the reuse estimate compares like clocks: a POSIX census row is judged on the kernel's boot clock, never the wall clock

**Status:** OPEN · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 4 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-32-deviation-78.md](../build/2026-10-23-build-TOOL-dSafePassage-32-deviation-78.md) | deviation | — |
| [2026-10-23-review-TOOL-dSafePassage-27-28-29-30-31-32-33-34-35-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-27-28-29-30-31-32-33-34-35-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-33 TOOL-dSafePassage-31 TOOL-dSafePassage-34 TOOL-dSafePassage-35 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 15 to 26
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-15-16-17-18-19-20-21-22-23-24-25-26-spec-audit-round1.md`)
confirmed finding **id 37** at HIGH, its item **D-5**. TOOL-dSafePassage-22's proof that the estimate
"can only err early" assumes the lock's `started`, the judge's `t0` and the census's `age_s` share one
clock. `take_write_lock` writes `started` from `time.time()` (`tools/govkit/govkit.py:7429`), a wall
reading. On POSIX the census runs `ps -eo pid,ppid,etimes,times,args`
(`tools/process-monitor/census.py:275`) and stores `etimes` as `age_s` (`:220`), elapsed time that
does not move with the wall clock. With a forward wall step D between the take and `t0`, the
estimate `t0 - age_s` lands about D after the true creation, so a live holder reads reused, then
dead, and its lock is reclaimed while it writes. NTP steps and WSL2's resync after host sleep both
cause this. Windows is unaffected: the CIM query computes `(Get-Date) - CreationDate` (`:63-70`), wall
against wall. This unit is id 37's promotion: on a POSIX census row both sides of the comparison are
read on the kernel's boot clock, and a lock that does not carry that reading cannot read reused.

## 2. Scope (IN)

- **S1** — The boot reading. `read_boot_clock()` in `tools/govkit/upgrade_steps.py` returns
  `time.clock_gettime(time.CLOCK_BOOTTIME)` where `time` defines `CLOCK_BOOTTIME`, and `None`
  elsewhere. Observed by AC1.
- **S2** — The record. `take_write_lock` writes `started_boot`, the value `read_boot_clock` returns,
  beside `started`, and leaves the key out where the value is `None`. Observed by AC1.
- **S3** — The judge reads both clocks first. `check_holder_dead` reads `time.time()` and
  `read_boot_clock()` immediately before it calls the census's `scan_processes`, the place
  TOOL-dSafePassage-22 S1 puts its one wall reading. No clock read after the census enters an
  estimate. Observed by AC2.
- **S4** — The frame by backend. A census row whose `backend` is `windows-join` is estimated and
  compared on the wall clock, `t0 - age_s` against `started`, as TOOL-dSafePassage-22 S1 says. A row
  whose `backend` is `posix-ps` is estimated on the boot clock, `t0_boot - age_s` against
  `started_boot`. Either way `reused` is the estimate exceeding the start by more than
  `REUSE_MARGIN_S`. Observed by AC2 and AC3.
- **S5** — The missing reading. A `posix-ps` row judged against a lock with no `started_boot`, or by
  a judge whose `read_boot_clock` returns `None`, never reads `reused`: where the wall estimate would
  say reused, the holder reads `unknown`, which refuses. A pid absent from the census still reads
  `dead`. Observed by AC4.
- **S6** — The plant. The `lock` family of `python3 "tools/govkit/upgrade_steps.py" fixture` gains
  `lock-wall-step`. Inside the fixture process only, it stubs the census to one `posix-ps` row for a
  live holder pid and stubs `read_boot_clock` to `time.monotonic`. It writes the holder's lock with
  both clocks' readings, then shifts the judge's `time.time` forward by 10 s, so the plant runs on
  Windows, where the `posix-ps` backend does not run (`tools/process-monitor/census.py:195-201`).
  Observed by AC3.

## 3. Non-goals (OUT)

- The census module and its two backends, which this unit reads and leaves as they are.
- The pid namespace of a holder: id 13, `TOOL-dSafePassage-31`.
- The per-backend rounding bound in the `REUSE_MARGIN_S` comment and the plants' timing figures:
  findings 19, 2 and 16, carried by the minors batch `TOOL-dSafePassage-35`.

### Edges

- **consumes-from** `TOOL-dSafePassage-22` — the clock read before the census, `REUSE_MARGIN_S` and the lock fixture family; without them there is no estimate to put in one frame
- **hands-off** `TOOL-dSafePassage-35` — the margin's per-backend bound and the timing of the two lock plants, which this unit's boot frame changes on POSIX
- **hands-off** `TOOL-dSafePassage-42` — finding 17 of the spec audit of units 27 to 35, AC1's WSL probe spelled with the path inside the program text

## 4. Design

### Data model

The lock record gains `started_boot`, a float of seconds on `CLOCK_BOOTTIME`, present only where the
platform defines that clock.

```
windows-join row:  estimate = t0_wall - age_s ;  reused = estimate > started      + REUSE_MARGIN_S
posix-ps row:      estimate = t0_boot - age_s ;  reused = estimate > started_boot + REUSE_MARGIN_S
posix-ps row, started_boot absent or t0_boot None:  reused never; would-be reused -> unknown
```

### Why the boot clock

`ps` derives `etimes` from the kernel's uptime less the process's start time, both counted from
boot. On node d's WSL `Ubuntu`, 2026-10-23, `time.clock_gettime(time.CLOCK_BOOTTIME)` read 4.897,
`/proc/uptime` read 4.88 and `ps -o etimes= -p 1` read 4, so the census's age and the boot clock
share one origin there (PINNED, that date). A kernel that counted the start time on a clock that
skips suspend would make `etimes` larger, never smaller, so the estimate would err early, toward
`live`, the safe side; that kernel behaviour is UNVERIFIED on this node.

### Inventory

Minted: `read_boot_clock` in `tools/govkit/upgrade_steps.py` (cell `py.function`, verb `read`, OK by
`python tools/lexicon/lexicon.py --suggest read_boot_clock --as py.function` on 2026-10-23); the lock
key `started_boot`; the plant `lock-wall-step`. No conf key, gate leg or policy key. The `unknown`
verdict is refused by TOOL-dSafePassage-2 S7's existing branch, so `BRANCH_PIN` does not move.

### Migration

Additive. A lock written before this unit has no `started_boot`; on a POSIX judge a reused-looking
holder of that lock reads `unknown` and refuses, as S5 says; on Windows nothing changes.

### Rollout

Live at landing. It builds at order 4, after TOOL-dSafePassage-22 (order 3), whose estimate it splits
by backend.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **`CLOCK_MONOTONIC`.** It skips suspend on Linux while `etimes`, counted from boot, includes it,
  so after a sleep the estimate lands early by the sleep's length. That errs toward `live`, so it is
  safe, but a reused pid of a dead holder then reads live and the lock is never reclaimed; the boot
  clock is exact where the two share an origin.
- **Recording the holder's own creation from the census at take time.** It spawns the census on every
  take, and the census can take up to `BACKEND_TIMEOUT_S` (`tools/process-monitor/census.py:59`).
- **Treating every wall step as unknown by bounding the estimate with elapsed monotonic time.** It
  needs the same boot reading in the lock and buys only the refusal this unit already gives a lock
  without one.

## 5. Production-readiness checklist

- security: the reclaim refuses where the clocks cannot be compared, the deny-by-default side.
- perf / scale: one more clock read per take and per judgement.
- error / empty / loading states: a missing boot reading reads `unknown`, never `dead`, for a pid the
  census still holds.
- observability: the refusal describes the holder as TOOL-dSafePassage-2 S6 prints it.
- risks: on a POSIX node, a lock from a govkit older than this unit whose pid was reused refuses
  rather than reclaims, so an operator clears it.
- testing: the plant of S6 beside TOOL-dSafePassage-22's two, through §7.
- migration: §4 "Migration".
- user docs: N/A — no operator-visible verb or message changes.

## 6. Acceptance criteria

- **AC1** — When `python3 "tools/govkit/upgrade_steps.py" fixture lock --plant lock-dead` runs on
  node d, the lock the take writes carries no `started_boot`, and a `python -c` probe of
  `read_boot_clock` under `wsl.exe -d Ubuntu` prints a float.
  Red when: the key is written as `null` off Linux, or the reading is `None` on Linux.
  fixture: the WSL half needs a WSL distro on the node; node d has `Ubuntu` (read 2026-10-23).
- **AC2** — When `git grep -n -e "read_boot_clock()" -e "scan_processes(" -- tools/govkit/upgrade_steps.py`
  runs, inside `check_holder_dead` both clock reads sit on lines before the census call.
  Red when: a clock is read after the census returns.
- **AC3** — When `python3 "tools/govkit/upgrade_steps.py" fixture lock --plant lock-wall-step` runs,
  the take refuses busy with the holder described, the lock file is unchanged, and the run exits 1.
  Red when: the `posix-ps` row is estimated on the wall clock, the 10 s step makes the live holder
  look reused, and the lock is reclaimed.
- **AC4** — When the same plant runs with the holder's lock written without `started_boot`, the take
  refuses with the holder `unknown` and exits 1, and TOOL-dSafePassage-2's `lock-reused` and
  `lock-dead` still reclaim and exit 0.
  Red when: a missing boot reading lets the wall estimate reclaim, or the plant stops a dead holder
  from ever being reclaimed.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC3 AC4 · the self-test calls `upgrade_steps.py fixture lock` with `lock-wall-step` and its no-boot-reading variant beside `lock-reused` and `lock-dead`, its failing case staged by a judge copy that estimates every row on the wall clock · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the round-1 spec audit of units 15 to 26's
  id 37 (HIGH, item D-5).
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the spec audit of units 27 to 35, written by the disposal stage: `TOOL-dSafePassage-42`; no other section moved.

## 10. Reuse audit

The seam extended is TOOL-dSafePassage-22's estimate in `check_holder_dead`, specced and unbuilt at
the base, over the census's two backends (`tools/process-monitor/census.py:63-70` and `:195-228`).
`python tools/codebase-map/reuse_lookup.py "compare process age with a lock start on one clock"`
ranked `resolve_compare_base`, `derive_run_starts` and `parse_cpu_clock`, none of which reads a boot
clock, so no existing seam fits beyond the estimate itself.

Recall terms used: `python tools/memory-recall/query.py "how were spec audit findings promoted into repair units placed beside the unit they repair" --terms "spec audit promoted unit repair blocker high minors batch disposal order edges rescope"`
