# DEPL-dSealedTally-2 — `rename_dests` is populated eagerly, before any row can exit

**Status:** SPECCED · rev-1 · 2026-09-04 · node d · Tier-2 · base 0f19429a · streams deployer · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-prompt-DEPL-dSealedTally-1-0-run-mandate.md](../prompts/2026-09-04-prompt-DEPL-dSealedTally-1-0-run-mandate.md) | journal | DEPL-dSealedTally-1 DEPL-dSealedTally-3 DEPL-dSealedTally-4 DEPL-dSealedTally-5 TOOL-dSealedTally-1 |

<!-- /gen:spec-records -->

## 1. Goal

The unclaimed-source landing excludes a destination the rename machinery already decided, by
reading `rename_dests`. That map is filled lazily inside the row walk, so a kit whose rows all exit
before the fill leaves it empty, and the landing re-lands a rename destination it is specifically
written not to touch. Fill it per kit, before the walk can skip it.

## 2. Scope (IN)

- **S1** `rename_dests[eid]` is populated for every kit the walk visits, at the point the kit is
  entered, rather than at the first row that reaches the fill site at line 5956.
- **S2** The landing block's `_decided` set therefore holds every rename destination for every kit
  in `(kits or claimed)`, not only those whose rows survived to the fill.
- **S3** A staged-RED arm proving the gap: a kit whose only row `continue`s before `classify_row`,
  whose descriptor declares a rename destination, and whose destination is landed as new before the
  change and refused after.

## 3. Non-goals (OUT)

- Not changing the rename machinery itself. What a rename IS, and how `by_src` is derived, is
  settled and is only being called earlier.
- Not widening `_decided` to hold anything else. Withdrawn rows are already in it and the
  `--kits` scoping is already fixed by `DEPL-dRatifiedSeam-1`.
- Not memoising across runs. The map is per-run by design.

## 4. Design

### Data model

`rename_dests` stays `dict[str, dict[str, list[str]]]` — kit id to source path to destination list.
Only WHEN it is filled changes. The existing guard `if eid not in rename_dests` becomes the
eager call site's guard, so the map is still built at most once per kit and the walk's own lookup
at line 5967 reads a map that is already there.

### Migration

None. The map is per-run and never persisted.

### Rollout

One code path. The change can only widen `_decided`, which can only turn a landing into a refusal,
never the reverse — so the failure direction it opens is a source that fails to land, which the
preview reports, rather than a source that lands wrongly.

### Files touched (estimate)

`tools/govkit/govkit.py` (~15 lines: hoisting the fill to the kit's entry point).
`tools/govkit/selftest.py` (~40 lines: the staged-RED arm and its mutation control).

### Alternatives rejected

Computing `_decided` from the descriptors directly in the landing block, bypassing `rename_dests`
entirely. Rejected: it would be a second model of what a rename destination is, and the two would
disagree the first time either changed. The map already answers the question; it just answers it
too late.

## 5. Production-readiness checklist

- security — no new write path. The change can only add exclusions to a landing decision.
- perf / scale — the fill moves earlier for kits whose rows all exit early, which is the rare case;
  for every other kit the work is identical and happens once either way.
- a11y — N/A — a CLI verb with no rendered surface.
- i18n — N/A — operator-facing English strings.
- error / empty / loading states — a kit with no renames fills an empty map, exactly as today.
- observability — the preview's `would REFUSE` line already names the reason; a destination
  excluded as already-decided is simply not offered, which is the existing behaviour.
- risks — the only new failure direction is over-exclusion, which shows as a source not landing.
  That is visible in the read-only preview before any write.
- testing + left-shift gates — S3's arm is the left-shift and fails before the change.
- migration / rollback — reverting the commit is the rollback.
- user docs — N/A — no user-facing page.

## 6. Acceptance criteria

- **AC1** — When a kit's rows all `continue` before `classify_row` and its descriptor declares a
  rename destination, `python tools/govkit/selftest.py` shows that destination REFUSED rather than
  landed.
- **AC2** — When the eager fill is reverted in a scratch copy, the AC1 arm FAILS, recorded as an
  observed staged break in `tools/govkit/selftest.py` rather than asserted.
- **AC3** — When an ordinary kit whose rows DO reach the fill site runs, `tools/govkit/selftest.py`
  reports the same landing decisions as at base `0f19429a`, so the hoist changes nothing else.
- **AC4** — When `python tools/govkit/selftest.py` runs, it exits 0 with an arm count strictly
  greater than the 1074 it reports at base `0f19429a`.

## 7. Gates

`govkit selftest` · `memory-hygiene` · `bash tools/run-gates/run-gates.sh` with
`GATE_FULL=1 GATE_SELFTESTS=1`.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft, grounded against `tools/govkit/govkit.py` lines 5922-5967 and
  7005-7020 at `0f19429a`.

## 10. Reuse audit

The seam is `rename_dests` itself, in `tools/govkit/govkit.py`, and this unit deliberately does not
add a second one — the "Alternatives rejected" note above is the reuse decision, taken because a
second model of what a rename destination is would be two answers to one question. The
`reuse_lookup.py` probe for the landing behaviour returned no candidate closer than the file's own
`target_context`, which is not this concern.

Recall terms used: `govkit update receipt rollback verify snapshot touched_kits landing unclaimed
sources liveness dead probe index_read topology`
