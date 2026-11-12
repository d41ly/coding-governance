**Serves:** research PLAY-dOrderedCharter-15

# Brief: unit 15's divergence — a retired row that `show` never reads, and five gaps beside it

## The prompt

> execute keeping the build unattended

— owner, 2026-11-03. Unit 15's builder (run wf_d860e651-2fa) returned `DIVERGENCE:` before writing code, against rev-9 at
`0ae7b853b`. The tree is clean.

## The brief

### Goal

Revise spec 15 so each conflict below is resolved and its builder can build it as written.

### Items

1. **The redirect.** S9, AC11 and fork F5 say `gov_tag.py show` already prints a `retired` row's text. It does not.
   - The `show` branch of `tools/playbook/gov_tag.py#run_kit_verb` reads rows from `tools/playbook/tag_index.py#resolve_address`,
     which reads only `DEFINE_KINDS`, so `show practice.old` resolves to no row and exits 1.
   - An extractor-only build cannot satisfy AC11: minting the tag as a define kind trips `check_retired`, and widening
     `resolve_address` makes a retired tag resolve as live. `where`, the pointer check and the edge resolver read through it.
   - Say that `show` alone falls back to `retired` rows when `resolve_address` returns none, printing kind `retired` and
     the row's text. State its exit code, and whether the subtree slice applies. `resolve_address`, `where` and both
     resolvers stay on `DEFINE_KINDS`.
   - Add `tools/playbook/gov_tag.py` to Files touched, and `tools/playbook/tag_index.py` if the read lands there.
   - Correct F5's reason for rejecting (c): (a) and (c) both need a `show` change, and (a) still wins on `INDEX_SCHEMA`.
   - Update S9's Readers clause, and name `run_kit_verb` in place of its stale line citation, beside it as the stable form.
2. **The record's field shape.** S7 says each field is a `**<Field>:** <value>` line, but
   `tools/memory-tree/build_records.py#write_record` writes and reads only `- **Key:** value` bullets, and AC9 needs its
   `read` verb to grade the record clean. S7 says the factory's bullet. S9 says the retired row's text is that line with
   its `- ` cut.
3. **The plants' leg.** Section 7's first `New arm:` line says a leg runs every `fixture --plant` case, but S10 says one
   leg, running the check. As written no bar leg runs the plants. Decide by the fork rule: a second leg with its own rows,
   the one leg also running the fixture, or the plants joining an existing leg such as unit 20's
   `instruction units selftest`.
4. **Landing the `change` kind.** It leaves `tools/playbook/instruction_units.py#derive_status_note` permanently None.
   - Its caller `tools/playbook/render_playbook.py#run_check_render` needs editing and is unlisted.
   - `arm_status` pins both the unarmed line and the read that raises; both are rewritten.
   - `tools/memory-tree/build_records.py#run_fixture` passes exception flags to every door, so `new change` needs its own
     flags and that fixture must branch. S7 names the verb but not its flags.
   - Spec 20's fork F7 hands this unit the body of `read_change_records`.
   - List every path in Files touched.
5. **The write verbs' inputs.** S2 and S7's verbs need the recording build, unit id, `Caused-by` and `Mark`, but AC6's
   command passes none. Say where they come from. Say what `After` holds on a split, since it is specified as one
   `<tag>@<hash8>` or `none`.
6. **AC1.** "Adding one tag twice is a conflict" reads as any pair, but unit 45's table takes same-bytes adds once. Say
   AC1's pair has different bytes.
7. **The watch list.** `tools/gate-legs.json` is on the kickoff manifest's watch list, so `memory/guides/SESSION-KICKOFF.md`
   joins Files touched if the unit edits it.

In the spec:

- Bump the **Status:** rev by one, dated 2026-11-04, with the status kept `DEFERRED`.
- Add one history line naming this brief, with the S and AC ids it touched.
- Each listed `path:line` citation stays byte for byte, and new text cites code as `path#symbol`, outside the acceptance
  bullets. An acceptance bullet spells a plain tracked path, with no `#` and no `HEAD:` prefix.
- A `python -c` path in an acceptance bullet takes spaces around it, as `open( 'a/b' , 'rb')`.
- New text names a section in words. It never uses the section-sign form, the method-rule form or the hygiene
  check-number form, and it adds no `path:line`.
- An item that retires a name carries a `**Readers:**` clause. Its by-name half names readers by plain tracked path.
- Stay under the 47000-byte authored budget.
- A consumes-from or hands-off edge you add or change has its mirror; list it in the return.

For the run:

- No unit is building, so edit the spec in the tree.
- Writes stay in spec 15. A fork no option survives is written open in the fork record and said in the return.
- Do not commit and run no gate. You may run `check_path_shaped` from `tools/check-spec-tokens.py` as a read-only probe.
- Return the new rev, each fork decision with its loser, and any edge needing a mirror.

### Acceptance

- Every item above is folded, or listed in the return with the reason it was not.

### Gates

The main loop's live sweep, then the memory-hygiene hook at its commit.

### Non-goals

- No code.
- No other spec.

### Limitations

The items above, "For the run".

### Reuse

`tools/playbook/gov_tag.py#run_kit_verb`; `tools/memory-tree/build_records.py`; spec 20's forks F7 and F12.
