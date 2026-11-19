# TOOL-dWitnessedBar-13 red-fix 13 — shell hygiene (a loop fed by a command substitution) fixed in 2bd7e6e3

**Serves:** red-fix TOOL-dWitnessedBar-13

- **Leg:** shell hygiene (a loop fed by a command substitution)
- **Red line:** tools/lib/resolve-python.test.sh: the registry declares 1 site at here-string and the scan measures 2
- **Files:** tools/gate-lint/legacy_ledger.py, tools/lib/legacy_ledger.py, tools/lib/resolve-python.test.sh, tools/memory-tree/check-verdict-epoch.sh, tools/memory-tree/legacy_ledger.py
- **Commit:** 2bd7e6e36d98341e55a996ef30dbe0b5b5f12676
- **Rerun:** python tools/gate-lint/sh_hygiene.py memory/project/substitution-fed-loops.txt, exit 0
- **Caused-by:** TOOL-dWitnessedBar-13
