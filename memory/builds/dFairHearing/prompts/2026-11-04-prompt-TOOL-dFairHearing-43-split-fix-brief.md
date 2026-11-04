# Fix brief — TOOL-dFairHearing-43: gotchas.py leaves the write set

**Serves:** research TOOL-dFairHearing-43

## The prompt

> /unattended dFairHearing

— owner, 2026-11-02, the invocation that started this build run.

## The brief

### Goal
Revise `memory/builds/dFairHearing/spec/2026-11-04-spec-TOOL-dFairHearing-43.md` so its dispatch passes. Its second build pass returned a DIVERGENCE before any write: read `memory/builds/dFairHearing/build/2026-11-04-build-TOOL-dFairHearing-43-2-builder-return.md` first. `--dispatch` refuses a write set declaring `memory/gotchas/INDEX.md` together with its generator `tools/memory-tree/gotchas.py`. S8 writes the generator and S11 regenerates the index, and the spec's "Why one unit" is wrong to say no split leaves two disjoint write sets. Commit nothing; the main loop commits.

### Items
1. Remove S8, AC8 and `tools/memory-tree/gotchas.py` from this spec, and correct "Why one unit" and the inventory. Finding id 5's docstrings move to unit `TOOL-dFairHearing-44`, which another writer is speccing. The severity rule admits two batch units across disjoint write sets. Keep this unit's class record for that finding and the `gotchas.py --write` regeneration: running the generator does not edit it.
2. Fold in the pass's two notes. S2 keeps the appendix-copy instruction near `tools/workflows/tier2-review.template.js:2876` telling the synthesis agent to escape a `|` in the record's own cell, since `renderCell` encodes only the returned table. S4 names the arm at `tools/workflows/spec-audit-optin.test.sh:566`, which expects `could not be loaded`, among the arms whose text it changes.
3. Bump the rev and add one change-log line per change, each naming a section, a scope id or an acceptance id, and this brief. Leave the status header's state as it is.

### Acceptance
No path in the spec's Files touched pairs a generated index with its generator; every criterion a correct build can pass on today's tree.

### Gates
None you run.

### Non-goals
No other spec, and no code.
