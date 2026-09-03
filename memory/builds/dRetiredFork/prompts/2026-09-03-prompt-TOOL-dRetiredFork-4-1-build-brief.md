# Build brief — TOOL-dRetiredFork-4

**Serves:** journal TOOL-dRetiredFork-4

## What the unit is

A RECONCILIATION, not an absorption. An adopter carries a divergence row asserting a gov defect;
rev-1 paraphrased it and got the shape wrong, rev-2 measured the WRONG SHAPE and called it refuted.
This unit obtains the actual claim, runs it, and disposes of it on evidence.

## What S1 found, and it changes the unit again

inCMS's D1, read verbatim from `C:/projects/incms/main/.claude/hooks/agent-cap.js:21-27`, is about
NESTED TEMPLATE INTERPOLATION — `renderCodeView` keeping interpolation brace depth in ONE scalar that
every `${` push zeroed. It is NOT about a nested sequential-agent LOOP.

So rev-1 described the wrong mechanism, and rev-2's refutation measured a nested LOOP fixture
(`agent-cap.test.sh:357`) which has nothing to do with D1. Both revisions were arguing about a
fixture the adopter never claimed.

## What to measure

The scalar is still there at gov HEAD: `agent-cap.js:233` and `:639` both do
`stack.push('interp'); interpDepth = 0`, one scalar, not saved with the frame. So the CODE SHAPE D1
names is present. The question is whether the FAIL-OPEN it observed is still reachable.

A first fixture will not exercise it: the zeroing only matters when the OUTER interpolation already
carries a non-zero brace depth when the inner `${` appears. The fixture must be
`` `a ${ f({ k: `b ${ x } c` }) } d` `` — with `f({` opening a brace inside the outer interpolation.

## Acceptance

AC1-AC4. Record the fixture, the invocation and both exit codes verbatim; pick exactly one
disposition from S3 and name its evidence; write the reconciliation into `memory/DECISIONS.md`, so
the next session reading that register row does not repeat rev-1's error a third time.
