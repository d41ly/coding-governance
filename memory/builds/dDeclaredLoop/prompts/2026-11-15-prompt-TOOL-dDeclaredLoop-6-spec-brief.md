**Serves:** research TOOL-dDeclaredLoop-6

# Brief: revise spec TOOL-dDeclaredLoop-6 after its builder's divergence, the policy-key factory's gate

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. The first dispatch of TOOL-dDeclaredLoop-6 returned a divergence: the policy-key factory writes only the
catalogue and then runs the whole `policy check`, whose mirror-parity arm compares the working-tree `.governance/policy.json`
with the mirror rendered at HEAD, so the factory's own key always reds it and AC3's green can never be observed. The
return is `memory/builds/dDeclaredLoop/build/2026-11-15-build-TOOL-dDeclaredLoop-6-1-builder-return.md`; the builder's
work in progress is a patch the run keeps for the rebuild.

## The brief

### Goal

Revise `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-6.md` as rev-7, with one revision-log line naming
that return, so a builder can build it as written over HEAD with every acceptance criterion observable.

### Items

1. Your worktree may be cut from main. First replace your copy of the spec with the branch's, through
   `git show branch/unattended-declared-loop-d56bf0:<path>`, and read every code claim from that branch the same way. Read
   the return whole.
2. Write the choice as a section 8 fork. The run already discards option (a), the factory running `policy.py mirror --write`
   as a held renderer, because `.governance/policy.json` is in `tools/policy/guarded-paths.txt` and writing it widens the
   write surface §5 priced, the build method's veto 3. Write the body on (b): the mirror is the caller's step in §4's "What
   a factory leaves to its caller" table, and the policy-key factory's gate is narrowed to the arms that read the catalogue
   alone (the return names arm_shape, arm_schema and arm_summaries; confirm them against the code). Rewrite S4, AC3, AC10
   and the policy-key-new plant's outcome to match, and say in §5 what the narrowed gate no longer checks.
3. The hook factory's innermost gate, `check-hook-destinations.sh`, reads only tracked fragments, so it never reads the
   fragment the factory just wrote. State that limit in S5 or in §4's "what check-commands does not check", or have the
   factory stage its own files, as a fork with your recommendation; the builder's plant staged them and ran the gate again.
4. Keep the unit one mechanism, its carries, its order and its INPROGRESS status. Write only that spec file. Do not commit and do
   not regenerate any index. Run the spec-token checker with its spec flag over the spec and fix every hit. Do not run the
   whole-tree memory hygiene gate, and do not ask any checker for its help text. A figure before a unit word carries PINNED on
   its line, and each Readers half sits on one line.
5. Never kill a process you did not start, never match processes by a script's name to stop them, and never run
   check-memory-hygiene.sh, not even with --help.

### Acceptance

- Every acceptance criterion of the revised spec can be observed green over a factory's own write, and the spec-token checker
  reports no unwaived hit.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no new unit.
