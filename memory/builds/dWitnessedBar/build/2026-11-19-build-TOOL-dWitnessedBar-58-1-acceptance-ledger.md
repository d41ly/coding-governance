# TOOL-dWitnessedBar-58 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-58

This pass ran no merge bar, no gate leg and no self-test suite. Every criterion below was checked on node
d on 2026-11-20 by probing the unit's own code: the hook suite's `build_ir_fixture` and `write_ir_stamp`,
cut from `.githooks/pre-push.test.sh` with the new arm read from the file itself, over a scratch fixture
under `%TEMP%`; and the evidence suite's whole `TOOL-dWitnessedBar-40 AC1-AC3` block, its `rec_repo`,
`rec_run` and `rec_dir` cut from `tools/run-gates/run-gates.evidence.test.sh`, run against the real runner
in a scratch clone under `%TEMP%`. The close owes the legs `pre-push self-test`, `run-gates evidence` and
`memory hygiene`, and the RED-first observation of both `New arm:` lines: the hook suite's stub capture,
staged red by deleting the hook's `export GATE_BASE_FROM=inherited`, and the evidence suite's leg-output
and no-`.scoped` assertion, staged red by deleting the runner's `unset GATE_BASE_FROM`.

**Evidences:** TOOL-dWitnessedBar-58
- AC1 — `inherited` — the `IR AC4` fixture's `c2` push, `GOV_GATE_CMD` naming the capturing stub, printed
  the `scoped gate on main push` decision and the stub's file under the fixture's git dir read `inherited`,
  the arm printing `ok — IR TOOL-dWitnessedBar-58 AC1`. The FULL half: the same fixture's `c3` push, the
  caller setting `GATE_BASE_FROM=inherited`, printed `FULL gate on main push` and the file read `unset`,
  the observation the landed `RP TOOL-dWitnessedBar-56 AC7` arm makes at the close.
- AC2 — `base_from_seen 0` — in the scratch clone over unit 40's `fx/legs.json`, after the run with
  `GATE_BASE=<sha>` and `GATE_BASE_FROM=inherited`, no `.scoped` file for the tree stood under
  `gate-verdict/`, the header's `base_from` row read `GATE_BASE` then `inherited` (unit 56's `AC8` arm
  green), and the leg's `0.out` read `base_from_seen 0`, the new arm printing
  `ok — TOOL-dWitnessedBar-58 AC2`; all seven assertions of the block green. `FLOOR_ASSERTIONS` raised
  309 to 310.
- AC3 — `GATE_BASE_FROM=inherited` — OWED to the main loop at the close, as S3 states: the AC4 line of
  `2026-11-19-build-TOOL-dWitnessedBar-56-1-acceptance-ledger.md` still reads `NOT OBSERVED` at this pass,
  and the close rewrites it to the OBSERVED form naming this unit's AC1 and AC2 and report id 12.
