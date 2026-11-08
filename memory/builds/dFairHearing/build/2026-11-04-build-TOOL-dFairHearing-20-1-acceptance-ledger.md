# Acceptance ledger — TOOL-dFairHearing-20

**Serves:** journal TOOL-dFairHearing-20

Built against spec rev-3 and committed as the pass commit `93531c2e8`, whose parent is `46921281d`. The main loop drafted this ledger at the close from the builder return `2026-11-03-build-TOOL-dFairHearing-20-1-builder-return.md`, and every observation below is that return's. No suite, gate or bar ran in the pass: the checks were a scratch AsyncFunction probe and greps standing in for the `tier2-review self-test` leg, and the `New arm:` line's red-first observation and the spec's legs are owed to the close.

The close observed this unit's `New arm:` lines on 2026-11-08 at `4896589bc`: each row, RED or UNSEEN with its log line, is in `2026-11-08-build-TOOL-dFairHearing-1-arm-observations.md`, and every suite holding them exits 0 at that tip.

**Evidences:** TOOL-dFairHearing-20
- AC1 — `BLOCKED: the walk table has 1 gap(s)` — a scratch AsyncFunction probe of the render, using the suite's walker stub shape, saw the gapped walk return all four fields null and a note opening `BLOCKED: the walk table has 1 gap(s)`. Before the change the same walk returned blockers 0, highs 0, roundCount 0 and CONVERGED beside walkGaps of 1
- AC2 — `grep -c "const walkRed" tools/workflows/tier2-review.js` — the same probe saw the complete walk still return 0, 0, 0 and CONVERGED with no BLOCKED sentence, and grep found `const walkRed` once. The spec's rev-2 edge hands this criterion's absence half to unit 27
- AC3 — `state=-` — the same probe read the gapped walk's round line as `count=-` and `state=-`, where it read count=0 state=CONVERGED before the change
- AC4 — `grep -c "walkRed" tools/workflows/tier2-review.template.js` — by grep, walkRed appears 10 times in the template and 10 in the render, and the template-to-render diff has no walkRed line. The return records the README's return bullet as naming the four nulled fields, the BLOCKED note and where it ranks
