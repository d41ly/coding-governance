/**
 * run-lease — the session-keyed binder every unattended hook shares: the repo walk that returns
 * the per-worktree git dir, the conf-line reader, the lease scan over the run-state records, the
 * sidecar path derivation and the append. Required by `__dirname` from `stop-guard.js` and from
 * `stall-recorder.js`; nothing here reads stdin or exits, and nothing here spells a path outside
 * this directory — the conf basename, the conf keys, the record basename and the sidecar dir name
 * are the only literals.
 *
 * gov:kit unattended@1.32 — a courtesy marker; the kit version gate pairs the four named `.sh`
 * carriers and every `*.template.md`, and does not read this one.
 *
 * Contract: the spec for TOOL-aWokenSentinel-3 under the build folder of that slug, §4 "The key".
 *
 * WHY A SECOND WALK BESIDE gate-guard.js's. That hook's `resolveRepoRoot` keys on the BRANCH: it
 * returns the HEAD ref and refuses a detached HEAD, both right for a guard over the branch a run is
 * on. A `Stop` hook keys on the SESSION, and the git dir is where its sidecar lives, so it needs the
 * dir back and never the ref. Extracting a shared shape would have been a third one (spec §8 F2);
 * the move of gate-guard.js onto this module is a backlog row at landing.
 *
 * THE KEY. A record binds to the session whose `session:` fact under `## Run facts` equals the
 * payload's `session_id`; the literal `absent` and an empty fact bind nothing. A record written
 * before that fact existed — every run preflighted before TOOL-aWokenSentinel-1 landed — is
 * invisible until `--resume --keepalive-id` re-records its lease. That is the dark landing.
 *
 * WHAT THIS DOES NOT CHECK: it does not grade the record's phase, does not ask whether the session
 * is alive, and does not validate the sidecar's lines beyond parsing each as JSON — a torn line is
 * skipped, never a refusal, because a reader that refuses on one bad line makes the whole log
 * unreadable to the hook that has to derive a bound from it.
 */
'use strict'

const fs = require('fs')
const path = require('path')

const CONF_BASENAME = '.unattended.conf'
const MEMORY_ROOT_KEY = 'MEMORY_ROOT'
const MEMORY_ROOT_DEFAULT = 'memory'
const RECORD_BASENAME = 'RUN.md'
const FACTS_HEADING = '## Run facts'
// The directory name under the git dir; the driver's `resolve_sidecar_dir` in lib-unattended.sh
// spells the same one, and the kit gate counts that spelling on exactly one code line there.
const SIDECAR_DIRNAME = 'unattended'

function readStdin() {
  try {
    return fs.readFileSync(0, 'utf8')
  } catch {
    return ''
  }
}

/**
 * Walk up from `cwd` to the nearest `.git` and return `{root, gitDir}`. A linked worktree's `.git`
 * is a FILE holding `gitdir: <path>`, and THAT directory is the per-worktree git dir — where
 * `gate-logs/` already sits — never the common dir, because a run lives in one worktree. No `.git`
 * within 64 levels, or a `.git` file that names nothing: null.
 */
function resolveRepo(cwd) {
  let dir = path.resolve(cwd)
  for (let i = 0; i < 64; i++) {
    const g = path.join(dir, '.git')
    let st = null
    try { st = fs.statSync(g) } catch { st = null }
    if (st) {
      if (st.isDirectory()) return { root: dir, gitDir: g }
      let m
      try { m = /gitdir:\s*(.+)/.exec(fs.readFileSync(g, 'utf8')) } catch { return null }
      if (!m) return null
      return { root: dir, gitDir: path.resolve(dir, m[1].trim()) }
    }
    const up = path.dirname(dir)
    if (up === dir) return null
    dir = up
  }
  return null
}

/**
 * The value of `KEY=` in the conf beside `.git`, read the way gate-guard.js reads MEMORY_ROOT: the
 * driver SOURCES this file, so every legal shell spelling of the line has to read the same here —
 * an `export` prefix admitted, a trailing comment stripped, surrounding quotes stripped, the LAST
 * assignment winning as it does in a shell. No conf, or no such line: null. A declared empty
 * value: the empty string, which is a value and not an absence.
 */
