**Serves:** research TOOL-dDeclaredLoop-25

# Brief: revise spec TOOL-dDeclaredLoop-25 after its builder's divergence, the gov-rename plant

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. The first dispatch of TOOL-dDeclaredLoop-25 returned a divergence before any write: the `gov-rename`
plant renames `step.test` to `step.verify` in the planted steps, but frame rule 8 runs `loop_lib.py`'s `check_program`,
which calls `check_loop` first and refuses any step tag outside `STEP_TAGS`, so the plant exits 1 where AC6 needs 0. The
return is `memory/builds/dDeclaredLoop/build/2026-11-15-build-TOOL-dDeclaredLoop-25-1-builder-return.md`.

## The brief

### Goal

Revise `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-25.md` as rev-6, with one revision-log line naming
that return, so every plant can pass as written over HEAD.

### Items

1. Your worktree may be cut from main. First replace your copy of the spec with the branch's, through
   `git show branch/unattended-declared-loop-d56bf0:<path>`, and read every code claim from that branch the same way. Read the
   return whole.
2. The run takes the return's option (a): invert the `gov-rename` plant. Keep the shipped definition, set the stage's
   `after` to an old tag such as `step.verify`, and plant a change record with `Unit step.verify` and `Successor step.test`,
   so AC6's line naming `step.adopter.security-review`, `step.test` and `step.verify` holds and R1 leaves `testing`. The
   `check_splices` signature and every frame rule stay as they are. Rewrite the fixture-case row and AC6 to match, and add
   a section 8 fork recording (a) against (b) a separate definition for rule 8 and (c) letting `check_program` skip
   `check_loop`, recommending (a).
3. Name in section 5 the companion files the commit rewrites, which the return lists, and the playbook kit's version bump
   owed once, after the last move of its shipped bytes.
4. Keep the unit one mechanism, its carries, its order and its INPROGRESS status. Write only that spec file. Do not commit and do
   not regenerate any index. Run the spec-token checker with its spec flag over the spec and fix every hit. Do not run the
   whole-tree memory hygiene gate, and do not ask any checker for its help text. Each Readers half sits on one line.
5. Never kill a process you did not start, never match processes by a script's name to stop them, and never run
   check-memory-hygiene.sh, not even with --help.

### Acceptance

- Every plant of the revised spec can be observed at its stated exit over the shipped definition, and the spec-token checker
  reports no unwaived hit.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no new unit.
