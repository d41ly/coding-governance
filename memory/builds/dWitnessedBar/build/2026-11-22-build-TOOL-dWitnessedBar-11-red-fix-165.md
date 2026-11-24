# TOOL-dWitnessedBar-11 red-fix 165 — layer dependencies (the core never depends on an expansion) fixed in da27f0ae

**Serves:** red-fix TOOL-dWitnessedBar-11

- **Leg:** layer dependencies (the core never depends on an expansion)
- **Red line:** layers: seven files of three core kits keep an edge to a non-core kit that no optional row of their descriptors names
- **Files:** tools/memory-tree/kit.toml, tools/playbook/kit.toml, tools/run-gates/kit.toml
- **Commit:** da27f0ae536798176a5efda80ed7c58d700d207c
- **Rerun:** python tools/playbook/check_layers.py: 59 allowed, 0 red, 0 contract reds
- **Caused-by:** TOOL-dWitnessedBar-11
