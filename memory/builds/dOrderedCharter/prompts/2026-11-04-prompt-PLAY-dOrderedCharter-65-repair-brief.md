**Serves:** research PLAY-dOrderedCharter-65

# Brief: repair unit 65 — three kind tags whose name is a namespace word

## The prompt

> execute keeping the build unattended

— owner, 2026-11-03. The main loop's lint after unit 7's pass found the tags leg red six times:
- Unit 7's `tools/playbook/kinds.toml` mints `kind.kit`, `kind.layer` and `kind.practice`.
- The tag grammar's shape arm refuses each, saying its first segment is a namespace word. The lexicon name-check
  refuses the same three.
- Unit 7 is CLOSED, so the fix is a repair unit (BUILD-METHOD, a repair corrects what a closed unit built).

## The brief

### Goal

Write the spec for PLAY-dOrderedCharter-65, a repair unit at order 11 that lands after unit 64 and before unit 53,
so that `python tools/playbook/gov_tag.py check` exits green over the tree.

### Items

1. **The fork.** Choose how the three kinds are named, by the build method's fork rule. The loser and the
   observation that rejected it go in the spec's fork record, delegated. Candidates include:
   - renaming the three tags to a segment no namespace owns, for example `kind.kit-descriptor`;
   - a grammar rule that lets the `kind` namespace name a namespace word;
   - another option.
   Test each candidate against the shape arm, the lexicon name-check and every reader of the kind tags.
2. **Readers.** Every reader of the three tags changes in the same pass. Find them with `git grep` at HEAD:
   `kinds.toml`, `core.py`'s kind gates and its plants, `core-pending.txt`, any principle or edge naming them, the
   help pages, and the tag index's cached rows.
3. **Acceptance by probe.**
   - A plant or fixture shows the old spelling red and the new one green.
   - `gov_tag.py check` over the tree reports 0 red, run as a probe of this unit's change and never as the tags
     leg's exact argv.
4. **Section 7** names every leg whose guard a Files-touched path trips (`check-spec-tokens.py --legs-for`).
5. **Shape.** Follow `memory/TEMPLATE-SPEC.md`, with unit 63's spec as the precedent.
   - Status `DEFERRED · rev-1 · 2026-11-04 · node d · Tier-2 · base <HEAD short sha> · streams playbook · order 11 · advances PLAY-dOrderedCharter-38`.
   - `closes` nothing, and `**Derived:** PLAY-dClosedLoop-2`.
   - Edges are `none`.
   - Any section-2 item that retires a name carries a `**Readers:**` clause. Its by-name half names readers by
     plain tracked path, with no pin and no symbol form.

In the spec:

- New text names a section in words. It never uses the section-sign form, the method-rule form or the hygiene
  check-number form, and it cites no `path:line`. Cite code as `path#symbol`.
- Stay under the 47000-byte authored budget.

For the run:

- A unit is building in the tree, so write the spec to the scratch path
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold3/2026-11-04-spec-PLAY-dOrderedCharter-65.md`.
  The main loop moves it in.
- Do not commit and run no check beyond read-only probes.
- Return the fork decision with its loser, the acceptance criteria and Files touched.

### Acceptance

- The spec exists at the scratch path, with every item above covered.

### Gates

The spec-token check and the memory-hygiene hook, at the main loop's commit.

### Non-goals

- No code.
- No other spec.
- No change to the tag grammar beyond what the fork picks.

### Limitations

The items above, "For the run".

### Reuse

`tools/playbook/tag_index.py`'s shape arm; unit 7's `tools/playbook/kinds.toml` and `tools/playbook/core.py`;
unit 63's spec.
