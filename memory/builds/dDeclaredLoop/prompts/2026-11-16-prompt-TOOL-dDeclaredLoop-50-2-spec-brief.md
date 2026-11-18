**Serves:** research TOOL-dDeclaredLoop-50

# Brief: revise spec TOOL-dDeclaredLoop-50 after its first builder return, the four review rows defined

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. The first dispatch of TOOL-dDeclaredLoop-50 returned a divergence before any write: spec 50 §2 S1 and §4
"The rows" give the needs, outcomes, witnesses and routes of `item.review.trigger`, `item.review.dispose`, `item.review.fold` and
`item.review.cost` "as unit 20 gives them", while unit 20 (CLOSED, rev-5, its §8 F4) wrote no row and its §4 "The item rows"
says unit 50 sets the outcome words and route targets. No spec names them. The return is
`memory/builds/dDeclaredLoop/build/2026-11-16-build-TOOL-dDeclaredLoop-50-1-builder-return.md`; it lists which of unit 20's prose
routes have no target the checks admit without a design choice, and that declaring the dispose row makes build row B10 pass only
if dispose routes the outcome `unit` to `transition`.

## The brief

### Goal

Revise `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-50.md` as rev-4, with one revision-log line naming
that return, so §4 "The rows" defines all six review rows in full and a builder can write them as specified.

### Items

1. Your worktree may be cut from main. First replace your copy of the spec with the branch's, through
   `git show branch/unattended-declared-loop-d56bf0:<path>`, and read every code claim from that branch the same way:
   `tools/loop/loop_lib.py#check_program`, `tools/loop/loop_table.py#check_transition_tables`, the build table's rows and its
   `[[stand-in]]` and `[[owed-row]]` rows in `tools/loop/loop.toml`, and unit 20's CLOSED spec and code (`--trigger`,
   `review_dispose.py`, the harness). Read the return whole.
2. In §4 "The rows", give each of the six rows its `outcomes` list, its `routes` table (each target a declared review tag,
   `transition` or a named `stand-in:{prefix}/...`), its witness `{ class, by }`, its `owner`, its needs and its actor, grounded
   on what unit 20's built code does. The dispose row's owner matches its stand-in row, and it routes `unit` to `transition`
   so build row B10 still passes.
3. In §5, list every cross-step route the rows make and how each passes `check_transition_tables`: covered by an existing build
   row, or by a new build row or `[[owed-row]]` row this unit adds, named in Files touched. Where a route has more than one
   admissible target, write a section 8 fork with your recommendation, mark it RESOLVED (agent, 2026-11-16, delegated) on the
   recommendation, and write the body on it.
4. Re-run the spec's sweep for anything the rows change, and keep everything else.
5. Keep the unit one mechanism, its carries, its order and its INPROGRESS status. Write only that spec file. Do not commit and do
   not regenerate any index. Run the spec-token checker with its spec flag over the spec and fix every hit. Keep the
   `<!-- gen:spec-records -->` region and its closing marker exactly as the branch has them. Do not run the whole-tree memory
   hygiene gate, and do not ask any checker for its help text.
6. Never kill a process you did not start, never match processes by a script's name to stop them, and never run
   check-memory-hygiene.sh, not even with --help.

### Acceptance

- Each of the six rows is fully specified, every route passes the transition-table check or is covered by a row this unit adds,
  and the spec-token checker reports no unwaived hit.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no new unit.
