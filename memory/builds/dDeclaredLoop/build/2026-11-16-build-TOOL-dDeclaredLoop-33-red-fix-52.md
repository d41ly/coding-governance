# TOOL-dDeclaredLoop-33 red-fix 52 — every held leg is budgeted, every budget row resolves fixed in 113dc6d9

**Serves:** red-fix TOOL-dDeclaredLoop-33

- **Leg:** every held leg is budgeted, every budget row resolves
- **Red line:** run-selftests: row 'loop guard fixtures' does not carry the four tab-separated fields the declaration's header names (name, budget, argv, reading), so its reading can run as its argv
- **Files:** tools/run-gates/selftest-budgets.txt
- **Commit:** 113dc6d9ce6603f383b182c0c0f871e8c9842382
- **Rerun:** bash tools/run-gates/pass-legs.sh --base 47fe3685598af10fb5c140e117cffa66daa11e6d
- **Caused-by:** TOOL-dDeclaredLoop-33
