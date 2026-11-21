# TOOL-dPlacedRequest-4 red-fix 37 — layer dependencies (the core never depends on an expansion) fixed in 4c15a05f

**Serves:** red-fix TOOL-dPlacedRequest-4

- **Leg:** layer dependencies (the core never depends on an expansion)
- **Red line:** tools/loop/placement.py's render_capped_value imports the runlog kit's render_redacted, a probe and an import edge from core kit loop to non-core kit runlog, and no optional row of the loop descriptor named the file
- **Files:** tools/loop/kit.toml, tools/playbook/core-pending.txt
- **Commit:** 4c15a05f947e6f80813cc14fc34af6f8f6a74c98
- **Rerun:** python tools/playbook/check_layers.py
- **Caused-by:** TOOL-dPlacedRequest-4
