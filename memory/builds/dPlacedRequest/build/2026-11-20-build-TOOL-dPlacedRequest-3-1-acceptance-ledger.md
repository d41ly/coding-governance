# TOOL-dPlacedRequest-3 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-3

The unit was built from its spec at rev-6 (PINNED) on base `537c5837e`. The loop definition gains the
entry program's five rows, `item.entry.orient`, `item.entry.place`, `item.entry.place-check`,
`item.entry.place-owner` and `item.entry.claim`, first among the item rows of `tools/loop/loop.toml`,
and loses the `[[stand-in]]` row for `item.entry.claim`. `tools/loop/loop_lib.py#PROGRAM_SEGMENTS` gains
the member `entry`, so `tools/loop/loop_lib.py#check_program` admits an `item.entry.<name>` row at the step
`none` and returns it as the program `entry`; the module docstring and the definition's header name it
beside the review and probe programs. Kickoff's Step 1 in `skills/session-kickoff/SKILL.md` takes the
branch, BASE, dirty count, worktree count and recent subjects from an `orientation —` card while HEAD
equals its `tree —` cell's BASE, and a paragraph before Step 2 states the `no-ready-card` stand-in.
`help/loop.md` gains the section "The entry items: orienting, placing and claiming a request" and names
`loop: program entry` in its `--check` paragraph. No function, file or leg was minted. The bug-class
checklist over the pass commit named `two-answers-to-one-question`: the loop kit's `tools/loop/README.md`
still listed the no-step programs as the review and probe programs alone, so its `check_program`
paragraph names the entry program too, in a path declared for it; and
`ledger-token-wrapped-across-a-line-joins-nothing`, which joined AC5's command onto one line here.

No gate, suite or bar ran in this pass, and no `--selftest`. Each criterion below was observed by a probe
of the changed definition and code on the run's node, 2026-11-20: the loop kit's own reader and checks run
over the built tree, and the staged breaks made in memory over the shipped definition by a scratch probe
that calls `tools/loop/loop_lib.py#check_program`, `tools/loop/loop_lib.py#check_probe_outcomes`,
`tools/loop/termination.py#derive_termination_composition` and `tools/loop/termination.py#check_termination`,
rather than over a copy of `tools/` on disk.

**Evidences:** TOOL-dPlacedRequest-3
- AC1 — `python loop_lib.py --check` in `tools/loop/` exited 0 and printed
  `loop: program entry · 5 item(s) · item.entry.orient item.entry.place item.entry.place-check item.entry.place-owner item.entry.claim` (DERIVED),
  and one `loop: item` line for each of the five tags.
- AC2 — `check_program` over the definition with `item.entry.place`'s `new` route pointed at
  `item.entry.nosuch` refused it, naming `the item item.entry.place routes new to 'item.entry.nosuch'`;
  with `PROGRAM_SEGMENTS` set back to the review and probe members it refused naming
  `tag 'item.entry.orient' opens no item.<step>. of a gov step`; restored, it accepted and returned the
  entry program in needs order. Observed in process; the `--check` exit over a scratch copy of `tools/`
  is the close's.
- AC3 — `python loop_items.py check` in `tools/loop/` exited 0. `read_outcome_set` printed
  `continue amend new patch repeat unit breakpoint ask none` for each placing tag, the
  `[dispositions]` set, and `agent-places declared-checked owner-places probe` for `item.entry.orient`.
- AC4 — the `--check` item lines read `role:gov-orienter · inputs from role:gov-orienter` on
  `item.entry.orient` and `item.entry.place`, never `pending`, and `inputs from item` on the command and
  owner rows; `loop: map item.entry.orient · map base` printed and the other four read `map none`; each
  entry tag's `loop: seed` line read `none`; and the `loop: probe outcomes` line refused nothing. In
  process, `item.entry.orient`'s `probe` routed to `item.probe.trigger` drew the refusal
  `routes probe to 'item.probe.trigger', not stand-in:{prefix}/loop/probe.py`.
- AC5 — `python loop_table.py move --level build --from none --item item.entry.claim --outcome claimed --fact disposition=new`
  printed `move — build · none → planning · item.entry.claim · lateral`, with no
  `stand-in` field (before the build it printed `stand-in dPlacedRequest`); `disposition=repeat` printed
  the move to `designing`; `disposition=patch` exited 1 printing `no row`; `python loop_table.py check`
  exited 0 printing no `loop: stand-in item.entry.claim` line.
- AC6 — `python termination.py check` in `tools/loop/` exited 0, its gov line reading `0 finding(s)`
  (DERIVED), no finding naming an entry item. In process over the definition's own rows: `deadline` cut
  from `item.entry.claim` drew a `wait` finding naming it; `waits` cut from it a `counted` finding on
  `item.entry.claim -> item.entry.claim`; `draws` cut from it the same `counted` finding; `deadline` cut
  from `item.entry.place-owner` a `wait` finding naming it.
- AC7 — `grep -n "now —" SKILL.md` in `skills/session-kickoff/` found Step 1's line taking HEAD, branch
  and dirty count from the replay's line, and `grep -c "never its branch or BASE" SKILL.md` printed 0
  (DERIVED).
- AC8 — `grep -n "READY — none yet" SKILL.md` found the paragraph before Step 2 naming `kickoff.runs`,
  `no-ready-card` and `## pockets` on that line.
- AC9 — `grep -n "item.entry.claim" loop.md` in `help/` found the entry items' section, its table naming
  the five tags, and `grep -n "loop: program entry" loop.md` found the `--check` paragraph naming the
  entry program.

**Size.** `skills/session-kickoff/SKILL.md` measured 20014 bytes CR-stripped after this pass (DERIVED),
against its 18432 bytes row in `tools/template-size-limits.txt` (PINNED), under `budgets.enforce = "warn"`;
it measured 19378 bytes at base (PINNED). The spec's risks line leaves a raise to the owner, so no row moved.

**Owed at the close.** The `loop definition`, `loop definition fixtures`, `loop item kind`,
`loop transition tables` and `loop termination` legs over the rows; the kickoff engine size leg, which
warns on the figure above; `manifest-check self-test`, `docs`, `help page commands`, `memory hygiene`,
`spec tokens`, `scratch-guard self-test`, `lexicon naming predicates`, `recall floor` and `recall floor arms`.
The spec declares no new arm.
