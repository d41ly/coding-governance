# TOOL-dDeclaredLoop-32 red-fix 47 — harness arms (fail branches armed or pinned) fixed in 192a4bb4

**Serves:** red-fix TOOL-dDeclaredLoop-32

- **Leg:** harness arms (fail branches armed or pinned)
- **Red line:** HYGIENE check-arms: tools/unattended/unattended.sh check 37 branch 22 has no POSITIVE assertion naming its own failure text
- **Files:** tools/unattended/unattended.test.sh
- **Commit:** 192a4bb4ca6319f43c1434c9cd86754696563955
- **Rerun:** python3 tools/memory-tree/check-arms.py --check, exit 0
- **Caused-by:** TOOL-dDeclaredLoop-32
