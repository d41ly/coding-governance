# TOOL-dWitnessedBar-1 widen 34 — fork-ceilings widened

**Serves:** widen TOOL-dWitnessedBar-1

- **Population:** fork-ceilings
- **Keys:** `check-unattended	5.3	709	git init -q . && git config user.email t@t.test && git config user.name t && git config core.autocrlf false && cp "$ROOT/.unattended.conf" "$ROOT/.memory-tree.conf" . && mkdir -p memory/builds && git add -A && git commit -q -m seed	bash "$ROOT/tools/unattended/check-unattended.sh"`, `run-gates-1leg	5.3	72	git init -q . && git config user.email t@t.test && git config user.name t && git config core.autocrlf false && printf '%s\n' '[{"name":"one","argv":["bash","-c","exit 0"],"ceiling":60}]' > legs.json && git add -A && git commit -q -m seed	GATE_TURNSTILE=0 GATE_JOBS=1 GATE_LEGS="$SCRATCH/legs.json" bash "$ROOT/tools/run-gates/run-gates.sh"`, `run-gates-2leg	5.3	97	git init -q . && git config user.email t@t.test && git config user.name t && git config core.autocrlf false && printf '%s\n' '[{"name":"one","argv":["bash","-c","exit 0"],"ceiling":60},{"name":"two","argv":["bash","-c","exit 0"],"ceiling":60}]' > legs.json && git add -A && git commit -q -m seed	GATE_TURNSTILE=0 GATE_JOBS=1 GATE_LEGS="$SCRATCH/legs.json" bash "$ROOT/tools/run-gates/run-gates.sh"`
- **Reason:** the landing merge over origin/main c2a407b03 joined origin's new forks in check-unattended.sh and run-gates.sh with this branch's, each side having fit its own ceiling; the three rows rise to the counts fork-count.sh measures at the merge, +3, +2 and +2
- **Caused-by:** TOOL-dWitnessedBar-1
