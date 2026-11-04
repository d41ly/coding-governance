**Serves:** research PLAY-dOrderedCharter-38

# Brief: fold drift sweep E into specs 52, 6, 2 and 11

## The prompt

> execute keeping the build unattended

— owner, 2026-11-03, approving the run's drift sweep (`prompts/2026-11-03-prompt-PLAY-dOrderedCharter-38-owner-speedup.md`), repeated
as the build advances. The sweep's reviewer read specs 52, 6, 2 and 11 against the tree at `c7269a97d` and returned the
findings below, every one with a tree path and line.

## The brief

### Goal

Revise specs 52, 6, 2 and 11 so each matches the tree at HEAD on every finding below.

### Items

1. **Where you write.** A unit is building in the tree, so edit only these scratch copies of the specs:
   - `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold2/2026-10-24-spec-PLAY-dOrderedCharter-52.md`
   - `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold2/2026-10-23-spec-PLAY-dOrderedCharter-6.md`
   - `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold2/2026-10-23-spec-PLAY-dOrderedCharter-2.md`
   - `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold2/2026-10-23-spec-PLAY-dOrderedCharter-11.md`
   - Do not touch the specs in the tree; the main loop moves the copies in between units.
   - Read the tree's code at HEAD as usual.
2. **Fold every finding below into its spec.** Re-verify each cited path and line at HEAD before writing it.
3. **A finding marked NEW MECHANISM, or NEEDS A FORK, is a fork.** Decide it by the build method's fork rule.
   - Record the loser, and the observation that rejected it, in the spec's fork record (its section 8), delegated.
   - If no option survives, write an open fork item with the options and the veto, and say so in the return.
4. **Listed citations stay as they are.** Every existing `path:line` citation in these specs is a row of
   `tools/playbook/positional-refs.txt`.
   - Editing one makes that row stale, and the tags leg reds a stale row.
   - Keep each one's text byte for byte. Write the current location beside it in a stable form: `path#symbol`, or
     `path@<sha8>:<line>` for a line with no symbol.
   - Write no new `path:line` citation.
5. **New text names a section in words.** A spec's own section is "section 7" or "the fork record".
   - Never write the section-sign form, the method-rule form, or the hygiene check-number form.
   - Unit 53's per-line rule grades every line added after the positional check landed.
6. **A new leg's rows ride its own pass.** Those rows are:
   - its dossier claim in `memory/map/features/playbook.md`, with the regenerated `memory/map/generated/*`;
   - its `tools/govkit/subject-pins.tsv` row;
   - its claiming `[[exempt_leg]]` row in `tools/govkit/registry.toml`, or `[[gate_leg]]` row in the kit's `kit.toml`.
   - Files touched lists those paths, and section 7 names the legs they trip (`check-spec-tokens.py --legs-for`).
   - A new selftest arm is wired into a leg, for example through `adopt-playbook.sh`'s `run_plant_rows`.
7. **The main loop decided these across the sweep:**
   - The caps still live in `tools/template-size-limits.txt`: dSafePassage's limits step moved to TOOL-dSafePassage-61,
     which is still DEFERRED. So:
     - a raise follows that file's raise conditions;
     - a cap is read through `budgets.py resolve`;
     - a dSafePassage edge names that file instead.
   - A `role.<name>` selector is reported `unarmed`, as an unregistered `feature.*` part is, until a unit registers a
     `role` namespace. No spec registers one.
   - A raise of BUILD-METHOD's cap is the owner's, so no spec raises it. Choose among the options that leave it alone.
   - The policy reader is unit 19's `tools/playbook/policy_value.py#read_policy_value`, and its refusal is
     `PolicyRefused`. Consumes-from edges name unit 19.
   - An AC never runs a leg's exact argv or a `--selftest`, because scratch-guard refuses both to a builder.

In every spec you revise:

- Bump the **Status:** rev by one, dated 2026-11-04, with the status kept `DEFERRED`.
- Add one line to the spec's history (its section 9) naming this brief.
- Stay under the 47000-byte authored budget.

For the run:

- Writes stay in the scratch copies above.
- Do not commit and run no check.
- Return each spec's new rev, each fork decision with its loser, and any finding you did not fold, with the reason.

**The findings** are in `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/sweep-E-findings.md`; read it whole. It cites the
tree at `c7269a97d` as `path:line`; any citation you carry into a spec takes the stable form of item 4.

### Acceptance

- Each finding above is folded, or listed in the return with the reason it was not.
- Each revised copy's Status line is one rev higher, and its history holds the new line.

### Gates

The spec-token check, run over the tree by the next `--dispatch` after the copies move in.

### Non-goals

- No code.
- No spec outside the ones above.
- No edit in the tree.

### Limitations

The items above, "For the run".

### Reuse

The landed units' builder returns in `memory/builds/dOrderedCharter/build/`; `tools/playbook/edge_grammar.py`;
`tools/playbook/policy_value.py`.
