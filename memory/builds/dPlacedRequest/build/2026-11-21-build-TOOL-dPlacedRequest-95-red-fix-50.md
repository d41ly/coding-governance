# TOOL-dPlacedRequest-95 red-fix 50 — shell hygiene (a fork spent on builtin work) fixed in dc8e55f8

**Serves:** red-fix TOOL-dPlacedRequest-95

- **Leg:** shell hygiene (a fork spent on builtin work)
- **Red line:** tools/hooks/scratch-guard.test.sh carries 6 path-subst and 6 var-pipe sites against rows of 5, and tools/unattended/lib-unattended.sh 7 path-subst against 5
- **Files:** tools/hooks/scratch-guard.test.sh, tools/unattended/lib-unattended.sh
- **Commit:** dc8e55f87d55d02c65cf8f728cc4681220f41268
- **Rerun:** python3 tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . :!*.test.sh :!memory/
- **Caused-by:** TOOL-dPlacedRequest-95
