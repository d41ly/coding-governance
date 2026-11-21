# TOOL-dPlacedRequest-95 red-fix 50 — shell hygiene (a fork spent on builtin work) fixed in 4ef06c5a

**Serves:** red-fix TOOL-dPlacedRequest-95

- **Leg:** shell hygiene (a fork spent on builtin work)
- **Red line:** tools/hooks/scratch-guard.test.sh carries 6 path-subst and 6 var-pipe sites against rows of 5, and tools/unattended/lib-unattended.sh 7 path-subst against 5
- **Files:** tools/hooks/scratch-guard.test.sh, tools/unattended/lib-unattended.sh
- **Commit:** 4ef06c5ab8896b6e1fa5acd26ba58a55f7dc58c2
- **Rerun:** python3 tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . :!*.test.sh :!memory/
- **Caused-by:** TOOL-dPlacedRequest-95
