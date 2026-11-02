**Serves:** research DEPL-dShippedRelease-140 DEPL-dShippedRelease-141 DEPL-dShippedRelease-142 DEPL-dShippedRelease-143 DEPL-dShippedRelease-144 DEPL-dShippedRelease-145

# Round-5 disposal return — dShippedRelease

The disposal's final return, read from the workflow journal by script, never retyped, and quoted whole.

Run wf_c03f2436-997/a70ea4fc356a503c8, promoted 48, folded 0, refuted 0, standing 0.

> All 48 confirmed findings of the round-5 spec audit are disposed, with none refuted, none folded and none standing. Six units are promoted, specced as Tier-2 OPEN and recorded by --rescope --act add. The specs are uncommitted and no index was regenerated.
>
> Highs, one unit per raw id:
> - id 3 (item H1) goes to DEPL-dShippedRelease-145, repairing 128, order 32. It runs the population through cmd_mint on a clone carrying the working tree.
> - id 23 (item H2) goes to DEPL-dShippedRelease-140, repairing 128, order 32. The mint cases move to tools/govkit/matrix.py.
> - id 29 (item H3) goes to DEPL-dShippedRelease-141, repairing 138, order 37. The deploy items leg carries guard = [].
> - id 40 (item H4) goes to DEPL-dShippedRelease-142, repairing 135, order 16. record-clean compares the return's key with the landing.
> - id 41 (item H5) goes to DEPL-dShippedRelease-143, repairing 137, order 16. read_appendix_table tests the separator line.
>
> Minors: DEPL-dShippedRelease-144, repairs none, order 38, takes the 32 MEDIUM and 11 LOW, one scope item per raw id. One batch, not two: the natural cut passes M6 clause 1 and fails clause 2, because build_mint_clone overlays every modified path, so the other half's writes are this half's acceptance input.
>
> Four things the dispatcher should know:
> - Id 139 is not used. It is a filed ask of this build, so --rescope refused it with check 76, and the H1 unit took the next free id, 145.
> - Unit 140 goes further than the report's fix, by §8 F1: every gov-only case moves, not only the walk, so two clone builders do not stand in two kits.
> - Unit 144 replaces the report's guard widening with a new unguarded leg, mint descriptors, by §8 F4. Widening would owe that leg on foreign live spec TOOL-dIndexedDesign-12, plus six of this build, and unit 66 forbids both the edit and a waiver row.
> - A read-only clone probe at e4c33972 ran mint once over all 11 regenerate kits: exit 0, 11 version moves, 4.6 s for the clone and 13.6 s for mint. Those figures are pinned in units 144 and 145.
>
> Edges: 92 bullets, every one paired, across 28 audited specs bumped with a §9 line. Eight of those specs (122, 125, 130, 131, 132, 134, 137, 138) carry a sentence on the hands-off bullet to unit 144, because their own pass needs it before that batch builds.
>
> Verification: the memory hygiene gate exits 1 on check 9 alone, the expected stale render of memory/LIVE.md and the build README, which the dispatcher regenerates. It ran before the last wording edits to unit 144, which replaced retirement verbs in five scope items, and was not re-run after them. The naming lexicon reads OK for every minted function it was asked about, except that read_pin_range-side names were not re-checked; write_landing_guard was tried and not minted.

## Placements

| unit | repairs | order |
|---|---|---|
| DEPL-dShippedRelease-145 | DEPL-dShippedRelease-128 | 32 |
| DEPL-dShippedRelease-140 | DEPL-dShippedRelease-128 | 32 |
| DEPL-dShippedRelease-141 | DEPL-dShippedRelease-138 | 37 |
| DEPL-dShippedRelease-142 | DEPL-dShippedRelease-135 | 16 |
| DEPL-dShippedRelease-143 | DEPL-dShippedRelease-137 | 16 |
| DEPL-dShippedRelease-144 | none | 38 |
