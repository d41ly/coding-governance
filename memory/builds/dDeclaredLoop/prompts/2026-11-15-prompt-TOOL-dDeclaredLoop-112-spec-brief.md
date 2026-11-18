**Serves:** research TOOL-dDeclaredLoop-112

# Brief: spec the repair unit TOOL-dDeclaredLoop-112, the cost of `--status` and `--resume` after the position engine

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. The run adopted this unit as a discovery with `--rescope --act add` on 2026-11-15, because it blocks
the run's own idle-wake ticks.

## What the run measured

- TOOL-dDeclaredLoop-7 (CLOSED, built at 1e11500da) S9 made `--status` print the position engine's lines and take its next
  unit from the engine's least-advanced unit. The engine, run with `GOV_POSITION_STATES` set empty, runs the driver's
  `--plan <slug>` for its hand-over (`tools/loop/position.py`, the hand-over reader).
- On node a at 1e11500da, `GOV_POSITION_STATES= bash tools/unattended/unattended.sh --plan dDeclaredLoop` took 11m25s
  real, 3m24s user and 6m22s sys over 111 units (all PINNED). `--status dDeclaredLoop` printed nothing within 400 s, and
  `--resume dDeclaredLoop --keepalive-id <id>` printed nothing within 600 PINNED s; before unit 7, `--resume` returned within
  about a minute. Every idle-wake tick runs `--resume`, then `--audit`.
- `memory/project/fork-ceilings.txt`'s `unattended-status` row measures `--status` over a one-build fixture with no
  units, so it cannot see a cost that scales with the roster, and it was re-set 47 to 45 by unit 7 while the real verb
  grew by minutes.

## The brief

### Goal

Write the spec of TOOL-dDeclaredLoop-112 at `memory/builds/dDeclaredLoop/spec/2026-11-15-spec-TOOL-dDeclaredLoop-112.md`,
Tier-2, status DEFERRED at rev-1, order 18 (it builds before the remaining order-18 units), streams tooling, with no
Carries line of its own but `**Derived:**` naming what it repairs, so that `--status` and `--resume` cost no more than they
did before unit 7 on a roster of this build's size, and the cost is gated so the class cannot return unseen.

### Items

1. Read unit 7's spec (CLOSED, rev-5) and the code it built: `tools/loop/position.py`, the `--plan` and `--status` paths of
   `tools/unattended/unattended.sh`, and `verb_resume`. Find where the time goes in `--plan`'s hand-over (per-row
   classification, spawns) and which callers need the engine's full answer.
2. Design the repair as one mechanism. Candidates to weigh in section 8, recommending one and writing the body on it:
   (a) `--status` and `--resume` take their next unit and position lines from a hand-over the driver builds without the
   per-row M2 classification, where a cheaper witness decides each row; (b) the per-row classification `--plan` runs is
   made cheaper, so every engine caller gains; (c) `--status` and `--resume` stop running the engine and a separate verb
   prints its lines. A CLOSED spec stays frozen: name each of unit 7's acceptance criteria the repair changes the
   observation of, and keep `--plan`'s `next:` shapes byte for byte.
3. Gate the class: a cost check whose fixture holds a roster large enough that a per-unit cost shows, with a declared
   wall-clock or spawn ceiling, so a later change that makes `--status` scale with the roster reds. Say what it does not
   check.
4. Write the full template: sections 1 to 10, the §3 edges, §5's write set naming every registry row, budget row, fork
   ceiling row, usage row, generated map file and existing arm the change could newly red, with what keeps each green, and
   §7's legs with a `New arm:` line.
5. Write only that spec file. Do not commit and do not regenerate any index. Run the spec-token checker with its spec flag
   over the new spec and fix every hit. Do not run the whole-tree memory hygiene gate, and do not ask any checker for its
   help text. A figure before a unit word carries PINNED on its line, a code citation is a symbol citation, a scope item
   that takes something away carries its Readers clause with its by name: and by value: halves each on one line, a by-name
   reader is a tracked path never `path#symbol`, and no by name: half names a unit id.
6. Never kill a process you did not start, never match processes by a script's name to stop them, and never run
   check-memory-hygiene.sh, not even with --help. A probe that runs `--plan`, `--status` or `--resume` over this build takes
   over ten minutes: run it in the background with a bound, or measure over a smaller fixture.

### Acceptance

- The spec names the measured cost, one mechanism that restores it, and a gate that reds when `--status` scales with the
  roster again; the spec-token checker reports no unwaived hit.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no edit to unit 7's CLOSED spec.
