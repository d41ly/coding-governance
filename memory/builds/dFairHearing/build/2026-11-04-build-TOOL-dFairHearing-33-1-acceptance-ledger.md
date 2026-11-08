# Acceptance ledger — TOOL-dFairHearing-33

**Serves:** journal TOOL-dFairHearing-33

Built against spec rev-3 at pass commit `479c500ca`. The main loop drafted this ledger at the close from
the builder return of that commit. Each criterion was observed at its parent `d44d3ebce` with `GATE_BASE`
unset, and the commit holds only the spec's status flip and the renders it forces. `constants.py` is the
spec's script byte for byte, written under the pass's scratch directory. The pass before it was refused
at dispatch and committed nothing; its readings at `f24a5052e` were the same. No suite, gate or bar
ran in the pass. The spec's Gates section declares no new arm, and its legs are owed to the close.

**Evidences:** TOOL-dFairHearing-33
- AC1 — `constants.py` — unit 31's probe printed `base 8bec4cefd957d194660a8d7c2916f420b7299074 from origin/main`. Over that base it printed `constants 20`, equal to the descriptor grep's count of 20, printed no `->` line and exited 0. `GATE_BASE` was unset. The build-wide half of the Red when clause is unit 40's, on its ledger's AC1 line
- AC2 — `python constants.py . 7d98741e3~1 7d98741e3` — it printed `check-wiring 1.32 -> 1.33` and `unattended 1.100 -> 1.101` and exited 1. It also printed `absent branch-reconcile`, `absent policy`, `absent roles` and `constants 17`; `absent policy` comes from a kit added after the spec's evidence was taken, and the criterion does not depend on it
- AC3 — `nosuchref` — with it as the base the probe exited 2 naming the ref, and at the pass before it that refusal read `version-constants: nothing compared: nosuchref does not resolve to a commit`. In the one-commit fixture under `%TEMP%/fcr` it exited 2 printing `the kit registry does not load: No module named 'govkit'`, and the fixture was removed. Unit 40's ledger, on its AC11 line, stages the refusals this criterion left unstaged
