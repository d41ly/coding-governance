# TOOL-dDeclaredLoop-17 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-17

No merge bar, no self-test suite and no gate leg ran in this pass, and `loop_witness.py --selftest`, the
new leg's command, was not run as a command. The criteria were observed on node `d` (win32) by probes
of the unit's own code: each plant of `tools/loop/loop_witness.py` run one at a time as
`--fixture --plant <case>`, the loop reader's two new plants run as `--fixture --plant <case>`, the
self-test's reader-plant arm called in-process with the four plants set aside, the factory's
`typed-kinds` and `pending-kind` plants, and the `grep` commands the criteria spell. Each scratch
repository sat under the host temp directory and was removed after.

RED observed in this pass, each on a staged break restored before the commit: the `acceptance` plant
failed with the commands run in the caller's working tree (its second exit read 0, not 1); the
`probe-rerun` plant failed with the re-run reading `HEAD` (the pinned commit answered `refuted`); the
`hold-inherited` plant failed with the join taken out of `run_hold` (the `OWN` hold exited 0), and
again with `check_bar_tied` ignoring the staged set (the admitted hold exited 1, `ran at`).

Owed to the close: every leg the spec's section 7 names; the `loop computed witness` leg itself, with
the RED-first observation its `New arm:` line names; the driver suite `tools/unattended/unattended.test.sh`,
waived under README rule 8, whose park-path arms observe the `write_gates_staged` call in the held
close (S6) and whose two edited arms now hold under `host-degraded`; and the govkit selfcheck over the
new `[[exempt_leg]]` row (deviation 173).

**Evidences:** TOOL-dDeclaredLoop-17
- AC1 — `Writer: stand-in` — `--plant acceptance` exited 0: the stand-in wrote
  `memory/builds/tFix/build/2026-11-14-build-TOOL-tFix-1-acceptance-1.md` from an eight-digit `--sha`,
  the record read `Writer` stand-in, the commit's full sha and two run lines whose exits read 0 then 1
  while the uncommitted edit beside them would have answered 0; `build_records.py read` exited 0 on it,
  and `git worktree list` showed the fixture's one worktree.
- AC2 — `Writer agent is outside executor · stand-in` — `--plant acceptance-malformed` exited 0: the
  record with no run line read exit 1, `run line is missing`, and the record whose `Writer` reads
  `agent` read exit 1 with that line.
- AC3 — `confirmed` — `--plant probe-rerun` exited 0: `rerun` at the pinned commit answered
  `confirmed`, exit 0; at the later commit `refuted`, exit 1; at `0badc0de` `inconclusive`, exit 1.
- AC4 — `UNATTENDED check 83 FAILED` — `--plant hold-inherited` exited 0: over a run the driver's
  `--preflight` opened, with a `gates-run` fact naming a bar record reading `x leg OWN`, the hold exited
  1 printing that line and `its attribution reads x leg OWN`; over every leg INHERITED with the
  run-state committed after the bar it exited 0 and the run-state read `phase: HELD`.
- AC5 — `ran at` — the same plant committed a `BACKLOG.md` row beside the run-state: with the bar
  record's `staged` file naming that path at its committed blob the hold exited 0, and with the file
  absent it exited 1 printing `UNATTENDED check 83 FAILED` and `ran at`.
- AC6 — `loop: computed-witness` — the definition's rows read through `read_computed_witnesses`, and
  each plant's printed lines, show three `loop: computed-witness` lines, `acceptance` reading
  `class history`; `--plant computed-actor` and `--plant computed-unserved` each exited 1 with a
  `loop: refused` line naming `computed-witness row 1 (acceptance)`. The `--check` command is the
  `loop definition` leg and was not run as a command.
- AC7 — `enforces` — `grep -n '"loop computed witness"' tools/gate-legs.json` found the row, its argv
  naming `loop_witness.py --selftest` and its `enforces` holding `principle.p2`;
  `grep -n 'inherited-red' tools/unattended/VERBS.template.md` found the `--hold` sentence. The
  criterion's `grep -c 'principle.p2' tools/playbook/core-pending.txt` printed 9, not 0, because the
  pattern also matches the rows of `principle.p20` to `principle.p29`, which stay; the `principle.p2` row
  itself is gone, `grep -cP 'principle\.p2\t'` printing 0. The criterion's grep is the spec's to revise.
- AC8 — `build-records: typed-kinds · acceptance · <path> · bound` — `build_records.py --fixture --plant
  typed-kinds` printed that line for `2026-11-14-build-ARCH-tKinds-1-acceptance-1.md` and ended `PASS`,
  having asserted each record's `S` row with its kind and no `A` row.
