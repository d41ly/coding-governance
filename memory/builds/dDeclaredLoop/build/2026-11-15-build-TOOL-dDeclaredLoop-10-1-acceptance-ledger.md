# TOOL-dDeclaredLoop-10 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-10

No merge bar, no self-test suite and no gate leg ran in this pass, and neither `check --selftest` of
`loop_table.py` nor that of `loop_transition.py`, the two legs' commands, was run as a command. The
criteria were observed on node `d` (win32) by probes of the unit's own code: `loop_table.py move` over
the shipped tables, the `python -c` call AC1 spells, the `backward-rows`, `skip-backward`, `default`,
`subset-log` and `field` plants of `loop_transition.py` run one at a time, a `python -c` liveness probe
of the `direction stored` counter, and the `grep` commands AC5 spells. The naming lexicon's `--check`
ran and passed.

Timing, for the budget row: the `backward-rows` plant alone took 12 s PINNED 2026-11-15 by direct CLI.

Liveness of the `direction stored` counter: with the trailer renderer patched to append a
`direction=` field and each record's stand-in value patched to hold the word, the `backward-rows`
plant printed `loop: fixture · direction stored · 6 trailer(s) · 6 record(s)`, so a zero is a reading
and not a counter that cannot move.

Owed to the close: every leg the spec's section 7 names; the `loop transition tables` leg with the
RED-first observation its `New arm:` line names, staged by `derive_direction` reading `STEP_TAGS` so
the `direction-order` case prints `forward`; the `loop transition record` leg with the RED-first
observation its `New arm:` line names, staged by exempting a backward move from the channel check so
the `skip-backward` plant exits 0; and the budget row read against the leg's own timing.

**Evidences:** TOOL-dDeclaredLoop-10
- AC1 — `move — build · building → testing` — `loop_table.py move --level build --from building --item item.build.exit --outcome recorded`
  printed `move — build · building → testing · item.build.exit · stand-in dScopedBuild · forward`;
  the testing case on `code-miss` ended `· backward`, the pause from building ended `· lateral`, and the
  unit move printed `move — unit · none → designed · item.design.ready · stand-in dIndexedDesign` with no
  direction field. The `python -c` call with building's and testing's orders swapped printed
  `backward`; unswapped, the same call printed `forward`. The `direction-order` selftest case is owed
  to the close.
- AC2 — `loop: fixture · records 6` — `loop_transition.py --fixture --plant backward-rows` exited 0;
  each of its `loop: fixture · trailer` lines, the B13, B8 and B6 moves' included, carried `build=tFix`,
  `item=`, `sha=` and `stand-in=` and nothing more; it printed one `transition — tFix · ` line and one
  `loop: recorded · ` line per move, B13's reading `loop: recorded · testing -> building · backward`,
  and its `check` printed no finding.
- AC3 — `loop: transition · commit <sha8> · log · the move designing -> planning owes a record, and none holds it`
  — `loop_transition.py --fixture --plant skip-backward` exited 1 printing that line with the B6
  move's commit, the check counting six trailers against five records.
- AC4 — `loop: fixture · direction stored · 0 trailer(s) · 0 record(s)` — the `backward-rows` plant
  printed it; its first `loop: fixture · read trailer` line opened `designing -> planning` and ended
  `· backward`, its last opened `planning -> designing` and ended `· forward`. The `subset-log` and
  `field` plants' read lines gained the trailing `· forward` and still opened as before.
- AC5 — `grep -n 'backward' help/loop.md` — found the sentence that a backward move is recorded
  through the same writer and channels as a forward one, in the section on recording a build's move;
  `grep -n 'skip-backward' help/loop.md` found the plant in that section's case list.
