# TOOL-dQuietDisk-7 widen 7 — shell-role widened

**Serves:** widen TOOL-dQuietDisk-7

- **Population:** shell-role
- **Keys:** `tools/lib/template-cache.sh`, `tools/lib/lib-selftest.sh`, `tools/lib/lib-selftest.test.sh`, `tools/lib/resolve-python.test.sh`
- **Reason:** TOOL-dQuietDisk-7: the suite template cache's bash face, which adds template-cache.sh (64 code lines, a new row, PINNED), its inline template_cache_sh block with build_fixture --template, arm_reading and the read-checkout check to lib-selftest.sh (243 code lines against the row's 126, PINNED), the template mode's arms to lib-selftest.test.sh (221 against 115, PINNED) and the template_cache_sh parity row to resolve-python.test.sh (1560 against 1559, PINNED), each measured by measure_code_lines in the gate-lint kit's sh_hygiene.py
- **Caused-by:** TOOL-dQuietDisk-7
