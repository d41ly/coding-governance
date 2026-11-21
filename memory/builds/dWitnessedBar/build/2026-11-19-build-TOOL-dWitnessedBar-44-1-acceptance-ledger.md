# TOOL-dWitnessedBar-44 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-44

No merge bar, no self-test suite and no gate leg ran in this pass, the naming lexicon excepted. The
criteria were observed on node d, 2026-11-20, by a scratch probe that drove the step's three verbs
under `-I`, as the runner runs them, over fixture repositories at `%TEMP%/p44`: every case below read
green over this pass's `inherited_red.py`, and the same probe over the step at `c9b50206` read red on
each of AC1, AC2 and AC3, so the probe can fail. The `New arm:` of spec section 7,
`check_inherited_red_step` in `tools/govkit/selftest.py`, holds the same fixtures and was not run: its
run and its RED-first observation are owed to the main loop at the close, with the legs section 7
names.

**Evidences:** TOOL-dWitnessedBar-44
- AC1 — `GATE_POLICY_FILE` — a target whose `.unattended.conf` names `ops/gate-policy.sh`, holding
  `INHERITED_RED=park  # old`, with no `.githooks/gate-env.sh`: the up exited 0, `policy.toml` read
  `blocks = "every-red"` under `[verdict]`, the custom file kept its other line alone, and the witness
  exited 1 before the up and 0 after, naming `ops/gate-policy.sh` and `park`. At `c9b50206` the up
  printed `no INHERITED_RED in .githooks/gate-env.sh` and wrote nothing: the red.
- AC2 — `INHERITED_RED=Park` — `Park`, `LAND`, `bogus` and `'park'` each wrote `every-red`, and `land`
  alone `own-mixed-contended`; a `.githooks/gate-env.sh` holding `land` beside a `GATE_POLICY_FILE`
  of `/etc/x`, `C:/x`, `../x`, `a/../b` or `..` wrote `every-red`. With no key in either file and an
  off-tree path, the witness held and the up wrote no byte. At `c9b50206` each off-table value wrote
  nothing and each off-tree path wrote `own-mixed-contended`: the red.
- AC3 — `down` — `.githooks/gate-env.sh` holding `land` beside `ops/p.sh` holding `park`: the up wrote
  `every-red` and took the key out of both files; the witness printed two lines, one naming
  `.githooks/gate-env.sh` and `land`, one naming `ops/p.sh` and `park`; the down restored every file
  byte for byte. A policy file already holding `own-mixed-contended` refused with `conflict ·
  verdict.blocks · policy own-mixed-contended · gate every-red` and no byte written. At `c9b50206` the
  up wrote `own-mixed-contended` and left `ops/p.sh` holding the key: the red.
- AC4 — `grep -c inherited_red.py help/upgrade-steps.md` — printed 4, and `grep -c GATE_POLICY_FILE
  help/upgrade-steps.md` printed 2; both printed 0 over the page at `c9b50206`.
