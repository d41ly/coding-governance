# memory/archive/ledger/ — the RETIRED sharded session ledger

**RETIRED.** This directory is where the authored per-node session ledger came to rest when the
memory rework (build `aMendedLedger`) drained `memory/project/` of its session machinery. Nothing
here is live. Work state is now DERIVED — from each build README's front matter plus its specs'
status headers — and rendered into `memory/LIVE.md` and the `memory/ledger/` month shards by
`tools/memory-tree/gen_build_index.py`. Read those, not this.

The three shards (`a.md`, `b.md`, `c.md`) land beside this README in U2 of that build, moved
byte-identically out of `memory/project/in-flight/`. This README is written in U1, one unit ahead of
them, so the protocol prose below is never absent from the tree: its sole carrier,
`memory/project/IN-FLIGHT.md`, is deleted in U1.

## The retired protocol, preserved

One file per node under `in-flight/`. **Write ONLY your own node file** (`in-flight/<tag>.md`) so the
ledger never conflicts on merge; **read all** of them for the who-is-touching-what / slug-collision
scan. Row: node · slug · branch · streams · status; status in {in-flight | merged:<sha>}. Self-prune
your own merged rows once the sha is an ancestor of `main`.

That is the whole of it: the write-own/read-all rule that kept the ledger merge-free, the five-field
row shape, the two-token status vocabulary, and the self-prune trigger keyed on ancestry rather than
on a session remembering to tidy up.

## Why it retired

The rule's own justification was that a shared mutable index forces a conflict on every land. That
question now has two better answers, and carrying all three would be three answers to one question:
the generated build index derives status from sources nobody edits by hand, and the row-keyed merge
driver resolves the two indexes that must stay authored. What the ledger uniquely held — worktree
names, review ids and session narrative — is why the shards are relocated here rather than deleted.
