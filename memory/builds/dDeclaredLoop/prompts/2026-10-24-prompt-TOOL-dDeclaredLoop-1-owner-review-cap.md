**Serves:** research TOOL-dDeclaredLoop-1

# Owner instruction — at most two rounds of spec audit this run

## The prompt

> no more than 2 rounds of audits this run.

— owner, 2026-10-24, after the round-2 spec audit (run `wf_d32b8dfd-f54`) had returned and while one spec-writer
pass was clearing the round-2 promotions' check hits, before any round-3 audit had started.

## What the run was doing

- BUILD-METHOD M4: each promoted unit of a SPEC subject is audited as a SPEC, and each audit takes a fresh subject,
  so only a promoting round whose precision falls below the review protocol's floor ends the chain. Rounds 1 and 2
  read precision 1.00 and 0.93 and promoted 67 and 64 findings, into 21 and 11 units (`TOOL-dDeclaredLoop-36` to
  `-56`, then `-57` to `-67`). Nothing in the chain was converging.

## How the run applies it

- Round 1 audited the 34 roster specs and round 2 audited round 1's promotions, each disposing its findings by
  severity. No spec-audit round runs after round 2.
- Round 2's promotions are specced and recorded like round 1's, each with its departure record, and carried forward
  to the build run. No audit names them. They close under a recorded override of `specs-audited` citing this
  record, as M4 provides when a chain ends.
- The spec run's closing review over its spec commits would be a third review of the same spec-only diff, so it is
  not run; the build run's closing diff review is unaffected.
- The wrap-up names the round-2 promotions as unaudited.
