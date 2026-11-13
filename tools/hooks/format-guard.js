#!/usr/bin/env node
/**
 * format-guard — a `Stop` hook that refuses the turn end of a session routed to a live build when the
 * final message lacks the charter's BUILD/SPEC pair, breaks rule r1, leaves a new commit unreported, or
 * leaves out the `agent` or `returned` line of an agent its turn dispatched or received.
 *
 * gov:kit agent-cap@1.48 — ships inside the hooks kit entry; the kit version is agent-cap.js's.
 *
 * Contract: the spec for TOOL-aHeardState-1 under the build folder of that slug.
 *
 * WHY THIS IS A HOOK. The charter's micro-formats are mandatory and emission had no machine gate: one
 * unattended session emitted none across 1,162 assistant entries, before and after a compaction. The
 * rule sat in the charter, and a `minimal-prose` reading of it said "say less". The `Stop` event is
 * the one surface that sees the final message at the moment the session decides to end its turn, and
 * a `{"decision":"block","reason":…}` on exit 0 there reaches the model as `Stop hook feedback:`.
 *
 * WHEN IT ARMS, all three or nothing: the payload's `session_id` has an orientation card under the
 * git common dir; the card's `## route` carries a `- build: <slug>` line; and `<slug>` is a row of
 * `<MEMORY_ROOT>/LIVE.md` at the payload cwd's toplevel. LIVE.md is the GENERATED non-terminal set, so
 * this hook restates no terminal-status list. Unarmed, it exits 0 and prints nothing.
 *
 * THE GRAMMAR IS READ, NEVER RESTATED. The BUILD, SPEC, committed and merged shapes are derived from
 * the `<!-- microformats -->` fence of the toplevel's AGENTS.md, the same fence check-microformats.sh
 * keys on. A placeholder `<…>` becomes a run carrying no ` · `, literal text stays literal, `[ · …]`
 * becomes an optional group, and the line is anchored at a column-0 `- `. A charter edit moves this
 * hook with it. No fence, or no definition for a head keyword, allows with one stderr witness line.
 *
 * WHAT BLOCKS, each a defect named in the reason with the definition it breaks:
 *   - no bare BUILD line; no bare SPEC line while the route names a unit with a `· spec` path;
 *   - the line after the last bare BUILD line is not a bare SPEC line (the [pair] rule);
 *   - a BUILD or SPEC line that is not a bare list item: backticked, bold, indented, a heading, inside
 *     a fence, or without its `- ` (rule r1);
 *   - a bare BUILD or SPEC line that fails its derived shape;
 *   - HEAD moved since this session's previous armed stop, and a new first-parent commit is named by
 *     no bare `committed` or `merged` line whose sha field is a 7+ hex prefix of it;
 *   - an agent this turn dispatched with no bare `agent` line, or received with no bare `returned`
 *     line, in its derived shape and whose text after its last ` · ` ends `/<agent-id>`
 *     (TOOL-aOrientedCast-21). Only when the fence defines both shapes; otherwise a turn that holds an
 *     agent writes one witness and requires nothing.
 * A blocking reason also prints the lines it asks for, ready to paste (TOOL-dPavedRoad-2): a
 * `committed` line rendered through the charter's shape from the commit's sha, the worktree's branch
 * and the subject, and each `agent` or `returned` line `handoff.py agents` derives, run with no shell,
 * no `--write` and the turn's own selector inside HANDOFF_BOUND_MS; a line off its shape is withheld,
 * and any failure keeps the verb's sentence with one witness line.
 * HOW THE TURN'S AGENTS ARE READ. From the transcript the payload's `transcript_path` names: the turn
 * opens at the earliest of the last run of typed `user` records, the run-log prose reader's rule, with
 * two exceptions (TOOL-aOrientedCast-24): a compaction summary opens nothing, and neither does a meta
 * record in a run of meta records directly after a tool result, such as a Skill's expansion or an
 * image's size note. An idle-wake tick or a stop hook's feedback follows assistant text, so it still
 * opens its turn. An
 * `Agent` result carrying `agentId` owes its `agent` line, and its `returned` line when `completed`; a
 * `Workflow` result carrying `runId` owes an `agent` line per `started` entry of
 * `<session dir>/subagents/workflows/<run id>/journal.jsonl`, and a `returned` line per `result` or
 * `failed` entry unless it was `async_launched`; a delivered task notification, a `user` record or a
 * `queued_command` attachment, owes the `returned` line of the agent its tool-use id names, or both
 * lines for every agent of the run it names. That id is read from the notification's header alone:
 * the first `<tool-use-id>` before its first `<result>`, so an id the agent quotes in its result names
 * nothing. A run id outside `[A-Za-z0-9_-]{1,64}` is never joined into a path. No `transcript_path`,
 * an unreadable transcript or journal, or a run id off its shape allows the arm with one witness line
 * each; lines in the turn that do not parse are counted into one witness line, and the arm
 * still grades the records that parsed.
 * The last HEAD seen lives in `<git-dir>/format-guard/<sid>.head`, per worktree, written on every
 * armed stop that reached the checks. The first armed stop of a session records a baseline only; a
 * recorded sha that is not an ancestor of HEAD writes a witness and blocks nothing. Git is spawned
 * only when HEAD moved.
 *
 * THE BOUND. Never a block when `stop_hook_active` is true: the harness sets it on every stop that
 * follows a block, whichever hook blocked, so this hook refuses at most once per turn end, keeps no
 * count, and cannot loop under the harness's cap.
 *
 * WHAT THIS DOES NOT CHECK. Emission mid-turn. The ⏳ heartbeat. Every other micro-format — gates,
 * pushed, READY, up, unchanged, skipped. Field VALUES: a well-formed pair naming the wrong build or a
 * stale count passes. WHERE in the message the pair sits, and whether the message opens with its
 * highest-severity item (the [state] rule). Sub-agent stops (`Stop` is the main agent's event; a
 * payload carrying `agent_id` exits 0). EVERY STOP AFTER A BLOCK IN THE SAME CHAIN, whichever hook
 * blocked — so inside an unattended run, whose stop-guard blocks `run-open` turn ends, only the first
 * stop of each chain is graded. A chained stop leaves the HEAD sidecar where it was, so a commit made
 * in the continuation is not graded there and is demanded at the next unchained armed stop, even when
 * a chained message already reported it. An `agent` or `returned` line's field VALUES: a well-formed
 * line naming the right agent with a wrong model passes. An agent a sub-agent spawned. An agent a
 * harness run starts after this stop. A task notification queued but not yet delivered. A second
 * notification block in one record: only the first block's header id is read, so that second agent's
 * `returned` line is not required (no measured delivery carried two). An agent dispatched before an
 * owner's interjection or an interrupt: a typed record that is not a meta record opens a turn
 * wherever it sits, a tool result before it included, so the turn splits there. The run-log prose
 * reader still opens a turn at every typed record, so the two readers differ on the two exceptions
 * above. Whether the
 * transcript format still holds: a renamed field reads as a turn with no agent, silently. A derived
 * line's field VALUES, which are the verb's. A line for an agent whose prompt carries no `gov:handoff`
 * marker, such as a built-in agent type. A derivation the bound cut short: that agent keeps the verb's
 * sentence. Whether this hook is WIRED: check-wiring.sh and check-hook-destinations.sh own that. A
 * broken hook never blocks a stop — every failure path is an allow, and an uncaught error exits 0.
 */
