# TOOL-aRepatriatedFork-49 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-49

Written by the unit pass on node a, 2026-09-30. No merge bar and no whole suite ran. The spec's
rev-1 and rev-2 committed before any code. The new pre-push block ran as a SLICE, the suite's
prologue plus that block, in a temp script inside `.githooks/`, removed afterwards. It ran first
over the `ce8a78f5` hook and then over the built one. The fixture runs a copy of the real runner,
because a stub runner reads none of the four knobs. Two neighbouring slices re-ran unchanged
behaviour: the suite's cases 1 to 7 with its prefix section and B1 block passed 24 of 24, and the
run-log suite's AC4, AC7, AC8 and EXITS arms passed through its own `PPRL_ARMS` selector.

**Evidences:** TOOL-aRepatriatedFork-49
- AC1 — `GATE_LEGS` — the slice's push naming an untracked one-leg manifest is refused as `gate-red`, the planted leg's marker is absent, and stderr names `GATE_LEGS`. Red first: on the `ce8a78f5` hook the push exited 0 with `GATE ok    planted` and `gates GREEN — 1/1 legs passed`
- AC2 — `GOV_PYTHON` — the push naming a planted interpreter is refused as `gate-red` and its marker is absent. Red first: on the `ce8a78f5` hook the red python leg printed `GATE ok    red leg` and the push exited 0
- AC3 — `gate-legs.json` — with the manifest untracked and ignored, `git status --porcelain` empty, the push is refused as `bar-refused` naming `gate-legs.json` before the planted leg runs. Red first: on the `ce8a78f5` hook the planted leg ran and the push exited 0
- AC4 — `GATE_REUSE=1` — after a direct green run wrote the ledger row, the push is refused as `gate-red`. Red first: on the `ce8a78f5` hook the runner printed `GATE reuse red leg  (proven green, inputs unchanged)` and the push exited 0
- AC5 — `gate-red` — the control push with nothing planted reaches `red leg` and is refused as `gate-red` on both hooks. The run-log suite's AC4 arm, a STUB bar driving a runner copy under `GOV_GATE_CMD_TEST` with `GATE_LEGS`, passes over the built hook
- AC6 — `GATE_PLANTED` — the class arm classifies all 21 of the runner's `GATE_`/`GOV_` knobs exactly once. A runner copy with `${GATE_PLANTED:-}` appended reds naming it, and a copy with `GATE_LEGS` renamed away reds naming `stale GATE_LEGS`. Red first: on the `ce8a78f5` hook the arm named `GATE_LEGS`, `GATE_REUSE` and `GOV_PYTHON` unclassified, and the stale arm failed
- AC7 — `.githooks/gate-env.sh` — its key list names `GOV_PYTHON` and `<KIT>_PY`, and says each must be exported to reach the bar. The bar mutation self-test, run from a copy beside the hook, passes 28 assertions, and the `  set +f` anchor line occurs once
- AC8 — `git grep -n 'PYTHONPATH' -- .githooks/pre-push` — prints one line of the paragraph after "WHAT THIS DOES NOT CLOSE", which also names `PATH` and `NODE_OPTIONS`
- AC9 — `EXITS` — the run-log suite's EXITS arm passes with `refuse-bar` at five sites. Red first: with the `ce8a78f5` hook and table staged in, it failed `expected [17], got [19]` and named `5 sites, table 3`

No kit version moves: `push-main`, which ships these files, declares none, and `govkit epoch` reads
it as `skip · no declared version`.
