# TOOL-dQuietDisk-28 widen 8 — shell-role widened

**Serves:** widen TOOL-dQuietDisk-28

- **Population:** shell-role
- **Keys:** `tools/lib/history-store.sh`, `tools/unattended/lib-unattended.sh`
- **Reason:** TOOL-dQuietDisk-28: init_hs runs the history store's resolve verb once and exports its line as HS_RESOLVED, two code lines in the inline history_store_sh block, so history-store.sh measures 61 code lines against the row's 59 and lib-unattended.sh 1392 against 1390 (PINNED, measured 2026-11-22 by measure_code_lines in the gate-lint kit's sh_hygiene.py)
- **Caused-by:** TOOL-dQuietDisk-28
