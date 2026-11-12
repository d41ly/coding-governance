# PLAY-dOrderedCharter-10 deviation 104 — the playbook render selftest's guard names the memory-tree modules unit 19 loads, and the lexicon

**Serves:** deviation PLAY-dOrderedCharter-10

- **Departs from:** `PLAY-dOrderedCharter-10@rev-4 [§4 Files touched]`
- **Hand-off:** spec-to-code
- **Before:** the `playbook render selftest` leg's guard in `tools/gate-legs.json` names `{prefix}/playbook/` and three memory-tree files, and neither `{prefix}/memory-tree/id_grammar.py` nor `{prefix}/memory-tree/coverage_join.py`, which `gov_tag.py` loads since PLAY-dOrderedCharter-19's pass; §4 "### Files touched" names no `gate-legs.json`.
- **After:** the guard also names `{prefix}/memory-tree/id_grammar.py`, `{prefix}/memory-tree/coverage_join.py` and `{prefix}/lexicon/`, the kit this unit's name-check slot calls from every plant, and the kickoff manifest's `last-audit` is re-stamped in the same commit.
- **Cause:** builder discovery
- **Reason:** a held suite whose guard misses a module its subject loads stays green through an edit that breaks it (class held-suite-guard-misses-a-sibling-kit); unit 19's builder return names the gap and this unit's brief owes the fix.
- **Evidence:** `memory/builds/dOrderedCharter/build/2026-11-03-build-PLAY-dOrderedCharter-19-4-builder-return.md:19`; `tools/playbook/tag_index.py`'s `load_memory_tree` imports `id_grammar`, and `check_namespace_joins` and `gov_tag.py`'s `run_check` import `coverage_join`; `run_name_check` runs the lexicon kit's `lexicon.py --tags` on every `check` a plant runs.
- **Risk:** stricter
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `report` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-19
