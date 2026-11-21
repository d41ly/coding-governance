# TOOL-dPlacedRequest-19 red-fix 38 — core meta-check fixed in 4c15a05f

**Serves:** red-fix TOOL-dPlacedRequest-19

- **Leg:** core meta-check
- **Red line:** pending principle row principle.p40 is stale: it is enforced now, armed by dPlacedRequest, so its row in tools/playbook/core-pending.txt is deleted
- **Files:** tools/loop/kit.toml, tools/playbook/core-pending.txt
- **Commit:** 4c15a05f947e6f80813cc14fc34af6f8f6a74c98
- **Rerun:** python tools/playbook/core.py meta-check
- **Caused-by:** TOOL-dPlacedRequest-19
