**Serves:** research TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30

# Brief: the units TOOL-dDeclaredLoop-56 §8 F5 (a) re-grounds

## The prompt

> resolve all forks with recommendations - record it

— owner, 2026-11-05. TOOL-dDeclaredLoop-56 §8 F5 is resolved to (a) by the fold the brief
`2026-11-05-prompt-TOOL-dDeclaredLoop-3-owner-forks.md` drove: "re-ground each such unit so its own
pass writes the key, its tag settled where no row names its clause, and S4 only observes". That fold
revised spec 56 only, so the units the pick names still add their legs with no `enforces` key. This
brief carries the pick into them.

## The brief

### Goal

Make each unit below write its own leg's `enforces` key in its own pass, so PLAY-dOrderedCharter-7 S3
never reds a leg the unit adds, and TOOL-dDeclaredLoop-56 S4 only observes. No other design changes.

### Items

- For each of units 2, 7, 8, 11, 13, 14, 15, 21, 25, 26, 28, 29 and 30: the leg or legs the unit adds
  carry `enforces = [<tag>]` in their `[[gate_leg]]` declaration, written by the unit's own pass. Its
  scope item, its files-touched entry and one acceptance criterion say so. The criterion observes the
  leg's `enforces` and `core meta-check` green on the unit's pass.
- The tag is the one TOOL-dDeclaredLoop-56 §4 "The owed leg rows" gives: `principle.p22` for 7,
  `principle.p23` for 8, `principle.p24` for 14, `principle.p38` for 21, `principle.p20` for 25,
  `principle.p39` for 30.
- Where no `[enforcement]` row names the unit's clause (units 2, 15, 26, 28 and 29, and units 11 (P11)
  and 13 (P20), which §4's table omits), settle the tag by the rule TOOL-dDeclaredLoop-3 §8 F7's pick
  used: the principle the unit's clause carries, read from its spec's binding line and the frozen
  design. State the tag and the one-line reason in the spec. Where two principles fit equally, take the
  one the clause cites first, and say so.
- Spec 56: its §4 table gains the tags settled here for units 2, 11, 13, 15, 26, 28 and 29, so the
  table states every unit's tag. Its rows stay in place.

One writer revises the specs
`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-<n>.md` for n in 2, 7, 8, 11, 13,
14, 15, 21, 25, 26, 28, 29, 30 and 56. Write probe copies only under
`C:/Users/d41ly/AppData/Local/Temp/claude/abaae6cd36b7dece/bc821d4c-b305-40e3-bf2f-7dc1519c57f1/scratchpad/forks/dDeclaredLoop-cascade/`,
and delete nothing else there. Return, per spec: the rev it now reads; the tag it carries and whether
it was settled here; the sections moved; and its byte count.

In every spec you revise:

- Bump the **Status:** line's `rev-N` to `rev-N+1`, dated 2026-11-05, the status kept `DEFERRED`. Specs
  26 and 56 already carry a rev dated 2026-11-05 from this fold: they keep that rev, and their 2026-11-05
  §9 line gains this brief and the sections moved.
- Add one §9 line naming TOOL-dDeclaredLoop-56 §8 F5 (a), this brief, and the sections moved.
- Stay under the class cap of 49152 bytes; spec 56, already over it, grows by no more than its table cells.

### Acceptance

- `wc -c <spec>` is under 49152, or, for spec 56, grew by no more than its table cells.
- Each revised spec's **Status:** line reads a rev dated 2026-11-05, and §9 holds the new line.
- `grep -n "enforces" <spec>` prints the unit's leg declaration and its acceptance criterion in each of
  the 13 unit specs.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only
  your specs staged into it through `GIT_INDEX_FILE`, names none of your specs. Findings that only a
  `gen_build_index.py --write` render cures belong to the main loop.

### Gates

Only the memory hygiene gate and the naming lexicon, as the role allows.

### Non-goals

- No file outside the 14 specs. No commit, no stage into the real index, no deviation record, no
  `BACKLOG.md` row, no `[enforcement]` table edit.
- No fork, and no other build's spec.
