# TOOL-dWitnessedBar-11 red-fix 154 — core meta-check fixed in d1260fdd

**Serves:** red-fix TOOL-dWitnessedBar-11

- **Leg:** core meta-check
- **Red line:** core: red · pending leg row shell hygiene (a stage committed with no staged-diff test) is stale: it is enforced now, so delete the row (armed by dWitnessedBar)
- **Files:** tools/playbook/core-pending.txt
- **Commit:** d1260fdd56f4b5968c2a1cdcb7e64c469dd8228c
- **Rerun:** python tools/playbook/core.py meta-check: green, 42 principles, 224 legs, 17 kinds
- **Caused-by:** TOOL-dWitnessedBar-11
