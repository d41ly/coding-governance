# TOOL-dWitnessedBar-13 red-fix 11 — install-prefix (shipped surface) fixed in 2bd7e6e3

**Serves:** red-fix TOOL-dWitnessedBar-13

- **Leg:** install-prefix (shipped surface)
- **Red line:** tools/lib/legacy_ledger.py and its two copies spell the govkit registry path; section 2o names the govkit and gate-lint kit directories
- **Files:** tools/gate-lint/legacy_ledger.py, tools/lib/legacy_ledger.py, tools/lib/resolve-python.test.sh, tools/memory-tree/check-verdict-epoch.sh, tools/memory-tree/legacy_ledger.py
- **Commit:** 2bd7e6e36d98341e55a996ef30dbe0b5b5f12676
- **Rerun:** bash tools/check-install-prefix.sh, exit 0
- **Caused-by:** TOOL-dWitnessedBar-13
