# TOOL-aOrientedCast-24 — acceptance ledger

**Serves:** journal TOOL-aOrientedCast-24

Direct checks only: no suite, slice or self-test ran in this pass. What ran: a node probe in the
run's scratch path that extracts the `write_transcript` builder from `tools/hooks/format-guard.test.sh`
by text, seeds the §6 fixture (a `git init` repository under `%TEMP%/fg24` with a copy of `AGENTS.md`,
a `LIVE.md` naming `tBuild` and an orientation card routing it) and feeds `node tools/hooks/format-guard.js`
each new scenario's Stop payload, reading stdout and stderr: 21 of 21 expectations held, the four
`TOOL-aOrientedCast-21` scenarios included. The same probe over a copy of the hook at `e088b0969`
failed 9 of them, the AC1 and AC2 ones, so those arms discriminate. A second node probe builds the
§6 gate-guard kit copy (the hook, `stop-guard.js` and `run-lease.js` beside a stub `unattended.sh`
printing a file the probe writes and exiting a code it sets) under `%TEMP%/gg24` and feeds it the
`AskUserQuestion` payload for `tSess-1`: 14 of 14 held, a `stop-guard.js` that throws on load
included; over the hook at `e088b0969` it failed 8. Also `bash -n` over both suites, the AC8, AC10
and AC11 commands from the worktree root, `lexicon.py --suggest` for `checkSettles` and
`checkToolResult`, `gen_map.py --write`, which moved `symbols.json` by those two names, and
`adopt-unattended.sh`, which re-rendered the four guides, the playbook template, the two fixture
records, the playbook fixture and the `/unattended` Skill at 1.106. Not run, and owed to the main
loop at the close (M8): every leg §7 lists; `adopt-unattended.sh --check`, which the role gate
refused as the `unattended skill wiring` leg; and §7's two `New arm:` lines, RED on each staged
break and GREEN once restored: the `TOOL-aOrientedCast-24` block of `format-guard.test.sh` with
`FLOOR_ASSERTIONS` at 129, and the Q7 to Q12 arms of `gate-guard.test.sh` with `FLOOR_ASSERTIONS`
at 179. Neither suite's executed count was observed here.

**Evidences:** TOOL-aOrientedCast-24
- AC1 — `<tool-use-id>t9</tool-use-id>` — with a1 and a9 dispatched in the earlier turn and the last turn opened by t1's notification whose `<result>` quotes `<tool-use-id>t9</tool-use-id>`, `node tools/hooks/format-guard.js` allowed the R1 message and blocked pair-only naming `no returned line for agent a1` and not `agent a9`; the headless notification quoting t9 allowed pair-only. At `e088b0969` all three went the other way.
- AC2 — `which this turn dispatched` — the Skill result with a `sourceToolUseID` meta record, the Read result with an `isMeta` image note, and the `compact_boundary` record with an `isCompactSummary` record each blocked pair-only naming `agent a1` and `which this turn dispatched`; at `e088b0969` each allowed.
- AC3 — `isMeta` — a1 dispatched in an earlier turn ending with assistant text and the last turn opened by an `isMeta` idle-wake record: pair-only allowed with 0 bytes of stderr.
- AC4 — `queued_command` — the notification delivered in a `queued_command` attachment, and a foreground `Agent` result with status `completed`, each blocked A1 alone naming `no returned line for agent a1` and allowed A1 with R1; the `Workflow` result with `runId` `wf_t-1` and status `completed` blocked A2 with A3 naming `no returned line for agent a3` and allowed all four lines.
- AC5 — `1 line(s)` — the agent scenario with one unparsable line in the turn blocked pair-only naming `agent a1`, and stderr carried `1 line(s)`.
- AC6 — `unattended.sh --landed fx` — on the stub kit copy a LANDING record at `verdict: TERMINAL` exited 0 with empty stderr; at `FINISHED-UNSTAMPED` it exited 2 naming `unattended.sh --landed fx` and not `--park`; a HELD record exited 0 at TERMINAL and 2 at HELD; a BUILDING record at LIVE exited 2 naming `liveness LIVE` and `unattended.sh --park fx`.
- AC7 — `verdict:` — a BUILDING record with the stub exiting 1, printing no `verdict:` line, and moved aside each exited 2 with stderr saying the liveness could not be read, and so did a `stop-guard.js` that throws on load; a LANDED record with the stub absent exited 0.
- AC8 — `at LANDING` — `node tools/unattended/gate-guard.js` fed the `AskUserQuestion` payload for the lease of `memory/builds/aBatchedMinors/RUN.md` with `cwd` this checkout exited 0 with 0 bytes of stderr in 7 s, and `unattended.sh --liveness aBatchedMinors` printed `verdict: TERMINAL`; the hook at `e088b0969`, copied beside `run-lease.js`, exited 2 naming `at LANDING`.
- AC9 — `42` — a BUILDING record with its `phase:` line deleted exited 0 with empty stderr, and a payload whose `cwd` is the number `42` exited 0.
- AC10 — `grep -n "restarts" tools/unattended/README.md` — it printed nothing; `next tool call` printed line 116 of the question-arm paragraph; `still grades` printed one line in `tools/hooks/format-guard.js` and one in `tools/hooks/README.md`; `reads TERMINAL` printed one line in `memory/map/features/unattended.md` and one in `tools/unattended/README.md`; `TOOL-aOrientedCast-22` printed line 22 of the settings gotcha.
- AC11 — `grep -c "KIT_AGENT_CAP_VERSION = '1.37'" tools/hooks/agent-cap.js` — the count printed 1, `git grep -l "gov:kit agent-cap@1.36" -- '*.js'` printed nothing, `^KIT_UNATTENDED_VERSION=1.106` counted 1, and `git grep -l "gov:kit unattended@1.105" -- tools memory/guides .claude/skills` printed nothing after the re-render.
