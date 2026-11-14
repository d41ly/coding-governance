# TOOL-dDeclaredLoop-3 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-3

No merge bar, no self-test suite and no gate leg ran in this pass, and
`loop_transition.py check --selftest`, the new leg's command, was not run as a command. The criteria
were observed on node `d` (win32) by probes of the unit's own code: each of the ten plants run one at a
time as `loop_transition.py --fixture --plant <case>`, the memory-tree factory's `typed-kinds` plant,
`loop_items.py check` over the tree, `python -c` calls of `main` with the policy kit finder made to
raise, of `parse_transition_trailer` on four malformed values, of `read_transition` on a malformed
record and of `check_transition_definition` over the tree's own `AGENTS.md`, a scratch repository
probing the witness and staged-index refusals, and the `grep` commands the criteria spell.

Timing, for the budget row: the ten plants run one at a time by direct CLI, each building its own
scratch repository, took 17 s in all, PINNED 2026-11-15, the proxy reading the
`loop transition record` budget row prices at its floor.

RED observed in this pass, each the refusal its plant owes: `log-drift` and `orphan-log` exit 1 naming
the commit and `To`, and the record; `line-drift` exits 1 naming the definition; `pre-spec`'s first
check exits 1 printing `pending`; `no-row` exits 1 `refused`; `empty-set` exits 2 naming
`transitions.record`; `--field colour=red` exits 2; and both verbs exit 2 `unarmed` where the policy
kit does not resolve.

Owed to the close: every leg the spec's section 7 names; the `loop transition record` leg, with the
RED-first observation its `New arm:` line names, staged by the `log-drift` plant with the check
comparing a record to itself; the `micro-format definitions` grammar over the new definition; the
`charter size` warning on the charter's size row, the owner's (F11); the `kickoff-manifest ratchet`
over the re-stamp; AC9's `core.py meta-check`; and a budget re-priced from the main loop's first
reading of the new leg alone.

**Evidences:** TOOL-dDeclaredLoop-3
- AC1 — `python loop_transition.py --fixture --plant default` — exited 0: `record` wrote the record
  `transition-1`, and its commit's trailer read back as
  `planning -> designing · build=tFix · item=item.plan.exit · sha=<sha8> · stand-in=dRankedPlan`;
  `build_records.py read` of the record exited 0; stdout carried
  `transition — tFix · planning → designing · item.plan.exit · <sha8>`; and `check` exited 0 with one
  trailer, one record and no finding.
- AC2 — `--plant subset-trailer-line` — exited 0 printing `records 0` and the trailer, `check` exit 0;
  `--plant subset-log` printed `trailer none` and `records 1`, and `read_transitions` returned the
  move with source `log`, `check` exit 0.
- AC3 — `--plant empty-set` — `record` exited 2 printing
  `loop: unanswered · transitions.record does not resolve at HEAD`, the policy refusal naming no valid
  revision before it; the commit count read `unchanged`; `check` exited 2.
- AC4 — `--plant log-drift` — `check` exited 1 naming the commit and
  `To: the trailer says designing, the record building`; `--plant orphan-log` exited 1 naming the
  `transition-2` record, which no trailer matches.
- AC5 — `--plant no-row` — `record` exited 1 printing
  `refused — build · planning · item.design.exit · recorded: no row`, the commit count `unchanged`.
- AC6 — `grep -n 'transition — <slug>' coding-governance-agents.template.md` — found the definition
  inside the microformats fence, after the `SPEC` line; `--plant line-drift` exited 1 naming the
  definition `AGENTS.md` reads against the renderer's.
- AC7 — `--plant pre-spec` — the first move wrote a trailer and `records 0`, and `check` printed
  `pending — 1 move(s) before the build's first spec`, exit 1; after the spec was committed and a
  second move recorded, the folder held `transition-1` from planning and `transition-2` from
  designing, in move order, and `check` exited 0.
- AC8 — `--plant field` — `--field colour=red` exited 2 naming `colour`; with `composition`
  registered, the trailer and `read_transitions` carried `composition=3f9c2a71`, and `check` exited
  0, holding the record's `Composition` field equal to the trailer's.
- AC9 — `grep -n '"loop transition record"' tools/gate-legs.json` — found the row, its argv naming
  `loop_transition.py`, `check` and `--selftest`; `python -m json.tool` parsed the file, and the
  row's `enforces` reads `principle.p20`. The `check --selftest` run itself and its PASS summary are
  owed to the close.
- AC10 — `grep -n 'transitions.record' help/loop.md` — found the section "Recording a build's move",
  which names `trailer`, `log` and `micro-format`, how to opt out of a channel, and the `record` verb.
- AC11 — `python tools/memory-tree/build_records.py --fixture --plant typed-kinds` — printed
  `build-records: typed-kinds · transition · <path> · bound` and its PASS line, eight typed kinds
  bound and no `A` row.
- AC12 — `python tools/loop/loop_items.py check` — exited 0 printing
  `loop: record-version record-kind.transition · 1 · 55701546` and no refusal naming
  `record-kind.transition`.
