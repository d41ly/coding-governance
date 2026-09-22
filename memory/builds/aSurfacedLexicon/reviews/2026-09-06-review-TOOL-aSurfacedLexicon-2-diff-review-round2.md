**Serves:** diff-review TOOL-aSurfacedLexicon-2 TOOL-aSurfacedLexicon-3 TOOL-aSurfacedLexicon-4 TOOL-aSurfacedLexicon-5 TOOL-aSurfacedLexicon-6 TOOL-aSurfacedLexicon-7 TOOL-aSurfacedLexicon-8 TOOL-aSurfacedLexicon-9 TOOL-aSurfacedLexicon-11 TOOL-aSurfacedLexicon-12 TOOL-aSurfacedLexicon-13 TOOL-aSurfacedLexicon-14

# Closing review round 2 — the fix, not the diff again

Tier-2 closing diff review, round 2 · 2026-09-06 · node `a` · build `aSurfacedLexicon` · streams
tooling. Round 1 is `2026-09-06-review-TOOL-aSurfacedLexicon-2-diff-review-round1.md`: BLOCKED, 17
findings — three blockers, four highs, six mediums, four lows.

## Verdict: CLEAN WITH FIXES

**Confirmed-blocker count: 7 to 0.** Strictly smaller and zero, so the loop CONVERGED.

All seventeen graded CLOSED by a reviewer that re-derived each of the three blockers itself rather
than inheriting them — constructing the conf-only commit shape and checking which legs select it,
putting names the bar actually reds on through the suggester, and scaffolding a fresh repo to run the
first command the installed Skill documents.

## What round 1 found, and why it was the right last review to run

Round 1's finding is not any of its seventeen defects. It is the shape they share.

**The kit's SUPPLY surface was tested against scratch declarations while its DEMAND surface was tested
against the real tree.** `--suggest`, the scaffolder and the shipped Skill answer questions; `--check`
grades a corpus. Every fixture in the build exercised one side or the other, and nothing ever asked
whether the two agreed. All three blockers and three of four highs lived in that gap:

- `--suggest` returned `OK` for names the bar reds on, because it gated its checks on per-cell flags
  no declaration arms while the grader graded unconditionally. The installed Skill tells every agent
  in this repo to trust that answer.
- A freshly scaffolded adopter's first `--suggest` — the one command the Skill it just installed
  documents — exited 2, because the scaffolder emitted no cell block while the flag was required.
- A conf-only commit skipped the only leg grading the pins, cells and canon this build added. The
  two-sided pin's own red text instructs the author to produce exactly that commit shape.

**The fold built the arm that closes the class**, and built it wider than round 1 proposed. Round 1
suggested feeding every `--check` OFFENDER back through `--suggest`; over offenders alone the arm goes
blind on a clean cell, which is precisely where a routing bug hides, and a green tree would hand it an
empty population — the vacuous-fixture class this repo names more than any other. It now asks about
EVERY name each armed cell grades, and asserts two things per name: the verb says `OK` exactly when
the grader found no offence, and where the answer names a cell it is the cell the grader routed the
name into, selector and all. A `file` cell is asked with the PATH rather than the stem, which is what
an author actually holds, and which is what forces the stemming and the routing to happen in the right
order — without that, two of the findings are invisible to it.

Over this repo it asks 1776 names and makes 951 cell assertions, both counters asserted live so a
future empty population announces itself rather than passing. Three of the seventeen findings fail it
tree-wide today and a fourth fails it on a routed fixture.

## Round 2's own findings

Six, all LOW or informational, and two of them are this build's most persistent classes re-earned by
the commit that was fixing them:

- **The fold's provenance entry said FOUR and named THREE.** That is the numbers-in-prose class, in
  the paragraph rewritten to stop carrying it. The count is now not stated at all.
- **A dead local survived the fix.** The arming flags the suggester used to read are discarded now
  that both surfaces read one predicate set, and the variable was left assigned and unread. Named and
  discarded explicitly, so the next reader does not restore the gate that caused the blocker.

Both closed. The remaining four are recorded in round 1's successor notes rather than fixed: the
agreement arm's suffix half is vacuous at every call site because this tree has no suffix offenders,
two liveness arms assert over string literals rather than over their own predicate, and a fixture conf
arms flags a stricter reading would refuse. None changes a verdict; all four are the same shape as the
work above and are named so a later reader does not mistake a green run for a covered one.

## The limit of this review

The suite carrying nearly all of this build's arms is chunk `selftests`, and the push boundary sets
`GATE_FULL` and never `GATE_SELFTESTS`. So 509 arms are ON-DEMAND coverage, not push-time coverage.
The specs say so in writing and this record says so again, because a reader counting arms could
otherwise believe the merge bar runs them. It does not.
