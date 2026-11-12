# PLAY-dOrderedCharter-86 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-86

Each line is a probe this pass ran at rev-1 of the spec, over `9f25dca06` with the pass applied in the worktree.
No leg, suite or bar ran in the pass: each checker the criteria name is the close's, and where a line says
"owed" the main loop observes it after every unit is terminal. The guard probe imported the built `guard.py` and called
`check_run_mandate` inside a scratch fixture repository on a branch `run/t`, holding a run-state record and a driver at
`vendor/gov/run/unattended.sh`, one scenario per commit.

**Evidences:** PLAY-dOrderedCharter-86
- AC1 — `install-prefix (shipped surface)` — a `grep -n` for the kit-segment spelling over the three files the spec names finds only `tools/policy/README.md:221`, which spells it under the drained `<tool-root>/` lead and was not among the base's hits (PINNED, that grep). The counter itself is owed: the main loop runs the leg.
- AC2 — `guard-run-live` — over the guard probe, a record reading `phase: BUILDING` returned the admission `memory/builds/tRun/RUN.md, phase BUILDING`; at the base guard the same probe returned `no unattended driver at HEAD declares PHASES_TERMINAL` (PINNED, that probe run, both guards). The fixture case is owed: the main loop runs `--fixture guard-run-live`.
- AC3 — `guard-run-terminal` — over the guard probe, `LANDED` refused with `its phase at HEAD, LANDED, is terminal` with the driver nested and again with it moved to the fixture's root, and the driver removed in a commit refused with `no unattended driver at HEAD declares PHASES_TERMINAL` (PINNED, that probe run). The fixture case is owed: the main loop runs `--fixture guard-run-terminal`.
- AC4 — `core meta-check` — `read_pending` from `tools/playbook/core.py` over the edited list returned no reds and 146 leg rows, among them the one leg in `tools/gate-legs.json` whose name holds `spec-audit opt-in`, spelled identically (PINNED, that probe run). The meta-check itself is owed: the main loop runs the leg.

**Owed to the close.** Every leg of the spec's Gates section. The spec declares no `New arm:` line and the pass adds no refusal site.
