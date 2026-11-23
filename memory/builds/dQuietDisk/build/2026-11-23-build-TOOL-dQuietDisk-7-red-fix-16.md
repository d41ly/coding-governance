# TOOL-dQuietDisk-7 red-fix 16 — selftest harness self-test fixed in 60229490

**Serves:** red-fix TOOL-dQuietDisk-7

- **Leg:** selftest harness self-test
- **Red line:** FAIL  a reading arm wrote into the read checkout .../read — a reader: hint: Support for <GIT_DIR>/info/grafts is deprecated
- **Files:** tools/lib/lib-selftest.sh
- **Commit:** 602294909f9ab82c115437af61b2d8989a155234
- **Rerun:** GIT_GRAFT_FILE=/dev/null bash tools/lib/lib-selftest.test.sh: PASS (38 assertions), red before the fix; and without the neutralizer: PASS (38 assertions)
- **Caused-by:** TOOL-dQuietDisk-7
