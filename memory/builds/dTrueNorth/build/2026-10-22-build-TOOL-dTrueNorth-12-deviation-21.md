# TOOL-dTrueNorth-12 deviation 21 — a spec-token waiver row holds another build's guards-join hit

**Serves:** deviation TOOL-dTrueNorth-12

- **Departs from:** dTrueNorth [spec-token waivers]
- **Hand-off:** spec-to-code
- **Before:** `memory/project/spec-token-waivers.txt` holds 25 rows and declares itself SHRINK-ONLY.
- **After:** one token row, `routed-commits selftest <- tools/unattended/`, holds the guards-join hit TOOL-dTrueNorth-12's guard widening makes on `TOOL-aOrientedCast-28`'s live spec; the count is 26; ask `TOOL-dTrueNorth-22` in dTrueNorth's `BACKLOG.md`, DEFERRED until `TOOL-aOrientedCast-28`, asks that build to name the leg and delete the row.
- **Cause:** builder discovery
- **Reason:** TOOL-dTrueNorth-12 widened the routed-commits selftest guard to `lib-unattended.sh`, which reaches every live spec listing `tools/unattended/`, and the spec-tokens join then refuses every later `--dispatch`. Editing aOrientedCast's spec is outside README rule 7 (veto 1); the waiver raise trips only a declared ceiling, the owner's, so the standing ruling takes it, as it took TOOL-dTrueNorth-20 F3's two rows. dTrueNorth's own TOOL-dTrueNorth-7, hit the same way, names the leg in its §7 instead.
- **Evidence:** `python tools/check-spec-tokens.py` after commit `bf8326aff`: two guards hits, on `TOOL-aOrientedCast-28` and `TOOL-dTrueNorth-7`; deviation-20, the record for the same choice before it.
- **Risk:** loosening
- **Approver:** author, the run's main loop, under the chain's `author-recorded` value, citing ER:388 (`PLAY-dClosedLoop-6`)
- **Follow-through:** ask TOOL-dTrueNorth-22
- **Caused-by:** PLAY-dClosedLoop-6
- **Surface:** memory/project/spec-token-waivers.txt
