# TOOL-dDeclaredLoop-7 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-7

No merge bar, no self-test suite and no gate leg ran in this pass, and `position.py --selftest` was not
run. The criteria were observed on node `d` (win32) by probes of the unit's own code: each of the
twelve plants of `tools/loop/position.py` run one at a time by direct CLI, each building its scratch
repository and bare remote under the host temp directory and removing it; `loop_table.py check` and
one `move` over the shipped tables after `derive_from_states` was factored out; `check_recorded_move`
probed over a held and an unheld move; the driver's `--plan` and `--status` over a kept scratch plant;
the spawn scanner's own `scan_spawn_tree` over the driver and its suite; `fork-count.sh --only
unattended-status`, which re-set that row; and `gen_map.py --write` for the map.

Owed to the close: every leg the spec's section 7 names, `core meta-check` and `docs` among them, the
meta-check refused to this role by the scratch guard; the RED-first observation of the spec's two
`New arm:` lines, each plant staged red, `typed-status` with the header read as a witness, and the
moved ladder arms of `tools/unattended/unattended.test.sh` staged red with one shape's wording
changed; and the `loop position fixtures` row in `tools/run-gates/selftest-budgets.txt` read against
the leg's own timing. The unattended suite is waived for this landing; its arms that assert a typed
`CLOSED` spec prints the terminal shape, and those counting one `--status` line, now read the engine.

The close's RED-first observation, made by the main loop on 2026-11-17 at `c7cbca292` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
Not observed: the arm in `tools/loop/position.py`, no staged break was run for it at this close.
Not observed: the arm in `tools/unattended/unattended.test.sh`, a suite arm, left unrun for the owner's opt-in
slow-suite run.

**Evidences:** TOOL-dDeclaredLoop-7
- AC1 — `unit —` — `python position.py --fixture --plant steps` in the loop kit's folder printed `unit —` lines `deployed`, `built` and `designed`, the position line's step `step.build`, the designed unit's, and `held`; `--plant typed-status` printed the unit whose header reads `CLOSED` as `designed`, and `held`; both exited 0.
- AC2 — `next —` — `--plant idempotent` printed `next — item.build.unit-lease`, the second item, with its key, and a `claim —` line for `item.build.base@TOOL-tPos-1#…` reading `fresh`, re-read rather than named next, and `held`, exit 0.
- AC3 — `derive_instance_key` — the same plant printed two keys for `item.build.base` over one input SHA and over that SHA changed, their `<inputs>` parts different, and `held`.
- AC4 — `awaiting` — `--plant owner-decision` answered `awaiting` with `interrupt — owner-decision · decision · item which-way`, read from the run-state file against the hand-over's owed sets, and `held`, exit 0.
- AC5 — `blocked` — `--plant parent-unlanded` answered `blocked`, its reason naming the parent `tPar`, which has no landed move and a hand-over phase of `RUNNING`, and `held`, exit 0.
- AC6 — `terminal` — `--plant terminal` answered `terminal` over a newest recorded move entering `landed`, and `held`, exit 0.
- AC7 — `invalid-input` — `--plant stale-remote` answered `stale-remote` with no remote, `held`, exit 0; `--plant bad-transition` answered `invalid-input` naming the move no build row holds, `held`, exit 2.
- AC8 — `stuck` — `--plant deadlock`, the step's root item needing an item of a later step, answered `stuck` naming `item.build.exit`, and `held`, exit 0.
- AC9 — `key k1:` — `--plant steps` printed a `read —` line for the README, HEAD, both acceptance records, the run-state file and the remote-tracking ref, and `claim — remote tip refs/remotes/origin/main · key k1:… · fresh`.
- AC10 — `NEXT_RUNGS` — `--plant plan-line` printed the driver's `next:` line equal to `render_next_line`'s in its three states, the READY unit's shape beside the undecided ask and the ask's shape once every unit was deployed, and `held`; `--plant bar-wait` answered `act` at `step.test` and printed `next: none - every tracked spec is terminal`, `held`; `grep -c NEXT_RUNGS tools/unattended/unattended.sh` printed 0.
- AC11 — `position —` — `--plant status-line` ran the driver's `--status` over the `steps` repository with a run-state file, which printed its status line naming the least-advanced unit, then the engine's `position — tPos · …` line, and `held`, exit 0.
- AC12 — `principle.p22` — `python -m json.tool gate-legs.json` in the tools folder read clean, the `loop position fixtures` row carrying `enforces` `["principle.p22"]`, and `grep -c principle.p22 tools/playbook/core-pending.txt` printed 0; the meta-check's own reading is owed to the close.
