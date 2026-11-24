# KICK-dKeptSession-80 red-fix 31 — policy fixtures fixed in dcc7e30f

**Serves:** red-fix KICK-dKeptSession-80

- **Leg:** policy fixtures
- **Red line:** policy-fixture: guard-trace, WRONG tools/playbook/layers.toml, runlog.py and prose.py, not under the policy fixtures guard
- **Files:** memory/guides/SESSION-KICKOFF.md, tools/gate-legs.json, tools/govkit/registry.toml
- **Commit:** dcc7e30f8173b407ce8aa82ef5805f424534a4f3
- **Rerun:** check_policy.py --fixture fixtures-guard-census and presets-core-only, each 0 wrong
- **Caused-by:** KICK-dKeptSession-80
