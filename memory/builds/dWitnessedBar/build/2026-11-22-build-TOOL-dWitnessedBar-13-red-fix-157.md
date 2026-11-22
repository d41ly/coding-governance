# TOOL-dWitnessedBar-13 red-fix 157 — install-prefix (shipped surface) fixed in 2cc967f7

**Serves:** red-fix TOOL-dWitnessedBar-13

- **Leg:** install-prefix (shipped surface)
- **Red line:** tools/lib/legacy_ledger.py and its two copies spell the govkit registry path; section 2o names the govkit and gate-lint kit directories
- **Files:** tools/memory-tree/check-verdict-epoch.sh, tools/memory-tree/legacy_ledger.py
- **Commit:** 2cc967f7b19bf5624c8a6097f7d5e53502ae2c28
- **Rerun:** bash tools/check-install-prefix.sh, exit 0 (the further part split from it at the replay)
- **Caused-by:** TOOL-dWitnessedBar-13
