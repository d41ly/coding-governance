# TOOL-dTrueNorth-20 deviation 20 — two spec-token waiver rows hold another build's guards-join hits

**Serves:** deviation TOOL-dTrueNorth-20

- **Departs from:** dTrueNorth [§8 F3 of TOOL-dTrueNorth-20]
- **Hand-off:** spec-revised
- **Before:** `memory/project/spec-token-waivers.txt` holds 23 rows and declares itself SHRINK-ONLY; TOOL-dTrueNorth-20's F3 leaves open how the three guards-join hits TOOL-dTrueNorth-11's guard makes on dPinnedHandoff's live specs clear.
- **After:** two token rows, `build-index selftest <- tools/check-spec-tokens.py` and `memory-hygiene self-test <- tools/check-spec-tokens.py`, hold the three hits; the count is 25; ask `TOOL-dTrueNorth-21` in dTrueNorth's `BACKLOG.md`, DEFERRED until `TOOL-dPinnedHandoff-2`, asks dPinnedHandoff to name both legs and delete the rows.
- **Cause:** builder discovery
- **Reason:** TOOL-dTrueNorth-15's `--dispatch` was refused (check 49) on the hits, and every later dispatch would have been. Editing dPinnedHandoff's specs is outside README rule 7 (veto 1), and raising `SPEC_GUARD_LEGS_CUTOFF` is a root-conf change outside the grant that grandfathers a whole date; the waiver raise trips only a declared ceiling, the owner's, so rung 5's standing ruling takes it as the narrowest option.
- **Evidence:** commit `0c0d1bb0e`; TOOL-dTrueNorth-20 §8 F3; TOOL-dTrueNorth-15's first builder return (run `wf_8e5276fb-cd0`).
- **Risk:** loosening
- **Approver:** author, the run's main loop, under the chain's `author-recorded` value, citing ER:388 (`PLAY-dClosedLoop-6`)
- **Follow-through:** ask TOOL-dTrueNorth-21
- **Caused-by:** PLAY-dClosedLoop-6
- **Surface:** memory/project/spec-token-waivers.txt
