# TOOL-aOrientedCast-21 — acceptance ledger

**Serves:** journal TOOL-aOrientedCast-21

Direct checks only: no gate, suite, slice or self-test ran in this pass. What ran: a node probe in the
run's scratch path that builds the §6 fixture, a `git init` repository under `%TEMP%/fg21` with gov's
`AGENTS.md` CR-stripped, a `LIVE.md` naming `tBuild`, an orientation card routing it, and a transcript
T under `sess/` beside its session dir, then feeds `node tools/hooks/format-guard.js` hand-built Stop
payloads, one staged break at a time with T rebuilt before each, reading stdout and stderr: 25 cases,
each criterion's and the degraded inputs' (an unreadable transcript, an unreadable journal, an
unparsable turn line, a `queued_command` notification, a foreground `completed` Agent). Also: the
arm's three functions run read-only over this session's live 12 MB transcript (56 ms, 94 turn
records, the dispatched and received agents found); the suite's `write_transcript` node program cut
out and run once per scenario, its required lines printed; `bash -n` over the suite; the AC8 and AC9
greps from the worktree root; and `lexicon.py --suggest` for every new function and nested helper,
each OK. Owed to the main loop at the close (M8): every leg §7 lists, and §7's `New arm:`, the
`TOOL-aOrientedCast-21` block of `tools/hooks/format-guard.test.sh` with `FLOOR_ASSERTIONS` at 101,
RED with `checkAgentLines` staged to return no defect and with the turn scan staged to start at the
file's first line, GREEN once restored. Neither break was observed here.

**Evidences:** TOOL-aOrientedCast-21
- AC1 — `which this turn dispatched` — the pair-only message blocked with a reason naming `a1`, `which this turn dispatched` and `handoff.py agents`, quoting the `agent` and `returned` definitions; with the bare `- agent — … · run direct/a1` line added it allowed with empty stderr.
- AC2 — `rule r1` — the backticked line blocked naming `rule r1`; the line with its last field cut to `direct/a1` blocked with `does not match its charter shape`. With the run field removed wholly the line names no agent, and §4's first defect applies: it blocked with `no agent line for agent a1`.
- AC3 — `a3` — over a `Workflow` result `wf_t-1` whose journal starts `a2` and `a3`, both `agent` lines allowed, and the message without `a3`'s blocked naming `agent a3` and not `agent a2`.
- AC4 — `returned` — with the `Agent` call in an earlier turn and the turn opened by its notification, the pair-only message blocked with `no returned line for agent a1, which this turn received` and no `agent` defect, and a bare `returned` line alone allowed; the run's notification with a `result` for `a2` and a `failed` for `a3` blocked the two `agent` lines alone on both missing `returned` lines and allowed all four.
- AC5 — `transcript_path` — no `transcript_path` allowed with a witness naming it; runId `../x` allowed with a witness naming `"../x"`, while a journal planted at `subagents/x`, where `../x` would land, started `aOutside` and no stream named it; the empty transcript allowed with empty stderr.
- AC6 — `1 agent(s)` — with the `agent` definition deleted from the fixture charter, AC1's message allowed and stderr carried one line naming `no agent shape` and `1 agent(s)`; with an empty transcript it wrote nothing.
- AC7 — `stop_hook_active` — AC1's first payload with `stop_hook_active` true allowed.
- AC8 — `handoff.py agents` — the grep printed the new bullet of "What the hooks refuse", line 89, naming the `agent` and `returned` lines and `handoff.py agents`.
- AC9 — `KIT_AGENT_CAP_VERSION = '1.36'` — the count printed 1 and `git grep -l "gov:kit agent-cap@1.35" -- '*.js'` printed nothing.
