# TOOL-dTotalRecall-5 red-fix 10 — install-prefix (shipped surface) fixed in fc5c593c

**Serves:** red-fix TOOL-dTotalRecall-5

- **Leg:** install-prefix (shipped surface)
- **Red line:** id_grammar.py scan_readers spelled the tool root as a quoted path segment in its git ls-files argv
- **Files:** tools/memory-tree/id_grammar.py, tools/playbook/instruction_units.py
- **Commit:** fc5c593c62f9c499949a2929a48e4350b425727b
- **Rerun:** bash tools/run-gates/pass-legs.sh --base e571543c8aecda21e1be18d9cea824977b352d36 at the fix commit plus its records
- **Caused-by:** TOOL-dTotalRecall-5
