**Serves:** research TOOL-dDeclaredLoop-25

# Brief: revise spec TOOL-dDeclaredLoop-25 after its second builder return, the step-gate plant

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. The second dispatch of TOOL-dDeclaredLoop-25 returned a divergence before any write: S6's step-gate
plant stages a definition holding every `[[step]]` table but the first, and the `drive` class's reader then raises through
`check_loop` (`the step step.plan is missing`), which the step gate reports as a refusal, exit 2, where AC5 needs
`step-gate: RED stage:step.plan`, exit 1, and govkit selftest's `[dSP-10] step-gate fixture stage` arm would newly red. The
return is `memory/builds/dDeclaredLoop/build/2026-11-15-build-TOOL-dDeclaredLoop-25-2-builder-return.md`.

## The brief

### Goal

Revise `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-25.md` as rev-7, with one revision-log line naming
that return, so S6, AC5 and §8 F7 can all hold over the shipped code.

### Items

1. Your worktree may be cut from main. First replace your copy of the spec with the branch's, through
   `git show branch/unattended-declared-loop-d56bf0:<path>`, and read every code claim from that branch the same way. Read the
   return whole.
2. Write the choice as a section 8 fork with the return's three options: (a) `render_playbook.py`'s `read_drive_rows` treats an
   unreadable definition as no order, changing the playbook kit's documented refusal; (b) the `stage` class's fixture case is
   admitted at exit 2 with the drive refusal named, which weakens AC5; (c) a member source for the class whose removal leaves
   `check_loop` passing. Look for (c) first, in the tree as built; recommend the option that keeps every written acceptance
   criterion and every existing arm green with the smallest change to another kit, and write the body on it. Correct F7's
   claim that an absent gov stage tag reds the gate where it in fact refuses.
3. Add the `[[class]] class = "stage"` row (`usage = "none"`, as the `item` class has) to §5's `tools/govkit/usage.toml`
   entries, and to Files touched.
4. The playbook kit's version bump is the close's: state that this unit does not bump `KIT_PLAYBOOK_RENDER_VERSION`, and drop
   it from Files touched.
5. Keep the unit one mechanism, its carries, its order and its INPROGRESS status. Write only that spec file. Do not commit and do
   not regenerate any index. Run the spec-token checker with its spec flag over the spec and fix every hit. Do not run the
   whole-tree memory hygiene gate, and do not ask any checker for its help text. Each Readers half sits on one line.
6. Never kill a process you did not start, never match processes by a script's name to stop them, and never run
   check-memory-hygiene.sh, not even with --help.

### Acceptance

- AC5 and govkit selftest's `[dSP-10] step-gate fixture stage` arm can both be observed green over the revised design, and the
  spec-token checker reports no unwaived hit.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no new unit.
