# TOOL-dWitnessedBar-108 red-fix 164 — python reads (a name never bound, an import outside its guard) fixed in 040e261d

**Serves:** red-fix TOOL-dWitnessedBar-108

- **Leg:** python reads (a name never bound, an import outside its guard)
- **Red line:** py-reads: five legs import memory-tree modules their guards do not name, so an edit to those modules never selects them
- **Files:** memory/guides/SESSION-KICKOFF.md, tools/codebase-map/kit.toml, tools/gate-legs.json, tools/govkit/registry.toml
- **Commit:** 040e261d123d8aace09c0de61821dd693209af7d
- **Rerun:** python tools/run-gates/py_reads.py: rc 0, no guard or params red
- **Caused-by:** TOOL-dWitnessedBar-108
