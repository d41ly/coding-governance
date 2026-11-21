# TOOL-dPlacedRequest-13 red-fix 1 — shell hygiene (a loop fed by a command substitution) fixed in 01d33237

**Serves:** red-fix TOOL-dPlacedRequest-13

- **Leg:** shell hygiene (a loop fed by a command substitution)
- **Red line:** tools/lib/gov-feed.sh: a loop is fed by <<< holding a command substitution, and no registry row declares it (1 site(s))
- **Files:** tools/lib/gov-feed.sh, tools/run-gates/post-merge.sh, tools/unattended/unattended.sh
- **Commit:** 01d332378f7e8a489b4ba348c629ffe48ba9d4d4
- **Rerun:** python3 tools/gate-lint/sh_hygiene.py memory/project/substitution-fed-loops.txt
- **Caused-by:** TOOL-dPlacedRequest-13
