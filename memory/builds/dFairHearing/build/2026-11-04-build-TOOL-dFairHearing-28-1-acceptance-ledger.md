# Acceptance ledger — TOOL-dFairHearing-28

**Serves:** journal TOOL-dFairHearing-28

Built against spec rev-3 in pass commit `386f830ff`, whose parent is `03ed40f98`. The main loop drafted this ledger at the close from the builder return. `census.py` is the spec's script byte for byte, written under the pass's scratch directory, and the two AC3 copies were made with `sed` and checked against it with `diff`. Units 16, 23 and 26 had finished the move, so no suite changed. No suite, gate or bar ran in the pass, and the spec's gate legs are owed to the close. Neither `New arm:` line has an arm to observe RED-first, because this unit moved none.

The close observed this unit's `New arm:` lines on 2026-11-08 at `4896589bc`: each row, RED or UNSEEN with its log line, is in `2026-11-08-build-TOOL-dFairHearing-1-arm-observations.md`, and every suite holding them exits 0 at that tip.

**Evidences:** TOOL-dFairHearing-28
- AC1 — `python census.py 3708a705` — it printed `rule0: 25`, `rule0/U7: 13`, `rule0/aWardedAudit: 10`, `rule0/aWardedAudit-6: 9`, `rule5: 14`, `labels 71` and `population 59 14`, and exited 0. This line is `precondition` evidence: it reads only `3708a705`, so it is green before any build
- AC2 — `python census.py 3708a705` — with `tools/hooks/agent-cap.test.sh`, `tools/workflows/spec-audit-optin.test.sh` and `tools/workflows/check-review-join.test.sh` as the three paths, it printed no failing line and exited 0
- AC3 — `the pattern lost a backslash` — the first copy exited 1 at the self-check before any `git show`. The second copy, with the self-check also removed, printed `labels 66` and `population 54 14`, then exited 1 printing `census: the population is not 59 and 14`. This line is `precondition` evidence, as AC1's is

## Supersessions

Each one is named by the hands-off bullet to `TOOL-dFairHearing-36` in this unit's spec.

- `TOOL-dFairHearing-28` AC3 — the second half is restated by `TOOL-dFairHearing-36` S2 as a copy expecting a population of 60 and 14
- `TOOL-dFairHearing-28` AC1 and AC3 — recorded as `precondition` evidence by `TOOL-dFairHearing-36` S7. Acceptance of the move rests on this unit's AC2 and that unit's AC1 and AC4
