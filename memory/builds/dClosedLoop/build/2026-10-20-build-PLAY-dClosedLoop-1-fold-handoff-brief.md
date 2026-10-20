# Fold handoff brief: the whole-design audit's fold writers

**Serves:** research PLAY-dClosedLoop-1

A fold writer's handoff renders its goal, items, acceptance, gates and non-goals from this brief record, through
`handoff.py render --input prompt=<this file>`. The fold is the owner's word after the scored walk ("Fold, re-measure
after", `whole-audit.md` `[recall-scored]`), and its places come from the fold inventory.

## The prompt

Fold the whole-design audit's findings at the places your fold brief lists, as one fold script.

## The brief

### Goal

Fold the confirmed and unverified findings of the whole-design audit, at the places your fold brief (`input:spec`)
lists, into dClosedLoop's design records in the working tree. Write every edit into one fold script in your scratch
folder, which the main loop dry-runs through the build's final checks and applies. Give every place one disposition,
and bring every real design choice to the owner as a fork, unfolded.

### Items

Each place your fold brief lists, in its order. A place is one record and the clause, item, principle or section
that its findings name.

### Acceptance

- Every place has exactly one disposition (fold, fork, plant, not a defect or duplicate), with its evidence from the
  working tree.
- The fold script applies cleanly at the base commit your fold brief names: each `sub` and `insert_before` matches
  exactly once, in your own records only.
- Each fork names its question, its options and a recommendation, and the findings it rests on.
- Edits another writer's records need are listed as requests, never written.

### Gates

None run by you. The main loop dry-runs your script on a copy through the build's nine final checks before it applies.

### Non-goals

- No product code: nothing under `tools/`, `skills/`, `coding-governance-agents.template.md` or `WIRE-INTO-PROJECT.md`,
  and no `AGENTS.md` re-render.
- No unit specs for the chain builds, and no status change to an existing build or ask.
- No edit to the audit's own records: its reports, returns, briefs, the round record and the fold inventory.
- Nothing read from, or written to, the sealed copy.
