# TOOL-dWitnessedBar-50 red-fix 15 — harness arms (fail branches armed or pinned) fixed in cb93e79f

**Serves:** red-fix TOOL-dWitnessedBar-50

- **Leg:** harness arms (fail branches armed or pinned)
- **Red line:** tools/lib/refuse-wrong-shell.sh: the --coverage break exit, delegated, has no positive assertion and is not pinned
- **Files:** memory/project/unarmed-branches.txt, tools/lib/refuse-wrong-shell.sh
- **Commit:** cb93e79f0d2e825651588e37eda76b4f7f1bd703
- **Rerun:** python tools/memory-tree/check-arms.py --check, exit 0
- **Caused-by:** TOOL-dWitnessedBar-50
