# KICK-dKeptSession-80 red-fix 28 — policy check fixed in 8e0a3ba6

**Serves:** red-fix KICK-dKeptSession-80

- **Leg:** policy check
- **Red line:** policy-check: arm_presets, 12 findings, each of the four presets lacks install.baseline, tests.fixture-templates and tests.history-verdicts
- **Files:** tools/policy/presets.toml
- **Commit:** 8e0a3ba6b9581500eda6a7af5c80fdf8ea312dbb
- **Rerun:** python tools/policy/presets.py check · green, 0 findings; check_policy.py keeps two reader-coverage findings origin/main prints too, and its unnamed-keys arm clears with widen-5
- **Caused-by:** KICK-dKeptSession-80
