**Serves:** research TOOL-dDeclaredLoop-68

# Brief: revise spec TOOL-dDeclaredLoop-68 after its first builder return, the bash-spelled worktree root

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. The first dispatch of TOOL-dDeclaredLoop-68 returned a divergence before any write. The return is
`memory/builds/dDeclaredLoop/build/2026-11-17-build-TOOL-dDeclaredLoop-68-1-builder-return.md`. S1 hands the run-gates kit's
`write_normaliser` three roots, the worktree's path, its realpath and the repo's path; but Git Bash mounts `/tmp` on the user's
temp folder, so a worktree that `tempfile.mkdtemp` placed under `%TEMP%` prints from bash's `pwd` as `/tmp/lw-<random>/tree`,
which no root spells, and the `normalise` plant's two re-runs cannot hash equal (AC1). The return lists three options and one
stale figure (the `from loop_witness import` readers are 16 at HEAD, not 13).

## The brief

### Goal

Revise `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-68.md` as rev-4, with one revision-log line at the
END of the log naming that return, so AC1 can hold on this node and the stale figure is fixed.

### Items

1. Your worktree may be cut from main. First replace your copy of the spec with the branch's, through
   `git show branch/unattended-declared-loop-d56bf0:<path>`, and read every code claim from that branch the same way,
   `tools/loop/loop_witness.py` and `tools/run-gates/lib-attribute.sh` whole. Read the return whole.
2. Write the choice as a section 8 fork with the return's three options: (a) a fourth root, the tree's path as the
   normaliser's own bash prints it, passed to `write_normaliser` inside that bash; (b) the worktree placed outside the `/tmp`
   mount, as the run-gates runners place theirs; (c) bash's `pwd` dropped from S4's command. Recommend the option that keeps
   AC1's strength and holds on every node, mark it `RESOLVED (agent, 2026-11-17, delegated): (<option>)`, and write S1, §4
   "The route", S4, AC1 and §5's risks on it.
3. Fix the stale figure in §5's sweep, and re-run the sweep for anything the change reaches. Keep every other fork's mark.
4. Keep the unit one mechanism, its carries, its order and its INPROGRESS status. Write only that spec file. Do not commit and do
   not regenerate any index. Run the spec-token checker with its spec flag over the spec and fix every hit. Keep the
   `<!-- gen:spec-records -->` region and its closing marker exactly as the branch has them. Do not run the whole-tree memory
   hygiene gate, and do not ask any checker for its help text.
5. Never kill a process you did not start, never match processes by a script's name to stop them, and never run
   check-memory-hygiene.sh, not even with --help.

### Acceptance

- The recommended option makes the `normalise` plant's two re-runs hash equal on a worktree under the `/tmp` mount, every fork
  carries a mark, and the spec-token checker reports no unwaived hit.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no new unit.
