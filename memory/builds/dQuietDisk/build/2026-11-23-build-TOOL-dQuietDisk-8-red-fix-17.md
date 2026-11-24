# TOOL-dQuietDisk-8 red-fix 17 — loop factories fixtures fixed in 8dbcc358

**Serves:** red-fix TOOL-dQuietDisk-8

- **Leg:** loop factories fixtures
- **Red line:** factories: selftest · FAIL workflow-new · loop: refused · the list row DOD_CORE parked-decisions-surfaced names the build dShippedRelease, which has no .../memory/builds/dShippedRelease/README.md
- **Files:** tools/policy/check_policy.py
- **Commit:** 8dbcc3586c259fbcd9f1c0137d4fd13c82f5f30f
- **Rerun:** python tools/loop/factories.py --selftest: PASS 16 cases (origin/main PASS, HEAD before the fix FAIL workflow-new); check_policy.py --fixture: 1096 assertions, 2 wrong, the two origin/main reads (budgets-cap-role-body, guard-trace), against 3 before the fix
- **Caused-by:** TOOL-dQuietDisk-8
