# TOOL-dDeclaredLoop-15 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-15

No merge bar, no self-test suite and no gate leg ran in this pass, and neither `check --selftest` of
`loop_table.py` nor `--selftest` of `loop_parents.py`, the two legs' commands, was run as a command.
The criteria were observed on node `d` (win32) by probes of the unit's own code: `check` over the tree,
each plant of `loop_table.py` run one at a time as `--fixture --plant <case>`, each `move` the criteria
spell, each case of the parent route's self-test run on its own as `loop_parents.py --fixture --plant
<case>`, a `python -c` call of `main` with the kit finder made to raise, and the `grep` commands the
criteria spell.

Timing, for the budget row: ten of the parent route's eleven cases, run one at a time by direct CLI,
each building its own scratch repository, took 12 s in all, PINNED 2026-11-14, the proxy reading the
`loop parent routes` budget row prices at its floor.

RED observed in this pass: every plant of `loop_table.py` exits 1 with the refusal it owes, the two
new ones included; the moves out of a terminal and past the landing push exit 1; and the parent route
exits 2 on a state outside the open states, on no kept branch, on a value outside the key's set, on a
README that does not read, and `unarmed` where the policy kit does not resolve.

Owed to the close: every leg the spec's section 7 names; the `loop transition tables` leg, with the
RED-first observation its `New arm:` line names, staged by the `terminal-from` plant with the terminal
branch of the `from` refusal taken out; the `loop parent routes` leg, with the RED-first observation
its `New arm:` line names, staged by the `withdrawn-parent` plant with `read_withdrawn_parents` reading
no `phase` fact; AC9's `core.py meta-check`; and a budget re-priced from the main loop's first reading
of the new leg alone.

The close's RED-first observation, made by the main loop on 2026-11-17 at `c7cbca292` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
`python tools/loop/loop_parents.py --fixture --plant withdrawn-parent` with `read_withdrawn_parents` reading
no phase fact exited 2, and 0 once restored: RED observed.
Not observed: the arm in `tools/loop/loop_table.py`, no staged break was run for it at this close.

**Evidences:** TOOL-dDeclaredLoop-15
- AC1 — `loop: terminal build` — `python loop_table.py check` in `tools/loop/` exited 0 printing
  `loop: terminal build · landed withdrawn superseded incomplete deferred retired refused merged
  answered` after the three level lines, and no level line for `terminal`; `--plant terminal-from`
  exited 1 printing a refusal of the planted row that `leaves landed, a terminal: no move leaves one`;
  `--plant terminal-open` exited 1 printing `landed is both an open build state and a terminal`.
- AC2 — `refused — build · landed` — `move --level build --from deploying --item item.deploy.close
  --outcome closed` exited 0 printing `move — build · deploying → landed · item.deploy.close · stand-in
  dShippedRelease`; from planning, `item.plan.triage-judge` and `item.plan.triage-rule` on refuse each
  named `refused`; from building, the close request on withdrawn with `pushed=no` named `withdrawn`
  and with `pushed=yes` exited 1; from paused, its superseded with `pushed=no` named `superseded`;
  from designing, `item.deploy.parents` on withdrawn named `planning`; and from landed, the resume
  with `prior=testing` exited 1 printing `refused — build · landed · item.life.request · resume: no row`.
- AC3 — `loop: owed item.plan.place · unplaced · dRankedPlan` — `grep -c 'by = "TOOL-dDeclaredLoop-15"'
  loop.toml` in `tools/loop/` printed 0, and `check` printed that line as its one owed line and the
  stand-in line of the close request owned by dWellOiledMachine, beside the four stand-in lines of the
  triage, parents and close items.
- AC4 — `route replan · parent tParent · move designing → planning · item.deploy.parents` — `python
  loop_parents.py --fixture --plant withdrawn-parent --value replan` exited 0 printing that line; with
  `--state testing` it exited 0 printing `route replan · parent tParent · held: testing admits no
  parent row`; with `--state landed` it exited 2 naming the open build states.
- AC5 — `no kept branch` — with `--value adopt-parent-work` the plant exited 0 printing the move line,
  its value named as `route adopt-parent-work`, then `inventory tParent` and the same commit its
  `loop: fixture · kept refs/heads/branch/tParent-run` line named, a branch tip one commit past
  `main`; `--plant no-kept-branch --value adopt-parent-work` exited 2 printing `no kept branch`.
- AC6 — `owner-item · propose item.life.close withdrawn` — with `--value withdraw-too` the plant
  exited 0 printing that text after `route withdraw-too · parent tParent`, no `move` line, and
  `loop: fixture · tree unchanged`.
- AC7 — `route none` — `--plant live-parent` and `--plant no-parents` each exited 0 printing `route
  none`; `route --build dDeclaredLoop --state building` over this tree printed the same.
- AC8 — `deps.on-parent-withdrawn` — `--plant withdrawn-parent` with no `--value` exited 0 printing
  AC4's `route replan` line; with `--value bogus` it exited 2 printing `loop: unanswered ·
  deps.on-parent-withdrawn does not resolve`, the policy refusal naming no valid revision before the
  scratch's one commit.
- AC9 — `meta-check · green` — `grep -n '"loop parent routes"' tools/gate-legs.json` found the leg row,
  its argv naming `loop_parents.py` and `--selftest`, its `enforces` holding `principle.p21`; `grep -n
  'deps.on-parent-withdrawn' help/loop.md` found the section "When a parent build is withdrawn"; and
  `grep -c 'principle.p21' tools/playbook/core-pending.txt` printed 0. The core meta-check is a gate
  and was not run; it is owed to the close.
