**Serves:** research TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6

# The agent-type probe — what a custom agent type reports, and whether `omitClaudeMd` trims the charter

Run 2026-10-11 on node `a`, Claude Code 2.1.292 (`claude` on PATH), by this build's main loop during
orientation, before the roster was written. It extends the instrument of aRoutedQuill's
subagent-payload probe (`TOOL-aRoutedQuill-2` F1) with two custom agent types.

## Instrument

- **Clone.** `git clone --local` of this worktree at `d22cca6cb` to `%TEMP%/ocp1`, a short root
  because a clone under the scratchpad hits MAX_PATH. Gov's own `.claude/settings.json` was kept,
  with two hooks appended that run one node logger: `PreToolUse` on matcher `Write`, and
  `SubagentStart` on an empty matcher. The logger writes one JSON line per call with
  `hook_event_name`, `tool_name`, `agent_id`, `agent_type`, `tool_input.file_path` and the
  payload's sorted key list, and always exits 0.
- **A codeword in the charter.** One line was appended to the clone's `AGENTS.md`, which
  `CLAUDE.md` imports: `PROBE-SENTINEL: the codeword for this repository is MARMALADE-4417.`
- **Two custom agent types** under the clone's `.claude/agents/`, created before the session
  started. They are byte-identical except for one front-matter line:
  - `gov-probe`: `tools: Write`, `model: inherit`, `omitClaudeMd: true`.
  - `gov-probe-full`: the same, without `omitClaudeMd`.

  Both bodies read: "You are a probe. You hold one tool, Write. Do exactly what the task says and
  nothing else. Never read a file. Answer only from the instructions and context you were started
  with."
- **Session.** One `claude -p --permission-mode bypassPermissions`. The main loop was told never to
  repeat the codeword in a prompt it wrote. Every agent got the same task: without reading a file,
  write the codeword named by any `PROBE-SENTINEL` line in its own starting instructions or context
  into its file, else write `NONE`. The six arms were:
  - **a1**: Agent, `general-purpose`.
  - **a2**: Agent, `gov-probe`.
  - **a3**: Agent, `gov-probe-full`.
  - **w1, w2, w3**: one inline `Workflow` script, run sequentially: `agentType: 'gov-probe'`, no
    `agentType`, and `agentType: 'gov-probe-full'`.

## Observation

| Arm | Spawn | Type asked | `agent_type` in both payloads | File |
|---|---|---|---|---|
| a1 | Agent | general-purpose | `general-purpose` | `MARMALADE-4417` |
| a2 | Agent | gov-probe (`omitClaudeMd`) | `gov-probe` | `NONE` |
| a3 | Agent | gov-probe-full | `gov-probe-full` | `MARMALADE-4417` |
| w1 | Workflow | gov-probe (`omitClaudeMd`) | `gov-probe` | `NONE` |
| w2 | Workflow | none | `workflow-subagent` | `MARMALADE-4417` |
| w3 | Workflow | gov-probe-full | `gov-probe-full` | `MARMALADE-4417` |

Every arm logged exactly one `SubagentStart` line and one `PreToolUse Write` line, and each pair
carries the same `agent_id`. The `SubagentStart` keys are `agent_id agent_type cwd hook_event_name
prompt_id scratchpad_dir session_id transcript_path`. A subagent's `PreToolUse` adds `effort
permission_mode tool_input tool_name tool_use_id`.

## Liveness

Both readings occurred on both spawn kinds. The codeword was reported by four arms and `NONE` by
two, and `agent_type` read the custom name on four arms and the built-in name on two. Either reading
could have been absent, so neither question is a DEAD PROBE. The two `NONE` arms differ from their
control arms (a3, w3) only in the `omitClaudeMd` line. So the difference is that key, and not the
body or the model declining the task.

## What this decides

- **A custom agent type reaches every hook payload under its own name**, for an `Agent` spawn and
  for a `Workflow` `agent()` given `agentType`. A hook can therefore key a write rule on the role
  that is writing, inside a harness pass as well as in a direct spawn. A `Workflow` agent given no
  `agentType` reads `workflow-subagent`, which names no role.
- **`omitClaudeMd: true` removes the charter from a custom agent's context on this CLI.** This
  supersedes, for 2.1.292, the 2026-10-04 observation recorded by `TOOL-aMendedFleet-67` that a
  custom type could not skip `CLAUDE.md`. A role agent rendered with the key starts holding only its
  own system prompt and the task it is handed.
- **Not measured here:** whether a definition created in a RUNNING session is spawnable (both
  types existed before `claude -p` started), and any CLI version other than 2.1.292. The render unit
  re-runs this probe as its own acceptance check rather than citing this record.

The clone at `%TEMP%/ocp1` and the log at `%TEMP%/ocp1-hook/` are throwaway. This record is the
evidence.