'use strict'

const fs = require('fs')
const path = require('path')
const { spawnSync } = require('child_process')
const { readCard, extractRouteUnits, readConfKey, resolveToplevel, resolveCommonDir } = require('./scratch-guard.js')

const CHARTER_FILE = 'AGENTS.md'
const CONF_FILE = '.memory-tree.conf'
const FENCE_OPEN = '<!-- microformats -->'
const FENCE_CLOSE = '<!-- /microformats -->'
const SIDECAR_DIR = 'format-guard'
const SHA_MIN = 7
const GIT_BOUND_MS = 10000
// One budget for every `handoff.py agents` spawn of one stop, well under the harness's Stop timeout.
const HANDOFF_BOUND_MS = 20000
// resolve_python's launcher order, after GOV_PYTHON.
const PYTHON_LAUNCHERS = ['python3', 'python', 'py']
const AGENT_HEADS = ['agent', 'returned']
const RUN_ID_RE = /^[A-Za-z0-9_-]{1,64}$/
// The Claude Code session directory holding one subdirectory per Workflow run, not the review-harness kit.
const WORKFLOW_RUNS_DIR = 'workflows'

function readStdin() {
  try {
    return fs.readFileSync(0, 'utf8')
  } catch {
    return ''
  }
}

/** The `.git` FILE's `gitdir:` target, or the `.git` directory itself: where this worktree's HEAD lives. */
function resolveGitDir(hit) {
  if (!hit.isFile) return hit.gitPath
  const m = /gitdir:\s*(.+)/.exec(fs.readFileSync(hit.gitPath, 'utf8'))
  return m ? path.resolve(hit.toplevel, m[1].trim()) : null
}

/** HEAD's sha without a spawn: a detached HEAD, a loose ref under the common dir, or packed-refs. '' when unreadable. */
function readHeadSha(gitDir, commonDir) {
  let head
  try { head = fs.readFileSync(path.join(gitDir, 'HEAD'), 'utf8').trim() } catch { return '' }
  if (/^[0-9a-f]{40}$/.test(head)) return head
  const m = /^ref:\s*(\S+)$/.exec(head)
  if (!m) return ''
  for (const dir of [gitDir, commonDir]) {
    try {
      const v = fs.readFileSync(path.join(dir, m[1]), 'utf8').trim()
      if (/^[0-9a-f]{40}$/.test(v)) return v
    } catch { /* not loose here */ }
  }
  try {
    for (const line of fs.readFileSync(path.join(commonDir, 'packed-refs'), 'utf8').split(/\r?\n/)) {
      const p = /^([0-9a-f]{40}) (\S+)$/.exec(line)
      if (p && p[2] === m[1]) return p[1]
    }
  } catch { /* no packed-refs */ }
  return ''
}

