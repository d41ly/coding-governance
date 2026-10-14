#!/usr/bin/env node
/**
 * format-guard — a `Stop` hook that refuses the turn end of a session routed to a live build when the
 * final message lacks the charter's BUILD/SPEC pair, breaks rule r1, leaves a new commit unreported, or
 * leaves out the `agent` or `returned` line of an agent its turn dispatched or received.
 *
 * gov:kit agent-cap@1.39 — ships inside the hooks kit entry; the kit version is agent-cap.js's.
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
 * transcript format still holds: a renamed field reads as a turn with no agent, silently. Whether this hook is WIRED: check-wiring.sh and check-hook-destinations.sh own that. A
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

/** The first-parent commits in prev..head, or null when prev is not an ancestor or git cannot answer. */
function extractNewCommits(top, prev, head) {
  const r = spawnSync('git', ['rev-list', '--first-parent', '--ancestry-path', `${prev}..${head}`], {
    cwd: top, encoding: 'utf8', timeout: GIT_BOUND_MS, windowsHide: true,
  })
  if (r.status !== 0) return null
  const shas = r.stdout.split(/\r?\n/).filter((l) => /^[0-9a-f]{40}$/.test(l))
  return shas.length ? shas : null
}

/** The commit defects: each new sha that no bare committed or merged line names by a 7+ hex prefix. */
function checkCommitLines(rows, shapes, shas) {
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
  return shas.filter((s) => !checkNamed(s)).map((s) => `commit ${s.slice(0, 9)} is new since this session's previous stop and no bare committed or merged line names it`)
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
 * `{ required, witnesses }`: the `{ head, agentId, why }` lines the turn owes, each pair once however
 * many routes reach it. A call's result is this turn's; a delivered notification's call may sit in an
 * earlier turn, so its result is found by the one raw transcript line carrying both its tool-use id
 * and `toolUseResult`. A notification naming any other tool requires nothing.
 */
function extractTurnAgents(turn, transcriptText, sessionDir) {
  const required = []
  const witnesses = []
  const keys = new Set()
  const addRequired = (head, agentId, why) => {
    if (typeof agentId !== 'string' || !agentId || keys.has(head + ' ' + agentId)) return
    keys.add(head + ' ' + agentId)
    required.push({ head, agentId, why })
  }
  const addRun = (runId, withReturned, why) => {
    const j = readJournalAgents(sessionDir, runId)
    if (j.error) { witnesses.push(`format-guard: ${j.error}, so that run's agents are not required`); return }
    for (const id of j.started) addRequired('agent', id, why)
    if (withReturned) for (const id of j.ended) addRequired('returned', id, 'received')
  }
  const calls = new Map()
  const results = new Map()
  const notified = []
  for (const rec of turn) {
    const content = rec.message && Array.isArray(rec.message.content) ? rec.message.content : []
    if (rec.type === 'assistant') {
      for (const b of content) if (b && b.type === 'tool_use' && (b.name === 'Agent' || b.name === 'Workflow')) calls.set(b.id, b.name)
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
  for (const [id, name] of calls) {
    const r = results.get(id)
    if (!r) continue
    if (name === 'Agent' && typeof r.agentId === 'string') {
      addRequired('agent', r.agentId, 'dispatched')
      if (r.status === 'completed') addRequired('returned', r.agentId, 'received')
    } else if (name === 'Workflow' && r.runId != null) {
      addRun(r.runId, r.status !== 'async_launched', 'dispatched')
    }
  }
  for (const id of notified) {
    const r = readResult(id)
    if (!r) continue
    // A Workflow result carries `runId`, an Agent result `agentId`; any other tool's carries neither.
    if (r.runId != null) addRun(r.runId, true, 'received')
    else if (typeof r.agentId === 'string') addRequired('returned', r.agentId, 'received')
  }
  return { required, witnesses }
}

/**
 * One defect per required `{ head, agentId, why }` no row meets: a row meets it when it is not fenced,
 * starts `- <head> — `, matches that head's derived shape, and its text after its last ` · ` ends
 * `/<agentId>`.
 */
function checkAgentLines(rows, shapes, required) {
  const checkCarries = (text, agentId) => {
    const t = text.trimEnd()
    const i = t.lastIndexOf(' · ')
    return (i < 0 ? t : t.slice(i + 3)).endsWith('/' + agentId)
  }
  const defects = []
  for (const { head, agentId, why } of required) {
    const bare = rows.filter((r) => !r.fenced && r.text.startsWith(`- ${head} — `) && checkCarries(r.text, agentId))
    if (bare.some((r) => shapes[head].re.test(r.text))) continue
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
  return defects
}

function renderBlockReason(slug, defects, shapes, withAgents) {
  return [
    `format-guard: this session routes build ${slug}, which LIVE.md lists as not yet terminal, and this final message breaks the charter's micro-format rules:`,
    ...defects.map((d) => `- ${d}`),
    '',
    `The definitions, from the ${FENCE_OPEN} fence of ${CHARTER_FILE}:`,
    ...['BUILD', 'SPEC', 'committed'].concat(withAgents ? AGENT_HEADS : []).map((h) => `- \`${shapes[h].def}\``),
    '',
    'Re-send the final message so it ends with its state block: one bare `- committed — …` or `- merged — …` line per new commit, then the BUILD line with the SPEC line directly under it, each a bare `- ` list item at column 0, outside any fence.' +
      (withAgents ? ' For each agent, paste unchanged the lines `handoff.py agents --handoff <path>` or `handoff.py agents --run <run-id>` prints.' : '') +
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
  let agentDefects = []
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
        agentDefects = checkAgentLines(rows, shapes, got.required)
      }
    }
  }
  defects.push(...agentDefects)
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
      const shas = extractNewCommits(hit.toplevel, prev, head)
      if (shas) defects.push(...checkCommitLines(rows, shapes, shas))
      else witnesses.push(`format-guard: HEAD moved from ${prev.slice(0, 9)} to ${head.slice(0, 9)} along no first-parent path, or git could not answer, so no commit is required to be named`)
    }
    try {
      fs.mkdirSync(path.dirname(sidecar), { recursive: true })
      fs.writeFileSync(sidecar, head + '\n')
    } catch (e) {
      witnesses.push(`format-guard: the HEAD sidecar ${sidecar} is unwritable (${(e && e.code) || e}), so the next stop cannot name new commits`)
    }
  }
  const witness = witnesses.join('\n')
  return defects.length ? { block: renderBlockReason(route.build, defects, shapes, agentDefects.length > 0), witness } : { witness }
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
module.exports = { buildShapeRegex, readCharterShapes, scanMessageLines, checkPair, checkCommitLines, checkStop, readLiveSlugs, readHeadSha, scanTurnRecords, extractTurnAgents, readJournalAgents, checkAgentLines }
