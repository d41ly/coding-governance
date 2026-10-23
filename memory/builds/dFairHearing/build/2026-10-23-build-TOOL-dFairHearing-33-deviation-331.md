# TOOL-dFairHearing-33 deviation 331 — the round-4 spec audit promoted a unit for the constant half of its high H1

**Serves:** deviation TOOL-dFairHearing-33

- **Departs from:** dFairHearing [roster]
- **Hand-off:** design-to-spec
- **Before:** dFairHearing's roster carries the specced units `TOOL-dFairHearing-1` to `TOOL-dFairHearing-18`, `TOOL-dFairHearing-20` to `TOOL-dFairHearing-23` and `TOOL-dFairHearing-25` to `TOOL-dFairHearing-32`, the round-3 spec audit's promotions `TOOL-dFairHearing-28` to `TOOL-dFairHearing-32` the last specced.
- **After:** the roster also carries `TOOL-dFairHearing-33`, ordered at 23 after `TOOL-dFairHearing-31` at 22: every kit version constant the registry declares, read at the build's base and at `HEAD` through govkit's own `resolve_version_value_at`, each by its entry's own pattern, exiting 1 on a moved value and 2 on an empty population.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a HIGH to a unit whose mechanism closes it. This unit closes the constant half of one confirmed high of the round-4 spec audit, item H1 (finding id 22, merged with id 31, whose marker half is `TOOL-dFairHearing-34`'s). Unit 31's probe matches version lines with one typed pattern, `KIT_[A-Z_]+_VERSION = `, so the shell form at `tools/check-wiring.sh:51`, `KIT_CHECK_WIRING_VERSION=1.34`, and the marker kind `governance-template: v4.4` are never matched, and a hand bump there exits 0. This is a spec run, so the unit is specced, audited and carried forward once, and the build run after it builds it (`UNATTENDED-STOPS.md` §15, the carry-forward term's second condition).
- **Evidence:** the round-4 spec audit, `memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-28-32-spec-audit.md`; the rescope add row for `TOOL-dFairHearing-33` in `memory/builds/dFairHearing/RUN.md`; the unit's spec, `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-33.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dFairHearing-33
- **Caused-by:** PLAY-dClosedLoop-2
