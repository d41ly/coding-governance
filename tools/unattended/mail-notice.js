#!/usr/bin/env node
/**
 * mail-notice — a `PostToolUse` hook on every tool that lists a session's build's unread mail from the
 * node's local copy, as `mailbox.notice` says, with no network call on the tool call's path.
 *
 * gov:kit unattended@1.135 — a courtesy marker; the kit version gate pairs the four named `.sh`
 * carriers and every `*.template.md`, and does not read this one.
 *
 * Contract: the spec for KICK-dKeptSession-21 under the dKeptSession build folder, S5 and S6. First
 * written by the hook kind's factory; this body is its author's.
 *
 * WHY POSTTOOLUSE. This hook is registered on every tool, matcher `*` in its fragment and in
 * `.claude/settings.json`, and it is the only carrier of the unread-mail line: the Bash tool and the
 * write tools as much as Read, Grep, Glob and Agent. The hooks kit's scratch-guard carries
 * `additionalContext` on its own `PreToolUse` matcher, and what it carries there is the card pointers
 * (KICK-dKeptSession-13 S7), never mail. This statement is KICK-dKeptSession-79 S8's, and it replaces
 * KICK-dKeptSession-44 S6's wording, which gave the non-Bash tools as the registration's reason.
 *
 * THE BINDING (KICK-dKeptSession-44 S9). The session's build is the route's `- build:` of the tree's
 * card file at CARD_FILE_REL whose `card-owner —` line names the session, read as the hooks kit's
 * `checkItemBoundary` reads it, with one file read and no spawn; else the run lease's slug
 * `resolveLease` finds. CARD_FILE_REL and `extractRouteUnits` are carried inline from that kit's
 * scratch-guard, never required, since a kit imports no sibling kit (TOOL-dGroundRules-1 §4); its
 * `readCard` is not carried, since it spawns a bash to find the card engine.
 *
 * THE STAMP. The driver's `--mail notice <slug>` is the one reader of `mailbox.notice` and
 * `mailbox.fetch-seconds`, and the one writer of `<git-dir>/unattended/mail-notice.<slug>.log`, the
 * path `deriveSidecarPath` derives: its first line `{"notice": …, "fetch-seconds": …, "bash": …}`,
 * then one JSON line per unread row, `{"id": …, "kind": …, "to": …}`, rewritten whole after every
 * notice that fetched. Its mtime is the age of the local copy. This hook reads it with one stat and
 * one read, and reads no policy: the JavaScript policy reader spawns git on every call.
 *
 * PER CALL, in order: the payload; a subagent's call (`agent_id` set), no `session_id`, no repository
 * or neither a card nor a lease binding the session leaves. The stamp absent, or its first line not `every-tool-call`,
 * leaves. A stamp older than its own `fetch-seconds` starts THE DETACHED FETCH: `<stamp>.fetching`
 * created with the exclusive flag, and only by the call that created it, the stamp's `bash` running
 * the driver beside this file as `--mail notice <slug>`, detached, its streams ignored, so the call
 * never waits; the verb clears the marker when its fetch rewrote the stamp, and a failed fetch keeps
 * the marker, touched at its end, so no call spawns again until it is older than twice `fetch-seconds`,
 * when it is replaced (KICK-dKeptSession-79 S3). Then, where the stamp holds a row, ONE `additionalContext` line:
 * `mail — <n> unread for <slug> · <ids> · local copy <age>s old`.
 *
 * WHAT THIS DOES NOT CHECK: that the local copy is current, only its age; the message bodies, never
 * read; a value changed in the policy file, which reaches this hook at the next notice. Every failure
 * path is silence and exit 0.
 */
'use strict'

const fs = require('fs')
const path = require('path')
const { spawn } = require('child_process')
const lease = require(path.join(__dirname, 'run-lease.js'))

const SIDECAR_KIND = 'mail-notice'
const NOTICE_EVERY_CALL = 'every-tool-call'
const SLUG_RE = /^[A-Za-z][A-Za-z0-9-]*$/
const ID_RE = /^[0-9a-f]{12}$/
/** The tree's card file, the hooks kit scratch-guard's CARD_FILE_REL, carried inline (S9). */
// >>> card_file_rel_js -- canonical copy: the hooks kit's scratch-guard.js (byte-identical; gated)
const CARD_FILE_REL = '.claude/orientation-card.md'
// <<< card_file_rel_js

/**
 * The card's `## route` section: `{ seen, build, units, lines }`, carried inline byte for byte from the
 * hooks kit scratch-guard's `extractRouteUnits` (S9), of which this hook reads `build` alone. Its
 * parity is gated between the markers (KICK-dKeptSession-62 S21).
 */
