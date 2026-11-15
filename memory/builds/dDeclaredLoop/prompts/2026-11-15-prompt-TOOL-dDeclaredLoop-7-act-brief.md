**Serves:** research TOOL-dDeclaredLoop-7

# Brief: map a built unit's act answer onto the terminal `next:` shape in spec TOOL-dDeclaredLoop-7

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. The re-ground writer of TOOL-dDeclaredLoop-45 found a defect in TOOL-dDeclaredLoop-7 rev-4, which is
committed on branch/unattended-declared-loop-d56bf0 and not yet built. Its section 4 table "The `next:` line" maps every `act`
answer whose unit's spec is tracked to the live-unit shape, `<id> (READY - build it)`. Once every unit of a build is `built`
and waits for the close's bar, the least-advanced unit is `built`, the engine answers `act` on its test step, and `--plan`
would tell the harness to build a unit it already built. Today `--plan` prints `none - every tracked spec is terminal` there,
and the harness reads that line as its cue to close.

## The brief

### Goal

Revise the spec in place as rev-5, with one revision-log line, so an `act` answer whose least-advanced unit is `built` or
`tested` maps to the `terminal` row's shape, `none - every tracked spec is terminal`, and the live-unit shape is printed only
for a unit in `none` or `designed`.

### Items

1. Your worktree may be cut from main, which holds an older copy of this spec and lacks the loop kit. First replace your copy
   of `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-7.md` with the branch's, through
   `git show branch/unattended-declared-loop-d56bf0:<path>`, and read every code claim from that branch the same way.
2. Change the `act` rows of the `next:` line table, the scope item and acceptance criterion that observe `render_next_line`,
   and add one plant to the plant table that seeds every unit `built` and expects the terminal shape. Name the plant in the
   acceptance criterion that runs the plant table.
3. Add a section 8 fork F7 with the options (a) the terminal shape, keeping today's bytes and the harness's close cue, and
   (b) a new shape for a build waiting on its bar, with the readers each would move, and recommend (a). Leave the RESOLVED
   mark to the run.
4. Say in section 5 that `tools/unattended/check-unattended.sh` and the harness's close cue read the terminal words, and that
   (a) keeps them green.
5. Keep the unit one mechanism, its carries, its order and its status. Write only that spec file. Do not commit and do not
   regenerate any index. Run the spec-token checker with its spec flag over the spec and fix every hit until none remains. Do
   not run the whole-tree memory hygiene gate, and do not ask any checker for its help text. A by-name reader in a Readers
   clause is a tracked path, never `path#symbol`; keep each Readers clause's by name: and by value: halves each on one line.
6. Never kill a process you did not start, never match processes by a script's name to stop them, and never run
   check-memory-hygiene.sh, not even with --help.

### Acceptance

- No row of the spec maps a `built` or `tested` least-advanced unit to the live-unit shape, and the spec-token checker
  reports no unwaived hit.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no new unit.
