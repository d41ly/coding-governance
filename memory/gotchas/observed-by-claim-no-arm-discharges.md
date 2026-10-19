---
name: observed-by-claim-no-arm-discharges
description: a spec scope item says a behaviour is "Observed by ACn", the arm that criterion names never reads the surface the behaviour renders on, and a staged break of the behaviour leaves the suite green
kind: class
universal: false
---

# The scope item's "Observed by" names an arm that never reads its surface

## Symptom

A scope item says its behaviour is "Observed by AC3". AC3 exists, its arm exists, and the arm is
sound: it fails when ITS surface breaks. But the behaviour the scope item adds renders somewhere
else — a log line, a second exit path, a note on another branch of a ternary — and the arm never
reads that place. Break the behaviour on the surface the scope item names and the suite stays green.

Each half reads as correct on its own. The criterion can fail, so a could-not-fail review passes it;
the scope item cites a real criterion, so the shape grader passes it. The defect is only in the JOIN
between the two, and nothing reads that join.

The tell: one behaviour rendered on two or more surfaces, routed through one shared helper, with the
cited arm reading the first surface only. A helper reused on a death path or a deferred path is the
usual second surface.

## Where it bit

This build's closing review, round 1, findings 13 and 14 (the record is
memory/builds/aSightedSkeptic/reviews/2026-10-01-review-TOOL-aSightedSkeptic-1-closing-diff-round1.md).
Two specs said their binding grade, their fix rendering and their uncertain count were "Observed by"
arms that read the synthesis prompt's CONFIRMED section and the result counts. The same values also
rendered on the synthesis-death log, the deferred-batch log, RUN INTEGRITY and the success note, and
staging a break on each of those lines left all of `tools/workflows/tier2-review.test.sh` green. The behaviour was
correct; the claim that something observed it was not.

It bit again in `TOOL-dSweptBranches-21` (the follow-up review of dSweptBranches, finding 8). A spec's
§7 `New arm:` line named a staged five-second delay as the arm's condition, and the delay lived only
in a scratch edit whose bytes were restored. The arm in the tree runs undelayed, so reverting the
spawn poll to a fixed wait leaves it green. A staged condition that is not in the shipped arm is an
observation by hand: say so on the line.

It bit again in `TOOL-dRenderedAnchor-3`, whose S1 named AC1 and AC13 as the observers of the
citation pass's harness branch in `tools/roles/roles_lib.py`, the tool root as `here` for a
`workflow`-driver harness. Both criteria hold their harnesses under the tool root, which either value
of `here` reaches, so staging the branch as `here = kit` left them and arms 14 to 16 green (the
closing review's round 3, M1, ids 1, 3 and 5). `TOOL-dRenderedAnchor-4` added arm 17 to
`tools/roles/adopt-roles.test.sh`, whose harnesses sit only above the tool root with no receipt. The
check: each branch of a conditional resolver needs a fixture whose answer depends on that branch,
observed red against the collapsed branch.

## The fix

Stage the break of the scope item's OWN surface and watch the cited arm go red. Never read the arm
and agree that it covers the behaviour — reading is how both of these shipped. Where the behaviour
renders on several surfaces, either one arm reads each, or the scope item names the one surface its
criterion reads and says the others are unobserved. Each new arm counts what it reads before grading
it, so a run that rendered nothing is red rather than vacuously green.

## Related

[[criterion-asserts-what-its-own-command-cannot-show]] is the criterion-level sibling: there the
criterion cannot fail at all. [[fixture-passes-by-finding-nothing]] is the test-level one: there the
arm reads the right surface and finds an empty population.

## Its gate

No machine gate. A spec-ledger check that each "Observed by ACn" line in a spec under `/spec/` names
an arm whose assertions mention the line's output surface would need a join from an acceptance label
to an arm's assertions, and nothing in the tree builds one; the shape grader behind
`memory/TEMPLATE-SPEC.md` reads the scope join's SHAPE only. It is a documented check: a reviewer
stages the break.
