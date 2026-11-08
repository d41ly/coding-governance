# Acceptance ledger — TOOL-dFairHearing-4

**Serves:** journal TOOL-dFairHearing-4

Built against spec rev-4 at pass commit `be4358a01`. The main loop drafted this ledger at the close from the builder return and that commit's message. A scratch node probe, cutting the prelude as the suite does and running the whole script over stub agents, passed 30 of 30 checks over AC1 to AC6, and on the base harness it was red with `deriveAddressKey is not defined`. No suite, gate or bar ran in the pass: the `New arm:` line on `tools/workflows/tier2-review.test.sh`, with its floor raised from 418 to 439, and the spec's legs are owed to the close, which records the arm's RED and GREEN here under a `Pass: none` commit.

The close observed this unit's `New arm:` lines on 2026-11-08 at `4896589bc`: each row, RED or UNSEEN with its log line, is in `2026-11-08-build-TOOL-dFairHearing-1-arm-observations.md`, and every suite holding them exits 0 at that tip.

**Evidences:** TOOL-dFairHearing-4
- AC1 — `deriveAddressKey` — the probe keyed the criterion's diff finding and its five spec `where` values as stated
- AC2 — `checkSameAddress` — it read lines 10 and 13 as one address, 10 and 14 and two files as two, `null` as matching nothing, a section-two address equal to itself and unequal to a section-three address
- AC3 — `deriveAddressOrder` — it ordered the six findings 4, 6, 1, 3, 5, 2 and left the argument reading 1 to 6, and a spec finding whose `at` is `null` sorted last in its file
- AC4 — `batchBy` — absent, `'id'` and `'address'` resolved, and `'section'`, `1` and `null` were refused naming it
- AC5 — `batchBy: 'address'` — a stub-agent run put the five `a.js` findings in batches 2, 2, 1, 0 and 0, and by id at most one per batch. Both runs spawned five skeptics, `verify:batch-1` to `verify:batch-5`, each prompt naming `verify-batch-<n>.json` and its own `ids`
- AC6 — `verify-batch-1.json` — a file with key, print and `ids` was reused, with `batchesReused` 1. `verify-1-2.json` and a file lacking `ids` were dispatched. The hands-off edge to TOOL-dFairHearing-32 at rev-4 adds a prompt half to this criterion, which that unit observes
- AC7 — `node tools/hooks/agent-cap.js --only=scripts` — the fan-out payload exited 0 on the render and 2 on a scratch copy reading `chunk(verifyOrder, 1)`
- AC8 — `git grep -n -e 'verify:ids' -e 'verify-<first id>'` — over `tools/` and `memory/guides/` it printed nothing, and the new spellings are found where the criterion says: the README, both protocol copies and the `args` header. The hands-off edge to TOOL-dFairHearing-32 at rev-4 supersedes the two absence patterns, so this line grades the patterns as this unit's commit read them
