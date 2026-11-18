**Serves:** research TOOL-dDeclaredLoop-90

# Brief: re-ground spec TOOL-dDeclaredLoop-90 on the code as built

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. This build's specs predate the code the parent builds and its own earlier units landed. This spec is
re-grounded before its builder is dispatched.

## The brief

### Goal

Revise the spec of TOOL-dDeclaredLoop-90 in place, as a rev bump with one revision-log line, so a builder can build it as written
over HEAD. Where every claim already holds, change nothing and say so in your return.

### Items

1. Read the whole spec against the code at HEAD of branch/unattended-declared-loop-d56bf0 and settle every claim the landed
   code has moved. The branch has built every unit through build order 36 (unit 56: the keyed `--claims` flag, the parent read by
   phase row and run branch, the absent remote; unit 70: `read_driver_conf` in `loop_lib.py`; unit 72:
   `resolve_memory_root` in `loop_lib.py`, `read_memory_root` retired) and every unit of order 37 (65: `read_fetch_time`; 68: the witness normaliser on the run-gates kit; 76:
   `resolve_memory_root_source` and the syntax-tree conf-read rule `derive_conf_reads`); unit 67 of order 38 is building now
   and 80, 74 and 66 follow (each built unit a CLOSED spec in this build's spec folder). Committed specs for later orders: 79
   rev-6 (order 40), 82 rev-7 (order 41, amends no sibling spec), 86 rev-8 (order 42, `derive_conf_constants`), 87 rev-6
   (order 43), and 89 rev-5 and 88 rev-6 (order 44: 89 mints `load_tree_lib`, 88 adds two catches to it). A CLOSED spec is frozen: never plan an edit to one. Unit 64 added a `breakpoints: held` line to
   `tools/loop/breakpoints.py` and the `pre-placement-records-root` plant; unit 55 wrote nothing. Built since the last re-grounds: unit 33
   (`tools/loop/termination.py`, its leg `loop termination`, `tools/loop/termination-pending.txt`, deviation 334 amending
   `cl-dClosedLoop-0118`), unit 63 (`derive_phase_position(phase, facts, phase_map=None, extra=())`, the `phase` verb's
   `--extra`, the driver passing `PHASES_EXTRA`) and unit 54 (per-level terminal sets `feature-terminal` and `unit-terminal` in
   `[states]`, `read_terminal_set(tables, level)`, the `unit-dead-end` plant). The driver's refusal census is 343. Committed
   specs to write against: order 36's 56 rev-6, 70 rev-3, 71 rev-4 and 72 rev-6; order 37's 65 rev-3, 68 rev-3 and 76 rev-6;
   order 38's 66 rev-4 (builds nothing), 67 rev-4, 74 rev-3 (`derive_fetch_url`, per-file skip lines) and 80 rev-6
   (`derive_fixture_boundary`, `write_pre_placement_plant`); order 39's 75 rev-10 and 77 rev-3 (`derive_fetch_url`'s
   user-part rule). Unit 34 is deferred against ask TOOL-dDeclaredLoop-113, and unit
   33's numeric direction against ask TOOL-dDeclaredLoop-114. An item the built code or a committed spec already satisfies
   leaves the spec's scope, said so.
2. THE SWEEP, before you return: for every function, file, constant and fixture the revised body changes or removes, find every
   caller, reader, fixture, suite arm, test population and frozen or pinned contract (upgrade step rows, subject pins,
   verdict-epoch delegates, census and family ceilings, size caps, the lexicon pin, help anchors and usage rows, the new leg's
   companions with a `stage` key) at the branch tip, and say in section 5 what keeps each green, with the commands that
   re-derive the counts. Unit 21's builder diverged four times on gaps its spec writers had not swept.
3. Check the write set against what the change really touches: registry rows, usage rows, subject pins, the verdict-epoch
   gate's delegate list, the kickoff manifest's watch list, generated map files, any line the install-prefix ban flags, and
   every existing fixture or selftest arm the change could newly red; name each in section 5 with what keeps it green.
4. A choice between designs is a section 8 fork with its options and your recommendation, and the spec body is written on the
   recommendation: the run takes it under its mandate. Every fork in section 8, old or new, ends with its own mark,
   `RESOLVED (agent, 2026-11-16, delegated): (<option>)`, on a line inside its span; a fork with no mark refuses the CLOSED commit.
5. Keep the unit one mechanism, its carries, its order and its status. Write only that spec file. Do not commit and do not
   regenerate any index.
6. Run the spec-token checker with its spec flag over the revised spec and fix every hit it names. Do not run the whole-tree
   memory hygiene gate, and do not ask any checker for its help text. A figure before a unit word carries PINNED on its line,
   a code citation is a symbol citation, a scope item that takes something away carries its readers clause, and no sentence
   in section 2 uses a retirement word for something it keeps. A by-name reader in a Readers clause is a tracked path,
   never `path#symbol`; name the symbol in words after the path.
7. Never kill a process you did not start, and never match processes by a script's name to stop them: other sessions run the
   same scripts on this node.
8. Units 90 and 91 build at build order 45, and unit 92 at order 46; where this spec reads a sibling's or an earlier order's code, write it on that unit's committed spec and name the dependency in section 5. Your worktree may be cut from main, which lacks the
   loop kit: read every code claim from branch/unattended-declared-loop-d56bf0 through git show, and say which tree each
   check ran on.
   Never run check-memory-hygiene.sh, not even with --help. Keep each Readers clause's by name: and by value: halves each on
   one line, and name no unit id in a by name: half.
9. Four budgets and records stopped this build's earlier builders; name each the change reaches in section 5 with what
   keeps it green: the lexicon offender pin (every new function name through the lexicon's suggest verb), the shared
   records in `.unattended.conf`'s SHARED_RECORDS (a pass never writes `memory/DECISIONS.md`; spell out any decision row
   the run must land ahead), each script's refusal ceiling and its `.families.txt` families (measured with
   `tools/memory-tree/check-arms.py`'s own readers), and a help anchor for any new verb or flag.

### Acceptance

- Every claim the revised spec makes about current code is one you read at HEAD.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no new unit.
