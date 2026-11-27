# TOOL-dTotalRecall-5 red-fix 9 — writing practice (records and units) fixed in fc5c593c

**Serves:** red-fix TOOL-dTotalRecall-5

- **Leg:** writing practice (records and units)
- **Red line:** read_populations raised the same AttributeError through instruction_units.read_document_registry
- **Files:** tools/memory-tree/id_grammar.py, tools/playbook/instruction_units.py
- **Commit:** fc5c593c62f9c499949a2929a48e4350b425727b
- **Rerun:** bash tools/run-gates/pass-legs.sh --base e571543c8aecda21e1be18d9cea824977b352d36 at the fix commit plus its records; the leg then reads the spec's unpinned facts, a spec fix owed through the writer
- **Caused-by:** TOOL-dTotalRecall-5
