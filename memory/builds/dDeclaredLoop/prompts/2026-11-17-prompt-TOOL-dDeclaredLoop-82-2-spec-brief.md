**Serves:** research TOOL-dDeclaredLoop-82

# Brief: revise spec TOOL-dDeclaredLoop-82 after its first builder return, the conf names in plant descriptions

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. The first dispatch of TOOL-dDeclaredLoop-82 returned a divergence before any write. The return is
`memory/builds/dDeclaredLoop/build/2026-11-17-build-TOOL-dDeclaredLoop-82-1-builder-return.md`. Its base probe ran S1 and S10's widened
`derive_conf_reads` rule, with unit 80's fixture boundary and S8's docstring set, over `tools/loop/budget.py` and `tools/loop/breakpoints.py`,
and found 8 conf-name hits at module level outside the boundary: description strings of each module's `PLANTS` dict that spell a conf file
name mid-string (6 in budget.py from units 72, 75, 76 and 79; 2 in breakpoints.py). Both `no-own-conf-read` plants end in a check of no hits,
so S10 as written reds the `loop budget fixtures` and `loop breakpoint fixtures` legs, against §4 "Evidence", §5 "The sweep" and AC1's
base probe; and breakpoints.py is not in §4 "Files touched". The return also lists stale figures: the budget rows read 498, 95 and 432 (not
476, 90 and 411), this spec has 1 positional row (not 9), the sweep's guard.py grep counts 5 (not 0) because of unit 75's
`push-merge-conflict-elsewhere` plant, and §4 "Evidence" spells the staging function by its old name, renamed `write_pre_placement_plant`.

## The brief

### Goal

Revise `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-82.md` as rev-8, with one revision-log line at the
END of the log naming that return, so S10's rule holds over both live modules and the sweep matches the code.

### Items

1. Your worktree may be cut from main. First replace your copy of the spec with the branch's, through
   `git show branch/unattended-declared-loop-d56bf0:<path>`, and read every code claim from that branch the same way,
   `tools/loop/loop_lib.py`, `tools/loop/budget.py` and `tools/loop/breakpoints.py` whole. Read the return whole, and its probe at
   `C:/Users/DAILY-~1/AppData/Local/Temp/claude/b120d4a7f8b5be2e/7c85732c-fa0c-43e9-83f2-238d293195e0/scratchpad/u82/probe_widened.py`.
2. Write the choice as a section 8 fork with the return's options: (a) reword the 8 descriptions so each names its conf without the dotted
   file name, adding `tools/loop/breakpoints.py` to Files touched, and the new `conf-read-forms` description owes the same; (b) narrow S10's
   anywhere-in-a-string rule so plant-description prose is passed over, saying how; (c) another exclusion you name. Recommend the option that
   keeps the rule's strength over code and is the smallest change, mark it `RESOLVED (agent, 2026-11-17, delegated): (<option>)`, and write
   S10, §4 "Files touched", §4 "Evidence", the two sweep rows, AC1 and any arm it moves on it.
3. Fix the stale figures and the staging function's old name, and re-run the sweep for anything the change reaches. Keep every other
   fork's mark.
4. Keep the unit one mechanism, its carries, its order and its INPROGRESS status. Write only that spec file. Do not commit and do
   not regenerate any index. Run the spec-token checker with its spec flag over the spec and fix every hit. Keep the
   `<!-- gen:spec-records -->` region and its closing marker exactly as the branch has them. Do not run the whole-tree memory
   hygiene gate, and do not ask any checker for its help text.
5. Never kill a process you did not start, never match processes by a script's name to stop them, and never run
   check-memory-hygiene.sh, not even with --help.

### Acceptance

- The widened rule, as revised, finds no hit outside the boundary in either live module at the base plus this unit's edits, every fork
  carries a mark, and the spec-token checker reports no unwaived hit.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no new unit.
