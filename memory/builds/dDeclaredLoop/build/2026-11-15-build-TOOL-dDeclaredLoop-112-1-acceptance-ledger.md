# TOOL-dDeclaredLoop-112 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-112

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on node
`a` (win32, bash 5.3) by probes of the unit's own code: the keyed expander and `spec_ask_verbs` sliced
out of this pass's driver and out of the base driver, extracted with `git archive 6d91c49a tools` into
a scratch repository under the host temp directory; the driver's `--plan`, `--plan --asks` and
`--status` run from this worktree and from that extraction over this tree; `fork-count.sh --only
unattended-plan-handover`, which measured the new row; the spawn scanner's own `scan_spawn_file` over
both drivers; and `gen_map.py --write` for the map.

Owed to the close: every leg the spec's section 7 names; the RED-first observation of the spec's
`New arm:` line, the row `unattended-plan-handover` run with the base driver's `build_ask_plan` and
`ask_rank_order` bytes restored in the worktree, which is AC4's second half; and the
`unattended-status` and `check-unattended` rows read by the leg itself.

The close's RED-first observation, made by the main loop on 2026-11-17 at `a48272d09` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
Not observed: the arm in `memory/project/fork-ceilings.txt`, no staged break was run for it at this close.

**Evidences:** TOOL-dDeclaredLoop-112
- AC1 — `--keyed` — with `lib-unattended.sh` sourced, `expand_id_runs --keyed` read `p` TAB `closes` TAB `TOOL-x-1..3 TOOL-y-7@rev-2` and printed four rows keyed `p` TAB `closes`, ids `TOOL-x-1`, `TOOL-x-2`, `TOOL-x-3` and `TOOL-y-7`, and the same words unkeyed printed the four bare ids; `spec_ask_verbs`, sliced with `read_spec_asks` and the expander out of this pass's driver and alone out of the base driver, printed byte-identical id lists for `closes` and `advances` over every tracked spec of `memory/builds/dDeclaredLoop/spec/` and `memory/builds/dConvergedCharter/spec/`, a non-empty population carrying both verbs.
- AC2 — `refused=duplicate-closer` — `GOV_POSITION_STATES= bash tools/unattended/unattended.sh --plan --asks dConvergedCharter` from this worktree and from the base extraction printed byte-identical output, an `ASK` row per filed ask with the `refused=duplicate-closer` row among them; `--plan dConvergedCharter` with the engine called printed the same output from both, its `next:` line included. The base run took 239 s, this pass's 98 s (PINNED 2026-11-15).
- AC3 — `position —` — `bash tools/unattended/unattended.sh --status dDeclaredLoop` printed the engine's `position — dDeclaredLoop · …` line, exit 0, in 50 s and again in 40 s against the 60 s ceiling (PINNED 2026-11-15); `GOV_POSITION_STATES= … --plan dDeclaredLoop` printed byte-identical hand-overs from this pass, in 33 s, and from the base extraction, in 747 s inside the 900 s bound, a first base run beside a concurrent probe having hit that bound (PINNED 2026-11-15).
- AC4 — `unattended-plan-handover` — `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt . --only unattended-plan-handover` printed `ok unattended-plan-handover · measured 209 · ceiling 209 · base 1100`, exit 0, after three readings of 209 over a scratch copy of the row; the base figure is the same row counted with the base extraction as its root, and `--only unattended-status` still read 45 at its ceiling. The row's setup run by hand with `--asks` printed three `ASK` rows, `TOOL-tFork-91` with `cover=TOOL-tFork-1`, the spec whose header closes it. The red half, the base driver's two functions restored in the worktree, is the New arm owed to the close.
- AC5 — `status-line` — `python tools/loop/position.py --fixture --plant plan-line` printed the driver's `next:` line equal to the engine's and `position: fixture · plan-line · held`; `--plant status-line` printed `position: fixture · status-line · held`; both exited 0.
