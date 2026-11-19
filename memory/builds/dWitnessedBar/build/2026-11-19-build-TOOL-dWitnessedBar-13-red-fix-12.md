# TOOL-dWitnessedBar-13 red-fix 12 — verdict epoch (kit version dates the engine) fixed in 2bd7e6e3

**Serves:** red-fix TOOL-dWitnessedBar-13

- **Leg:** verdict epoch (kit version dates the engine)
- **Red line:** legacy_ledger.py and coverage_join.py are imported by merge-rows.py and not in DELEGATES
- **Files:** tools/gate-lint/legacy_ledger.py, tools/lib/legacy_ledger.py, tools/lib/resolve-python.test.sh, tools/memory-tree/check-verdict-epoch.sh, tools/memory-tree/legacy_ledger.py
- **Commit:** 2bd7e6e36d98341e55a996ef30dbe0b5b5f12676
- **Rerun:** bash tools/memory-tree/check-verdict-epoch.sh, exit 0
- **Caused-by:** TOOL-dWitnessedBar-13
