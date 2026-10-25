**Serves:** research PLAY-dOrderedCharter-1

# Owner instruction — at most two rounds of spec review

## The prompt

> Important: no more than 2 rounds of spec reviews.

— owner, 2026-10-23, while the spec stage of `tools/workflows/unattended-build.js` (run `wf_3b06f35c-f18`) was
authoring the 37 roster specs, before any spec-audit round had run.

## What the run was doing

- BUILD-METHOD M4: each promoted unit of a SPEC subject is audited as a SPEC, and each audit takes a fresh subject,
  so only a promoting round whose precision falls below the review protocol's floor ends the chain. dFairHearing's
  chain ran five rounds and dSafePassage's seven before their owners stopped them, neither converging.

## How the run applies it

- Round 1 audits the 37 roster specs and disposes its findings by severity. Round 2 audits round 1's promotions and
  disposes its findings the same way. No spec-audit round runs after round 2.
- Round 2's promotions are specced and recorded like round 1's, each with its departure record, and carried
  forward to the build run. No audit names them. They close under a recorded override of `specs-audited` citing this
  record, as M4 provides when a chain ends.
- A spec whose round is CONVERGED or BOUNDED inside the two rounds is not re-reviewed for this cap's sake.
- The spec run's closing review over its spec commits is a third review of the same spec-only diff, so it is not
  run; the build run's closing diff review is unaffected.
- The wrap-up names the round-2 promotions as unaudited.
