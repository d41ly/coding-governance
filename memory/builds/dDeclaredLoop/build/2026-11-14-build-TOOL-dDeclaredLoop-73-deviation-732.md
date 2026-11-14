# TOOL-dDeclaredLoop-73 deviation 732 — TOOL-dDeclaredLoop-73's spec revised before its build

**Serves:** deviation TOOL-dDeclaredLoop-73

- **Departs from:** `TOOL-dDeclaredLoop-73@rev-2`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dDeclaredLoop-73`'s spec as the revision at `TOOL-dDeclaredLoop-73@rev-2` reads it.
- **After:** the spec at rev-3: each kit's requires are read through the registry at the target vintage with the existing descriptor reader, the registry read is shared, and §8 F2 is resolved to (b).
- **Cause:** design defect
- **Reason:** rev-2 read requires at the working tree's descriptor paths, which would refuse the upgrade-walk leg's rollback to release 0, where the loop kit's descriptor does not exist.
- **Evidence:** `memory/builds/dDeclaredLoop/prompts/2026-11-14-prompt-TOOL-dDeclaredLoop-73-reground-brief.md`, and the rev-3 line in this spec's §9.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer handoff of this revision, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); the fork picks are the run's under its mandate
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-14-prompt-TOOL-dDeclaredLoop-73-reground-brief
