**Serves:** research KICK-dKeptSession-8

# Brief — dKeptSession: KICK-dKeptSession-8's hands-off to KICK-dKeptSession-44, re-stated

## The prompt

> /unattended dKeptSession

## The brief

### Goal

KICK-dKeptSession-44 rev-6 moved its S10 observation: unit 8's fixture stubs the policy reader, so `card.pointers` never
reaches it, and the observation is now a row in the `pointers-at-transitions` plant that reads the tree's card file. Its
§ consumes-from edge from this unit now reads "§8 F3 (b)'s read of the tree's card file, which S10 observes". This spec's
hands-off bullet to KICK-dKeptSession-44 still says "the `actions.free` plants, run under both `card.pointers` values by
the batch's S10", which no longer describes what 44 consumes. This spec was re-grounded at rev-6; revise only what the
items below name.

### Items

1. F-edge: rewrite the hands-off bullet to KICK-dKeptSession-44 so its payload names what 44 rev-6's consumes-from edge
   names (§8 F3 (b)'s read of the tree's card file, observed by 44's S10), keeping its id. Probe whether any other clause,
   criterion or §8 text of this spec still promises the plants run under both `card.pointers` values for 44's sake; where
   one does, say whether it stays true for this unit's own criteria (AC2, AC6, AC10) and keep or narrow it accordingly.
2. Bump the spec one rev, with one revision-log line naming this brief by its file stem. Cite code by `path#symbol`, pin
   every figure with DERIVED or PINNED, write no `[..](..)` link shape outside the generated records table, keep within
   the live-spec size cap, and leave no fork open.

### Acceptance

`bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`, a plain
`bash tools/memory-tree/check-memory-hygiene.sh --only 2`, `python tools/check-spec-tokens.py --spec <path>`, a PLAIN
`python tools/playbook/writing_practice.py check pinned-facts` and
`bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-8` report nothing for the spec.

### Gates

The memory hygiene gate (`--only 12,25 --spec`, and `--only 2`), the spec-token checker, the pinned-facts check and the
driver's `--check-specs`; no other.

### Non-goals

No product code, no commit, no index render, and no spec other than KICK-dKeptSession-8's (other writers may be revising
other specs at the same time; read them, never edit them). Read files; edit only the spec, in the run worktree.
