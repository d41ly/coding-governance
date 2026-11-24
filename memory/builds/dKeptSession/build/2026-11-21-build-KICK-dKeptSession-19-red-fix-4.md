# KICK-dKeptSession-19 red-fix 4 — lexicon naming predicates fixed in 265db5b9

**Serves:** red-fix KICK-dKeptSession-19

- **Leg:** lexicon naming predicates
- **Red line:** verb offenders 1217 over pin 1216: tools/policy/check_policy.py defines judge, not a declared verb
- **Files:** tools/policy/check_policy.py
- **Commit:** 265db5b9ce61427063c178e0776f1658d6d65038
- **Rerun:** python tools/lexicon/lexicon.py · exit 0, offenders 1216
- **Caused-by:** KICK-dKeptSession-19
