**Serves:** research TOOL-dDeclaredLoop-21

# Brief: revise spec TOOL-dDeclaredLoop-21 after its third builder return, the historical records and the fixture policy

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. The third dispatch of TOOL-dDeclaredLoop-21 returned a divergence before any write, naming two design gaps
in rev-6: S6's per-subject comparison in check-unattended.sh's check 2 reds tracked append-only RUN records written under the
retired 8-round backstop (69 subjects over their new bound, 4 even against `review.max-rounds`), and the driver suite's per-arm
policy file that S4 asks for is never read, because `review_bounds.py show` with no `--rev` reads the landed revision while the
fixture works on a branch. The return is
`memory/builds/dDeclaredLoop/build/2026-11-16-build-TOOL-dDeclaredLoop-21-3-builder-return.md`.

## The brief

### Goal

Revise `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-21.md` as rev-7, with one revision-log line naming
that return, so both gaps are closed and the close's `unattended kit gate` can hold over the tracked corpus.

### Items

1. Your worktree may be cut from main. First replace your copy of the spec with the branch's, through
   `git show branch/unattended-declared-loop-d56bf0:<path>`, and read every code claim from that branch the same way. Read the
   return whole.
2. Write each gap as a section 8 fork with the return's options. For the historical records the run's preference, unless the
   tree shows a reason against it, is grandfathering by the record's first-commit date through the `rv_fc` idiom check 2
   already applies to its other cutoffs, with the cutoff's value and home named. For the fixture policy the run's preference is
   seeding the default policy on the fixture's main before the ORIGIN push and stating how a per-arm value lands without moving
   the anchor, which keeps the driver reading the landed revision. Recommend by the ratify rule, mark each RESOLVED (agent,
   2026-11-16, delegated) on its recommendation, and write the body on it, naming any new value, reader or file in §4 and
   Files touched.
3. §4 "What this does not check" and AC6 say how a pre-cutoff record is graded. State the census and families after the change
   (no new `fail` site in check-unattended.sh, which sits at 266 of 266).
4. Change nothing else. Keep the unit one mechanism, its carries, its order and its INPROGRESS status. Write only that spec
   file. Do not commit and do not regenerate any index. Run the spec-token checker with its spec flag over the spec and fix
   every hit. Do not run the whole-tree memory hygiene gate, and do not ask any checker for its help text.
5. Never kill a process you did not start, never match processes by a script's name to stop them, and never run
   check-memory-hygiene.sh, not even with --help.

### Acceptance

- Both gaps are answered in the body, and the spec-token checker reports no unwaived hit.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no new unit.
