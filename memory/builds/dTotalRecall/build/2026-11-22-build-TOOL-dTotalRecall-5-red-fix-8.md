# TOOL-dTotalRecall-5 red-fix 8 — playbook render wiring fixed in fc5c593c

**Serves:** red-fix TOOL-dTotalRecall-5

- **Leg:** playbook render wiring
- **Red line:** read_document_registry raised AttributeError: a leftover HOLD_RE = None rebound the pattern load_slug_patterns had bound
- **Files:** tools/memory-tree/id_grammar.py, tools/playbook/instruction_units.py
- **Commit:** fc5c593c62f9c499949a2929a48e4350b425727b
- **Rerun:** bash tools/run-gates/pass-legs.sh --base e571543c8aecda21e1be18d9cea824977b352d36 at the fix commit plus its records
- **Caused-by:** TOOL-dTotalRecall-5
