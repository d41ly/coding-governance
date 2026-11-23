# TOOL-dBoundRoles-42 widen 8 — dead-path-waivers widened

**Serves:** widen TOOL-dBoundRoles-42

- **Population:** dead-path-waivers
- **Keys:** `{prefix}/hooks/kit.toml	surfaces = ["installable:{prefix}/hooks/agent-cap.js", "file:{prefix}/hooks/agent-cap.js"]`, `{prefix}/govkit/steps/spawn_guard_pack.py	OLD_MARKER = "agent-cap.js"`
- **Reason:** the upgrade step names the file it retires
- **Caused-by:** TOOL-dBoundRoles-42
