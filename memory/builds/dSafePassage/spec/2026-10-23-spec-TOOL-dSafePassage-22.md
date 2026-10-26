# TOOL-dSafePassage-22 — the lock reclaim reads its clock before the census, so a slow census errs toward live

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 3 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-22-deviation-68.md](../build/2026-10-23-build-TOOL-dSafePassage-22-deviation-68.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-26-prompt-TOOL-dSafePassage-22-build-brief.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-22-build-brief.md) | journal | — |
| [2026-10-23-review-TOOL-dSafePassage-15-16-17-18-19-20-21-22-23-24-25-26-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-15-16-17-18-19-20-21-22-23-24-25-26-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-16 TOOL-dSafePassage-20 TOOL-dSafePassage-15 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-24 TOOL-dSafePassage-17 TOOL-dSafePassage-23 TOOL-dSafePassage-25 TOOL-dSafePassage-21 TOOL-dSafePassage-26 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md`)
confirmed finding **id 16** at HIGH, its item **D-6**. TOOL-dSafePassage-2 estimates a census row's
creation time as `now - age_s` and never says when `now` is read (its spec, §4 "The reclaim and the
census", line 185); S7 reads a row created more than two seconds after the lock's `started` as a
reused pid, so the lock reads dead. On Windows `age_s` is sampled inside the census's PowerShell CIM
query (`_CIM_QUERY`, `tools/process-monitor/census.py:63`), rounded to whole seconds, in a backend
allowed 90 seconds (`BACKEND_TIMEOUT_S`, `:59`). Read after the census returns, `now` makes a live
holder look younger by the census's latency, and under load the live lock is reclaimed while its
holder writes. This unit is id 16's promotion: `now` is read before the census is spawned, so the
estimate can only err early, toward "created before the lock", which reads `live` and refuses.

## 2. Scope (IN)

- **S1** — The clock read. `check_holder_dead` reads `time.time()` once, immediately before it calls
  the census's `scan_processes`, and estimates each row's creation as that reading less the row's
  `age_s`. No clock read after the census enters the estimate. Observed by AC1 and AC2.
- **S2** — Why that side. The census samples each row at some time no earlier than the reading, so
  the estimate is at most the true creation time plus the census's half-second rounding, at any
  latency. A live holder, created before it took its lock, therefore never estimates later than the
  lock's `started` plus half a second, inside the window. Observed by AC1.
- **S3** — The window named. The two-second margin of TOOL-dSafePassage-2 §4 is the constant
  `REUSE_MARGIN_S = 2.0` in `tools/govkit/upgrade_steps.py`, its comment stating that it covers the
  census's rounding and no latency. A reused pid seen through a slow census estimates early too and
  reads `live`, which refuses, the safe direction. Observed by AC2.
- **S4** — The plant. The `lock` family of `python3 "tools/govkit/upgrade_steps.py" fixture` gains
  `lock-live-slow-census`: the holder takes its lock within one second of starting, and the fixture
  wraps the loaded census's `scan_processes` with a three-second delay inside the fixture process
  only, so no switch ships. Observed by AC1.

## 3. Non-goals (OUT)

- The pid's namespace across WSL and Windows: id 58, `TOOL-dSafePassage-26`.
- A census that refuses or times out, which reads `unknown` and refuses as TOOL-dSafePassage-2 S7 says.
- Changing the census module or its rounding.

### Edges

- **consumes-from** `TOOL-dSafePassage-2` — `check_holder_dead`, the census load and the `lock` fixture family; without them there is no reclaim to correct
- **hands-off** `TOOL-dSafePassage-26` — recording the pid's namespace in the lock and judging a holder from another namespace unknown, the reclaim's other liveness gap
- **hands-off** `TOOL-dSafePassage-32` — the reuse estimate on one clock per census backend, the boot clock on POSIX, the repair of finding 37 of the round-1 audit of units 15 to 26
- **hands-off** `TOOL-dSafePassage-35` — the minors batch of the round-1 audit of units 15 to 26, which pins the two lock plants' timing, states the margin per backend and guards the leg on the census

## 4. Design

### Data model

The estimate, with `t0` the clock read before the census spawn and `t_s` the census's own sample of
the row, `t_s >= t0`:

```
estimate = t0 - age_s,   age_s = round(t_s - created)
estimate <= created + 0.5          at any census latency
reused   = estimate > started + REUSE_MARGIN_S
```

### Inventory

Minted: the constant `REUSE_MARGIN_S` in `tools/govkit/upgrade_steps.py`; the plant
`lock-live-slow-census`. No function, conf key, gate leg or policy key.

### Migration

None.

### Rollout

Live at landing. It builds at order 3, after TOOL-dSafePassage-2 (order 2), and shares
`tools/govkit/upgrade_steps.py` with the other order-3 repairs, so the build run sequences those
passes by M6's disjointness rule.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **A wider margin with `now` read after the census.** Any margin is beaten by a slower census; the
  latency stays in the estimate.
- **Reading the process's creation time directly**, as `read_process_created` in
  `tools/run-gates/measure_legs.py` does. TOOL-dSafePassage-2 §4 rejected it as Windows-only.

## 5. Production-readiness checklist

- security: the reclaim now refuses wherever the census is too slow to tell, the deny-by-default
  side.
- perf / scale: unchanged.
- error / empty / loading states: unchanged; a refused census reads `unknown`.
- observability: the refusal describes the holder as TOOL-dSafePassage-2 S6 prints it.
- risks: a reused pid behind a slow census is refused rather than reclaimed, so an operator clears
  it; that is the cost of never reclaiming a live lock.
- testing: the plant of S4 and TOOL-dSafePassage-2's `lock-reused`.
- migration: none.
- user docs: N/A — no operator-visible verb or message changes.

## 6. Acceptance criteria

- **AC1** — When `python3 "tools/govkit/upgrade_steps.py" fixture lock --plant lock-live-slow-census`
  runs, the take refuses busy with the holder described and the remedy naming the reclaim, the
  holder's lock file is unchanged, and the run exits 1.
  Red when: the estimate reads the clock after the census, the live holder looks reused, and the
  lock is reclaimed.
- **AC2** — When `python3 "tools/govkit/upgrade_steps.py" fixture lock --plant lock-reused` runs with
  no delay, TOOL-dSafePassage-2's reused pid is still reclaimed and the run exits 0, and
  `git grep -n "REUSE_MARGIN_S" -- tools/govkit/upgrade_steps.py` prints the constant and its use in
  `check_holder_dead`.
  Red when: the clock move stops a reused pid from ever being reclaimed, or the margin is a bare
  literal.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · the self-test calls `upgrade_steps.py fixture lock` with `lock-live-slow-census` beside `lock-reused`, its failing case staged by a judge copy that reads the clock after the census · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the round-1 spec audit's id 16 (HIGH, item
  D-6).
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the round-1 audit of units 15 to 26, written by the disposal stage: `TOOL-dSafePassage-32`, `TOOL-dSafePassage-35`; no other section moved.

## 10. Reuse audit

The seam extended is TOOL-dSafePassage-2's `check_holder_dead` over the process-monitor census,
`scan_processes` (`tools/process-monitor/census.py:260`), whose row field `age_s` (`:19`) and CIM query
(`:63`) this unit read. `python tools/codebase-map/reuse_lookup.py "compare a process creation time with
a lock start time read before the census"` ranked `read`, `read_text`, `before` and `census`
(`merge-rows.py`), name-token matches, so no existing seam fits beyond the census itself.

Recall terms used: `python tools/memory-recall/query.py "how were spec audit findings promoted into repair units placed beside the unit they repair" --terms "spec audit promoted unit repair blocker high minors batch disposal order edges rescope"`
