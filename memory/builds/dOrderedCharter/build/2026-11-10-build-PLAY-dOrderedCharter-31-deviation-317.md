# PLAY-dOrderedCharter-31 deviation 317 — selfcheck's default-requires check reads only the members that are entries

**Serves:** deviation PLAY-dOrderedCharter-31

- **Departs from:** `PLAY-dOrderedCharter-31@rev-15` [Design]
- **Hand-off:** spec-to-code
- **Before:** the design's sketch of S11 passes `list(default_kits(reg))` whole to `derive_unsatisfied_requires`.
- **After:** the check passes the default members that are registry entries, `[k for k in default_kits(reg) if k in descs]`.
- **Cause:** builder discovery
- **Reason:** `tools/govkit/govkit.py#derive_unsatisfied_requires` indexes `descs[eid]` for each member, so a default member that is no entry would raise a `KeyError` inside selfcheck instead of the finding the line above it already prints for that member. The filter leaves that finding as the one answer and changes nothing for a default whose members are all entries, which gov's is.
- **Evidence:** a probe over the live registry returned `[]` for the default and `[('check-microformats', 'playbook-render')]` with `playbook-render` taken out, the pair AC17 names.
- **Risk:** editorial
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-31
