# TOOL-dBoundRoles-54 deviation 543 — unit 49's AC2 and its "Why two checks" claim are superseded by unit 54's roster-side overlay compare

**Serves:** deviation TOOL-dBoundRoles-54

- **Departs from:** `TOOL-dBoundRoles-49@rev-5` [AC2]
- **Hand-off:** spec-revised
- **Before:** unit 49's AC2, "When the same probe drops one overlay's seed row from the scratch roles descriptor while the file stays under `house/`, S3's check reports that overlay by name", and its §4 "Why two checks" claim, "S3 is what ties the figure to the roster: a roles overlay that the roster seeds and the plan drops reds by name".
- **After:** both are superseded by `TOOL-dBoundRoles-54`'s AC2, unit 49's AC2 restated for S1's roster set, and by its S1 set, `house/<slot>.md` for every slot of the roles kit's roster, which `tools/govkit/selftest.py#derive_overlay_expected` derives and `tools/govkit/selftest.py#derive_overlay_drift` compares both ways with the roles seed rows.
- **Cause:** review finding
- **Reason:** unit 49's spec is CLOSED at rev-5 and `doc.build-method#m4-the-spec-audit-owed-only-where-the-build-or-its-project-declares-it` freezes a CLOSED spec, correcting it only by a unit on top, so the frozen spec cannot carry the restatement; its S3 read its expected side from the same seed rule the plan rows come from, so its AC2 removed the overlay from both sides and the check compared the descriptor with itself.
- **Evidence:** finding id 14 at HIGH, item H2, of `memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-45-spec-audit-round1.md`; `TOOL-dBoundRoles-54` §1 and §8 F3; unit 49's spec at blob `f28a8bb8`, its AC2 and its §4 "Why two checks".
- **Risk:** stricter
- **Approver:** spec writer, the gov-spec-writer role that resolved `TOOL-dBoundRoles-54` §8 F3, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dBoundRoles-54
- **Caused-by:** TOOL-dBoundRoles-54
