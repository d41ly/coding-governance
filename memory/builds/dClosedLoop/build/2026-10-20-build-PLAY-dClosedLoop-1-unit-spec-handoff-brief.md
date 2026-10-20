# Unit spec handoff brief: dClosedLoop's own unit, PLAY-dClosedLoop-1

**Serves:** research PLAY-dClosedLoop-1

The unit spec's writer renders its goal, items, acceptance, gates and non-goals from this brief record, through
`handoff.py render --input prompt=<this file>`. The owner asked to land the build on main: "Land this on main". The
landing's full bar finds that 547 record lines serve `PLAY-dClosedLoop-1` while no spec in the tree defines it.
Hygiene check 21 resolves a Serves id only against a spec H1, and dClosedLoop never wrote its own unit spec, because
its design lives in its build records.

## The prompt

Write dClosedLoop's own unit spec, PLAY-dClosedLoop-1, describing the unit as it stands, so every record that serves
it binds.

## The brief

### Goal

One Tier-2 spec, `memory/builds/dClosedLoop/spec/2026-10-20-spec-PLAY-dClosedLoop-1.md`, whose H1 defines
`PLAY-dClosedLoop-1`. It states the unit's goal, scope, non-goals, design, acceptance, gates, open questions, revision
log and reuse audit as the build's records already settle them. It points at the records that own each fact and
restates none of them.

### Items

The one spec, in the shape `memory/TEMPLATE-SPEC.md` requires of a Tier-2 spec dated 2026-10-20, as the unit brief
(`input:spec`) describes.

### Acceptance

- `memory/TEMPLATE-SPEC.md`'s Tier-2 canon holds:
  - the status header within the first five unfenced lines;
  - the ten sections in order, none empty;
  - §3's edges;
  - §7 as a list of leg names;
  - §8 F-item shaped;
  - §9 logging rev-1;
  - §10's reuse facts;
  - no skeleton placeholder.
- Every leg named in §7 is a `name` in `tools/gate-legs.json`. Every backticked path in §6 is tracked. Every
  `path:line` citation is in range.
- Every fact is cited to the record that owns it. The spec adds no decision the records do not hold.
- No unit id that no build has minted appears bare, and no other build's id leads a table cell, a heading or a list
  item.

### Gates

None of the bar's legs. The main loop runs the spec-tokens leg and memory hygiene on the staged spec.

### Non-goals

- No file but the spec: no record, README, instrument, plan or v2 edit.
- No product code, and no chain build's spec.
- No new decision. A question the records leave open goes into §8 as an open F-item, never answered by the spec.
