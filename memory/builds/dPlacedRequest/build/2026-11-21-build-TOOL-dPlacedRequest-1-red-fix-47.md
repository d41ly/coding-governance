# TOOL-dPlacedRequest-1 red-fix 47 — shell hygiene (a fork spent on builtin work) fixed in 64d5d5bb

**Serves:** red-fix TOOL-dPlacedRequest-1

- **Leg:** shell hygiene (a fork spent on builtin work)
- **Red line:** tools/unattended/unattended.sh carries 7 cat-file, 14 path-subst, 14 printf-subst and 47 pure-fn-subst sites against registry rows of 6, 13, 8 and 44
- **Files:** tools/unattended/unattended.sh
- **Commit:** 64d5d5bbfb2dda5afbfdb24f839577084928134e
- **Rerun:** python3 tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . :!*.test.sh :!memory/
- **Caused-by:** TOOL-dPlacedRequest-1
