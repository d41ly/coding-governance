# TOOL-dLinkedLibrary-49 — `--observe` records `refused` only on the leg's failing status, bounded, and every other outcome as `unobservable`

**Status:** DEFERRED · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 6 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102 |
| [2026-10-26-build-TOOL-dLinkedLibrary-49-deviation-491.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-49-deviation-491.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 25 unit specs
(`memory/builds/dLinkedLibrary/reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md`) confirmed
finding **id 64 at HIGH**, report item **R13**. No other id shares the item.

`TOOL-dLinkedLibrary-24` S3 records `refused` for any non-zero exit of the planted run: a crash, an exit-2
usage or environment error, or a signal all read as the leg refusing the plant, and no timeout is stated.
A plant that breaks the leg's own script, a missing interpreter or a signal then makes the class `gated`,
and that unit's S5 leaves it off every review checklist: a gate claiming a refusal it never saw. A
hanging run blocks `--observe` for ever.

This unit records `refused` only when the clean run exits 0 and the planted run exits the leg's failing
status, bounds both runs by the leg's own ceiling, and records every other outcome as `unobservable`
with its reason. It repairs `TOOL-dLinkedLibrary-24` and builds one step after it (order 6).

## 2. Scope (IN)

- **S1** — The verdicts. `gotchas.py --observe` (`TOOL-dLinkedLibrary-24` S3) records, per class:
  `refused` when the clean run exits 0 and the planted run exits 1, the failing status the house's checks
  use (exit 1 on a finding, 2 on a refusal); `passed` when both exit 0; and `unobservable: <reason>` for
  every other outcome, a clean run that does not exit 0, a planted exit of 2 or more, a death by signal,
  or a run past the bound. Observed by AC1, AC2 and AC3.
- **S2** — The bound. Each run is given the leg's manifest `ceiling` in seconds, read with the leg's argv
  from `LEG_MANIFEST`; a leg with no `ceiling` is bounded at 300 seconds, the `gotchas selftest` leg's own
  ceiling (`tools/gate-legs.json:530`). A run past it is killed and recorded `unobservable: past <n>s`.
  Observed by AC3.
- **S3** — The status reads it. `derive_gate_status` (`TOOL-dLinkedLibrary-24` S2) reads `unobservable`,
  whatever its reason, as `partly-gated`, so a class whose observation is not a clean refusal stays on
  every checklist. Observed by AC2 and AC3.
- **S4** — The page. The bug-class catalogue's sentence on `--observe` in
  `tools/memory-tree/HYGIENE.template.md`, rendered into `memory/HYGIENE.md`, says which exits count as a
  refusal, the bound, and what `unobservable` means. Observed by AC4.

## 3. Non-goals (OUT)

- Whether the plant stages the class's mistake rather than any break: `TOOL-dLinkedLibrary-24` §4 names it
  the record reviewer's question.
- A leg whose failing status is not 1: none is declared in the manifest at base; such a leg would declare
  its status in its row, which no row carries.
- The class-to-leg link and the observation's record: id 33's item in `TOOL-dLinkedLibrary-52`.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-24` — `gotchas.py --observe` and `derive_gate_status`, whose exit reading S1 and S2 replace (id 64)
- **hands-off** `TOOL-dLinkedLibrary-61` — S2's bound, which unit 61 enforces over the process tree (id 24 of the spec audit of units 37 to 53)
- **hands-off** `TOOL-dLinkedLibrary-64` — `--observe`'s runs and verdict spellings, which unit 64 completes (ids 18, 11 of the spec audit of units 37 to 53)

## 4. Design

### Evidence

- `TOOL-dLinkedLibrary-24` S3: "a clean run that exits non-zero records `unobservable`, a planted run that
  exits non-zero records `refused`"; its §4 table reads `refused` as `gated`.
- `tools/gate-legs.json:530` gives the `gotchas selftest` leg `"ceiling": 300`.
- The house convention of exit 1 on a finding and 2 on a refusal: `TOOL-dLinkedLibrary-9` S3 and
  `TOOL-dLinkedLibrary-4` S9, among this build's own checks.

### The observation's verdicts

| Clean run | Planted run | Recorded |
|---|---|---|
| exit 0 | exit 1 | `refused` |
| exit 0 | exit 0 | `passed` |
| exit 0 | exit 2 or more, or a signal | `unobservable: planted exit <n>` |
| exit 0 | past the bound | `unobservable: past <n>s` |
| not exit 0, or past the bound | not run | `unobservable: clean exit <n>` |

### Files touched (estimate)

- `tools/memory-tree/gotchas.py`: S1 to S3, and the plants of §6
- `tools/memory-tree/HYGIENE.template.md`, `memory/HYGIENE.md`: S4

### Alternatives rejected

- **Any non-zero planted exit as `refused`, with the stderr inspected.** Reading a leg's message for its
  meaning is a parse of free text per leg; the exit status is the contract the runner already reads.
- **No bound, the runner's wall clock trusted.** `--observe` runs outside the bar, where no wall clock
  stands over it.

## 5. Production-readiness checklist

- security — runs the leg's own argv in a scratch clone, as `TOOL-dLinkedLibrary-24` S3; the bound kills
  the child it started and nothing else.
- perf / scale — at most two bounded runs per class.
- error / empty / loading states — every outcome other than a clean refusal is `unobservable` with a
  reason, never `refused`.
- observability — the verb prints `observed — <class> · <leg> · <verdict>` with the reason.
- risks — a leg that legitimately refuses with 2 reads `unobservable`; it stays `partly-gated`, the safe
  side.
- testing — the plants of §6 in `gotchas.py --selftest`.
- migration — an observation recorded before this unit is re-run by S8's backfill at its pass.
- user docs — `memory/HYGIENE.md`, S4.

## 6. Acceptance criteria

- **AC1** — When `python gotchas.py --fixture --plant observe-refused` runs `--observe` against a stub leg
  exiting 0 clean and 1 planted, it records `refused` and the class reads `gated`.
  Red when: the clean refusal is not recognised.
- **AC2** — When `--plant observe-usage-error` runs against a stub leg exiting 2 on the plant, it records
  `unobservable: planted exit 2` and the class reads `partly-gated`.
  Red when: an error exit is recorded as a refusal.
- **AC3** — When `--plant observe-hang` runs against a stub leg declaring `ceiling` 2 that sleeps 10
  seconds on the plant, `--observe` returns within 5 seconds, records `unobservable: past 2s`, and the
  class reads `partly-gated`.
  Red when: the run is unbounded, or a timeout reads as a refusal.
- **AC4** — When `grep -n "unobservable" memory/HYGIENE.md` runs, it finds the catalogue sentence naming
  the failing status, the bound and the reading.
  Red when: the page says any non-zero exit is a refusal.

## 7. Gates

`gotchas selftest` · `policy fixtures` · `recall floor` · `recall floor arms` · `memory hygiene` · `kit/dogfood doc parity` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gotchas.py · covers AC1 AC2 AC3 · the three observation plants against stub legs, the failing case staged by recording `refused` on any non-zero planted exit · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 24 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of the 25 unit specs, id 64
  (HIGH, item R13).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-61, TOOL-dLinkedLibrary-64, promoted from the spec audit of units 37 to 53; nothing else moved.

## 10. Reuse audit

The seams extended are `TOOL-dLinkedLibrary-24`'s `--observe` and `derive_gate_status` in
`tools/memory-tree/gotchas.py`, which already read the leg's argv from `LEG_MANIFEST` through
`load_leg_names` (`tools/memory-tree/gotchas.py:191`); S2 reads the `ceiling` beside it. `python
tools/codebase-map/reuse_lookup.py "classify a child process exit as failure versus error with a
timeout"` ranked `MapError`, `classify` and two error classes, none an exit reader, so no existing seam
fits beyond the verb being repaired.

Recall terms used: `python tools/memory-recall/query.py "how is a promoted spec-audit finding repaired by a unit placed after the unit it repairs" --terms "spec-audit promoted finding repairs order rescope add batch minors disjoint write set"`
