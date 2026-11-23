# TOOL-dQuietDisk-9 widen 15 — shell-role widened

**Serves:** widen TOOL-dQuietDisk-9

- **Population:** shell-role
- **Keys:** `tools/run-gates/run-gates.sh`, `tools/run-gates/run-selftests.sh`, `tools/lib/owned-scratch.sh`
- **Reason:** TOOL-dQuietDisk-9: both runners carry the owned_work_sh block, and run-selftests.sh also health_log_sh, derive_temp_path, ts_alive and one owned startup root (run-gates.sh 3779 against 3770, run-selftests.sh 1630 against 1542), and tools/lib/owned-scratch.sh is the block's new canonical file (39), measured by sh_hygiene.py#measure_code_lines at 525d33285
- **Caused-by:** TOOL-dQuietDisk-9
