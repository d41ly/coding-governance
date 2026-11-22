# TOOL-dWitnessedBar-13 red-fix 12 — verdict epoch (kit version dates the engine) fixed in 15710a90

**Serves:** red-fix TOOL-dWitnessedBar-13

- **Leg:** verdict epoch (kit version dates the engine)
- **Red line:** legacy_ledger.py and coverage_join.py are imported by merge-rows.py and not in DELEGATES
- **Files:** tools/gate-lint/legacy_ledger.py, tools/lib/legacy_ledger.py, tools/lib/resolve-python.test.sh
- **Commit:** 15710a90a6ffc23f75f759cc03ac8d2f54484874
- **Rerun:** bash tools/memory-tree/check-verdict-epoch.sh, exit 0
- **Caused-by:** TOOL-dWitnessedBar-13
