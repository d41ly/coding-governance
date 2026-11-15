# TOOL-dDeclaredLoop-46 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-46

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on node
`d` (win32), at rev-5 of the spec, by probes of the unit's own code: greps over the carriers, a
`python -c` import of the floor, a `tomllib` join of every descriptor table to its manifest row, the
floor reader called in process, a `govkit.py apply --kits push-main` into a scratch manifest-kind
target holding no run-gates, and a probe of origin/main read through `git show` after `git fetch
origin`. `selfcheck --fix` ran once, as S1's carrier writer; the scratch-guard hook refused a plain
`selfcheck`, so its exit is owed to the close.

Owed to the close: every leg the spec's section 7 names, `govkit selfcheck` and `govkit selftest`
among them, AC4's scratch-copy selfcheck runs, AC5 again over the landing's reconciled tree, and the
RED-first observation of the `New arm:` line, staged against the base emitter and the base 7h.

**Evidences:** TOOL-dDeclaredLoop-46
- AC1 — `KIT_RUN_GATES_VERSION` — the runner's version line and the README marker both print 1.49, one above origin/main's 1.48 at `179486e8f`, the higher of it and the branch's 1.47 PINNED 2026-11-15; `govkit.STAGE_FLOOR_RUN_GATES` prints `(1, 49)`, and the canary's `KNOWN` count prints 2 PINNED 2026-11-15.
- AC2 — `tomllib` — the join reads 70 tables in 27 files, none lacking `stage`, none differing from its row, and `stage` last in each, PINNED 2026-11-15; the `govkit.py selfcheck` exit is owed to the close.
- AC3 — `check_target_reads_subject` — with `floor=STAGE_FLOOR_RUN_GATES` it answered False at 1.48 and True at 1.49 PINNED 2026-11-15; the push-main apply exited 0 and each of its three emitted rows carried the descriptor's `stage` as its last key, the `pre-push self-test` row after its `ceiling`, PINNED 2026-11-15.
- AC4 — `pre-push self-test` — owed to the close: the plain selfcheck run a scratch copy needs is a gate the hook refuses in this pass; the new arm in `tools/govkit/selftest.py#check_benched_probe_arms` stages the disagreeing and the absent value.
- AC5 — `STAGE_FLOOR_RUN_GATES` — after `git fetch origin` the probe printed origin/main 1.48, floor `(1, 49)`, tree 1.49 and an origin/main canary that does not admit `stage`, so the floor stands above origin/main's runner and at the tree's own, PINNED 2026-11-15; the close and the landing observe it again.
