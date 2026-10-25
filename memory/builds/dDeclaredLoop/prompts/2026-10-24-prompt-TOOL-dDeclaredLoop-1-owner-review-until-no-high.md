**Serves:** research TOOL-dDeclaredLoop-1

# Owner instruction — audit until a round confirms no HIGH, then stop

## The prompt

> correction, run reviews until there are no HIGHs left, stop reviewing once it comes back without confirmed HIGH.

— owner, 2026-10-24, correcting the earlier cap
(`memory/builds/dDeclaredLoop/prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-owner-review-cap.md`, "no more than 2
rounds of audits this run"), after the run had committed round 2's promotions (`8d138b361`), deferred every unit
(`7af03e9bb`) and moved to VERIFYING (`07202550d`), before the keepalive was reaped or the landing prepared.

## What the run was doing

- Rounds 1 and 2 read 20 and 10 confirmed HIGHs, at precision 1.00 and 0.93, and promoted 21 and 11 units
  (`TOOL-dDeclaredLoop-36` to `-56`, then `-57` to `-67`). Under the cap, round 2 was the last.

## How the run applies it

- This record supersedes the two-round cap. The run returns to REVIEWING and audits each round's promotions, round
  3 auditing `TOOL-dDeclaredLoop-57` to `-67`, exactly as M4 runs the chain.
- The chain stops at the first round whose audit confirms no HIGH (and no BLOCKER). That round's findings are still
  disposed by severity: its MEDIUM and LOW findings are promoted to one batch unit, two only across disjoint write
  sets. Those last promotions are specced and carried forward unaudited, closing under a recorded override of
  `specs-audited` citing this record.
- The units already deferred stay DEFERRED: a status flip changes nothing an audit reads, and the harness reads
  their committed specs. Each unit a later round adds is deferred the same way before the close.
- The spec run's closing review over its spec commits is still not run: the audit chain is the review of this
  spec-only diff, and the build run's closing diff review is unaffected.
