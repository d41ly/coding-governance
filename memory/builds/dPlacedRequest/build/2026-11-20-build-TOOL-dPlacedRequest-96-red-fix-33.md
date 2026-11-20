# TOOL-dPlacedRequest-96 red-fix 33 — shell hygiene (a loop fed by a command substitution) fixed in 2ca295ec

**Serves:** red-fix TOOL-dPlacedRequest-96

- **Leg:** shell hygiene (a loop fed by a command substitution)
- **Red line:** the static arm's membership test is a here-string over a substituted variable inside a loop, a site the registry does not declare
- **Files:** tools/unattended/unattended.test.sh
- **Commit:** 2ca295ec08ce0369b8894088103d44d201c8cbe6
- **Rerun:** python3 tools/gate-lint/sh_hygiene.py memory/project/substitution-fed-loops.txt
- **Caused-by:** TOOL-dPlacedRequest-96
