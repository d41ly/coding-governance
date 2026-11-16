**Serves:** research TOOL-dDeclaredLoop-33

# Brief: revise spec TOOL-dDeclaredLoop-33 after its second builder return, with F7's amends record and the re-pinned carry

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. The second dispatch of TOOL-dDeclaredLoop-33 returned a divergence before any write. The return is
`memory/builds/dDeclaredLoop/build/2026-11-16-build-TOOL-dDeclaredLoop-33-2-builder-return.md`. It names three blockers, each
measured at 440236882: S11's boundary check through `check_program` refuses the compositions of four `loop adapt fixtures`
plants (the lint-pass add row carries no outcomes; the loosening plant's exclusion leaves `item.test.route` routing to the
excluded `item.test.flakes`); gov's pending list goes stale over any build's composition that excludes or supersedes an item a
pending row names; and F7's departure needs an `amends` deviation record, which moves `cl-dClosedLoop-0118`'s hash in the
as-built view, so the spec's `**Carries:**` pin must move with it in the same commit, as deviation 61 did for unit 6. It also
lists four minor points to fold.

## The brief

### Goal

Revise `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-33.md` as rev-8, with one revision-log line naming
that return, and write F7's `amends` deviation record beside it, so a builder can build the spec as written at HEAD.

### Items

1. Your worktree may be cut from main. First replace your copy of the spec with the branch's, through
   `git show branch/unattended-declared-loop-d56bf0:<path>`, and read every code claim from that branch the same way. Read the
   return whole, and read `memory/builds/dDeclaredLoop/build/2026-10-24-build-TOOL-dDeclaredLoop-6-deviation-61.md` and the
   commit that landed it as the precedent for item 4.
2. Blocker 1 is a section 8 fork: (a) the boundary grades a composition `check_program` refuses as a finding of its own, so a
   flow change that breaks the program is refused for that reason; (b) the adapt plants change to compose a well-formed
   program, which puts `tools/loop/adapt.py`'s plants in this unit's scope and write set; (c) another you find. Measure each
   over the four plants and over gov's composition, recommend the one that keeps every existing `loop adapt fixtures` case
   green with the smallest change, mark it RESOLVED (agent, 2026-11-16, delegated), and write S11, AC9 and the sweep on it.
3. Blocker 2 is a section 8 fork: staleness graded over gov's own composition only, or a build's composition reading gov's
   list with rows whose item it excluded set aside, or another. Recommend, resolve and write §4 "The pending list" and S5 on
   it, and show over the loosening plant's composition that no stale finding appears.
4. Blocker 3: write F7's departure as a deviation record under `memory/builds/dDeclaredLoop/build/`, following deviation 61's
   shape, with an `amends` follow-through carrying the amended clause text as **After:**, cause design defect, approver
   spec writer. Derive the clause's new hash with `design_lib.derive_clause_hash` over the as-built row that record would
   produce, and re-pin the spec's `**Carries:**` line to it. Keep every backticked token of the clause in a carrier.
5. Fold the return's four minor points into §4 and AC2.
6. Re-run the spec's sweep for anything the change reaches, and keep everything else, including F9, F12 and the 23 cycles.
7. Keep the unit one mechanism, its order and its INPROGRESS status. Write only that spec file and that one deviation record.
   Do not commit and do not regenerate any index; return the record's path and the hash you derived. Run the spec-token
   checker with its spec flag over the spec and fix every hit. Keep the `<!-- gen:spec-records -->` region and its closing
   marker exactly as the branch has them. Do not run the whole-tree memory hygiene gate, and do not ask any checker for its
   help text.
8. Never kill a process you did not start, never match processes by a script's name to stop them, and never run
   check-memory-hygiene.sh, not even with --help.

### Acceptance

- Every blocker the return names is settled in the body, the four adapt plants and gov's composition both pass the revised
  checks by the spec's own probes, and the spec-token checker reports no unwaived hit.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no new unit.
