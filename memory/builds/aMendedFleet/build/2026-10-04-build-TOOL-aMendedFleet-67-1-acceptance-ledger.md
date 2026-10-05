# TOOL-aMendedFleet-67 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-67

**Evidences:** TOOL-aMendedFleet-67
- AC1 — `agentType` — a scratchpad stub runner evaluated `tools/workflows/tier2-review.js` as an async function body with recording `agent` stubs, a diff review and two canned findings under `workerType: 'Plan'`: five finders and two skeptic batches all carried `agentType` `Plan`, `resume:probe` and `synth` carried none, no judge prompt contained `DURABILITY`, and the log carried the `worker type Plan` line saying the results are NOT durable. Staged break: the same runner over the starting commit's harness failed all four
- AC2 — `tools/workflows/tier2-review.js` — the same stub run with no `workerType`, over the tip and over `git show HEAD:tools/workflows/tier2-review.js` at the pass's starting commit `726f90ac`: nine spawns each, and the JSON of every recorded prompt and option was identical, as was the review key. The `workerType` run's key differed from both
- AC3 — `workerType` — `'two words'`, `7` and a 65-character name each threw an error naming `workerType` with zero spawns recorded; a 64-character name ran to completion. Staged break: over the starting commit's harness all three reached a spawn
- AC4 — `Plan` — `tools/workflows/drift-audit-code.js` and `tools/workflows/drift-audit-state.js`, each run with `workerType: 'Plan'` and one canned finding: five finders with no `agentType`, the skeptic batch with `agentType` `Plan`, the synthesis with none, and `'two words'` refused before any spawn. Staged break: over the starting commit's renders the skeptic carried no type and the malformed value reached a spawn
- AC5 — `grep -n "workerType" tools/workflows/README.md` — hits the new section's heading and both `args` lines, one naming `tier2-review.js` and one the two drift harnesses; the section names `Plan` and `Explore`, the stamp `2026-10-04, node a, Claude Code 2.1.178`, the drift finders' exclusion and the restart caveat as UNVERIFIED. The binary fact was re-read this pass with the same read-only probe: `omitClaudeMd:!0` on the `haiku` and `inherit` built-ins and read on the spawn path
- AC6 — `node tools/workflows/check-workflow-syntax.js` — 6 scripts parsed clean, exit 0; `bash tools/workflows/check-verifier-fanout.sh` clean, exit 0; a `diff` of each template against its render differs only on the `FANOUT_CAP` lines, and on drift-audit-state the `TOOL_ROOT` line, it differed on at the starting commit

## The suite arm

S5's arms in `tools/workflows/tier2-review.test.sh` are written and not run as a suite: `bash -n`
passed and `node --check` over its extracted JavaScript passed. The arm records `agentType` per
spawn, checks the default run carries none, the `Plan` run routes all ten judges and neither
orchestrating agent, and three malformed values refuse before a spawn. The tier2-review self-test,
the review-join and verifier fan-out self-tests, the unattended-build self-test, install-prefix,
kit epoch and spec tokens are owed at the close; `bash tools/check-line-length.sh` and the
encoding-posture checker ran here, both exit 0.
