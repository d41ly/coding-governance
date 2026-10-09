**Serves:** research TOOL-aRoutedQuill-2 TOOL-aRoutedQuill-4

# The subagent payload probe — TOOL-aRoutedQuill-2 F1 and TOOL-aRoutedQuill-4 F1

Run 2026-10-09 on node `a`, Claude Code 2.1.292 (`claude` on PATH), by the unattended run's main
loop before step 3. The harness is the one both forks name.

- **Clone.** `git clone --local` of the primary tree to `%TEMP%/rqp1`, a short root because the
  scratchpad hits MAX_PATH. Gov's own `.claude/settings.json` was kept. Two hooks were appended,
  each running one node logger that writes one JSON line per call: a PreToolUse hook on `Write`,
  and a SubagentStart hook with an empty matcher. Each line records `hook_event_name`,
  `session_id`, `agent_id`, `agent_type`, the `tool_input` keys and the hook's own
  `CLAUDE_CODE_SESSION_ID`.
- **Session.** One `claude -p --permission-mode bypassPermissions`, never `--bare`. The main loop
  did three things: a `Write` to `probe/main.txt`, one `Agent` subagent (general-purpose) writing
  `probe/agent.txt`, and one inline `Workflow` script whose one agent wrote `probe/wf.txt`. All three
  files exist, and the session exited 0.

## Observation — five lines, verbatim fields

| # | event | session_id | agent_id | agent_type | hook env CLAUDE_CODE_SESSION_ID |
|---|---|---|---|---|---|
| 1 | PreToolUse Write `main.txt` | ffb9b24b-1347-4e3f-a11e-51e43cd0b681 | — | — | ffb9b24b-1347-4e3f-a11e-51e43cd0b681 |
| 2 | SubagentStart | ffb9b24b-1347-4e3f-a11e-51e43cd0b681 | a1c4abcdce88b8d7f | general-purpose | ffb9b24b-1347-4e3f-a11e-51e43cd0b681 |
| 3 | PreToolUse Write `agent.txt` | ffb9b24b-1347-4e3f-a11e-51e43cd0b681 | a1c4abcdce88b8d7f | general-purpose | ffb9b24b-1347-4e3f-a11e-51e43cd0b681 |
| 4 | SubagentStart | ffb9b24b-1347-4e3f-a11e-51e43cd0b681 | a94acd73b3be04d3b | workflow-subagent | ffb9b24b-1347-4e3f-a11e-51e43cd0b681 |
| 5 | PreToolUse Write `wf.txt` | ffb9b24b-1347-4e3f-a11e-51e43cd0b681 | a94acd73b3be04d3b | workflow-subagent | ffb9b24b-1347-4e3f-a11e-51e43cd0b681 |

The SubagentStart payload keys are `session_id transcript_path cwd scratchpad_dir prompt_id
agent_id agent_type hook_event_name`. A subagent's PreToolUse payload adds `agent_id` and
`agent_type` to the main loop's keys.

## Liveness

The log holds the main loop's Write line (1), and each spawn kind's own Write line (3, 5). It also
holds a SubagentStart line for each kind (2, 4). Neither kind is a DEAD PROBE. The probe could have
answered no: line 4 could have been absent, and an `agent_id` line could have carried a different
`session_id`. Neither happened.

## Decisions

- **TOOL-aRoutedQuill-2 F1: yes.** Every line carrying `agent_id` has a `session_id` byte-equal to
  the main loop's Write line, for both the `Agent` and the `Workflow` spawn kinds. The card keyed by
  the payload's `session_id` is the parent's card, and no option (a) to (c) is needed.
- **TOOL-aRoutedQuill-4 F1: yes, it fires for both kinds.** `SubagentStart` fires for an `Agent`
  subagent and for a `Workflow` sidechain agent (`agent_type: workflow-subagent`), and its
  `session_id` is the parent's. The context hook reads the same card as the gate.

The clone at `%TEMP%/rqp1` and the log at `%TEMP%/rqp1-hook/` are throwaway. This record is the
evidence.
