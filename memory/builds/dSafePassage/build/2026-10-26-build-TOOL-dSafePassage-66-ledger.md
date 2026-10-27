**Serves:** journal TOOL-dSafePassage-66

# TOOL-dSafePassage-66 — acceptance ledger

The unit as built, at spec rev-1. `tools/govkit/govkit.py`: the verify pass's per-kit restore (the
kit's wiring undone, each `snap_rows` path put back to its pre-run index entry, the receipt row's
`ROLLBACK_FIELDS` put back, the withdrawn fragments wired again) is `write_kit_restore`, which returns
`restored`, `removed`, `unrestored`, `untouched` and the withdrawn paths whose row was kept. `_cmd_update`
derives `written_paths` right after the `HELD BACK` lines, calls `write_kit_restore` once for each held
kit in `touched_kits` there, before TOOL-dSafePassage-62's receipt write and the step walk, and the
verify pass prints its line, writes its `update-rollback-<eid>.md` order and fails the run from those
lists for a held kit, calling `write_kit_restore` only for a kit whose own check reds.
`tools/govkit/fixtures/retired_edits.py` gains the plant `render-edited-kill` and two observations on
`render-edited`; `tools/govkit/selftest.py`'s `_rte_cases` rows gain the plant; `help/upgrade-steps.md`'s
"After a kill" paragraph gains the held-kit sentence.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. AC1 and AC2 were observed by
the unit's own fixture, `python tools/govkit/fixtures/retired_edits.py --plant <case>`, over its
scratch repositories under `%TEMP%` on node d (Windows, Git Bash), AC1's red by the same plant run
with `govkit.py` at `HEAD` in the working copy; AC3's first half by `git grep`. They stand in for the
`govkit selftest` leg's `[dSafePassage-66]` and `[dSafePassage-9] plant render-edited` rows for this
unit only. `--plant fragment-rollback`, `render-clean` and `render-edited-no-oid`, which reach the
check-red restore and the held restore through the new call sites, still exited 0.

Owed at the close: `govkit selftest` (its `[aHI-4 ha/hg/hz]` arms drive a held kit with a conflicting
row through the moved restore), `govkit refusal join`, `govkit acceptance matrix`, `govkit selfcheck`,
`recall floor arms`, `policy fixtures`, `encoding posture`, `lexicon naming predicates`, `docs` (AC3's
`python tools/govkit/docs_leg.py` exits 0, a gate leg the role hook refuses in this pass), `memory
hygiene`, `spec tokens`; and the new arm's RED-first observation (§7): the `_rte_cases` row
`render-edited-kill`, its red staged by the pre-walk restore taken out of a working copy.

**Evidences:** TOOL-dSafePassage-66
- AC1 — `--plant render-edited-kill` exited 0 printing `the demo kit's eng.txt: 'v2\n'`, `its receipt row's commit: 'B'`, `fx/s1: 'failed · interrupted:'`, `5 of 5 observation(s) matched`. Red: with `govkit.py` at `HEAD` it printed `the demo kit's eng.txt: 'v3\n' · expects 'v2\n' · MISS` and `its receipt row's commit: '480224d4…' · expects 'B' · MISS`, `3 of 5 observation(s) matched`.
- AC2 — `--plant render-edited` exited 0 printing its six existing observations ok, `the demo kit's eng.txt: 'v2\n'` and `the order's restored line: 'True'`, `8 of 8 observation(s) matched`.
- AC3 — `git grep -n -e "held back" -- help/upgrade-steps.md` printed `help/upgrade-steps.md:175`, the "After a kill" sentence. `python tools/govkit/docs_leg.py` is a gate leg the role hook refuses here: owed at the close.
