**Serves:** journal TOOL-aGradedDialect-1

# Acceptance ledger — TOOL-aGradedDialect-1

The unit's deliverable is a RECORD, so its acceptance is observed by reading that record and by
re-running the two derived criteria. Both were re-run at close on 2026-09-10, on node `a`, against
`C:/projects/incms/main`, read-only.

**Evidences:** TOOL-aGradedDialect-1

- AC1 — `2026-09-10-build-TOOL-aGradedDialect-1-typescript-extraction-research.md` §3 carries a
  four-row table naming C1 through C4 with a `loses if` column, and §4 reports the outcome against
  each. The losing conditions were composed before the measurements ran, which is the property the
  criterion is about and the one no later reader can re-derive from the file alone; it is asserted
  here rather than implied.
- AC2 — `ts-oracle.js` re-run at close over the adopter's tracked TypeScript: the file list holds
  1257 paths and the oracle emitted 1257 JSON lines, one per file with none skipped. Totals 5017
  function/method and 1369 type definitions, matching the record's §2 table exactly.
- AC3 — `regex_vs_oracle.py` re-run at close. The shipped `js-regex` types pattern recalls
  **0.6%** (8 of 1369), which is under the 1% the criterion names. The two readings disagree on
  **1123** function names against an oracle total of 5017, which is **22.4%** and over the 20% the
  criterion names. Both halves hold, so the pre-registered losing condition fired and C1 and C4
  remain refuted on re-measurement rather than on the first run alone.
- AC4 — the record's §4.4 states the casing distribution per EXTENSION in a four-row table and the
  `canon.py` verb-lead rate for both extensions, each measured 2026-09-10 and dated in the section's
  opening line.
- AC5 — amended rev-2. The criterion originally addressed §5 of the record alone while S5 scopes
  three clauses that land in §3, §4.1 and §4.3; §9's rev-2 line logs the move. As amended it holds:
  §3 names the four losing conditions, §4.1 and §4.3 report the three losses against them, and §5
  names the pick, the `.tsx` role-split problem and the `case:` selector refusal by the vacuity
  argument.

## What this unit did NOT observe, stated rather than left out

AC2 and AC3 both depend on an adopter tree this repository does not own. Their `fixture:` fields say
so, and the observation above is only as durable as that checkout. A later session on a node without
`C:/projects/incms/main` cannot reproduce these two lines and should read them as PINNED to this
date and this machine, not as something a gate re-derives.
