// orient-counterfactual.js — ONE stage-2 arm per call: two matched kickoffs under one agent type
// and one probe set, each measured as tokens and wall to READY. TOOL-aReplayedCard-5.
//
// THE MATRIX IS THE CALLER'S. {agent: orient | Explore} x {recall: in | out} x {reuse: in | out}
// is eight arms, and this script runs exactly one of them per `Workflow` call, the way
// unattended-unit.js builds one unit per call: the parent holds the roster and the order, and a
// script that iterated the matrix would need a loop the fan-out hook cannot size.
//
// THE RUN COUNT IS A MARKED TWO-ELEMENT LITERAL iterated by the ONE loop shape agent-cap.js admits,
// `for (const i of RUNS)` under `gov:sequential-agents(2)`, with `await agent(` directly inside.
// The marker is what makes the two kickoffs SEQUENTIAL rather than a fan: two kickoffs sharing the
// repository's wall clock would each measure the other's disk and index traffic, and a matched pair
// is matched only when the second starts after the first ends. The record proves that property
// per run rather than asserting it.
//
// THE SCRIPT RETURNS THE RECORD AND WRITES NOTHING. A workflow script holds no filesystem, no
// `Date.now()`, and no way to read a subagent's context size. So: wall is the AGENT's own `date`
// at its first and last Bash call, returned in the schema; tokens are `budget.spent()` deltas
// around each spawn, which count the workflow's OUTPUT tokens during that spawn and nothing else,
// and the record says so in its own `tokensNote` so a reader cannot mistake the figure for the
// subagent's total context. The caller writes the return under the build's record folder.
//
// EVERY RUN CARRIES A CLOSED `outcome`, so a dead arm is a named value and never a zero:
// `spawned`, `null` (the harness's documented dead-agent shape), `threw` (a terminal error, its
// message kept), or `refused-step` (the agent ran but reports a step it could not execute — an
// Explore-typed agent with no Bash, say — with the step named). A `refused-step` arm is re-run ONCE
// with the default workflow agent type, outside the marked loop, and the record names which type
// ran. An arm none of whose runs spawned reads `arm unavailable` naming the type, which is how a
// missing `orient` definition is reported rather than measured.
//
// IT SPELLS NO PATHS. The repository, the task and the arm arrive in `args`; the engine's text, when
// the arm's agent type holds no Skill tool to load it, arrives as an optional `engine` path the
// caller spells. A kit file names nothing outside itself by literal.
export const meta = {
  name: 'orient-counterfactual',
  version: '1.0', // gov:kit orient-counterfactual@1.0 — engine identity (deployed verbatim)
  description:
    'Measures ONE stage-2 orientation arm: two sequential kickoffs under one agent type and one probe set, each as a budget.spent() token delta and the agent-read wall to READY. Returns the record; the caller writes it.',
  phases: [{ title: 'Measure', detail: 'two sequential kickoffs under the arm, then one default-type fallback if a step was refused' }],
}

// ARGS ARRIVE AS A STRING even when the caller hands the tool JSON — parse first, validate second,
// the guard tier2-review.js added after twice reviewing the wrong repository.
let cfg = args
if (typeof cfg === 'string') {
  try {
    cfg = JSON.parse(cfg)
  } catch (e) {
    throw new Error(
      'orient-counterfactual: args must be JSON carrying repo, task and arm; could not parse the string given (' +
        e.message + '). Refusing to default any of them.',
    )
  }
}
if (!cfg || typeof cfg !== 'object' || Array.isArray(cfg)) {
  throw new Error('orient-counterfactual: args must be an object carrying repo, task and arm. Refusing to default any of them.')
}
if (!cfg.repo) throw new Error('orient-counterfactual: args must carry an explicit `repo`. Defaulting the kickoff root to the process cwd is how a sibling harness reviewed the wrong repository, twice.')
if (!cfg.task || typeof cfg.task !== 'string') throw new Error('orient-counterfactual: args must carry an explicit `task` string. A kickoff with no task derives no scope, and two runs of it would match on nothing.')
// THE ARM IS CLOSED. `agent` is one of the two matrix values and the two probe flags are booleans;
// a third agent type or a truthy string where a boolean belongs is refused, never coerced, because
// a coerced flag measures an arm nobody asked for and files it under the arm they did.
const arm = cfg.arm
const AGENTS = ['orient', 'Explore']
if (!arm || typeof arm !== 'object' || AGENTS.indexOf(arm.agent) === -1 || typeof arm.recall !== 'boolean' || typeof arm.reuse !== 'boolean') {
  throw new Error(
    'orient-counterfactual: args.arm must be {agent: ' + AGENTS.join(' | ') + ', recall: boolean, reuse: boolean}. Got ' +
      JSON.stringify(arm) + '. Refusing to coerce — a coerced arm files a measurement under the wrong cell.',
  )
}
const repo = cfg.repo
const task = cfg.task
const engine = typeof cfg.engine === 'string' && cfg.engine ? cfg.engine : ''

