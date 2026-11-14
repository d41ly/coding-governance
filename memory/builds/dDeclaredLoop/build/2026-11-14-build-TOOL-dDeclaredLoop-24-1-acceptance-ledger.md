# TOOL-dDeclaredLoop-24 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-24

No merge bar, no self-test suite and no gate leg ran in this pass, and `check --selftest` of
`loop_items.py`, the new leg's command, was not run as a command. The criteria were observed on node `d`
(win32) by probes of the unit's own code: `check` over the tree, each plant run one at a time as
`--fixture --plant <case>`, the `new` verb's refusals over the tree, the `compose` verb over the tree,
the step gate's class functions loaded through `step_gate.load_class_callable`, an in-process kind-row
grade through `core.check_kind_row`, and `run_selftest_cases` driven in process over five of the
self-test's cases on one shared scratch, which printed PASS for each and exit 0.

Timing, for deviation 244 and the budget row: a `git add` of the whole tool root into a scratch took
26 s on this node, PINNED 2026-11-14, against about 3 s for the five kits the check reaches, PINNED
2026-11-14. `check` and its 21 plants run one at a time, each plant building its own scratch, took
118 s in all, PINNED 2026-11-14, the proxy reading the `loop item kind` budget row prices at 177.

RED observed in this pass: every refusing plant exits 1 with the refusal it owes (below), and the `new`
verb, given an actor kind outside the set and an input naming no layer, exited 1 and left the
definition's bytes equal to a copy taken before, checked by `cmp`. The rev-4 read this unit replaces,
`git show HEAD:` of the definition, was observed refusing the first render by the first dispatch's
builder return; the `definition-uncommitted` plant stages that state and the render now refuses nothing.

Owed to the close: every leg the spec's section 7 names; the `loop item kind` leg itself, with the
RED-first observation its `New arm:` line names, the failing case staged by the `repo-cycle` plant;
govkit selftest's `check_step_gate_fixture` with the `item` case, its other `New arm:` line, and its
`OC8 AC4 a default apply into a scratch target exits 0` arm, which `definition-uncommitted` stands in
for here; AC2's `core.py kinds` and `core.py meta-check`; the `docs` leg over the new anchors and the
re-rendered kinds page; and a budget re-priced from the main loop's first reading of the leg alone.

**Evidences:** TOOL-dDeclaredLoop-24
- AC1 — `item.test.demo` — `--plant factory` ran `core.py new item demo ...` in its scratch, which
  exited 0 printing `loop: new · appended item.test.demo`; `check` over the committed result exited 0;
  the same `new` again exited 2 printing `the definition declares item.test.demo already`.
- AC2 — `principle.p16` — `core.check_kind_row` over the `kind.item` row returned no red and conforms,
  and `core-pending.txt` holds no `kind.item` row; a `python -c` read of the `loop item kind` row of
  `tools/gate-legs.json` printed its `enforces` as `principle.p16`. `core.py kinds` and `core.py
  meta-check` are gates and were not run; owed to the close.
- AC3 — `repo-cycle` — `--plant repo-cycle` exited 1 naming the cycle item.test.adopter.cycle-a ->
  item.test.adopter.cycle-b -> item.test.adopter.cycle-a; `--plant repo-unresolved-need` exited 1
  naming the need item.test.adopter.nosuch, which no row declares.
- AC4 — `version-stale-input` — `--plant repo-input-unproduced` exited 1 naming the input
  layer.memory:record-kind.acceptance@1; `repo-input-produced` exited 0 printing `loop: record inputs ·
  1 joined`; `version-unbumped` exited 1 naming record-kind.acceptance, its pinned c24a6acc against the
  recomputed 2f3b42fb; `version-bumped` exited 0 printing `loop: record-version record-kind.acceptance ·
  2 · 2f3b42fb`; `version-stale-input` exited 1 naming the input still at @1.
- AC5 — `supersede-floor` — `--plant patch-witness` exited 1 naming the row and `fixed by
  principle=principle.p2`, `patch-outcomes` naming `principle=principle.p24`, `supersede-floor` naming
  the fixed row item.test.verdict and `principle=principle.p2`, and `supersede-exit` naming the fixed
  row item.build.exit and `principle=principle.p20`.
- AC6 — `exclude-breakpoint` — `--plant exclude-needed` exited 1 naming item.test.verdict, which still
  holds item.test.select in its needs; `exclude-breakpoint`, excluding item.test.flakes, exited 1
  naming the policy key review.breakpoints.
- AC7 — `needs remove · widens` — `--plant patch-remove-need` printed that patch line, `patch-add-need`
  printed `needs add · narrows`, and `patch-routes` printed `routes add · widens` beside `routes remove ·
  narrows`, each exiting 0.
- AC8 — `RED item:` — in a scratch clone holding this pass's diff, committed, `step_gate.py --fixture
  --plant item` exited 1 printing `RED item:item.plan.input`, with `--with-row` exited 0, one vanished
  and one witnessed, and `--plant content-edit` exited 0 with none vanished. The govkit selftest arm
  is owed to the close.
- AC9 — `amended-cycle` — `--plant amended-cycle` printed `needs add · narrows` for the amends and
  exited 1 naming the cycle item.test.merge -> item.test.verdict -> item.test.select -> item.test.merge.
- AC10 — `kind.item` — `grep -n '"loop item kind"' tools/gate-legs.json` found the leg row, its argv
  naming `loop_items.py`, `check` and `--selftest`; `grep` found `kind.item` in `help/loop.md` and
  `compose` in `help/overlay-rows.md`.
- AC11 — `exit-unfixed` — `--plant exit-unfixed` exited 1 printing `the step step.build exit
  item.build.exit holds no [[fixed-row]] in tools/loop/item-schema.toml`.
- AC12 — `schema-absent` — `--plant schema-absent`: the scratch's `compose --kind item` exited 2
  printing `unarmed` and `tools/loop/item-schema.toml, its schema, is absent`, `check` exited 2, and the
  `read_kind_rows` probe printed no item row.
- AC13 — `loop: items composed · 61 row(s) · 0 repository` — `python loop_items.py check` in
  `tools/loop/` exited 0 printing that line and two `loop: record-version` lines, PINNED 2026-11-14.
- AC14 — `definition-uncommitted` — `--plant definition-uncommitted`: the scratch's `compose` exited 2
  printing `unarmed` and `HEAD holds no tools/loop/loop.toml`, `check` exited 2, the
  `render_delta_report` probe returned no refusal and 0 `gov:item` lines, and after a commit of the
  staged definition it printed 61, the count of its item tables, PINNED 2026-11-14.
