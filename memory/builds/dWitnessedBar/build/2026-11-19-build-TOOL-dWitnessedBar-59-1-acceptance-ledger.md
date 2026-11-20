# TOOL-dWitnessedBar-59 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-59

No merge bar, no self-test suite and no gate leg ran in this pass, the naming lexicon excepted. The
criteria were observed on node d, 2026-11-20, at base `b0cf02bad`, by a scratch probe that drove
`tools/govkit/steps/inherited_red.py` under `-I` over fixture targets at `%TEMP%/ir59p`, cut
`read_policy_key` from `.githooks/pre-push` as the parity arm cuts it and ran it under the resolved
bash, and ran the same three observations over a staged copy of the step whose five `.split("\n")`
calls read `.splitlines()`. The new checks in `check_inherited_red_step`, `tools/govkit/selftest.py`,
hold the same fixtures and were compiled, not run: their run, their RED-first observation and the legs
of spec section 7 are owed to the main loop at the close. No step code moved: the landed step meets S1
and S2.

**Evidences:** TOOL-dWitnessedBar-59
- AC1 — `blocks = "every-red"` — a `.githooks/gate-env.sh` holding
  `A=1<LF>INHERITED_RED=park<CR>INHERITED_RED=land<LF>B=2<LF>`: the up exited 0 and `policy.toml` read
  `every-red` under `[verdict]`. The staged `splitlines()` step wrote `own-mixed-contended`: the red.
- AC2 — `not an assignment` — a file holding `A=1<LF>INHERITED_RED=park<CR> INHERITED_RED=land<LF>B=2<LF>`:
  the witness before the up exited 1 with `assigns` once in its stdout and `not an assignment` nowhere,
  and the up left exactly `A=1<LF>B=2<LF>`. The staged step's witness printed `not an assignment` and
  its up left `A=1<LF> INHERITED_RED=land<LF>B=2`: the red on both halves.
- AC3 — `lone-cr` — after the sentinel `K=plain` read `plain`, the cut `read_policy_key` and the step's
  `read_value` both read `park<CR>INHERITED_RED=land` from `INHERITED_RED=park<CR>INHERITED_RED=land<LF>`;
  the staged step's `read_value` read `land`, which the arm's check labelled `lone-cr` reds on. The arm's
  row-count check now asserts twelve rows graded, and its comment no longer names a lone CR as unchecked.
