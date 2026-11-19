**Serves:** journal TOOL-dWitnessedBar-17

# TOOL-dWitnessedBar-17 — builder return 2 (run `wf_28fe1f1f-aec`), a divergence, nothing committed

## Why

DIVERGENCE: rev-7 can't pass its own section-7 gate `memory-hygiene self-test`, and every freshly scaffolded adopter goes red on its first run.

1. Fresh-scaffold arming (S4, section 4, section 8 F2, section 7). S4 arms checks 13-15 on any home that is present. Section 4 says the scaffold's comment in `adopt-memory-tree.sh` "names the row shape and no pin", so the scaffold keeps writing `id-orphan-waiver.txt` and `corpus-path-unresolved.txt`. S3 takes the blank `ORPHAN_ID_PIN` and `DEAD_PATH_PIN` out of `.memory-tree.conf.example`, and those blank pins were what kept 13-15 off on a fresh install. So after this unit, every `adopt-memory-tree.sh --scaffold` tree is armed. Its own rendered documents cite paths the tree doesn't hold, so check 15 goes red.
   - I built the change and ran a probe that rebuilds the test suite's `A=$TMP/scaffolded` fixture (conf `MEMORY_ROOT`/`DISCIPLINES`/`FAMILIES`/`READINESS_ROWS`, gov's `--scaffold`, commit). The full hygiene script exited 1 on `HYGIENE check 15: memory/guides/BUILD-METHOD.md:281 cites memory/gotchas, which resolves to nothing`.
   - The kit-staged shape that unit 46's arm builds gave 8 such check-15 reds (TEMPLATE-SPEC.md and BUILD-METHOD.md citing `tools/codebase-map/*`, `tools/gate-legs.json`, `tools/workflows/*`, `memory/gotchas`).
   - That breaks the arm `FAIL a tree built by adopt-memory-tree.sh --scaffold is not hygiene-clean` in `check-memory-hygiene.test.sh`, a leg on section 7's line, and turns every new adopter red.
   - S8 only covers adopters taking an update, by removing a folded pin's home where the pin was blank. Nothing in the spec covers a fresh install.
   - What the spec has to say: either the scaffold stops writing the two homes, so a fresh adopter is off as the blank pins left it (and the section 4 scaffold-comment sentence changes), or it writes them and says what makes the scaffolded tree's own citations pass check 15. Whichever it picks, the fixtures that write both homes empty and expect 13-15 off need to be named in S4's readers with their new expected outcome.

2. A seed that can't run at an adopter (section 4 "The pins", S8, S9). The `dossier-decisions-empty` seed `python {prefix}/codebase-map/test_codebase_map.py --list-empty-decisions` names a file the codebase-map descriptor ships as `project-owned` and keeps out of an adopter's kit dir: `[[files]] include = [..., "test_codebase_map.py"]`, and an adopter's gate lives at `GATE_FILE`. So at every adopter the S8 step's seed exits non-zero, and the step leaves `DOSSIER_DECISIONS_EMPTY_PIN` in the conf, so that adopter never converts. In gov the template and the gate are byte-identical, and `{prefix}/codebase-map/test_codebase_map.template.py` would exist at both. The spec has to name a seed program an adopter actually holds.

Also found, not a spec defect: the `memory hygiene` leg is already red at base a62caf17, in a clean clone. Check 13 reports `PLAY-dOrderedCharter-10` claimed by dOrderedCharter and dWitnessedBar. Check 15 reports `tools/dead-path-waivers.txt` cited from dHonouredPark/BACKLOG.md and dSpentCeiling/BACKLOG.md, and `memory/map/baseline.toml` cited from memory/project/dead-path-waivers.txt:37. The brief says install-prefix is the only known red, so the run's red-leg accounting is off.

## Summary

Nothing is committed. I built the whole unit, found the divergence above with a probe, then put back every product path. The tree is clean at a62caf17 apart from memory/builds/dWitnessedBar/RUN.md, which `--dispatch` staged when I declared `.gitattributes` (a 39/180 draw row and a dispatch row). I left those rows staged so the budget count stays true; the next pass commits them. `--brief` reported the brief already recorded, unchanged.

The full working build is saved for the next builder:
- tracked changes: C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/unit17-wip/tracked.patch (`git apply`)
- new files: C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/unit17-wip/untracked (the four homes and tools/govkit/steps/conf_pins_to_ledger.py)

The patch covers: S9 in all three factory copies, with the `resolve_prefix_token` block inlined into both kit coverage_join.py files; the six memory-tree `[[ledger]]` tables and one codebase-map table; the eight `[[upgrade]]` rows and the step program; `measure-cutoffs` over a conf walk it shares with `measure_scalar_pins`, plus `cutoff-later` and `cutoff-blank` selftest plants; check 20 graded against `row-duplicates` with `--list-duplicates`; corpus_ids `armed(root, conf)` on the homes, the registry read through the factory, `--list-unbound`, and its selftest re-pointed; the hygiene `--list-unbound` print mode, check 21 graded against `unbound-records`, and the check 3 list; test_codebase_map against `dossier-decisions-empty`; the drift RATCHETS rows; the confs and examples; `.gitattributes`; homes seeded at 3, 16, 14 and 39 rows; and the 7 `conf-scalar-pins` rows drained. (DERIVED from the builder's probe)

Not yet done in the patch: re-pointing the RECORD_UNBOUND_PIN and ORPHAN_ID_PIN fixtures in check-memory-hygiene.test.sh, the resolve-python.test.sh arm, the gotchas.py fixture, the docs pages (README, HYGIENE template, WIRE-INTO-PROJECT.md, LEXICON.md, .lexicon.conf, the row-grammar dossier, reuse_lookup, the adopt-memory-tree.sh comments), and the records.

Each probe below stands in, partly, for the gate in brackets; none of them is a gate:
- AC1 conf grep printed nothing and `keys-not-scalar --measure` printed only the two .lexicon.conf rows (`ratchet (keys, not a scalar)`).
- AC4 head line, and corpus_ids `--check` arming 13-15 on empty homes (`corpus-ids selftest`).
- AC5 `seed --population severity-unlabelled` and `live-rows` each printed `unarmed <population> no seed` at exit 0 with no home written (`ratchet (unarmed)`).
- AC7 in a scratch fixture: a cutoff a day later gave `count rose` at exit 1, a day earlier exit 0, blanked `measured 99991231` at exit 1, and never-gains gave `above ceiling` (`ratchet (both ways)`, `ratchet (never gains)`).
- AC8: `measure-cutoffs` printed 39 lines (`ratchet (both ways)`). (DERIVED from the builder's probe)
- AC9: `git check-attr` printed `merge: rows` (`memory hygiene` check 3).
- AC10 in a scratch adopter: RECORD_UNBOUND_PIN up seeded, removed the key and drained its row, witness exited 0, and down restored the conf and conf-scalar-pins bytes exactly. ORPHAN_ID_PIN blank: up removed the key and the home, down restored both. A failed seed refused and left the key (`govkit selftest`).
- check 20 fixtures: keyed, stale, net-to-zero, grown and absent cases each read as expected (`row-grammar selftest`).
- S9: all three factory copies resolved `{prefix}`, so the read-back seeds ran.

Not observed, owed at the close: AC2, AC3 and AC6, every gate on section 7's line, and the RED-first observation of all four `New arm:` lines. No command timed out. No gotchas checklist ran, because nothing was committed. The scratch clones under %TEMP% are removed.
