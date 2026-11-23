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
 * THE STAMP. The driver's `--mail notice <slug>` is the one reader of `mailbox.notice` and
 * `mailbox.fetch-seconds`, and the one writer of `<git-dir>/unattended/mail-notice.<slug>.log`, the
 * path `deriveSidecarPath` derives: its first line `{"notice": …, "fetch-seconds": …, "bash": …}`,
 * then one JSON line per unread row, `{"id": …, "kind": …, "to": …}`, rewritten whole after every
 * notice that fetched. Its mtime is the age of the local copy. This hook reads it with one stat and
 * one read, and reads no policy: the JavaScript policy reader spawns git on every call.
 *
 * PER CALL, in order: the payload; a subagent's call (`agent_id` set), no `session_id`, no repository
 * or no lease binding the session leaves. The stamp absent, or its first line not `every-tool-call`,
 * leaves. A stamp older than its own `fetch-seconds` starts THE DETACHED FETCH: `<stamp>.fetching`
 * created with the exclusive flag, and only by the call that created it, the stamp's `bash` running
 * the driver beside this file as `--mail notice <slug>`, detached, its streams ignored, so the call
 * never waits; the verb clears the marker when it ends, and a marker older than twice
 * `fetch-seconds` is replaced. Then, where the stamp holds a row, ONE `additionalContext` line:
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
  const memoryRoot = lease.readMemoryRoot(repo.root)
  if (!memoryRoot) return
  const bound = lease.resolveLease(repo.root, memoryRoot, sid)[0]
  if (!bound || !SLUG_RE.test(bound.slug)) return
  const file = lease.deriveSidecarPath(repo.gitDir, SIDECAR_KIND, bound.slug)
  const stamp = readMailNotice(file)
  if (!stamp) return
  const seconds = checkFetchDue(stamp.head, stamp.ageS)
  if (seconds !== null) runDetachedFetch(file, stamp.head, bound.slug, repo.root, seconds)
  const line = renderMailNotice(bound.slug, stamp.rows, stamp.ageS)
  if (!line) return
  process.stdout.write(JSON.stringify({ hookSpecificOutput: { hookEventName: 'PostToolUse', additionalContext: line } }) + '\n')
}

try { main() } catch { /* a throw is silence: the tool call it follows is never held up */ }
