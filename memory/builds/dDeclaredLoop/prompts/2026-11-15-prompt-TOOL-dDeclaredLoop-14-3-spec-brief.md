**Serves:** research TOOL-dDeclaredLoop-14

# Brief: revise spec TOOL-dDeclaredLoop-14 after its third builder return, the refusal budgets

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. The third dispatch of TOOL-dDeclaredLoop-14 returned a divergence before any write: S3's new check-48
refusals take `tools/unattended/unattended.sh`'s refusal census past its `REFUSAL_CEILINGS` row in `.memory-tree.conf`
(324 of 324 at base) and the `field-shape` family in `tools/unattended/unattended.families.txt` past its ceiling (36 of 37,
three new guards make 39). The return is `memory/builds/dDeclaredLoop/build/2026-11-15-build-TOOL-dDeclaredLoop-14-3-builder-return.md`.

## The brief

### Goal

Revise `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-14.md` in place as rev-7, with one revision-log line
naming that return, so a builder can build it as written with the `harness arms (fail branches armed or pinned)` leg green.

### Items

1. Read the return whole, then `tools/unattended/check-arms.py`'s census and family readers, the `REFUSAL_CEILINGS` row and its
   `RAISED` comment lines, `tools/unattended/unattended.families.txt`, and `verb_propose`'s field guards. Measure the census
   and the family yourself with check-arms' own readers, not a grep.
2. Write the choice as a section 8 fork: (a) raise both ceilings, each with a decision row committed ahead of the pass, as
   TOOL-dDeclaredLoop-5's row raised the unattended leg's refusal ceiling; (b) factor the field guards `verb_propose` and the
   new verb share into one helper so the family stays flat, with the arms that move; (c) a mix, with the smallest raise left.
   Prefer what keeps the counts flattest; recommend one and write the body on it.
3. For every raise the body keeps, write in section 4 the exact `RAISED` comment line the pass adds and the exact text of each
   decision row, so the run can commit the rows to `memory/DECISIONS.md` before the pass. The pass never writes that file:
   it is a shared record `--dispatch` refuses. Add `.memory-tree.conf` and `tools/unattended/unattended.families.txt` to
   Files touched where they move, and name in section 5 every arm and census the choice reaches.
4. Keep section 7's `harness arms` leg and say the close observes the ceiling line `check-arms: ceiling
   tools/unattended/unattended.sh <census>/<ceiling>`.
5. Keep the unit one mechanism, its carries, its order and its INPROGRESS status. Write only that spec file. Do not commit and do
   not regenerate any index. Run the spec-token checker with its spec flag over the revised spec and fix every hit. Do not run
   the whole-tree memory hygiene gate, and do not ask any checker for its help text. A figure before a unit word carries PINNED
   on its line, and each Readers half sits on one line.
6. Never kill a process you did not start, never match processes by a script's name to stop them, and never run
   check-memory-hygiene.sh, not even with --help.

### Acceptance

- Building the revised spec leaves the driver's census and every family at or under its ceiling at the pass, with each raise's
  decision row text written out for the run to land first; the spec-token checker reports no unwaived hit.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no new unit.
