**Serves:** research TOOL-dDeclaredLoop-24

# Brief: revise spec TOOL-dDeclaredLoop-24 after its builder's divergence

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. The dispatch of TOOL-dDeclaredLoop-24 returned a divergence before any write: its composition read refuses
the first render of a default install whose loop definition is staged but not yet committed. The return is
`memory/builds/dDeclaredLoop/build/2026-11-14-build-TOOL-dDeclaredLoop-24-1-builder-return.md`.

## The brief

### Goal

Revise `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-24.md` in place, as a rev bump with one revision-log
line naming that return, so a builder can build it with govkit selftest's default-apply arm and every first render still green.

### Items

1. Read the return, then `render_playbook.py` and `instruction_units.py` yourself where the composition read reaches `git show
   HEAD:` and where a failed read becomes a Refusal. Settle in S3, section 4's composition read, AC12 and section 5 what
   `derive_kind_composition` answers when the namespace source is absent at HEAD but present on disk. Weigh answering None as
   for a missing schema, answering zero gov rows, and reading gov's rows from the working tree; write it as a section 8 fork
   with your recommendation and the body on it.
2. Add an acceptance criterion that renders over an install not yet committed, and name govkit selftest's default-apply arm in
   section 5 with what keeps it green.
3. The new leg runs in the `selftests` chunk, so add its row in `tools/run-gates/selftest-budgets.txt` to Files touched, with how
   the budget is read.
4. The record-version rule compares a pinned hash with a recomputed one, so a re-pinned hash with no version bump stays green.
   Say in section 5 what the rule does not check, or make it compare against the row at a base; if that is a choice, it is a
   section 8 fork with your recommendation.
5. Keep the unit one mechanism, its carries, its order and its INPROGRESS status. Write only that spec file. Do not commit and do
   not regenerate any index. Run the spec-token checker with its spec flag over the revised spec and fix every hit. Do not run
   the whole-tree memory hygiene gate, and do not ask any checker for its help text. A by-name reader in a Readers clause is a
   tracked path, never `path#symbol`.

### Acceptance

- The revised spec says what a render over an uncommitted install answers, and an acceptance criterion observes it.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no new unit.
