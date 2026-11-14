# TOOL-dDeclaredLoop-13 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-13

No merge bar, no self-test suite and no gate leg ran in this pass, and neither `check --selftest` of
`loop_table.py` nor that of `loop_checklist.py`, the two legs' commands, was run as a command. The
criteria were observed on node `d` (win32) by probes of the unit's own code: `check` over the tree,
each plant run one at a time as `--fixture --plant <case>`, each `move` the criteria spell, the shared
case loop called in process over a stub `main`, and the `grep` commands the criteria spell. The empty
and absent definitions were observed by pointing the module's definition name at a scratch copy in the
session scratch folder whose transition headers were renamed, and at a path that does not exist.

RED observed in this pass, each on a break made in memory and never on disk: every plant exits 1 with
the refusal it owes, and `run_selftest_cases` over a stub `main` printed FAIL for a case owing exit 1
that exited 0 and for one whose needle no line held, its summary FAIL and its exit 1. The shared case
loop and the checklist's former loop, both run over the same stub cases, printed the same bytes and
the same exit.

Owed to the close: every leg the spec's section 7 names; the `loop transition tables` leg itself, with
the RED-first observation its `New arm:` line names, the failing case staged by deleting row B7; the
`loop checklist tags` leg, with its `New arm:` line's RED-first observation, staged by one case owing
exit 0 set to owe 1, and AC10's comparison of its lines with those at the pass's base; the core
meta-check AC8 names; and `govkit selfcheck`, whose one finding at its `--write` run named
`loop_table.py` as shipped by no rule while the file was still untracked, cleared by staging it.

**Evidences:** TOOL-dDeclaredLoop-13
- AC1 — `loop: table` — `python loop_table.py check` in `tools/loop/` exited 0 printing one line per
  level: build with 25 rows and 7 states, PINNED 2026-11-14
  feature with 8 rows and 5 states, and unit with 8 rows and 4 states, PINNED 2026-11-14;
  `--plant bad-state` exited 1 naming the planted unit row that enters reviewing, and `--plant
  two-rows` exited 1 naming the move `build · building · item.build.exit · recorded` matched by two
  rows, the seventh and the planted one.
- AC2 — `refused` — `move --level build --from planning --item item.design.exit --outcome recorded`
  exited 1 printing `refused — build · planning · item.design.exit · recorded: no row`, and with
  `--from designing` exited 0 printing `move — build · designing → building`.
- AC3 — `@prior` — the resume move with `--fact prior=testing` exited 0 naming `testing`; with no
  `prior` fact, and with `prior=landed`, it exited 2 printing `unanswered`.
- AC4 — `before-push` — the re-entry move from building with `reenters=item.plan.input` and
  `pushed=no` exited 0 naming `planning`; with `pushed=yes` it exited 1; with no `pushed` fact, and
  with `pushed=maybe`, it exited 2.
- AC5 — `bad-exit` — `--plant bad-exit` exited 1 naming three planted rows: one whose item is the
  bare plan.exit, one naming item.plan.nosuch, and one firing on approved, outside the set of
  `item.plan.exit`.
- AC6 — `owed-stale` — `--plant dropped-row` exited 1 naming `item.build.exit` routing recorded to
  transition with no build row and no owed row; `--plant unrouted-row` exited 1 naming the build row on
  `item.build.acceptance`'s pass, routed to `item.build.scope`; `--plant owed-stale` exited 1 naming
  the stale owed row for `item.build.exit`'s recorded; and `check` on the tree printed
  `loop: owed item.deploy.close · closed · TOOL-dDeclaredLoop-15`.
- AC7 — `stand-in dRankedPlan` — `move --level build --from planning --item item.plan.exit --outcome
  recorded` exited 0 printing `move — build · planning → designing · item.plan.exit · stand-in
  dRankedPlan`, and `--plant stand-in` exited 1 naming the stand-in row for item.plan.input, which no
  row names, and the `item.design.exit` row naming dRankedPlan against its item's dIndexedDesign.
- AC8 — `principle.p20` — `grep -n '"loop transition tables"' tools/gate-legs.json` found the leg row,
  its argv naming `loop_table.py`, `check` and `--selftest`; `python -m json.tool` read it with
  `enforces` holding `principle.p20`; `grep -c 'principle.p20' tools/playbook/core-pending.txt`
  printed 0. The core meta-check is a gate and was not run; it is owed to the close.
- AC9 — `loop_table.py move` — `grep -n 'loop_table.py move' loop.md` in `help/` found the section
  "Transition tables", which names `refused`, `stand-in` and the owed rows.
- AC10 — `PASS` — each case of the table's self-test was run on its own as a command and answered as
  the case owes; the self-test itself and the checklist's are legs, not run, and owed to the close.
