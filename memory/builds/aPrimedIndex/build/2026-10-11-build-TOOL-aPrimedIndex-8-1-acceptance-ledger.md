# TOOL-aPrimedIndex-8 — acceptance ledger

**Serves:** journal TOOL-aPrimedIndex-8

No merge bar and no self-test suite ran in this pass. Every criterion was observed through lander
arms 24 to 32, run as a slice: the suite's prologue plus those arms. The slice ran in `pi6`, a clone
of this branch carrying this pass's lander, suite and pin as a local commit, its outputs
regenerated. Every arm printed `ok` and the slice printed `push-main.test: all cases ok`.

Red observations:
- Arm 30's cleanup was red against the lander as committed before this pass, run with this pass's
  suite in `pi7`. It reported exit 1, the branch unmoved and checked out, and no `clean=1`, because
  the stub's untracked file survived the reset.
- The attended refusal sites read red in `check-arms.py --check` before arm 32 and the pin, both in
  this build's pre-run and in the closing review.
- Arm 25 read red against the built lander with its old fixture, as the closing review reproduced
  (`l25=0`).
- Arm 26 read red with its old fixture against both landers earlier in this build (TOOL-aPrimedIndex-5).

The close still owes the lander self-test whole.

**Evidences:** TOOL-aPrimedIndex-8
- AC1 — `git status --porcelain` — arm 30's stub `regen.py` wrote `regen-litter.txt` and exited 1. `--prepare` refused, left `feat` unmoved and checked out, and `git status --porcelain` printed nothing.
- AC2 — `check-arms.py --check` — arm 32 asserted the whole refusal `push-main: the generated outputs this landing owes could not be regenerated (named above). Aborted (no push).`, and the remote's main stayed at its pre-run sha. With the commit-failure site pinned beside its mint twin, `check-arms.py --check` exited 0.
- AC3 — `ok` — arm 25 printed `ok   — 25 a tree without the lexicon and govkit files skips both checks by name, with no DEAD PROBE or REFUSED` once its fixture also left out `regen.py`.
- AC4 — `for TOOL-tFix-26` — arm 26 passed with its mint subject ending `for TOOL-tFix-26`, and arm 29 passed on the whole regen subject `regen: generated outputs onto origin/main at <tip8> for TOOL-tFix-29`. Both fixtures define their unit through a spec the new `write_unit_spec` commits into the clone's first spec folder.
