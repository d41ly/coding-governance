**Serves:** research PLAY-dOrderedCharter-64

# Brief: repair unit 64 — the revision-scope arm accepts a section named in words

## The prompt

> execute keeping the build unattended

— owner, 2026-11-03. The second drift fold found that two gates in this repository disagree about one line.
- The template-conformance check of `tools/memory-tree/check-memory-hygiene.sh` passes a revision entry only when it
  holds the section-sign form followed by a digit, or an S or AC id. That is the `rs_has` predicate in its rev-scope
  arm.
- Unit 26's positional check grades the section-sign form, and unit 53's per-line rule will red every such line added
  after the positional check landed.
- So a revision that changes only sections, with no S or AC id, cannot satisfy both. Spec 4's rev-4 entry hit this and
  carries the section-sign form for now.

## The brief

### Goal

Write the spec for PLAY-dOrderedCharter-64, a repair unit at order 11 that lands before unit 53. It must:
- widen the rev-scope predicate so it also accepts a section named in words: `section <n>`, case-insensitive, `<n>`
  a digit run;
- rewrite spec 4's rev-4 entry into words in the same pass.

### Items

1. **One mechanism.**
   - Widen the predicate in `check-memory-hygiene.sh`, and in any copy or template the memory-tree kit ships of it.
     Find them with `git grep -n rs_has`.
   - Keep the refusal text byte for byte; the existing arm greps it.
   - The new form adds no positional reference anywhere.
2. **Acceptance by fixture.** Use the kit's own fixture style: the rev-scope arms in `check-memory-hygiene.test.sh`,
   under the `TOOL-aJoinedCanon-1` rev-scope comment.
   - An entry naming only `section 7` passes.
   - An entry naming no section and no id still reds with the same refusal.
   - An entry naming `sections` with no digit still reds.
   - Each case is observed by a direct run of the script over a scratch fixture, never by running the suite.
   - The suite's new arm goes on a `New arm:` line in section 7.
3. **The spec 4 rewrite.** The pass rewrites spec 4's rev-4 entry from the section-sign form into words, and drops
   spec 4's history line that said the form waits on this unit.
4. **Section 7** names every leg whose guard a Files-touched path trips (`check-spec-tokens.py --legs-for`).
5. **Shape.** Follow `memory/TEMPLATE-SPEC.md`, with unit 63's spec as the house precedent for a repair unit.
   - Status `DEFERRED · rev-1 · 2026-11-04 · node d · Tier-2 · base <HEAD short sha> · streams playbook · order 11 · advances PLAY-dOrderedCharter-38`.
   - `closes` nothing, and `**Derived:** PLAY-dClosedLoop-2`.
   - section 3 Edges is `none`.

In the spec:

- New text names a section in words, never in the section-sign form, the method-rule form or the hygiene
  check-number form, and cites no `path:line`. Cite code as `path#symbol`.
- Stay under the 47000-byte authored budget.

For the run:

- A unit is building in the tree, so write the spec to the scratch path
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold3/2026-11-04-spec-PLAY-dOrderedCharter-64.md`.
  The main loop moves it in.
- Do not commit and run no check.
- Return the spec's acceptance criteria and its Files touched.

### Acceptance

- The spec exists at the scratch path, with every item above covered.

### Gates

The spec-token check, run by the next `--dispatch` after the spec moves in.

### Non-goals

- No code.
- No other spec.
- No change to which entries the arm grades: the cutoff, the rev-2-and-later rule and per-entry joining all stay.

### Limitations

The items above, "For the run".

### Reuse

The rev-scope arm in `tools/memory-tree/check-memory-hygiene.sh` and its fixture arms; unit 63's spec.
