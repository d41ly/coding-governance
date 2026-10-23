# TOOL-dGroundRules-32 deviation 61 — the spec revised past its audited revision by the disposals' edges

**Serves:** deviation TOOL-dGroundRules-32

- **Departs from:** TOOL-dGroundRules-32@rev-1 [§3 edges]
- **Hand-off:** spec-revised
- **Before:** TOOL-dGroundRules-32's spec at rev-1, the revision its spec audit pinned at `b9f7b5c4e`.
- **After:** at `d794a81bc`, the hands-off edge to `TOOL-dGroundRules-52`.
- **Cause:** review finding
- **Reason:** a later audit round or the closing review promoted units that consume from TOOL-dGroundRules-32, and each promoted unit's consumes-from edge owes its reciprocal hands-off line here, a rev bump with its §9 line; a trim took the spec back under the ceiling after the closing review's generated records row joined it. Neither moves the unit's scope, design or acceptance.
- **Evidence:** commit `d794a81bc`; TOOL-dGroundRules-32's §9 lines for those revisions.
- **Risk:** editorial
- **Approver:** author, the run's main loop, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dGroundRules-12
- **Caused-by:** PLAY-dClosedLoop-2
