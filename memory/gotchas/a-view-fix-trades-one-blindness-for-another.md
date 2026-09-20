---
name: a-view-fix-trades-one-blindness-for-another
description: a scanner that grades source through a rendered view has a blind spot, and building a better view moves it rather than closing it, each move a new fail-open or false-deny
kind: class
universal: false
---

# A view fix trades one blindness for another

**Class.** A scanner that grades source through a rendered VIEW has a blind spot. Fixing the blind
spot by building a better view moves it rather than closing it — and each move is a new fail-open or
a new false-deny, because the new view has its own unmodelled construct.

## Symptom

A review reports that the scanner is wrong about one shape. The fix changes which view the scanner
reads, or post-processes the view. The next review reports that the scanner is now wrong about a
DIFFERENT shape, in the opposite direction. The suite is green throughout, because every arm pins the
shape a review reported and none pins the axis.

## Where it bit

`tools/hooks/agent-cap.js`, the fan-out cap hook — the only mechanical control this repo has against
an agent burst — over four rounds of one closing review, `aWeldedTribunal`, 2026-09-04/05.

| round | reported | the fix | what the fix bought |
|---|---|---|---|
| 1 | a block comment mentioning `X.push(` revoked a bound (false DENY) | read the blanked view | it ERASES `${…}` bodies, so a real `` `${X.push(y)}` `` went invisible — FAIL-OPEN |
| 2 | that fail-open | strip block comments over the joined text | a regex literal's `/*` paired with the next real `*/` below it and deleted every take-back between — FAIL-OPEN |
| 3 | that fail-open | strip per line | the same pairing WITHIN one line — FAIL-OPEN |
| 4 | that fail-open | remove the strip; accept the false deny | closed |

Three consecutive folds each introduced a new fail-open on a security control, and the suite was
196, then 206, then 212 passed / 0 failed while they did.

## The root cause, and it is not any of those regexes

**The file models no regex literal, by a standing decision its own view header records.** Every
comment strip built on top of that inherits the blindness in a new shape. The rounds were not four
mistakes; they were one mistake made four ways.

## The fix

**Decide which direction the residual points, then stop moving the view.** Weigh the two errors:

- a FALSE DENY costs the author one reworded comment, and it is visible the moment it happens
- a FAIL-OPEN costs an unbounded agent burst, and it is invisible by construction

Where the scanner is a control rather than a convenience, take the false deny, NAME it in the code
beside the decision, and give it an arm that asserts the denial — so the residual is a stated
property rather than a bug someone will later "fix" and reopen the whole sequence.

## The gate

**Gated at `tools/hooks/agent-cap.test.sh`** by the frozen deny corpus this class produced — and the
general form is a **documented check**, because no static predicate separates "this fix moved the
blind spot" from "this fix closed it".

**A frozen corpus on the axis the fix CHANGES, not the axis the review reported.** Ten spellings of
the mutation could not catch any of the three fail-opens above, because the mutation was never what
changed — the VIEW was. The corpus that works is the cross product: every shape that must deny,
crossed with every rendering context the scanner can encounter it in.

**And measure every fold against the PRE-BUILD blob, in both directions.** Every one of these was
found by running the same payload against `BASE` and `HEAD` side by side and reading two exit codes.
None of them was visible in the diff, and none of them failed the suite.

## What this does NOT say

It does not say views are wrong, or that a scanner should never be improved. It says that when a
review reports a view-level defect, the question to ask first is *which direction should this
scanner's residual point*, and the answer is only sometimes "build a better view".
