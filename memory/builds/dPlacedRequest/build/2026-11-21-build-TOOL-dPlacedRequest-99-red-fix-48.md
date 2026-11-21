# TOOL-dPlacedRequest-99 red-fix 48 — shell hygiene (a fork spent on builtin work) fixed in b833648b

**Serves:** red-fix TOOL-dPlacedRequest-99

- **Leg:** shell hygiene (a fork spent on builtin work)
- **Red line:** skills/session-kickoff/manifest-check.sh carries 4 pure-fn-subst sites against a row of 2, its suite 9 path-subst, 11 printf-subst and 19 var-pipe against 8, 10 and 15, and tools/run-gates/run-selftests.sh 11 var-pipe against 10
- **Files:** memory/guides/SESSION-KICKOFF.md, skills/session-kickoff/manifest-check.sh, skills/session-kickoff/manifest-check.test.sh, tools/run-gates/run-selftests.sh
- **Commit:** b833648b1cac7a7ad2d451b4d3f84b145e3f7821
- **Rerun:** python3 tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . :!*.test.sh :!memory/
- **Caused-by:** TOOL-dPlacedRequest-99
