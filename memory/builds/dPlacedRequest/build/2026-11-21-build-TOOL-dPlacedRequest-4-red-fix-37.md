# TOOL-dPlacedRequest-4 red-fix 37 — layer dependencies (the core never depends on an expansion) fixed in 735e6e31

**Serves:** red-fix TOOL-dPlacedRequest-4

- **Leg:** layer dependencies (the core never depends on an expansion)
- **Red line:** tools/loop/placement.py's render_capped_value imports the runlog kit's render_redacted, a probe and an import edge from core kit loop to non-core kit runlog, and no optional row of the loop descriptor named the file
- **Files:** tools/loop/kit.toml, tools/playbook/core-pending.txt
- **Commit:** 735e6e31ab2d528d1e39f798484e7e72f01d5102
- **Rerun:** python tools/playbook/check_layers.py
- **Caused-by:** TOOL-dPlacedRequest-4
