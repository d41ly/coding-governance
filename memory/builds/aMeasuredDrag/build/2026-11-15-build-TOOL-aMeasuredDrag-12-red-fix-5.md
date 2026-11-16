# TOOL-aMeasuredDrag-12 red-fix 5 — shell hygiene (a fork spent on builtin work) fixed in eefb596b

**Serves:** red-fix TOOL-aMeasuredDrag-12

- **Leg:** shell hygiene (a fork spent on builtin work)
- **Red line:** sh-hygiene: 4 finding(s) — the scan measures one var-pipe site over the registry in .githooks/pre-commit.test.sh, and one printf-subst, one path-subst and two cat-file sites over it in tools/run-gates/run-gates.test.sh
- **Files:** .githooks/pre-commit.test.sh, tools/run-gates/run-gates.test.sh
- **Commit:** eefb596b49c66b31c6cb9217b1c7068d07b5b0b0
- **Rerun:** sh_hygiene.py --spawn-idioms · OK · 2196 registered site(s) in 296 row(s) match the scan
- **Caused-by:** TOOL-aMeasuredDrag-12
