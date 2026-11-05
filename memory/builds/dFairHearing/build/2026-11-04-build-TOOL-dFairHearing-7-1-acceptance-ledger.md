# Acceptance ledger — TOOL-dFairHearing-7

**Serves:** journal TOOL-dFairHearing-7

Built against spec rev-1 at pass commit `a1956d229`. The main loop drafted this ledger at the close from the builder return and that commit's message. A scratch node runner cut from the suite's own JS block, over `tools/workflows/tier2-review.js`, passed 20 and failed 0. Each line reads this unit's own commit: TOOL-dFairHearing-1's pass `2d992a209` later moved absent `addressTwins` to `shown` on its replay's hit. No suite, gate or bar ran in the pass: the `New arm:` line on `tools/workflows/tier2-review.test.sh`, with its floor raised from 460 to 473, and the spec's legs are owed to the close, which records the arm's RED and GREEN here under a `Pass: none` commit.

**Evidences:** TOOL-dFairHearing-7
- AC1 — `deriveTwinPairs` — the runner read `[{confirmed: 1, refuted: 2}]` for the diff findings, and `section 2 S5` paired with the section-sign spelling of section 2 while `status header` paired with nothing
- AC2 — `addressTwins` — absent, `'hidden'` and `'shown'` each resolved, with absent defaulting to `'hidden'`, and `'on'` and `true` were refused naming it
- AC3 — `addressTwins: 'shown'` — the shown prompt carries `REFUTED findings` with id 2's claim and `by design` reason, and `SAME-ADDRESS PAIRS` with `confirmed id=1 and refuted id=2`, and its schema requires `twinFlags`. The default run carries neither block and no `twinFlags`
- AC4 — `twinFlags` — of the four flags, `{refuted: 2, confirmed: 1, sameAddress: true}` was kept, `twinPairs` read 1, and the `WARNING:` line named `1/2` and `9/1`. A refuted id 5 at `c.js` was kept at `sameAddress: false`
- AC5 — `confirmedFindings` — the hidden and shown runs agree on the eight fields the criterion names
- AC6 — `twinPairs` — a `duplicate of id=1` read `twinPairs` 0 and a `(none)` block
- AC7 — `tools/workflows/README.md` — by grep, `addressTwins` is in its argument paragraph and in the template's `args` header line, and `twinFlags` is in its return-field entry