/** The build slugs `<MEMORY_ROOT>/LIVE.md` lists: every table row whose link target is `builds/<slug>/README.md`. */
function readLiveSlugs(top) {
  let conf
  try { conf = fs.readFileSync(path.join(top, CONF_FILE), 'utf8') } catch { return null }
  // No default root: a guessed one would arm the hook in a tree that never declared a memory tree.
  const memRoot = (readConfKey(conf, 'MEMORY_ROOT') || '').trim()
  if (!memRoot) return null
  let live
  try { live = fs.readFileSync(path.join(top, memRoot, 'LIVE.md'), 'utf8') } catch { return null }
  const slugs = new Set()
  for (const line of live.split(/\r?\n/)) {
    const m = /^\|\s*\[[^\]]*\]\(builds\/([^/)]+)\/README\.md\)/.exec(line)
    if (m) slugs.add(m[1])
  }
  return slugs
}

/**
 * One line regex from one charter definition. The definition's text between the backticks is split
 * into literal runs and `<…>` placeholders; `[ · …]` is an optional group. A placeholder matches a
 * run that carries no ` · `, so a missing or extra field moves the field count and fails.
 */
function buildShapeRegex(def) {
  const renderLiteral = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')
  const field = '(?:(?! · ).)+?'
  const render = (s) => s.split(/(<[^>]*>)/).map((t) => (/^<[^>]*>$/.test(t) ? field : renderLiteral(t))).join('')
  let body = ''
  let rest = def
  for (;;) {
    const i = rest.indexOf('[ · ')
    if (i < 0) { body += render(rest); break }
    const j = rest.indexOf(']', i)
    if (j < 0) { body += render(rest); break }
    body += render(rest.slice(0, i)) + '(?:' + render(rest.slice(i + 1, j)) + ')?'
    rest = rest.slice(j + 1)
  }
  return new RegExp('^- ' + body.replace(/(?: …|…)$/, '(?: · .+)*') + '\\s*$')
}

/** `{ shapes: { head: { def, re } }, error }` from the charter's fence; `error` names what is missing. */
function readCharterShapes(top) {
  const file = path.join(top, CHARTER_FILE)
  let text
  try { text = fs.readFileSync(file, 'utf8') } catch { return { shapes: null, error: `no ${CHARTER_FILE} at ${top}` } }
  const lines = text.split(/\r?\n/)
  const a = lines.indexOf(FENCE_OPEN)
  const b = lines.indexOf(FENCE_CLOSE)
  if (a < 0 || b < a) return { shapes: null, error: `${CHARTER_FILE} carries no ${FENCE_OPEN} fence` }
  const shapes = {}
  for (const line of lines.slice(a + 1, b)) {
    const m = /^- `(.*)`$/.exec(line)
    if (!m) continue
    const head = m[1].split(' — ')[0]
    shapes[head] = { def: m[1], re: buildShapeRegex(m[1]) }
  }
  for (const need of ['BUILD', 'SPEC', 'committed', 'merged']) {
    if (!shapes[need]) return { shapes: null, error: `${CHARTER_FILE}'s micro-format fence defines no ${need} shape` }
  }
  return { shapes, error: '' }
}

/**
 * Each line of the message with whether it sits inside a fenced block. A backtick run whose line
 * closes it again (an inline span such as three backticks around a command) is not a fence: in
 * CommonMark a backtick fence's info string carries no backtick.
 */
function scanMessageLines(message) {
  let fenced = false
  return String(message).split(/\r?\n/).map((text) => {
    const m = /^ {0,3}(`{3,}|~{3,})(.*)$/.exec(text)
    const fence = !!m && !(m[1][0] === '`' && m[2].includes('`'))
    const row = { text, fenced: fenced || fence }
    if (fence) fenced = !fenced
    return row
  })
}

/** The pair defects of one message: missing, not bare, not adjacent, or off-shape. */
function checkPair(rows, shapes, wantSpec) {
  const defects = []
  const checkBare = (r, head) => !r.fenced && r.text.startsWith(`- ${head} — `)
  for (const head of wantSpec ? ['BUILD', 'SPEC'] : ['BUILD']) {
    const hits = rows.filter((r) => checkBare(r, head))
    if (hits.length === 0) {
      const loose = rows.find((r) => r.text.includes(`${head} — `))
      defects.push(loose
        ? `the ${head} line is not a bare list item at column 0 (rule r1): ${JSON.stringify(loose.text.trim())}`
        : `no ${head} line`)
      continue
    }
    const last = hits[hits.length - 1]
    if (!shapes[head].re.test(last.text)) {
      defects.push(`the ${head} line does not match its charter shape \`${shapes[head].def}\`: ${JSON.stringify(last.text)}`)
    }
  }
  if (wantSpec && defects.length === 0) {
    const i = rows.map((r) => checkBare(r, 'BUILD')).lastIndexOf(true)
    const next = rows[i + 1]
    if (!next || !checkBare(next, 'SPEC')) defects.push('the SPEC line is not on the line right after the BUILD line (the [pair] rule)')
  }
  return defects
}

/**
 * The first-parent commits in prev..head as `[{ sha, subject }]`, or null when prev is not an ancestor
 * or git cannot answer. One spawn, the rev-list walk with each subject beside its sha.
 */
function extractNewCommits(top, prev, head) {
  const r = spawnSync('git', ['log', '--first-parent', '--ancestry-path', '--format=%H%x1f%s', `${prev}..${head}`], {
    cwd: top, encoding: 'utf8', timeout: GIT_BOUND_MS, windowsHide: true,
  })
  if (r.status !== 0) return null
  const commits = []
  for (const line of r.stdout.split(/\r?\n/)) {
    const m = /^([0-9a-f]{40})\x1f(.*)$/.exec(line)
    if (m) commits.push({ sha: m[1], subject: m[2] })
  }
  return commits.length ? commits : null
}

