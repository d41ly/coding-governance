# TOOL-dPlacedRequest-19 red-fix 38 — core meta-check fixed in 735e6e31

**Serves:** red-fix TOOL-dPlacedRequest-19

- **Leg:** core meta-check
- **Red line:** pending principle row principle.p40 is stale: it is enforced now, armed by dPlacedRequest, so its row in tools/playbook/core-pending.txt is deleted
- **Files:** tools/loop/kit.toml, tools/playbook/core-pending.txt
- **Commit:** 735e6e31ab2d528d1e39f798484e7e72f01d5102
- **Rerun:** python tools/playbook/core.py meta-check
- **Caused-by:** TOOL-dPlacedRequest-19
