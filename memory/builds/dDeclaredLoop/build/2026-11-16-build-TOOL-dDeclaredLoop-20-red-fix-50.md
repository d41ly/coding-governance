# TOOL-dDeclaredLoop-20 red-fix 50 — shell hygiene (a loop fed by a command substitution) fixed in 272d7a40

**Serves:** red-fix TOOL-dDeclaredLoop-20

- **Leg:** shell hygiene (a loop fed by a command substitution)
- **Red line:** tools/unattended/unattended.sh: the registry declares 2 site(s) at <<< and the scan measures 3
- **Files:** tools/unattended/unattended.sh
- **Commit:** 272d7a4016b6fc6532f112e484de1abaade127f1
- **Rerun:** python3 tools/gate-lint/sh_hygiene.py memory/project/substitution-fed-loops.txt, exit 0
- **Caused-by:** TOOL-dDeclaredLoop-20
