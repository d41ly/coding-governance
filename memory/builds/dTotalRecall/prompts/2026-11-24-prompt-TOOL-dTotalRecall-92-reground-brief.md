**Serves:** journal TOOL-dTotalRecall-92
**Caused-by:** TOOL-dTotalRecall-92

# Brief — dTotalRecall: TOOL-dTotalRecall-92 re-grounded on the tree as built, before dispatch

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run, resumed on node a on 2026-11-24 by the owner's handoff.

## The brief

### Goal

Revise the spec named here in place, as a rev bump with one revision-log line naming this brief by its file stem,
so a builder can build it as written over HEAD. Where every claim already holds, change nothing and say so.

### Items

1. Read `memory/builds/dTotalRecall/prompts/2026-11-24-prompt-TOOL-dTotalRecall-92-reground-brief.md` whole: its Notes section is part of this task.
2. Apply items 1 to 6 of `memory/builds/dTotalRecall/prompts/2026-11-23-prompt-TOOL-dTotalRecall-58-reground-brief.md` to this spec, reading them
   whole, with this spec's id and path for that one's.
3. Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-92`,
   `python tools/check-spec-tokens.py --spec <path>` and `python tools/playbook/positional.py check` over the spec, and
   fix every finding naming it, save a `stale` row the main loop shrinks. Every number carries an id, a path:line,
   PINNED or DERIVED on its line, and no code line is cited bare as a file, a colon and a number.

### Acceptance

The commands name no finding of the spec; it carries the next rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dTotalRecall-92. No product code. No change to Goal or Scope intent beyond what the tree forces.

### Limitations

The status header keeps its status (`DEFERRED`). The write grant is
`memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-92.md` alone. Temporary files go under
`C:/Temp/claude/7a8436c9e3b87ce5/9067262b-db21-4497-8ba8-ef2deab46f53/scratchpad/92/`, spelled absolute. Do not commit: the main loop commits the re-ground. Each command is bounded, and a
command that runs past two minutes is run in the background and waited for, never polled.

### Reuse

The spec's §10 seam, re-verified at HEAD.

## Notes

Built since the brief of unit 58: TOOL-dTotalRecall-55 to -58, -60, -65, -66, -68, -69 (`f7011dd6f`: nothing stamped), -70 (`408d05723`, deviation 1013 of unit 38), -73 (`6d0627dd6`), -75 (`59c4af40d`), -74 (`0114569d9`: `s1-59 206422580b73 1`, `s1-46 254057fa6d5b 0`, no record written) and -87 (`073d03dd7`: `resolve_memory_root`, `run_cause_writers`, plants `kept-home-trailing-root` and `kept-root-blank`) are CLOSED. Building in order, each at the spec revision named: -76 (rev-4: its manifest sweep run by the main loop at `073d03dd7`, one red span at unit 22 closed by unit 3), -83 (rev-4: no unit 59 record), -84 (rev-3), -77 (rev-4: no second run), -78 (rev-3: worktree `gate-mc78`), -79 (rev-3), -80 (rev-4: worktree `gate-mc80`), -85 (rev-3), -86 (rev-3), -90 (rev-3), -88 (rev-4: `set_fixture_env` in `deviation_join.py`, the dWitnessedBar ask, no registration or remote), -91 (rev-3), -93 (rev-2: `has_deviation` by the file stem, `_ID.pattern`), -94 (rev-2) and -95 (rev-2: no record re-keyed, `key59 0 0`). and -89 (rev-3), -96 (rev-2) and -97 (rev-2). Take their specs as what lands, and read each commit that lands first. The run is on node a. Each unit of an order is re-grounded by its own writer: edit no other unit's spec, and name in your return any edge you need from one.

From the earlier writers, each to verify before folding. Order 39 is unit 92 alone; orders 40 and 41 are 98, 99 and 100.
- S6 and AC6: `kept-home-trailing-root` prints `read at` and `registered at` lines and exits 0; no compare line, no base
  sha. S10 and AC10: the precedent paragraph of unit 87 rev-3 states the divergence, its cites now
  `runlog_lib.py#resolve_memory_root` and `design_lib.py#main`. S23 and AC23: unit 87's is the fourth definition of the
  name; the docstring wording is this unit's.
- S6, S12, S19 to S21 and AC20 expect spec 88 rev-3 facts: a compare line, "the fixture base S15 built", a
  `TemporaryDirectory` call in `record_causes.py`, mid-line fence counts of 5 and 1 over specs 74 and 76 (now 0 and 1).
  Read spec 88 rev-4, and spec 86's table rows in its fourth section re-spelled with two backticks on 2026-11-24.
- It consumes `mc77`, `mc78` and `mc80` paths: unit 77 rev-4 makes no worktree; units 78 rev-3 and 80 rev-4 use
  `gate-mc78` and `gate-mc80`. S9's completion sweep is largely met by unit 78; its span script should accept a
  `gate-mc78 red orphan` line as not a unit and take unit 79's history order. S4's `sep` line is already in unit 79's
  script, and the base read is no longer recorded under a `Pass: none` commit.
- S18's correction is already in spec 83 rev-4. S22's `dup` key names the address: its edge overrides it (unit 93).
- The main loop may owe a background run before this unit's dispatch: name each in your return, with its exact command.

`packet.py --check dTotalRecall` runs past ten minutes on node a: spell `python tools/chain-packet.py --check
dTotalRecall`, the instrument's own `main` and bytes (TOOL-aBatchedPacket-1), where a criterion needs it. A role agent
may run no gate leg's own command, so a criterion is a probe. The held units (TOOL-dTotalRecall-8, -37, -14, -15, -26)
build nothing: an item that needs one is cut to what HEAD can observe and named in your return. Keep every S and AC,
each built, re-observed, or cut with its reason.
