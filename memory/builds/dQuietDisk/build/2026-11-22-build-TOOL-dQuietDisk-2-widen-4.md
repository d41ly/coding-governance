# TOOL-dQuietDisk-2 widen 4 — shell-role widened

**Serves:** widen TOOL-dQuietDisk-2

- **Population:** shell-role
- **Keys:** `tools/unattended/check-pass-order.sh`, `tools/unattended/check-pass-order.test.sh`
- **Reason:** TOOL-dQuietDisk-2: the pass-order leg grades only units whose key moved, which adds its store read, key build and write guard to the leg (627 code lines against the row's 401, PINNED) and the section 7 arm to its suite (796 against 747, PINNED), each measured by the leg's own counter at b24fe84dc
- **Caused-by:** TOOL-dQuietDisk-2
