# TOOL-dCalibratedLens-32 deviation 322 — the spec's title reworded so it spells no other build's unit id

**Serves:** deviation TOOL-dCalibratedLens-32

- **Departs from:** `TOOL-dCalibratedLens-32@rev-2`
- **Hand-off:** spec-revised
- **Before:** the H1 title read `… which TOOL-dTotalRecall-42 S4 refuses`.
- **After:** the H1 title reads `… which dTotalRecall's unit 42 refuses at its S4`; no criterion, scope item, mark, rev, status line or §9 line changed, and the spec stays at rev-2.
- **Cause:** external
- **Reason:** the unattended kit gate's check 24 ADD arm reads every `[A-Z]+-[A-Za-z0-9]+-[0-9]+` token in the README's generated units table, titles included, so a title quoting another build's unit id read that unit as one added to this run's roster with no rescope row, and the close's bar went red on it. The title is reworded off the bare-id form, and the gate's reading is filed as its own ask.
- **Evidence:** the re-title (`git diff -- memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-32.md` in this record's commit); the close's bar, `UNATTENDED check 24 FAILED … TOOL-dTotalRecall-42 in memory/builds/dCalibratedLens/RUN.md`; `tools/unattended/check-unattended.sh`, check 24's ADD arm.
- **Risk:** editorial
- **Approver:** author, the main loop of dCalibratedLens's spec run, which made this title-only edit, recorded under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** usage spec-audit-fold
- **Caused-by:** PLAY-dClosedLoop-2
