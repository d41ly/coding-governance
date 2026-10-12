#!/usr/bin/env node
/**
 * format-guard — a `Stop` hook that refuses the turn end of a session routed to a live build when the
 * final message lacks the charter's BUILD/SPEC pair, breaks rule r1, or leaves a new commit unreported.
 *
 * gov:kit agent-cap@1.34 — ships inside the hooks kit entry; the kit version is agent-cap.js's.
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
 *     no bare `committed` or `merged` line whose sha field is a 7+ hex prefix of it.
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
 * a chained message already reported it. Whether this hook is WIRED: check-wiring.sh and check-hook-destinations.sh own that. A
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

function renderBlockReason(slug, defects, shapes) {
  return [
    `format-guard: this session routes build ${slug}, which LIVE.md lists as not yet terminal, and this final message breaks the charter's micro-format rules:`,
    ...defects.map((d) => `- ${d}`),
    '',
    `The definitions, from the ${FENCE_OPEN} fence of ${CHARTER_FILE}:`,
    ...['BUILD', 'SPEC', 'committed'].map((h) => `- \`${shapes[h].def}\``),
    '',
    'Re-send the final message so it ends with its state block: one bare `- committed — …` or `- merged — …` line per new commit, then the BUILD line with the SPEC line directly under it, each a bare `- ` list item at column 0, outside any fence. This hook refuses once per turn end.',
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
  return defects.length ? { block: renderBlockReason(route.build, defects, shapes), witness } : { witness }
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
module.exports = { buildShapeRegex, readCharterShapes, scanMessageLines, checkPair, checkCommitLines, checkStop, readLiveSlugs, readHeadSha }
