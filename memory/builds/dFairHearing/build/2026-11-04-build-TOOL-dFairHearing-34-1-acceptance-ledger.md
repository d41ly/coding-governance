# Acceptance ledger — TOOL-dFairHearing-34

**Serves:** journal TOOL-dFairHearing-34

Built against spec rev-3 at pass commit `f94f3ecb9`, whose parent is `ef46b7428`. The main loop drafted
this ledger at the close from the builder return. `markers.py` is the spec's script, written under the
pass's scratch directory and matched to the spec's block with `diff`, and `GATE_BASE` was unset for every
run. No suite, gate or bar ran in the pass. The spec's Gates section declares no new arm, and its legs
are owed to the close.

**Evidences:** TOOL-dFairHearing-34
- AC1 — `python markers.py . <base>` — unit 31's probe printed `base 8bec4cefd957d194660a8d7c2916f420b7299074 from origin/main`. Over that base it printed `files 96`, equal to git's own `--diff-filter=M` line count of 96, printed no `->` line and exited 0, at `ef46b7428` and again at `f94f3ecb9`. `GATE_BASE` was unset. The build-wide half of the Red when clause is unit 40's, on its ledger's AC1 line
- AC2 — `python markers.py . e7d256af4~1 e7d256af4` — it printed `files 10` and nine `->` lines and exited 1, with `memory/HYGIENE.md memory-tree 2.144 -> 2.145` and `tools/memory-tree/HYGIENE.template.md memory-tree 2.144 -> 2.145` among them
- AC3 — `nosuchref` — with it as the base the probe printed `version-markers: nothing compared: git rev-parse exited 1` to stderr, printed no `files` line and exited 2
