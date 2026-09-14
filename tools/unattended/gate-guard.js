#!/usr/bin/env node
/**
 * gate-guard — a PreToolUse guard that refuses the flagged merge bar and every self-test suite
 * while the unattended run on the current branch is in a phase before VERIFYING.
 *
 * gov:kit unattended@1.21 — a courtesy marker; the kit version gate pairs the four named `.sh`
 * carriers and every `*.template.md`, and does not read this one.
 *
 * Contract: the spec for TOOL-aDeferredBar-3 under the build folder of that slug.
 *
 * WHY THIS IS A HOOK AND NOT A RULE. The rule already exists in five carriers a build agent reads
 * (TOOL-aDeferredBar-1) and the memory gate refuses a spec that names the bar as an observation
 * (TOOL-aDeferredBar-2). Neither reaches the act: an agent inside a `Workflow` sidechain holds the
 * instruction and still types `GATE_SELFTESTS=1 bash <prefix>/run-gates/run-gates.sh` into a unit
 * pass, and the run stalls for the hours the close will spend again. The tool call is the only
 * surface that sees the act, and a `Bash|PowerShell` PreToolUse hook fires inside a sidechain
 * (`TOOL-cRefutedPremise-1`). Close to half of the corpus runs come from there.
 *
 * WHAT IT DENIES, at COMMAND POSITION in a string-blanked view of the command:
 *   D1  `GATE_FULL=<value>` or `GATE_SELFTESTS=<value>` with a NON-EMPTY value, bare or after
 *       `export`; the empty assignment is the OFF spelling the runner's own `-n` test reads, so it
 *       is the plain bar and is not a hit.
 *   D2  a word ending `run-selftests.sh`           — every declared self-test
 *   D3  a word ending `run-unattended-gates.sh`    — this kit's own suites
 *   D4  a word ending `.test.sh`                   — any one suite, other kits' included
 *   D5  the quoted body of `bash -c` / `sh -c`, scanned once as a command of its own
 * A D2, D3 or D4 token is NOT a hit when the same simple command carries one of READ_ONLY_VERBS:
 * those forms answer in seconds and one of them is how the memory-tree kit re-renders its guides.
 *
 * WHAT IT NEVER DENIES. The plain bar — `run-gates.sh` with neither flag — is the scoped form the
 * owner allows at the main loop, and this hook cannot tell a child from the main loop; the child
 * prompt forbids it there by instruction. A quoted MENTION of any of the shapes — a commit
 * message, a `grep` argument, a heredoc body — is invisible by construction of the view.
 *
 * THE KEY. The predicate runs first, and the filesystem is read only on a hit: the overwhelming
 * majority of tool calls carry no deny shape and cost one scan of one string. On a hit the hook
 * walks up from the payload's `cwd` to `.git`, reads the PER-WORKTREE `HEAD` (never the common
 * dir's, whose HEAD is the primary tree's branch), reads `MEMORY_ROOT` from `.unattended.conf`,
 * and reads every `<MEMORY_ROOT>/builds/<slug>/RUN.md` whose `run-branch:` — else `branch-ref:`,
 * for a record written before that fact existed — equals the ref `HEAD` names. Two stale BUILDING
 * records on branches nobody has checked out for days must key nothing, which is why the key is
 * the branch and never the existence of a record. A matched record in a phase outside
 * PHASES_ALLOW denies, naming that record.
 *
 * NO PATH OUTSIDE THIS FILE IS SPELLED. The conf key, the conf basename and the record basename
 * are the only names; the kit dir, the memory root and the record path are derived from the walk.
 * The four allowed phase names are restated here deliberately (spec §8 F5): reading them from the
 * driver at run time would switch this hook off silently the day the driver could not be read,
 * because the hook fails open; four literals pinned by a direct read and a suite arm fail loudly.
 *
 * ponytail: the predicate is TEXTUAL, the same ceiling scratch-guard.js states of itself. A path
 * assembled at run time (`s=<dir>; bash $s/x.test.sh`) and a python heredoc that spawns a suite
 * both walk past it. No call in the corpus has either shape; the upgrade path is a tokenizer.
 * ponytail: READ_ONLY_VERBS is textual and generic — a suite that ignores an unparsed `--check`
 * would run whole behind it. No call in the corpus has that shape either.
 *
 * FAILS OPEN. Unparseable stdin, an unknown tool, a missing command, no `.git`, a detached HEAD,
 * no conf, no record on this branch: every one exits 0. This is a hygiene rule, not a containment
 * boundary; a security control would have to fail the other way.
 *
 * Protocol: deny = stderr text + exit 2. Allow = print nothing, exit 0. Matches the sibling hooks.
 */
