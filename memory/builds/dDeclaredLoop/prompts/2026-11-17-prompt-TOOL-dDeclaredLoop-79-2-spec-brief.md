**Serves:** research TOOL-dDeclaredLoop-79

# Brief: revise spec TOOL-dDeclaredLoop-79 after its first builder return, the gained prune's D-to-E exit

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. The first dispatch of TOOL-dDeclaredLoop-79 returned a divergence after building every other item. The return is
`memory/builds/dDeclaredLoop/build/2026-11-17-build-TOOL-dDeclaredLoop-79-1-builder-return.md`. §4 "The gained prune" and AC19 owe exit 0
for the D-to-E update, but E takes the `extra` kit's descriptor out while the registry still names it, so any read-only `update --to E`
reaches the step reader at the target commit after the prune, and it refuses the absent descriptor with exit 2, whether or not `extra` is
gained. The return also finds the driver-conf subshell sketch setting ROOT before the unset loop the prose puts first, and two stale sweep
figures (the `loop guard fixtures` budget row reads 95 at HEAD, not 90; `memory/project/positional-refs.txt` holds 1 row of this spec, not 16).

## The brief

### Goal

Revise `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-79.md` as rev-7, with one revision-log line at the
END of the log naming that return, so AC19 can hold against the landed update and the sketch and the sweep match the code.

### Items

1. Your worktree may be cut from main. First replace your copy of the spec with the branch's, through
   `git show branch/unattended-declared-loop-d56bf0:<path>`, and read every code claim from that branch the same way,
   `tools/govkit/govkit.py` (the update command and the pending-steps derivation) and `tools/govkit/upgrade_steps.py` whole. Read the
   return whole. The builder's built edits are a patch at
   `C:/Users/DAILY-~1/AppData/Local/Temp/claude/b120d4a7f8b5be2e/7c85732c-fa0c-43e9-83f2-238d293195e0/scratchpad/pending/TOOL-dDeclaredLoop-79-divergence.patch`;
   read it for what was built, and never apply it.
2. Write the choice as a section 8 fork with the return's two options: (a) the D-to-E row owes exit 2, the prune's NOT installed line
   printed and then the step reader's refusal naming the absent descriptor, and the arm grades that line and that refusal and never
   `update would leave` or the requires-unknown line; (b) E staged another way, one where the requires read answers unknown and the step
   reader does not refuse. Recommend the option the landed code supports without a product change outside this unit's write set, mark it
   `RESOLVED (agent, 2026-11-17, delegated): (<option>)`, and write §4 "The gained prune", S19, AC19 and the arm's `New arm:` line on it.
3. Make §4 "The driver-conf subshell" sketch match its prose: hold the second argument in a private name, unset the names, then set
   ROOT and CONF after the loop, as the builder built it.
4. Fix the two stale figures in §5's sweep, and re-run the sweep for anything the change reaches. Keep every other fork's mark.
5. Keep the unit one mechanism, its carries, its order and its INPROGRESS status. Write only that spec file. Do not commit and do
   not regenerate any index. Run the spec-token checker with its spec flag over the spec and fix every hit. Keep the
   `<!-- gen:spec-records -->` region and its closing marker exactly as the branch has them. Do not run the whole-tree memory
   hygiene gate, and do not ask any checker for its help text.
6. Never kill a process you did not start, never match processes by a script's name to stop them, and never run
   check-memory-hygiene.sh, not even with --help.

### Acceptance

- The D-to-E row's owed exit and lines are what the landed update prints over the staged E, every fork carries a mark, the sketch
  sets ROOT and CONF after the unset loop, and the spec-token checker reports no unwaived hit.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no new unit.
