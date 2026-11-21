# TOOL-dWitnessedBar-17 red-fix 156 — memory hygiene fixed in 882701e5

**Serves:** red-fix TOOL-dWitnessedBar-17

- **Leg:** memory hygiene
- **Red line:** corpus_ids check 13 read a TOML comment inside a spec's fenced block as an H1 claiming another build's id, and check 15 found two asks citing the dead-path waiver list at its pre-move home with no registry row
- **Files:** memory/project/corpus-path-unresolved.txt, tools/memory-tree/corpus_ids.py
- **Commit:** 882701e5d66d1ae8a7ed341d1a23e0b74991148e
- **Rerun:** python tools/memory-tree/corpus_ids.py --check: no check 13 to 15 line; --selftest: the fenced near miss passes, and fails with the fence test removed; check 25 is owed to the spec writer
- **Caused-by:** TOOL-dWitnessedBar-17