/** The worktree's branch from its HEAD file, or `HEAD`, git's own name for a detached or unreadable one. */
function readHeadBranch(gitDir) {
  let head = ''
  try { head = fs.readFileSync(path.join(gitDir, 'HEAD'), 'utf8').trim() } catch { /* unreadable */ }
  const m = /^ref:\s*refs\/heads\/(\S+)$/.exec(head)
  return m ? m[1] : 'HEAD'
}

/**
 * `- ` plus a charter definition with each `<name>` set to `fields[name]`: in each value ` · ` becomes
 * `, ` and a line break a space, so no value adds a field, and an empty value becomes `unknown` —
 * `render_shape_line`'s rule in handoff.py. Null when the definition names a field `fields` lacks.
 */
function renderShapeLine(def, fields) {
  let lacking = false
  const body = String(def).replace(/<([^<>]+)>/g, (whole, name) => {
    if (!Object.prototype.hasOwnProperty.call(fields, name)) { lacking = true; return whole }
    const v = String(fields[name] == null ? '' : fields[name]).replace(/\r\n|\r|\n/g, ' ').split(' · ').join(', ')
    return v === '' ? 'unknown' : v
  })
  return lacking ? null : '- ' + body
}

/**
 * `{ defects, unmet }`: one defect per new `{ sha, subject }` that no bare committed or merged line
 * names by a 7+ hex prefix, and the commits that produced them.
 */
function checkCommitLines(rows, shapes, commits) {
  const named = []
  for (const r of rows) {
    if (r.fenced) continue
    if (r.text.startsWith('- committed — ') && shapes.committed.re.test(r.text)) {
      named.push(r.text.slice('- committed — '.length).split(' · ')[0].trim())
    } else if (r.text.startsWith('- merged — ') && shapes.merged.re.test(r.text)) {
      const f = r.text.split(' · ')
      if (f.length > 1) named.push(f[1].trim())
    }
  }
  const checkNamed = (sha) => named.some((n) => /^[0-9a-f]+$/.test(n) && n.length >= SHA_MIN && sha.startsWith(n))
  const unmet = commits.filter((c) => !checkNamed(c.sha))
  return { defects: unmet.map((c) => `commit ${c.sha.slice(0, 9)} is new since this session's previous stop and no bare committed or merged line names it`), unmet }
}

/**
 * The final turn of a main transcript: `{ records, text, skipped }`, or `{ error }` when the file is
 * unreadable. A turn opens at a typed `user` record — string content, or text blocks with no
 * `tool_result` — and back-to-back openers are one turn (the run-log prose reader's rule), with two
 * exceptions (TOOL-aOrientedCast-24 S2): a compaction summary opens nothing, and neither does a meta
 * record whose nearest earlier main-file `user` or `assistant` record that is not itself a typed meta
 * record holds a `tool_result`. Walking from the end, such a meta record is PENDING until that older
 * record is parsed, and a pending record with none before it opens the turn. The file is read once
 * and its lines parsed from the end only until the opener is passed; a line that does not parse is
 * skipped and counted. Sidechain records are left out.
 */
function scanTurnRecords(transcriptPath) {
  let text
  try { text = fs.readFileSync(transcriptPath, 'utf8') } catch (e) { return { error: String((e && e.code) || e) } }
  const checkTyped = (rec) => {
    if (!rec || rec.type !== 'user' || rec.isSidechain === true || !rec.message) return false
    const c = rec.message.content
    if (typeof c === 'string') return true
    return Array.isArray(c) && !c.some((b) => b && b.type === 'tool_result') && c.some((b) => b && b.type === 'text' && typeof b.text === 'string')
  }
  // An assistant record that carries text or a tool call ends a run of openers; thinking alone does not.
  const checkSpoke = (rec) => !!rec && rec.type === 'assistant' && rec.isSidechain !== true && !!rec.message && Array.isArray(rec.message.content) &&
    rec.message.content.some((b) => b && ((b.type === 'text' && String(b.text || '').trim()) || b.type === 'tool_use'))
  // The record that settles a pending meta record: main-file, `user` or `assistant`, and not a typed meta record.
  const checkSettles = (rec) => !!rec && (rec.type === 'user' || rec.type === 'assistant') && rec.isSidechain !== true &&
    !(rec.isMeta === true && checkTyped(rec))
  const checkToolResult = (rec) => !!rec.message && Array.isArray(rec.message.content) && rec.message.content.some((b) => b && b.type === 'tool_result')
  const lines = text.split(/\r?\n/)
  const seen = [] // newest first; null marks a line that did not parse
  let opener = -1
  let pending = -1 // the oldest typed meta record of the run still waiting for the record before it
  for (let i = lines.length - 1; i >= 0; i--) {
    if (!lines[i].trim()) continue
    let rec
    try { rec = JSON.parse(lines[i]) } catch { seen.push(null); continue }
    if (pending >= 0 && checkSettles(rec)) {
      if (!checkToolResult(rec)) opener = pending
      pending = -1
    }
    if (opener >= 0 && checkSpoke(rec)) break
    seen.push(rec)
    if (checkTyped(rec) && rec.isCompactSummary !== true) {
      if (rec.isMeta === true) pending = seen.length - 1
      else opener = seen.length - 1
    }
  }
  if (pending >= 0) opener = pending
  const turn = opener < 0 ? [] : seen.slice(0, opener + 1).reverse()
  return {
    records: turn.filter((r) => r && r.isSidechain !== true),
    text,
    skipped: turn.filter((r) => r === null).length,
  }
}

