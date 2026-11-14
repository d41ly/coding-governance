# TOOL-dDeclaredLoop-24 deviation 243 — TOOL-dDeclaredLoop-24's spec revised before its build

**Serves:** deviation TOOL-dDeclaredLoop-24

- **Departs from:** `TOOL-dDeclaredLoop-24@rev-4`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dDeclaredLoop-24`'s spec as the revision at `TOOL-dDeclaredLoop-24@rev-4` reads it.
- **After:** the spec at rev-5: derive_kind_composition answers None when HEAD holds no copy of the loop definition and reads it at HEAD through tree_lib.read_blobs_at (F9), AC14 renders over an install not yet committed, the selftest-budgets row joins the write set, and section 5 names the record-version re-pin gap (F10).
- **Cause:** builder discovery
- **Reason:** the builder found that rev-4's git show HEAD read refuses the first render of a default install, whose loop definition govkit apply stages but does not commit.
- **Evidence:** `memory/builds/dDeclaredLoop/build/2026-11-14-build-TOOL-dDeclaredLoop-24-1-builder-return.md`, and the rev-5 line in this spec's §9.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer handoff of this revision, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); the fork picks are the run's under its mandate
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-14-build-TOOL-dDeclaredLoop-24-1-builder-return
