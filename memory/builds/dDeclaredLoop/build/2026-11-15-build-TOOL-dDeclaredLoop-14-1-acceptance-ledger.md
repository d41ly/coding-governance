# TOOL-dDeclaredLoop-14 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-14

No merge bar, no self-test suite and no gate leg ran in this pass, and `position.py --selftest` was not
run. The criteria were observed on node `d` (win32) by probes of the unit's own code: each of the
eighteen plants of `tools/loop/position.py` run one at a time by direct CLI, each building its scratch
repository and bare remote under the host temp directory and removing it, the six new ones and unit
7's twelve, which all still read `held`; `check_step_fields` called from the sourced driver over a
separator, a line feed, the bypass flag and a clean triple; runlog's `read_run_state` over one
refusal row; check-arms' own `branches` and `scan_refusal_sites` readers imported by path; the
unattended adopter's render of the Skill; and `gen_map.py --write` for the map.

Owed to the close: every leg the spec's section 7 names, `core meta-check`, `harness arms`, `unattended
kit gate`, `docs` and `positional` among them; the RED-first observation of the spec's two `New arm:`
lines, `frontier-chain` staged red with the needs test removed from `derive_frontier`, and the suite's
`--refused` arms and the three reworded `--propose` arms staged red with one message's wording changed
under the arms check; and the `loop position fixtures` row in `tools/run-gates/selftest-budgets.txt`
and the leg's hang ceiling in `tools/gate-legs.json` read against the leg's own timing, since the
eighteen plants read slower under load than unit 7's twelve did alone. The unattended suite is waived
for this landing; its parity row, hostile-value entry and `--refused` arms were written, not run.

The close's RED-first observation, made by the main loop on 2026-11-17 at `c7cbca292` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
Not observed: the arm in `tools/loop/position.py`, no staged break was run for it at this close.
Not observed: the arm in `tools/unattended/unattended.test.sh`, a suite arm, left unrun for the owner's opt-in
slow-suite run.

**Evidences:** TOOL-dDeclaredLoop-14
- AC1 — `frontier — B` — `python tools/loop/position.py --fixture --plant frontier-chain` printed `frontier — item.build.unit-lease`, B, and no other tag, with A, `item.build.base`, witnessed by a recorded move naming it, and `next — item.build.unit-lease`, the frontier's first entry, then `held`, exit 0.
- AC2 — `frontier-parallel` — the plant printed `frontier — item.build.base · item.build.unit-lease`, A and B, B's needs emptied in its in-memory definition and neither witnessed, and `held`, exit 0.
- AC3 — `refusal —` — `--plant frontier-refused` printed `frontier — item.build.base` and one `refusal — item.build.base · item.build.base@TOOL-tPos-1#… · probe` line, the key the frontier gave A, and `held`, exit 0.
- AC4 — `refusal · item <tag> · step <key> · reason probe` — the same plant ran the driver's `--refused tPos --item item.build.base --key <A's key> --reason probe`, which printed `unattended: refusal recorded against …`; the plant printed the one scratch run-state row matching that grammar, one non-blank line added, the engine's `--check-refusal` reading gov's own items over the scratch tree's unarmed composition (deviation 145).
- AC5 — `check 48` — `--plant frontier-bad-key` ran `--refused` with the key `item.build.base@TOOL-tPos-1` and then the tag `item.build.nowhere`, each exit 1 printing `UNATTENDED check 48 FAILED — the position engine did not hold this refusal, …` with the engine's `loop: refused` reason, and the run-state file's bytes unchanged, then `held`.
- AC6 — `frontier — none` — `--plant frontier-none`, step.build narrowed to A, witnessed, and `item.build.acceptance` needing `item.test.merge`, printed `frontier — none` and neither tag, and `held`, exit 0.
- AC7 — `frontier:` — `--plant plan-frontier` recorded the refusal and ran the driver's `--plan tPos`, whose line after `next:` read `frontier: item.build.base`, and `held`, exit 0.
- AC8 — `principle.p24` — `python -m json.tool gate-legs.json` in the tools folder read clean, the `loop position fixtures` row's `enforces` holding `principle.p22` and `principle.p24`, and `grep -c principle.p24 tools/playbook/core-pending.txt` printed 0; the meta-check's own reading is owed to the close.
- AC9 — `read_run_state` — `python -c` importing runlog's model read one row `2026-11-15T00:00:00Z refusal · item item.build.base · step item.build.base@TOOL-x-1#0123abcd · reason probe` as kind `refusal` with that step and no unknown kind; `grep -c '"refusal"' tools/drift-audit/drift_report.py` printed 1.
- AC10 — `unattended.sh --refused ` — `grep -c` over the Skill render printed 1; `cmp` of the verb carrier and its render exited 0, each with a `--refused` entry; the render's CR-stripped byte count equals the Skill's raised row in `tools/template-size-limits.txt`, both read at observation time.
- AC11 — `field-shape` — check-arms imported by path counted the driver's fail branches plus its gate's refusal sites, a sum equal to the count field of the one `TOOL-dDeclaredLoop-14` token `grep -oE` prints from `.memory-tree.conf`; the `field-shape` ERE matched no more messages than its ceiling, `missing-run-state` and `required-flag` each at their own; `grep -c '^- \*\*TOOL-dDeclaredLoop-14\*\*' memory/DECISIONS.md` printed 1.
