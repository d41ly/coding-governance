# TOOL-dTotalRecall-13 red-fix 7 — install-prefix (shipped surface) fixed in 3b9d71f7

**Serves:** red-fix TOOL-dTotalRecall-13

- **Leg:** install-prefix (shipped surface)
- **Red line:** tools/codebase-map/selftest.py spelled the lexicon kit's path in its fixture's no-lexicon assertion
- **Files:** tools/codebase-map/map_lib.py, tools/codebase-map/selftest.py
- **Commit:** 3b9d71f755ee2cf10861f0242bb7df0482bd8c4d
- **Rerun:** bash tools/run-gates/pass-legs.sh --base a3d6d07edf5de2e4c9f1adffbea12d3c3205f143 at the fix commit plus its records
- **Caused-by:** TOOL-dTotalRecall-13
