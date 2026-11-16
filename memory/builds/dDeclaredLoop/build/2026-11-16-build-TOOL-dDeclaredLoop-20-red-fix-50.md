# TOOL-dDeclaredLoop-20 red-fix 50 — shell hygiene (a loop fed by a command substitution) fixed in 67d8fb09

**Serves:** red-fix TOOL-dDeclaredLoop-20

- **Leg:** shell hygiene (a loop fed by a command substitution)
- **Red line:** tools/unattended/unattended.sh: the registry declares 2 site(s) at <<< and the scan measures 3
- **Files:** tools/unattended/unattended.sh
- **Commit:** 67d8fb09a547ef0a76836b90599960fc5b266a6f
- **Rerun:** python3 tools/gate-lint/sh_hygiene.py memory/project/substitution-fed-loops.txt, exit 0
- **Caused-by:** TOOL-dDeclaredLoop-20
