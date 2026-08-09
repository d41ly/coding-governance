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

## The retirement record

**Retired 2026-08-09.** All three shards now sit beside this README:

| shard | node | data rows | moved from |
|---|---|---|---|
| `a.md` | `a` (daily-agent) | 6 | `memory/project/in-flight/a.md` |
| `b.md` | `b` (agent5) | 3 | `memory/project/in-flight/b.md` |
| `c.md` | `c` (agent-0) | 2 | `memory/project/in-flight/c.md` |

Each moved byte-identically — `git mv`, so git records a 100% rename and the blob is never re-read
and never re-normalised. `memory/project/in-flight/` went with them, its `.gitkeep` deleted in the
same commit, and `memory/project/` now holds only its five waiver registries.

**What retired them.** The owner ratified F2 and F5 of the build's master spec as **retire
everywhere** — not merely here, but in the product too: the memory-tree kit stops scaffolding a
ledger for adopters, and the governance playbook stops mandating one. Those two forks were one
decision taken twice, because a rule the playbook mandates and the kit refuses to scaffold is a
contradiction an adopter discovers on their first hygiene run.

**These files are frozen.** They are under `memory/archive/`, which is append-only territory: the
hygiene gate's `APPEND_ONLY_ERE` at `tools/memory-tree/check-memory-hygiene.sh:47` names
`archive/` alongside `DECISIONS.md` and `decisions/`. Nothing here is edited, corrected or pruned.
That freeze is also why every path in this README is written in backticks rather than as a relative
link: check 2's link scan exempts `archive/`, so a link that rotted under this directory would rot in
silence, and an unpoliced link is worse than a plain path a reader has to resolve themselves.

**Where work state lives now.** Read the GENERATED index, never these shards: `memory/LIVE.md` for
what is open, and `memory/ledger/<month>.md` for the month's landings. Both are rendered from build
README front matter plus spec status headers by `tools/memory-tree/gen_build_index.py`, and hygiene
check 9 byte-compares the committed render against a fresh one, so a hand edit reds the bar. Where
one of these retired rows and the derived index disagreed, the derived index was right in every
case — which is the measurement that made retirement safe rather than merely tidy.

**The drift probe that read them.** `ledger_rows_contradicting_git` still ships in the kit engine and
still reads `<memory_root>/project/in-flight/*.md`, because an adopter who keeps a ledger keeps a
working signal. In THIS repo its population is now empty on purpose, so it is declared in
`tools/drift-audit/drift_signals.py`'s `DECLARED_EMPTY` and its pin of 4 is retired: a pin over an
empty population is a ratchet that can never turn. The declaration is not a muzzle — put one row back
under `memory/project/in-flight/` and the probe goes live and scores again, which
`tools/drift-audit/selftest.py` asserts in both directions rather than leaving to trust.
