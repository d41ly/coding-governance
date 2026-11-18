**Serves:** research TOOL-dDeclaredLoop-32

# Brief: revise spec TOOL-dDeclaredLoop-32 after its first builder return, the driver-suite arms

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. The first dispatch of TOOL-dDeclaredLoop-32 built rev-5 nearly whole, then returned a divergence: two of its
scope items change behaviour `tools/unattended/unattended.test.sh` already asserts, and §5's sweep names neither the arms nor how
each stays green. The no-fall rule for spec subjects makes a flat spec subject read CONVERGING under the suite's fixed-count-7
policy, so four arms that drive a spec subject to NON-CONVERGENT and promote (subjects `F1 (fork)`, `S1`, `D2`, `S8`) are
refused; and the promotion target on every promoting exit changes eight exact-row assertions. The return is
`memory/builds/dDeclaredLoop/build/2026-11-16-build-TOOL-dDeclaredLoop-32-1-builder-return.md`; the builder's work is saved as a
patch the next builder will reuse.

## The brief

### Goal

Revise `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-32.md` as rev-6, with one revision-log line naming
that return, so §5's sweep names every suite arm the change reaches and how each is kept green or re-planted.

### Items

1. Your worktree may be cut from main. First replace your copy of the spec with the branch's, through
   `git show branch/unattended-declared-loop-d56bf0:<path>`, and read every code claim from that branch the same way. Read the
   return whole.
2. Write the four spec-subject arms' re-plant as a section 8 fork. Options include re-planting each on the build slug (whose
   closing bound still reaches NON-CONVERGENT and promotes), planting a BOUNDED exit where the arm tests the row's shape, or
   retiring an arm whose path no longer exists, with its readers. Recommend by the ratify rule, preferring the option that
   keeps what each arm tests; mark it RESOLVED (agent, 2026-11-16, delegated) and write the body on it, naming each arm.
3. Name the eight exact-row assertions the return lists, each re-pointed to carry ` · to units` before the disposition, in §5
   and in §4 Files touched.
4. Re-run the sweep's `review_state` and `verb_review` rows over the suite at the branch tip and record every arm that drives
   either, with its fate.
5. Keep the unit one mechanism, its carries, its order and its INPROGRESS status. Write only that spec file. Do not commit and do
   not regenerate any index. Run the spec-token checker with its spec flag over the spec on the branch's tree and fix every
   hit. Do not run the whole-tree memory hygiene gate, and do not ask any checker for its help text. Keep the spec's
   `<!-- gen:spec-records -->` region and its closing marker exactly as the branch has them.
6. Never kill a process you did not start, never match processes by a script's name to stop them, and never run
   check-memory-hygiene.sh, not even with --help.

### Acceptance

- Every suite arm the change reaches is named in §5 with its fate, and the spec-token checker reports no unwaived hit.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no new unit.
