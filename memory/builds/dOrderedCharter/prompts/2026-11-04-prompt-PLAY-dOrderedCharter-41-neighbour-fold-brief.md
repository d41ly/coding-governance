**Serves:** research PLAY-dOrderedCharter-41

# Brief: specs 2, 6 and 41 against what specs 1 and 3 ruled at rev-8

## The prompt

> execute keeping the build unattended

— owner, 2026-11-03. Spec 1's divergence fold and spec 3's interim hold, both committed at `730f9225f`, moved facts these three specs
rest on. Each writer named the neighbours. Unit 1 is building, so this fold runs on scratch copies.

## The brief

### Goal

Revise specs 2, 6 and 41 so each agrees with specs 1 and 3 at rev-8 and a builder can build it as written.

### Items

1. **Where you write.** A unit is building in the tree, so edit only these scratch copies, and write nothing under the repository:
   - `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold7/2026-10-23-spec-PLAY-dOrderedCharter-2.md`
   - `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold7/2026-10-23-spec-PLAY-dOrderedCharter-6.md`
   - `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold7/2026-10-24-spec-PLAY-dOrderedCharter-41.md`
2. **Spec 2 and the hold.** Its precedence rule says unenveloped text is data, and its map lists `memory/guides/BUILD-METHOD.md` at
   level 3. Under spec 3's hold (S9, fork F5) that guide has no envelope until the owner rules, so the two statements disagree for as
   long as the hold stands. Say how the held document reads, without moving its row, source or prose, and without settling F5.
   Decide by the fork rule. If the rule's text lands in the charter, keep it within what the charter's row allows.
3. **Spec 41's scratch targets.** Spec 1's F7 refuses a target that is no repository, or whose default branch has no commit. S4's arm
   and the AC3 and AC5 scratch targets must be repositories committed on `main`.
4. **Spec 41's pointers.** Its S1 and S3 "supersedes" sentences point at spec 1 text that is gone. Re-read spec 1's S6 and re-point them.
5. **Spec 41's note.** Its S2 note replaces spec 1's S6 note, and its `practices` prefix does not print under `--check`, which prints
   only `legacy` and `retired` notes. Make S2 true of the code, or say what changes so the prefix prints.
6. **Spec 6 and the wiring guide.** `WIRE-INTO-PROJECT.md`'s "Section 1 … is not droppable" goes false once unit 1 lands. Add the
   one-line correction to spec 6's scope and Files touched, if unit 6 is the right home; if it is not, name the right unit in your return.

Read each spec whole against the tree and against spec 1 and spec 3, and fix any other clause that reads the old state.

In each spec you change:

- Bump the **Status:** rev by one, dated 2026-11-04, with the status kept `DEFERRED`.
- Add one history line naming this brief, with the S and AC ids it touched.
- Each listed `path:line` citation stays byte for byte, and new text cites code as `path#symbol`, outside the acceptance
  bullets. An acceptance bullet spells a plain tracked path, with no `#` and no `HEAD:` prefix, and never a file not yet tracked.
- A `python -c` path in an acceptance bullet takes spaces around it, as `open( 'a/b' , 'rb')`.
- New text names a section in words, and names a check by what it checks.
- Any retirement word in section 2 owes its Readers clause.

### Acceptance

- Each item is resolved in its spec, forks in section 8 with the loser recorded.
- Consumes-from and hands-off edges still mirror across the specs you touch.

### Gates

None run: this is a scratch edit. The main loop live-sweeps each spec before its dispatch.

### Non-goals

- No code.
- No edit outside the three scratch copies; name any other neighbour in your return.
- No ruling on spec 3's F5.
