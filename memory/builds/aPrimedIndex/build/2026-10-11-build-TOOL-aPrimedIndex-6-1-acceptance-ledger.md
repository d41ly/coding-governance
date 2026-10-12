# TOOL-aPrimedIndex-6 — acceptance ledger

**Serves:** journal TOOL-aPrimedIndex-6

No merge bar and no self-test suite ran in this pass. The H49 arm's check and the hook's scrub loop
were each replayed alone. The arm's `check_knob_classes`, `read_hook_const` and `BAR_INERT_KNOBS`
were taken from the pre-push suite by `sed` and run over the current runner, first against the hook
as committed before this pass and then against the built hook. The scrub loop was taken from the
built hook and run with the knob exported. The new bug-class record joined the run-gates dossier's
`gotcha-classes` claims, because the map's coverage gate reads a gotcha file as an inventory key. The
close still owes the pre-push self-test whole.

**Evidences:** TOOL-aPrimedIndex-6
- AC1 — `check_knob_classes` — against the committed hook it printed `unclassified-or-twice GATE_REGEN_CHECK (0)`; against the built hook it printed nothing.
- AC2 — `ENV_CLEARED` — the scrub loop, run with `GATE_REGEN_CHECK=0` exported and a `default` bar class, left the variable unset and printed `cleared=[ GATE_REGEN_CHECK]`.
- AC3 — `python tools/memory-tree/gotchas.py --for-paths tools/run-gates/run-gates.sh` — it selected `a-runner-knob-owes-a-push-class (path)`. After `--write` regenerated the index, `gotchas.py --check` exited 0. A first draft of the record redded check 18 for naming no gate; its Gating section now says what gates it.
