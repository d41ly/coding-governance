**Serves:** research PLAY-dOrderedCharter-26

# Brief: unit 26's divergence — the symbol citation against the tree's other `<path>#<name>` forms

## The prompt

> Try again

— owner, 2026-11-03, the run's last instruction. Unit 26's builder (run wf_981dd517-45c) returned `DIVERGENCE:` before
writing code. S1 and S4 (with AC6 and AC10) make any `path#symbol` a symbol citation and red an unresolved one in every
tracked path outside `memory/builds/`. The tree holds two other forms: govkit's usage ids `script:<path>#<verb>` (21 in
`tools/govkit/usage.toml`, the `<!-- usage: ... -->` markers across `help/`, the fixture in `tools/govkit/docs_leg.py`),
whose `#<verb>` names a CLI verb, not a definition; and the namespace registry's `purpose-source = "<path>#<field>"`
(unit 22) in `tools/playbook/namespaces.toml`, `gov_tag.py` and `adopt-playbook.sh`, often a `.toml` path. A grep of
S1's grammar finds 57 such sites in live text, so AC10 cannot pass. Second: `tools/playbook/positional-refs.txt` lacks
the row `gov_tag.py --list-positional` prints for `memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-19-ledger.md`
(`BUILD-METHOD M5`), and S2's seed writes only `file:line` rows.

## The brief

### Goal

Revise spec 26 so its symbol scan reads only symbol citations, AC10's positional arm exits 0 on the tree at its pass,
and the seed covers every positional row the tree holds then.

### Items

1. **Telling a symbol citation apart (S1, S4).** Decide by M3 between at least: excluding the `script:` usage-id
   prefix and the `purpose-source` value by rule; requiring a definition-shaped context; an opt-in marker; or another
   mechanism. State what a symbol citation whose path is outside py/sh/js is graded as. Record the loser and the
   observation that rejected it (M12) in §8, delegated. Run the chosen predicate over the tree and write the count it
   leaves red into §6 (it must be 0) beside the count it reads as citations.
2. **The seed (S2, AC10).** Say whether the seed joins every `§n`, `Mn` and `check n` positional reference present at
   the build pass, not only `file:line` rows, so the one row above and any like it are listed.
3. **ACs.** Observe by fixture plants or a probe of the unit's own code; no AC observes a suite, a bar, or the `tags`
   leg over the tree.

In the spec:

- Bump the **Status:** rev by one, dated 2026-11-03, the status kept `DEFERRED`, and add one §9 line naming this brief.
- §7's leg line names every leg whose guard a Files-touched path trips.
- Verify every path, count and line you cite against the tree at HEAD; stay under the 47000-byte authored budget.

For the run:

- Writes stay in spec 26 and the files `gen_build_index.py --write` rewrites.
- This is an unattended run and nobody answers a question: a fork no option survives is written as an open §8 item
  with the options and the veto, and said in the return.
- Do not commit and run no check: the main loop re-renders the packet, runs the spec-token check, renders the index
  and commits.
- Scratch files go under the session scratchpad
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad`.
- Return the new rev, the §8 decision with its loser, and the counts item 1 measures.

### Acceptance

- Spec 26's §6 carries item 1's red count, and it is 0.
- The Status line is one rev higher, and §9 holds the new line.

### Gates

The spec-token check, run by the main loop before the commit.

### Non-goals

No code; no spec but 26; the usage-id grammar, the `help/` usage markers and the registry's field grammar stay as
they are.

### Limitations

The items above, "For the run".

### Reuse

`tools/govkit/docs_leg.py`'s usage-id grammar; `tools/playbook/tag_index.py`'s purpose-source reader (unit 22);
`gov_tag.py --list-positional`.