/**
 * One harness run's agents from `<sessionDir>/subagents/workflows/<runId>/journal.jsonl`:
 * `{ started, ended }` agent ids, or `{ error }`. The path is built from a shape-checked run id only,
 * never from the result's own `transcriptDir`, so nothing outside the session directory is read.
 */
function readJournalAgents(sessionDir, runId) {
  if (typeof runId !== 'string' || !RUN_ID_RE.test(runId)) {
    return { error: `the Workflow run id ${JSON.stringify(String(runId).slice(0, 80))} fails ${RUN_ID_RE} and names no journal` }
  }
  const file = path.join(sessionDir, 'subagents', WORKFLOW_RUNS_DIR, runId, 'journal.jsonl')
  let text
  try { text = fs.readFileSync(file, 'utf8') } catch (e) { return { error: `the journal ${file} is unreadable (${(e && e.code) || e})` } }
  const started = []
  const ended = []
  for (const line of text.split(/\r?\n/)) {
    let e
    try { e = JSON.parse(line) } catch { continue }
    if (!e || typeof e.agentId !== 'string' || !e.agentId) continue
    if (e.type === 'started') started.push(e.agentId)
    else if (e.type === 'result' || e.type === 'failed') ended.push(e.agentId)
  }
  return { started, ended }
}

/**
 * `{ required, witnesses }`: the `{ head, agentId, why, via }` lines the turn owes, each pair once
 * however many routes reach it, a repeated pair keeping its first `via`. A call's result is this
 * turn's; a delivered notification's call may sit in an earlier turn, so its result is found by the
 * one raw transcript line carrying both its tool-use id and `toolUseResult`. A notification naming any
 * other tool requires nothing. `via` is the `handoff.py agents` selector (TOOL-dPavedRoad-2 S1):
 * `{ run }` for a harness run, `{ handoff }` for an Agent prompt's one `gov:handoff` marker path, or
 * null.
 */
function extractTurnAgents(turn, transcriptText, sessionDir) {
  const required = []
  const witnesses = []
  const keys = new Set()
  const addRequired = (head, agentId, why, via) => {
    if (typeof agentId !== 'string' || !agentId || keys.has(head + ' ' + agentId)) return
    keys.add(head + ' ' + agentId)
    required.push({ head, agentId, why, via: via || null })
  }
  const addRun = (runId, withReturned, why) => {
    const j = readJournalAgents(sessionDir, runId)
    if (j.error) { witnesses.push(`format-guard: ${j.error}, so that run's agents are not required`); return }
    for (const id of j.started) addRequired('agent', id, why, { run: runId })
    if (withReturned) for (const id of j.ended) addRequired('returned', id, 'received', { run: runId })
  }
  // The prompt is the call's own input when this turn holds the call, else the result's. The marker
  // path reaches a child process as an argument, so it is denied by default: an absolute or
  // drive-qualified path, one holding a `..` segment on either slash, or one opening `-` gives null.
  // agent-cap.js is required only when a prompt names the marker, so a turn with none parses nothing new.
  const readHandoffVia = (toolUseId, r) => {
    const input = calls.has(toolUseId) ? calls.get(toolUseId).input : null
    const prompt = input && typeof input === 'object' && typeof input.prompt === 'string' ? input.prompt : r.prompt
    if (typeof prompt !== 'string' || !prompt.includes('gov:handoff')) return null
    // A missing module or export reads as no selector, never a throw: a throw here would allow the stop.
    let marks
    try { marks = require('./agent-cap.js').extractHandoffMarker(prompt) } catch { return null }
    if (!Array.isArray(marks) || marks.length !== 1) return null
    const p = marks[0].path
    if (path.win32.isAbsolute(p) || path.posix.isAbsolute(p) || /^[A-Za-z]:/.test(p) || p.startsWith('-') ||
        p.split(/[\\/]/).includes('..')) return null
    return { handoff: p }
  }
  const calls = new Map()
  const results = new Map()
  const notified = []
  for (const rec of turn) {
    const content = rec.message && Array.isArray(rec.message.content) ? rec.message.content : []
    if (rec.type === 'assistant') {
      for (const b of content) if (b && b.type === 'tool_use' && (b.name === 'Agent' || b.name === 'Workflow')) calls.set(b.id, { name: b.name, input: b.input })
    } else if (rec.type === 'user' && rec.toolUseResult && typeof rec.toolUseResult === 'object') {
      for (const b of content) if (b && b.type === 'tool_result') results.set(b.tool_use_id, rec.toolUseResult)
    }
    let note = ''
    if (rec.type === 'user' && rec.origin && rec.origin.kind === 'task-notification') {
      note = JSON.stringify(rec.message ? rec.message.content : '')
    } else if (rec.type === 'attachment' && rec.attachment && rec.attachment.type === 'queued_command' && typeof rec.attachment.prompt === 'string') {
      note = rec.attachment.prompt.includes('<task-notification>') ? rec.attachment.prompt : ''
    }
    // The HEADER's id alone (TOOL-aOrientedCast-24 S1): the first tag before the first `<result>`, so an
    // id the agent quotes in its result names nothing. A second notification block in one record is lost.
    const m = /<tool-use-id>([^<]+)<\/tool-use-id>/.exec(String(note || '').split('<result>')[0])
    if (m) notified.push(m[1].trim())
  }
  let lines = null
  const readResult = (toolUseId) => {
    if (results.has(toolUseId)) return results.get(toolUseId)
    if (lines === null) lines = String(transcriptText || '').split(/\r?\n/)
    for (const line of lines) {
      if (!line.includes(toolUseId) || !line.includes('"toolUseResult"')) continue
      let rec
      try { rec = JSON.parse(line) } catch { continue }
      const content = rec && rec.message && Array.isArray(rec.message.content) ? rec.message.content : []
      if (rec.toolUseResult && typeof rec.toolUseResult === 'object' &&
          content.some((b) => b && b.type === 'tool_result' && b.tool_use_id === toolUseId)) return rec.toolUseResult
    }
    return null
  }
  for (const [id, { name }] of calls) {
    const r = results.get(id)
    if (!r) continue
    if (name === 'Agent' && typeof r.agentId === 'string') {
      const via = readHandoffVia(id, r)
      addRequired('agent', r.agentId, 'dispatched', via)
      if (r.status === 'completed') addRequired('returned', r.agentId, 'received', via)
    } else if (name === 'Workflow' && r.runId != null) {
      addRun(r.runId, r.status !== 'async_launched', 'dispatched')
    }
  }
  for (const id of notified) {
    const r = readResult(id)
    if (!r) continue
    // A Workflow result carries `runId`, an Agent result `agentId`; any other tool's carries neither.
    if (r.runId != null) addRun(r.runId, true, 'received')
    else if (typeof r.agentId === 'string') addRequired('returned', r.agentId, 'received', readHandoffVia(id, r))
  }
  return { required, witnesses }
}

