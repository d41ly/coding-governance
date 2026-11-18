# TOOL-dDeclaredLoop-14 deviation 144 — TOOL-dDeclaredLoop-14's spec revised before its build

**Serves:** deviation TOOL-dDeclaredLoop-14

- **Departs from:** `TOOL-dDeclaredLoop-14@rev-5`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dDeclaredLoop-14`'s spec as the revision at `TOOL-dDeclaredLoop-14@rev-5` reads it.
- **After:** the spec at rev-6: the size raise's decision row lands in memory/DECISIONS.md ahead of the pass, in a records commit, and the pass's files drop that record.
- **Cause:** builder discovery
- **Reason:** --dispatch's check 49 refuses any pass declaring memory/DECISIONS.md, a shared mutable record this project declares.
- **Evidence:** `memory/builds/dDeclaredLoop/build/2026-11-15-build-TOOL-dDeclaredLoop-14-2-builder-return.md`, and the rev-6 line in this spec's §9.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer handoff of this revision, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); the fork picks are the run's under its mandate
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-15-build-TOOL-dDeclaredLoop-14-2-builder-return
