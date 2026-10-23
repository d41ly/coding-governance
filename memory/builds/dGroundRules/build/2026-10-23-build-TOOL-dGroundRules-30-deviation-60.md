# TOOL-dGroundRules-30 deviation 60 — the spec revised past its audited revision by the disposals' edges

**Serves:** deviation TOOL-dGroundRules-30

- **Departs from:** TOOL-dGroundRules-30@rev-1 [§3 edges]
- **Hand-off:** spec-revised
- **Before:** TOOL-dGroundRules-30's spec at rev-1, the revision its spec audit pinned at `b9f7b5c4e`.
- **After:** at `0ced625e1`, the hands-off edge to `TOOL-dGroundRules-43`.
- **Cause:** review finding
- **Reason:** a later audit round or the closing review promoted units that consume from TOOL-dGroundRules-30, and each promoted unit's consumes-from edge owes its reciprocal hands-off line here, a rev bump with its §9 line; a trim took the spec back under the ceiling after the closing review's generated records row joined it. Neither moves the unit's scope, design or acceptance.
- **Evidence:** commit `0ced625e1`; TOOL-dGroundRules-30's §9 lines for those revisions.
- **Risk:** editorial
- **Approver:** author, the run's main loop, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dGroundRules-12
- **Caused-by:** PLAY-dClosedLoop-2
