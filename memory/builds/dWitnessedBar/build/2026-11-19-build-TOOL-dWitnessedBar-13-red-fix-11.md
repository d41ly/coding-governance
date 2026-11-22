# TOOL-dWitnessedBar-13 red-fix 11 — install-prefix (shipped surface) fixed in 15710a90

**Serves:** red-fix TOOL-dWitnessedBar-13

- **Leg:** install-prefix (shipped surface)
- **Red line:** tools/lib/legacy_ledger.py and its two copies spell the govkit registry path; section 2o names the govkit and gate-lint kit directories
- **Files:** tools/gate-lint/legacy_ledger.py, tools/lib/legacy_ledger.py, tools/lib/resolve-python.test.sh
- **Commit:** 15710a90a6ffc23f75f759cc03ac8d2f54484874
- **Rerun:** bash tools/check-install-prefix.sh, exit 0
- **Caused-by:** TOOL-dWitnessedBar-13
