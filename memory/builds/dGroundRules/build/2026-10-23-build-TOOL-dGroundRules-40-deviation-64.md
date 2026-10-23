# TOOL-dGroundRules-40 deviation 64 — the spec revised past its audited revision by the disposals' edges

**Serves:** deviation TOOL-dGroundRules-40

- **Departs from:** TOOL-dGroundRules-40@rev-1 [§3 edges]
- **Hand-off:** spec-revised
- **Before:** TOOL-dGroundRules-40's spec at rev-1, the revision its spec audit pinned at `d794a81bc`.
- **After:** at `c35750a56`, the hands-off edge to `TOOL-dGroundRules-59`.
- **Cause:** review finding
- **Reason:** a later audit round or the closing review promoted units that consume from TOOL-dGroundRules-40, and each promoted unit's consumes-from edge owes its reciprocal hands-off line here, a rev bump with its §9 line; a trim took the spec back under the ceiling after the closing review's generated records row joined it. Neither moves the unit's scope, design or acceptance.
- **Evidence:** commit `c35750a56`; TOOL-dGroundRules-40's §9 lines for those revisions.
- **Risk:** editorial
- **Approver:** author, the run's main loop, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dGroundRules-12
- **Caused-by:** PLAY-dClosedLoop-2
