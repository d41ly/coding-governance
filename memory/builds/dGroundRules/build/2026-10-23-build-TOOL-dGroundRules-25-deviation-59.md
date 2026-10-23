# TOOL-dGroundRules-25 deviation 59 — the spec revised past its audited revision by the disposals' edges

**Serves:** deviation TOOL-dGroundRules-25

- **Departs from:** TOOL-dGroundRules-25@rev-1 [§3 edges]
- **Hand-off:** spec-revised
- **Before:** TOOL-dGroundRules-25's spec at rev-1, the revision its spec audit pinned at `f4d31452a`.
- **After:** at `b9f7b5c4e`, the hands-off edges to `TOOL-dGroundRules-33`, `TOOL-dGroundRules-34`; at `c35750a56`, prose shortened under the 49152-byte spec ceiling, no meaning moved.
- **Cause:** review finding
- **Reason:** a later audit round or the closing review promoted units that consume from TOOL-dGroundRules-25, and each promoted unit's consumes-from edge owes its reciprocal hands-off line here, a rev bump with its §9 line; a trim took the spec back under the ceiling after the closing review's generated records row joined it. Neither moves the unit's scope, design or acceptance.
- **Evidence:** commit `b9f7b5c4e`, commit `c35750a56`; TOOL-dGroundRules-25's §9 lines for those revisions.
- **Risk:** editorial
- **Approver:** author, the run's main loop, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dGroundRules-12
- **Caused-by:** PLAY-dClosedLoop-2
