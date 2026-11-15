**Serves:** research TOOL-dDeclaredLoop-46

# Brief: revise spec TOOL-dDeclaredLoop-46 after its builder's divergence, the version origin/main already shipped

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. The first dispatch of TOOL-dDeclaredLoop-46 returned a divergence before any write: origin/main at
179486e8f already ships `KIT_RUN_GATES_VERSION=1.48`, minted by the aMeasuredDrag landing 30bb17eb4, and its canary's two
`KNOWN` copies admit no `stage`. S1 as written mints 1.48 again, so `STAGE_FLOOR_RUN_GATES` would name a shipped runner that
refuses the key. The return is `memory/builds/dDeclaredLoop/build/2026-11-15-build-TOOL-dDeclaredLoop-46-1-builder-return.md`.

## The brief

### Goal

Revise `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-46.md` as rev-5, with one revision-log line naming
that return, so its version and floor stay above every shipped runner whose canary lacks `stage`.

### Items

1. Your worktree may be cut from main. First replace your copy of the spec with the branch's, through
   `git show branch/unattended-declared-loop-d56bf0:<path>`, and read every code claim from that branch and from
   `origin/main` the same way. Read the return whole.
2. S1: the new version is one above the higher of the branch's value and the default branch's remote-tracking value, and
   `STAGE_FLOOR_RUN_GATES` is that tuple. Re-pin §4 Evidence's origin/main reading, and derive AC1's starting figure from the
   higher of the two values.
3. Say in §5, or as an acceptance criterion, how the floor stays above every shipped version without the admission if
   origin/main mints again before this build lands: for example a close-time probe that compares the floor with
   origin/main's runner version and canary. If that is a choice, it is a section 8 fork with your recommendation.
4. Name the landing's reconcile of the version marker in §5: what the close does when origin/main's runner version moves
   between this pass and the landing.
5. Keep the unit one mechanism, its carries, its order and its INPROGRESS status. Write only that spec file. Do not commit and do
   not regenerate any index. Run the spec-token checker with its spec flag over the spec and fix every hit. Do not run the
   whole-tree memory hygiene gate, and do not ask any checker for its help text. A figure before a unit word carries PINNED on
   its line, and each Readers half sits on one line.
6. Never kill a process you did not start, never match processes by a script's name to stop them, and never run
   check-memory-hygiene.sh, not even with --help.

### Acceptance

- No reading of the revised spec mints a run-gates version origin/main has already shipped, and the spec-token checker
  reports no unwaived hit.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no new unit.