/** Whether a line's text after its last ` · ` ends `/<agentId>`, the agent line's own id field. */
function checkCarries(text, agentId) {
  const t = String(text).trimEnd()
  const i = t.lastIndexOf(' · ')
  return (i < 0 ? t : t.slice(i + 3)).endsWith('/' + agentId)
}

/**
 * `{ defects, unmet }`: one defect per required `{ head, agentId, why }` no row meets, and the entries
 * that produced them. A row meets one when it is not fenced, starts `- <head> — `, matches that head's
 * derived shape, and carries the agent id (checkCarries).
 */
function checkAgentLines(rows, shapes, required) {
  const defects = []
  const unmet = []
  for (const q of required) {
    const { head, agentId, why } = q
    const bare = rows.filter((r) => !r.fenced && r.text.startsWith(`- ${head} — `) && checkCarries(r.text, agentId))
    if (bare.some((r) => shapes[head].re.test(r.text))) continue
    unmet.push(q)
    if (bare.length) {
      defects.push(`the ${head} line for agent ${agentId} does not match its charter shape \`${shapes[head].def}\``)
      continue
    }
    // ponytail: a substring test, so `/a1` also hits `/a10`; it picks only the wording, and agent ids are 17 hex.
    const loose = rows.some((r) => r.text.includes(`${head} — `) && r.text.includes('/' + agentId))
    defects.push(loose
      ? `the ${head} line for agent ${agentId} is not a bare list item at column 0 (rule r1)`
      : `no ${head} line for agent ${agentId}, which this turn ${why}`)
  }
  return { defects, unmet }
}

/**
 * `{ lines }`, every stdout line opening `- `, from `<launcher> -B <script> agents <selector> --session
 * <transcriptPath>` run with no shell at the toplevel, `CLAUDE_CODE_SESSION_ID` set to `sid`; or
 * `{ error }`. Never `--write`; `-B` writes no bytecode, so the spawn writes nothing. The launcher is
 * GOV_PYTHON, then PYTHON_LAUNCHERS: a spawn failing ENOENT or exiting 9009, the Microsoft Store
 * stub's exit, is passed over, and any other outcome ends the search. Each spawn gets what remains of
 * `deadline`.
 */
function readHandoffLines({ script, top, sid, transcriptPath, selector, deadline }) {
  const name = path.basename(script)
  const pick = selector.run != null ? ['--run', String(selector.run)] : ['--handoff', String(selector.handoff)]
  const args = ['-B', script, 'agents', ...pick, '--session', String(transcriptPath)]
  const env = Object.assign({}, process.env, { CLAUDE_CODE_SESSION_ID: String(sid) })
  const launchers = [process.env.GOV_PYTHON, ...PYTHON_LAUNCHERS].filter((c) => typeof c === 'string' && c)
  for (const exe of launchers) {
    const timeout = deadline - Date.now()
    if (timeout <= 0) return { error: `the ${HANDOFF_BOUND_MS} ms bound was spent before ${name} agents ${pick.join(' ')} ran` }
    const r = spawnSync(exe, args, { cwd: top, env, timeout, windowsHide: true, shell: false })
    if ((r.error && r.error.code === 'ENOENT') || r.status === 9009) continue
    if (r.error) return { error: `${name} agents ${pick.join(' ')} did not finish under ${exe} (${r.error.code || r.error.message})` }
    if (r.status !== 0) {
      const first = String(r.stderr || '').split(/\r?\n/).find((l) => l.trim()) || 'no stderr'
      return { error: `${name} agents ${pick.join(' ')} exited ${r.status === null ? 'on ' + r.signal : r.status}: ${first.trim()}` }
    }
    return { lines: Buffer.from(r.stdout || '').toString('utf8').split(/\r?\n/).filter((l) => l.startsWith('- ')) }
  }
  return { error: `no python launcher ran ${name}: tried ${launchers.join(', ')}` }
}

