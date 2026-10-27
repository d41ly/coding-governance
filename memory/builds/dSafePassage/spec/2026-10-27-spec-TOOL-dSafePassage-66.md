# TOOL-dSafePassage-66 — `update` puts a held kit's writes back before the first upgrade step, so a walk killed inside a step leaves that kit at its pre-run bytes

**Status:** CLOSED · rev-1 · 2026-10-27 · node d · Tier-2 · base 60d90cb7 · streams tooling · order 5 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dSafePassage-66-ledger.md](../build/2026-10-26-build-TOOL-dSafePassage-66-ledger.md) | journal | — |
| [2026-10-27-prompt-TOOL-dSafePassage-66-build-brief.md](../prompts/2026-10-27-prompt-TOOL-dSafePassage-66-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

TOOL-dSafePassage-5's fourth build pass (HEAD `98a01d518`) killed the walk inside each step over a
release-0 tree whose `edited-render` plant holds the lexicon kit back (TOOL-dSafePassage-9 S5,
`tools/govkit/govkit.py:10463-10467`). For all three steps, the re-run's digest differed from `up`'s
and the rollback's from release-0's at the receipt, its sidecar, and the bytes and index entry of
`tools/lexicon/adopt-lexicon.sh`.

A held kit's writes are put back only in the verify pass (`:12236-12632`), after the step walk
(`:11781-11804`). TOOL-dSafePassage-62's receipt, written before the first step (`:11796`), records
them at the tip. The code says so: the held kit's "engine is half old and half new right now, and the
verify pass below puts the new half back" (`:11870-11872`). A kill inside a step ends the run before
that pass. The next run holds the kit again and puts back its pre-run index entry, which is now the
tip, so the kit never returns. This is the class `verdict-printed-before-the-step-that-reverts-it`
(`memory/gotchas/verdict-printed-before-the-step-that-reverts-it.md`): a write the run has decided to
revert outlives the decision when the run dies between them. No record lets it stand: the verify
pass's own order calls a kit half at each vintage "the state this rollback exists to prevent"
(`:12556-12558`). This unit puts a held kit back where the hold is decided, before the walk.

## 2. Scope (IN)

- **S1** — The restore moves to the hold. The verify pass's restore of one kit (`:12285-12540`: the
  kit's wiring undone, each `snap_rows` path put back to its pre-run index entry, and the receipt
  row's `ROLLBACK_FIELDS` put back with it) becomes `write_kit_restore` in
  `tools/govkit/govkit.py`, returning the four path lists the verify pass prints and writes in its
  order. It runs once for each kit in `_held_kits` right after the `HELD BACK` lines
  (`:11769-11771`), before the receipt write of `:11796`, and in the verify pass for a kit whose own
  check reds. Observed by AC1.
- **S2** — The verify pass for a held kit restores nothing again. It prints its `HELD BACK (...) ·
  ROLLED BACK ·` line and writes its `update-rollback-<eid>.md` order from S1's lists, and fails the
  run as today (`:12620-12628`), so the stamp stays withheld (`:13014-13020`). Observed by AC2.
- **S3** — The plants, in `tools/govkit/fixtures/retired_edits.py`. `render-edited-kill`: the
  `render-edited` setup, with commit C also shipping one step `fx/s1` through `tools/govkit/upgrade_steps.py`'s
  `render_fixture_row` and `FIXTURE_WALK_STEP`, its `s1.block-after` set; the `update --write` to C is
  run by `run_killed` and killed while `s1` blocks. The `render-edited` plant gains two observations:
  the demo kit's `eng.txt` and the order's `restored` line naming it. Observed by AC1 and AC2.
- **S4** — The docs. The "After a kill" paragraph of `help/upgrade-steps.md` says a kit held back is
  put back before the first step, so a kill leaves it at the bytes it had. Observed by AC3.

## 3. Non-goals (OUT)

- A held kit as a finding before the walk, so no step walks while a kit is held. It would hold every
  step behind an adopter's unresolved render order, and no record asks for it; TOOL-dSafePassage-2
  §8 F3 stops the walk only on a finding (`:11785-11789`).
- A kit whose own check reds after the run. That red is measured after the walk, so no decision to
  revert exists while a step runs.
- The upgrade-walk leg and its `kill` case, which TOOL-dSafePassage-5 owns.

### Edges

- **hands-off** `TOOL-dSafePassage-5` — the `kill` case's re-run and rollback digests over the held lexicon kit, which equal `up`'s and release-0's once the kit is put back before the walk

Read and closed, so named here rather than joined: TOOL-dSafePassage-62's receipt write before the
first step, which then records the held kit's reverted rows, and TOOL-dSafePassage-9's render hold.

## 4. Design

### Why the kit stays at the tip

The write loop lands every row of the lexicon kit at the tip and holds the kit on the edited render,
adding no finding (`:10463-10467`), so the walk runs (`:11785`). The receipt written before it names
the kit's rows at the tip. Killed inside a step, the run never reaches the verify pass. The re-run
classifies those rows from the tip, holds the kit on the same render, and its verify pass restores
the index entries it found before it ran, the tip's. A rollback from the killed state does the same.

### The move

```
after the HELD BACK lines:
  for eid in _held_kits: restore[eid] = write_kit_restore(eid, ...)     # files, index, rows
  write_install_receipt(...)                                              # TOOL-dSafePassage-62
  run_step_walk(...)
verify pass:
  held kit       -> line, order and r.fail from restore[eid]; nothing restored twice
  check-red kit  -> write_kit_restore(eid, ...) as today
```

The hold set is final at the `HELD BACK` lines: every `_add_held` call sits above them, the last at
`:11767`. The restore's inputs are bound before the walk: `snap_rows` (`:10824`), the pin block's
flags (`:10931-10988`), and the write loop's `changed`, `renamed`, `deleted` and `_landed_new`, from
which `written_paths` (`:12145-12147`) is derived. A held kit's regenerate is already skipped
(`:11875-11880`) and its fragments are not wired (`:12064-12070`), so the restore meets only the write
loop's writes.

### Inventory

Minted: the function `write_kit_restore` (`python tools/lexicon/lexicon.py --suggest
write_kit_restore --as py.function`, OK, 2026-10-27); the fixture plant `render-edited-kill`. No
verdict, role, order kind, conf key, gate leg or receipt field.

### Migration

None. A tree a killed run already left with a held kit at the tip keeps it until an adopter resolves
the render order; the next run then lands the kit whole.

### Rollout

Live at landing, in order 5 beside TOOL-dSafePassage-5, which consumes it and builds after it.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/fixtures/retired_edits.py`
- `tools/govkit/selftest.py`
- `help/upgrade-steps.md`

### Alternatives rejected

- **Record the held kit's rows at their pre-run values before the walk and leave the bytes.** A
  rollback from the killed state then reads the tip bytes as an adopter's edit and keeps them, the
  defect TOOL-dSafePassage-62 closed.
- **Skip a held kit's writes in the write loop.** The hold is decided per row while the loop runs, by
  the problem count (`:11000-11016`), so earlier rows of the kit are already written.
- **Copy the restore loop to the hold.** Two restores of one kit drift; the charter's `[reuse]`.

## 5. Production-readiness checklist

- security: no new write path; the restore's containment check (`:12331-12336`) moves with it.
- perf / scale: unchanged; each held kit is restored once, earlier.
- error / empty / loading states: no held kit restores nothing; a path the restore cannot return is
  reported `NOT restored` in the order, as today.
- observability: the verify line and the order name the same paths as before, now restored before the
  walk.
- risks: a step a held kit declares now runs over that kit's pre-run bytes, where before it ran over
  the half the verify pass then reverted. The verify pass's check of a held kit runs over restored
  bytes, and its verdict is not consulted for a held kit (`:12236`).
- testing: the two plants through the arm of §7.
- migration: none.
- user docs: `help/upgrade-steps.md` (S4).

## 6. Acceptance criteria

- **AC1** — When `python "tools/govkit/fixtures/retired_edits.py" --plant render-edited-kill` runs,
  it exits 0: in the killed state the demo kit's `eng.txt` reads `v2`, its receipt row's `commit` is B,
  and `fx/s1` reads `failed` with `interrupted:`.
  Red when: the restore runs only in the verify pass, so the killed state holds `v3` and a row at C.
- **AC2** — When `python "tools/govkit/fixtures/retired_edits.py" --plant render-edited` runs, it
  exits 0 with its existing observations, the demo kit's `eng.txt` reading `v2`, and the
  `update-rollback-demo.md` order naming that file on a `restored` line.
  Red when: the verify pass restores again or builds its order from empty lists, so the order names no
  restored path.
- **AC3** — When `git grep -n -e "held back" -- help/upgrade-steps.md` runs, it prints the "After a
  kill" sentence, and `python "tools/govkit/docs_leg.py"` exits 0.
  Red when: the page says nothing of a held kit across a kill.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `policy fixtures` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `docs` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · the `_rte_cases` rows (`tools/govkit/selftest.py:18329-18340`) gain `render-edited-kill`, its failing case staged by the pre-walk restore taken out of a working copy · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, from TOOL-dSafePassage-5's fourth build-pass measurement of a
  held kit left at the tip by a walk killed inside a step, by
  `2026-10-27-prompt-TOOL-dSafePassage-5-8-spec-writer.md`.

## 10. Reuse audit

The seam extended is the verify pass's per-kit restore (`tools/govkit/govkit.py:12285-12540`,
DEPL-aHalvedInstall-4 and DEPL-cMendedVintage-2), extracted at its second call site as the charter's
factory rule asks, and TOOL-dSafePassage-62's receipt write before the first step, which it now
precedes. `python tools/codebase-map/reuse_lookup.py "roll back a held kit's writes to the pre-run
index entry before the upgrade step walk"` ranked `run`, `write`, `step`, `resolve_entry` and
`write_commit`: none restores a kit's index entries, and the restore lives inline in `_cmd_update`.
The fixture reuses `upgrade_steps.py`'s `FIXTURE_WALK_STEP`, `render_fixture_row` and `run_killed`
(`tools/govkit/upgrade_steps.py:2093`, `:2246`, `:2381`). The recall probe found TOOL-dSafePassage-62,
DEPL-dRatifiedSeam-2's landed sources outside the verify pass, and DEPL-cMendedVintage-2's restore
reporting. Line numbers are read at `98a01d518`.

Recall terms used: `python tools/memory-recall/query.py "a kit held back by update is rolled back only after the upgrade step walk, so a killed walk leaves it at the new vintage" --terms "held back kit rollback verify phase step walk killed receipt pre-run index entry render-edited restore"`
