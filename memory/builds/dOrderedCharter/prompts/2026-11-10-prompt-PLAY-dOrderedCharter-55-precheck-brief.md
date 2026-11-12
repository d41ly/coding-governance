**Serves:** research PLAY-dOrderedCharter-55

# Brief: spec 55 — a pre-check against HEAD before its builder runs

## The prompt

> take forks' recommendations, land it

— owner, 2026-11-10. Spec 55 builds in this run after PLAY-dOrderedCharter-31; checked against HEAD now, its fixes fold before its
builder starts rather than after a hand-back.

## The brief

### Goal

Revise spec 55 so a builder can build it as written over HEAD.

### Items

1. **Where you write.** Units build in this tree meanwhile, so edit only this scratch copy and write nothing under the repository:
   `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold55/2026-10-24-spec-PLAY-dOrderedCharter-55.md`
2. **Pre-check every claim against HEAD.** Units landed since the spec's last revision include PLAY-dOrderedCharter-33's later commit,
   37, 40, 75, 76 and 77, which changed the overlay, the tag index, the step gate's classes, the docs leg, govkit's registry, the render
   and the help pages. For every symbol, file, row, signature, key or count the spec names, read the code; probe with `python -I` in a
   scratch folder of your own where a read cannot settle it.
3. Spec 55's S3 says unit 37's AC1 four-page half, AC8 and AC10 `unit-usage` half are observed at unit 37's later commit or at PLAY-dOrderedCharter-40's pass; that work is PLAY-dOrderedCharter-76, CLOSED at `8b16e46fb`. Fold each such hand-off to name unit 76. Spec 55 consumes 31, 39 and 49, which build before it: check its claims about them against their specs as written.
4. **The spec-token check grades a live spec's acceptance bullets word by word**: no acceptance command whose words include a path that
   is not a tracked file (an inline `python -c` with a quoted path fails this), never a `path#symbol` in an acceptance bullet, never a
   test suite or the self-test runner as the observation, each backticked span on one line, and every leg the files touched trip on
   the gates section's leg line. Cite code as `path#symbol` or a blob-pinned line, never a bare `path:line`.
5. Every section 8 fork carries a resolution mark; every new fact is pinned, keyed or marked DERIVED on its own line, outside backticks;
   every function name it mints passes `python tools/lexicon/lexicon.py --suggest <name> --as py.function`.
6. **Every reader claim is a grep**, at HEAD, for anything this revision moves or retires.

7. **Specs 39 and 49 are folded, not yet committed**: rev-5 at `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold39/2026-10-24-spec-PLAY-dOrderedCharter-39.md` and rev-8 at `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold49/2026-10-24-spec-PLAY-dOrderedCharter-49.md`; read those copies as what unit 55 consumes. Two of their picks contradict spec 55 and need re-deciding under the fork rule:
   - spec 39 F3 (b) keeps the agent-instructions wiring leg on gov's own bar as a gov-only `[[exempt_leg]]` row, not shipped with `playbook-render`, because every new adopter's bar would red on install day; spec 55's S28, AC28 and F3 give every `playbook-render` adopter the leg. Spec 55's S10 says unit 39 deletes the self-test leg's baseline line, which unit 31 rev-13 does instead.
   - spec 49 F3 builds no census step, since the census moves no unit at HEAD; spec 55's S9 and AC9 observe that step.

Resolve each choice under the fork rule and record it in section 8. Bump the **Status:** rev by one, dated 2026-11-10, status kept
`DEFERRED`, with a revision-log line naming this brief and the sections, scope ids and acceptance ids it touches.

### Acceptance

- Spec 55 builds as written over HEAD, every edge it gains is named in your return, and each change has a revision-log line.

### Gates

None run on the repository: this is a scratch edit. The main loop sweeps the spec and runs the spec-token check with it live.

### Non-goals

- No code. No edit outside the scratch copy.
