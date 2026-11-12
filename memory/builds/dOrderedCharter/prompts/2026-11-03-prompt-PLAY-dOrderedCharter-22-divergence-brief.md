**Serves:** research PLAY-dOrderedCharter-22

# Brief: unit 22's divergence — the purpose sources against the rows units 19 and 10 built

## The prompt

> dOrderedCharter

— owner, 2026-11-02, invoking `/unattended` for the build run. Unit 22's builder (run wf_e035d45b-bbf) returned
`DIVERGENCE:` before writing code. Units 19 and 10 (CLOSED) gave every one of the ten rows in
`tools/playbook/namespaces.toml` the value `purpose-source =
"memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md#design-tags"`, a section anchor
(`### [design-tags] Tags`) and no member-row field, so S2's `purpose` arm reds all ten. §4's own values would still red
at least seven at HEAD: `doc` and `unit` are prose; `tools/playbook/practices.toml`, `tools/playbook/principles.toml`,
`tools/playbook/instruction_units.py` and `.governance/instructions.toml` are not tracked yet; `tools/playbook/readers.toml`'s
rows carry no `purpose` field. `python tools/playbook/gov_tag.py check` is the bar leg `tags (the resolver's checks)`.

## The brief

### Goal

Revise spec 22 so its `purpose` arm leaves the `tags` leg green over the tree at its pass and still reds a namespace
whose purpose source is wrong, and each later unit that lands a source turns it into a graded path.

### Items

1. **The grading rule (S2, §4 "The ten purpose sources").** Decide by M3 between at least: (a) this unit writes each
   row's value in `namespaces.toml` (lifting §3's non-goal for that field alone); (b) S2 grades a markdown `#anchor`
   source as a heading the file holds; (c) a source whose file or field is not yet in the tree prints `pending` with a
   count and the unit that lands it, the way S4 prints the chain builds awaiting review, and reds once the file exists
   without the field. Combinations count. Record the loser and the observation that rejected it (M12) in §8,
   delegated. Name, per row, the value it carries at this unit's pass and the roster unit that later lands its source.
2. **`readers.toml`.** Say whether `[[reader]]` rows gain a `purpose` field in this unit or the `reader` row's source is
   a different field they already carry.
3. **Measure.** Write into §6 the count the chosen rule leaves red over the tree at HEAD (it must be 0) and the count it
   prints pending, from a probe of unit 19's and 10's built functions in `tools/playbook/tag_index.py`, never from
   `gov_tag.py check` over the tree.
4. **AC3 and AC4** observe by that probe or by fixture plants, never the tree's own run of the leg.

In the spec:

- Bump the **Status:** rev by one, dated 2026-11-03, the status kept `DEFERRED`, and add one §9 line naming this brief.
- Check your revision's §6 and §7 by eye against `tools/check-spec-tokens.py`'s `BAR` pattern, and keep §7's leg line
  naming every leg whose guard a Files-touched path trips.
- Verify every path, count and line you cite against the tree at HEAD; stay under the 47000-byte authored budget.

For the run:

- Writes stay in spec 22 and the files `gen_build_index.py --write` rewrites.
- This is an unattended run and nobody answers a question: a fork no option survives is written as an open §8 item
  with the options and the veto, and said in the return.
- Do not commit and run no check: the main loop re-renders the packet, runs the spec-token check, renders the index
  and commits.
- Scratch files go under the session scratchpad
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad`.
- Return the new rev, the §8 decision with its loser, and the red and pending counts item 3 measures.

### Acceptance

- Spec 22's §6 carries item 3's red count, and it is 0, beside the pending count.
- The Status line is one rev higher, and §9 holds the new line.

### Gates

The spec-token check, run by the main loop before the commit.

### Non-goals

No code; no spec but 22; specs 19 and 10 stay frozen.

### Limitations

The items above, "For the run".

### Reuse

`tools/playbook/tag_index.py` and `tools/playbook/namespaces.toml` as units 19, 10 and 44 built them; S4's
awaiting-review print as the pending shape.
