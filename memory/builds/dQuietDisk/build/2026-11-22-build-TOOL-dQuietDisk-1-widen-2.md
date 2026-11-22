# TOOL-dQuietDisk-1 widen 2 — shell-role widened

**Serves:** widen TOOL-dQuietDisk-1

- **Population:** shell-role
- **Keys:** `tools/lib/history-store.sh`, `tools/lib/resolve-python.test.sh`, `tools/unattended/lib-unattended.sh`
- **Reason:** TOOL-dQuietDisk-1 S12: the history store's bash face, a sourced shim units 2 and 3 consume (59 code lines new, PINNED), and the 2 and 59 lines it adds to resolve-python.test.sh and lib-unattended.sh, PINNED. The rows also absorb the excess the merge b3f5a2bc3 already carried over them, 137 and 12 lines PINNED, inherited from dWitnessedBar's land tip and re-measured at the re-merge onto its landing
- **Caused-by:** TOOL-dQuietDisk-1
