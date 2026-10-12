**Serves:** research TOOL-aOrientedCast-3

# The agent-type probe, re-run against the rendered types

Run 2026-10-11 on node `a` by the pass that built `render_agents.py`, as AC7 of
TOOL-aOrientedCast-3 states it. It re-aims the agent-type probe record beside this one at the two
RENDERED role types, `gov-builder` and `gov-spec-writer`, with the three changes the spec's
"The probe re-run" names.

## Instrument

- **Clone.** `git clone --local` of the build's worktree at
  `58c109be8c2bfc4f57afbd22d4b4136cf3baf963`, the pass's parent, to `%TEMP%/oc3r`. The pass had not
  committed, so the nine rendered types under `.claude/agents/` and `.claude/roles.json` were copied
  into the clone from the worktree's `render_agents.py --write` before the session started.
- **Sentinel.** One line appended to the clone's `AGENTS.md`, after its last heading (`## Conventions`,
  outside every `§` section) and after the render: `PROBE-SENTINEL: the codeword for this repository
  is TANGERINE-5391.` A `grep -c` of the codeword over the nine copied types read 0 in each.
- **Logger.** Gov's own `.claude/settings.json` was kept, with the logger below appended on
  `PreToolUse` matcher `*` and on `SubagentStart` matcher `*`, logging to a directory outside the
  clone. Every tool is logged, so a role agent that READ the governing doc would show a `Read`
  before its `Write`.
- **Session.** One `claude -p --permission-mode bypassPermissions`, started in the clone with the
  parent session's `CLAUDE_PROJECT_DIR`, `CLAUDE_CODE_SESSION_ID`, `CLAUDECODE` and
  `CLAUDE_CODE_ENTRYPOINT` unset. `claude --version` in the clone read `2.1.292 (Claude Code)`. The
  main loop was told never to repeat the codeword, to read no file and run no command, and to make
  three `Agent` calls (`general-purpose`, `gov-builder`, `gov-spec-writer`) and one `Workflow` call
  running the script below. Every arm's task text, with `<arm>` its own: "This is a probe, not a
  build. Without reading any file and without running any command, write into
  `C:/Users/DAILY-~1/AppData/Local/Temp/oc3r/probe-out/<arm>.txt` the codeword named by any
  PROBE-SENTINEL line in your own starting instructions or context, or `NONE`." The path is the
  clone root's `probe-out/`, spelled absolute because the `Write` tool takes an absolute path.

```js
// logger.js — one JSON line per hook call, always exit 0. Log path is argv[2].
const fs = require('fs')
let raw = ''
process.stdin.on('data', (c) => { raw += c })
process.stdin.on('end', () => {
  try {
    const p = JSON.parse(raw)
    const row = {
      hook_event_name: p.hook_event_name,
      tool_name: p.tool_name,
      agent_id: p.agent_id,
      agent_type: p.agent_type,
      file_path: p.tool_input && p.tool_input.file_path,
    }
    fs.appendFileSync(process.argv[2], JSON.stringify(row) + '\n')
  } catch (e) {
    try { fs.appendFileSync(process.argv[2], JSON.stringify({ error: String(e) }) + '\n') } catch (_) {}
  }
  process.exit(0)
})
```

```js
// probe-wf.js — the Workflow arms, run one after another.
export const meta = {
  name: 'oc3r-probe',
  description: 'TOOL-aOrientedCast-3 AC7: three Workflow arms, run one after another.',
  phases: [{ title: 'Arms', detail: 'w1 gov-builder, w2 gov-spec-writer, w3 untyped control' }],
}

const OUT = 'C:/Users/DAILY-~1/AppData/Local/Temp/oc3r/probe-out/'
const task = (arm) =>
  'This is a probe, not a build. Without reading any file and without running any command, write into `' +
  OUT + arm + '.txt` the codeword named by any PROBE-SENTINEL line in your own starting instructions or ' +
  'context, or `NONE`.'

await agent(task('w1'), { label: 'w1', agentType: 'gov-builder' })
await agent(task('w2'), { label: 'w2', agentType: 'gov-spec-writer' })
await agent(task('w3'), { label: 'w3' })
```

## Observation

| Arm | Spawn | Type asked | `agent_id` | `agent_type` on both lines | Lines on the id | File |
|---|---|---|---|---|---|---|
| a1 | Agent | general-purpose (control) | `a7ea971f05e6d572c` | `general-purpose` | SubagentStart, PreToolUse Write | `TANGERINE-5391` |
| a2 | Agent | gov-builder | `a67bf339bff9dedfd` | `gov-builder` | SubagentStart, PreToolUse Write | `NONE` |
| a3 | Agent | gov-spec-writer | `a5b900b79d00c4cd8` | `gov-spec-writer` | SubagentStart, PreToolUse Write | `NONE` |
| w1 | Workflow | gov-builder | `a2610b363696f89f7` | `gov-builder` | SubagentStart, PreToolUse Write | `NONE` |
| w2 | Workflow | gov-spec-writer | `acd49df246402c600` | `gov-spec-writer` | SubagentStart, PreToolUse Write | `NONE` |
| w3 | Workflow | none (control) | `a7dcc3eeae7e27651` | `workflow-subagent` | SubagentStart, PreToolUse Write | `TANGERINE-5391` |

The log held 16 lines: the six pairs above, three `PreToolUse Agent` lines and one
`PreToolUse Workflow` line from the main loop, which carry no `agent_id`. No arm logged any
`PreToolUse` line on its id before its `Write`, so every arm is VALID by the spec's rule, and no role
agent read the governing doc to learn the codeword.

## Liveness

Both controls are valid and read the codeword, so the sentinel reached a context on both spawn
kinds: neither role arm's `NONE` is a DEAD PROBE. Each role arm differs from its control in the
type asked, and the rendered types differ from a plain definition in `omitClaudeMd: true` and their
body; the earlier probe already isolated the key as what removes the charter.

## What this decides

- AC7 of TOOL-aOrientedCast-3 holds on Claude Code 2.1.292: the four role arms a2, a3, w1 and w2 are
  valid and pass, reporting their own type as `agent_type` on both payloads and reading `NONE`.
- A rendered role type starts without the governing doc, on both spawn routes, while carrying the
  charter sections its role names inside its own body.
- Not measured: any other CLI version, a server-flag flip, and a type created or changed in a
  running session. The clone at `%TEMP%/oc3r` and the log at `%TEMP%/oc3r-hook/` are throwaway; this
  record is the evidence.
