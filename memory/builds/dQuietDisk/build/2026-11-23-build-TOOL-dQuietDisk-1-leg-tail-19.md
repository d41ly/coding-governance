# TOOL-dQuietDisk-1 leg-tail 19 — codebase-map kit selftest failed in run unattended-179540992358805920005-2030153

**Serves:** leg-tail TOOL-dQuietDisk-1

- **Leg:** codebase-map kit selftest
- **Hash:** 24d9de78844daacc894507c97f6c2c1f1191f9d2
- **Run:** unattended-179540992358805920005-2030153
- **Sha:** 87fdd8497b08c75f63e601a265ac6f30eb285324
- **Cause:** run:dQuietDisk

```
ok   affordance exemption drop on touch (S4a / AC1)
ok   seed-affordances worklist (S4b / AC5)
ok   install sites: copies counted, the canonical source left out
ok   reuse-lookup shared primitives (stems + fan-in + threshold)
ok   reuse-lookup shortlist (AC3 fixture)
ok   the neighbour cap slices the RANKED pool, not the alphabetical one
ok   the same-kind neighbour arm is directory-scoped, both directions
# reuse-lookup: "normalise a display name into a url slug"
# corpus: 3 symbols | 0 inventory keys | 1 affordance seams | 1 dossiers
# a seam = fan-in + installs >= 3 (SEAM_FANIN_THRESHOLD)
# neighbours are ranked by fan-in, which counts NAME TOKENS and resolves no symbols:
# a high rank means 'this name appears a lot'
# scan coverage: 1 files scanned | 0 parse skips | unscanned layers: none — every present layer has an extractor

## candidates (ranked - read these before building)
- slug_case  [function | src/text.py | fan-in 0]  (name stem: slug; via symbol)
- slug_helper  [function | src/text.py | fan-in 0]  (name stem: slug; via symbol)
- slugify  [function | src/text.py | fan-in 0]  (name stem: slug; via symbol/affordance-seam)

## sources to open
- symbol def: src/text.py
- dossier: memory/map/features/text.md

# install sites: none found (no canonical-copy marker in the tracked tree)

Decision: wire the behaviour through one seam above, or reply "no seam fits" if none matches - then record the reuse decision in the feature's ## Reuse affordance.
ok   the map log row records the sources it showed, capped and never fatal
ok   fan-in subtracts every definer (S1)
ok   rank_harness: control and measurement share a denominator (review F5)
ok   replay-phrases: a miss predictor needs a separable AUC AND enough misses
ok   gen_map: every advertised read-only mode runs (review F1)
ok   dark layers: present layers see outside the symbol roots (review F2)
ok   dark layers: no scan is not an empty corpus (review F3)
ok   gate-coverage: a GATE_FILE naming nothing REFUSES (review F6)
ok   dark layers: an undeclared layer refuses with both remedies (AC1)
ok   dark layers: the banner is derived, not declared (AC2/AC4)
ok   dark layers: a stale declaration is reported (AC3)
ok   dark layers: the legacy spelling refuses (AC6)
ok   dark layers: every declared layer is present here (AC5)
ok   shell layer: public definitions only, untokenizable refuses (aMendedFleet-35)
ok   gate-coverage: an uncompared artifact fails (AC1)
ok   gate-coverage: a customised gate passes (AC2)
ok   gate-coverage: an unset GATE_FILE is a named skip (AC3)
ok   gate-coverage: a predicate matching nothing REFUSES
gate-coverage: ok — tools/codebase-map/test_codebase_map.py names every one of the 4 artifact(s) the engine writes. Byte differences from the template are NOT reported: a project is entitled to customise its gate.
ok   gate-coverage: green on this tree
ok   freshness: an orphaned artifact is a refusal (AC2)
ok   freshness: a NEW conditional tier reports itself (AC1/AC4)
ok   gate and template are byte-identical (AC5)
ok   reuse-lookup: the byte budget keeps the first candidate (aMendedFleet-36)
ok   gov-only files withheld on both paths (AC13)
ok   scan coverage line cannot go quiet (AC12)
ok   every co-defined symbol reaches every definer (AC2)
ok   stale dossiers: ancestry, whole and by range, map-root excluded (aMendedFleet-37)
ok   record roots: code and records split, undeclared and dead named (aMendedFleet-86)
FAIL baseline additions: graded against the base, absent base is no comparison (aMendedFleet-40): ({}, 'compared at upstream/main tip')
ok   identifier tokens: one arm per over-strip class
ok   identifier tokens: corpus recall + precision floors
codebase-map selftest: 60 executed, 0 skipped (0 of 4 guarded)
3 FAILURE(S)
```
