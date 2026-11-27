# TOOL-dTotalRecall-40 red-fix 12 — positional (the citation check alone) fixed in 4763f307

**Serves:** red-fix TOOL-dTotalRecall-40

- **Leg:** positional (the citation check alone)
- **Red line:** record_kinds.py's selftest expectation spelled the fixture plant as a path:line, and unit 40's acceptance ledger quoted it
- **Files:** tools/memory-tree/record_kinds.py
- **Commit:** 4763f3070e7342cebfb5f9fb8850ad5d55afdbe5
- **Rerun:** bash tools/run-gates/pass-legs.sh --base cab28c239b51117e3a9bd294c8148003a220f2fb at the fix commit plus its records
- **Caused-by:** TOOL-dTotalRecall-40
