**Serves:** research TOOL-dDeclaredLoop-115

# Brief: write the spec of TOOL-dDeclaredLoop-115, promoted from the closing diff review

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. The build's closing diff review converged at round 2 (records `memory/builds/dDeclaredLoop/reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md` and `memory/builds/dDeclaredLoop/reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md`), and under the owner's
2026-10-04 rule every confirmed finding is PROMOTED to a unit of this build: one per HIGH, the minors batched into one. This unit is
round 1's item 1 (HIGH, findings 1 and 2 merged): the push arm of `tools/loop/guard.py` reads only a merge's FIRST parent to decide whether a commit adds `.governance/policy.toml`, and its early continue on an absent first-parent policy keeps such a merge out of the re-merge grading and the parents-only grading, so a merge whose first parent lacks the file passes ungraded. Close it so such a merge is graded (the review's fix: read the absent first parent as an empty policy and fall through, matching the parents-only path's rule that a lacking parent reads as empty), with a plant for that topology, and bring `help/policy.md` and the module docstring current.

## The brief

### Goal

Write the NEW spec `memory/builds/dDeclaredLoop/spec/2026-11-17-spec-TOOL-dDeclaredLoop-115.md`, Tier-2, status DEFERRED, order 52, streams tooling, one mechanism that closes the finding(s)
above, in the shape `memory/TEMPLATE-SPEC.md` gives, so a builder can build it as written over the branch tip.

### Items

1. Your worktree may be cut from main, which lacks the loop kit: read every code claim from branch/unattended-declared-loop-d56bf0
   through git show, read both review records whole, and say which tree each check ran on. Take the header, binding line and
   records region shape from `memory/builds/dDeclaredLoop/spec/2026-11-15-spec-TOOL-dDeclaredLoop-112.md`, a unit this build added
   mid-run, and leave the `<!-- gen:spec-records -->` region empty for the index to fill.
2. Every unit of the build's roster through order 51 is CLOSED (unit 34 deferred against ask TOOL-dDeclaredLoop-113) and frozen:
   never plan an edit to a CLOSED spec. Units 115, 116 and 117 build in that order at orders 52, 53 and 54; 116 and 117 both touch
   `tools/loop/loop_lib.py`.
3. THE SWEEP: for every function, file, constant and fixture the body changes, find every caller, reader, fixture, suite arm and
   pinned contract (census and family ceilings, the lexicon pin, help anchors and usage rows, budget rows) at the branch tip, and say
   in section 5 what keeps each green, with the commands that re-derive the counts.
4. Each acceptance criterion names an observation a pass can make without a gate, and its staged break. Declare each new or moved
   arm on a `New arm:` line in section 7. A choice between designs is a section 8 fork with a recommendation, ending with its own
   `RESOLVED (agent, 2026-11-17, delegated): (<option>)` mark.
5. Name each budget the change reaches in section 5: the lexicon offender pin (1215; every new function name through the lexicon's
   suggest verb), SHARED_RECORDS in `.unattended.conf` (a pass never writes `memory/DECISIONS.md`), each script's refusal ceiling and
   `.families.txt`, and a help anchor for any new verb or flag. Every PLANTS description names a conf in words, never by its file
   name. A figure before a unit word carries PINNED; a code citation is a symbol citation, never a bare path:line.
6. Write only that spec file. Do not commit and do not regenerate any index. Run the spec-token checker with its spec flag over the
   spec and fix every hit. Do not run the whole-tree memory hygiene gate, and do not ask any checker for its help text.
7. Never kill a process you did not start, and never match processes by a script's name to stop them.

### Acceptance

- The spec closes its finding(s) with one mechanism, every claim about code is one you read at the tip, every fork carries a mark,
  and the spec-token checker reports no unwaived hit.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no other unit.
