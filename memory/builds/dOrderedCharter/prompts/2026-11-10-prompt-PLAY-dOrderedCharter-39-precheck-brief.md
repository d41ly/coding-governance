**Serves:** research PLAY-dOrderedCharter-39

# Brief: spec 39 — a pre-check against HEAD before its builder runs

## The prompt

> take forks' recommendations, land it

— owner, 2026-11-10. Spec 39 builds in this run after PLAY-dOrderedCharter-31; checked against HEAD now, its fixes fold before its
builder starts rather than after a hand-back.

## The brief

### Goal

Revise spec 39 so a builder can build it as written over HEAD.

### Items

1. **Where you write.** Units build in this tree meanwhile, so edit only this scratch copy and write nothing under the repository:
   `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold39/2026-10-24-spec-PLAY-dOrderedCharter-39.md`
2. **Pre-check every claim against HEAD.** Units landed since the spec's last revision include PLAY-dOrderedCharter-33's later commit,
   37, 40, 75, 76 and 77, which changed the overlay, the tag index, the step gate's classes, the docs leg, govkit's registry, the render
   and the help pages. For every symbol, file, row, signature, key or count the spec names, read the code; probe with `python -I` in a
   scratch folder of your own where a read cannot settle it.
3. Spec 39 consumes PLAY-dOrderedCharter-31, whose rev-13 (committed, building next) folds the owner's picks: F10 lets govkit's selection resolver read a retired kit id through its `[[retired]]` row and F11 adds `playbook-render` to the default selection; build against rev-13 as written.
4. **The spec-token check grades a live spec's acceptance bullets word by word**: no acceptance command whose words include a path that
   is not a tracked file (an inline `python -c` with a quoted path fails this), never a `path#symbol` in an acceptance bullet, never a
   test suite or the self-test runner as the observation, each backticked span on one line, and every leg the files touched trip on
   the gates section's leg line. Cite code as `path#symbol` or a blob-pinned line, never a bare `path:line`.
5. Every section 8 fork carries a resolution mark; every new fact is pinned, keyed or marked DERIVED on its own line, outside backticks;
   every function name it mints passes `python tools/lexicon/lexicon.py --suggest <name> --as py.function`.
6. **Every reader claim is a grep**, at HEAD, for anything this revision moves or retires.

Resolve each choice under the fork rule and record it in section 8. Bump the **Status:** rev by one, dated 2026-11-10, status kept
`DEFERRED`, with a revision-log line naming this brief and the sections, scope ids and acceptance ids it touches.

### Acceptance

- Spec 39 builds as written over HEAD, every edge it gains is named in your return, and each change has a revision-log line.

### Gates

None run on the repository: this is a scratch edit. The main loop sweeps the spec and runs the spec-token check with it live.

### Non-goals

- No code. No edit outside the scratch copy.
