**Serves:** research TOOL-dDeclaredLoop-62

# Brief: revise spec TOOL-dDeclaredLoop-62 after its first builder return, unit 61 as built

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. The first dispatch of TOOL-dDeclaredLoop-62 returned a divergence before any write: rev-3 was grounded before
TOOL-dDeclaredLoop-61 built (5fe74a281), and 61 took its own §8 option (b), extending `parallel-append` to draw the same item on
both sides and adding a `draw-id-rows` plant, where rev-3 expected a `parallel-append-identical` plant to join. The return is
`memory/builds/dDeclaredLoop/build/2026-11-16-build-TOOL-dDeclaredLoop-62-1-builder-return.md` and names three changes.

## The brief

### Goal

Revise `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-62.md` as rev-4, with one revision-log line naming
that return, so it builds over unit 61 as shipped.

### Items

1. Your worktree may be cut from main. First replace your copy of the spec with the branch's, through
   `git show branch/unattended-declared-loop-d56bf0:<path>`, and read every code claim from that branch the same way, unit 61's
   `tools/loop/budget.py` first. Read the return whole.
2. §4 "The plant" and S2: the shared branch keeps 61's same-item side draw for `parallel-append`; only `parallel-append-uneven`
   draws its own items on side; S2's "each on its own item" is limited to the new case.
3. §5 "dependency": name 61's extended `parallel-append` and `draw-id-rows` as what landed, and drop the joining clause.
4. Refresh the figures: PLANTS holds 17 keys; the `loop budget fixtures` row reads 339 from 226 PINNED seconds, and S4's re-price starts
   there; the help/loop.md quote is the text 61 wrote.
5. Change nothing else. Keep the unit one mechanism, its carries, its order and its DEFERRED status. Write only that spec file. Do
   not commit and do not regenerate any index. Run the spec-token checker with its spec flag over the spec and fix every hit.
   Keep the `<!-- gen:spec-records -->` region and its closing marker exactly as the branch has them. Do not run the whole-tree
   memory hygiene gate, and do not ask any checker for its help text.
6. Never kill a process you did not start, never match processes by a script's name to stop them, and never run
   check-memory-hygiene.sh, not even with --help.

### Acceptance

- Each of the return's three changes is made, and the spec-token checker reports no unwaived hit.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no new unit.
