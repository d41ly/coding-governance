# TOOL-dQuietDisk-13 widen 10 — shell-role widened

**Serves:** widen TOOL-dQuietDisk-13

- **Population:** shell-role
- **Keys:** `tools/run-gates/run-gates.turnstile.test.sh`, `tools/lib/template-cache.sh`, `tools/lib/lib-selftest.sh`
- **Reason:** TOOL-dQuietDisk-13: the turnstile suite clones its two fixture shapes from the template cache, and read_template_mode joins the template_cache_sh block in both carriers
- **Caused-by:** TOOL-dQuietDisk-13
