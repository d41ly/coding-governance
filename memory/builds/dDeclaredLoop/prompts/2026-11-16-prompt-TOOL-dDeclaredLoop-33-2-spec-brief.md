**Serves:** research TOOL-dDeclaredLoop-33

# Brief: revise spec TOOL-dDeclaredLoop-33 after its first builder return, the reachable rule made to hold over gov's own rows

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. The first dispatch of TOOL-dDeclaredLoop-33 returned a divergence before any write: S3's `reachable` rule,
walked from each program's items with no needs along routes and need edges, leaves `item.build.resolve` unreached, because its
one need `item.test.merge` sits in the test program and the only route into it comes from there. AC10 and §5 Rollout need gov's
composition to exit 0, and §4 "Gov's own cycles at landing" bounds only cycles. The return is
`memory/builds/dDeclaredLoop/build/2026-11-16-build-TOOL-dDeclaredLoop-33-1-builder-return.md`; it measures three readings of
the walk over gov's rows at HEAD and shows that counting a cross-program item as an entry would leave the rule unable to flag
anything, so AC3's `orphan-item` plant could not go red.

## The brief

### Goal

Revise `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-33.md` as rev-7, with one revision-log line naming
that return, so S3, AC3, AC10 and §4 all hold over gov's own rows at HEAD and AC3's plant still goes red.

### Items

1. Your worktree may be cut from main. First replace your copy of the spec with the branch's, through
   `git show branch/unattended-declared-loop-d56bf0:<path>`, and read every code claim from that branch the same way. Read the
   return whole.
2. Write the choice as a section 8 fork with at least the return's two options: (a) the walk starts from every program's
   entries and grades only this program's items, with AC3's orphan plant rebuilt so it still reds; (b) `item.build.resolve`, and
   any item like it, carries a declared bound, such as a pending row of a new kind. Measure each option over gov's rows at HEAD
   and over AC3's plant, recommend the one that keeps the rule able to red with the smallest change, mark it RESOLVED (agent,
   2026-11-16, delegated), and write S3, AC3, AC10 and §4 on it.
3. Update the PINNED cycle count to 23 at e8018d94f (the two new cycles come from unit 50's review rows), and name both in §4's
   rules where they are bounded.
4. Re-run the spec's sweep for anything the change reaches, and keep everything else, including F7's departure and F9.
5. Keep the unit one mechanism, its carries, its order and its INPROGRESS status. Write only that spec file. Do not commit and do
   not regenerate any index. Run the spec-token checker with its spec flag over the spec and fix every hit. Keep the
   `<!-- gen:spec-records -->` region and its closing marker exactly as the branch has them. Do not run the whole-tree memory
   hygiene gate, and do not ask any checker for its help text.
6. Never kill a process you did not start, never match processes by a script's name to stop them, and never run
   check-memory-hygiene.sh, not even with --help.

### Acceptance

- Over gov's rows at HEAD the revised rules print no finding, AC3's plant reds under them, and the spec-token checker reports
  no unwaived hit.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no new unit.
