# TOOL-dPlacedRequest-7 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-7

The unit was built from its spec at rev-9 (PINNED) on base `222f05e8b`. `tools/loop/loop.toml` gains the
probe program's eight (DERIVED) `[[item]]` rows at `step = "none"`, five (DERIVED) `[[trigger-cause]]`
rows, the `[[record-version]]` rows of `record-kind.probe-trigger` and `record-kind.probe`, the
`probe-rerun` computed witness serving `item.probe.run`, and the outcome `probe` routed to the probe
tool on each of the 19 (DERIVED) role items outside the probe program.
`tools/loop/loop_lib.py#check_program` admits `step = "none"` for the segments of
`tools/loop/loop_lib.py#PROGRAM_SEGMENTS` and returns each program under its segment;
`tools/loop/loop_lib.py#check_probe_outcomes` and `tools/loop/loop_lib.py#read_trigger_causes` are new,
with four (DERIVED) plants by the end of the checklist pass. `tools/loop/probe.py` is the program's tool.
The record factory gains the two kinds and their readers,
`tools/memory-tree/build_records.py#read_probe_trigger` and `tools/memory-tree/build_records.py#read_probe`,
and `tools/memory-tree/tree_lib.py#TYPED_RECORD_KINDS` and the HYGIENE template and its render name them.
The leg `loop probe fixtures` is registered as `loop request fixtures` is, and the pending row of
`principle.p31` is deleted. `PROGRAM_SEGMENTS` replaces the constant `REVIEW_PROGRAM`, which the kit
README cited, so the write set gained `tools/loop/README.md` through `--dispatch`, its reader paragraph
re-pointed and a section on the probe program added.

No gate, suite or bar ran in this pass, and no `--selftest`: the role hook refuses one. Each criterion
below was observed by a probe of the changed code: a `python -c` call of the loop reader's functions over
the parsed definition, or one `--fixture --plant` case of `tools/loop/probe.py` run by direct CLI.

**Evidences:** TOOL-dPlacedRequest-7
- AC1 — `check_loop`, `check_witness_classes` and `check_program` over the tree raised nothing, and the
  program `probe` read the eight items in needs order; `check_item_declarations` refused nothing; each
  probe row carries the owner of the spec's item table. `write_loop_plant` with `probe-step`, then
  `check_program`, raised
  `loop.toml: the item item.plan.x step 'none' is not step.plan, the step its tag opens`.
  `tools/loop/loop_table.py#check_transition_tables` over the tree returned no refusal and no
  `stand-in item.probe.` line.
- AC2 — `--fixture --plant trigger-causes` held, exit 0 (PINNED): `--cause hunch` exited 2 (PINNED)
  naming `point owner observation raised reproduction`;
  `--cause owner --build dExample --unit TOOL-dExample-2` exited 0 (PINNED) writing
  `<date>-build-TOOL-dExample-2-probe-trigger-1.md`; the same call without `--unit` exited 2 (PINNED)
  and the build folder held one (DERIVED) record.
- AC3 — the plants `raise-owner-only`, `raise-off`, `points-unlisted`, `observation-at-plan` and
  `observation-on-request` each held, exit 0 (PINNED): every refused cause exited 1 (PINNED) printing
  `probe — not opened` naming its key and ending `· to item.entry.place`, `git status --porcelain`
  printed nothing after each, and each value's admitted case opened, the `--cause owner` case under
  `on-request` among them.
- AC4 — `--fixture --plant pin` held: an unresolvable `--sha` exited 2 (PINNED) writing nothing;
  `git log -1 --format=%s` read `probe pin(item.entry.place): verification`, and
  `git show HEAD:<record>` held the `Losing` field and no run line; the entry-time trigger's pin wrote
  `3f9c2a71d0e4.probe.md` in the fixture's git common dir `requests/` store, holding `Losing`, and
  `git rev-parse HEAD` was unmoved.
- AC5 — `--fixture --plant run-judge` held: the planted failing command's exit and hash were measured
  through `tools/loop/loop_witness.py#run_witness_commands` at the pinned commit, and `design`, `run`,
  `judge` and `return` wrote `Verdict: confirmed` and `Judged: computed` and printed
  `probe — confirmed · <record> · to item.entry.place`. `--fixture --plant run-refuted` held with
  `refuted`.
- AC6 — `--fixture --plant visual` held: `run` wrote no run line, `Verdict: unrunnable` and
  `Judged: computed`, and `return` printed the route
  `to stand-in:{prefix}/unattended/unattended.sh`. `judge-claimed` held: `Judged: claimed` with no
  `Verdict`, routed to `item.probe.judge-claimed`, and `return` routed to the owner item. `experiment`
  held: `pin` routed to `item.probe.experiment` and printed the beyond-authority line naming dBoundRoles
  and `probe.experiment.authority=within-cap`.
- AC7 — inside `run-judge`, `build_records.py read` exited 0 (PINNED) over both records, and
  `gen_build_index.py --print-bindings` over the fixture printed one (DERIVED) `S` row of kind
  `probe-trigger` and one of kind `probe` and no `A` row. `--fixture --plant verdict-cross` held:
  `read` exited 1 (PINNED) naming `Verdict` over a reproduction carrying `measured`. The factory's own
  `--fixture --plant typed-kinds` printed `PASS typed-kinds — 12 typed kinds bound` (DERIVED).
- AC8 — `--fixture --plant entry-time` held: the record landed at
  `requests/3f9c2a71d0e4.probe-trigger.md` under the fixture's git common dir, the build folder gained
  no file, a second subject printed `probe — joined` and the record held two (DERIVED) `Subject` lines,
  and the first trigger again exited 1 (PINNED) as already opened.
