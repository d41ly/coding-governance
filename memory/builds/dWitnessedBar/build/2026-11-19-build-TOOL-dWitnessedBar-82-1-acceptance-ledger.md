# TOOL-dWitnessedBar-82 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-82

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on node d,
2026-11-21, by reading `tools/run-gates/run-gates.gov.test.sh` and by a scratch counting probe over it,
which sums each `a=$((a+<k>))` line and multiplies an indented one by the word list of its enclosing
`for` loop. The suite and both scratch copies below passed `bash -n`. The change is comment lines and
the constant's value, so the suite's `memory/project/shell-role.txt` row holds
(`tools/gate-lint/sh_hygiene.py#measure_code_lines` counts code lines only) and no widen record is
written. The arm's runs in scratch clones and the `New arm:` line's RED-first observation are the
main loop's at the close.

**Evidences:** TOOL-dWitnessedBar-82
- AC1 — `PASS (<n> assertions)` — the probe counted 74 executed assertions over the built suite and 72 over unit 73's blob `71f212ad1`, the difference being unit 78's every-key and line-rule records (DERIVED from the builder's probe); the plant loop counted at its 26 cases, the signer-temp sweep at 5 and each PM_SCRUB copy loop at 2 (DERIVED from the builder's probe). `grep '^FLOOR_ASSERTIONS='` prints `FLOOR_ASSERTIONS=74`, and the `RAISED 72 -> 74 by TOOL-dWitnessedBar-82` comment sits directly below it (DERIVED from the builder's probe). The arm's `PASS` line in a scratch clone at the pass commit is OWED to the main loop at the close.
- AC2 — `_rg_v:1}` — over a scratch copy without unit 78 S13's fourth-record arm, from its `# THE LINE RULES` header to its failure line, the probe counted 73, one short of the floor (DERIVED from the builder's probe); over a copy without the `'${_rg_v:1}'` call of `check_key_variant` it counted 74, so at this pass that copy passes as S2 says, and it reds only once `TOOL-dWitnessedBar-85` S1 counts the variants (DERIVED from the builder's probe). The arm's two runs in scratch clones and their floor lines, recorded here, are OWED to the main loop at the close.
- AC3 — `FLOOR_ASSERTIONS` — the criterion's grep over the ledgers of units 76, 77 and 78 prints one line in each, and each line names `TOOL-dWitnessedBar-82` S1 and S3 (DERIVED from the builder's probe).
