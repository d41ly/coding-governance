# Acceptance ledger — TOOL-dFairHearing-5

**Serves:** journal TOOL-dFairHearing-5

Built against spec rev-2 at pass commit `d1db0fc80`. The main loop drafted this ledger at the close from the builder return and that commit's message. A scratch node runner over `tools/workflows/tier2-review.js`, cutting the prelude as the suite does, passed 15 of 15, and the same runner over the parent render passed 2 and failed 13. No suite, gate or bar ran in the pass: the `New arm:` line on `tools/workflows/tier2-review.test.sh`, with its floor raised from 439 to 451, and the spec's legs are owed to the close, which records the arm's RED and GREEN here under a `Pass: none` commit.

The close observed this unit's `New arm:` lines on 2026-11-08 at `4896589bc`: each row, RED or UNSEEN with its log line, is in `2026-11-08-build-TOOL-dFairHearing-1-arm-observations.md`, and every suite holding them exits 0 at that tip.

**Evidences:** TOOL-dFairHearing-5
- AC1 — `extractDuplicateTarget` — the runner read `duplicate of id=4` as 4, `  Duplicate of id=12: same claim` as 12, and `duplicate of prior a.js:3`, `dup of id=4`, an empty string and `undefined` as `null`
- AC2 — `refuted=0 merged=1` — stub-agent runs with id 2 refuted `duplicate of id=1` read `confirmed` 9, `merged` 1, `refuted` 0 and `precision` 1, and the owning lens's yield row read `merged` 1 and `precision` 1, on a diff review and a spec audit
- AC3 — `duplicate of id=1` — the ledger and appendix rows of id 2 keep `refuted` and that reason, and `duplicate of prior a.js:3` returned `merged` 0 and `refuted` 1
- AC4 — `duplicate of an unconfirmed id` — on the diff kind, `duplicate of id=3` and a refuted id 1 each left row 2 `unverified` with that reason, a `WARNING:` line naming `ids 2`, and RUN INTEGRITY's orphan clause
- AC5 — `duplicate of id=<n>` — every diff verify prompt carries it
- AC6 — `confirmedFindings` — it and the CONFIRMED list lack id 2, `blockers` read 0 and `highs` 9, and the tally raised no fault
- AC7 — `grep -n "^const REVIEW_SHAPE" tools/workflows/tier2-review.template.js` — at the commit it read `lenses5-r4`, not `lenses5-r3`
- AC8 — `tools/workflows/README.md` — by grep at the commit, `merged=<n|->` and `confirmed + merged` are found in it and in `tools/workflows/REVIEW-PROTOCOL.template.md` and `memory/guides/REVIEW-PROTOCOL.md`
