# TOOL-dWitnessedBar-60 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-60

This pass ran no merge bar, no gate leg and no self-test suite. Every criterion below was checked on node
d on 2026-11-20 by probing the unit's own code: the `sed` and `grep` lines each criterion spells, run over
the built tree; `check_bar_scrub_parity`, cut from `tools/run-gates/run-gates.gov.test.sh#check_bar_scrub_parity`
and run over the shipped files and staged copies in the run's scratch; and `tools/run-gates/post-merge.sh`
run in a scratch bare remote and clone under `%TEMP%`, built as the evidence suite's post-merge fixture
builds it, with `GOV_GATE_CMD="bash bar.sh"` and the suite's `env` dump bar. The close owes the legs
`pre-push self-test`, `pre-push bar self-test`, `measure-legs selftest`, `run-gates evidence`,
`run-gates gov canary`, `scratch-guard self-test`, `tier2-review self-test` and `memory hygiene`, and the
RED-first observation of both `New arm:` lines: the gov canary's parity arm, staged red by cutting
`GATE_SELECTION` from a copy of `PM_SCRUB`, and the evidence suite's post-merge run, staged red by
restoring the old `PM_SCRUB`.

**Evidences:** TOOL-dWitnessedBar-60
- AC1 — `BAR_CLEARED_KNOBS` — the cut of `.githooks/pre-push` printed `GATE_DOCS_BASE GATE_BASE_FROM
  GATE_SELECTION GATE_REUSE_PUSH GATE_REUSE_LINEAGE GATE_REUSE_DIGEST_ENV GATE_REUSE_SAMPLE GATE_REUSE_DAY`,
  and `grep -c 'GATE_SELECTION'` printed 2 for `tools/run-gates/post-merge.sh` and 1 for
  `tools/unattended/unattended.sh`. The hook's one loop, cut and sourced under four set knobs, left
  `ENV_CLEARED` reading ` GATE_DOCS_BASE GATE_BASE_FROM GATE_SELECTION GATE_REUSE_DAY`, the order the four
  loops it replaced produced, and none of the four in the environment.
- AC2 — `PM_SCRUB` — `check_bar_scrub_parity` printed nothing and returned 0 over the built tree; over a
  `post-merge.sh` copy with `GATE_SELECTION` cut from `PM_SCRUB` it printed `PM_SCRUB in <copy> lacks
  GATE_SELECTION` and returned 1; over a hook copy with no `BAR_CLEARED_KNOBS` line it printed
  `BAR_CLEARED_KNOBS reads empty in <copy>` and returned 1. Over both callers at the base commit it named
  the seven names S2 adds, once per caller list, the population §4 pins. `FLOOR_ASSERTIONS` raised 35 to 38.
- AC3 — `GATE_SELECTION` — in the scratch clone, `post-merge.sh` run with `GATE_SELECTION` and
  `GATE_BASE_FROM=inherited` in its environment exited 0, its output read `post-merge: not honoured from the
  environment: GATE_BASE_FROM GATE_SELECTION`, and `grep -c '^GATE_SELECTION=\|^GATE_BASE_FROM='` over the
  bar's dump printed 0, on a first run and on a second run of the same sha, as the arm runs after AC5's.
  The base commit's `post-merge.sh` in the same fixture printed 1. `FLOOR_ASSERTIONS` raised 310 to 311.
- AC4 — `_gknobs` — the cut of `tools/unattended/unattended.sh` printed the seven names it had plus the
  seven S3 adds, every name of both hook constants, and the `_gscrub` grep named the scoped call in `tools/unattended/unattended.sh#dod_met`,
  carrying `${_gfrom[@]+"${_gfrom[@]}"}` after `"${_gscrub[@]}"`.
  `GATE_BASE_FROM=x GATE_SELECTION=y env -u GATE_SELECTION -u GATE_BASE_FROM GATE_BASE_FROM=inherited`
  printed `inherited unset` to the child.
