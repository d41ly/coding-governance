# TOOL-dTotalRecall-1 deviation 15 — the `record-kinds` leg's ceiling is 122 seconds, not the spec's 120

**Serves:** deviation TOOL-dTotalRecall-1

- **Departs from:** `TOOL-dTotalRecall-1@rev-7` [§2 S3]
- **Hand-off:** spec-to-code
- **Before:** S3 declares the `record-kinds` leg with a ceiling of 120 seconds.
- **After:** the `[[exempt_leg]]` row in `tools/govkit/registry.toml` declares `ceiling = 122`, rendered into `tools/gate-legs.json`.
- **Cause:** builder discovery
- **Reason:** the `leg ceilings clear their evidenced maximum` pass leg requires a ceiling to clear its evidenced maximum by max(120 s, 1.0x) (DERIVED, that leg's failure line at `a9b4e3739`'s parent), and the leg's evidence is 1.6 s (`tools/run-gates/ceiling-evidence.txt`, the `record-kinds` row), so 120 fell short and 122 clears it.
- **Evidence:** red-fix commit `a9b4e3739` and its record `memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-1-red-fix-5.md`.
- **Risk:** editorial
- **Approver:** author, the main loop's inline red fix under the build's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** TOOL-dTotalRecall-1
