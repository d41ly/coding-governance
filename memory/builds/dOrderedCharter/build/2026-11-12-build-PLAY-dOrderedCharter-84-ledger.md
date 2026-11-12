# PLAY-dOrderedCharter-84 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-84

Each line is a probe this pass ran at rev-2 of the spec, over `21740db85` with the pass applied in the worktree.
No leg, suite or bar ran in the pass: each checker the criteria name is the close's, and where a line says
"owed" the main loop observes it after every unit is terminal. The guard probe ran the built `guard.py --staged`
over a scratch fixture repository holding a driver and a run-state record on a branch `run/t`, one scenario at a time.

**Evidences:** PLAY-dOrderedCharter-84
- AC1 — `guard-run-live` — over the guard probe, a record reading `phase: BUILDING` with `run-branch: refs/heads/run/t`, and again with `run-branch: run/t`, each exited 0 printing `policy-guard: admitted · .governance/deploy.toml .governance/instructions.toml · the run-branch of memory/builds/tRun/RUN.md, phase BUILDING` (PINNED, that probe run). The fixture case itself is owed: the main loop runs `--fixture guard-run-live`.
- AC2 — `guard-run-terminal` — over the guard probe, `LANDED` and `ABORTED` each exited 1 with `its phase at HEAD, <PHASE>, is terminal`, and the driver removed in a commit exited 1 with `no unattended driver at HEAD declares PHASES_TERMINAL` (PINNED, that probe run). The fixture case is owed.
- AC3 — `guard-run-other-branch` — over the guard probe, a record naming `run/other`, the HEAD record removed with a live one only staged, and a detached HEAD each exited 1, the first two with `no run-state file at HEAD names run/t as its run-branch` and the third with `HEAD is detached` (PINNED, that probe run). The fixture case is owed.
- AC4 — `live run's branch` — the criterion's `grep -c` over `help/policy.md` and `tools/policy/README.md` reads 2 for each, where the base reads 0 for each (PINNED, over `21740db85` with the pass applied).
- AC6 — `policy-guard: admitted` — owed: the main loop commits this run's deploy-rule hunk on the run branch after the build. A read-only call of the built `check_run_mandate` from this worktree returned `memory/builds/dOrderedCharter/RUN.md, phase BUILDING` (PINNED, at `21740db85`).

**Owed to the close.** Every leg of the spec's Gates section, and the three `New arm:` lines' cases in `tools/policy/check_policy.py`,
observed red at the base and green at the close. One new refusal site carries its own text in an arm: `policy-guard: not a live run's branch · `,
asserted by `guard-run-terminal` and `guard-run-other-branch`.