/**
 * `{ owed, witnesses }` for a blocking stop: a `committed` line per unmet commit, then per unmet agent
 * entry, in `required` order, the first line `handoff.py agents` prints for its selector that opens
 * `- <head> — `, carries the agent id and matches the head's shape. One run per distinct selector, all
 * inside HANDOFF_BOUND_MS. An entry or commit with no such line adds a witness and no line, so its
 * defect keeps the verb's sentence. The roles kit is found by agent-cap.js's resolveKitDir, required
 * only when some entry has a selector.
 */
function deriveOwedLines({ agents, commits, branch, shapes, top, sid, transcriptPath }) {
  const owed = []
  const witnesses = []
  for (const c of commits) {
    const line = renderShapeLine(shapes.committed.def, { sha: c.sha.slice(0, 9), branch, subject: c.subject })
    if (line && shapes.committed.re.test(line)) owed.push(line)
    else witnesses.push(`format-guard: no committed line is derived for commit ${c.sha.slice(0, 9)}: the charter's committed shape renders off itself or names a field the hook does not derive`)
  }
  const deadline = Date.now() + HANDOFF_BOUND_MS
  let found = { error: '' }
  if (agents.some((q) => q.via)) {
    try {
      found = { script: path.join(require('./agent-cap.js').resolveKitDir('roles', 'handoff.py', __dirname), 'handoff.py') }
    } catch (e) {
      found = { error: (e && e.message) || String(e) }
    }
  }
  const read = new Map()
  for (const q of agents) {
    let why
    if (!q.via) {
      why = 'no Workflow run id or single gov:handoff marker path names its selector'
    } else if (!found.script) {
      why = `handoff.py was not found: ${found.error}`
    } else {
      const key = q.via.run != null ? 'run ' + q.via.run : 'handoff ' + q.via.handoff
      if (!read.has(key)) read.set(key, readHandoffLines({ script: found.script, top, sid, transcriptPath, selector: q.via, deadline }))
      const got = read.get(key)
      if (got.error) {
        why = got.error
      } else {
        const carrying = got.lines.filter((l) => l.startsWith(`- ${q.head} — `) && checkCarries(l, q.agentId))
        const line = carrying.find((l) => shapes[q.head].re.test(l))
        if (line) { owed.push(line); continue }
        why = carrying.length ? `the line handoff.py agents printed is off its charter shape` : `handoff.py agents printed no ${q.head} line for it`
      }
    }
    witnesses.push(`format-guard: no ${q.head} line is derived for agent ${q.agentId}: ${why}`)
  }
  return { owed, witnesses }
}

/**
 * The block reason. `withAgents` counts the agent defects: any shows the agent definitions, and the
 * `handoff.py agents` sentence stays while `owed` derives fewer agent lines than that count. `owed`,
 * committed lines first, is printed after the definitions, one line each, ready to paste.
 */
function renderBlockReason(slug, defects, shapes, withAgents, owed = []) {
  const derived = owed.filter((l) => AGENT_HEADS.some((h) => l.startsWith(`- ${h} — `))).length
  return [
    `format-guard: this session routes build ${slug}, which LIVE.md lists as not yet terminal, and this final message breaks the charter's micro-format rules:`,
    ...defects.map((d) => `- ${d}`),
    '',
    `The definitions, from the ${FENCE_OPEN} fence of ${CHARTER_FILE}:`,
    ...['BUILD', 'SPEC', 'committed'].concat(withAgents ? AGENT_HEADS : []).map((h) => `- \`${shapes[h].def}\``),
    ...(owed.length ? ['', 'The lines this message owes, derived for it — paste each unchanged as a bare `- ` list item at column 0:', ...owed] : []),
    '',
    'Re-send the final message so it ends with its state block: one bare `- committed — …` or `- merged — …` line per new commit, then the BUILD line with the SPEC line directly under it, each a bare `- ` list item at column 0, outside any fence.' +
      (withAgents > derived ? ' For each agent, paste unchanged the lines `handoff.py agents --handoff <path>` or `handoff.py agents --run <run-id>` prints.' : '') +
      ' This hook refuses once per turn end.',
  ].join('\n')
}

