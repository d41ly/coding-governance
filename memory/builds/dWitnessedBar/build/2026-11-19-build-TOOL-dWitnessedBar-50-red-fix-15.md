# TOOL-dWitnessedBar-50 red-fix 15 — harness arms (fail branches armed or pinned) fixed in 3b4c5ba9

**Serves:** red-fix TOOL-dWitnessedBar-50

- **Leg:** harness arms (fail branches armed or pinned)
- **Red line:** tools/lib/refuse-wrong-shell.sh: the --coverage break exit, delegated, has no positive assertion and is not pinned
- **Files:** memory/project/unarmed-branches.txt, tools/lib/refuse-wrong-shell.sh
- **Commit:** 3b4c5ba9ca08aa3a863373b4c3691759475594ed
- **Rerun:** python tools/memory-tree/check-arms.py --check, exit 0
- **Caused-by:** TOOL-dWitnessedBar-50
