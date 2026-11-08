**Serves:** research PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-37

# Brief: the six specs after unit 33, against the tree, before their units build

## The prompt

> Resume the build, it's no longer paused

— owner, 2026-11-08. Units 64 to 74 landed since these specs were last folded, and three repair specs bounced off claims the tree no
longer held. This sweep finds and folds each such claim before a builder dispatches.

## The brief

### Goal

Revise specs 46, 35, 36, 34, 31 and 37 so each matches the tree at HEAD and a builder can build it as written.

### Items

1. **Where you write.** A unit is building, so edit only these scratch copies, and write nothing under the repository:
   - `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold12/2026-10-23-spec-PLAY-dOrderedCharter-31.md`
   - `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold12/2026-10-23-spec-PLAY-dOrderedCharter-34.md`
   - `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold12/2026-10-23-spec-PLAY-dOrderedCharter-35.md`
   - `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold12/2026-10-23-spec-PLAY-dOrderedCharter-36.md`
   - `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold12/2026-10-23-spec-PLAY-dOrderedCharter-37.md`
   - `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold12/2026-10-24-spec-PLAY-dOrderedCharter-46.md`
2. **What moved.** Read each spec against HEAD, not its base. In particular:
   - unit 72 moved `positional-refs.txt` and `positional-producers.txt` to `memory/project/` and replaced the kit's path literals with
     `{prefix}` or derived paths;
   - unit 71 made the adopter-name ban read only the roles an adopter receives;
   - unit 73 left the renderer's requires row alone, its dependency parked for the owner.
3. **Every reader claim is a grep.** For each symbol a spec says it retires, renames, moves or reads, grep its readers at HEAD and fix the
   claim. Specs 72 and 73 each bounced on one such claim.
4. **Folded neighbours:** specs 3, 41, 52, 6, 2, 11, 27, 21, 5, 4, 8, 14, 43, 30, 29, 23, 32 and 33 are folded; the last six land with
   unit 52's records, so read their scratch copies in the folder `fold11` beside these. Spec 29 moves the unpinned-facts list to
   `memory/project/`; spec 33 lands two registry rows in a later commit of its unit.
5. **Forks.** A conflict that is a choice goes to section 8, ruled by the fork rule. One whose surviving option trips the second or third
   veto is left open and named in your return; the run parks it.

In each spec you change:

- Bump the **Status:** rev by one, dated 2026-11-08, status kept `DEFERRED`, with one history line naming this brief.
- Each listed `path:line` citation stays byte for byte, and new text cites code as `path#symbol`, outside the acceptance bullets, which
  spell plain tracked paths and never a file not yet tracked. New text names a section in words, and a check by what it checks.
- Any retirement word in section 2 owes its Readers clause.

### Acceptance

- Each spec matches HEAD on every claim checked, and every change has a history line.
- Your return names, per spec, what changed, and any fork left open.

### Gates

None run: this is a scratch edit. The main loop live-sweeps each spec before its dispatch.

### Non-goals

- No code. No edit outside the six scratch copies. No change to an owner-parked question.