// THE RETURN SHAPE OF ONE KICKOFF. `refusedStep` is REQUIRED and an empty string means every step
// ran: an absent field would be indistinguishable from a run that never reached the question.
// `startMs` and `endMs` are the agent's own `date` readings, because this script cannot stamp time.
const RUN_SCHEMA = {
  type: 'object',
  required: ['ready', 'card', 'startMs', 'endMs', 'refusedStep', 'recallRan', 'reuseRan'],
  additionalProperties: true,
  properties: {
    ready: { type: 'string' },
    card: { type: 'string' },
    startMs: { type: 'integer' },
    endMs: { type: 'integer' },
    refusedStep: { type: 'string' },
    recallRan: { type: 'boolean' },
    reuseRan: { type: 'boolean' },
  },
}

// The prompt for run `i`. Rendered once per spawn rather than hoisted, because the run index is
// in the text: the second kickoff is told it is the second so it does not read the first's warm
// index as its own doing, and the record's reader can tell the two apart by their READY lines.
function renderPrompt(i) {
  return (
    'You are kickoff run ' + (i + 1) + ' of 2 under one measured arm. Work ONLY in the repository at ' + repo + '.\n\n' +
    'FIRST, before anything else, run `date +%s%3N` in Bash and keep the integer: that is startMs. ' +
    'Your LAST action before returning is the same command: that is endMs. Both are epoch milliseconds.\n\n' +
    'Then run the kickoff engine\'s Steps 0 through 4 for this task:\n  ' + task + '\n\n' +
    'Load the engine by invoking the `session-kickoff` Skill.' +
    (engine
      ? ' If you hold no Skill tool, Read the engine\'s text WHOLE at ' + engine + ' instead and follow it.'
      : ' If you hold no Skill tool, you cannot run this arm: return refusedStep naming `Skill`.') +
    '\n\n' +
    'Probe set for this arm: the memory-recall probe is ' + (arm.recall ? 'IN — run it where the engine asks' : 'OUT — skip it and say so in the card') +
    '; the reuse-lookup probe is ' + (arm.reuse ? 'IN — run it where the engine asks' : 'OUT — skip it and say so in the card') + '.\n\n' +
    'Rules: never mint a session slug; write NO file and run NO command that mutates the tree; every ' +
    'question the engine would put to a user becomes a line under `open` in the card instead of an ask. ' +
    'Cite files by path and line, never ingest them into the card.\n\n' +
    'Return JSON {ready, card, startMs, endMs, refusedStep, recallRan, reuseRan}: `ready` is the READY ' +
    'line the engine derives (empty if you never reached it); `card` is the orientation card body you ' +
    'would append — task, the rows you read, the records recall found, the gotcha classes, the open ' +
    'questions — as text; `refusedStep` is EMPTY when every step ran, else the step you could not ' +
    'execute and why (a tool you do not hold, a command that was refused); `recallRan` and `reuseRan` ' +
    'say whether each probe actually executed.'
  )
}

// The spawn options. `agentType` is present only for the two matrix types; the fallback run omits
// it so the default workflow agent is what runs, and the record names that type as `default`.
function buildOpts(i, type) {
  const o = { label: 'run:' + (i + 1) + ':' + type, phase: 'Measure', schema: RUN_SCHEMA }
  if (type !== 'default') o.agentType = type
  return o
}

