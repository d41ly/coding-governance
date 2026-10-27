**Serves:** research TOOL-dFurnishedOrders-50 TOOL-dFurnishedOrders-51 TOOL-dFurnishedOrders-52

# Round-6 fix brief — dFurnishedOrders, what the checks found in the round-6 promotions

## The prompt

Fix the findings listed in the brief below, in the promoted specs they name.

## The brief

### Goal

The round-6 spec audit (`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-47-spec-audit-round1.md`)
promoted its findings into units 50 to 52, which the disposal stage authored. The main loop then ran
`python tools/check-spec-tokens.py` (six lines, on units 50 and 52) and the memory-hygiene gate (check 13, on unit
50). Fix each in the spec it names and nothing else. Units 50 to 52 are new and uncommitted, so they stay `rev-1`
and owe no §9 line. Every rule of the spec brief
`memory/builds/dFurnishedOrders/prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md` still binds.

### Items

- **R1 · foreign ids read as claimed (hygiene check 13).** TOOL-dFurnishedOrders-50's table near its line 140 opens
  four rows with `TOOL-aOrientedCast-28`, `DEPL-aScoutedSeam-1`, `KICK-aScoutedSeam-1` and `TOOL-aScoutedSeam-3` in
  the first cell, and check 13 reads an id leading a table cell as one this build DEFINES, so each id reads as
  claimed by two build folders. Restructure the table so no row's first cell is another build's unit id: lead with
  the spec's path or the leg, and move the id to a later cell or into prose. Grep the other two promoted specs for
  the same shape and fix any you find.
- **R2 · legs a files-touched path trips, absent from §7's leg line (`[guards]`).** TOOL-dFurnishedOrders-50 and
  TOOL-dFurnishedOrders-52 each name `tools/codebase-map/gen_map.py` among Files touched; add `codebase-map kit
  selftest`, `codebase-map gate coverage` and `codebase-map adopter e2e` to each spec's §7 leg line, verbatim, as
  `tools/gate-legs.json` spells them.

### Acceptance

`python tools/check-spec-tokens.py` prints no line naming a `memory/builds/dFurnishedOrders/spec/` file, and the
hygiene gate prints no check-13 line naming dFurnishedOrders, both run by the main loop on the real tree after you
return.

### Gates

The memory-hygiene gate's checks 2, 12 and 25, which your role admits, in a throwaway clone under your scratch path
with every spec of the folder committed there; the main loop re-runs the spec-token check and the whole gate.

### Non-goals

Any new unit or new design, and any edit outside `memory/builds/dFurnishedOrders/spec/`. You commit nothing and
render no index: the main loop commits once after you return.
