# Build brief — TOOL-dBriefedPass-2

**Serves:** journal TOOL-dBriefedPass-2

What the pass building this unit was handed, recorded by `--brief` and hash-joined to these bytes.

## The unit

`TOOL-dBriefedPass-2` — the unit BRIEF: a tracked record of what a building agent was handed.
Its spec is `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-2.md` at rev-4, and
that spec is the only design input. Build what it says; to diverge, bump its rev first.

## What this build already established that the pass must not re-derive

- The store is the run-state file's parked region, NOT a piece record. S1 settles it.
- The row is `park()`'s grammar, `<ISO-Z> brief · item <unit> · reason <hash> <path>`, with the
  reason line-final because `recorded_waivers` and leg check 17 both depend on that.
- The kind is `history`: in `PARK_KINDS`, deliberately NOT in `PARK_KINDS_OWED`.
- The three carrier rows for the verb land in THIS unit, not at order 5. Check 26 joins a verb to
  the driver header, `PROTOCOL.template.md` and `SKILL.template.md`, and its leg is unguarded.
- `--status` is the staleness reader. Nothing else recomputes a hash held in a parked row.

An edit made after the brief was recorded.

second edit