function readConfValue(root, key) {
  let text
  try {
    text = fs.readFileSync(path.join(root, CONF_BASENAME), 'utf8')
  } catch {
    return null
  }
  let value = null
  const re = new RegExp('^(?:export\\s+)?' + key + '=(.*)$')
  for (const line of text.split(/\r?\n/)) {
    const m = re.exec(line)
    if (m) value = m[1].replace(/\s+#.*$/, '').trim().replace(/^["']|["']$/g, '')
  }
  return value
}

/**
 * `MEMORY_ROOT` from the conf, defaulting to `memory` when the key is absent. No conf keys nothing
 * (null): the driver refuses to run without one, so no record with a lease can exist there. A value
 * that could escape the root is not a memory root; fail open rather than read outside it.
 */
function readMemoryRoot(root) {
  const declared = readConfValue(root, MEMORY_ROOT_KEY)
  let exists = false
  try { exists = fs.statSync(path.join(root, CONF_BASENAME)).isFile() } catch { exists = false }
  if (!exists) return null
  const value = declared === null ? MEMORY_ROOT_DEFAULT : declared
  if (!value || path.isAbsolute(value) || value.split(/[\\/]/).includes('..')) return null
  return value
}

/**
 * A positive-integer knob, the driver's `read_bound_key` rule with one divergence: `{value, source}`
 * where `source` is `declared`, `default` (absent or declared empty — the driver's own reading of an
 * empty value) or `malformed` (declared and not a positive integer). The driver EXITS 2 on malformed;
 * this returns it, because for a `Stop` hook exit 2 is a block and a conf typo must never become a
 * session that cannot end its turn (spec §8 F4). The caller decides what `malformed` buys.
 */
function readBoundKey(root, key, fallback) {
  const raw = readConfValue(root, key)
  if (raw === null || raw === '') return { value: fallback, source: 'default', raw }
  if (!/^[0-9]+$/.test(raw) || Number(raw) === 0) return { value: fallback, source: 'malformed', raw }
  return { value: Number(raw), source: 'declared', raw }
}

/**
 * Every run-state record under `<root>/<memoryRoot>/builds/<slug>/RUN.md` that carries a lease: its
 * slug, the `session:` fact, the `phase:` fact and the record's root-relative path. A record with
 * no `session:` fact, or one reading `absent`, is not in the list — it keys nothing. This is the
 * one scan every session on the node pays: a directory listing and one small read per build
 * folder, no spawn.
 */
function scanLeases(root, memoryRoot) {
  const buildsDir = path.join(root, memoryRoot, 'builds')
  let slugs
  try { slugs = fs.readdirSync(buildsDir) } catch { return [] }
  const out = []
  for (const slug of slugs) {
    let text
    try { text = fs.readFileSync(path.join(buildsDir, slug, RECORD_BASENAME), 'utf8') } catch { continue }
    // The `## Run facts` region only: from its heading to the next `## ` heading or the end, so a
    // parked row or a generated block that happens to start a line with `session:` keys nothing.
    let region = ''
    const i = text.indexOf(FACTS_HEADING)
    if (i >= 0) {
      const rest = text.slice(i + FACTS_HEADING.length)
      const j = rest.search(/^## /m)
      region = j < 0 ? rest : rest.slice(0, j)
    }
    const readFact = (key) => {
      const m = new RegExp('^' + key + ':[ \t]*(.*)$', 'm').exec(region)
      return m ? m[1].replace(/\r$/, '').trim() : ''
    }
    const session = readFact('session')
    if (!session || session === 'absent') continue
    out.push({ slug, session, phase: readFact('phase') || 'absent',
               record: [memoryRoot, 'builds', slug, RECORD_BASENAME].join('/') })
  }
  return out
}

/**
 * The leases whose `session:` equals `sessionId`, in directory order. Normally zero or one; the
 * driver writes the fact from one CLAUDE_CODE_SESSION_ID, so two can only come from a hand-edited
 * tree, and then the caller reads them all and names the first (the way gate-guard.js handles two
 * records on one branch). An empty `sessionId` matches nothing.
 */
function resolveLease(root, memoryRoot, sessionId) {
  if (!sessionId) return []
  return scanLeases(root, memoryRoot).filter((l) => l.session === sessionId)
}

/** `<git-dir>/unattended/<kind>.<slug>.log` — `stop` for the stop-guard, `stall` for the recorder. */
function deriveSidecarPath(gitDir, kind, slug) {
  return path.join(gitDir, SIDECAR_DIRNAME, kind + '.' + slug + '.log')
}

/**
 * Append ONE line, creating the directory on first write. Throws when it cannot — a caller that
 * blocks on a bound derived from this file must know the line did not land, so the failure is
 * the caller's decision and never swallowed here.
 */
function writeSidecarLine(file, line) {
  fs.mkdirSync(path.dirname(file), { recursive: true })
  fs.appendFileSync(file, line + '\n', 'utf8')
}

/** Every parseable JSON line of a sidecar, in order; an absent file is an empty list. */
function readSidecarLines(file) {
  let text
  try { text = fs.readFileSync(file, 'utf8') } catch { return [] }
  const out = []
  for (const line of text.split(/\r?\n/)) {
    if (!line.trim()) continue
    try { out.push(JSON.parse(line)) } catch { /* a torn line is skipped, never a refusal */ }
  }
  return out
}

/** `2026-09-16T12:00:05Z` — second precision, the spelling the driver's `--park` writes. */
function renderUtc(date) {
  return (date || new Date()).toISOString().replace(/\.\d{3}Z$/, 'Z')
}

module.exports = {
  readStdin, resolveRepo, readConfValue, readMemoryRoot, readBoundKey, scanLeases, resolveLease, deriveSidecarPath, writeSidecarLine, readSidecarLines, renderUtc,
  CONF_BASENAME, MEMORY_ROOT_KEY, MEMORY_ROOT_DEFAULT, RECORD_BASENAME, SIDECAR_DIRNAME,
}
