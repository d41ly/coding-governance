**Serves:** journal DEPL-aPrimedIndex-1 TOOL-aPrimedIndex-6 TOOL-aPrimedIndex-7 TOOL-aPrimedIndex-8

# Build brief — aPrimedIndex, the closing review's four promotions

The main loop builds these four units INLINE, one at a time: DEPL-aPrimedIndex-1, then
TOOL-aPrimedIndex-6, -7 and -8. Their write sets are disjoint, and the inline author sequences them
rather than delegating a concurrent set. The design input of each is its spec and the finding it
cites in `reviews/2026-10-11-review-TOOL-aPrimedIndex-1-4-implementation-diff-round1.md`; the rules of
the first brief, `2026-10-11-prompt-TOOL-aPrimedIndex-1-2-build-brief.md`, hold unchanged.

1. **Route, then write.** Before a pass edits a product path, its unit is routed on the session's
   orientation card and its spec moves to INPROGRESS, which the write guard reads.
2. **Declare, then stage by name**, the run record included; never `git add -A`.
3. **No merge bar, no suite run whole.** A criterion is observed directly or through one arm run as
   a slice, red on a staged break first, then green.
4. **Run `check-arms.py --check` before committing a pass that adds an exit site** (review M8's
   procedural gap), and `gen_map.py --write` when a symbol moves.
5. **The acceptance ledger is owed** for every unit, in the grammar of `memory/HYGIENE.md`.
6. **After every commit, run the bug-class checklist** over it.
