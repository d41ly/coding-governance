# TOOL-aMendedFleet-93 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-93

**Evidences:** TOOL-aMendedFleet-93
- AC1 — `--selftest` — the instrument's selftest, run with `--scratch` under the session scratchpad, printed 16/16 passed and exited 0: each judge's first-turn sum, both medians, `Plan` on every arm-B judge, and the unlabelled agent counted unclassified. Staged break: a copy whose `derive_role` returned `finder` for an unlabelled agent printed 13/16 and exited 1
- AC2 — `arms` — over the two committed return objects it printed `exit='complete' lensesReused=0 batchesReused=0 lensesDead=0 skepticsDead=0 — OK` for arm A and for arm B, exit 0
- AC3 — `tokens` — re-run by this pass over the main session `f1d79f53` and its two workflow directories, `wf_6fa64b60-4e5` for arm A and `wf_2eba1b24-a2d` for arm B: finder=5 skeptic=5 orchestration=2 unclassified=0 in each arm, exit 0, and the rewritten judges TSV was byte-identical to the committed one. `aggregate` reads from those rows that every arm-B judge's `agentType` is `Plan` and no arm-A judge's is
- AC4 — `aggregate` — run from a fresh `git clone --local` of `77b6e727` under `%TEMP%/t93c`, whose three input files this pass did not move: the table lines compared byte-identical to the reading's by `cmp`, and the output carried exactly one verdict word, `DEFAULT-PLAN`, the word the reading states. Re-run from a clone of the closing commit after it landed, reported in the pass's return
- AC5 — `git log --format=%s` — `00f3a363b` adds the run brief and the instrument, `77b6e7273` adds the return objects, reports and judge rows, and the closing commit adds the reading; the spec at `00f3a363b` and at `77b6e7273` reads INPROGRESS and reads CLOSED first in the closing commit
- AC6 — `tools/workflows/tier2-review.js` — a scratchpad stub runner evaluated the render with recording `agent` stubs over a diff review with one finding per lens: with no `workerType` all ten finder and skeptic spawns carried `agentType` `Plan`; with `workerType: 'none'` its twelve recorded prompts, options and review key were identical to unit 67's tip render, `b5a8ed08f`, run with none. Staged breaks: unit 67's render with no `workerType` spawned no judge as `Plan`, and a copy whose `none` was taken as a type name failed the identity check
- AC7 — `grep -n "workerType" memory/guides/REVIEW-PROTOCOL.md` — hits line 203, inside the "Results are durable only on request" paragraph; a CR-insensitive `diff` of `tools/workflows/REVIEW-PROTOCOL.template.md` against `memory/guides/REVIEW-PROTOCOL.md`, hunk headers aside, compared byte-identical to the same diff taken before the edit
- AC8 — amended rev-4 — the first grep is scoped to `build/`, because over the whole build folder it matched this spec's own AC8 sentence; scoped, it printed nothing, and `git grep -c "journal TOOL-aMendedFleet-93" -- memory/builds/aMendedFleet/` counted one in each arm report among five files

## Owed at the close

The new arm in `tools/workflows/tier2-review.test.sh` is written and not run as a suite: `bash -n`
passed and its extracted JavaScript parsed under `vm.Script`. It pins `workerType: 'none'` on the
shared diff and spec arguments, so every durable-spawn arm keeps testing the pre-default spawns, and
adds an absent run whose ten judges must spawn as `Plan` and whose key must equal an explicit `Plan`
run's. The tier2-review self-test, the review-protocol parity leg, the unattended-build self-test,
memory hygiene, spec tokens, install-prefix, line length and kit epoch are the close's.
`node tools/workflows/check-workflow-syntax.js` and the encoding-posture checker ran here, exit 0.
