**Serves:** journal TOOL-dMergedTally-1

# dMergedTally — acceptance ledger for TOOL-dMergedTally-1

*Node `d`, 2026-09-16. Every observation below ran the fixture spec section 6 names, built into the
session scratchpad from the suite at the rev-2 tree, with `HERE` pointed at copies of the landed
scripts for GREEN and at `4cf0944d`'s for RED. The harness suite was also run whole once after the
fold: 415 arms, exit 0.*

**Evidences:** TOOL-dMergedTally-1
- AC1 — `run_merged_review` over the measured shape returned `"blockers":3,"highs":6`, and `run_merged_build` logged `disposal: done — promoted 9 · folded 4`; against the base callee the same arms returned blockers 1 and highs 5 and the note `do not split by severity`.
- AC2 — dropping id 33 returned `"blockers":null,"highs":null` with `confirmed id(s) 33 sit in no item`; id 4 in two items named `sit in more than one item`, and the harness printed `non-integer blocker count` with no `phase:Disposal` line.
- AC3 — id 48 unjudged and listed at BLOCKER left `"unverified":1,` beside 3 and 6; `CRITICAL` left id 33 unplaced; `high` kept 3 and 6.
- AC4 — no verdicts and an empty item list returned `"blockers":0,"highs":0` beside 48 unverified, and the harness logged `disposal: done — promoted 0 · folded 48`.
- AC5 — the `prompt:synth:` line carried `Return JSON {path, items, summary}`, and a double with no `items` under `RUN_WF_SCHEMA=strict` returned `the synthesis agent died` with both counts null.
- AC6 — `diff tools/workflows/unattended-build.js tools/workflows/unattended-build.template.js` printed 12 lines, the six token pairs, and `grep -c 'Every count above is of RAW'` printed 1 for each file.
- AC7 — against `4cf0944d`'s callee and render, 18 of the 22 arms failed and the 4 that passed are the liveness controls; each of the eight mutations the criterion names failed between 1 and 11 arms, and none survived.
