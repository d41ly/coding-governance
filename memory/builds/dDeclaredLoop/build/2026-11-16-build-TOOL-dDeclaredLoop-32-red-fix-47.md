# TOOL-dDeclaredLoop-32 red-fix 47 — harness arms (fail branches armed or pinned) fixed in 1c963fec

**Serves:** red-fix TOOL-dDeclaredLoop-32

- **Leg:** harness arms (fail branches armed or pinned)
- **Red line:** HYGIENE check-arms: tools/unattended/unattended.sh check 37 branch 22 has no POSITIVE assertion naming its own failure text
- **Files:** tools/unattended/unattended.test.sh
- **Commit:** 1c963fec890ecc100d748592bfc42084ec8afecb
- **Rerun:** python3 tools/memory-tree/check-arms.py --check, exit 0
- **Caused-by:** TOOL-dDeclaredLoop-32