'use strict'

const fs = require('fs')
const path = require('path')

const KIT_GATE_GUARD_VERSION = '1.0'

const TOOLS = ['Bash', 'PowerShell']
// The TAIL of PHASES_CORE in unattended.sh from VERIFYING onward. Pinned to the driver by a direct
// read (spec AC6) and by the parity arm in gate-guard.test.sh; every other phase denies, a
// project's PHASES_EXTRA members included, because an extra phase is by construction before landing.
const PHASES_ALLOW = ['VERIFYING', 'LANDING', 'LANDED', 'ABORTED']
// Measured on node a, 2026-09-13, each direct: --list 5 s · --check 17 s · --rank 3 s · --help 3 s ·
// --render 1 s. Generic over rows D2 to D4 and never over D1.
const READ_ONLY_VERBS = ['--list', '--check', '--rank', '--help', '--render']
const CONF_BASENAME = '.unattended.conf'
const CONF_KEY = 'MEMORY_ROOT'
const RECORD_BASENAME = 'RUN.md'
const MAX_NEST = 1

function readStdin() {
  try {
    return fs.readFileSync(0, 'utf8')
  } catch {
    return ''
  }
}

/**
 * Blank the CONTENTS of quoted strings and heredoc bodies, preserving length so offsets still line
 * up with the original. Copied from scratch-guard.js rather than required from it: a `require` of
 * a sibling kit's file is a literal the install-prefix ban refuses, and an adopter may not hold
 * that kit at all.
 */
