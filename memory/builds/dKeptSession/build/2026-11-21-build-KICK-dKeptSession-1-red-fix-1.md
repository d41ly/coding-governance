# KICK-dKeptSession-1 red-fix 1 — lexicon naming predicates fixed in b25f851e

**Serves:** red-fix KICK-dKeptSession-1

- **Leg:** lexicon naming predicates
- **Red line:** verb offenders 1220 over pin 1216: tools/policy/check_policy.py defines judge, ok, plant_absent_by_key and plant_accept_all, none a declared verb
- **Files:** memory/map/generated/symbols.json, tools/policy/check_policy.py, tools/run-gates/selftest-budgets.txt
- **Commit:** b25f851e47343378bc869d545e0474a5272ce2f9
- **Rerun:** python tools/lexicon/lexicon.py · exit 0, offenders 1216
- **Caused-by:** KICK-dKeptSession-1