// ONE RUN'S RECORD, derived from what the spawn returned or threw and the token figures around it.
// The outcome set is closed here and nowhere else; a reader greps `outcome` and finds one of four.
function measureRun(i, type, before, after, r, err) {
  const run = { run: i + 1, type: type, tokens: after - before, outcome: '', reason: '', startMs: null, endMs: null, wallMs: null, ready: '', card: '', recallRan: null, reuseRan: null }
  if (err) {
    run.outcome = 'threw'
    run.reason = String(err && err.message ? err.message : err)
    return run
  }
  if (r === null || r === undefined) {
    run.outcome = 'null'
    run.reason = 'agent() returned null: the agent died on a terminal error after retries, or was skipped'
    return run
  }
  run.startMs = r.startMs
  run.endMs = r.endMs
  run.wallMs = r.endMs - r.startMs
  run.ready = r.ready
  run.card = r.card
  run.recallRan = r.recallRan
  run.reuseRan = r.reuseRan
  if (r.refusedStep) {
    run.outcome = 'refused-step'
    run.reason = 'the agent could not execute a step: ' + r.refusedStep
    return run
  }
  run.outcome = 'spawned'
  return run
}

phase('Measure')

const RUNS = [0, 1] // gov:fixed-verifiers
const runs = []
for (const i of RUNS) { // gov:sequential-agents(2)
  const before = budget.spent()
  let r = null
  let err = null
  try {
    r = await agent(renderPrompt(i), buildOpts(i, arm.agent))
  } catch (e) {
    err = e
  }
  runs.push(measureRun(i, arm.agent, before, budget.spent(), r, err))
  log('run ' + (i + 1) + ' ' + arm.agent + ': ' + runs[i].outcome + (runs[i].wallMs === null ? '' : ' · ' + runs[i].wallMs + ' ms') + ' · ' + runs[i].tokens + ' output tokens')
}

// THE FALLBACK, once and outside the loop. An arm whose agent type could not execute a step has
// answered the question the arm asks — that type cannot orient — and the re-run under the default
// type says whether the STEP or the TYPE was the problem. One spawn, never one per refused run: a
// second marked loop is refused by the hook, and one answer is all the question needs.
let fallback = null
const refusedIdx = runs.findIndex(function (x) { return x.outcome === 'refused-step' })
if (refusedIdx !== -1) {
  const before = budget.spent()
  let r = null
  let err = null
  try {
    r = await agent(renderPrompt(refusedIdx), buildOpts(refusedIdx, 'default'))
  } catch (e) {
    err = e
  }
  fallback = measureRun(refusedIdx, 'default', before, budget.spent(), r, err)
  fallback.fallbackFor = arm.agent
  log('fallback for run ' + (refusedIdx + 1) + ' under the default type: ' + fallback.outcome)
}

// THE VERDICT IS DERIVED, never authored: an arm none of whose runs spawned is UNAVAILABLE and the
// record says so naming the type; `sequential` is proven from the two agents' own clocks and is
// null, not true, when either run has no clock to compare.
const spawnedN = runs.filter(function (x) { return x.outcome === 'spawned' }).length
const sequential = runs[0].endMs !== null && runs[1].startMs !== null ? runs[1].startMs > runs[0].endMs : null
const verdict =
  spawnedN === 0
    ? 'arm unavailable: ' + arm.agent + ' — ' + runs.map(function (x) { return 'run ' + x.run + ' ' + x.outcome + ': ' + x.reason }).join('; ')
    : spawnedN === runs.length
      ? 'measured'
      : 'partial: ' + spawnedN + '/' + runs.length + ' runs spawned'

return {
  arm: { agent: arm.agent, recall: arm.recall, reuse: arm.reuse },
  repo: repo,
  task: task,
  verdict: verdict,
  sequential: sequential,
  runs: runs,
  fallback: fallback,
  tokensNote:
    'each `tokens` is the budget.spent() delta around that spawn: the OUTPUT tokens the workflow spent while the agent ran, not the subagent\'s total context and not the main loop\'s occupancy',
  wallNote: 'each `wallMs` is endMs - startMs as the agent itself read `date +%s%3N` at its first and last Bash call; the harness stamps no time',
}
