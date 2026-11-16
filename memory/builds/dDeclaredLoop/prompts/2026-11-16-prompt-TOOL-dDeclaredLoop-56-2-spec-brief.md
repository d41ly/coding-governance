**Serves:** research TOOL-dDeclaredLoop-56

# Brief: revise spec TOOL-dDeclaredLoop-56 after its first builder return, the edge with unit 70 reversed

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. The first dispatch of TOOL-dDeclaredLoop-56 returned before any write: `--dispatch` refused it under check
49, because §3 Edges reads `consumes-from TOOL-dDeclaredLoop-70` while unit 70 is DEFERRED and builds after this unit, writing
`tree=root` onto this unit's call. The return is
`memory/builds/dDeclaredLoop/build/2026-11-16-build-TOOL-dDeclaredLoop-56-1-builder-return.md`; it also names two stale counts
and three gaps. Unit 70's spec now reads `consumes-from TOOL-dDeclaredLoop-56` (its rev-4).

## The brief

### Goal

Revise `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-56.md` as rev-7, with one revision-log line at the
END of the log naming that return, so the dispatch admits it and a builder can build it at HEAD.

### Items

1. Your worktree may be cut from main. First replace your copy of the spec with the branch's, through
   `git show branch/unattended-declared-loop-d56bf0:<path>`, and read every code claim and unit 70's spec from that branch the
   same way. Read the return whole.
2. Make §3's edge with unit 70 a `hands-off TOOL-dDeclaredLoop-70` naming S18's `derive_phase_position` call, onto which unit
   70 writes `tree=root`, reciprocal to unit 70's `consumes-from`; and make §4 Dependency read the `extra=()` default that
   `derive_phase_position` already has at HEAD, not unit 70's.
3. Fix the two stale counts the return names (the positional rows for this spec, and the `--claims` reads of
   `tools/unattended/unattended.test.sh`), dropping `memory/project/positional-refs.txt` from Files touched if no row moves.
4. Settle the three gaps: name `tools/workflows/README.md` in Files touched with the sentence S41 changes; state in S36 what a
   scratch with no remote does with the remote-tip claim, as a section 8 fork if there is a choice; and add to §5's sweep the
   two `derive_position` callers over remote-less scratches (`tools/loop/adapt.py`'s mid-step plant and
   `tools/loop/composition.py`'s rename plant) with what keeps each green.
5. Every fork in section 8, old or new, ends with its own `RESOLVED (agent, 2026-11-16, delegated): (<option>)` mark.
6. Keep the unit one mechanism, its carries, its order and its INPROGRESS status. Write only that spec file. Do not commit and do
   not regenerate any index. Run the spec-token checker with its spec flag over the spec and fix every hit. Keep the
   `<!-- gen:spec-records -->` region and its closing marker exactly as the branch has them. Do not run the whole-tree memory
   hygiene gate, and do not ask any checker for its help text.
7. Never kill a process you did not start, never match processes by a script's name to stop them, and never run
   check-memory-hygiene.sh, not even with --help.

### Acceptance

- The spec consumes from no unit that builds after it, every fork carries a mark, the return's counts and gaps are settled, and
  the spec-token checker reports no unwaived hit.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no new unit.
