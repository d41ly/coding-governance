# DEPL-dShippedRelease-4 deviation 41 — the mailbox closes before the build's tombstone, the reverse of the clause's wording order

**Serves:** deviation DEPL-dShippedRelease-4

- **Departs from:** `cl-dClosedLoop-0415@82cfbcec` [deploy.unlease]
- **Hand-off:** design-to-spec
- **Before:** its `deploy.unlease` closing each of a build's leases with a terminal tombstone and never deleting it, ... and closing its mailbox
- **After:** the deploy engine, its `deploy.unlease` closing its mailbox first, every message still on its ref, disposed or not, copied into the build folder with the undisposed ones marked, and only then the ref pruned, seen on a planted build unleased with an undisposed message, its marked copy in the folder before its ref is pruned, and then closing each of a build's leases with a terminal tombstone and never deleting it, seen red on a queued claim replayed against an unleased build, which is refused (P40, the parked debt's review)
- **Cause:** design defect
- **Reason:** The clause and `flow-steps.md:445` name the tombstone first, and TOOL-dWellOiledMachine-58 S5 admits a mailbox prune only from a writer holding the build's lease live, so a tombstone written first makes the prune refusable by the door. The order is the only one the door admits, and it is the order that spec's own `life.unlease` takes at S9. The clause's seen-red cases, a queued claim refused and a marked copy before the prune, are unchanged. Pin C5 rules it, rung 1. Also follows through as: usage deploy.unlease.
- **Evidence:** the door, `memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-58.md` S5 and S9; `flow-steps.md:445`, `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`; scout A disagreement 7, `memory/builds/dShippedRelease/build/2026-10-30-build-DEPL-dShippedRelease-1-reuse-scout-a.md:101`; DEPL-dShippedRelease-4 §8 F6
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer role of dShippedRelease's spec run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); carried for the owner's walk unless it rules otherwise
- **Follow-through:** amends cl-dClosedLoop-0415@82cfbcec
- **Caused-by:** DEPL-dShippedRelease-4
