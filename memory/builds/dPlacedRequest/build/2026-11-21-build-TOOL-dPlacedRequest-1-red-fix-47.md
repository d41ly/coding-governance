# TOOL-dPlacedRequest-1 red-fix 47 — shell hygiene (a fork spent on builtin work) fixed in b041ab69

**Serves:** red-fix TOOL-dPlacedRequest-1

- **Leg:** shell hygiene (a fork spent on builtin work)
- **Red line:** tools/unattended/unattended.sh carries 7 cat-file, 14 path-subst, 14 printf-subst and 47 pure-fn-subst sites against registry rows of 6, 13, 8 and 44
- **Files:** tools/unattended/unattended.sh
- **Commit:** b041ab694a8245bae3b79ccefa95b4290fdb23ae
- **Rerun:** python3 tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . :!*.test.sh :!memory/
- **Caused-by:** TOOL-dPlacedRequest-1
