# TOOL-dScopedBuild-10 deviation 101 — the reproduction is owed by any unit that closes a reported bug, read off the ask, since no parent marks a patch build's origin

**Serves:** deviation TOOL-dScopedBuild-10

- **Departs from:** `cl-dClosedLoop-0408@e14d93bc`
- **Hand-off:** design-to-spec
- **Before:** a red-first reproduction, a `reproduction` probe, before a patch build's fix when the build comes from a bug report (night pass, point 2)
- **After:** a red-first reproduction, a confirmed `reproduction` probe record serving the unit, before the first dispatch of any unit whose spec header closes or advances an ask carrying a `seen` clause, the ask being the bug report and the unit its fix, whether or not the build is a patch (night pass, point 2)
- **Cause:** external
- **Reason:** no parent marks a build as a patch from a bug report: TOOL-dPlacedRequest-21 S4 types a patch only by `parents: <origin slug>`, absent at base, and a patch is not always a bug; the one bug-report shape the tree holds is an ask whose row carries a `seen` locator, which `memory/guides/UNATTENDED-ASKS.md` reads as the place the defect was observed. Reading the report off the ask and gating the unit that closes it carries the clause's intent, a fix never landing before its bug was made red, and is stricter than its text on a non-patch build that closes a reported bug (TOOL-dScopedBuild-10 §8 F4).
- **Evidence:** scout D's row 10 (`memory/builds/dScopedBuild/build/2026-11-01-build-TOOL-dScopedBuild-10-reuse-scout-d.md:13`, "The predicate 'comes from a bug report': no seam fits"); TOOL-dPlacedRequest-21 S4 (`memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-21.md`); the asks guide's `seen` reading (`memory/guides/UNATTENDED-ASKS.md:71-78`); the probe run in TOOL-dScopedBuild-10 §8 F1.
- **Risk:** stricter
- **Approver:** spec writer, the gov-spec-writer role of the harness's spec stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** amends cl-dClosedLoop-0408@e14d93bc
- **Caused-by:** TOOL-dScopedBuild-10