/** `{ block, witness }` for one Stop payload; both empty means allow silently. */
function checkStop(data) {
  if (!data || data.hook_event_name !== 'Stop' || data.agent_id) return {}
  if (data.stop_hook_active === true) return {}
  const cwd = typeof data.cwd === 'string' && data.cwd ? data.cwd : ''
  const sid = data.session_id ? String(data.session_id) : ''
  if (!cwd || !sid) return {}
  const hit = resolveToplevel(cwd)
  if (!hit) return {}
  const common = resolveCommonDir(hit)
  if (!common) return {}
  const card = readCard(common, sid)
  if (card.text === null) return {}
  const route = extractRouteUnits(card.text)
  if (!route.build) return {}
  const live = readLiveSlugs(hit.toplevel)
  if (!live || !live.has(route.build)) return {}
  const { shapes, error } = readCharterShapes(hit.toplevel)
  if (!shapes) return { witness: `format-guard: armed for build ${route.build} but not checking — ${error}` }
  if (typeof data.last_assistant_message !== 'string') {
    return { witness: `format-guard: armed for build ${route.build} but not checking — the payload carries no last_assistant_message` }
  }
  const rows = scanMessageLines(data.last_assistant_message)
  const defects = checkPair(rows, shapes, route.units.some((u) => u.spec))
  // One line per degraded outcome: two can happen in one stop, and a scalar would keep only the last.
  const witnesses = []
  // The agent arm (TOOL-aOrientedCast-21): each agent the turn dispatched or received owes its line.
  let agentGot = { defects: [], unmet: [] }
  const tp = data.transcript_path
  if (typeof tp !== 'string' || !tp) {
    witnesses.push('format-guard: the payload carries no transcript_path, so no agent line is required')
  } else {
    const scan = scanTurnRecords(tp)
    if (scan.error) {
      witnesses.push(`format-guard: the transcript ${tp} is unreadable (${scan.error}), so no agent line is required`)
    } else {
      if (scan.skipped) witnesses.push(`format-guard: ${scan.skipped} line(s) of this turn in ${tp} did not parse and were skipped`)
      const got = extractTurnAgents(scan.records, scan.text, tp.replace(/\.jsonl$/i, ''))
      witnesses.push(...got.witnesses)
      const missing = AGENT_HEADS.filter((h) => !shapes[h])
      if (got.required.length && missing.length) {
        const n = new Set(got.required.map((q) => q.agentId)).size
        witnesses.push(`format-guard: this turn dispatched or received ${n} agent(s), and ${CHARTER_FILE}'s micro-format fence defines no ${missing.join(' or ')} shape, so no agent line is required`)
      } else {
        agentGot = checkAgentLines(rows, shapes, got.required)
      }
    }
  }
  defects.push(...agentGot.defects)
  let unmetCommits = []
  const gitDir = resolveGitDir(hit)
  const head = gitDir ? readHeadSha(gitDir, common) : ''
  if (!head) {
    witnesses.push(`format-guard: HEAD is unreadable under ${gitDir || hit.gitPath}, so no commit is required to be named`)
  } else {
    // readCard already refused a non-id-shaped session id, so this join is safe.
    const sidecar = path.join(gitDir, SIDECAR_DIR, sid + '.head')
    let prev = ''
    try { prev = fs.readFileSync(sidecar, 'utf8').trim() } catch { /* first armed stop */ }
    if (prev && prev !== head) {
      const commits = extractNewCommits(hit.toplevel, prev, head)
      if (commits) {
        const c = checkCommitLines(rows, shapes, commits)
        defects.push(...c.defects)
        unmetCommits = c.unmet
      } else witnesses.push(`format-guard: HEAD moved from ${prev.slice(0, 9)} to ${head.slice(0, 9)} along no first-parent path, or git could not answer, so no commit is required to be named`)
    }
    try {
      fs.mkdirSync(path.dirname(sidecar), { recursive: true })
      fs.writeFileSync(sidecar, head + '\n')
    } catch (e) {
      witnesses.push(`format-guard: the HEAD sidecar ${sidecar} is unwritable (${(e && e.code) || e}), so the next stop cannot name new commits`)
    }
  }
  if (!defects.length) return { witness: witnesses.join('\n') }
  // TOOL-dPavedRoad-2: only a stop that already blocks derives the lines it asks for, and a throw in
  // the derivation keeps the block with one witness rather than reaching main's allow.
  let derived
  try {
    derived = deriveOwedLines({
      agents: agentGot.unmet, commits: unmetCommits, branch: unmetCommits.length ? readHeadBranch(gitDir) : 'HEAD',
      shapes, top: hit.toplevel, sid, transcriptPath: tp,
    })
  } catch (e) {
    derived = { owed: [], witnesses: [`format-guard: deriving the owed lines threw (${(e && e.message) || e}), so none is printed`] }
  }
  witnesses.push(...derived.witnesses)
  return { block: renderBlockReason(route.build, defects, shapes, agentGot.defects.length, derived.owed), witness: witnesses.join('\n') }
}

function main() {
  let data
  try { data = JSON.parse(readStdin()) } catch { return }
  const out = checkStop(data)
  if (out.witness) process.stderr.write(out.witness + '\n')
  if (out.block) process.stdout.write(JSON.stringify({ decision: 'block', reason: out.block }))
}

if (require.main === module) {
  try { main() } catch (e) { process.stderr.write(`format-guard: allowed on an internal error — ${(e && e.message) || e}\n`) }
  process.exitCode = 0
}
module.exports = {
  buildShapeRegex, readCharterShapes, scanMessageLines, checkPair, checkCommitLines, checkStop, readLiveSlugs, readHeadSha,
  scanTurnRecords, extractTurnAgents, readJournalAgents, checkAgentLines, renderBlockReason,
  readHandoffLines, deriveOwedLines, renderShapeLine, readHeadBranch, extractNewCommits,
}
