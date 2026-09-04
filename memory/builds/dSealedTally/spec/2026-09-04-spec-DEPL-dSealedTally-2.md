# DEPL-dSealedTally-2 — `rename_dests` is populated eagerly, before any row can exit

**Status:** CLOSED · rev-3 · 2026-09-04 · node d · Tier-2 · base 0f19429a · streams deployer · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-build-DEPL-dSealedTally-2-1-acceptance-ledger.md](../build/2026-09-04-build-DEPL-dSealedTally-2-1-acceptance-ledger.md) | journal | — |
| [2026-09-04-prompt-DEPL-dSealedTally-1-0-run-mandate.md](../prompts/2026-09-04-prompt-DEPL-dSealedTally-1-0-run-mandate.md) | journal | DEPL-dSealedTally-1 DEPL-dSealedTally-3 DEPL-dSealedTally-4 DEPL-dSealedTally-5 TOOL-dSealedTally-1 |
| [2026-09-04-review-DEPL-dSealedTally-1-spec-audit-round1.md](../reviews/2026-09-04-review-DEPL-dSealedTally-1-spec-audit-round1.md) | spec-audit | DEPL-dSealedTally-1 DEPL-dSealedTally-3 DEPL-dSealedTally-4 DEPL-dSealedTally-5 TOOL-dSealedTally-1 |

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
- **S4** `_decided` is NARROWED to the destinations of sources gov actually renamed:
  `for _new_src in renames.values(): _decided.update(_m.get(_new_src) or [])`. Without this the
  eager fill makes `_decided` the entire declared surface of every kit, and nothing can ever land
  as an unclaimed source. Discovered while building, by the `[-RS1]` arms going red.
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

The eager fill WRAPS the resolver in a `try/except Refusal: continue`, copying the landing
block's own handling at `tools/govkit/govkit.py:6216` and its stated reason. Without it the
hoist moves a refusal that previously fired only for kits whose rows reached line 5956 onto
EVERY kit in the walk, so one unresolvable descriptor would abort a run that used to skip it.

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
- risks — TWO directions, and rev-1 named only one. Over-exclusion shows as a source not landing,
  visible in the read-only preview before any write. The second is the hoist moving an
  unresolvable descriptor’s `Refusal` onto every kit’s path; the Migration bullet’s
  `try/except` is what bounds it, and AC5 observes it.
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
- **AC4** — When a kit carries a descriptor that raises `Refusal` during the eager fill, the run
  SKIPS that kit and completes, proved by an arm in `tools/govkit/selftest.py` — the hoist must
  not move a refusal onto a path that previously never reached it.
- **AC5** — When the `try/except Refusal` is removed by mutation in a scratch copy of
  `tools/govkit/govkit.py`, the AC4 arm FAILS, recorded as an observed staged break.
- **AC6** — When `python tools/govkit/selftest.py` runs, it exits 0 and its arm count is at
  least 4 greater than the count observed at base `0f19429a`, which is this build’s FIRST step
  and so the only unit that may pin against the base count.

## 7. Gates

`govkit selftest` · `memory-hygiene` · `bash tools/run-gates/run-gates.sh` with
`GATE_FULL=1 GATE_SELFTESTS=1`.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft, grounded against `tools/govkit/govkit.py` lines 5922-5967 and
  7005-7020 at `0f19429a`.
- rev-2 · 2026-09-04 · folded the spec audit’s M3 and H5. M3: the hoist moves an unwrapped
  `Refusal` onto every kit’s path, where it previously fired only for kits whose rows reached the
  fill site — the Migration bullet now wraps it and AC4/AC5 observe it, and the §5 risks bullet
  named only one direction. H5: the arm-count criterion states a delta, and this unit is the one
  that may measure against the base because it is `order 1`.

- rev-3 · 2026-09-04 · BUILT, and the build changed the mechanism, so the spec moved first. The
  hoist alone broke the unclaimed-source landing: `rename_dests[eid]` is a kit's FULL
  source-to-destination map, and `_decided` took every value in it, so filling eagerly made
  `_decided` the whole declared surface of every kit and nothing could land. Latent while the fill
  was lazy, because a run with no renames left the map empty. Seven `[-RS1]` arms caught it. S4
  adds the narrowing, and the unit is two changes rather than one.
## 10. Reuse audit

The seam is `rename_dests` itself, in `tools/govkit/govkit.py`, and this unit deliberately does not
add a second one — the "Alternatives rejected" note above is the reuse decision, taken because a
second model of what a rename destination is would be two answers to one question. The
`reuse_lookup.py` probe for the landing behaviour returned no candidate closer than the file's own
`target_context`, which is not this concern.

Recall terms used: `govkit update receipt rollback verify snapshot touched_kits landing unclaimed
sources liveness dead probe index_read topology`