// >>> extract_route_units_js -- canonical copy: the hooks kit's scratch-guard.js (byte-identical; gated)
function extractRouteUnits(text) {
  let inRoute = false
  let build = ''
  let seen = false
  const units = []
  const lines = []
  for (const raw of String(text || '').split(/\r?\n/)) {
    const line = raw.replace(/`/g, '').trim()
    if (line === '## route') { inRoute = true; seen = true; lines.push({ text: raw, unit: null }); continue }
    if (line.startsWith('## ') || line.replace(/^- /, '').startsWith('READY — ')) { inRoute = false; continue }
    if (!inRoute || line === '') continue
    let unit = null
    const b = /^- build:\s*(\S+)\s*$/.exec(line)
    const u = /^- unit:\s*(\S+)(?:\s*·\s*spec\s+(\S+))?\s*$/.exec(line)
    if (b) build = b[1]
    else if (u) units.push(unit = { unit: u[1], spec: u[2] || '' })
    lines.push({ text: raw, unit })
  }
  return { seen, build, units, lines }
}
// <<< extract_route_units_js

/**
 * S9: the build the tree's card file at `<root>/` CARD_FILE_REL binds `sid` to — its route's build where
 * its first `card-owner —` line names `sid`, else ''. One file read, no spawn.
 */
function readCardBuild(root, sid) {
  let text
  try { text = fs.readFileSync(path.join(root, CARD_FILE_REL), 'utf8') } catch { return '' }
  const owner = text.split(/\r?\n/).map((l) => /^card-owner — ([A-Za-z0-9][A-Za-z0-9._-]*)(?: · .*)?$/.exec(l)).find(Boolean)
  if (!owner || owner[1] !== sid) return ''
  return extractRouteUnits(text).build
}

/**
 * The stamp at `file` -> `{head, rows, ageS}` when its first line reads `every-tool-call`, else null:
 * absent, unreadable, a first line that is no head, or any other value. One stat, one read.
 */
function readMailNotice(file) {
  let st
  try { st = fs.statSync(file) } catch { return null }
  const lines = lease.readSidecarLines(file)
  const head = lines[0]
  if (!head || typeof head !== 'object' || head.notice !== NOTICE_EVERY_CALL) return null
  const ageS = Math.max(0, Math.floor((Date.now() - st.mtimeMs) / 1000))
  return { head, rows: lines.slice(1), ageS }
}

/** The stamp's own `fetch-seconds` when it is a positive number, else null: no interval, no fetch. */
function checkFetchDue(head, ageS) {
  const s = Number(head['fetch-seconds'])
  if (!Number.isFinite(s) || s <= 0) return null
  return ageS > s ? s : null
}

/**
 * S6: the marker beside the stamp created exclusively, one older than twice `seconds` removed first,
 * then the stamp's `bash` running `<this directory>/unattended.sh --mail notice <slug>` detached in the
 * repository. A call that did not create the marker spawns nothing.
 */
function runDetachedFetch(file, head, slug, root, seconds) {
  const bash = head.bash
  if (typeof bash !== 'string' || !path.isAbsolute(bash)) return false
  const marker = file + '.fetching'
  try {
    const st = fs.statSync(marker)
    if ((Date.now() - st.mtimeMs) / 1000 <= 2 * seconds) return false
    fs.unlinkSync(marker)
  } catch { /* no marker, or one another call just removed: the exclusive create decides */ }
  try { fs.writeFileSync(marker, '', { flag: 'wx' }) } catch { return false }
  const driver = path.join(__dirname, 'unattended.sh').replace(/\\/g, '/')
  const child = spawn(bash, [driver, '--mail', 'notice', slug], {
    cwd: root, detached: true, stdio: 'ignore', windowsHide: true, env: { ...process.env, GOV_RUNLOG: '0' },
  })
  child.on('error', () => {})
  child.unref()
  return true
}

/** The one line: the rows' ids in the stamp's order, or null where the stamp holds none. */
function renderMailNotice(slug, rows, ageS) {
  const ids = rows.map((r) => r && r.id).filter((id) => typeof id === 'string' && ID_RE.test(id))
  if (!ids.length) return null
  return `mail — ${ids.length} unread for ${slug} · ${ids.join(' ')} · local copy ${ageS}s old`
}

function main() {
  let data
  try { data = JSON.parse(lease.readStdin()) } catch { return }
  if (!data || typeof data !== 'object' || data.agent_id) return
  const sid = typeof data.session_id === 'string' ? data.session_id : ''
  if (!sid) return
  const repo = lease.resolveRepo(typeof data.cwd === 'string' && data.cwd ? data.cwd : process.cwd())
  if (!repo) return
  let slug = readCardBuild(repo.root, sid)
  if (!slug) {
    const memoryRoot = lease.readMemoryRoot(repo.root)
    if (!memoryRoot) return
    const bound = lease.resolveLease(repo.root, memoryRoot, sid)[0]
    slug = bound ? bound.slug : ''
  }
  if (!SLUG_RE.test(slug)) return
  const file = lease.deriveSidecarPath(repo.gitDir, SIDECAR_KIND, slug)
  const stamp = readMailNotice(file)
  if (!stamp) return
  const seconds = checkFetchDue(stamp.head, stamp.ageS)
  if (seconds !== null) runDetachedFetch(file, stamp.head, slug, repo.root, seconds)
  const line = renderMailNotice(slug, stamp.rows, stamp.ageS)
  if (!line) return
  process.stdout.write(JSON.stringify({ hookSpecificOutput: { hookEventName: 'PostToolUse', additionalContext: line } }) + '\n')
}

try { main() } catch { /* a throw is silence: the tool call it follows is never held up */ }
