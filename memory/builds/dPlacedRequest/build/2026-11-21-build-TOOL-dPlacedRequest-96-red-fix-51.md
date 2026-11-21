# TOOL-dPlacedRequest-96 red-fix 51 — shell hygiene (a fork spent on builtin work) fixed in 19347e1e

**Serves:** red-fix TOOL-dPlacedRequest-96

- **Leg:** shell hygiene (a fork spent on builtin work)
- **Red line:** tools/push-main.test.sh carries 16 cat-file and 16 var-pipe sites against rows of 10 and 15, and tools/unattended/unattended.test.sh 25 printf-subst against 23
- **Files:** tools/push-main.test.sh, tools/unattended/unattended.test.sh
- **Commit:** 19347e1ec6013cbe15173feeb6ff59d9d2ea2c0d
- **Rerun:** python3 tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . :!*.test.sh :!memory/
- **Caused-by:** TOOL-dPlacedRequest-96
