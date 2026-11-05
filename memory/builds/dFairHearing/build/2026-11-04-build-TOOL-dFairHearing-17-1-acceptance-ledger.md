# Acceptance ledger — TOOL-dFairHearing-17

**Serves:** journal TOOL-dFairHearing-17

Built against spec rev-5 and committed as the pass commit `3745b407a`, whose parent is `b52de5586`. The main loop drafted this ledger at the close from the builder return `2026-11-03-build-TOOL-dFairHearing-17-1-builder-return.md`, and every observation below is that return's. No suite, gate or bar ran in the pass: the checks were scratch probes standing in for the `tier2-review self-test` leg, and the `New arm:` line's red-first observation and the spec's legs are owed to the close.

**Evidences:** TOOL-dFairHearing-17
- AC1 — `NON-CONVERGENT` — a node probe ran the 13 calls these three criteria specify against the render, and all matched, the flat and oscillating sequences among them
- AC2 — `BOUNDED` — the same probe's calls matched, the sequence reaching its limit and the one past it among them
- AC3 — `CONVERGED` — the same probe's calls matched, a count of 0 after each prior sequence among them
- AC4 — `roundLimit` — the opening-section cut the suite uses ran the six refusals, the disagreeing round, the round that should proceed and the inferred round 3, and each behaved as specified
- AC5 — `review-round round=3 limit=3 prior=4,2 count=1 state=BOUNDED` — a stub run of the whole render passed 19 of 19 checks. They covered `BOUNDED` with count 1 and the ROUND block, a dead lens, round 2 with no `priorCounts`, no findings, every finding refuted, a dead synthesis and every lens dead
- AC6 — amended rev-3 — the revision log's rev-3 line adds the hands-off edge to unit 23, which replaces the five-token assertion with the four in-domain tokens and holds CEILING directly. CEILING cannot occur in this domain on either side, because the round never passes the limit. Under the amended clause, the suite's shell block cut out and run alone wrote 448 rows, all agreeing with deriveRoundState, and a scratch copy with the comparison weakened disagreed on 81 rows. The AC2 row covers CEILING directly
- AC7 — `roundLimit` — checked with grep: the args header and the kit README name `roundLimit`, `priorCounts`, the two return fields and the `review-round` line
- AC8 — `tools/gate-legs.json` — checked with `python -c`: the leg's guard in `tools/gate-legs.json` now includes `{prefix}/unattended/unattended.sh`
- AC9 — `grep -c roundState` — both unattended-build files have 0 hits for the old phrase and at least 1 for `roundState`, and each template's changed lines equal its render's
