# TOOL-dDeclaredLoop-33 red-fix 52 — every held leg is budgeted, every budget row resolves fixed in 422c21e7

**Serves:** red-fix TOOL-dDeclaredLoop-33

- **Leg:** every held leg is budgeted, every budget row resolves
- **Red line:** run-selftests: row 'loop guard fixtures' does not carry the four tab-separated fields the declaration's header names (name, budget, argv, reading), so its reading can run as its argv
- **Files:** tools/run-gates/selftest-budgets.txt
- **Commit:** 422c21e72df02cf06c0289cbe3ccdebf6c157b8a
- **Rerun:** bash tools/run-gates/pass-legs.sh --base 0d65b661c285532278eeb360e13ef46fa2932159
- **Caused-by:** TOOL-dDeclaredLoop-33
