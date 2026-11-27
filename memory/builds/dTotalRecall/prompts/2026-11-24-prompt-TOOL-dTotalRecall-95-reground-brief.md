**Serves:** journal TOOL-dTotalRecall-95
**Caused-by:** TOOL-dTotalRecall-95

# Brief — dTotalRecall: TOOL-dTotalRecall-95 re-grounded on the tree as built, before dispatch

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run, resumed on node a on 2026-11-24 by the owner's handoff.

## The brief

### Goal

Revise the spec named here in place, as a rev bump with one revision-log line naming this brief by its file stem,
so a builder can build it as written over HEAD. Where every claim already holds, change nothing and say so.

### Items

1. Read `memory/builds/dTotalRecall/prompts/2026-11-24-prompt-TOOL-dTotalRecall-95-reground-brief.md` whole: its Notes section is part of this task.
2. Apply items 1 to 6 of `memory/builds/dTotalRecall/prompts/2026-11-23-prompt-TOOL-dTotalRecall-58-reground-brief.md` to this spec, reading them
   whole, with this spec's id and path for that one's.
3. Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-95`,
   `python tools/check-spec-tokens.py --spec <path>` and `python tools/playbook/positional.py check` over the spec, and
   fix every finding naming it, save a `stale` row the main loop shrinks. Every number carries an id, a path:line,
   PINNED or DERIVED on its line, and no code line is cited bare as a file, a colon and a number.

### Acceptance

The commands name no finding of the spec; it carries the next rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dTotalRecall-95. No product code. No change to Goal or Scope intent beyond what the tree forces.

### Limitations

The status header keeps its status (`DEFERRED`). The write grant is
`memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-95.md` alone. Temporary files go under
`C:/Temp/claude/7a8436c9e3b87ce5/9067262b-db21-4497-8ba8-ef2deab46f53/scratchpad/95/`, spelled absolute. Do not commit: the main loop commits the re-ground. Each command is bounded, and a
command that runs past two minutes is run in the background and waited for, never polled.

### Reuse

The spec's §10 seam, re-verified at HEAD.

## Notes

Built since the brief of unit 58: TOOL-dTotalRecall-55 to -58, -60, -65, -66 (`17aac82e4`), -68 (`7252440fd`), -69 (`f7011dd6f`: nothing stamped), -70 (`408d05723`, deviation 1013 of unit 38), -73 (`6d0627dd6`: `resolve_kept_home`, `check_kept_home`), -75 (`59c4af40d`: `last-body-change` advanced to `8b31081ac`) and -74 (`0114569d9`: `s1-59 206422580b73 1`, `s1-46 254057fa6d5b 0`, no record written) are CLOSED. Building in order, each at the spec revision named: -87 (rev-3: `resolve_memory_root(conf)`, `run_cause_writers(root)`), -76 (rev-4: the manifest sweep is the main loop's; plants `kept-row-gained` and `kept-base-unresolved` cut), -83 (rev-4: no unit 59 record), -84 (rev-3), -77 (rev-4), -78 (rev-3), -79 (rev-3), -80 (rev-4), -85 (rev-3), -86 (rev-3) and -90 (rev-3). Take their specs as what lands, and read each commit that lands first. The run is on node a. Each unit of an order is re-grounded by its own writer: edit no other unit's spec, and name in your return any edge you need from one.

From the earlier writers, each to verify before folding. Order 37 is units 88, 91, 93, 94 and 95.
- Unit 83 rev-4 finds no unit 59 departure owed, and unit 90 rev-3 writes no record of unit 59, so nothing of that kind is there to re-key: `key59` prints `key59 0 0` over the build folder. Where the item has nothing to act on, re-observe it.

`packet.py --check dTotalRecall` runs past ten minutes on node a: spell `python tools/chain-packet.py --check
dTotalRecall`, the instrument's own `main` and bytes (TOOL-aBatchedPacket-1), where a criterion needs it. A role agent
may run no gate leg's own command, so a criterion is a probe. The held units (TOOL-dTotalRecall-8, -37, -14, -15, -26)
build nothing: an item that needs one is cut to what HEAD can observe and named in your return. Keep every S and AC,
each built, re-observed, or cut with its reason.
