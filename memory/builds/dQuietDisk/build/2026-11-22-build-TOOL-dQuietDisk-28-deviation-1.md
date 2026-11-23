# TOOL-dQuietDisk-28 deviation 1 — the two widened rows carry the measured count, set after the door wrote them

**Serves:** deviation TOOL-dQuietDisk-28

- **Departs from:** `TOOL-dQuietDisk-28@rev-1` [S8]
- **Hand-off:** spec-to-code
- **Before:** S8 has every code line S5 adds widened through `ratchet.py widen shell-role`, and says no row is edited by hand.
- **After:** the door ran once, wrote `2026-11-22-build-TOOL-dQuietDisk-28-widen-8` and rewrote both rows with HEAD's sha and `widened:2026-11-22-build-TOOL-dQuietDisk-28-widen-8`, each count raised by one, 59 to 60 and 1390 to 1391. The pass then set the two counts to the measured 61 and 1392, and changed nothing else in either row or in any other row.
- **Cause:** builder discovery
- **Reason:** `tools/memory-tree/ratchet.py#run_widen` raises each key's count by exactly one per call, and S5 adds two code lines to each file. A second call would write a second widen record for the same change. The brief tells the pass to widen through the door and then set each row to the measured code lines, and unit 7's pass did the same, its rows rising 126 to 243 and 115 to 221 under the one record `2026-11-22-build-TOOL-dQuietDisk-7-widen-7` (PINNED, `git log -p -- memory/project/shell-role.txt` at `360d706f6`).
- **Evidence:** `python tools/gate-lint/sh_hygiene.py --shell-role --measure . ":!memory/"` printed 61 for `tools/lib/history-store.sh` and 1392 for `tools/unattended/lib-unattended.sh` after the edit, and `git diff -- memory/project/shell-role.txt` changes those two rows only (PINNED, both run in this pass).
- **Risk:** additive
- **Approver:** author, the builder pass, under the chain's `author-recorded` value
- **Follow-through:** report
- **Caused-by:** TOOL-dQuietDisk-28
