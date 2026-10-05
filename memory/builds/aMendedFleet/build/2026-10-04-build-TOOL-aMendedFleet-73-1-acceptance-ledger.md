# TOOL-aMendedFleet-73 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-73

**Evidences:** TOOL-aMendedFleet-73
- AC1 — `grep -c "^| D[0-9]"` — over the brief journal printed 18, at least the 14 §4 lists; the journal's vague brief is the unit pass's byte copy of §4
- AC2 — `stub` — the trial's verifier ran `freeze` then `stub`: `stub: 25 tests, 0 passed the exit-0 stub`, and the committed `-73-freeze.tsv` carries the hidden-suite and decision-list sha256 rows that `hidden` asserted before grading the pilot
- AC3 — `intent` — `hidden` printed the pilot at `intent 10/10 = 1.000`, above 0.8, and the workflow returned `stopped: headroom` before stage 3 spawned an agent
- AC4 — `node tools/workflows/check-workflow-syntax.js` — 7 scripts parsed clean; `check-verifier-fanout.sh` clean over 7; and `tools/hooks/agent-cap.js` allowed the real Workflow call that ran the script on 2026-10-06
- AC5 — amended rev-3 — stages 4 and 5 never ran after the headroom stop, which the trial report states; the §9 line for rev-3 logs it
- AC6 — amended rev-3 — `aggregate` over the committed rows exits `DEAD PROBE: no score row`, and the rows file carries the pilot's four grading rows the report quotes; the §9 line for rev-3 logs it
- AC7 — amended rev-3 — the `tokens` verb now searches for the tag the harness preamble displaced, and reports `verifier`, `pilot` and `runner-pilot` sums; 138 other workflow agents in this shared session read untagged, as the amended criterion states
- AC8 — `git log --format=%s` — the instruments landed in the unit pass commit `1eee9ef4c` with the spec INPROGRESS, and the spec reads CLOSED only in the later commit that adds the result rows
- AC9 — `bash tools/memory-tree/check-memory-hygiene.sh` — exit 0 at the unit pass tip, naming none of the unit's files; re-run before the closing commit
