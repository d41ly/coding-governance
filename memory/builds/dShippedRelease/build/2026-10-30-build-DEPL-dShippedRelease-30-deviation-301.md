# DEPL-dShippedRelease-30 deviation 301 — a root closed before leases gains its tombstone at its first draw

**Serves:** deviation DEPL-dShippedRelease-30

- **Departs from:** `cl-dClosedLoop-0440@13cc3301` [the closed root's tombstone]
- **Hand-off:** design-to-spec
- **Before:** a draw on a closed root always finding the root's tombstone, which is never pruned (cl-0134)
- **After:** a patch build raised by a landing, or a Maintain patch whose offender is a landed SHA, its intake keyed by (`default-branch-red`, landed SHA) so one red files one patch, drawing on the originating build's rework budget, so a chain of patch builds shares one budget, a draw on a closed root re-opening the root's transition record under the root's lease: the patch build acquires the root's terminal lease for that draw alone, its epoch bumped, and appends the draw and releases the lease terminal again in one push, so concurrent draws serialize on the acquisition's compare-and-swap, a draw on a closed root always finding the root's tombstone, or, on a root closed before dPlacedRequest landed tombstones, minting it with that first draw, the tombstone never pruned (cl-0134), the loser re-reading the remaining budget before it draws, each release retry drawing on it too, and each keep-waiting answer to a release hold counted per build and landed SHA, the third parking the build, seen red on a planted patch chain, on two planted concurrent draws on one closed root whose budget admits only one, both landing, on two such draws on a root closed longer ago than `leases.queued-claim-days`, neither refused, on a planted owner who answers keep-waiting three times and on a planted double filing of one red (P39, the parked debt's review, the owner's FK-1-5)
- **Cause:** design defect
- **Reason:** The clause assumes every closed root holds a tombstone. Measured at `f4597719`, the remote holds legacy `refs/gov/runs/*` claims and nothing else under `refs/gov/`, while 147 build READMEs read CLOSED, so the clause's "always" is false for nearly every root that could be patched. The first draw minting the tombstone keeps the clause's serialization and its "never pruned", and costs no backfill. An unknown slug is still refused, so nothing is minted for a build that never existed. Also follows through as: ask DEPL-dShippedRelease-32.
- **Evidence:** scout B disagreement 5 and fork F5, `memory/builds/dShippedRelease/build/2026-10-30-build-DEPL-dShippedRelease-11-reuse-scout-b.md:95`; pin C8 in the spec brief; DEPL-dShippedRelease-30 §8 F7
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of dShippedRelease's spec run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** amends cl-dClosedLoop-0440@13cc3301
- **Caused-by:** DEPL-dShippedRelease-30
