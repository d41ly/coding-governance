**Serves:** journal TOOL-dDeclaredLoop-14

# Builder return — TOOL-dDeclaredLoop-14, dispatch 3: the driver's refusal census and the field-shape family are full

## Why

DIVERGENCE: section 5 ("risks") does not account for the driver's refusal budget, and that budget is already full. Building S3 as written would newly red the `harness arms (fail branches armed or pinned)` leg twice.

(1) The census ceiling. `REFUSAL_CEILINGS` in .memory-tree.conf caps tools/unattended/unattended.sh at 324 (2026-11-10, TOOL-aSmoothedDispatch-2). I measured the census at base with check-arms.py's own `branches` and `scan_refusal_sites` readers: 319 fail branches plus 5 refusal sites, 324 in all. That is exactly the ceiling.
- S3 requires `write_refusal` to add new check-48 refusals: line-end, separator, bypass flag, the engine's refusal, and the unarmed-engine refusal.
- The engine and unarmed cases need a `fail 48 "<literal>"` site, because a site with no literal of 12 or more characters is a hard error in check-arms.
- So even a single new site makes the census 325, over the ceiling. check-arms reds it with "growth past the budget is raised only through the retirement review in the memory-tree README, with a dated decision id".

(2) The field-shape family. tools/unattended/unattended.families.txt caps `field-shape` (ERE `newline|carriage return|field separator|own separator|bypass flag`) at 37, and it measures 36. S3's three field guards (line-end, separator, bypass flag) make it 39.

Both raises need a decision id that a memory/DECISIONS.md row carries. This pass may not write that shared record: check 49 refuses it, as the second dispatch found. No such row exists today; DECISIONS.md holds only the Skill size row for this unit. Section 4 "Files touched" also lists neither .memory-tree.conf nor tools/unattended/unattended.families.txt.

What the spec would have to say:
- **Section 5 risks** names both budgets (the unattended.sh census at 324/324 and the field-shape family at 36/37) and how this unit stays inside them. Either:
  - (a) raise both. The decision row for each lands in memory/DECISIONS.md ahead of the pass in a records commit, as rev-6 did for the Skill row. The pass then raises the ceiling to the new census, with a `RAISED` comment line in the shape of the existing ones, and raises the family's ceiling. Or:
  - (b) name the consolidation that keeps the count flat, for example the three field-shape guards factored out of `verb_propose` into one shared helper that both verbs call. The existing `verb_propose` arms at unattended.test.sh lines 6510, 6515 and 6520 would have to move with it.
- **Section 4 Files touched** gains .memory-tree.conf and tools/unattended/unattended.families.txt for (a), or `verb_propose` and its arms for (b).
- **Section 7** keeps `harness arms (fail branches armed or pinned)` and says the close observes the ceiling line `check-arms: ceiling tools/unattended/unattended.sh <census>/<ceiling>`.

The rest of rev-6 was checked and holds, with nothing else found that would newly red:
- position.py: `derive_next_item`, `PLANTS`, `run_plant`, and the composition fallback that deviation 145 records.
- In the driver: `park`, `verb_propose`, `verb_plan`, `resolve_position_engine`, `VERB_REQUIRES`, `VERBS_SLUG`, and the argument loop between the `gov:argv` markers.
- check-unattended.sh checks 26, 27 and 52.
- In the suite: `PARITY_ROWS`, `_rf_matrix`, `run_hostile_verb`.
- The `loop position fixtures` rows in gate-legs.json and selftest-budgets.txt, and the `principle.p24` pending row.

## Summary

I committed nothing for TOOL-dDeclaredLoop-14 and wrote nothing. The driver's refusal budget is already full, so the spec's new check-48 refusals would red the `harness arms` leg twice; the spec needs revising first (details in `why`). The tree is clean at base d4d80fe3897691d3b81f8dc057da546f4e462165, so no patch file was needed.

**Not run, and why:**
- `--dispatch` and `--brief`: the divergence was found before the first write, and both verbs write rows to RUN.md.
- `gotchas.py --for-diff`: there is no commit to check.
- Deviation record 145 (the `--check-refusal` handling, where an unarmed composition (exit 2) falls back to gov's own `[[item]]` rows): not written, because no pass ran. It is still owed by the pass that builds this unit, at memory/builds/dDeclaredLoop/build/2026-11-15-build-TOOL-dDeclaredLoop-14-deviation-145.md.

**Checks that ran, all read-only, none a gate:**
- A refusal-budget probe, which stands in for the ceiling and families arms of the `harness arms (fail branches armed or pinned)` leg. It imported check-arms.py's `branches` and `scan_refusal_sites` readers, not its `--check`, from C:/Users/DAILY-~1/AppData/Local/Temp/claude/b120d4a7f8b5be2e/7c85732c-fa0c-43e9-83f2-238d293195e0/scratchpad/census.py. It measured:
  - tools/unattended/unattended.sh at 319 branches plus 5 sites, 324 against its ceiling of 324;
  - families `missing-run-state` at 1/1, `required-flag` at 11/11 and `field-shape` at 36/37.
- Reads of the code the spec relies on: tools/loop/position.py whole; in tools/unattended/unattended.sh, `park`, `verb_propose`, `verb_plan`, `resolve_position_engine`, `VERB_REQUIRES`, `PARK_KINDS`, the argument loop and the dispatch; tools/unattended/check-unattended.sh checks 26, 27 and 52; in tools/unattended/unattended.test.sh, `PARITY_ROWS`, `_rf_matrix` and `run_hostile_verb`.
- Reads of the rows the spec cites: the gate-legs.json rows for `loop position fixtures` and `harness arms`, the selftest-budgets.txt row, and core-pending.txt's `principle.p24` row.

**Still owed at the close once the unit is built, unchanged from section 7:** the RED-first observation of both `New arm:` lines (the position.py frontier plants, and the unattended.test.sh `--refused` arms), the `core meta-check` for AC8, the re-price of the `loop position fixtures` budget row, the ceiling and families check above, and the bar.
