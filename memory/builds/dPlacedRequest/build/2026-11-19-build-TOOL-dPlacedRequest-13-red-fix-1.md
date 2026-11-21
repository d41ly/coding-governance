# TOOL-dPlacedRequest-13 red-fix 1 — shell hygiene (a loop fed by a command substitution) fixed in 3b92d470

**Serves:** red-fix TOOL-dPlacedRequest-13

- **Leg:** shell hygiene (a loop fed by a command substitution)
- **Red line:** tools/lib/gov-feed.sh: a loop is fed by <<< holding a command substitution, and no registry row declares it (1 site(s))
- **Files:** tools/lib/gov-feed.sh, tools/lib/resolve-python.test.sh, tools/run-gates/post-merge.sh, tools/unattended/unattended.sh, tools/unattended/unattended.test.sh
- **Commit:** 3b92d470a96617ad9d0cb107c8a33eec34f032eb
- **Rerun:** python3 tools/gate-lint/sh_hygiene.py memory/project/substitution-fed-loops.txt
- **Caused-by:** TOOL-dPlacedRequest-13
