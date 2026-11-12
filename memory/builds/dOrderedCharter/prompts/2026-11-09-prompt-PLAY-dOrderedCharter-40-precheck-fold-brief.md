**Serves:** research PLAY-dOrderedCharter-40

# Brief: spec 40 — fold unit 37's hand-off and pre-check every claim against HEAD

## The prompt

> why are the specs being reviews (and 11 times at that) instead of building?

— owner, 2026-11-09. Specs are now checked against HEAD while the unit before them builds, so their fixes fold before their builder
starts rather than after a hand-back.

## The brief

### Goal

Revise spec 40 so a builder can build it as written over this tree, once unit 37 lands as its spec rev-7 says.

### Items

1. **Where you write.** A unit is building, so edit only this scratch copy and write nothing under the repository:
   `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold40/2026-10-24-spec-PLAY-dOrderedCharter-40.md`
2. **Unit 37's hand-off changed.** Spec 37 rev-7, committed in this tree, lands three reference pages at its pass and moves the units
   reference row, its page and every row's `unit` field to a later commit after this unit's gov unit rows are tracked. Spec 40's scope,
   its criterion that says the reference check exits 0 over four pages, and its consumes-from text naming the four reference rows no
   longer hold at this unit's pass; `tools/playbook/references.toml` may leave Files touched if this unit only reads it. Fold them, and
   mirror the edge.
3. **Unit 33's later commit.** Unit 33's fork F5 lands the `unit` class row in `tools/govkit/surface-classes.toml` and the `unit` row in
   `tools/govkit/usage.toml` once a gov unit row is tracked, which this unit writes first. Say whether this unit's pass or a commit right
   after it carries those two rows, under whose dispatch, and with which of unit 33's criteria they let the close observe.
4. **Pre-check every claim against HEAD.** For every symbol, file, row, signature, return shape, key or count the spec names, read the
   code; probe with `python -I` in a scratch folder of your own where a read cannot settle it. Units landed since the spec's last
   revision include 29, 23, 32, 33, 46, 35, 36 and 34, which changed the overlay, its readers, the composer, the renderer and the charter.
   PLAY-dOrderedCharter-31 is parked and will not land in this run, so nothing in this spec may rest on it.
5. **Every reader claim is a grep**, at HEAD, for anything this revision moves or retires.

Resolve each choice under the fork rule and record it in section 8.

In the spec:

- Bump the **Status:** rev by one, dated 2026-11-09, status kept `DEFERRED`, with one history line naming this brief.
- Each listed `path:line` citation stays byte for byte unless an item above corrects it, and new text cites code as `path#symbol`,
  outside the acceptance bullets, which spell plain tracked paths and never a file not yet tracked. New text names a section in words,
  and a check by what it checks. A sha written in section 2 stays out of backticks, and a Readers clause names readers only, never the
  command that found them. Every new fact is pinned, keyed or marked PINNED or DERIVED; name a unit by its id. Every function name it
  mints passes `python tools/lexicon/lexicon.py --suggest <name> --as py.function`.
- Any retirement word in section 2 owes its Readers clause.

### Acceptance

- Spec 40 builds as written over HEAD with unit 37 landed, every edge it gains is named in your return for the main loop, and each
  change has a history line.
- Your return names the pick for each item, and any fork left open because its surviving option trips the second or third veto.

### Gates

None run: this is a scratch edit. The main loop sweeps the spec before its dispatch.

### Non-goals

- No code. No edit outside the scratch copy.
