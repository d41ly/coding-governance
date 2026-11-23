# TOOL-dTotalRecall-9 widen 10 — dead-path-waivers widened

**Serves:** widen TOOL-dTotalRecall-9

- **Population:** dead-path-waivers
- **Keys:** `{prefix}/playbook/memory_index.py	figures = f"MEMORY.md {measured['bytes']} B {side} its {measured['budget']} B budget"`, `{prefix}/playbook/memory_index.py	figures = (f"card {measured['card']} B {card_side} · MEMORY.md {measured['bytes']} B {side} · "`
- **Reason:** unit 9 card figures name MEMORY.md, the harness auto-memory index file the module measures, not a path of this repository; the module's other MEMORY.md lines are waived on the same ground
- **Caused-by:** TOOL-dTotalRecall-9
