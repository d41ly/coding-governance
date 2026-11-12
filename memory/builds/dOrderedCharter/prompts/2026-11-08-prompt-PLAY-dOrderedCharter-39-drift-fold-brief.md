**Serves:** research PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55

# Brief: the last five specs, against the tree, before their units build

## The prompt

> Resume the build, it's no longer paused

— owner, 2026-11-08. Units 64 to 74 landed since these specs were last folded, and three repair specs bounced off claims the tree no
longer held. This sweep finds and folds each such claim before a builder dispatches.

## The brief

### Goal

Revise specs 39, 40, 49, 54 and 55 so each matches the tree at HEAD and a builder can build it as written.

### Items

1. **Where you write.** A unit is building, so edit only these scratch copies, and write nothing under the repository:
   - `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold13/2026-10-24-spec-PLAY-dOrderedCharter-39.md`
   - `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold13/2026-10-24-spec-PLAY-dOrderedCharter-40.md`
   - `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold13/2026-10-24-spec-PLAY-dOrderedCharter-49.md`
   - `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold13/2026-10-24-spec-PLAY-dOrderedCharter-54.md`
   - `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold13/2026-10-24-spec-PLAY-dOrderedCharter-55.md`
2. **What moved.** Read each spec against HEAD, not its base. In particular:
   - unit 72 moved `positional-refs.txt` and `positional-producers.txt` to `memory/project/` and replaced the kit's path literals with
     `{prefix}` or derived paths;
   - unit 71 made the adopter-name ban read only the roles an adopter receives;
   - unit 73 left the renderer's requires row alone, its dependency parked for the owner.
3. **Every reader claim is a grep.** For each symbol a spec says it retires, renames, moves or reads, grep its readers at HEAD and fix the
   claim. Specs 72 and 73 each bounced on one such claim.
4. **Folded neighbours:** every other unit's spec is folded. Specs 46, 35, 36, 34, 31 and 37 land with unit 3's records, so read
   their scratch copies in the folder `fold12` beside these.
5. **Known drift to fold:**
   - Spec 49 is 49745 bytes, over the 49152-byte spec ceiling: trim it under the ceiling with no requirement lost.
   - Spec 49's derivation of crossed documents must read enveloped files, not registry rows, or it reports the held
     `memory/guides/BUILD-METHOD.md` as crossed; and its item and criterion that spec 2 already met are dropped or rebased.
   - Spec 55: its sentence quoted from spec 41's first scope item is gone from spec 41; its delete of the
     playbook edge-checks module is moot if no unit builds that file; its item on stale ids is checked against HEAD.
     Keep its `closes PLAY-dOrderedCharter-38` header.
   - Spec 55 sits at 49333 bytes: leave it under the ceiling.
6. **Forks.** A conflict that is a choice goes to section 8, ruled by the fork rule. One whose surviving option trips the second or third
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

- No code. No edit outside the five scratch copies. No change to an owner-parked question.
