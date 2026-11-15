# TOOL-dDeclaredLoop-25 deviation 255 — TOOL-dDeclaredLoop-25's spec revised before its build

**Serves:** deviation TOOL-dDeclaredLoop-25

- **Departs from:** `TOOL-dDeclaredLoop-25@rev-6`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dDeclaredLoop-25`'s spec as the revision at `TOOL-dDeclaredLoop-25@rev-6` reads it.
- **After:** the spec at rev-7: S6's stage plant reds the step gate, exit 1, because the playbook render reads a loop definition that does not read as no order (§8 F10 (a)); F7 says the gate as built refuses; usage.toml gains the stage class row; the playbook version bump moves to the close.
- **Cause:** builder discovery
- **Reason:** The rev-6 stage plant made the drive class's reader raise through check_loop, a refusal at exit 2 where AC5 needs a RED at exit 1; no member source can leave the definition without that raise.
- **Evidence:** `memory/builds/dDeclaredLoop/build/2026-11-15-build-TOOL-dDeclaredLoop-25-2-builder-return.md`, and the rev-7 line in this spec's §9.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer handoff of this revision, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); the fork picks are the run's under its mandate
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-15-build-TOOL-dDeclaredLoop-25-2-builder-return
