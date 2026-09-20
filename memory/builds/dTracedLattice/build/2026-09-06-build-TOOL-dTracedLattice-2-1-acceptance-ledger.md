# TOOL-dTracedLattice-2 — acceptance ledger

**Serves:** journal TOOL-dTracedLattice-2

**Evidences:** TOOL-dTracedLattice-2
- AC1 — `python3 tools/codebase-map/selftest.py` — the arm `freshness: a NEW conditional tier reports itself (AC1/AC4)` asserts the run prints `skipped widget tier … NOTHING WAS COMPARED` and does NOT refuse, because that tier's artifact is absent. Observed RED against the pre-fix `if population:` with no `else`, which printed nothing at all
- AC2 — `python3 tools/codebase-map/selftest.py` — the arm `freshness: an orphaned artifact is a refusal (AC2)` runs the real gate against the real map tree with the symbol population emptied, and asserts the refusal names the tier, the artifact and the regen command. Observed RED against the pre-fix spelling, which returned `None` — a silent pass over a committed `symbols.json` nothing on the bar reproduces
- AC3 — `tools/codebase-map/test_codebase_map.py` header — states four things it does not check: it never reads code, so a feature no extractor enumerates is invisible; it checks dossier headings and claimed keys, never whether the prose is true; freshness is a byte compare of the artifacts THIS gate lists, so an artifact `gen_map.py` writes and it does not list is uncompared (which is `TOOL-dTracedLattice-4`); and a conditional tier that compares nothing says so, which is not a verdict about the tree
- AC4 — `python3 tools/codebase-map/selftest.py` — same arm as AC1, and this is the half that could not be graded any other way: `symbols.json` is the only conditional tier today, so an enumeration criterion would grade a population of one. The arm appends a SECOND tier to `CONDITIONAL_TIERS` in a fixture and asserts it is reported with no reporting line written for it. The list IS the mechanism
- AC5 — `python3 tools/codebase-map/selftest.py` — the arm `gate and template are byte-identical (AC5)` byte-compares the pair. Observed RED by appending one comment line to the template: `13862 vs 13883 bytes`. Both files carry every edit in this unit
- S1/S3 — `tools/codebase-map/test_codebase_map.py` `CONDITIONAL_TIERS` — the class fix, not the instance: every conditional tier is a row in one list and the reporter walks that list, so a tier cannot be absent from the output by being absent from the map

## One design change the arms forced, and it is an improvement

The skip lines were first printed AFTER the compare loop, on the reasoning that a real staleness
failure should lead. The AC1/AC4 arm then failed for an unrelated reason — the tree was stale from
this build's own new symbols — and the skip line it was asserting had never been reached. That is
the defect one level up: "which tiers did not run" is exactly what a reader needs when something
else is red. The announcement now precedes the compares and the REFUSAL still runs last, because a
refusal is a verdict and an announcement is not.

## What this ledger does not evidence

The gate prints its skip lines to stdout, so a pytest run without `-s` captures them. The leg's own
argv is `python {gate_file}` — the standalone runner — where they are visible. An adopter collecting
this file through pytest sees the refusal (an assertion) but not the skip announcement unless they
pass `-s`; that is a real limit of the chosen carrier and is not fixed here.
