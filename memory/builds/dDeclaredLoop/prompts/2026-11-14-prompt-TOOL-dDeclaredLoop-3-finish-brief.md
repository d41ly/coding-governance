**Serves:** research TOOL-dDeclaredLoop-3

# Brief: finish the re-ground of spec TOOL-dDeclaredLoop-3

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. The first re-ground writer of TOOL-dDeclaredLoop-3, briefed by
`memory/builds/dDeclaredLoop/prompts/2026-11-14-prompt-TOOL-dDeclaredLoop-3-reground-brief.md`, wrote rev-5 into the working
tree and was cut off by an expired session before it ran the spec-token checker. That rev-5 is uncommitted.

## The brief

### Goal

Finish rev-5 of `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-3.md` in place, so it meets the re-ground
brief named above and a builder can build it as written over HEAD. Keep it rev-5 with its one revision-log line.

### Items

1. Read the re-ground brief above, then read the working-tree rev-5 whole against the code at HEAD, and correct any claim you
   cannot confirm there.
2. The spec-token checker names three hits on rev-5: `tools/loop/loop_transition.py`, a file not yet tracked, is spelled as a
   path; §4 names `memory/HYGIENE.md`, which trips the `kit/dogfood doc parity` leg's guard; and §4 names
   `tools/memory-tree/build_records.py`, which trips the `policy fixtures` leg's guard. Spell the untracked file the way a
   spec names a file the unit creates, and add each tripped leg to section 7's leg line.
3. Every section 8 fork the revision opened carries a recommendation and the body follows it; leave the RESOLVED marks to the
   run.
4. Keep the unit one mechanism, its carries, its order and its status. Write only that spec file. Do not commit and do not
   regenerate any index. Run the spec-token checker with its spec flag over the spec and fix every hit until none remains. Do
   not run the whole-tree memory hygiene gate, and do not ask any checker for its help text. A by-name reader in a Readers
   clause is a tracked path, never `path#symbol`.

### Acceptance

- The spec-token checker with its spec flag reports no unwaived hit on the finished rev-5.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no new unit.
