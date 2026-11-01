# DEPL-dShippedRelease-12 deviation 121 — plan priority reads first-verified while no plan priority exists

**Serves:** deviation DEPL-dShippedRelease-12

- **Departs from:** `cl-dClosedLoop-0422@027c3b9f`
- **Hand-off:** design-to-spec
- **Before:** landings ordered through the landing queue it builds, as `landing.order` says, by plan priority then first verified, by first verified, or as the owner orders, each value seen on its planted queue
- **After:** landings ordered through the landing queue it builds, as `landing.order` says, by plan priority then first verified, which reads first verified with its reason printed while no plan priority exists in this build's closure, by first verified, or as the owner orders, each value seen on its planted queue, across nodes by a landing-turn ref the queue takes on the remote by compare-and-swap, two nodes' planted landings taking one turn seen red, and a planted `owner-orders` landing admitted with no order seen red (`gap-flow-08`, the owner's FK-4-7)
- **Cause:** design defect
- **Reason:** the priority field is dRankedPlan's (`cl-dClosedLoop-0369`), dRankedPlan is outside dShippedRelease's parent closure and holds no spec, so the default's first half has no input to read and no planted case can show it. Adding the parent changes the closure the packet pins, and refusing the default stops every landing, so the default reads its second half with a recorded reason, as pin C7 states. Also follows through as: ask DEPL-dShippedRelease-32.
- **Evidence:** the packet's Parents section; scout B disagreement 11 and fork F6; `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1168`; DEPL-dShippedRelease-12 §8 F4
- **Risk:** loosening
- **Approver:** spec writer, the gov-spec-writer stage of the harness's spec run for dShippedRelease, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); carried for the owner's walk unless it rules otherwise
- **Follow-through:** amends cl-dClosedLoop-0422@027c3b9f
- **Caused-by:** cl-dClosedLoop-0422@027c3b9f
