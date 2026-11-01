# DEPL-dShippedRelease-4 deviation 42 — what reaches the tree after a landing rides one records landing on the default path, and a held close lands its transition alone

**Serves:** deviation DEPL-dShippedRelease-4

- **Departs from:** `cl-dClosedLoop-0415@82cfbcec` [deploy.close]
- **Hand-off:** design-to-spec
- **Before:** the spec brief's pin C3: the mailbox's copies, the terminal snapshot and the transition's folder copy ride ONE records-only commit landed through the lander
- **After:** the deploy engine, its `deploy.unlease` closing its mailbox first, every message still on its ref, disposed or not, copied into the build folder with the undisposed ones marked, and only then the ref pruned, seen on a planted build unleased with an undisposed message, its marked copy in the folder before its ref is pruned, and then closing each of a build's leases with a terminal tombstone and never deleting it, seen red on a queued claim replayed against an unleased build, which is refused, one records-only landing carrying the mailbox's copies, the snapshot and, where the close is due, the transition's copy, and `deploy.close` landing that copy alone where a release, a red landing or a review holds the close (P40, the parked debt's review)
- **Cause:** design defect
- **Reason:** The clause names no commit; pin C3 does, and it holds on the default path only. Under `build.closes: after-release-verifies` with `close-only`, on a red landing and under an open landing review the mailbox must close while the close itself is days away (`flow-steps.md:88-89`), so at the commit no transition exists to copy. A brief pin found wrong takes a deviation record and not a second answer, the brief's rule. The invariants the pin protects stand on every path: nothing bypasses the lander, every commit is gated, no ref is pruned before its copy is on the default branch, and a records landing raises no landing record. Also follows through as: usage deploy.close.
- **Evidence:** `flow-steps.md:84-90` and `:446`, `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`; the snapshot's commit, `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-2.md` S5; DEPL-dShippedRelease-4 §4 "The one commit" and §8 F3
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of dShippedRelease's spec run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); carried for the owner's walk unless it rules otherwise
- **Follow-through:** amends cl-dClosedLoop-0415@82cfbcec
- **Caused-by:** DEPL-dShippedRelease-4
- **Supersedes:** 2026-10-30-build-DEPL-dShippedRelease-4-deviation-41
