**Serves:** journal TOOL-aPrimedIndex-9

# Build brief — aPrimedIndex, the lexicon render's own freshness check

The main loop builds TOOL-aPrimedIndex-9 INLINE, after the reconcile with origin/main showed the
preflight reading the lexicon render STALE on naming violations main carries. The design input is
the unit's spec; the rules of `2026-10-11-prompt-TOOL-aPrimedIndex-6-1-build-brief.md` hold unchanged.

1. **Route, then write.** The unit is routed on the session's orientation card and its spec is at
   INPROGRESS before a product path is edited.
2. **Declare, then stage by name**; never `git add -A`.
3. **No merge bar, no suite run whole.** The new arm runs inside the lexicon selftest, red on a
   staged break first, then green; AC2 is observed with `run-gates.sh --regen-check`.
4. **Run `check-arms.py --check` and `gen_map.py --write` before committing the pass.**
5. **No kit version is bumped by hand**; the lander mints it.
