# TOOL-dWitnessedBar-108 widen 38 — unread-params widened

**Serves:** widen TOOL-dWitnessedBar-108

- **Population:** unread-params
- **Keys:** `tools/loop/claim.py	read_claim_lines	root`, `tools/loop/loop_lib.py	read_builds_dir	kit_dir`
- **Reason:** origin's loop kit, landed since this run's base, came under this build's python-reads params arm at the landing merge; each function keeps a parameter its body never reads, the arm's tolerated shape
- **Caused-by:** TOOL-dWitnessedBar-108