- AC9 — `write_loop_plant` with `role-no-probe`, then `check_probe_outcomes`, refused
  `the item item.plan.research, a role item, carries no probe outcome: it could not ask for a test`,
  and `probe-self` refused
  `the item item.probe.design carries the probe outcome: a probe never asks for a probe of itself`.
  Over the tree it printed, and refused nothing,
  `loop: probe outcomes · 19 role item(s) route probe to stand-in:{prefix}/loop/probe.py · 8 probe item(s) carry none`
  (DERIVED); `check_transition_tables` refused no cross-step route, and
  `tools/loop/termination.py#check_termination` over gov's composition returned no finding, so no
  counted cycle passes a probe item.
- AC10 — the catalogue read printed the four `probe.*` keys, and the `probe.points` row read `set` and
  `[]`. After the pass commit `09732d80b`, `check_policy.scan_reader_keys` at the repository root
  printed a list holding `probe.experiment.authority`, `probe.observations`, `probe.points` and
  `probe.raise`, and `git grep -n "probe.raise" -- probe.py` in the loop kit's directory found the
  literal-key read `policy.resolve("probe.raise", str(root))`. The same list held one message text
  opening `probe.points`, which the checklist pass reworded to open `the key`.
- AC11 — `grep -n "probe.observations" loop.md` in `help/` finds the section
  `Testing outside Test: the probe program`, which names the two ways in and the four keys.
- AC12 — `tools/gate-legs.json` holds the row `loop probe fixtures`, its argv
  `python {prefix}/loop/probe.py --selftest` and `enforces` holding `principle.p31`; `json.load` read
  the file.
- AC13 — `check_item_declarations` printed
  `loop: item item.probe.design · role:gov-tester · pending · the roles kit holds no gov-tester role`,
  the same for `item.probe.judge-claimed`, and `item.probe.experiment` as `role:gov-researcher` with its
  fields from the role and no `pending`; `grep -c 'actor = "role:tester"' loop.toml` and the same for
  `role:researcher` each printed `0` (DERIVED).
- AC14 — `--fixture --plant design` held: the first call appended one `- method` line, a second with
  `--mark visual` appended a line ending `· visual`; a bad `--expect`, a `--mark` outside the two and a
  command holding the separator each exited 2 (PINNED) with the record's bytes unchanged; over a second
  pinned record, once `run` wrote a run line, a further `design` exited 2 (PINNED) naming the record,
  whose bytes stayed unchanged.
- The sixteen (DERIVED) plants of the pass commit, run one at a time by direct CLI, all held, in 36 s
  (PINNED) on the run's node; after the checklist pass the eighteen (DERIVED) plants held in 111 s
  (PINNED) under load and 49 s (PINNED) again, and the budget row prices the worst reading.

**The checklist, acted on.** The bug-class checklist over the pass commit `09732d80b` selected 40
classes (DERIVED: 34 by an anchor and 6 universal). Four needed a change.
rule-stated-with-no-check-that-fails: refusal branches had no arm, so the plant `refusals` stages a bad
`--asker`, `--request` and `--build`, a retried trigger, pin, design, run, judge and return, a pin of a
path that is no trigger record, run, judge and return out of order, an experiment's run and a returned
request probe, and held, exit 0 (PINNED); `record-malformed` stages a bad `Sha`, a verdict beside a
claimed judgment, a verdict with no `Judged`, a bad method line, a bad run line and a trigger's bad
`Asker`, each read exit 1 (PINNED) naming its field; `loop_lib.py`'s plant `probe-route` routes a role
item's `probe` into the probe program, exit 1 (PINNED), and drew
`routes probe to 'item.probe.trigger', not stand-in:{prefix}/loop/probe.py`.
append-without-an-idempotence-key: a retried `trigger` over a build and a retried `design` each appended
a second copy, so a build trigger whose cause, asker, subject and position a record holds, and a method
entry the record holds, now exit 1 (PINNED) writing nothing. naming-leg-grades-what-python-named: the
plants' inner helpers were named after the verbs they call, `trigger` among them, and are renamed
through the naming lexicon. budget-row-not-remeasured-after-added-arms: the budget row and the leg's
ceiling are re-priced from the eighteen plants. The rest named nothing in this diff: each plant asserts
the line its arm prints, never an empty population; every write is one line through the factory's
forged-field rule; the probe verbs strip the inherited git variables through
`tools/loop/loop_witness.py#read_clean_env`; no fence opens inline. Not driven by any arm: the
`LoopError` branches of `tools/loop/loop_lib.py#read_trigger_causes`, which reads the shipped definition
alone; the cause with no rule in `tools/loop/probe.py#check_trigger_cause`, which needs a definition row
the tree does not hold; and a pin whose commit git refuses.

The checklist over the checklist commit `b1f8f9160` selected 25 classes (DERIVED: 19 by an anchor and 6
universal). One needed a change: ledger-token-wrapped-across-a-line-joins-nothing, since this ledger's
quoted refusal lines were wrapped mid-span, and each is now one line.

**Owed to the main loop at the close:** the `loop probe fixtures` leg itself, `loop definition fixtures`
over the four (DERIVED) new plants, `loop definition`, `loop transition tables`, `loop item kind`,
`loop termination`, the `testsuite counts` leg reading the new count line, the core meta-check over the
deleted pending row, the docs leg, and both New arm lines' RED-first observations.
