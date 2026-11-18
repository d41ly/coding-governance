**Serves:** research TOOL-dDeclaredLoop-54

# Brief: revise spec TOOL-dDeclaredLoop-54 after its first builder return, on unit 33's module as built

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. The first dispatch of TOOL-dDeclaredLoop-54 returned a divergence before any write. The return is
`memory/builds/dDeclaredLoop/build/2026-11-16-build-TOOL-dDeclaredLoop-54-1-builder-return.md`. Unit 33 built
`tools/loop/termination.py` at rev-9 (b6c23d4fd), and rev-3 of this spec was written on unit 33's rev-6: its §8 forks F3 to F5
carry no resolution mark, so hygiene check 12 would refuse the CLOSED commit; AC3 expects the plant to exit 1, where the built
plants exit 0 when they hold and print the inner check's exit as a line; and S4 puts the per-level fill in
`read_termination_inputs`, where the built composition is made in `derive_termination_composition`, which every in-memory plant
calls.

## The brief

### Goal

Revise `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-54.md` as rev-4, with one revision-log line at the
END of the log naming that return, so a builder can build it over unit 33's module as built.

### Items

1. Your worktree may be cut from main. First replace your copy of the spec with the branch's, through
   `git show branch/unattended-declared-loop-d56bf0:<path>`, and read every code claim from that branch the same way, unit 33's
   built `tools/loop/termination.py` whole. Read the return whole.
2. Give F3, F4 and F5 each its mark, `RESOLVED (agent, 2026-11-16, delegated): (a)`, on its own line inside the fork's span,
   and every fork you add the same. A fork with no mark refuses the CLOSED commit.
3. Rewrite AC3 on the built plants' exit contract, and S4 and §4 on `derive_termination_composition` as the place that calls
   `read_terminal_set` for each level; name termination.py's docstring passages that say the feature and unit levels print
   unchecked, `derive_unchecked_levels` and the dead-end plant's expectation as carriers S4 or S5 updates.
4. Re-run the spec's sweep against unit 33's built code for everything else the change reaches, and keep the rest.
5. Keep the unit one mechanism, its carries, its order and its INPROGRESS status. Write only that spec file. Do not commit and do
   not regenerate any index. Run the spec-token checker with its spec flag over the spec and fix every hit. Keep the
   `<!-- gen:spec-records -->` region and its closing marker exactly as the branch has them. Do not run the whole-tree memory
   hygiene gate, and do not ask any checker for its help text.
6. Never kill a process you did not start, never match processes by a script's name to stop them, and never run
   check-memory-hygiene.sh, not even with --help.

### Acceptance

- Every §8 fork carries a resolution mark, AC3 and S4 hold over unit 33's built module, and the spec-token checker reports no
  unwaived hit.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no new unit.
