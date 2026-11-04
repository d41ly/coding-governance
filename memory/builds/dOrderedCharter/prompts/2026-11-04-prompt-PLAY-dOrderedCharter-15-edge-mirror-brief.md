**Serves:** research PLAY-dOrderedCharter-38

# Brief: the edge mirrors the second drift fold owes

## The prompt

> execute keeping the build unattended

— owner, 2026-11-03. The main loop ran the memory-hygiene edge join over the tree with the second fold's scratch
copies, and it found one-sided edges. The commit hook holds that join under `--staged`, but the full run at the
close grades every spec in the build, CLOSED ones included.

## The brief

### Goal

Make every edge below pair with its mirror, so the edge join reads clean.

### Items

1. Fix each one-sided edge below. A `consumes-from X` on unit U needs `hands-off U` on unit X, and the reverse.
   - unit 2 (DEFERRED) consumes-from 19 (CLOSED) — no hands-off 2 back
   - unit 6 (DEFERRED) consumes-from 1 (DEFERRED) — no hands-off 6 back
   - unit 7 (DEFERRED) consumes-from 24 (CLOSED) — no hands-off 7 back
   - unit 7 (DEFERRED) hands-off 27 (DEFERRED) — no consumes-from 7 back
   - unit 11 (DEFERRED) consumes-from 19 (CLOSED) — no hands-off 11 back
   - unit 27 (DEFERRED) consumes-from 19 (CLOSED) — no hands-off 27 back
   - unit 52 (DEFERRED) consumes-from 15 (DEFERRED) — no hands-off 52 back
   - unit 61 (CLOSED) consumes-from 16 (CLOSED) — no hands-off 61 back
   - unit 62 (CLOSED) consumes-from 61 (CLOSED) — no hands-off 62 back
2. Use these rules:
   - **An edge is still true:** add the missing mirror on its target, with one line of prose matching the source's.
     That holds even when the target is CLOSED, because an edge is a record of the dependency.
   - **An edge no longer names a real dependency:** drop it from its source. Unit 7's hands-off to unit 27 is one,
     since unit 27 now reads `read_policy_value` from unit 19.
   - **Order:** a hands-off target comes later in the build order than its source.
3. Edit only the scratch copies in `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold2/`. That folder holds every spec this pass may touch. The tree stays
   untouched.
4. New text names a section in words ("section 3"). It never uses the section-sign form, the method-rule form or the
   hygiene check-number form, and it adds no `path:line` citation.
5. Add no status rev for a mirror-only edit. Each spec you edit gains one history line naming this brief.

For the run:

- Writes stay in the scratch copies.
- Do not commit and run no check.
- Return the edges as they now read, each pair from both ends.

### Acceptance

- Every row above is paired or dropped, and the return lists each one.

### Gates

The main loop re-runs the edge join over the copies before they move in.

### Non-goals

- No other edit.

### Limitations

The items above, "For the run".

### Reuse

The edge grammar in `memory/TEMPLATE-SPEC.md`.
