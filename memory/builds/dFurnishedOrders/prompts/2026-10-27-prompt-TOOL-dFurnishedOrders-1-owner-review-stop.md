**Serves:** research TOOL-dFurnishedOrders-1

# Owner instruction — stop the spec audit once no HIGH is left

## The prompt

> stop reviewing once there are no HIGHs left

— owner, 2026-10-27, while round 3 (run `wf_9ff204f4-f84`, auditing `TOOL-dFurnishedOrders-31` to `-37`) was
running.

## What the run was doing

- Under BUILD-METHOD M4 the chain runs until a promoting round's precision falls below the review protocol's floor or
  the owner stops it. Two rounds had finished: round 1 over the 20 roster units at precision 0.95 (BOUNDED, 2
  BLOCKER, 5 HIGH, 51 minors, promoted to units 22 to 30), and round 2 over units 22 to 30 at precision 0.98
  (CONVERGED, 0 BLOCKER, 6 HIGH, 37 minors, promoted to units 31 to 37). Round 3 was in flight.

## How the run applies it

- The first round that confirms no BLOCKER and no HIGH is the last: no further round starts after it. A round that
  still confirms a BLOCKER or a HIGH promotes as M4 says, and the round after it audits those promotions.
- That last round's promotions, its MEDIUM and LOW batch, are specced and recorded like every earlier round's, their
  check-spec-tokens and hygiene reds cleared, and carried forward to the build run. No audit names them. They close
  under a recorded override of `specs-audited` citing this record, as M4 provides when a chain ends.
- Every roster unit and every unit the rounds added is deferred, advancing `TOOL-dFurnishedOrders-21`, and the ask's
  DEFERRED row names the last unit in build order.
- The spec run's closing review over its spec commits is not run, under a recorded override of
  `closing-review-recorded` citing this record: its whole diff is specs and records, already read by the audit
  rounds, and the build run's closing diff review over its code meets it. The wrap-up names the last round's
  promotions as unaudited.