function buildCommandView(cmd) {
  const buildBlankedRun = (s, from, to) =>
    to <= from ? s : s.slice(0, from) + ' '.repeat(to - from) + s.slice(to)
  let view = cmd

  const here = /<<-?\s*(['"]?)([A-Za-z_][A-Za-z0-9_]*)\1/g
  let hm
  while ((hm = here.exec(view)) !== null) {
    const tag = hm[2]
    const bodyStart = view.indexOf('\n', hm.index)
    if (bodyStart === -1) break
    const end = view.slice(bodyStart).search(new RegExp('\\n[ \\t]*' + tag + '[ \\t]*(?:\\n|$)'))
    const bodyEnd = end === -1 ? view.length : bodyStart + end
    view = buildBlankedRun(view, bodyStart + 1, bodyEnd)
    here.lastIndex = bodyEnd
  }

  let out = ''
  let i = 0
  while (i < view.length) {
    const ch = view[i]
    if (ch === "'" || ch === '"') {
      let j = i + 1
      while (j < view.length && view[j] !== ch) {
        if (ch === '"' && view[j] === '\\') j++
        j++
      }
      const close = j < view.length ? j : view.length
      out += ch + ' '.repeat(Math.max(0, close - i - 1)) + (j < view.length ? ch : '')
      i = close + 1
    } else {
      out += ch
      i++
    }
  }
  return out
}

/** Read the whitespace-delimited token starting at `from` in the ORIGINAL text, unquoted. */
function readTokenAt(cmd, from, stop) {
  let i = from
  while (i < stop && /\s/.test(cmd[i])) i++
  let out = ''
  let quote = ''
  while (i < stop) {
    const ch = cmd[i]
    if (quote) {
      if (ch === quote) quote = ''
      else out += ch
    } else if (ch === "'" || ch === '"') {
      quote = ch
    } else if (/[\s;|&(){}`]/.test(ch)) {
      break
    } else {
      out += ch
    }
    i++
  }
  return { text: out, end: i }
}

/**
 * Every simple command's tokens, read from the ORIGINAL at the segment boundaries the VIEW locates.
 *
 * Separators are read in the view, where every quoted character is blank, so a `;` inside a commit
 * message is not one. Tokens are read from the original, so a quoted path still resolves. A segment
 * whose view is all blank while its text is not can only be a heredoc body — a quoted string keeps
 * its quote marks — and is skipped whole; without that the body of `python - <<EOF` would be read
 * as commands, which is exactly what the view exists to prevent.
 */
function scanSegments(cmd, view) {
  const out = []
  let s = 0
  const readSegment = (e) => {
    if (e <= s) return
    if (/\S/.test(cmd.slice(s, e)) && !/\S/.test(view.slice(s, e))) return
    const toks = []
    let at = s
    while (at < e) {
      const t = readTokenAt(cmd, at, e)
      if (t.end <= at) break
      if (t.text !== '' || /["']/.test(cmd.slice(at, t.end))) toks.push(t.text)
      at = t.end
    }
    // `then`, `do` and `else` open a command position; drop them so the word after is the head.
    while (toks.length && /^(then|do|else)$/.test(toks[0])) toks.shift()
    if (toks.length) out.push(toks)
  }
  for (let i = 0; i < view.length; i++) {
    if (/[;|&(){}`\n]/.test(view[i])) {
      readSegment(i)
      s = i + 1
    }
  }
  readSegment(view.length)
  return out
}

const FLAG_RE = /^(GATE_FULL|GATE_SELFTESTS)=(.*)$/
const ASSIGN_RE = /^[A-Za-z_][A-Za-z0-9_]*=/
const DURATION_RE = /^\d+[smhd]?$/
const SHORT_OPT_RE = /^-[A-Za-z]+$/

function resolveFileRow(tok) {
  if (/run-selftests\.sh$/.test(tok)) return { row: 'D2', what: 'runner', shape: 'the self-test runner' }
  if (/run-unattended-gates\.sh$/.test(tok)) return { row: 'D3', what: 'runner', shape: 'the self-test runner' }
  if (/\.test\.sh$/.test(tok)) return { row: 'D4', what: 'suite', shape: 'a self-test suite' }
  return null
}

/**
 * Rows D1 to D5 over every simple command. Command position is the head word after any of `env`,
 * `export`, `time`, `nohup`, `NAME=value` words, `timeout N`, and `bash`/`sh` with one short option;
 * row D5 re-enters once on the argument of `-c`. `{`, `time` and `nohup` were added by the corpus
 * measurement (spec rev-4): 38 runs sat among the near-misses of the grammar without them.
 */
function scanDenyHits(cmd, view, depth) {
  depth = depth || 0
  const hits = []
  for (const toks of scanSegments(cmd, view)) {
    const readOnly = toks.some((t) => READ_ONLY_VERBS.includes(t))
    let k = 0
    let head = null
    while (k < toks.length) {
      const t = toks[k]
      const flag = FLAG_RE.exec(t)
      if (flag && flag[2] !== '') {
        hits.push({ row: 'D1', what: 'flag', shape: 'the flagged merge bar', token: t })
        k++
      } else if (t === 'env' || t === 'export' || t === 'time' || t === 'nohup' || ASSIGN_RE.test(t)) {
        k++
      } else if (t === 'timeout' && k + 1 < toks.length && DURATION_RE.test(toks[k + 1])) {
        k += 2
      } else if (t === 'bash' || t === 'sh') {
        k++
        if (k < toks.length && SHORT_OPT_RE.test(toks[k])) {
          const opt = toks[k]
          k++
          // `bash -n <file>` parses and executes nothing — the syntax check every suite author
          // types, 412 times in the corpus. Spec rev-5, after the wired hook denied this build's own.
          if (opt === '-n') { head = null; break }
          if (opt === '-c' && depth < MAX_NEST && k < toks.length) {
            const body = toks[k]
            for (const h of scanDenyHits(body, buildCommandView(body), depth + 1)) {
              hits.push(Object.assign({}, h, { row: 'D5' }))
            }
            head = null
            k = toks.length
            break
          }
        }
      } else {
        head = t
        break
      }
    }
    if (head === null) continue
    const cls = resolveFileRow(head)
    if (cls && !readOnly) hits.push(Object.assign({ token: head }, cls))
  }
  return hits
}

/** `ref: refs/heads/x` → the ref; a bare sha → null, because a detached HEAD keys nothing. */
function readHeadRef(gitDir) {
  let text
  try {
    text = fs.readFileSync(path.join(gitDir, 'HEAD'), 'utf8')
  } catch {
    return null
  }
  const m = /^ref:\s*(\S+)/.exec(text.trim())
  return m ? m[1] : null
}

/**
 * Walk up from `cwd` to the nearest `.git`. A worktree's `.git` is a FILE holding `gitdir: <path>`
 * and THAT directory's HEAD is the worktree's branch — the common dir's HEAD is the primary tree's,
 * which is the one difference from agent-cap's `gitCommonDir`.
 */
function resolveRepoRoot(cwd) {
  let dir = path.resolve(cwd)
  for (let i = 0; i < 64; i++) {
    const g = path.join(dir, '.git')
    let st = null
    try { st = fs.statSync(g) } catch { st = null }
    if (st) {
      let gitDir = g
      if (!st.isDirectory()) {
        let m
        try { m = /gitdir:\s*(.+)/.exec(fs.readFileSync(g, 'utf8')) } catch { return null }
        if (!m) return null
        gitDir = path.resolve(dir, m[1].trim())
      }
      const headRef = readHeadRef(gitDir)
      return headRef ? { root: dir, headRef } : null
    }
    const up = path.dirname(dir)
    if (up === dir) return null
    dir = up
  }
  return null
}

/** `MEMORY_ROOT` from the conf beside `.git`; no conf keys nothing, an absent key means `memory`. */
function readMemoryRoot(root) {
  let text
  try {
    text = fs.readFileSync(path.join(root, CONF_BASENAME), 'utf8')
  } catch {
    return null
  }
  // The driver SOURCES this file; this is a second reader, so every legal shell spelling of the
  // line has to read the same here — a trailing comment or a quoted value must not turn into a
  // path that resolves nowhere and switch the hook off silently.
  let value = 'memory'
  for (const line of text.split(/\r?\n/)) {
    const m = new RegExp('^(?:export\\s+)?' + CONF_KEY + '=(.*)$').exec(line)
    if (m) value = m[1].replace(/\s+#.*$/, '').trim().replace(/^["']|["']$/g, '')
  }
  // A value that could escape the root is not a memory root; fail open rather than read outside it.
  if (!value || path.isAbsolute(value) || value.split(/[\\/]/).includes('..')) return null
  return value
}

/**
 * Every run-state record whose branch fact equals `ref`: `run-branch:` first, `branch-ref:` for a
 * record written before that fact existed. A record with neither, or with no phase, keys nothing.
 */
function resolveRunPhase(root, memoryRoot, ref) {
  const buildsDir = path.join(root, memoryRoot, 'builds')
  let slugs
  try { slugs = fs.readdirSync(buildsDir) } catch { return [] }
  const matched = []
  for (const slug of slugs) {
    let text
    try { text = fs.readFileSync(path.join(buildsDir, slug, RECORD_BASENAME), 'utf8') } catch { continue }
    const readFact = (key) => {
      const m = new RegExp('^' + key + ': (.*)$', 'm').exec(text)
      return m ? m[1].trim() : ''
    }
    const branch = readFact('run-branch') || readFact('branch-ref')
    const phase = readFact('phase')
    if (!branch || !phase || branch !== ref) continue
    matched.push({ slug, phase, record: [memoryRoot, 'builds', slug, RECORD_BASENAME].join('/') })
  }
  return matched
}

/** The whole decision: hits first, the filesystem only on a hit. Null means allow. */
function checkCommand(cmd, cwd) {
  const hits = scanDenyHits(cmd, buildCommandView(cmd), 0)
  if (hits.length === 0) return null
  const repo = resolveRepoRoot(cwd)
  if (!repo) return null
  const memoryRoot = readMemoryRoot(repo.root)
  if (!memoryRoot) return null
  const live = resolveRunPhase(repo.root, memoryRoot, repo.headRef).filter((r) => !PHASES_ALLOW.includes(r.phase))
  if (live.length === 0) return null
  return { hits, live }
}

function renderDeny(hits, live) {
  const shapes = [...new Set(hits.map((h) => h.shape))].join(' and ')
  const where = live.map((r) => `${r.phase} (${r.record})`).join(' and ')
  const lines = hits.map((h) => `  ${h.what}: ${h.token}`).join('\n')
  return (
    `BLOCKED by gate-guard: this command runs ${shapes} while the unattended run on this\n` +
    `branch is at ${where}, which is before ${PHASES_ALLOW[0]}.\n\n` +
    lines +
    '\n\nInside a build pass a unit is observed by the direct check its spec names, in seconds. The\n' +
    `flagged bar and the self-test suites run once, at ${PHASES_ALLOW[0]}, by the main loop. A quoted mention\n` +
    'of the file is not a hit.\n'
  )
}

function main() {
  let data
  try {
    data = JSON.parse(readStdin())
  } catch {
    process.exit(0)
  }
  if (!data || !TOOLS.includes(data.tool_name)) process.exit(0)
  const cmd = (data.tool_input && data.tool_input.command) || ''
  if (!cmd) process.exit(0)
  // Wrapped because a hygiene guard that THROWS is worse than one that misses: an uncaught error
  // exits 1 and surfaces noise on a command that was probably fine. Fail open.
  let verdict
  try {
    verdict = checkCommand(String(cmd), data.cwd || process.cwd())
  } catch {
    process.exit(0)
  }
  if (!verdict) process.exit(0)
  process.stderr.write(renderDeny(verdict.hits, verdict.live))
  process.exit(2)
}

if (require.main === module) main()
module.exports = {
  readStdin, buildCommandView, scanSegments, scanDenyHits, resolveRepoRoot, readHeadRef, readMemoryRoot,
  resolveRunPhase, checkCommand, renderDeny, main,
  PHASES_ALLOW, READ_ONLY_VERBS, TOOLS, KIT_GATE_GUARD_VERSION,
}
